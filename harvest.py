############
# Part 1   #
############

muskmelon = MelonType("musk", "1998, "green", True, True, "Muskmelon")
casaba = MelonType("cas", "2003", "orange", False, False, "Casaba") 
crenshaw = MelonType("cren", "1996", "g")                     

class MelonType:
    """A species of melon at a melon farm."""

    # muskmelon_dict = ('code': 'musk',
    #                   'First Harvest': 1998,
    #                   'color': 'Green',
    #                   'pairs_with': ['Mint'], #take out list if doesnt work
    #                   'is_seedless': True,
    #                   'is_bestseller': True,
    #                   'name': 'Muskmelon'

    # )

    # casaba_dict = ()'code': 'cas',
    #                'first_harvest': 2003,
    #                'color': 'Orange',
    #                'pairs_with': ['Strawberries', 'Mint'],
    #                'is_seedless': False,
    #                'is_bestseller': False,
    #                'name': 'Casaba'
    # )

    # crenshaw_dict = {'code': 'cren',
    #                'first_harvest': 1996,
    #                'color': 'Green',
    #                'pairs_with': ['Proscuitto'],
    #                'is_seedless': False,
    #                'is_bestseller': False,
    #                'name': 'Crenshaw'
    # }

    # yellow_watermelon_dict = {'code': 'yw',
    #                'first_harvest': 2013,
    #                'color': 'Yellow',
    #                'pairs_with': ['Ice Cream'],
    #                'is_seedless': False,
    #                'is_bestseller': True,
    #                'name': 'Yellow Watermelon'
    # }
    
    

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

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
