import math


def track_points(time, eventParameters):
    """Calculate the score of an athlete in a track event.

    Args:
        time (float): the athlete's time in seconds
        eventParameters (tuple): a tuple containing 3 items - the
        event's parameters

    Raises:
        ValueError: raised if eventParameters doesn't have
        exactly 3 values

    Returns:
        int: the athletes score (rounded down)
    """
    if (len(eventParameters) != 3):
        raise ValueError("eventParameters doesn't have three values")

    points = (eventParameters[0]
              * pow((eventParameters[1] - time), eventParameters[2]))

    if isinstance(points, complex):  # imaginary number
        points = 0

    if (points < 0):
        points = 0

    return math.floor(points)
