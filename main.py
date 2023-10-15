from parser import get_pages, get_jobs, print_res
from resources import all_url

ITEMS = 20


def main():
    result = []
    for url in all_url:
        url = f'{url}&items_on_page={ITEMS}'
        pages = get_pages(url)
        result.append(get_jobs(pages, url))

    print_res(result)


if __name__ == "__main__":
    main()