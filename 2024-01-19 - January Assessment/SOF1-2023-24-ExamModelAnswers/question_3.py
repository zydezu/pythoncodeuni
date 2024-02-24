from typing import Tuple, Set

def trick_score(trick: Set[Tuple[str,str]], trump_suit: str) -> int:
    """Returns the score of a trick given a trump suit.

    A trick is a set of exactly four cards, and card is a tuple (rank, suit) of
    two strings where rank is one of the value in {"7", "8", "9", "10", "Jack", 
    "Queen", "King", "Ace"} and suit is one of the value in {"Diamonds", 
    "Spades", "Hearts", "Clubs"}.

    Args:
        trick (Set[Tuple[str,str]]): The set of cards contained in the trick.
        trump_suit (str): the trupm suit for that game.

    Raises:
        ValueError: if the trick does not have exactly four cards or if a card
            in the trick is not a valid card.
        TypeError: if trump_suit is not a valid suit.

    Returns:
        int: The score of the trick.
    """
    ## Although it was not requested in the paper, the use of type annotation
    ## within docstrings and the code as shown here was accepted.

    ## Here I used three local variables card_points, trump_points and suits.
    ## Alternatively you could have defined three constants outside the
    ## function. However, you have lost marks if you declareed three global
    ## variables instead.
    ## Note also that I do not provide comments for the three varaibles
    ## card_points, trump_points, suits as teh code provide sufficient
    ## details and is self explanatory.
    card_points = {"7":0, "8":0, "9":0, "10":10,
                   "Jack":2, "Queen":3, "King":4, "Ace":11}
    trump_points = {"7":0, "8":0, "9":14, "10":10,
                    "Jack":20, "Queen":3, "King":4, "Ace":11}
    suits = {"Diamonds", "Spades", "Hearts", "Clubs"}

    if len(trick) != 4:
        raise ValueError("Invalid trick size.")
    if trump_suit not in suits:
        raise TypeError("Invalid suits.")
    score = 0
    for rank, suit in trick:
        if suit not in suits or rank not in card_points:
            raise ValueError("Invalid card.")
        if suit == trump_suit:
            score += trump_points[rank]
        else:
            score += card_points[rank]
    return score
