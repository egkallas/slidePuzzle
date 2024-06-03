# Puzzle Piece Class for a 2x2 puzzle

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

topLeftCorner = puzzlePiece(1, 1, False, False, False, False, False, False)
topRightCorner = puzzlePiece(1, 2, False, True, False, False, False, True)
bottomLeftCorner = puzzlePiece(2, 1, False, True, False, True, False, False)
bottomRightCorner = puzzlePiece(2, 2, True, None, True, False, True, False)
    
# Function to determine if a piece is adjacent to the empty space for movement logic

def isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece):
    if((targetPiece.isEmptySpace != True) | (pieceChecking.isEmptySpace != False)): # This line contains two basic checks to make sure valid parameters are being fed in. (i.e. there is actually something to check)
        return False # Either the target piece is not the empty space or the piece being checked is the empty space. In either case, the function call is useless
    if((pieceChecking.row == targetPiece.row) and (pieceChecking.col == targetPiece.col)): # If the two pieces fed in are in fact the same piece, there is no adjacency to check
        return False
    elif((pieceChecking.row + 1 == targetPiece.row) and (pieceChecking.col == targetPiece.col) and (targetPiece.isEmptySpace == True)): # If the piece is below the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True # Updating the piece being inspected's isAdjacentToEmptySpace attribute to reflect that it is adjacent to the empty space
        return True, (targetPiece.row, targetPiece.col) # Returning the cordinates of the empty space
    elif((pieceChecking.row - 1 == targetPiece.row) and (pieceChecking.col == targetPiece.col) and (targetPiece.isEmptySpace == True)): # If the piece is above the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True # Updating the piece being inspected's isAdjacentToEmptySpace attribute to reflect that it is adjacent to the empty space
        return True, (targetPiece.row, targetPiece.col) # Returning the cordinates of the empty space
    elif((pieceChecking.col + 1 == targetPiece.col) and (pieceChecking.row == targetPiece.row) and (targetPiece.isEmptySpace == True)): # If the piece is to the right of the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True # Updating the piece being inspected's isAdjacentToEmptySpace attribute to reflect that it is adjacent to the empty space
        return True, (targetPiece.row, targetPiece.col) # Returning the cordinates of the empty space
    elif((pieceChecking.col - 1 == targetPiece.col) and (pieceChecking.row == targetPiece.row) and (targetPiece.isEmptySpace == True)): # If the piece is to the left of the empty space, it is adjacent to the empty space
        pieceChecking.isAdjacentToEmptySpace = True # Updating the piece being inspected's isAdjacentToEmptySpace attribute to reflect that it is adjacent to the empty space
        return True, (targetPiece.row, targetPiece.col)
    else:
        pieceChecking.isAdjacentToEmptySpace = False # In any other case, (i.e. pieceChecking's center makes a 45 degree angle with targetPiece's center) the piece is not adjacent to the empty space
        return False, targetPiece.row, targetPiece.col # Returning the cordinates of the empty space

# Functions to check if a piece can move left, right, up, or down

def canMove(pieceChecking, targetPiece):
    moveableDirections = []
    if((pieceChecking.row == targetPiece.row) and (pieceChecking.col == targetPiece.col)):
        return moveableDirections, 'pieceChecking and targetPiece are the same piece.'
    pieceChecking.isAdjacentToEmptySpace = isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece)

    if((pieceChecking.isAdjacentToEmptySpace != False) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col > 1)): # Can the piece move left?
        pieceChecking.canMoveLeft = True
        moveableDirections.append(Direction.Left)
    else:
        pieceChecking.canMoveLeft = False
   
    if((pieceChecking.isAdjacentToEmptySpace != False) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col < 2)): # Can the piece move right?
        pieceChecking.canMoveRight = True
        moveableDirections.append(Direction.Right)
    else:
        pieceChecking.canMoveRight = False

    if((pieceChecking.isAdjacentToEmptySpace != False) and (pieceChecking.col == targetPiece.col) and (pieceChecking.row > 1)): # Can the piece move up?
        pieceChecking.canMoveUp = True
        moveableDirections.append(Direction.Up)
    else:
        pieceChecking.canMoveUp = False

    if((pieceChecking.isAdjacentToEmptySpace != False) and (pieceChecking.col == targetPiece.col) and (pieceChecking.row < 2)): # Can the piece move down?
        pieceChecking.canMoveDown = True
        moveableDirections.append(Direction.Down)
    else:
        pieceChecking.canMoveDown = False

    if(pieceChecking.canMoveLeft or pieceChecking.canMoveRight or pieceChecking.canMoveUp or pieceChecking.canMoveDown):
        return True, 'the piece can move ', moveableDirections
    return False
    
# Function to calculate the new empty space that results from a move. Set new values for isAdjacentToEmptySpace and canMove values for each piece?
    
def calculateNewEmptySpaceAfterMove(pieceClickedOn, pieceBeingSwappedWith): # If a move is initiated, the empty space (pieceBeingSwappedWith) will move to the space occupied by pieceClickedOn. The empty space will then be in the space previously occupied by pieceClickedOn
    if((pieceClickedOn.row == pieceBeingSwappedWith.row) and (pieceClickedOn.col == pieceBeingSwappedWith.col)): # If the two pieces fed in are in fact the same, there are no movement possibilities to consider
        return
    
    pieceCapableOfMoving = canMove(pieceClickedOn, pieceBeingSwappedWith)

    if((pieceCapableOfMoving) and (pieceClickedOn.row != pieceBeingSwappedWith.row)): # The two pieces swapped are not of the same row, therefore they must be in the same column
        tempSwapColumn = pieceClickedOn.col
        pieceClickedOn.col = pieceBeingSwappedWith.col
        pieceBeingSwappedWith.col = tempSwapColumn
        return(pieceClickedOn.row, pieceClickedOn.col)

    if((pieceCapableOfMoving) and (pieceClickedOn.col != pieceBeingSwappedWith.col)): # The two pieces swapped are not of the same column, therefore they must be in the same row
        tempSwapRow = pieceClickedOn.row
        pieceClickedOn.row = pieceBeingSwappedWith.row
        pieceBeingSwappedWith.row = tempSwapRow
        return(pieceClickedOn.row, pieceClickedOn.col)



"""""

# TESTS BEGIN HERE
        
# isAdjacentToEmptySpace Tests:

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topLeftCorner' '\n')
        
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(topRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomLeftCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomRightCorner))

# canMove Tests:

print('\n' 'Conducting canMove tests for the topLeftCorner' '\n')

print(canMove(topLeftCorner, topLeftCorner))
print(canMove(topLeftCorner, topRightCorner))
print(canMove(topLeftCorner, bottomLeftCorner))
print(canMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topRightCorner' '\n')

print(canMove(topRightCorner, topLeftCorner))
print(canMove(topRightCorner, topRightCorner))
print(canMove(topRightCorner, bottomLeftCorner))
print(canMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomLeftCorner' '\n')

print(canMove(bottomLeftCorner, topLeftCorner))
print(canMove(bottomLeftCorner, topRightCorner))
print(canMove(bottomLeftCorner, bottomLeftCorner))
print(canMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomRightCorner' '\n')

print(canMove(bottomRightCorner, topLeftCorner))
print(canMove(bottomRightCorner, topRightCorner))
print(canMove(bottomRightCorner, bottomLeftCorner))
print(canMove(bottomRightCorner, bottomRightCorner))

# calculateNewEmptySpaceAfterMove Tests:

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomRightCorner))

"""
