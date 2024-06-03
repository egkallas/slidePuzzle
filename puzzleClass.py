import pygame
import copy
from pygame.locals import *
from puzzlePieceClasses.twoxtwopuzzlePieceClass import *
from random import randint
from copy import deepcopy

PUZZLE_H_W = 600    # Pixel dimensions
MOVE_SPEED = 5      # How fast the pieces slide
SIDE_OFFSET = 150   # Side offset of the puzzle relative to the sides of the window
TOP_OFFSET = 155     # Top offset of the puzzle relative to the sides of the window
SHUFFLE_MULT = 50   # How many moves are made for each puzzle difficulty starting at 50 for a 2x2

class puzzle:
    def __init__(self, img, dim, screen, backColor, loadConfig = [], moves = 0): 
        self.image = pygame.transform.scale(img, (PUZZLE_H_W, PUZZLE_H_W))
        self.rectangle = Rect((SIDE_OFFSET, TOP_OFFSET),(PUZZLE_H_W, PUZZLE_H_W))
        self.surf = pygame.Surface((PUZZLE_H_W, PUZZLE_H_W))
        self.dimensions = dim
        self.moveCounter = moves
        self.screen = screen
        self.backColor = backColor
        self.pieceDim = PUZZLE_H_W/self.dimensions
        self.pieces = [[0]*self.dimensions for i in range(self.dimensions)]
        self.imgPiece = [[0]*self.dimensions for i in range(self.dimensions)]
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                left = j*self.pieceDim
                top = i*self.pieceDim
                self.pieces[i][j] = puzzlePiece(i, j, left, top, self.pieceDim)
                self.imgPiece[i][j] = self.image.subsurface(self.pieces[i][j].rectangle)
                
        self.pieces[self.dimensions - 1][self.dimensions - 1].isEmptySpace = True
        if(loadConfig == []): # Testing if this initialization is a loaded game
            self.checkMovement()
            self.shuffle()
            self.initialState = self.saveData()[2]
        else: 
            self.load(loadConfig)
            self.initialState = self.saveData()[2]
        self.refresh()

    def refresh(self, finalShow = False): # Refresh the display of the puzzle, can be used externally 
        self.surf.fill(self.backColor)
        if finalShow:
            self.surf.blit(self.imgPiece[self.dimensions-1][self.dimensions-1], self.pieces[self.dimensions-1][self.dimensions-1].rectangle)
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if self.pieces[i][j].isEmptySpace == False:
                    self.surf.blit(self.imgPiece[i][j], self.pieces[i][j].rectangle)
        self.screen.blit(self.surf, (SIDE_OFFSET, TOP_OFFSET))
   
    def puzzleClicked(self, evPos): # Action handling for clicking pieces
        (xCor, yCor) = evPos
        xCor -= SIDE_OFFSET
        yCor -= TOP_OFFSET
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if self.pieces[i][j].rectangle.collidepoint((xCor, yCor)):
                    self.move(i,j)
                    

    def checkMovement(self): # Sets booleans of individual piece objects to identify what can move and how
        for i in self.pieces: # Sets all Directions to unable so tiles aren't accidentally moved onto other tiles.
            for j in i:
                j.moveableDirections = Direction.Unable

        for i in range(self.dimensions): # Finds the empty tile and then changes all adjacent files
            for j in range(self.dimensions):
                if(self.pieces[i][j].isEmptySpace):
                    if (i+1) < self.dimensions:
                        self.pieces[i+1][j].moveableDirections = Direction.Up
                    if (i-1) >= 0:
                        self.pieces[i-1][j].moveableDirections = Direction.Down
                    if (j+1) < self.dimensions:
                        self.pieces[i][j+1].moveableDirections = Direction.Left
                    if (j-1) >= 0:
                        self.pieces[i][j-1].moveableDirections = Direction.Right
    
    def winConfig(self): # Returns a boolean representing if the puzzle is solved or not
        i = 0
        properPos = True
        while(i < self.dimensions and properPos):
            j = 0
            while(j < self.dimensions and properPos):
                properPos = (self.pieces[i][j].row == i and self.pieces[i][j].col == j)
                j+=1
            i+=1
        return properPos

    
    def move(self, row, col, shuffle = False): # Mainly internal, is used by puzzleClicked function and shuffle
        if(self.pieces[row][col].moveableDirections != Direction.Unable):
            k = 1
            match self.pieces[row][col].moveableDirections:
                case Direction.Up:
                    self.swapPieceRectangles(row, col, (row - 1), col)
                    self.pieces[row][col].rectangle.move_ip(0, self.pieceDim)
                    while(k*MOVE_SPEED <= self.pieceDim):
                        self.pieces[row - 1][col].rectangle.move_ip(0, -MOVE_SPEED)
                        if(not shuffle):
                            self.refresh()
                            pygame.display.update(self.rectangle)
                        k+=1
                case Direction.Down:
                    self.swapPieceRectangles(row, col, (row + 1), col)
                    self.pieces[row][col].rectangle.move_ip(0, -self.pieceDim)
                    while(k*MOVE_SPEED <= self.pieceDim):
                        self.pieces[row + 1][col].rectangle.move_ip(0, MOVE_SPEED)
                        if(not shuffle):
                            self.refresh()
                            pygame.display.update(self.rectangle)
                        k+=1
                case Direction.Right:
                    self.swapPieceRectangles(row, col, row, (col + 1))
                    self.pieces[row][col].rectangle.move_ip(-self.pieceDim, 0)
                    while(k*MOVE_SPEED <= self.pieceDim):
                        self.pieces[row][col + 1].rectangle.move_ip(MOVE_SPEED, 0)
                        if(not shuffle):
                            self.refresh()
                            pygame.display.update(self.rectangle)
                        k+=1
                case Direction.Left:
                    self.swapPieceRectangles(row, col, row, (col - 1))
                    self.pieces[row][col].rectangle.move_ip(self.pieceDim, 0)
                    while(k*MOVE_SPEED <= self.pieceDim):
                        self.pieces[row][col - 1].rectangle.move_ip(-MOVE_SPEED, 0)
                        if(not shuffle):
                            self.refresh()
                            pygame.display.update(self.rectangle)
                        k+=1
            if(not shuffle):
                self.moveCounter += 1 # increment the move counter
            self.checkMovement()

    def swapPieceRectangles(self, row1, col1, row2, col2): # Internal function, used for move functions
        temp = self.pieces[row1][col1]
        self.pieces[row1][col1] = self.pieces[row2][col2]
        self.pieces[row2][col2] = temp
        temp = self.imgPiece[row1][col1]
        self.imgPiece[row1][col1] = self.imgPiece[row2][col2]
        self.imgPiece[row2][col2] = temp

    def shuffle(self): # Function shuffles the puzzle. Could be used with a button to re-shuffle
        while(self.winConfig()):
            prevI = prevJ = -1
            if(self.dimensions == 2): # This if else statement is to make sure if the user does a 2x2 it is not always sorted the same.
                randAdd = randint(0, 10)
            else:
                randAdd = 0

            for index in range(SHUFFLE_MULT * (self.dimensions - 1) + randAdd):
                i = j = 0
                emptyFound = False
                while(i < self.dimensions and not emptyFound): # find empty space
                    j = 0
                    while(j < self.dimensions and not emptyFound):
                        emptyFound = self.pieces[i][j].isEmptySpace
                        if(not emptyFound):
                            j+=1
                    if(not emptyFound):
                        i+=1
                moveArr = [[0]*2 for i in range(4)]# move in random one of four directions
                possMoves = 0
                if(i+1 < self.dimensions and (i+1 != prevI or j != prevJ)):
                    moveArr[possMoves] = [i+1, j]
                    possMoves += 1
                if(i-1 >= 0 and (i-1 != prevI or j != prevJ)):
                    moveArr[possMoves] = [i-1, j]
                    possMoves += 1
                if(j+1 < self.dimensions and (i != prevI or j+1 != prevJ)):
                    moveArr[possMoves] = [i, j+1]
                    possMoves += 1
                if(j-1 >= 0 and (i != prevI or j-1 != prevJ)):
                    moveArr[possMoves] = [i, j-1]
                    possMoves += 1
                if(possMoves == 1):
                    randIndex = 0
                else:
                    randIndex = randint(0, possMoves - 1)
                prevI = i
                prevJ = j
                self.move(moveArr[randIndex][0], moveArr[randIndex][1], True)
                

    def reset(self): # Reset function
        if hasattr(self, 'initialState'): # Have to use deep copy to ensure it can be reset to the same configuration multiple times
            self.load(copy.deepcopy(self.initialState))
            self.moveCounter = 0

    def load(self, loadArray): # For loading from array. Internal function only.
        tempArrPiece = [[0]*self.dimensions for i in range(self.dimensions)]
        tempArrImg = [[0]*self.dimensions for i in range(self.dimensions)]
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                tempArrImg[i][j] = self.imgPiece[loadArray[i][j][0]][loadArray[i][j][1]]
                tempArrPiece[i][j] = deepcopy(self.pieces[loadArray[i][j][0]][loadArray[i][j][1]])
                testVar = self.pieces[i][j].rectangle
                tempArrPiece[i][j].rectangle = self.pieces[i][j].rectangle
        self.imgPiece = tempArrImg
        self.pieces = tempArrPiece
        self.checkMovement()

    def saveData(self):
        try:
            saveArray = [[0] * self.dimensions for _ in range(self.dimensions)]
            for i in range(self.dimensions):
                for j in range(self.dimensions):
                    if self.pieces[i][j] is not None:
                        saveArray[i][j] = [self.pieces[i][j].row, self.pieces[i][j].col]
                    else:
                        raise ValueError(f"Missing puzzle piece at position ({i}, {j})")
                    #print(f"Saving piece at {i},{j} with position {saveArray[i][j]}") # Debugging 
            return (self.dimensions, self.moveCounter, saveArray)
        except Exception as e:
            print(f"Error saving puzzle data: {e}")
            return None

    
    def showFullPhoto(self):
        self.pieces[self.dimensions - 1][self.dimensions - 1].rectangle.move_ip(0, -self.pieceDim)
        k = 1
        while(k*MOVE_SPEED <= self.pieceDim):
            self.pieces[self.dimensions - 1][self.dimensions - 1].rectangle.move_ip(0, MOVE_SPEED)
            self.refresh(True)
            pygame.display.update(self.rectangle)
            k+=1
