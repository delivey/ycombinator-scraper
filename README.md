# ycombinator-scraper

Proof-of-concept YCombinator scraper, which gets all of the companies with other data from YCombinator's Algolia search

# Running

```
py main.py
```

This will export the companies to a file called companies.json and pretty-print all of them

# Example company

```json
{
    "id": 12064,
    "name": "Deel",
    "slug": "deel",
    "former_names": ["SciDex", "Deel", "D"],
    "small_logo_thumb_url": "https://bookface-images.s3.amazonaws.com/small_logos/9152bb798308624071239d0e8cb4421c8d24857d.png",
    "website": "https://www.deel.com/",
    "all_locations": "San Francisco, CA, USA; Remote",
    "long_description": "Deel is the all-in-one HR platform for global teams. It helps companies simplify every aspect of managing an international workforce, from culture and onboarding, to local payroll and compliance. Deel works for independent contractors and full-time employees in more than 150 countries, compliantly. And getting set up takes just a few minutes. For more information, visit Deel.com.",
    "one_liner": "The all-in-one HR platform for global teams.",
    "team_size": 2000,
    "highlight_black": false,
    "highlight_latinx": false,
    "highlight_women": true,
    "industry": "B2B",
    "subindustry": "B2B -> Finance and Accounting",
    "launched_at": 1541644458,
    "tags": ["Fintech", "SaaS", "B2B", "Compliance", "HR Tech"],
    "tags_highlighted": [],
    "top_company": true,
    "top_company_by_revenue": true,
    "isHiring": true,
    "nonprofit": false,
    "batch": "W19",
    "status": "Active",
    "industries": ["B2B", "Finance and Accounting"],
    "regions": [
        "United States of America",
        "America / Canada",
        "Remote",
        "Fully Remote"
    ],
    "stage": "Early",
    "app_video_public": false,
    "demo_day_video_public": false,
    "app_answers": null,
    "question_answers": true,
    "objectID": "12064",
    "_highlightResult": {
        "name": {
            "value": "Deel",
            "matchLevel": "none",
            "matchedWords": []
        },
        "former_names": [
            {
                "value": "SciDex",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "Deel",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "D",
                "matchLevel": "none",
                "matchedWords": []
            }
        ],
        "website": {
            "value": "https://www.deel.com/",
            "matchLevel": "none",
            "matchedWords": []
        },
        "all_locations": {
            "value": "San Francisco, CA, USA; Remote",
            "matchLevel": "none",
            "matchedWords": []
        },
        "long_description": {
            "value": "Deel is the all-in-one HR platform for global teams. It helps companies simplify every aspect of managing an international workforce, from culture and onboarding, to local payroll and compliance. Deel works for independent contractors and full-time employees in more than 150 countries, compliantly. And getting set up takes just a few minutes. For more information, visit Deel.com.",
            "matchLevel": "none",
            "matchedWords": []
        },
        "one_liner": {
            "value": "The all-in-one HR platform for global teams.",
            "matchLevel": "none",
            "matchedWords": []
        },
        "tags": [
            {
                "value": "Fintech",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "SaaS",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "B2B",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "Compliance",
                "matchLevel": "none",
                "matchedWords": []
            },
            {
                "value": "HR Tech",
                "matchLevel": "none",
                "matchedWords": []
            }
        ]
    }
}
```
