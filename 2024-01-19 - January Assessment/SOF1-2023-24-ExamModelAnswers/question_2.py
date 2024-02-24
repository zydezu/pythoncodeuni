def shrink(signal, element):
    """Shrinks a one dimensional binary signal using a structural element.

    Args:
        signal (list[int]): a list of int repressenting a one dimensional 
            binary signal composed of 1s and 0s
        element (list[int]): a one dimensional list of int composed of 1s
            and smaller than the signal.

    Returns:
        list[int]: a one dimensional binary signal composed of 1s and 0s. 
            The result is a shrinked version of the original signal.
    """
    filtered = [0] * len(signal)
    for i in range(len(signal)):
        keep = True
        for j in range(i, min(i + len(element), len(signal))):
            if signal[j] == 0:
                keep = False
        if keep:
            filtered[i] = 1
    return filtered


def expand(signal, element):
    """Expands a one dimensional binary signal using a structural element.

    Args:
        signal (list[int]): a list of int repressenting a one dimensional 
            binary signal composed of 1s and 0s
        element (list[int]): a one dimensional list of int composed of 1s
            and smaller than the signal.

    Returns:
        list[int]: a one dimensional binary signal composed of 1s and 0s. 
            The result is an expanded version of the original signal.
    """
    filtered = [0] * len(signal)
    for i in range(len(signal)):
        for j in range(i, min(i + len(element), len(signal))):
            if signal[j] == 1:
                filtered[i] = 1
                break
    return filtered


def denoise(signal, element):
    """Denoises a one dimensional binary signal using a structural element.

    Removing noise from the signal is done by first shrinking and then 
    expanding the signal.

    Args:
        signal (list[int]): a list of int repressenting a one dimensional 
            binary signal composed of 1s and 0s
        element (list[int]): a one dimensional list of int composed of 1s
            and smaller than the signal.

    Returns:
        list[int]: a one dimensional binary signal composed of 1s and 0s.
            The result is a denoised version of the original signal.
    """
    ## Note that a docstring is necessay here to inform user of the API for
    ## this module. If you have used a lambda expression without a docstring
    ## instead you will lose marks in the docstring part of the assessment.
    return expand(shrink(signal, element), element)
        