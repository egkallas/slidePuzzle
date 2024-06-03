# Puzzle Piece Class for a 3x3 puzzle

from enum import Enum

class Direction(Enum): # Enum class to represent the four moveableDirections a piece can move in
    Left = 'Left'
    Right = 'Right'
    Up = 'Up'
    Down = 'Down'



# Initializing puzzle pieces and their attributes

class puzzlePiece:
    def __init__(self, row, col, isEmptySpace = False, isAdjacentToEmptySpace = False, canMoveLeft = False, canMoveRight = False, canMoveUp = False, canMoveDown = False, moveableDirections = []):
        self.row = row
        self.col = col
        self.isEmptySpace = isEmptySpace
        self.isAdjacentToEmptySpace = isAdjacentToEmptySpace
        self.canMoveLeft = canMoveLeft
        self.canMoveRight = canMoveRight
        self.canMoveUp = canMoveUp
        self.canMoveDown = canMoveDown
        self.moveableDirections = moveableDirections

topLeftCorner = puzzlePiece(1, 1, False, False, False, False, False, False, [])
topMiddle = puzzlePiece(1, 2, False, False, False, False, False, False, [])
topRightCorner = puzzlePiece(1, 3, False, False, False, False, False, False, [])
middleLeft = puzzlePiece(2, 1, False, False, False, False, False, False, [])
trueMiddle = puzzlePiece(2, 2, False, False, False, False, False, False, [])
middleRight = puzzlePiece(2, 3, False, False, False, False, False, True, [])
bottomLeftCorner = puzzlePiece(3, 1, False, False, False, False, False, False, [])
bottomMiddle = puzzlePiece(3, 2, False, False, False, True, False, False, [])
bottomRightCorner = puzzlePiece(3, 3, True, None, True, False, True, False, [])

# Function to determine if a piece is adjacent to the empty space for movement logic

def isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece):
    if((targetPiece.isEmptySpace != True) or (pieceChecking.isEmptySpace != False)): # This line contains two basic checks to make sure valid parameters are being fed in. (i.e. there is actually something to check)
        return False
    if((pieceChecking.row == targetPiece.row) and (pieceChecking.col == targetPiece.col)): # If the two pieces fed in are in fact the same piece, there is no adjacency to check
        return False
    elif((pieceChecking.row + 1 == targetPiece.row) and (pieceChecking.col == targetPiece.col) and (targetPiece.isEmptySpace == True)): # If the piece is above the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True
        return True, (targetPiece.row, targetPiece.col)
    elif((pieceChecking.row - 1 == targetPiece.row) and (pieceChecking.col == targetPiece.col) and (targetPiece.isEmptySpace == True)): # If the piece is below the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True
        return True, (targetPiece.row, targetPiece.col)
    elif((pieceChecking.col + 1 == targetPiece.col) and (pieceChecking.row == targetPiece.row) and (targetPiece.isEmptySpace == True)): # If the piece is to the right of the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True
        return True, (targetPiece.row, targetPiece.col)
    elif((pieceChecking.col - 1 == targetPiece.col) and (pieceChecking.row == targetPiece.row) and (targetPiece.isEmptySpace == True)): # If the piece is to the left of the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True
        return True, (targetPiece.row, targetPiece.col)
    else:
        pieceChecking.isAdjacentToEmptySpace = False
        return False
    
# Function to check if a piece can move left, right, up, or down

def canMove(pieceChecking, targetPiece):
    moveableDirections = []
    if((pieceChecking.row == targetPiece.row) and (pieceChecking.col == targetPiece.col)): # If the two pieces fed in are in fact the same piece, there are no movement possibilities to consider
        canMove = False
        return moveableDirections, 'pieceChecking and targetPiece are the same piece.'
    
    pieceChecking.isAdjacentToEmptySpace = isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece) # If the piece is not adjacent to the empty space, and the piece is not the empty piece, it cannot possibly move
    if((pieceChecking.isAdjacentToEmptySpace == False) or (pieceChecking.isEmptySpace != True)): # If the piece is not adjacent to the empty space, and the piece is not the empty space, it cannot possibly move/be moved
        return moveableDirections, 'pieceChecking is not adjacent to the empty space and/or the pieceChecking is not the empty space'
    
    else:
        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col > 1)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the leftmost column, it can move left
            if(pieceChecking.col - 1 == targetPiece.col): # If the piece under examination is in the second row, we must ensure that both the left and right movement branches don't evaluate to True.
                pieceChecking.canMoveLeft = True
                moveableDirections.append(Direction.Left)
        else:
            pieceChecking.canMoveLeft = False

        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col < 3)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the rightmost column, it can move right
            if(pieceChecking.col + 1 == targetPiece.col): # If the piece under examination is in the second row, we must ensure that both the left and right movement branches don't evaluate to True.
                pieceChecking.canMoveRight = True
                moveableDirections.append(Direction.Right)
        else:
            pieceChecking.canMoveRight = False
   
        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.col == targetPiece.col) and (pieceChecking.row > 1)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the topmost row, it can move up
            if(pieceChecking.row - 1 == targetPiece.row): # If the piece under examination is in the second column, we must ensure that both the up and down movement branches don't evaluate to True. 
                pieceChecking.canMoveUp = True
                moveableDirections.append(Direction.Up)
        else:
            pieceChecking.canMoveUp = False

        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.col == targetPiece.col) and (pieceChecking.row < 3)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the bottommost row, it can move down
            if(pieceChecking.row + 1 == targetPiece.row): # If the piece under examination is in the second column, we must ensure that both the up and down movement branches don't evaluate to True.
                pieceChecking.canMoveDown = True
                moveableDirections.append(Direction.Down)
        else:
            pieceChecking.canMoveDown = False

        if(pieceChecking.canMoveLeft or pieceChecking.canMoveRight or pieceChecking.canMoveUp or pieceChecking.canMoveDown):
            return True, 'The piece can move ', moveableDirections
        return False
    
# Function to calculate the new empty space that results from a move. Set new values for isAdjacentToEmptySpace and canMove values for each piece?

def calculateNewEmptySpaceAfterMove(pieceClickedOn, pieceBeingSwappedWith): # If a move is initiated, the empty space (pieceBeingSwappedWith) will move to the space occupied by pieceClickedOn. The empty space will then be in the space previously occupied by pieceClickedOn
    if((pieceClickedOn.row == pieceBeingSwappedWith.row) and (pieceClickedOn.col == pieceBeingSwappedWith.col)): # If the two pieces fed in are in fact the same, there are no movement possibilities to consider
        return 'The pieces are the same.'
    if(pieceBeingSwappedWith.isEmptySpace != True): # If the pieceBeingSwappedWith is not the empty space, pieceClickedOn cannot possibly take its place. In other words, the move is not possible
        return 'The pieceBeingSwappedWith is not the empty space.'
    if(pieceClickedOn.isEmptySpace == True): # If the pieceClickedOn is the empty space, the move is not possible
        return 'The pieceClickedOn is the empty space.'

    pieceCapableOfMoving = canMove(pieceClickedOn, pieceBeingSwappedWith) # Check if the two pieces are capable of swapping places
    
    if(pieceClickedOn.canMoveLeft == True or pieceClickedOn.canMoveRight == True or pieceClickedOn.canMoveUp == True or pieceClickedOn.canMoveDown == True): # If the two pieces are in fact capable of swapping (adjacency condition met), the pieces may swap places
        pieceSwapTemp = pieceClickedOn # Temporary variable to hold the pieceClickedOn piece
        pieceClickedOn = pieceBeingSwappedWith # The pieceClickedOn piece takes the place of pieceBeingSwappedWith
        pieceBeingSwappedWith = pieceSwapTemp # And pieceBeingSwappedWith takes the place of pieceClickedOn
        return(pieceSwapTemp.row, pieceSwapTemp.col) # Return the row and column of the (now) empty space
    
    else: # In any other case, the piece may not move
        return 'The pieces cannot be swapped.'
    

"""""

# TESTS BEGIN HERE
        
# isAdjacentToEmptySpace Tests:

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topLeftCorner' '\n')
        
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topMiddle))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, middleLeft))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, trueMiddle))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, middleRight))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topMiddle' '\n')

print(isAdjacentToEmptySpaceCheck(topMiddle, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddle, topMiddle))
print(isAdjacentToEmptySpaceCheck(topMiddle, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topMiddle, middleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddle, trueMiddle))
print(isAdjacentToEmptySpaceCheck(topMiddle, middleRight))
print(isAdjacentToEmptySpaceCheck(topMiddle, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddle, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(topMiddle, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(topRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topMiddle))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, middleLeft))
print(isAdjacentToEmptySpaceCheck(topRightCorner, trueMiddle))
print(isAdjacentToEmptySpaceCheck(topRightCorner, middleRight))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the middleLeft' '\n')

print(isAdjacentToEmptySpaceCheck(middleLeft, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(middleLeft, topMiddle))
print(isAdjacentToEmptySpaceCheck(middleLeft, topRightCorner))
print(isAdjacentToEmptySpaceCheck(middleLeft, middleLeft))
print(isAdjacentToEmptySpaceCheck(middleLeft, trueMiddle))
print(isAdjacentToEmptySpaceCheck(middleLeft, middleRight))
print(isAdjacentToEmptySpaceCheck(middleLeft, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(middleLeft, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(middleLeft, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the trueMiddle' '\n')

print(isAdjacentToEmptySpaceCheck(trueMiddle, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(trueMiddle, topMiddle))
print(isAdjacentToEmptySpaceCheck(trueMiddle, topRightCorner))
print(isAdjacentToEmptySpaceCheck(trueMiddle, middleLeft))
print(isAdjacentToEmptySpaceCheck(trueMiddle, trueMiddle))
print(isAdjacentToEmptySpaceCheck(trueMiddle, middleRight))
print(isAdjacentToEmptySpaceCheck(trueMiddle, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(trueMiddle, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(trueMiddle, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the middleRight' '\n')

print(isAdjacentToEmptySpaceCheck(middleRight, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(middleRight, topMiddle))
print(isAdjacentToEmptySpaceCheck(middleRight, topRightCorner))
print(isAdjacentToEmptySpaceCheck(middleRight, middleLeft))
print(isAdjacentToEmptySpaceCheck(middleRight, trueMiddle))
print(isAdjacentToEmptySpaceCheck(middleRight, middleRight))
print(isAdjacentToEmptySpaceCheck(middleRight, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(middleRight, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(middleRight, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomLeftCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topMiddle))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, middleLeft))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, trueMiddle))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, middleRight))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomMiddle' '\n')

print(isAdjacentToEmptySpaceCheck(bottomMiddle, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, topMiddle))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, middleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, trueMiddle))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, middleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(bottomMiddle, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topMiddle))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, middleLeft))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, trueMiddle))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, middleRight))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomMiddle))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomRightCorner))



# canMove Tests:

print('\n' 'Conducting canMove tests for the topLeftCorner' '\n')

print(canMove(topLeftCorner, topLeftCorner))
print(canMove(topLeftCorner, topMiddle))
print(canMove(topLeftCorner, topRightCorner))
print(canMove(topLeftCorner, middleLeft))
print(canMove(topLeftCorner, trueMiddle))
print(canMove(topLeftCorner, middleRight))
print(canMove(topLeftCorner, bottomLeftCorner))
print(canMove(topLeftCorner, bottomMiddle))
print(canMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topMiddle' '\n')

print(canMove(topMiddle, topLeftCorner))
print(canMove(topMiddle, topMiddle))
print(canMove(topMiddle, topRightCorner))
print(canMove(topMiddle, middleLeft))
print(canMove(topMiddle, trueMiddle))
print(canMove(topMiddle, middleRight))
print(canMove(topMiddle, bottomLeftCorner))
print(canMove(topMiddle, bottomMiddle))
print(canMove(topMiddle, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topRightCorner' '\n')

print(canMove(topRightCorner, topLeftCorner))
print(canMove(topRightCorner, topMiddle))
print(canMove(topRightCorner, topRightCorner))
print(canMove(topRightCorner, middleLeft))
print(canMove(topRightCorner, trueMiddle))
print(canMove(topRightCorner, middleRight))
print(canMove(topRightCorner, bottomLeftCorner))
print(canMove(topRightCorner, bottomMiddle))
print(canMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the middleLeft' '\n')

print(canMove(middleLeft, topLeftCorner))
print(canMove(middleLeft, topMiddle))
print(canMove(middleLeft, topRightCorner))
print(canMove(middleLeft, middleLeft))
print(canMove(middleLeft, trueMiddle))
print(canMove(middleLeft, middleRight))
print(canMove(middleLeft, bottomLeftCorner))
print(canMove(middleLeft, bottomMiddle))
print(canMove(middleLeft, bottomRightCorner))

print('\n' 'Conducting canMove tests for the trueMiddle' '\n')

print(canMove(trueMiddle, topLeftCorner))
print(canMove(trueMiddle, topMiddle))
print(canMove(trueMiddle, topRightCorner))
print(canMove(trueMiddle, middleLeft))
print(canMove(trueMiddle, trueMiddle))
print(canMove(trueMiddle, middleRight))
print(canMove(trueMiddle, bottomLeftCorner))
print(canMove(trueMiddle, bottomMiddle))
print(canMove(trueMiddle, bottomRightCorner))

print('\n' 'Conducting canMove tests for the middleRight' '\n')

print(canMove(middleRight, topLeftCorner))
print(canMove(middleRight, topMiddle))
print(canMove(middleRight, topRightCorner))
print(canMove(middleRight, middleLeft))
print(canMove(middleRight, trueMiddle))
print(canMove(middleRight, middleRight))
print(canMove(middleRight, bottomLeftCorner))
print(canMove(middleRight, bottomMiddle))
print(canMove(middleRight, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomLeftCorner' '\n')

print(canMove(bottomLeftCorner, topLeftCorner))
print(canMove(bottomLeftCorner, topMiddle))
print(canMove(bottomLeftCorner, topRightCorner))
print(canMove(bottomLeftCorner, middleLeft))
print(canMove(bottomLeftCorner, trueMiddle))
print(canMove(bottomLeftCorner, middleRight))
print(canMove(bottomLeftCorner, bottomLeftCorner))
print(canMove(bottomLeftCorner, bottomMiddle))
print(canMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomMiddle' '\n')

print(canMove(bottomMiddle, topLeftCorner))
print(canMove(bottomMiddle, topMiddle))
print(canMove(bottomMiddle, topRightCorner))
print(canMove(bottomMiddle, middleLeft))
print(canMove(bottomMiddle, trueMiddle))
print(canMove(bottomMiddle, middleRight))
print(canMove(bottomMiddle, bottomLeftCorner))
print(canMove(bottomMiddle, bottomMiddle))
print(canMove(bottomMiddle, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomRightCorner' '\n')

print(canMove(bottomRightCorner, topLeftCorner))
print(canMove(bottomRightCorner, topMiddle))
print(canMove(bottomRightCorner, topRightCorner))
print(canMove(bottomRightCorner, middleLeft))
print(canMove(bottomRightCorner, trueMiddle))
print(canMove(bottomRightCorner, middleRight))
print(canMove(bottomRightCorner, bottomLeftCorner))
print(canMove(bottomRightCorner, bottomMiddle))
print(canMove(bottomRightCorner, bottomRightCorner))



# calculateNewEmptySpaceAfterMove Tests:

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topMiddle))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, middleLeft))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, trueMiddle))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, middleRight))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topMiddle' '\n')

print(calculateNewEmptySpaceAfterMove(topMiddle, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddle, topMiddle))
print(calculateNewEmptySpaceAfterMove(topMiddle, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topMiddle, middleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddle, trueMiddle))
print(calculateNewEmptySpaceAfterMove(topMiddle, middleRight))
print(calculateNewEmptySpaceAfterMove(topMiddle, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddle, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(topMiddle, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topMiddle))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, middleLeft))
print(calculateNewEmptySpaceAfterMove(topRightCorner, trueMiddle))
print(calculateNewEmptySpaceAfterMove(topRightCorner, middleRight))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the middleLeft' '\n')

print(calculateNewEmptySpaceAfterMove(middleLeft, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(middleLeft, topMiddle))
print(calculateNewEmptySpaceAfterMove(middleLeft, topRightCorner))
print(calculateNewEmptySpaceAfterMove(middleLeft, middleLeft))
print(calculateNewEmptySpaceAfterMove(middleLeft, trueMiddle))
print(calculateNewEmptySpaceAfterMove(middleLeft, middleRight))
print(calculateNewEmptySpaceAfterMove(middleLeft, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(middleLeft, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(middleLeft, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the trueMiddle' '\n')

print(calculateNewEmptySpaceAfterMove(trueMiddle, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(trueMiddle, topMiddle))
print(calculateNewEmptySpaceAfterMove(trueMiddle, topRightCorner))
print(calculateNewEmptySpaceAfterMove(trueMiddle, middleLeft))
print(calculateNewEmptySpaceAfterMove(trueMiddle, trueMiddle))
print(calculateNewEmptySpaceAfterMove(trueMiddle, middleRight))
print(calculateNewEmptySpaceAfterMove(trueMiddle, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(trueMiddle, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(trueMiddle, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the middleRight' '\n')

print(calculateNewEmptySpaceAfterMove(middleRight, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(middleRight, topMiddle))
print(calculateNewEmptySpaceAfterMove(middleRight, topRightCorner))
print(calculateNewEmptySpaceAfterMove(middleRight, middleLeft))
print(calculateNewEmptySpaceAfterMove(middleRight, trueMiddle))
print(calculateNewEmptySpaceAfterMove(middleRight, middleRight))
print(calculateNewEmptySpaceAfterMove(middleRight, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(middleRight, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(middleRight, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topMiddle))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, middleLeft))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, trueMiddle))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, middleRight))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomMiddle' '\n')

print(calculateNewEmptySpaceAfterMove(bottomMiddle, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, topMiddle))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, middleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, trueMiddle))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, middleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(bottomMiddle, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topMiddle))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, middleLeft))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, trueMiddle))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, middleRight))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomMiddle))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomRightCorner))

"""
