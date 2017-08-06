"""Unit tests for gossamer."""

import unittest

from gossamer import Publishers


class TestMethods(unittest.TestCase):
    """Tests for methods on Publishers enum."""

    def test_names(self):
        """Publishers has a list of publisher names."""
        expected = [
            'MARVEL_COMICS',
            'DC_COMICS',
            'DCS_YOUNG_ANIMAL',
            'VERTIGO',
            'DARK_HORSE',
            'IDW_PUBLISHING',
            'IMAGE_COMICS',
            'ACTION_LAB_ENTERTAINMENT',
            'AMAZE_INK_SLAVE_LABOR_GRAPHICS',
        ]

        self.assertEqual(expected, Publishers.names())

    def test_choices(self):
        """Publishers has a Django-inspired choices iterable."""
        expected = (
            (1, 'MARVEL_COMICS'),
            (2, 'DC_COMICS'),
            (3, 'DCS_YOUNG_ANIMAL'),
            (4, 'VERTIGO'),
            (5, 'DARK_HORSE'),
            (6, 'IDW_PUBLISHING'),
            (7, 'IMAGE_COMICS'),
            (8, 'ACTION_LAB_ENTERTAINMENT'),
            (9, 'AMAZE_INK_SLAVE_LABOR_GRAPHICS'),
            (10, 'OTHER'),
        )

        self.assertEqual(expected, Publishers.choices())


class TestPrintableNames(unittest.TestCase):
    """Tests for various pretty-printed publisher names."""

    def test_marvel_comics(self):
        """MARVEL_COMICS is Marvel Comics."""
        self.assertEqual(
            'Marvel Comics', Publishers['MARVEL_COMICS'].printable_name)

    def test_dc_comics(self):
        """DC_COMICS printable name is DC Comics."""
        self.assertEqual('DC Comics', Publishers['DC_COMICS'].printable_name)

    def test_dc_young_animal(self):
        """DCS_YOUNG_ANIMAL is DC's Young Animal."""
        self.assertEqual(
            "DC's Young Animal", Publishers['DCS_YOUNG_ANIMAL'].printable_name)

    def test_vertigo(self):
        """VERTIGO is Vertigo."""
        self.assertEqual('Vertigo', Publishers['VERTIGO'].printable_name)

    def test_dark_horse(self):
        """DARK_HORSE is Dark Horse."""
        self.assertEqual('Dark Horse', Publishers['DARK_HORSE'].printable_name)

    def test_idw_publishing(self):
        """IDW_PUBLISHING is IDW Publishing."""
        self.assertEqual(
            'IDW Publishing', Publishers['IDW_PUBLISHING'].printable_name)

    def test_image_comics(self):
        """IMAGE_COMICS is Image Comics."""
        self.assertEqual(
            'Image Comics', Publishers['IMAGE_COMICS'].printable_name)

    def test_action_lab(self):
        """ACTION_LAB_ENTERTAINMENT is Action Lab Entertainment."""
        self.assertEqual(
            'Action Lab Entertainment',
            Publishers['ACTION_LAB_ENTERTAINMENT'].printable_name)

    def test_amazing_ink(self):
        """AMAZE_INK_SLAVE_LABOR_GRAPHICS is Amazing Ink/Slave Labor."""
        self.assertEqual(
            'Amazing Ink/Slave Labor Graphics',
            Publishers['AMAZE_INK_SLAVE_LABOR_GRAPHICS'].printable_name)

    def test_other(self):
        """OTHER is Other."""
        self.assertEqual('Other', Publishers['OTHER'].printable_name)
