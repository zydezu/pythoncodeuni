def rasterise(list_1d, width):    
    try:
        if len(list_1d) % width != 0:
            print("width is not a multiple of the length of list_1d!")
            return None
    except ZeroDivisionError:
        print("tried to divide by 0... so width is not a multiple of the "
              "length of list_1d!")
        return None
    if width < 1:
        print("Width too small!")
        return None
    list_2d = []

    count = 0
    for item in list_1d:
        if count % width == 0:
            list_2d.append([])  # Every width items, made a new inner list object
        list_2d[count // width].append(item)  # determines what index to place the current item in
        count += 1

    return list_2d


print(rasterise([1, 2, 3, 4, 5, 6, 7, 8], 4))