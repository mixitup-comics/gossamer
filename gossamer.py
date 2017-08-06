"""Utils for connecting comics series and publishers."""

import enum


class Publishers(enum.Enum):
    """A list of publishers."""
    MARVEL_COMICS = enum.auto()
    DC_COMICS = enum.auto()
    DCS_YOUNG_ANIMAL = enum.auto()
    VERTIGO = enum.auto()
    DARK_HORSE = enum.auto()
    IDW_PUBLISHING = enum.auto()
    IMAGE_COMICS = enum.auto()
    ACTION_LAB_ENTERTAINMENT = enum.auto()
    AMAZE_INK_SLAVE_LABOR_GRAPHICS = enum.auto()
    OTHER = enum.auto()

    @classmethod
    def names(self):
        """Returns a list of Publisher names."""
        return [item.name for item in self if item.name != 'OTHER']

    @classmethod
    def choices(self):
        """Returns a Django-inspired choices iterable."""
        return tuple((item.value, item.name) for item in self)

    @property
    def printable_name(self):
        """Returns the name of the member in printable form."""
        if self.name == 'DC_COMICS':
            return 'DC Comics'
        elif self.name == 'DCS_YOUNG_ANIMAL':
            return "DC's Young Animal"
        elif self.name == 'IDW_PUBLISHING':
            return 'IDW Publishing'
        elif self.name == 'AMAZE_INK_SLAVE_LABOR_GRAPHICS':
            return 'Amazing Ink/Slave Labor Graphics'
        return self.name.replace('_', ' ').title()
