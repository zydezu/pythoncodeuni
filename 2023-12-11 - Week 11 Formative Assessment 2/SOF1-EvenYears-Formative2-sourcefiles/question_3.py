def read_from_file(filename):
    """Reads files with times of athletes, returns data in a dictionary.

    Args:
        filename (string): the filename of the data to read

    Raises:
        ValueError: raised if the text file format isn't correct (there
        being too many or too few fields)

    Returns:
        dictionary: athelete's names as keys, with values being dicts of
        athletes times, keys being "200m", "800m" or "110m" and values
        being the corresponding times
    """
    data = dict()

    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if line[0] == '#':
            pass
        else:
            # name, 200m split, 110m split, 800m split
            athlete_data = line.strip().split(', ')
            if (len(athlete_data) != 4):
                raise ValueError("File format is incorrect")
            data[athlete_data[0]] = dict({'200m': float(athlete_data[1]),
                                          '800m': float(athlete_data[3]),
                                          '110m': float(athlete_data[2])})
    return data
