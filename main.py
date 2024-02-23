from batches import get_batches
from batch import scrape_batch
from concurrent.futures import ThreadPoolExecutor
from batches import get_batches
from batch import scrape_batch
import json


def scrape_all_companies():
    batches = get_batches()
    all_companies = []

    def scrape_and_collect(batch):
        companies = scrape_batch(batch)
        all_companies.extend(companies)

    with ThreadPoolExecutor() as executor:
        executor.map(scrape_and_collect, batches)

    return all_companies


def pretty_print_companies(companies):
    for idx, company in enumerate(companies):
        description = company['one_liner']
        if description == "":
            description = company['long_description']
        print(
            f"{idx+1}. {company['name']} ({company['batch']}) - {company['one_liner']}")


def export_all_companies(companies):
    with open('companies.json', 'w', encoding='utf-8') as f:
        json.dump(companies, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    companies = scrape_all_companies()
    companies.sort(key=lambda x: x['launched_at'])
    pretty_print_companies(companies)
    export_all_companies(companies)
