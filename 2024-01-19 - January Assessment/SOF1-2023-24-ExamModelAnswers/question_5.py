from copy import deepcopy

class GameObject:
    """Class representing an wooden piece for the game "bazar bizzare".

    Attributes:
        shape (str): The shape of the wooden piece, for example a "chair".
        colour (str): The colour of the wooden piece, for example "red".
    """
    def __init__(self, shape, colour) -> None:
        self._shape = shape
        self._colour = colour

    def __str__(self) -> str:
        return f'<{self.shape}, {self.colour}>'

    def __repr__(self) -> str:
        return f"GameObject('{self._shape}', '{self._colour}')"

    @property
    def shape(self):
        """The shape of the wooden piece, for example a "chair".
        """
        return self._shape

    @property
    def colour(self):
        """The colour of the wooden piece, for example "red"."""
        return self._colour

    def __eq__(self, other):
        if not isinstance(other, GameObject):
            return False
        return self.shape == other.shape and self.colour == other.colour

    def __ne__(self, other: object) -> bool:
        return not other == self


class GameCard:

    def __init__(self, object1, object2) -> None:
        self._content = [object1, object2]

    def __str__(self) -> str:
        return f'({self.content[0]}, {self.content[1]})'

    def __repr__(self) -> str:
        return f"GameCard({repr(self._content[0])}, {repr(self._content[1])})"

    @property
    def content(self):
        return deepcopy(self._content)

    def __eq__(self, other):
        if not isinstance(other, GameCard):
            return False
        return ((self.content[0], self.content[1])== (other.content[0], other.content[1])
                or (self.content[0], self.content[1]) == (other.content[1], other.content[0]))

    def __ne__(self, other: object) -> bool:
        return not other == self


class CardDeck:

    def __init__(self, game_objects) -> None:
        if len(game_objects) not in [3, 4, 5]:
            raise ValueError('Invalid number of objects!')
        self._shapes = list({obj.shape for obj in game_objects})
        self._colours = list({obj.colour for obj in game_objects})
        if (len(game_objects) != len(self._shapes)
                or len(game_objects) != len(self._colours)):
            raise ValueError('Duplicate colour or shape not allowed.')
        self._objects = game_objects.copy()
        self._cards = {str(obj):list() for obj in self._objects}

    def __str__(self) -> str:
        return '{'+ ', '.join(map(str,self._objects)) + '}'

    def __repr__(self) -> str:
        return str(self)

    def _isvalid(self, card:GameCard) -> bool:
        """Returns True if the card is a valid card for the game "Bazar Bizare".

        A card is valid if it satisfies all the following conditions:
            - The two wooden pieces on the card do not have the same shape or
              colour
            - The shape and colour of the wooden pieces on the card are one of 
              the colour and shape used for the game.
            - Only one wooden piece can be infered from the two pieces on the 
              card. 

        Args:
            card (GameCard): The card to be considered.

        Returns:
            bool: True if the cards satisfies all the condition previously 
                described, False otherwise. 
        """
        object1, object2 = card.content
        # The two pieces on a card cannot have the same shape or colour.
        if object1.shape == object2.shape or object1.colour == object2.colour:
            return False
        # The two pieces on a card cannot both be a valid wooden piece.
        if object1 in self._objects and object2 in self._objects:
            return False
        elif object1 in self._objects or object2 in self._objects:
            return True
        possible_pick = [] # The list of wooden pieces that can be infered
        for game_object in self._objects:
            # an infered wooden piece cannot have the shape or colour of the
            # pieces on the card.
            if not (game_object.shape in (object1.shape,object2.shape)
                or game_object.colour in (object1.colour, object2.colour)):
                possible_pick.append(game_object)
        if len(possible_pick) == 1:
            return True

        return False


    def generate_deck(self):
        deck = []
        # Generate all possible combinations of the first wooden piece
        for shape1 in self._shapes:
            for colour1 in self._colours:
                for shape2 in self._shapes:
                    # Generate all possible combinations of the second
                    # wooden pieces
                    for colour2 in self._colours:
                        card = GameCard(GameObject(shape1, colour1),
                                        GameObject(shape2, colour2))
                        # If the two wooden pieces built make a valid card
                        # and the card is not already in the deck, then it
                        # should be added to the deck.
                        if self._isvalid(card) and card not in deck:
                            deck.append(card)
        return deck
