# Mancala, by Al Sweigart

def drawBoard(board):
    b = board # Using a shorter variable name.
    print("""
                <-<-<-<-<
+----+----+----+----+----+----+----+----+
|2   |G   |H   |I   |J   |K   |L   |1   |
|    | %s | %s | %s | %s | %s | %s |    |
|    |    |    |    |    |    |    |    |
| %s +----+----+----+----+----+----+ %s |
|    |A   |B   |C   |D   |E   |F   |    |
|    | %s | %s | %s | %s | %s | %s |    |
|    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+
                >->->->->
""" % (sp(b['G']), sp(b['H']), sp(b['I']), sp(b['J']), sp(b['K']), sp(b['L']), sp(b['2']), sp(b['1']), sp(b['A']), sp(b['B']), sp(b['C']), sp(b['D']), sp(b['E']), sp(b['F'])))


def sp(number):
    # Adds a space if needed to make the number take up two chracters.
    return str(number).rjust(2)


def getNewBoard():
    board = {'1': 0, '2': 0}
    for i in 'ABCDEFGHIJKL':
        board[i] = 4
    return board


def getPlayerMove(board, turn):
    drawBoard(board)
    move = None
    while True:
        if turn == '1':
            print('Player 1, choose move: A-F')
        elif turn == '2':
            print('Player 2, choose move: G-L')
        move = input().upper()

        if (turn == '1' and move not in 'ABCDEF') or (turn == '2' and move not in 'GHIJKL') or (move == ''):
            print('Please pick a letter on your side of the board.')
            continue
        if board.get(move) == 0:
            print('Please pick a non-empty pocket.')
            continue
        return move


def makeMove(board, turn, move):
    POCKETS = 'ABCDEF1LKJIHG2'
    toSow = board[move] # Get number of seeds from selected pocket.
    board[move] = 0 # Empty out the selected pocket.

    while toSow > 0:
        move = POCKETS[(POCKETS.index(move) + 1) % 14] # Next pocket.
        if (turn == '1' and move == '2') or (turn == '2' and move == '1'):
            continue # Skip opponent's mancala.
        board[move] += 1 # Add one seed to the pocket.
        toSow -= 1 # Decrease one seed from toSow.

    if move == '1' or move == '2':
        return 'one more turn' # Last sow in player's mancala; take another turn.

    # Check if last sow was in an empty pocket; take opposite pocket's seeds.
    if (turn == '1' and move in 'ABCDEF' and board[move] == 1):
        oppositePocket = 'GHIJKL'['ABCDEF'.index(move)]
        board['1'] += board[oppositePocket]
        board[oppositePocket] = 0
    elif (turn == '2' and move in 'GHIJKL' and board[move] == 1):
        oppositePocket = 'ABCDEF'['GHIJKL'.index(move)]
        board['2'] += board[oppositePocket]
        board[oppositePocket] = 0
    return 'done'


def checkForWinner(board):
    b = board # Just to get a shorter variable name.

    if b['1'] > 24:
        return '1'
    if b['2'] > 24:
        return '2'

    if (b['A'] == 0 and b['B'] == 0 and b['C'] == 0 and b['D'] == 0 and b['E'] == 0 and b['F'] == 0) or \
       (b['G'] == 0 and b['H'] == 0 and b['I'] == 0 and b['J'] == 0 and b['K'] == 0 and b['L'] == 0):
        # Game is over, find player with largest score.
        player1Score = b['A'] + b['B'] + b['C'] + b['D'] + b['E'] + b['F']
        player2Score = b['G'] + b['H'] + b['I'] + b['J'] + b['K'] + b['L']

        if player1Score > player2Score:
            return '1'
        elif player2Score > player1Score:
            return '2'
        else:
            return 'tie'
    return 'no winner'


def runGame():
    gameBoard = getNewBoard()
    playerTurn = '1'

    while True:
        playerMove = getPlayerMove(gameBoard, playerTurn)

        nextAction = makeMove(gameBoard, playerTurn, playerMove)
        if nextAction != 'one more turn':
            if playerTurn == '1':
                playerTurn = '2'
            elif playerTurn == '2':
                playerTurn = '1'

        winner = checkForWinner(gameBoard)
        if winner in '12':
            print('Player %s has won!' % (winner))
            break
        elif winner == 'tie':
            print('There is a tie!')
            break

if __name__ == '__main__':
    runGame()