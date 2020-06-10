from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItemLocators:
    NAME_LOCATOR = "article.product_pod h3 a"
    LINK_LOCATOR = "article.product_pod a"
    PRICE_LOCATOR = "article.product_pod div.product_price p.price_color"
    RATING_LOCTAOR = "article.product_pod p.star-rating"


class ParseItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(ITEM_HTML, "html.parser")

    @property
    def find_name(self):
        locators = ParsedItemLocators.NAME_LOCATOR
        name = self.soup.select_one(locators).attrs["title"]
        return name

    @property
    def find_link(self):
        locators = ParsedItemLocators.LINK_LOCATOR
        link = self.soup.select_one(locators).attrs["href"]
        return link

    @property
    def find_price(self):
        locators = ParsedItemLocators.PRICE_LOCATOR
        price = self.soup.select_one(locators)
        return price.string

    @property
    def find_rating(self):
        locators = ParsedItemLocators.RATING_LOCTAOR
        rating = self.soup.select_one(locators)
        classes = rating.attrs['class']
        rating_classes = [r for r in classes if r != "star-rating"]
        return rating_classes


item = ParseItem(ITEM_HTML)
print(item.find_name)
print(item.find_link)
print(item.find_price)
print(item.find_rating)
