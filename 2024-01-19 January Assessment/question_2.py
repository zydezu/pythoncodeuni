def shrink(signal, element):
    """Shrinks the signal, by manipulating the binary elements of signal,
    and matching each binary digital against the structuring element

    Args:
        signal (list): the binary signal to be modified
        element (list): the structuring element, used to shrink the
        signal, if all the values from signal- corresponding to
        element- match, 1 will be outputted in the result, if not, 0
        will be outputted

    Returns:
        list: the shrunk signal
    """
    output = [0 for x in range(len(signal))]
    for i in range(len(signal)):
        checking_block = signal[i:i+len(element)]
        # Incase checking_block is smaller than element, eg: [1] vs [1,1]
        if checking_block == element[:len(checking_block)]:
            output[i] = 1
    return output

def expand(signal, element):
    """Expands the signal, by manipulating the binary elements of signal,
    and matching each binary digital against the structuring element

    Args:
        signal (list): the binary signal to be modified
        element (list): the structuring element, used to expand the
        signal, if one of the values from signal- corresponding to
        element- match, 1 will be outputted in the result, if not, 0
        will be outputted

    Returns:
        list: the expanded signal
    """
    output = [0 for x in range(len(signal))]
    for i in range(len(signal)):
        for j in range(len(element)):
            if i + j < len(signal):
                if signal[i + j] == element[j]:
                    output[i] = 1
                    break
    return output

def denoise(signal, element):
    """Shrinks the signal, then expands that resulting signal,
    resulting in a denoised signal

    Args:
        signal (list): the binary signal to be modified
        element (list): the structuring element, used to shrink
        or expand the binary signal based on what 0s and 1s match

    Returns:
        list: the denoised signal
    """
    data = shrink(signal, element)
    return expand(data, element)