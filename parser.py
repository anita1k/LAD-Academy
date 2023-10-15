import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                         '/117.0.0.0 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_pages(url):
    response = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    pages = []
    paginator = soup.find_all("span", {'class': 'pager-item-not-in-short-range'})
    if not paginator:
        return 1
    else:
        for page in paginator:
            pages.append(int(page.find('a').text))

    return pages[-1]


def get_jobs(pages, url):
    jobs = []

    for page in range(pages):
        result = get_html(url, params={'page': page})
        soup = BeautifulSoup(result.text, "lxml")
        results = soup.find_all('div', {'class': 'serp-item'})

        for result in results:
            jobs.append(result.find('a').text)
    return len(jobs)


def print_res(results):
    print(
        f'Grade: Junior\nVacancies: Аналитик данных, Data Scientist\nNumber: {results[0] + results[3]}\n\n'
        f'Grade: Middle\nVacancies: Аналитик данных, Data Scientist\nNumber: {results[1] + results[4]}\n\n'
        f'Grade: Senior\nVacancies: Аналитик данных, Data Scientist\nNumber: {results[2] + results[5]}\n\n'
    )
