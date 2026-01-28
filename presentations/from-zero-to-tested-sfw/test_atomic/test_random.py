from unittest.mock import Mock, patch
from unittest import TestCase

import random


class TestRandom(TestCase):
    @patch("random.randint", return_value=5)
    def test_random(self, mock_random: Mock):
        result = random.randint(10, 20)
        assert result == 5

        mock_random.assert_called_once()
