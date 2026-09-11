"""
Minimal working example: run the "Google Trends Scraper" Apify Actor
and print its results.

Setup:
    pip install apify-client
    export APIFY_TOKEN=your_apify_token_here   # console.apify.com > Settings > Integrations

This repo is just usage documentation for the Actor — the Actor's own source
code is not included here (it runs on Apify's infrastructure).
"""
import os
import sys

from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
ACTOR_ID = "leadsbrary/google-trends-scraper"

RUN_INPUT = {
    "searchTerms": [
        "web scraping"
    ],
    "isMultiple": false,
    "skipDebugScreen": false,
    "startUrls": [
        {
            "url": "https://trends.google.com/trends/explore?date=today%2012-m&q=web%20scraping"
        }
    ],
    "maxItems": 0,
    "maxConcurrency": 10,
    "maxRequestRetries": 7,
    "pageLoadTimeoutSecs": 180
}


def main() -> None:
    if not APIFY_TOKEN:
        sys.exit("Set the APIFY_TOKEN environment variable first (get one at console.apify.com).")

    client = ApifyClient(APIFY_TOKEN)

    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")

    print("Results:")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
