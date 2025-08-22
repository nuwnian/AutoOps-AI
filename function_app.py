import azure.functions as func
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HealthCheck")
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    endpoints = {
    "web": "https://autoops-ai.azurewebsites.net/health"
    }
    results = {}
    overall_status = "healthy"

    for name, url in endpoints.items():
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200 and r.text.strip().lower() == "ok":
                results[name] = "healthy"
            else:
                results[name] = "degraded"
                overall_status = "degraded"
        except Exception as e:
            results[name] = "down"
            overall_status = "down"

    return func.HttpResponse(
        body=f'{{\"status\": \"{overall_status}\", \"details\": {results}}}',
        status_code=200 if overall_status == "healthy" else 503,
        mimetype="application/json"
    )