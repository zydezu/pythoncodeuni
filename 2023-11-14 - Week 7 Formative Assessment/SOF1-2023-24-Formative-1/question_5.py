def molecule_to_list(molecule):
    molecule_list = []
    if (not molecule[0].isalpha()):
        return None
    for i in range(len(molecule)):
        if not molecule[i].isalpha():
            return None
        if not molecule[i].isupper():
            return None
        
        if molecule[i+1].isalpha(): #Ca

            if molecule[i+1].isupper():
                molecule_list.append((molecule[i], 1))
            else:
                molecule_list.append((molecule[i] + molecule[i+1], 
                                 molecule[i+2]))
            i+=2
        elif molecule[i+1].isnumeric():
            molecule_list.append((molecule[i], molecule[i+1]))
            i+=1
        else:
            molecule_list.append((molecule[i], molecule[i+1]))