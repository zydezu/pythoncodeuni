def trick_score(trick, trump_suit):
    """Calculate the score of a trick, within a set of four cards,
    whether a card is in the trump_suit or not will influence it's
    value

    Args:
        trick (set(tuple(string, string))): a set, with four cards 
        (tuples with the card's rank and suit) in it
        trump_suit (string): which suit is the trump suit

    Raises:
        ValueError: raised if the trick doesn't have exactly four cards
        TypeError: raised if the trump_suit isn't valid
        ValueError: raised if the rank in the card tuple, in the trick 
        set, isn't valid
        ValueError: raised if the suit in the card tuple, in the trick 
        set, isn't valid

    Returns:
        int: returns the sum of the score of all the cards
    """
    valid_ranks = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    valid_suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

    trick_card_values = {"Jack": 20, "9": 14, "Ace": 11, "10": 10,
                          "King": 4, "Queen": 3, "8": 0, "7": 0}
    card_values = {"Ace": 11, "10": 10, "King": 4, "Queen": 3,
                    "Jack": 2, "9": 0, "8": 0, "7": 0}

    if (len(trick) != 4):
        raise ValueError(f"{trick} doesn't have exactly four cards")
    if not trump_suit in valid_suits:
        raise TypeError(f"{trump_suit} is not a valid suit")

    score = 0
    for card in trick:
        rank, suit = card[0], card[1]
        if not rank in valid_ranks:
            raise ValueError(f"{rank} is not a valid rank")
        if not suit in valid_suits:
            raise ValueError(f"{suit} is not a valid suit")

        score += (trick_card_values[rank] if (suit == trump_suit) 
                  else card_values[rank])
    return score