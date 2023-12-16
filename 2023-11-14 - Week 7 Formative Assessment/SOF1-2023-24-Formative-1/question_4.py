def encrypt(message, shifts, alphabet):
    """A modified version of the Caesar cipher, it encrypts the message,
    by shifting each character by the amount representing in the list 
    shifts, using an custom alphabet. 

    Args:
        message (string): the message about to be encrypted
        shifts (list): an array of ints, representing the amount each 
        character should be shifted by 
        alphabet (string): the alphabet that is used to set and 
        shift characters

    Returns:
        string: the encrypted message
    """

    new_message = ""
    if len(message) != len(shifts):
        return None
    for i in range(len(message)):
        current_char = message[i]
        if current_char not in alphabet:
            return None
        current_shift = shifts[i]
        if current_shift < 0 or current_shift >= len(alphabet):
            return None
        new_char = alphabet[(alphabet.index(current_char) 
                             + current_shift) % len(alphabet)]
        new_message += new_char
    return new_message