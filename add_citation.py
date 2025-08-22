def add_citation(url, license="unknown"):
    with open("Code Citations.md", "a", encoding="utf-8") as f:
        f.write(f"\n## License: {license}\n{url}\n")

if __name__ == "__main__":
    url = input("Enter the code source URL: ").strip()
    license = input("Enter the license (or leave blank for 'unknown'): ").strip() or "unknown"
    add_citation(url, license)
