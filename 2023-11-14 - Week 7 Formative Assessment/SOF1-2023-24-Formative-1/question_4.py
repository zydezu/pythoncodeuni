def encrypt(message, shifts, alphabet):
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