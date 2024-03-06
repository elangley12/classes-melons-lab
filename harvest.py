############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    muskmelon_dict = {'Reporting Code': 'musk',
                      'First Harvest': 1998,
                      'Color': 'Green',
                      'Pairs with': ['Mint'], #take out list if doesnt work
                      'Seedless': True,
                      'Bestseller': True,

    }

    casaba_dict = {'Reporting Code': 'cas',
                   'First Harvest': 2003,
                   'Color': 'Orange',
                   'Pairs with': ['Strawberries', 'Mint'],
                   'Seedless': False,
                   'Bestseller': False,
    }

    crenshaw_dict = {'Reporting Code': 'cren',
                   'First Harvest': 1996,
                   'Color': 'Green',
                   'Pairs with': ['Proscuitto'],
                   'Seedless': False,
                   'Bestseller': False,
    }

    yellow_watermelon_dict = {'Reporting Code': 'yw',
                   'First Harvest': 2013,
                   'Color': 'Yellow',
                   'Pairs with': ['Ice Cream'],
                   'Seedless': False,
                   'Bestseller': True,
    }

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
