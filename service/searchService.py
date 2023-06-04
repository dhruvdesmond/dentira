from typing import Dict, List

from bs4 import BeautifulSoup
import requests
from service.utils import Company, companyDetails


class Search:
    @staticmethod
    async def search(company_name: Company, query: str) -> List[Dict[str, str]]:
        if company_name not in companyDetails:
            raise ValueError(f"Company '{company_name}' is not supported")

        details = companyDetails[company_name]

        base_url = details["url"]
        url = f"{base_url}{query}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        # Send a GET request to the search URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        results = []

        # Extract the relevant HTML elements from the page
        items = soup.select(details["mainDiv"])
        print("Items: ", len(items))

        # Parse each item and extract the necessary information
        for item in items:
            name_element = item.select_one(details["name"])
            image_element = item.select_one(details["image"])
            price_element = item.select_one(details["price"])

            if name_element and image_element and price_element:
                # Extract the name, image URL, and price from the elements
                name = name_element.text.strip()
                image = image_element["src"]
                price = float(price_element.text.replace(",", "").replace("₹", ""))

                # Add the item details to the results list
                results.append({"name": name, "image": image, "price": price})

        return results
