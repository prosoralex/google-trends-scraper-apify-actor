# Google Trends Scraper — Apify Actor usage guide

FAST & CHEAP — $1 / 1,000 results. Scrape Google Trends by keyword or URL: trends over time, subregions, related queries/topics, locations, time ranges and categories. Export data, run via API, schedule and monitor runs.

> **This repository does not contain the Actor's source code.** The Actor
> itself is closed-source and runs on Apify's infrastructure — this repo is
> just documentation and example client code showing how to call it via the
> Apify API/SDK with your own Apify API token. Think of it as a "cookbook"
> repo, not the product itself.

**Run it on Apify →** [https://apify.com/leadsbrary/google-trends-scraper?fpr=aupara](https://apify.com/leadsbrary/google-trends-scraper?fpr=aupara)

## What it does

Extract Google Trends data for search terms, comparison groups, Google Trends explore URLs, or public spreadsheets without an API key. The Actor scrapes Google Trends explore widgets and returns structured trend metrics: time-series interest scores (weekly or daily, normalized 0–100), average interest for compared terms, geographic distributions (country, subregion, city, metro), top and rising related search queries, top and rising related topics, and indicators of any widgets that returned no data. It supports multi-term comparisons (up to five terms per comparison), reading all parameters from a pasted Google Trends URL, custom time ranges, and can route requests through a residential proxy in a specified country for geo-accurate results.…

## Pricing

Pay-per-event pricing — you only pay for what the Actor actually delivers:

- **Actor Start** — $0.00005 (one-time, per run). Charged when the Actor starts running. Number of events charged depends on Actor memory (one event per GB, minimum one event).
- **result** — $0.0012–$0.001 depending on your Apify usage tier. Single result in the default dataset.

*(Apify may also charge a small amount for the platform compute the Actor
uses while running — see the [pricing tab](https://apify.com/leadsbrary/google-trends-scraper?fpr=aupara) on the Actor page
for exact current numbers.)*

## Quick start

You need an Apify account and API token (`console.apify.com` → Settings →
Integrations). Don't have one yet? See the signup section below — new
accounts get **$5 of free usage credit every month**.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~google-trends-scraper/runs?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

### Python (`apify-client`)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
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

run = client.actor("leadsbrary/google-trends-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });

const runInput = {
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
};

const run = await client.actor('leadsbrary/google-trends-scraper').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

See [`example.py`](./example.py) in this repo for a complete runnable script.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get **$5 of free platform credit
every month**, enough to try most Actors without paying anything upfront.
Browsing for other tools? The full [Apify Store](https://apify.com/store?fpr=aupara) has thousands
of ready-made Actors.

## Links

- Actor page (run it, see live pricing/reviews): [https://apify.com/leadsbrary/google-trends-scraper?fpr=aupara](https://apify.com/leadsbrary/google-trends-scraper?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API docs: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## License

The example code in this repository (README snippets, `example.py`) is
released under the MIT License — see [LICENSE](./LICENSE). This does not
cover the Actor itself, which remains closed-source and is operated by its
developer on the Apify platform.
