from unittest import TestCase
from unittest.mock import patch, Mock

from src.interfaces import Product

from src.update_products_end_of_day import update_products_end_of_day


@patch("src.update_products_end_of_day.cursor")
class UpdateProductsEndOfDayShould(TestCase):
    def test_update_promozione_speciale_data_when_called(
        self, mock_cursor: Mock
    ) -> None:
        """
        La promozione speciale aumenta di quality di 1 dopo un giorno
        """

        # Arrange
        special_promotion = Product(
            id=2,
            name="Promozione Speciale",
            exp_days=5,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [special_promotion]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(special_promotion.exp_days, 4)
        self.assertEqual(special_promotion.quality, 13)

    def test_update_promozione_speciale_scaduto_when_called(
        self, mock_cursor: Mock
    ) -> None:
        """
        La promozione speciale perde tutta la quality dopo la scadenza
        """

        # Arrange
        special_promotion = Product(
            id=2,
            name="Promozione Speciale",
            exp_days=-1,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [special_promotion]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(special_promotion.exp_days, -2)
        self.assertEqual(special_promotion.quality, 0)

    def test_update_promozione_speciale_quality_max_50_when_called(
        self, mock_cursor: Mock
    ) -> None:
        """
        La promozione speciale non supera mai quality 50
        """

        # Arrange
        special_promotion = Product(
            id=2,
            name="Promozione Speciale",
            exp_days=5,
            quality=55,
        )

        mock_cursor.fetchall.return_value = [special_promotion]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(special_promotion.exp_days, 4)
        self.assertEqual(special_promotion.quality, 55)

    def test_update_promozione_speciale_exp_date_lt_11_gt_6_when_called(
        self, mock_cursor: Mock
    ) -> None:
        """
        La promozione speciale aumenta di quality di 3 quando mancano meno di 6 giorni alla scadenza
        """

        # Arrange
        special_promotion = Product(
            id=2,
            name="Promozione Speciale",
            exp_days=10,
            quality=10,
        )

        mock_cursor.fetchall.return_value = [special_promotion]

        # Act
        update_products_end_of_day()

        # Assert
        self.assertEqual(special_promotion.exp_days, 9)
        self.assertEqual(special_promotion.quality, 12)
