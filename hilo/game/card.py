import random


# TODO: Implement the Card class as follows...

# 1) Add the class declaration. Use the following class comment.
class Card:
    """A card representing a number 1 through 13 

    The responsibility of Card is to hold a value to be represented when drawn.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    # 3) Create the roll(self) method. Use the following method comment.
    def draw(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)