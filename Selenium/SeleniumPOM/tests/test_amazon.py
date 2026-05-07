import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon in not correct'
    print("\nOpened Amazon Homepage. Title & URL verified")

@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"),
    ("shoes")
])
def test_search_product(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"\nSearching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True,'Search results page did not load.'
    print(f"Search results page loaded successfully - {searchproduct}")


@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"),
    ("shoes")
])
def test_find_elements_amazon(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"\nSearching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"Search results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert val, "No products found on Amazon search results!"       #we can write val == True if we want but assert will by default take true as correct

@pytest.mark.parametrize(("searchproduct", "brandname"),
[
    ("wireless mouse", 'Logitech'),
    ("shoes", "Nike")
])
def test_brand_filter(driver, searchproduct, brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"\nSearching product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"Search results page loaded successfully - {searchproduct}")

    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)
    #for shoes it will give error here because we hard coded it in for logitech but for shoes it is not able to find the element
    assert productlistingpage.check_product_titles_for_brand_filter(brandname), "Brand filter didn't apply properly"


