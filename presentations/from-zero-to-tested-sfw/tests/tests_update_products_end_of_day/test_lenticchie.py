from unittest import TestCase
from unittest.mock import Mock, patch

from src.update_products_end_of_day import update_products_end_of_day
from src.interfaces import Product


@patch("src.update_products_end_of_day.cursor")
class UpdateProductsEndOfDayShould(TestCase):
    def test_update_lenticchie_product_when_called(self, mock_cursor: Mock) -> None:
        # Arrange
        product = Product(
            id=3,
            name="Lenticchie Biologiche",
            exp_days=5,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(product.quality, 8)
        self.assertEqual(product.exp_days, 4)
