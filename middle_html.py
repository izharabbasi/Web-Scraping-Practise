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


soup = BeautifulSoup(ITEM_HTML, "html.parser")


def find_name():
    locators = "article.product_pod h3 a"
    name = soup.select_one(locators).attrs["title"]
    print(name)


def find_link():
    locators = "article.product_pod a"
    link = soup.select_one(locators).attrs["href"]
    print(link)


def find_price():
    locators = "article.product_pod div.product_price p.price_color"
    price = soup.select_one(locators)
    print(price.string)


def find_rating():
    locators = "article.product_pod p.star-rating"
    rating = soup.select_one(locators)
    classes = rating.attrs['class']
    rating_classes = [r for r in classes if r != "star-rating"]
    print(rating_classes)


find_name()
find_link()
find_price()
find_rating()
