import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_product_ordering(driver):
    assert "amazon" in driver.current_url, 'URL for amazon in not correct'
    print("\nOpened Amazon Homepage. Title & URL verified")

@pytest.mark.parametrize(("searchproduct", "brandname", "mensize"),
[
    ("shoes", 'Nike', "9")
])
def test_search_product(driver, searchproduct, brandname, mensize):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"\nSearching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True,'Search results page did not load.'
    print(f"Search results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)
    print(f"Applying Brand Filter - {brandname}")
    # for shoes it will give error here because we hard coded it in for logitech but for shoes it is not able to find the element
    assert productlistingpage.check_product_titles_for_brand_filter(brandname), "Brand filter didn't apply properly"

    productlistingpage.mensize_locator(mensize)
    print(f"Applying Size filter for men's shoes - {mensize}")
    assert productlistingpage.check_size_in_title(mensize), "Mensize filter didn't apple"


