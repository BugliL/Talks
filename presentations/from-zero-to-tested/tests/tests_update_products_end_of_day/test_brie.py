from contextlib import AbstractContextManager
from typing import Any
from unittest import TestCase
from unittest.mock import patch, Mock

from src.interfaces import Product

from src.update_products_end_of_day import update_products_end_of_day


@patch("src.update_products_end_of_day.cursor")
class UpdateProductsEndOfDayShould(TestCase):
    def test_update_formaggio_brie_data_when_called(self, mock_cursor: Mock) -> None:
        """
        Il Formaggio Brie aumenta di quality di 1 dopo un giorno
        """

        # Arrange
        brie_product = Product(
            id=2,
            name="Formaggio Brie",
            exp_days=5,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [brie_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(brie_product.exp_days, 4)
        self.assertEqual(brie_product.quality, 11)

    def test_update_formaggio_brie_scaduto_when_called(self, mock_cursor: Mock) -> None:
        """
        Il Formaggio Brie aumenta di quality di 2 dopo la scadenza
        """

        # Arrange
        brie_product = Product(
            id=2,
            name="Formaggio Brie",
            exp_days=-1,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [brie_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(brie_product.exp_days, -2)
        self.assertEqual(brie_product.quality, 12)

    def test_update_formaggio_brie_max_quality_when_called(
        self, mock_cursor: Mock
    ) -> None:
        """
        Il Formaggio Brie non supera mai quality 50
        """

        # Arrange
        brie_product = Product(
            id=2,
            name="Formaggio Brie",
            exp_days=5,
            quality=50,
        )

        mock_cursor.fetchall.return_value = [brie_product]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(brie_product.exp_days, 4)
        self.assertEqual(brie_product.quality, 50)
