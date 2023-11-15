def molecule_to_list(molecule):
    """Takes in a string, representing a list of molecules, and
    outputs a list of tuples, each representing an element and its
    quantity in the compound.

    Args:
        molecule (string): a string representing molecules and their 
        quantities, represented by characters and numbers

    Returns:
        list[tuple]: a list of tuples, with each tuple containing 
        the element and its quantity
    """
    molecule_list = []
    
    char_num = 0
    current_atom = ""
    current_number = ""

    for i in range(len(molecule)):
        if char_num == 0 and not molecule[i].isupper():
            return None
        if not molecule[i].isalnum():
            return None
        
        if char_num == 0: #Get first character of element
            char_num += 1
            current_atom += molecule[i]
        elif char_num == 1: #Check if second character is a new element
            if molecule[i].isupper(): #eg: CO
                molecule_list.append((current_atom, 1))
                char_num = 1
                current_atom = molecule[i]
            elif molecule[i].isnumeric(): #eg: C6
                current_number = str(molecule[i])
                if (i+1 < len(molecule)): #Check if last index of string
                    if (molecule[i+1].isnumeric()):
                        current_number += str(molecule[i+1])
                        char_num = 4

                if char_num != 4:
                    molecule_list.append((current_atom, 
                                          int(current_number)))
                    char_num = 0
                    current_atom = ""
                    current_number = ""
            else: #eg: Ca
                current_atom += molecule[i]
                char_num =+ 1
        elif char_num == 2: #Check elements with two letters
            if molecule[i].isupper(): #eg: CaC
                molecule_list.append((current_atom, 1))
                char_num = 0
                current_atom = ""
            elif molecule[i].isnumeric(): #eg: Ca3
                current_number = str(molecule[i])
                if (i+1 < len(molecule)): #Check if last index of string
                    if (molecule[i+1].isnumeric()):
                        current_number += str(molecule[i+1])
                        char_num = 4

                molecule_list.append((current_atom, 
                                      int(current_number)))
                char_num = 0
                current_atom = ""
                current_number = ""
            else:
                return None
        elif char_num == 4: #get second number in element
            molecule_list.append((current_atom, 
                                  int(current_number)))
            char_num = 0
            current_atom = ""
            current_number = ""

    if len(current_atom) > 0: #add last element
        molecule_list.append((current_atom, 1))

    return molecule_list