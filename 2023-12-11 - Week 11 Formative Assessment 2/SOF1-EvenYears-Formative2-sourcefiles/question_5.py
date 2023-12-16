class Blotris:
    """A game board, comprised of spaces - rows and columns, which can
      have shapes placed onto it, with full rows being cleared, and
      other rows subsequently being shifted down.
    """


    def __init__(self, rows, cols):
        """Initiate the board with a given amount of rows and columns."""
        if (rows < 5 or cols < 5):
            raise ValueError("Rows, or cols is not greater or equal to 5")
        self._board = [[0 for _ in range(cols)] for _ in range(rows)]
        self._rows = rows
        self._cols = cols

    def __str__(self):
        """Print a clear representation of the board."""
        build = ""
        for row in self._board:
            build += str(row).replace(',', '') + "\n"
        return build

    def add(self, shape, row, col):
        """Adds a shape to the game board, with it's first index
        starting from the top-left (row, col)

        Args:
            shape (list): a 2D list, 0- empty block, 1- occupied block
            row (int): the row to place the top-left of the shape from
            col (int): the column to place the top-left of the shape
        """

        # Check if the shape can be placed
        if (row < 0 or col < 0):  # Wont cause an error, but disallowed
            return False
        currentrow = row
        for rowline in shape:
            currentcol = col
            if (currentrow + 1 > self._rows):  # Check out of index
                return False
            for colline in rowline:
                if (currentcol + 1 > self._cols):  # Check out of index
                    return False
                if (colline == 1 and
                    self._board[currentrow][currentcol] == 1):
                        return False
                currentcol += 1
            currentrow += 1

        # Actually place the shape
        currentrow = row
        for rowline in shape:
            currentcol = col
            for colline in rowline:
                if (colline == 1 and
                    self._board[currentrow][currentcol] == 0):
                        self._board[currentrow][currentcol] = 1
                currentcol += 1
            currentrow += 1

        return True

    def update(self):
        """Check if a line (row) of the board is fully occupied, if it is
        clear it and shift all other rows down, all lines are checked, so
        multiple shifts can happen in one call (recursively).
        """
        for i in range(self._rows - 1, -1, -1):
            if (all(self._board[i])):
                del(self._board[i])
                self._board.insert(0, [0 for _ in range(self._cols)])
                self.update()  # Start this process again for other lines
