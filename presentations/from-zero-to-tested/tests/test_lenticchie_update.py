from unittest import TestCase

from src.update_products_end_of_day import update_lenticchie_product
from src.interfaces import Product


class TestLenticchieUpdate(TestCase):
    def test_update_lenticchie_product_when_called(self) -> None:
        # Arrange
        product = Product(
            id=3,
            name="Lenticchie Biologiche",
            exp_days=5,
            quality=10,
        )

        # Act
        update_lenticchie_product(item=product)

        # Assert
        self.assertEqual(product.quality, 8)
        self.assertEqual(product.exp_days, 4)
