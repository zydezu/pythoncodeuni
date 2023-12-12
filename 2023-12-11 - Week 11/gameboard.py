class Board:
    def __init__(self):
        self.PLAYER1 = 1
        self.PLAYER2 = 2
        self._board = [[0 for x in range(7)] for x in range(6)]
        
    def __str__(self):
        build = ""
        for row in self._board:
            build += "\n+---+---+---+---+---+---+---+\n|"
            for item in row:
                symbol = ("." if item == 0 else 
                          ("O" if item == self.PLAYER1 else 
                           "X" if item == self.PLAYER2 else
                           "error"))
                build += f" {symbol} |"
            
        build += "\n+===+===+===+===+===+===+===+\n|"
        for item in range(7):
            build += f" {item} |"
        build += "\n+---+---+---+---+---+---+---+\n"
        return build
    
    def __repr__(self) -> str:
        build = ""
        for row in self._board:
            build += str(row).replace(',', '') + "\n"
        return build
    
    def get_move(self, move: int, player: int):
        assert player == self.PLAYER1 or player ==self.PLAYER2, "Invalid player"
        for checkingRow in range(5, -1, -1):
            currentSquare = self._board[checkingRow][move]
            if (currentSquare == 0):
                self._board[checkingRow][move] = player
                return
        raise IndexError("This column is full!")
    
    def get_valid_moves(self) -> list:
        valid_moves = []
        for i in range(0, 7):
            if (self._board[0][i] == 0):
                valid_moves.append(i)
        return valid_moves
            
    def iswinner(self, player):
        for i in range(0, 6):
            for j in range(0, 7):
                # i row
                # j column
                currentSquare = self._board[i][j]
                if (currentSquare == player):
                    if (i < 3): # |
                        if (currentSquare == player and
                            self._board[i+1][j] == player and
                            self._board[i+2][j] == player and
                            self._board[i+3][j] == player):
                            return True
                    
                    if (j < 4): # -
                        if (currentSquare == player and
                            self._board[i][j+1] == player and
                            self._board[i][j+2] == player and
                            self._board[i][j+3] == player):
                            return True
                        
                    if (i > 3 and j < 4): # /
                        if (currentSquare == player and
                            self._board[i-1][j+1] == player and
                            self._board[i-2][j+2] == player and
                            self._board[i-3][j+3] == player):
                            return True
                        
                    if (i < 3 and j < 4): # \
                        if (currentSquare == player and
                            self._board[i+1][j+1] == player and
                            self._board[i+2][j+2] == player and
                            self._board[i+3][j+3] == player):
                            return True
                             
gameboard = Board()
playerTurn = 1

while(True):
    validMoves = gameboard.get_valid_moves()
    print(repr(gameboard))
    print(gameboard)
    if (gameboard.iswinner(playerTurn)):
        break
    print(f"Player {playerTurn}, place a piece!")
    selection = "-999"
    
    while (not selection in validMoves):
        selection = int(input("Enter the row to place your piece > "))
        if (not selection in validMoves):
            print("Invalid selection!")
            
    gameboard.get_move(selection, playerTurn)
    
    playerTurn = 2 if (playerTurn == 1) else 1
    
print(f"{playerTurn} won!")