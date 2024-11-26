"""
Unit tests for the main package
"""

import unittest

from ${{ values.module }}.main import main


class TestMain(unittest.TestCase):
    """
    Test the functionality of the main package.
    """

    def test_main(self) -> None:
        """
        Test the functionality of the :py:func:`${{ values.module }}.main` function
        """

        main()
