from solver import even_odd, sum_all, time_of_day, Product, Shop
from freezegun import freeze_time
import pytest


# Testing function "even_odd"
@pytest.mark.parametrize("new_val, expected", [(4, "even"), (5, "odd")])
def test_even_or_odd(new_val, expected):
    """Test of even_odd function

    first even was given return 'even'
    then odd number must return 'odd'
    """
    assert even_odd(new_val) == expected


# Testing next function "sum_all"
def test_sum_all_int():
    """Sum_all sums all given numbers together
    int
    """
    assert sum_all(15, 1, 2, 3) == 21, "21 should be"


# Testing next function "sum_all"
def test_sum_all_float():
    """Sum_all sums all given numbers together
    float
    """
    assert sum_all(-15.5, -1, -2, -2.7) == -21.2, "21.2 should be"


# Testing next function "time_of_day"
night = freeze_time("5:59:59")


def test_time_night():
    """Testing current time of day.

     must be night
     """
    night.start()
    assert time_of_day() == "night", "night should be"
    night.start()


def test_time_morning():
    """Testing current time of day.

    must be morning
    """
    with freeze_time("6:0:0"):
        assert time_of_day() == "morning", "morning should be"


@freeze_time("17:21:34")
def test_time_morning():
    """Testing current time of day.

    must be morning
    """
    assert time_of_day() == "afternoon", "afternoon should be"


@freeze_time("21:21:21")
def test_time_morning():
    """Testing current time of day.

    must be morning
    """
    assert time_of_day() == "night", "night should be"


@pytest.fixture()
def new_product(price=6.7, quantity=6):
    """Create new product : title, price, quantity=1"""
    return Product("chocolate", price=price, quantity=quantity)


@pytest.mark.parametrize("sub_quan, expected", [(4, 2), (-1, 7), (0, 6), (10, -4)])
def test_subtract_quantity(sub_quan, expected, new_product):
    """Test method 'subtract_quantity' quantity must be >= 0"""
    new_product.subtract_quantity(sub_quan)
    assert new_product.quantity == expected, "must be >= 0 failed (10, 0)"


@pytest.mark.parametrize("sub_quan, expected", [(4, 10), (-10, -4)])
def test_add_quantity(sub_quan, expected, new_product):
    """Test method 'add_quantity' quantity must be >= 0"""
    new_product.add_quantity(sub_quan)
    assert new_product.quantity == expected, "must be >= 0 failed (-10, 0)"


@pytest.mark.parametrize("sub_quan", [89.5])
def test_change_price(sub_quan, new_product):
    """Test method 'change_price' price must be the same as given"""
    new_product.change_price(sub_quan)
    assert new_product.price == 89.5, "must be the same as given"


class TestShop:
    """Testing methods from class Shop"""

    @pytest.fixture()
    def empty_shop(self, products=None):
        """Fixture function create empty shop"""
        return Shop(products)

    def test_if_products_is_none(self, empty_shop):
        """Testing __init__
         when we create empty shop products == []
        """
        assert empty_shop.products == [], "[] should be"

    @pytest.fixture()
    def one_product_shop(self, price=6.7, quantity=8):
        """Fixture function create shop with one product"""
        snikers = Product(title="chocolate", price=price, quantity=quantity)
        return Shop(snikers)

    def test_one_products_in_shop(self, one_product_shop):
        """Test function elif
        Shop.products = [products]
        products should be class Product
        """
        assert isinstance(one_product_shop.products[0], Product), "class Product should be"
        # assert one_product_shop.products[0].title == "chocolate", "'chocolate' should be"

    def test_empty_shop_add_product(self, empty_shop, new_product):
        """Testing method add_product
        empty_shop should append first product
        """
        empty_shop.add_product(new_product)
        assert len(empty_shop.products) == 1, "1 should be"

    @pytest.fixture()
    def two_product_shop(self, price=6.7, quantity=8):
        """Fixture function create shop with two products"""
        snikers = Product(title="chocolate", price=price, quantity=quantity)
        knee_socks = Product(title="socks", price=9.9, quantity=3)
        return Shop([snikers, knee_socks])

    def test_two_product_shop_append_one(self, two_product_shop, new_product):
        """Testing method add_product

        if shop with two products append one product
        3 in sum
        2+1=3
        """
        two_product_shop.add_product(new_product)
        assert len(two_product_shop.products) == 3, "3 should be"

    @pytest.mark.parametrize("parameter, index",
                             [("socks", 1), ("chocolate", 0), ("explicit-implicit", None)])
    def test_get_product_index(self, parameter, index, two_product_shop):
        """Testing method get_product_index

        if product.title == gotten parameter
            then we getting index of product from Shop object
            Shop([product, product])
        """
        assert two_product_shop._get_product_index(parameter) == index, "1, 0 and None should be"

    @pytest.mark.parametrize("title, qty_to_sell", [("chocolate", 9)])
    def test_sell_product_raise_ValueError(self, title, qty_to_sell, one_product_shop):
        """Testing method sell_product raise ValueError

        if product_index is not None
        and Shop.products[product_index].quantity < qty_to_sell
        raise ValueError
        """
        with pytest.raises(ValueError):
            one_product_shop.sell_product(title, qty_to_sell)

    @pytest.mark.parametrize("title, qty_to_sell", [("chocolate", 8)])
    def test_sell_product_should_del_product(self, title, qty_to_sell, one_product_shop):
        """Testing method sell_product del products

        if qty_to_sell == product.quantity
            product.quantity - qty_to_sell
        we delete Shop.products[product_index]

        in one_product_shop we have only one product
        after del null left
        """
        one_product_shop.sell_product(title, qty_to_sell)
        assert len(one_product_shop.products) == 0, "0 should be"

    @pytest.mark.parametrize("title, qty_to_sell", [("chocolate", 7)])
    def test_sell_product_should_subtract_quantity(self, title, qty_to_sell, one_product_shop):
        """Testing method sell_product should subtract quantity

        we have 8 products, 7 sold, 1 left
        """
        one_product_shop.sell_product(title, qty_to_sell)
        assert one_product_shop.products[0].quantity == 1, "1 should be"

    @pytest.mark.parametrize("title, qty_to_sell", [("chocolate", 2)])
    def test_sell_product_more_money(self, title, qty_to_sell, one_product_shop):
        """Testing method sell_product
        sell 2 products
        price = 6.7
        receipt = 13.4
        """
        one_product_shop.sell_product(title, qty_to_sell)
        assert one_product_shop.money == 13.4, "13.4 should be"




