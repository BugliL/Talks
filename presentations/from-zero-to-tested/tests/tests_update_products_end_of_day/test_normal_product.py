from unittest import TestCase
from unittest.mock import patch, Mock

from src.interfaces import Product

from src.update_products_end_of_day import update_products_end_of_day


@patch("src.update_products_end_of_day.cursor")
class UpdateProductsEndOfDayShould(TestCase):
    def test_update_normal_product_data_when_called(self, mock_cursor: Mock) -> None:
        """
        Un prodotto normale diminuisce quality ed exp_days di 1 dopo un giorno
        """

        # Arrange
        normal_product = Product(
            id=1,
            name="Prodotto Normale",
            exp_days=5,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [normal_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(normal_product.exp_days, 4)
        self.assertEqual(normal_product.quality, 9)

    def test_update_expired_normal_product_when_called(self, mock_cursor: Mock) -> None:
        """
        Un prodotto normale diminuisce di quality di 2 dopo la scadenza
        """

        # Arrange
        normal_product = Product(
            id=1,
            name="Prodotto Normale",
            exp_days=-1,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [normal_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(normal_product.exp_days, -2)
        self.assertEqual(normal_product.quality, 8)
