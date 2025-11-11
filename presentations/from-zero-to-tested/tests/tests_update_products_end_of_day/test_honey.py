from unittest import TestCase
from unittest.mock import patch, Mock

from src.interfaces import Product

from src.update_products_end_of_day import update_products_end_of_day


@patch("src.update_products_end_of_day.cursor")
class UpdateProductsEndOfDayShould(TestCase):
    def test_update_miele_data_when_called(self, mock_cursor: Mock) -> None:
        """
        Il Miele non degrada mai di qualita' e non scade mai
        """

        # Arrange
        brie_product = Product(
            id=2,
            name="Miele",
            exp_days=10,
            quality=5,
        )

        mock_cursor.fetchall.return_value = [brie_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(brie_product.exp_days, 10)
        self.assertEqual(brie_product.quality, 5)
