import copy

class GameObject:
    """
    The pieces in the board game, consisting of a shape and colour,
    this class is used in GameCard (in pairs) or in CardDeck as
    wooden pieces
    """
    def __init__(self, shape, colour):
        self._shape = shape
        self._colour = colour

    @property
    def shape(self):
        return self._shape

    @property
    def colour(self):
        return self._colour

    def __eq__(self, other):
        try:
            if (self._shape == other._shape 
                and self._colour == other._colour):
                return True
            return False
        except:
            return False
    
class GameCard:
    """
    Consists of two GameObjects, as two different
    objects are displayed on a card in the game
    """
    def __init__(self, object1, object2):
        self._content = [object1, object2]

    @property
    def content(self):
        content_copy = copy.deepcopy(self._content)
        return content_copy
    
    def __eq__(self, other):
        try:
            if (self._content[0] == other._content[0] 
                or self._content[0] == other._content[1]):
                if (self._content[1] == other._content[0] 
                    or self._content[1] == other._content[1]):
                    return True
            return False
        except:
            return False

class CardDeck:
    """
    The overall board game, with objects in the middle of the table
    to 'grab' (the wooden pieces)-object_list. This class also
    generates the possible cards allowed in a game, based of those
    wooden pieces
    """
    def __init__(self, object_list):
        length = len(object_list)
        if length < 3 and length > 5:
            raise ValueError(f"The list has {len(object_list)} objects")
        
        self._unique_shapes, self._unique_colours = set(), set()

        for object in object_list:
            if (object.shape in self._unique_shapes 
                or object.colour in self._unique_colours):
                raise ValueError("Objects have the same shape or color")

            self._unique_shapes.add(object.shape)
            self._unique_colours.add(object.colour)

        self._object_list = object_list

    def generate_deck(self):
        game_cards = []

        # get a list of all the possible cards, based on unique properties
        potential_cards = []
        for shape in self._unique_shapes:
            for colour in self._unique_colours:
                potential_cards.append((shape, colour))

        for card in potential_cards:
            for other_card in potential_cards:
                if not card == other_card:
                    samecount = 0
                    for object in self._object_list:
                        if (card == (object.shape, object.colour)):
                            samecount += 1
                    for object in self._object_list:
                        if (other_card == (object.shape, object.colour)):
                            samecount += 1
                    if samecount == 1:
                        # print(f"(<{card},{other_card}>)")
                        first_object = GameObject(card[0], card[1])
                        second_object = GameObject(other_card[0], other_card[1])
                        new_card = GameCard(first_object, second_object)
                        game_cards.append(new_card)
                    elif samecount == 0:
                        for item in self._object_list:
                            if (card[0] == item.shape):
                                break
                            elif (card[1] == item.colour):
                                break
                            elif (other_card[0] == item.shape):
                                break
                            elif (other_card[1] == item.colour):
                                break
                            else:
                                first_object = GameObject(card[0], card[1])
                                second_object = GameObject(other_card[0], other_card[1])
                                new_card = GameCard(first_object, second_object)
                                game_cards.append(new_card)