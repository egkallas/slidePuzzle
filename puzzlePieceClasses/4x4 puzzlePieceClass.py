# Puzzle Piece Class for a 4x4 puzzle

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
topMiddleLeft = puzzlePiece(1, 2, False, False, False, False, False, False, [])
topMiddleRight = puzzlePiece(1, 3, False, False, False, False, False, False, [])
topRightCorner = puzzlePiece(1, 4, False, False, False, False, False, False, [])
upperMiddleLeftmost = puzzlePiece(2, 1, False, False, False, False, False, False, [])
upperMiddleLeft = puzzlePiece(2, 2, False, False, False, False, False, False, [])
upperMiddleRight = puzzlePiece(2, 3, False, False, False, False, False, False, [])
upperMiddleRightmost = puzzlePiece(2, 4, False, False, False, False, False, False, [])
lowerMiddleLeftmost = puzzlePiece(3, 1, False, False, False, False, False, False, [])
lowerMiddleLeft = puzzlePiece(3, 2, False, False, False, False, False, False, [])
lowerMiddleRight = puzzlePiece(3, 3, False, False, False, False, False, False, [])
lowerMiddleRightmost = puzzlePiece(3, 4, False, True, False, False, False, True, [])  
bottomLeftCorner = puzzlePiece(4, 1, False, False, False, False, False, False, [])
bottomMiddleLeft = puzzlePiece(4, 2, False, False, False, False, False, False, [])
bottomMiddleRight = puzzlePiece(4, 3, False, True, False, True, False, False, [])
bottomRightCorner = puzzlePiece(4, 4, True, None, True, False, True, False, [])

# Function to determine if a piece is adjacent to the empty space for movement logic

def isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece):
    if((targetPiece.isEmptySpace != True) or (pieceChecking.isEmptySpace == True)): # This line contains two basic checks to make sure valid parameters are being fed in. (i.e. there is actually something to check)
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
        pieceChecking.canMoveLeft = False 
        pieceChecking.canMoveRight = False 
        pieceChecking.canMoveUp = False
        pieceChecking.canMoveDown = False
        return moveableDirections, 'pieceChecking and targetPiece are the same piece.'
    
    pieceCheckingAdjacencyToEmptyPiece = isAdjacentToEmptySpaceCheck(pieceChecking, targetPiece)
    if((pieceCheckingAdjacencyToEmptyPiece == False) and (pieceChecking.isEmptySpace == False)): # If pieceChecking is not adjacent to the empty space, and pieceChecking is not the empty space, it cannot possibly move/be moved
        return moveableDirections, 'pieceChecking is not adjacent to the empty space and/or pieceChecking is not the empty space and/or targetPiece is not the empty space.'
    
    else:
        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col > 1)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the leftmost column, it can move left
            if(pieceChecking.col - 1 == targetPiece.col): # If the piece under examination is in the second row, we must ensure that both the left and right movement branches don't evaluate to True.
                pieceChecking.canMoveLeft = True
                moveableDirections.append(Direction.Left)
        else:
            pieceChecking.canMoveLeft = False

        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.row == targetPiece.row) and (pieceChecking.col < 4)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the rightmost column, it can move right
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

        if(((pieceChecking.isAdjacentToEmptySpace != False) or (pieceChecking.isEmptySpace == True)) and (pieceChecking.col == targetPiece.col) and (pieceChecking.row < 4)): # If the piece is adjacent to the empty space, or is the empty space, and is not in the bottommost row, it can move down
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
    if(pieceBeingSwappedWith.isEmptySpace == False): # If the pieceBeingSwappedWith is not the empty space, pieceClickedOn cannot possibly take its place. In other words, the move is not possible
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
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(topLeftCorner, bottomRightCorner))


print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for topMiddleLeft' '\n')

print(isAdjacentToEmptySpaceCheck(topMiddleLeft, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleLeft, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for topMiddleRight' '\n')

print(isAdjacentToEmptySpaceCheck(topMiddleRight, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(topMiddleRight, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the topRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(topRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(topRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topRightCorner, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topRightCorner, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(topRightCorner, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topRightCorner, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(topRightCorner, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topRightCorner, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(topRightCorner, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(topRightCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for upperMiddleLeftMost' '\n')

print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, topRightCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for upperMiddleLeft' '\n')

print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, topRightCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleLeft, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for upperMiddleRight' '\n')

print(isAdjacentToEmptySpaceCheck(upperMiddleRight, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, topRightCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRight, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the upperMiddleRightmost' '\n')

print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, topRightCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(upperMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for lowerMiddleLeftmost' '\n')

print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, topRightCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for lowerMiddleLeft' '\n')

print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, topRightCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleLeft, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for lowerMiddleRight' '\n')

print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, topRightCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRight, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for lowerMiddleRightmost' '\n')

print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, topRightCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(lowerMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomLeftCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomMiddleLeft' '\n')

print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleLeft, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomMiddleRight' '\n')

print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomMiddleRight, bottomRightCorner))

print('\n' 'Conducting isAdjacentToEmptySpaceCheck tests for the bottomRightCorner' '\n')

print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, topRightCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, upperMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, upperMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, upperMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, upperMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, lowerMiddleLeftmost))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, lowerMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, lowerMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, lowerMiddleRightmost))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomLeftCorner))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomMiddleLeft))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomMiddleRight))
print(isAdjacentToEmptySpaceCheck(bottomRightCorner, bottomRightCorner))



# canMove Tests:

print('\n' 'Conducting canMove tests for the topLeftCorner' '\n')

print(canMove(topLeftCorner, topLeftCorner))
print(canMove(topLeftCorner, topMiddleLeft))
print(canMove(topLeftCorner, topMiddleRight))
print(canMove(topLeftCorner, topRightCorner))
print(canMove(topLeftCorner, upperMiddleLeftmost))
print(canMove(topLeftCorner, upperMiddleLeft))
print(canMove(topLeftCorner, upperMiddleRight))
print(canMove(topLeftCorner, upperMiddleRightmost))
print(canMove(topLeftCorner, lowerMiddleLeftmost))
print(canMove(topLeftCorner, lowerMiddleLeft))
print(canMove(topLeftCorner, lowerMiddleRight))
print(canMove(topLeftCorner, lowerMiddleRightmost))
print(canMove(topLeftCorner, bottomLeftCorner))
print(canMove(topLeftCorner, bottomMiddleLeft))
print(canMove(topLeftCorner, bottomMiddleRight))
print(canMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topMiddleLeft' '\n')

print(canMove(topMiddleLeft, topLeftCorner))
print(canMove(topMiddleLeft, topMiddleLeft))
print(canMove(topMiddleLeft, topMiddleRight))
print(canMove(topMiddleLeft, topRightCorner))
print(canMove(topMiddleLeft, upperMiddleLeftmost))
print(canMove(topMiddleLeft, upperMiddleLeft))
print(canMove(topMiddleLeft, upperMiddleRight))
print(canMove(topMiddleLeft, upperMiddleRightmost))
print(canMove(topMiddleLeft, lowerMiddleLeftmost))
print(canMove(topMiddleLeft, lowerMiddleLeft))
print(canMove(topMiddleLeft, lowerMiddleRight))
print(canMove(topMiddleLeft, lowerMiddleRightmost))
print(canMove(topMiddleLeft, bottomLeftCorner))
print(canMove(topMiddleLeft, bottomMiddleLeft))
print(canMove(topMiddleLeft, bottomMiddleRight))
print(canMove(topMiddleLeft, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topMiddleRight' '\n')

print(canMove(topMiddleRight, topLeftCorner))
print(canMove(topMiddleRight, topMiddleLeft))
print(canMove(topMiddleRight, topMiddleRight))
print(canMove(topMiddleRight, topRightCorner))
print(canMove(topMiddleRight, upperMiddleLeftmost))
print(canMove(topMiddleRight, upperMiddleLeft))
print(canMove(topMiddleRight, upperMiddleRight))
print(canMove(topMiddleRight, upperMiddleRightmost))
print(canMove(topMiddleRight, lowerMiddleLeftmost))
print(canMove(topMiddleRight, lowerMiddleLeft))
print(canMove(topMiddleRight, lowerMiddleRight))
print(canMove(topMiddleRight, lowerMiddleRightmost))
print(canMove(topMiddleRight, bottomLeftCorner))
print(canMove(topMiddleRight, bottomMiddleLeft))
print(canMove(topMiddleRight, bottomMiddleRight))
print(canMove(topMiddleRight, bottomRightCorner))

print('\n' 'Conducting canMove tests for the topRightCorner' '\n')

print(canMove(topRightCorner, topLeftCorner))
print(canMove(topRightCorner, topMiddleLeft))
print(canMove(topRightCorner, topMiddleRight))
print(canMove(topRightCorner, topRightCorner))
print(canMove(topRightCorner, upperMiddleLeftmost))
print(canMove(topRightCorner, upperMiddleLeft))
print(canMove(topRightCorner, upperMiddleRight))
print(canMove(topRightCorner, upperMiddleRightmost))
print(canMove(topRightCorner, lowerMiddleLeftmost))
print(canMove(topRightCorner, lowerMiddleLeft))
print(canMove(topRightCorner, lowerMiddleRight))
print(canMove(topRightCorner, lowerMiddleRightmost))
print(canMove(topRightCorner, bottomLeftCorner))
print(canMove(topRightCorner, bottomMiddleLeft))
print(canMove(topRightCorner, bottomMiddleRight))
print(canMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for  upperMiddleLeftmost' '\n')

print(canMove(upperMiddleLeftmost, topLeftCorner))
print(canMove(upperMiddleLeftmost, topMiddleLeft))
print(canMove(upperMiddleLeftmost, topMiddleRight))
print(canMove(upperMiddleLeftmost, topRightCorner))
print(canMove(upperMiddleLeftmost, upperMiddleLeftmost))
print(canMove(upperMiddleLeftmost, upperMiddleLeft))
print(canMove(upperMiddleLeftmost, upperMiddleRight))
print(canMove(upperMiddleLeftmost, upperMiddleRightmost))
print(canMove(upperMiddleLeftmost, lowerMiddleLeftmost))
print(canMove(upperMiddleLeftmost, lowerMiddleLeft))
print(canMove(upperMiddleLeftmost, lowerMiddleRight))
print(canMove(upperMiddleLeftmost, lowerMiddleRightmost))
print(canMove(upperMiddleLeftmost, bottomLeftCorner))
print(canMove(upperMiddleLeftmost, bottomMiddleLeft))
print(canMove(upperMiddleLeftmost, bottomMiddleRight))
print(canMove(upperMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting canMove tests for upperMiddleLeft' '\n')

print(canMove(upperMiddleLeft, topLeftCorner))
print(canMove(upperMiddleLeft, topMiddleLeft))
print(canMove(upperMiddleLeft, topMiddleRight))
print(canMove(upperMiddleLeft, topRightCorner))
print(canMove(upperMiddleLeft, upperMiddleLeftmost))
print(canMove(upperMiddleLeft, upperMiddleLeft))
print(canMove(upperMiddleLeft, upperMiddleRight))
print(canMove(upperMiddleLeft, upperMiddleRightmost))
print(canMove(upperMiddleLeft, lowerMiddleLeftmost))
print(canMove(upperMiddleLeft, lowerMiddleLeft))
print(canMove(upperMiddleLeft, lowerMiddleRight))
print(canMove(upperMiddleLeft, lowerMiddleRightmost))
print(canMove(upperMiddleLeft, bottomLeftCorner))
print(canMove(upperMiddleLeft, bottomMiddleLeft))
print(canMove(upperMiddleLeft, bottomMiddleRight))
print(canMove(upperMiddleLeft, bottomRightCorner))

print('\n' 'Conducting canMove tests for the upperMiddleRight' '\n')

print(canMove(upperMiddleRight, topLeftCorner))
print(canMove(upperMiddleRight, topMiddleLeft))
print(canMove(upperMiddleRight, topMiddleRight))
print(canMove(upperMiddleRight, topRightCorner))
print(canMove(upperMiddleRight, upperMiddleLeftmost))
print(canMove(upperMiddleRight, upperMiddleLeft))
print(canMove(upperMiddleRight, upperMiddleRight))
print(canMove(upperMiddleRight, upperMiddleRightmost))
print(canMove(upperMiddleRight, lowerMiddleLeftmost))
print(canMove(upperMiddleRight, lowerMiddleLeft))
print(canMove(upperMiddleRight, lowerMiddleRight))
print(canMove(upperMiddleRight, lowerMiddleRightmost))
print(canMove(upperMiddleRight, bottomLeftCorner))
print(canMove(upperMiddleRight, bottomMiddleLeft))
print(canMove(upperMiddleRight, bottomMiddleRight))
print(canMove(upperMiddleRight, bottomRightCorner))

print('\n' 'Conducting canMove tests for the upperMiddleRightmost' '\n')

print(canMove(upperMiddleRightmost, topLeftCorner))
print(canMove(upperMiddleRightmost, topMiddleLeft))
print(canMove(upperMiddleRightmost, topMiddleRight))
print(canMove(upperMiddleRightmost, topRightCorner))
print(canMove(upperMiddleRightmost, upperMiddleLeftmost))
print(canMove(upperMiddleRightmost, upperMiddleLeft))
print(canMove(upperMiddleRightmost, upperMiddleRight))
print(canMove(upperMiddleRightmost, upperMiddleRightmost))
print(canMove(upperMiddleRightmost, lowerMiddleLeftmost))
print(canMove(upperMiddleRightmost, lowerMiddleLeft))
print(canMove(upperMiddleRightmost, lowerMiddleRight))
print(canMove(upperMiddleRightmost, lowerMiddleRightmost))
print(canMove(upperMiddleRightmost, bottomLeftCorner))
print(canMove(upperMiddleRightmost, bottomMiddleLeft))
print(canMove(upperMiddleRightmost, bottomMiddleRight))
print(canMove(upperMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting canMove tests for  lowerMiddleLeftmost' '\n')

print(canMove(lowerMiddleLeftmost, topLeftCorner))
print(canMove(lowerMiddleLeftmost, topMiddleLeft))
print(canMove(lowerMiddleLeftmost, topMiddleRight))
print(canMove(lowerMiddleLeftmost, topRightCorner))
print(canMove(lowerMiddleLeftmost, upperMiddleLeftmost))
print(canMove(lowerMiddleLeftmost, upperMiddleLeft))
print(canMove(lowerMiddleLeftmost, upperMiddleRight))
print(canMove(lowerMiddleLeftmost, upperMiddleRightmost))
print(canMove(lowerMiddleLeftmost, lowerMiddleLeftmost))
print(canMove(lowerMiddleLeftmost, lowerMiddleLeft))
print(canMove(lowerMiddleLeftmost, lowerMiddleRight))
print(canMove(lowerMiddleLeftmost, lowerMiddleRightmost))
print(canMove(lowerMiddleLeftmost, bottomLeftCorner))
print(canMove(lowerMiddleLeftmost, bottomMiddleLeft))
print(canMove(lowerMiddleLeftmost, bottomMiddleRight))
print(canMove(lowerMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting canMove tests for lowerMiddleLeft' '\n')

print(canMove(lowerMiddleLeft, topLeftCorner))
print(canMove(lowerMiddleLeft, topMiddleLeft))
print(canMove(lowerMiddleLeft, topMiddleRight))
print(canMove(lowerMiddleLeft, topRightCorner))
print(canMove(lowerMiddleLeft, upperMiddleLeftmost))
print(canMove(lowerMiddleLeft, upperMiddleLeft))
print(canMove(lowerMiddleLeft, upperMiddleRight))
print(canMove(lowerMiddleLeft, upperMiddleRightmost))
print(canMove(lowerMiddleLeft, lowerMiddleLeftmost))
print(canMove(lowerMiddleLeft, lowerMiddleLeft))
print(canMove(lowerMiddleLeft, lowerMiddleRight))
print(canMove(lowerMiddleLeft, lowerMiddleRightmost))
print(canMove(lowerMiddleLeft, bottomLeftCorner))
print(canMove(lowerMiddleLeft, bottomMiddleLeft))
print(canMove(lowerMiddleLeft, bottomMiddleRight))
print(canMove(lowerMiddleLeft, bottomRightCorner))

print('\n' 'Conducting canMove tests for lowerMiddleRight' '\n')

print(canMove(lowerMiddleRight, topLeftCorner))
print(canMove(lowerMiddleRight, topMiddleLeft))
print(canMove(lowerMiddleRight, topMiddleRight))
print(canMove(lowerMiddleRight, topRightCorner))
print(canMove(lowerMiddleRight, upperMiddleLeftmost))
print(canMove(lowerMiddleRight, upperMiddleLeft))
print(canMove(lowerMiddleRight, upperMiddleRight))
print(canMove(lowerMiddleRight, upperMiddleRightmost))
print(canMove(lowerMiddleRight, lowerMiddleLeftmost))
print(canMove(lowerMiddleRight, lowerMiddleLeft))
print(canMove(lowerMiddleRight, lowerMiddleRight))
print(canMove(lowerMiddleRight, lowerMiddleRightmost))
print(canMove(lowerMiddleRight, bottomLeftCorner))
print(canMove(lowerMiddleRight, bottomMiddleLeft))
print(canMove(lowerMiddleRight, bottomMiddleRight))
print(canMove(lowerMiddleRight, bottomRightCorner))

print('\n' 'Conducting canMove tests for lowerMiddleRightmost' '\n')

print(canMove(lowerMiddleRightmost, topLeftCorner))
print(canMove(lowerMiddleRightmost, topMiddleLeft))
print(canMove(lowerMiddleRightmost, topMiddleRight))
print(canMove(lowerMiddleRightmost, topRightCorner))
print(canMove(lowerMiddleRightmost, upperMiddleLeftmost))
print(canMove(lowerMiddleRightmost, upperMiddleLeft))
print(canMove(lowerMiddleRightmost, upperMiddleRight))
print(canMove(lowerMiddleRightmost, upperMiddleRightmost))
print(canMove(lowerMiddleRightmost, lowerMiddleLeftmost))
print(canMove(lowerMiddleRightmost, lowerMiddleLeft))
print(canMove(lowerMiddleRightmost, lowerMiddleRight))
print(canMove(lowerMiddleRightmost, lowerMiddleRightmost))
print(canMove(lowerMiddleRightmost, bottomLeftCorner))
print(canMove(lowerMiddleRightmost, bottomMiddleLeft))
print(canMove(lowerMiddleRightmost, bottomMiddleRight))
print(canMove(lowerMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomLeftCorner' '\n')

print(canMove(bottomLeftCorner, topLeftCorner))
print(canMove(bottomLeftCorner, topMiddleLeft))
print(canMove(bottomLeftCorner, topMiddleRight))
print(canMove(bottomLeftCorner, topRightCorner))
print(canMove(bottomLeftCorner, upperMiddleLeftmost))
print(canMove(bottomLeftCorner, upperMiddleLeft))
print(canMove(bottomLeftCorner, upperMiddleRight))
print(canMove(bottomLeftCorner, upperMiddleRightmost))
print(canMove(bottomLeftCorner, lowerMiddleLeftmost))
print(canMove(bottomLeftCorner, lowerMiddleLeft))
print(canMove(bottomLeftCorner, lowerMiddleRight))
print(canMove(bottomLeftCorner, lowerMiddleRightmost))
print(canMove(bottomLeftCorner, bottomLeftCorner))
print(canMove(bottomLeftCorner, bottomMiddleLeft))
print(canMove(bottomLeftCorner, bottomMiddleRight))
print(canMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomMiddleLeft' '\n')

print(canMove(bottomMiddleLeft, topLeftCorner))
print(canMove(bottomMiddleLeft, topMiddleLeft))
print(canMove(bottomMiddleLeft, topMiddleRight))
print(canMove(bottomMiddleLeft, topRightCorner))
print(canMove(bottomMiddleLeft, upperMiddleLeftmost))
print(canMove(bottomMiddleLeft, upperMiddleLeft))
print(canMove(bottomMiddleLeft, upperMiddleRight))
print(canMove(bottomMiddleLeft, upperMiddleRightmost))
print(canMove(bottomMiddleLeft, lowerMiddleLeftmost))
print(canMove(bottomMiddleLeft, lowerMiddleLeft))
print(canMove(bottomMiddleLeft, lowerMiddleRight))
print(canMove(bottomMiddleLeft, lowerMiddleRightmost))
print(canMove(bottomMiddleLeft, bottomLeftCorner))
print(canMove(bottomMiddleLeft, bottomMiddleLeft))
print(canMove(bottomMiddleLeft, bottomMiddleRight))
print(canMove(bottomMiddleLeft, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomMiddleRight' '\n')

print(canMove(bottomMiddleRight, topLeftCorner))
print(canMove(bottomMiddleRight, topMiddleLeft))
print(canMove(bottomMiddleRight, topMiddleRight))
print(canMove(bottomMiddleRight, topRightCorner))
print(canMove(bottomMiddleRight, upperMiddleLeftmost))
print(canMove(bottomMiddleRight, upperMiddleLeft))
print(canMove(bottomMiddleRight, upperMiddleRight))
print(canMove(bottomMiddleRight, upperMiddleRightmost))
print(canMove(bottomMiddleRight, lowerMiddleLeftmost))
print(canMove(bottomMiddleRight, lowerMiddleLeft))
print(canMove(bottomMiddleRight, lowerMiddleRight))
print(canMove(bottomMiddleRight, lowerMiddleRightmost))
print(canMove(bottomMiddleRight, bottomLeftCorner))
print(canMove(bottomMiddleRight, bottomMiddleLeft))
print(canMove(bottomMiddleRight, bottomMiddleRight))
print(canMove(bottomMiddleRight, bottomRightCorner))

print('\n' 'Conducting canMove tests for the bottomRightCorner' '\n')

print(canMove(bottomRightCorner, topLeftCorner))
print(canMove(bottomRightCorner, topMiddleLeft))
print(canMove(bottomRightCorner, topMiddleRight))
print(canMove(bottomRightCorner, topRightCorner))
print(canMove(bottomRightCorner, upperMiddleLeftmost))
print(canMove(bottomRightCorner, upperMiddleLeft))
print(canMove(bottomRightCorner, upperMiddleRight))
print(canMove(bottomRightCorner, upperMiddleRightmost))
print(canMove(bottomRightCorner, lowerMiddleLeftmost))
print(canMove(bottomRightCorner, lowerMiddleLeft))
print(canMove(bottomRightCorner, lowerMiddleRight))
print(canMove(bottomRightCorner, lowerMiddleRightmost))
print(canMove(bottomRightCorner, bottomLeftCorner))
print(canMove(bottomRightCorner, bottomMiddleLeft))
print(canMove(bottomRightCorner, bottomMiddleRight))
print(canMove(bottomRightCorner, bottomRightCorner))



# calculateNewEmptySpaceAfterMove Tests:

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(topLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for topMiddleLeft' '\n')

print(calculateNewEmptySpaceAfterMove(topMiddleLeft, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleLeft, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topMiddleRight' '\n')

print(calculateNewEmptySpaceAfterMove(topMiddleRight, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(topMiddleRight, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the topRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(topRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(topRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topRightCorner, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topRightCorner, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(topRightCorner, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topRightCorner, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(topRightCorner, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topRightCorner, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(topRightCorner, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(topRightCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for upperMiddleLeftmost' '\n')

print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, topRightCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for upperMiddleLeft' '\n')

print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, topRightCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleLeft, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for upperMiddleRight' '\n')

print(calculateNewEmptySpaceAfterMove(upperMiddleRight, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, topRightCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRight, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for upperMiddleRightmost' '\n')

print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, topRightCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(upperMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for  lowerMiddleLeftmost' '\n')

print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, topRightCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeftmost, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for lowerMiddleLeft' '\n')

print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, topRightCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleLeft, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for lowerMiddleRight' '\n')

print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, topRightCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRight, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for lowerMiddleRightmost' '\n')

print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, topRightCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(lowerMiddleRightmost, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomLeftCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomLeftCorner, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomMiddleLeft' '\n')

print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleLeft, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomMiddleRight' '\n')

print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomMiddleRight, bottomRightCorner))

print('\n' 'Conducting calculateNewEmptySpaceAfterMove tests for the bottomRightCorner' '\n')

print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, topRightCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, upperMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, upperMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, upperMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, upperMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, lowerMiddleLeftmost))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, lowerMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, lowerMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, lowerMiddleRightmost))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomLeftCorner))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomMiddleLeft))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomMiddleRight))
print(calculateNewEmptySpaceAfterMove(bottomRightCorner, bottomRightCorner))

"""
