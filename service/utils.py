from enum import Enum


class Company(Enum):
    FLIPKART = "flipkart"
    AMAZON = "amazon",
    CROMA = "croma",
    RELIANCE = ""

companyDetails = {
    Company.FLIPKART: {
        "url": "https://www.flipkart.com/search?q=",
        "mainDiv": "._1AtVbE.col-12-12",
        "name": "div._4rR01T",
        "image": "img._396cs4",  # Add the CSS selector for the image element
        "price": "div._1_WHN1",  # Add the CSS selector for the price element
    },
    Company.AMAZON: {
        "url": "https://www.amazon.in/s?k=",
        "mainDiv": "div.s-result-item",
        "name": "span.a-size-medium",
        "image": "img.s-image",
        "price": "span.a-price-whole",
    },    Company.CROMA: {
        "url": "https://www.croma.com/search/?text=",
        "mainDiv": "ul.search-productList > li",
        "name": ".product__name",
        "image": ".product-image img",
        "price": ".price .pdpPrice",
    },Company.RELIANCE:{
        "url": "https://www.reliancedigital.in/search?q=",
            "mainDiv": "li.pl__container__sp",
            "name": "p.sp__name",
            "image": "div.lazy-load-image-background img",
            "price": "span.TextWeb__Text-sc-1cyx778-0",
        }
}
