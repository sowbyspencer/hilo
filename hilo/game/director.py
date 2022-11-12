from game.card import Card

#Variables for formatting
green = "\033[1;32;40m"
default = "\033[0;37;40m"
yellow = "\033[1;33;40m"
red = "\033[1;31;40m"

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: A card with a possible value of 1 through 13
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        print(f"{red}RED")
        self.is_playing = True
        self.total_points = 300
        self.turns = 0

        self.card1 = Card()
        self.card2 = Card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.drawCards()
            
            #Display card values and get input from the user
            print(f"{default}\nThe card is: {yellow}{self.card1.value}")
            guess = self.getUserInput()
            print(f"{default}Next card is: {yellow}{self.card2.value}{default}")

            #Update the score based on the users guest
            self.updateScore(guess)
            self.turns += 1

            #Check points to see if the game should end
            if self.total_points <= 0:
                print(f"{red}GAME OVER{default}")
                print(f"You took one too many chances.")
                self.is_playing = False
            else:
                #Input validation
                play = ""
                while not play in ["y","n"]:
                    play = self.is_playing = input(f"{default}Play again? [y/n]: {green}")
                    if not play in ["y", "n"]:
                        print(f"{default}Input not valid.")
                
                # If user selected "n" end the game.
                self.is_playing = play == "y"
                if not self.is_playing:
                    print(f"{default}\nThanks for playing. You final score is: {yellow}{self.total_points}{default}")
        
    def drawCards(self): 
        """Draws (randomly generates a card)
    
        Parameter(s)
            crd: none
        Return: card: none
        """
        # If it is the first turn draw the first card
        if self.turns == 0:
            self.card1.draw()
        #Else set the value of the firsr card to the second card
        else:
            self.card1.value = self.card2.value
        #Draw the second card
        self.card2.draw()
    
    def getUserInput(self): 
        """Gets the Hi/Low guess from the user
    
        Parameter(s)
            : none
        Return: hiLow: the users gues if the next card will be higher or lower.
        """
        #Input validation
        hiLow = ""
        while not hiLow in ["h", "l"]:
            hiLow = input(f"{default}Higher or lower? [h/l]: {green}")
            if not hiLow in ["h", "l"]:
                print(f"{default}Input not valid.")
        return hiLow
    
    def updateScore(self, guess): 
        """Determins the points based on the user guess. If they were correct points go up 100 points.
        If they guessed wrong their points go down 75 points. It then displays the updated score.
    
        Parameter(s)
            guess: the user's guess
        Return: none
        """
        #Check the cards against each other
        diff = self.card1.value - self.card2.value
        if diff > 0:
            hiLow = "l"
        elif diff < 0:
            hiLow = "h"
        else:
            hiLow = "n"

        #Set Points
        if guess == hiLow:
            self.total_points += 100
        else:
            self.total_points -= 75

        #Print score
        print(f"{default}Your score is: {yellow}{self.total_points}")