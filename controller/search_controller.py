import httpx
import http
from fastapi import APIRouter, Depends

from service.searchService import Search
from service.utils import Company

search_router = APIRouter(prefix="/search", tags=["search"])


@search_router.get("/", status_code=http.HTTPStatus.CREATED)
async def search_products(q: str):
    try:
        # Create an asynchronous HTTP client
        async with httpx.AsyncClient() as client:
            # Perform search on different platforms asynchronously
            amazon_results = await Search.search(Company.AMAZON, q)
            flipkart_results = await Search.search(Company.FLIPKART, q)
            reliance_digital_results = await Search.search(Company.RELIANCE, q)
            # croma_results = await CromaSearch.search(Company.CROMA, q)

        # Collect the search results from different platforms
        results = {
            "amazon": amazon_results,
            "flipkart": flipkart_results,
            "reliance_digital": reliance_digital_results,
            # "croma": croma_results
        }

        # Return the results as the API response
        return {"results": results}

    except Exception as e:
        print("Error:", e)
        return {"error": "Internal Server Error"}