import json
from typing import Dict, List

SITE_DATABASE = [
    {
        "id": 1,
        "name": "Portal Page HTH",
        "url": "https://portal-page-hth.com",
        "keywords": ["hth", "portal", "page"],
        "tags": ["landing", "web-app", "demo"],
        "description": "Main entry point for the HTH ecosystem, providing user dashboards and navigation."
    },
    {
        "id": 2,
        "name": "HTH Documentation Hub",
        "url": "https://portal-page-hth.com/docs",
        "keywords": ["hth", "docs", "guide"],
        "tags": ["documentation", "reference", "help"],
        "description": "Comprehensive guides and API references for the HTH platform."
    },
    {
        "id": 3,
        "name": "HTH Community Forum",
        "url": "https://portal-page-hth.com/community",
        "keywords": ["hth", "forum", "community"],
        "tags": ["discussion", "support", "updates"],
        "description": "Official community forum for HTH users to share ideas and get support."
    },
    {
        "id": 4,
        "name": "HTH Status Page",
        "url": "https://portal-page-hth.com/status",
        "keywords": ["hth", "status", "uptime"],
        "tags": ["monitoring", "health", "reliability"],
        "description": "Real-time status and incident reports for all HTH services."
    }
]

def format_summary(site: Dict) -> str:
    """Convert a single site dictionary into a readable summary string."""
    kw_list = ", ".join(site["keywords"])
    tag_list = ", ".join(site["tags"])
    return (
        f"Site: {site['name']}\n"
        f"URL: {site['url']}\n"
        f"Keywords: {kw_list}\n"
        f"Tags: {tag_list}\n"
        f"Description: {site['description']}\n"
        f"{'─' * 40}\n"
    )

def generate_all_summaries(sites: List[Dict]) -> str:
    """Iterate over all sites and produce a combined summary block."""
    header = "=== HTH Site Summary ===\n\n"
    body = ""
    for entry in sites:
        body += format_summary(entry)
    footer = f"Total sites: {len(sites)}"
    return header + body + footer

def write_summary_to_file(content: str, output_path: str = "site_summary_output.txt") -> None:
    """Write the generated summary to a text file."""
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"[INFO] Summary written to {output_path}")

def filter_sites_by_keyword(sites: List[Dict], keyword: str) -> List[Dict]:
    """Return only sites that contain the given keyword in their keywords list."""
    return [s for s in sites if keyword in s["keywords"]]

def main() -> None:
    """Main entry point: produce structured summary and optionally filter by keyword."""
    print("Generating structured summary of HTH sites...\n")
    full_summary = generate_all_summaries(SITE_DATABASE)
    print(full_summary)
    
    # Example filtering
    filtered = filter_sites_by_keyword(SITE_DATABASE, "hth")
    print(f"\nFiltered sites (keyword='hth'): {len(filtered)}")
    for site in filtered:
        print(f"  - {site['name']}")

    # Persist output
    write_summary_to_file(full_summary)

if __name__ == "__main__":
    main()