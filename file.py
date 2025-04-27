import os
import requests
import json
from lxml import etree
import pandas as pd


def extract_urls():
    """
    Extracts hotel detail URLs from the API response of the SLH website.
    """
    url = "https://slh.com/api/slh/hotelsearchresults/gethotelsearchresults"
    base_query_params = {
        "roomsList": "adults=2+children=",
        "sort": "ascName",
        "resultsPerPage": "10",
        "viewType": "list",
    }
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
    }
    base_url = "http://slh.com"
    end_url = "?roomsList=adults%3D2%2Bchildren%3D"
    urls = []
    page_index = 0

    while True:
        query_params = base_query_params.copy()
        query_params["pageIndex"] = str(page_index)

        try:
            response = requests.get(url, headers=headers, params=query_params)
            response.raise_for_status()
            response_content = response.content.decode('utf-8-sig')
            data = json.loads(response_content)

            total_pages = data.get("totalPages", 0)
            hotels = data.get("items", [])

            if not hotels:
                print(f"No more hotels found on page {page_index}. Stopping.")
                break

            for hotel in hotels:
                detail_url = hotel.get("detailUrl", "")
                if detail_url:
                    urls.append(base_url + detail_url + end_url)

            if page_index >= total_pages - 1:
                print("Reached the last page. Exiting.")
                break

            page_index += 1

        except requests.exceptions.RequestException as e:
            print(f"Request error on page {page_index}: {e}")
            break
        except Exception as e:
            print(f"Unexpected error on page {page_index}: {e}")
            break

    return urls


def extract_data_from_page(url):
    """
    Extracts hotel details from a given hotel detail URL.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers, timeout=60)
        response.raise_for_status()
        tree = etree.HTML(response.text)

        hotel_name = tree.xpath('//h1[@class="ui-headline ui-headline--h1 ui-headline--t-9"]/text()')
        hotel_name = hotel_name[0].strip() if hotel_name else "N/A"

        address_data = tree.xpath('//a[@class="ui-link ui-color-c-4 ui-link--caption"]/text()')
        address_data = address_data[0].strip() if address_data else "N/A"
        parts = address_data.split(",")
        location, city, country = "N/A", "N/A", "N/A"

        if len(parts) > 0:
            other_parts = parts[0].split("-")
            location = other_parts[0].strip() if len(other_parts) > 0 else "N/A"
            city = other_parts[1].strip() if len(other_parts) > 1 else 'N/A'
            if country == "N/A" and location:
                country = location
                location = 'N/A'
        if len(parts) > 1:
            country = parts[1].strip()

        attributes = tree.xpath('//div[@class="sc-hotel-location-strained"]/p/text()')
        full_address = " /n".join([attr.strip() for attr in attributes]) if len(attributes) > 0 else ''

        return [hotel_name, location, city, country, full_address, url]

    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed for URL: {url} | Error: {e}")
        return []
    except Exception as e:
        print(f"Error extracting data from URL: {url} | Error: {e}")
        return []


def main():
    """
    Main function to extract hotel data and save it to an Excel file.
    """
    output_file = 'SLH.xlsx'
    backup_file = 'SLH_old.xlsx'

    if os.path.exists(output_file):
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(output_file, backup_file)
        print(f"Renamed {output_file} to {backup_file}")

    urls = extract_urls()
    print(f"Total URLs extracted: {len(urls)}")

    all_data = []
    for i, url in enumerate(urls):
        print(f"Processing {i + 1}/{len(urls)}: {url}")
        data = extract_data_from_page(url)
        if data:
            print(data)
            print('*'*50)
            all_data.append(data)

    print(f"Total records extracted: {len(all_data)}")
    df = pd.DataFrame(
        all_data,
        columns=['hotel_name', 'location', 'city', 'country', 'address', 'url']
    )
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")


if __name__ == "__main__":
    main()
