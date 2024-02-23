import requests


def scrape_batch(name):
    data = {
        "requests": [
            {
                "indexName": "YCCompany_production",
                "params": f"facetFilters=%5B%5B%22batch%3A{name}%22%5D%5D&facets=%5B%22app_answers%22%2C%22app_video_public%22%2C%22batch%22%2C%22demo_day_video_public%22%2C%22highlight_black%22%2C%22highlight_latinx%22%2C%22highlight_women%22%2C%22industries%22%2C%22isHiring%22%2C%22nonprofit%22%2C%22question_answers%22%2C%22regions%22%2C%22subindustry%22%2C%22tags%22%2C%22top_company%22%2C%22top_company_by_revenue%22%5D&hitsPerPage=1000&maxValuesPerFacet=1000&page=0&query=&tagFilters="
            },
            {
                "indexName": "YCCompany_production",
                "params": "analytics=false&clickAnalytics=false&facets=batch&hitsPerPage=0&maxValuesPerFacet=1000&page=0&query="
            }
        ]
    }

    response = requests.post(
        'https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%3B%20JS%20Helper%20(3.16.1)&x-algolia-application-id=45BWZJ1SGC&x-algolia-api-key=MjBjYjRiMzY0NzdhZWY0NjExY2NhZjYxMGIxYjc2MTAwNWFkNTkwNTc4NjgxYjU0YzFhYTY2ZGQ5OGY5NDMxZnJlc3RyaWN0SW5kaWNlcz0lNUIlMjJZQ0NvbXBhbnlfcHJvZHVjdGlvbiUyMiUyQyUyMllDQ29tcGFueV9CeV9MYXVuY2hfRGF0ZV9wcm9kdWN0aW9uJTIyJTVEJnRhZ0ZpbHRlcnM9JTVCJTIyeWNkY19wdWJsaWMlMjIlNUQmYW5hbHl0aWNzVGFncz0lNUIlMjJ5Y2RjJTIyJTVE',
        json=data,
    )
    json = response.json()
    data = json['results'][0]['hits']
    return data
