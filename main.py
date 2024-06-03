import pygame
from pygame.locals import *
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
import os   
import json
import datetime
from puzzleClass import puzzle

# pygame setup
pygame.init()
WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH), HWSURFACE | DOUBLEBUF | RESIZABLE)
clock = pygame.time.Clock()
running = True
manager = pygame_gui.UIManager((WINDOW_HEIGHT, WINDOW_WIDTH))
background = pygame.Surface((WINDOW_HEIGHT, WINDOW_WIDTH))
modeCheck = 2

current_directory = os.getcwd()

#creates a folder for save files
folderName = "save_files"
saveFolderPath = os.path.join(current_directory, folderName)
if not os.path.exists(saveFolderPath):
    os.makedirs(saveFolderPath)

#get image file path
def openFile(): 
    file_selection = UIFileDialog(rect=Rect(0, 0, 900, 750), manager=manager, allow_picking_directories=False)
    running = True
    while running: 
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == file_selection.ok_button:
                        return str(file_selection.current_file_path)
                    if event.ui_element == file_selection.cancel_button:
                        return str(0)
                    if event.ui_element == file_selection.close_window_button:
                        return str(0)
            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(background, (0,0))
        manager.draw_ui(screen)
        pygame.display.update()


#save image path to txt file
def saveImagePath(file_path):
    with open("saved_images.txt", "a") as file:
        file.write(file_path + "\n")


def saveGame(puzzle, imagePath):
    
    current_directory = os.getcwd()

    #creates a folder for save files
    folderName = "save_files"
    folder_path = os.path.join(current_directory, folderName)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    currentDateTime = datetime.datetime.now()
    dateTimeString = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
    fileName = f"{dateTimeString}.json"
    saveFilePath = os.path.join(folder_path, fileName)

    #adds currentImage (global variable) and array data from puzzle method to dictionary
    (dimensions, moves, loadArray) = puzzle.saveData()
    data = {
        "image": imagePath,
        "dimensions": dimensions,
        "moves": moves,
        "loadArray": loadArray
    }

    # Write the dictionary to a JSON file
    with open(saveFilePath, "w") as json_file:
        json.dump(data, json_file, indent=4)
        

def loadSave(): 
    file_selection = UIFileDialog(rect=Rect(0, 0, 900, 750), manager=manager, allow_picking_directories=False, initial_file_path = saveFolderPath)
    savePath = ""
    while savePath == "": 
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == file_selection.ok_button:
                        savePath = str(file_selection.current_file_path)
                    if event.ui_element == file_selection.cancel_button:
                        return str(0)
                    if event.ui_element == file_selection.close_window_button:
                        return str(0)
            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(background, (0,0))
        manager.draw_ui(screen)
        pygame.display.update()
    with open(savePath, 'r') as json_file:
        data = json.load(json_file)

    global currentImage
    imagePath = data["image"]
    currentImage = imagePath
    loadedImage = pygame.image.load(imagePath)
    loadDim = data["dimensions"]
    loadMoves = data["moves"]
    loadArray = data["loadArray"]
    loadInfo = [loadedImage, loadDim, loadArray, loadMoves]
    return loadInfo
    

def startScreen():
    running = True
    global backGroundColor
    global textColor
    global modeCheck
    while running:
        #This is where the logic of the color change happens
        if modeCheck % 3 == 0:
            backGroundColor = pygame.Color("#ffffff") 
            textColor = pygame.Color("#3395ff") 
            modeLetter = 'D'
        if modeCheck % 3 == 1:
            backGroundColor = pygame.Color("#000000") 
            textColor = pygame.Color("#FF9D33") 
            modeLetter = 'M'
        if modeCheck % 3 == 2:
            backGroundColor = pygame.Color("#2e2f34") 
            textColor = pygame.Color("#0015ff") 
            modeLetter = 'L'
            
        titleFont = pygame.font.Font('freesansbold.ttf', 84)
        optionFont = pygame.font.Font('freesansbold.ttf', 50)

        titleText = titleFont.render('PuzzleBlast', True, textColor)
        newText = optionFont.render('New Game', True, backGroundColor)
        loadText = optionFont.render('Load Game', True, backGroundColor)
        exitText = optionFont.render('Quit', True, backGroundColor)
        modeText = optionFont.render(modeLetter, True, backGroundColor)

        titleRect = titleText.get_rect()
        titleRect.center = ((450,80))

        newRect = newText.get_rect()
        newRect.center = ((450, 380))

        loadRect = loadText.get_rect()
        loadRect.center = ((450, 500))

        exitRect = exitText.get_rect()
        exitRect.center = ((450, 620))

        modeRect = modeText.get_rect()
        modeRect.center = ((840, 790))

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect(250, 340, 400, 80).collidepoint(event.pos):
                        newGameScreen()
                        # Here we will put the call to the new game function
                    elif pygame.Rect(250, 460, 400, 80).collidepoint(event.pos):
                        loadInfo = loadSave()
                        if loadInfo != "0":
                            isLoadGame = True
                            imageToLoad = loadInfo[0]
                            gameScreen(imageToLoad, loadInfo[1], loadInfo[2], loadInfo[3])
                        
                        # Here we will put the call to the Load game function
                    elif pygame.Rect(250, 580, 400, 80).collidepoint(event.pos):
                        quit()
                        # Here we will exit the game
                    elif pygame.Rect(800, 750, 80, 80).collidepoint(event.pos):
                        modeCheck = modeCheck + 1
                        # Here we will change the number to change the colors

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(backGroundColor)


        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 340, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            newText = optionFont.render('New Game', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 460, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            loadText = optionFont.render('Load Game', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 580, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            exitText = optionFont.render('Quit', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(800, 750, 80, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            modeText = optionFont.render(modeLetter, True, 'yellow')

        # RENDER YOUR GAME HERE
        pygame.display.set_caption('Start Game')
        screen.blit(titleText, titleRect)
        screen.blit(newText, newRect)
        screen.blit(loadText,loadRect)
        screen.blit(exitText,exitRect)
        screen.blit(modeText,modeRect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


def newGameScreen():
       
    running = True
    while running:
        
        screen.fill(backGroundColor)

        chooseFont = pygame.font.Font('freesansbold.ttf', 40)
        chooseText = chooseFont.render('Choose New Image', True, backGroundColor)
        chooseRect = chooseText.get_rect()
        chooseRect.center = ((450, 380))

        chooseOldFont = pygame.font.Font('freesansbold.ttf', 33)
        chooseOldText = chooseOldFont.render('Choose Previous Image', True, backGroundColor)
        chooseOldRect = chooseOldText.get_rect()
        chooseOldRect.center = ((450, 500))
        
        backText = chooseOldFont.render('Back', True, backGroundColor)
        backRect = backText.get_rect()
        backRect.center = ((450, 620))

        #poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect(250, 340, 400, 80).collidepoint(event.pos):
                        path = openFile()
                        if path != "0":
                            global currentImage
                            currentImage = path
                            loadedImg = pygame.image.load(path)
                            saveImagePath(path) 
                            difficultySelectionScreen(loadedImg)
                            #get file path and pass it as argument to main game loop
                            running = False
                    elif pygame.Rect(250, 460, 400, 80).collidepoint(event.pos):
                        galleryScreen()
                    elif pygame.Rect(250, 580, 400, 80).collidepoint(event.pos):
                        running = False

                            

        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 340, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            chooseText = chooseFont.render('Choose New Image', True, 'yellow')

        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 460, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            chooseOldText = chooseOldFont.render('Choose Previous Image', True, 'yellow')
            
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 580, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            backText = chooseOldFont.render('Back', True, 'yellow')
        
        # RENDER YOUR GAME HERE
        pygame.display.set_caption('New Game')
        screen.blit(chooseText, chooseRect)
        screen.blit(chooseOldText, chooseOldRect)
        screen.blit(backText, backRect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)

def loadGameScreen():
        
    running = True
    while running:

        screen.fill(backGroundColor)

        chooseSaveFont = pygame.font.Font('freesansbold.ttf', 40)
        chooseSaveText = chooseSaveFont.render('Choose Save File', True, backGroundColor)
        chooseSaveRect = chooseSaveText.get_rect()
        chooseSaveRect.center = ((450, 120))


        #poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    break
                            
        
        # RENDER YOUR GAME HERE
        pygame.display.set_caption('Load Game')
        pygame.draw.rect(screen, textColor, pygame.Rect(250, 80, 400, 80),  0, 3)
        screen.blit(chooseSaveText, chooseSaveRect)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)


def difficultySelectionScreen(loadedImg): #choose difficulty screen

    dimension = 0 #difficulty variable. 1 = easy, 2 = medium, so on. passed to game screen function.

    running = True
    while running:
        screen.fill(backGroundColor)

        #difficulty screen text/rects
        titleFont = pygame.font.Font('freesansbold.ttf', 84)
        optionFont = pygame.font.Font('freesansbold.ttf', 50)

        titleText = titleFont.render('Choose Difficulty', True, textColor)
        easyText = optionFont.render('Easy', True, backGroundColor)
        mediumText = optionFont.render('Medium', True, backGroundColor)
        hardText = optionFont.render('Hard', True, backGroundColor)
        extremeText = optionFont.render("Extreme", True, backGroundColor)
        backText = optionFont.render('Back', True, backGroundColor)


        titleRect = titleText.get_rect()
        titleRect.center = ((450,80))

        easyRect = easyText.get_rect()
        easyRect.center = ((450, 340))

        mediumRect = mediumText.get_rect()
        mediumRect.center = ((450, 460))

        hardRect = hardText.get_rect()
        hardRect.center = ((450, 580))

        extremeRect = extremeText.get_rect()
        extremeRect.center = ((450, 700))

        backRect = backText.get_rect() 
        backRect.center = ((792, 842))
        

        for event in pygame.event.get(): # Event handler (mouse clicks)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.Rect(250, 300, 400, 80).collidepoint(event.pos): # Difficulty selections
                        print("Easy difficulty button pushed")
                        dimension = 2
                        gameScreen(loadedImg, dimension)
                    elif pygame.Rect(250, 420, 400, 80).collidepoint(event.pos):
                        print("Medium difficulty button pushed")
                        dimension = 3
                        gameScreen(loadedImg, dimension)
                    elif pygame.Rect(250, 540, 400, 80).collidepoint(event.pos):
                        print("Hard difficulty button pushed")
                        dimension = 4
                        gameScreen(loadedImg, dimension)
                    elif pygame.Rect(250, 660, 400, 80).collidepoint(event.pos):
                        print("Extreme difficulty button pushed")
                        dimension = 5
                        gameScreen(loadedImg, dimension)
                    elif pygame.Rect(720, 800, 150, 80).collidepoint(event.pos):
                         running = False
                    
        #make text flash yellow upon hover
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 300, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            easyText = optionFont.render('Easy', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 420, 400, 80),  0, 3) .collidepoint(pygame.mouse.get_pos()):
            mediumText = optionFont.render('Medium', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 540, 400, 80),  0, 3) .collidepoint(pygame.mouse.get_pos()):
            hardText = optionFont.render('Hard', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 660, 400, 80),  0, 3) .collidepoint(pygame.mouse.get_pos()):
            extremeText = optionFont.render('Extreme', True, 'yellow')
        if pygame.draw.rect(screen, textColor, pygame.Rect(720, 800, 150, 80),  0, 3) .collidepoint(pygame.mouse.get_pos()):
            backText = optionFont.render('Back', True, 'yellow')

        pygame.display.set_caption('Choose Difficulty')
        
        #blit text 
        screen.blit(titleText, titleRect)
        screen.blit(easyText, easyRect)
        screen.blit(mediumText, mediumRect)
        screen.blit(hardText, hardRect)
        screen.blit(extremeText, extremeRect)
        screen.blit(backText, backRect)

        pygame.display.flip() # Flip the display to work on screen

        clock.tick(60)  # Limit FPS to 60

#gallery to load previous images
def galleryScreen():
    if os.path.isfile("saved_images.txt") == False:
        open("saved_images.txt", "x")
    
    triangleRightPos = ((800,350),(800,550),(875,450))
    TriangleLeftPos = ((100,350),(100,550),(25,450))
    waitForEventToStart = 0

    moveGal = 0
    held = False

    galHeight = 200
    galwidth = 200

    # Get image paths
    imagePaths = []
    with open("saved_images.txt", "r") as file:
        for line in file:
            filepath = line.strip()
            if os.path.exists(filepath):
                imagePaths.append(filepath)
       
    galImages = []
    galFilePath = []
    # Resize gal images and create surfaces
    for path in imagePaths:
        galFilePath.append(path)
        image = pygame.image.load(path)
        resized_image = pygame.transform.scale(image, (galwidth, galHeight))
        surface = resized_image.convert()  
        galImages.append(surface)

    total_width = len(galImages[0:3]) * (galwidth + 20)

    # Calculate the initial x-coordinate for blitting
    start_x = (WINDOW_WIDTH - total_width) // 2 + 10

    running = True
    while running:

        chooseFromGalFont = pygame.font.Font('freesansbold.ttf', 40)
        chooseFromGalText = chooseFromGalFont.render('Choose an image.', True, textColor)
        chooseFromGalRect = chooseFromGalText.get_rect()
        chooseFromGalRect.center = ((450, 300))
        
        backFont = pygame.font.Font('freesansbold.ttf', 50)
        backText = backFont.render('Back', True, backGroundColor)
        backRect = backText.get_rect()
        backRect.center = ((450, 670))

        removeFont1 = pygame.font.Font('freesansbold.ttf', 35)
        removeText1 = removeFont1.render('Remove', True, textColor)
        removeRect1 = removeText1.get_rect()
        removeRect1.center = (((start_x + 100, (WINDOW_HEIGHT - galHeight) / 1.2)))

        removeFont2 = pygame.font.Font('freesansbold.ttf', 35)
        removeText2 = removeFont2.render('Remove', True, textColor)
        removeRect2 = removeText2.get_rect()
        removeRect2.center = (((start_x + galwidth + 120, (WINDOW_HEIGHT - galHeight) / 1.2)))

        removeFont3 = pygame.font.Font('freesansbold.ttf', 35)
        removeText3 = removeFont3.render('Remove', True, textColor)
        removeRect3 = removeText3.get_rect()
        removeRect3.center = (((start_x + galwidth * 2 + 130, (WINDOW_HEIGHT - galHeight) / 1.2)))
        x = start_x

    
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backRect.collidepoint(event.pos):
                        running = False
                        pygame.event.clear()  # Clearing the event queue after handling the back button
                        break 
                    if pygame.Rect(250, 630, 400, 80).collidepoint(event.pos):
                        waitForEventToStart = 0
                        running = False
                    #poll for event to remove images
                    elif removeRect1.collidepoint(event.pos):
                        if len(galImages) > 0:
                            del galImages[moveGal]
                            del imagePaths[moveGal]
                            del galFilePath[moveGal]
                    elif removeRect2.collidepoint(event.pos):
                        if len(galImages) > 1:
                            del galImages[moveGal + 1]
                            del imagePaths[moveGal + 1]
                            del galFilePath[moveGal + 1]
                    elif removeRect3.collidepoint(event.pos): 
                        if len(galImages) > 2:
                            del galImages[moveGal + 2]
                            del imagePaths[moveGal + 2]
                            del galFilePath[moveGal + 2]
                    elif moveGal+3 > len(galImages) & len(galImages) > 2:
                        moveGal = moveGal-1
                for place, image in enumerate(galImages[moveGal:moveGal+3]):
                    if pygame.draw.rect(screen, textColor, pygame.Rect(x, (WINDOW_HEIGHT - galHeight) // 2, 200, 200)).collidepoint(pygame.mouse.get_pos()) == True:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                running = False
                                path = galFilePath[place]
                                global currentImage
                                currentImage = path
                                loadedImg = pygame.image.load(path)
                            difficultySelectionScreen(loadedImg)
                    x += galwidth + 20
                

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(backGroundColor)
        
        # RENDER YOUR GAME HERE
        pygame.display.set_caption('Choose Image')
        if pygame.draw.rect(screen, textColor, pygame.Rect(250, 630, 400, 80),  0, 3).collidepoint(pygame.mouse.get_pos()):
            backText = backFont.render('Back', True, 'yellow')
        if removeRect1.collidepoint(pygame.mouse.get_pos()):
            removeText1 = removeFont1.render('Remove', True, 'yellow')
        if removeRect2.collidepoint(pygame.mouse.get_pos()):
            removeText2 = removeFont2.render('Remove', True, 'yellow')
        if removeRect3.collidepoint(pygame.mouse.get_pos()):
            removeText3 = removeFont3.render('Remove', True, 'yellow')
        
        # RENDER YOUR GAME HERE
        #This is all to generate triangles that allow you to shuffle between pictures
        if len(galImages) > 3:
            if pygame.draw.polygon(screen, textColor, triangleRightPos).collidepoint(pygame.mouse.get_pos()) == True:#Triangle on the right
                if len(galImages) > moveGal+3:
                    pygame.draw.polygon(screen, 'yellow', triangleRightPos)
                    if event.type == pygame.MOUSEBUTTONUP:
                        if held == False: # Check if button is held down
                                moveGal = moveGal + 1 # If button is not held down, go to the next image
                        held = True # Set held eqaual to true for next iteration
                    else: # If left mouse button is not pressed
                        held = False
            if pygame.draw.polygon(screen, textColor, TriangleLeftPos).collidepoint(pygame.mouse.get_pos()) == True:#Triangle on the right
                if 0 < moveGal:
                    pygame.draw.polygon(screen, 'yellow', TriangleLeftPos)
                    if event.type == pygame.MOUSEBUTTONUP:
                        if held == False: # Check if button is held down
                                moveGal = moveGal - 1# If button is not held down, go to the previous image
                        held = True # Set held eqaual to true for next iteration
                    else: # If left mouse button is not pressed
                        held = False


        
        screen.blit(backText, backRect)
        screen.blit(chooseFromGalText, chooseFromGalRect)
       
        if len(galImages) > 0:
            screen.blit(removeText1, removeRect1)
        if len(galImages) > 1:
            screen.blit(removeText2, removeRect2)
        if len(galImages) > 2:
            screen.blit(removeText3, removeRect3)
        
        
        x = start_x
        for image in galImages[moveGal:moveGal+3]:
            screen.blit(image, (x, (WINDOW_HEIGHT - galHeight) // 2))
            x += galwidth + 20
        
        
       
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    #logic to clear out images that were deleted as well as txt that dosent belong
    newSaved = open("saved_images.txt", "w")
    for path in imagePaths:
        newSaved.write(path + "\n")
    newSaved.close()

            


############################

def optionsScreen(game, currentImage):
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    showConfirmation = False

    saveText = font.render('Save Game', True, textColor)
    saveRect = saveText.get_rect()
    saveRect.center = ((450, 240))

    newText = font.render('New Game', True, textColor)
    newRect = newText.get_rect()
    newRect.center = ((450, 340))

    resetText = font.render('Reset', True, textColor)
    resetRect = resetText.get_rect()
    resetRect.center = ((450, 440))

    mainText = font.render('Main Menu', True, textColor)
    mainRect = mainText.get_rect()
    mainRect.center = ((450, 540))

    backText = font.render('Back', True, textColor)
    backRect = backText.get_rect()
    backRect.center = ((450, 640))

    yesText = font.render('Yes', True, textColor)
    noText = font.render('No', True, textColor)
    yesRect = yesText.get_rect()
    noRect = noText.get_rect()
    yesRect.center = (350, 420)
    noRect.center = (550, 420)

    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    saveRect = saveText.get_rect(center=(450, 240))
    newRect = newText.get_rect(center=(450, 340))
    resetRect = resetText.get_rect(center=(450, 440))
    mainRect = mainText.get_rect(center=(450, 540))
    backRect = backText.get_rect(center=(450, 640))
    yesRect = yesText.get_rect(center=(350, 520))
    noRect = noText.get_rect(center=(550, 520))


    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if saveRect.collidepoint(event.pos):
                        saveGame(game, currentImage)
                        savePopUp()
                        running = False
                    if newRect.collidepoint(event.pos):
                        running = False
                        toMain = False
                        newGamePopUp(game, currentImage, toMain)
                    if resetRect.collidepoint(event.pos):
                        running = False
                        restartGamePopUp(game)
                        #showConfirmation = True
                    elif resetRect.collidepoint(event.pos):
                        running = False  # Close the options menu
                    elif backRect.collidepoint(event.pos):
                        running = False
                    elif mainRect.collidepoint(event.pos):
                        running = False
                        toMain = True
                        newGamePopUp(game, currentImage, toMain)


                    #if showConfirmation:
                        #if yesRect.collidepoint(event.pos):
                            #game.reset()  # Perform the reset
                            #running = False  # Close menu after reset
                        #elif noRect.collidepoint(event.pos):
                            #showConfirmation = False  # Cancel reset

        if saveRect.collidepoint(pygame.mouse.get_pos()):
            saveText = font.render('Save Game', True, 'yellow')
        else:
            saveText = font.render('Save Game', True, textColor)
        
        if newRect.collidepoint(pygame.mouse.get_pos()):
            newText = font.render('New Game', True, 'yellow')
        else:
            newText = font.render('New Game', True, textColor)
        
        if resetRect.collidepoint(pygame.mouse.get_pos()):
            resetText = font.render('Reset', True, 'yellow')
        else:
            resetText = font.render('Reset', True, textColor)

        if mainRect.collidepoint(pygame.mouse.get_pos()):
            mainText = font.render('Main Menu', True, 'yellow')
        else:
            mainText = font.render('Main Menu', True, textColor)

        if backRect.collidepoint(pygame.mouse.get_pos()):
            backText = font.render('Back', True, 'yellow')
        else:
            backText = font.render('Back', True, textColor)

        if yesRect.collidepoint(pygame.mouse.get_pos()):
            yesText = font.render('Yes', True, 'yellow')
        else:
            yesText = font.render('Yes', True, textColor)

        if noRect.collidepoint(pygame.mouse.get_pos()):
            noText = font.render('No', True, 'yellow')
        else:
            noText = font.render('No', True, textColor)


        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)
        

        screen.blit(saveText, saveRect)
        screen.blit(newText, newRect)
        screen.blit(resetText, resetRect)
        screen.blit(mainText, mainRect)
        screen.blit(backText, backRect)

        #if showConfirmation:
            # Overlay for confirmation
            #pygame.draw.rect(screen, backGroundColor, (300, 450, 300, 100), 0)
            #screen.blit(yesText, yesRect)
            #screen.blit(noText, noRect)
            #screen.blit(font.render('Are you sure?', True, textColor), (350, 460))

      
        pygame.display.flip()
        clock.tick(30)  # Reduced FPS for the pause menu

def restartGamePopUp(game):
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    askToRestartFont = pygame.font.Font('freesansbold.ttf', 50)

    askToRestartText = askToRestartFont.render('Are you sure?', True, textColor)
    askToRestartRect = askToRestartText.get_rect()
    askToRestartRect.center = ((450, 240))

    yesText = font.render('Yes', True, textColor)
    yesRect = yesText.get_rect()
    yesRect.center = ((450, 440))

    noText = font.render('No', True, textColor)
    noRect = noText.get_rect()
    noRect.center = ((450, 540))

    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesRect.collidepoint(event.pos):
                        game.reset()  # Reset the game to the initial shuffled state
                        running = False  # Close the popup and continue the game
                    if noRect.collidepoint(event.pos):
                        running = False  # Close the popup without resetting

        if yesRect.collidepoint(pygame.mouse.get_pos()):
            yesText = font.render('Yes', True, 'yellow')
        else:
            yesText = font.render('Yes', True, textColor)

        if noRect.collidepoint(pygame.mouse.get_pos()):
            noText = font.render('No', True, 'yellow')
        else:
            noText = font.render('No', True, textColor)

        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)

        screen.blit(askToRestartText, askToRestartRect)
        screen.blit(yesText, yesRect)
        screen.blit(noText, noRect)

        pygame.display.flip()
        clock.tick(30)  # Reduced FPS for the pause menu


def savePopUp():
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    gameSavedFont = pygame.font.Font('freesansbold.ttf', 50)

    gameSavedText = gameSavedFont.render('Game Saved', True, textColor)
    gameSavedRect = gameSavedText.get_rect()
    gameSavedRect.center = ((450, 240))

    backText = font.render('Back', True, textColor)
    backRect = backText.get_rect()
    backRect.center = ((450, 540))

    mainText = font.render('Main Menu', True, textColor)
    mainRect = mainText.get_rect()
    mainRect.center = ((450, 640))

    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backRect.collidepoint(event.pos):
                        running = False
                    if mainRect.collidepoint(event.pos):
                        running = False
                        startScreen()

        if backRect.collidepoint(pygame.mouse.get_pos()):
            backText = font.render('Back', True, 'yellow')
        else:
            backText = font.render('Back', True, textColor)

        if mainRect.collidepoint(pygame.mouse.get_pos()):
            mainText = font.render('Main Menu', True, 'yellow')
        else:
            mainText = font.render('Main Menu', True, textColor)

        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)

        screen.blit(gameSavedText, gameSavedRect)
        screen.blit(backText, backRect)
        screen.blit(mainText, mainRect)

        
        
        pygame.display.flip()
        clock.tick(30)  


def newGamePopUp(game, imagePath, toMain):
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    askToSaveFont = pygame.font.Font('freesansbold.ttf', 50)

    askToSaveText = askToSaveFont.render('Save Game?', True, textColor)
    askToSaveRect = askToSaveText.get_rect()
    askToSaveRect.center = ((450, 240))

    yesText = font.render('Yes', True, textColor)
    yesRect = yesText.get_rect()
    yesRect.center = ((450, 440))

    noText = font.render('No', True, textColor)
    noRect = noText.get_rect()
    noRect.center = ((450, 540))

    backText = font.render('Back', True, textColor)
    backRect = backText.get_rect()
    backRect.center = ((450, 640))

    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backRect.collidepoint(event.pos):
                        running = False
                        optionsScreen()
                    if yesRect.collidepoint(event.pos):
                        if toMain == True:
                            running = False
                            saveGame(game, currentImage)
                            startScreen()
                        else:
                            running = False
                            saveGame(game, currentImage)
                            newGameScreen()
                    if noRect.collidepoint(event.pos):
                        if toMain == False:
                            running = False
                            newGameScreen()
                        else:
                            running = False
                            startScreen()

        if backRect.collidepoint(pygame.mouse.get_pos()):
            backText = font.render('Back', True, 'yellow')
        else:
            backText = font.render('Back', True, textColor)

        if yesRect.collidepoint(pygame.mouse.get_pos()):
            yesText = font.render('Yes', True, 'yellow')
        else:
            yesText = font.render('Yes', True, textColor)

        if noRect.collidepoint(pygame.mouse.get_pos()):
            noText = font.render('No', True, 'yellow')
        else:
            noText = font.render('No', True, textColor)

        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)

        screen.blit(askToSaveText, askToSaveRect)
        screen.blit(yesText, yesRect)
        screen.blit(noText, noRect)
        

        
        
        pygame.display.flip()
        clock.tick(30)  

def winScreen(game, imagePath):
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    playAgainFont = pygame.font.Font('freesansbold.ttf', 40)

    winFont = pygame.font.Font('freesansbold.ttf', 100)
    winText = winFont.render('YOU WIN!', True, 'yellow')
    winRect = winText.get_rect()
    winRect.center = ((450, 100))

    playAgainText = playAgainFont.render('Play Again?', True, textColor)
    playAgainRect = playAgainText.get_rect()
    playAgainRect.center = ((450, 240))

    yesText = font.render('Yes', True, textColor)
    yesRect = yesText.get_rect()
    yesRect.center = ((450, 440))

    noText = font.render('No', True, textColor)
    noRect = noText.get_rect()
    noRect.center = ((450, 540))


    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesRect.collidepoint(event.pos):
                        postWinScreen(currentImage)
                    if noRect.collidepoint(event.pos):
                        running = False
                        startScreen()

        if yesRect.collidepoint(pygame.mouse.get_pos()):
            yesText = font.render('Yes', True, 'yellow')
        else:
            yesText = font.render('Yes', True, textColor)

        if noRect.collidepoint(pygame.mouse.get_pos()):
            noText = font.render('No', True, 'yellow')
        else:
            noText = font.render('No', True, textColor)

        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)

        screen.blit(winText, winRect)
        screen.blit(playAgainText, playAgainRect)
        screen.blit(yesText, yesRect)
        screen.blit(noText, noRect)
        

        
        
        pygame.display.flip()
        clock.tick(30) 

def postWinScreen(imagePath):
    running = True
    clock = pygame.time.Clock()
   
    font = pygame.font.Font('freesansbold.ttf', 30)
    playAgainFont = pygame.font.Font('freesansbold.ttf', 40)

    newImageText = playAgainFont.render('New Image', True, textColor)
    newImageRect = newImageText.get_rect()
    newImageRect.center = ((450, 240))

    orText = playAgainFont.render('or', True, textColor)
    orRect = orText.get_rect()
    orRect.center = ((450, 300))

    sameImageText = playAgainFont.render('Same Image?', True, textColor)
    sameImageRect = sameImageText.get_rect()
    sameImageRect.center = ((450, 360))

    newText = font.render('New', True, textColor)
    newRect = newText.get_rect()
    newRect.center = ((450, 540))

    oldText = font.render('Old', True, textColor)
    oldRect = oldText.get_rect()
    oldRect.center = ((450, 640))


    menuRect1 = pygame.Rect(255, 170, 380, 540)
    menuRect2 = pygame.Rect(245, 160, 400, 560)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if oldRect.collidepoint(event.pos):
                        running = False
                        loadedImg = pygame.image.load(currentImage)
                        difficultySelectionScreen(loadedImg)
                    if newRect.collidepoint(event.pos):
                        running = False
                        newGameScreen()

        if newRect.collidepoint(pygame.mouse.get_pos()):
            newText = font.render('New', True, 'yellow')
        else:
            newText = font.render('New', True, textColor)

        if oldRect.collidepoint(pygame.mouse.get_pos()):
            oldText = font.render('Old', True, 'yellow')
        else:
            oldText = font.render('Old', True, textColor)

        pygame.draw.rect(screen, textColor, menuRect2, 0, 3)
        pygame.draw.rect(screen, backGroundColor, menuRect1, 0, 3)

        screen.blit(newImageText, newImageRect)
        screen.blit(orText, orRect)
        screen.blit(sameImageText, sameImageRect)
        screen.blit(newText, newRect)
        screen.blit(oldText, oldRect)
        

        
        
        pygame.display.flip()
        clock.tick(30) 

def gameScreen(loadedImg, dimensions, loadArr = [], loadMoves = 0):
    running = True
    surface = pygame.Surface((loadedImg.get_width(), loadedImg.get_height()))
    game = puzzle(loadedImg, dimensions, screen, backGroundColor, loadArr, loadMoves)
    while running:
        # poll for events

        optionsFont = pygame.font.Font('freesansbold.ttf', 25)
        optionsText = optionsFont.render('Options', True, backGroundColor)
        optionsRect = optionsText.get_rect()
        optionsRect.center = ((95, 63))

        moveFont = pygame.font.Font('freesansbold.ttf', 25)
        moveText = moveFont.render('Move Count', True, textColor)
        countText = moveFont.render(str(game.moveCounter), True, textColor)
        moveRect = moveText.get_rect()
        countRect = countText.get_rect()
        moveRect.center = ((420, 835))
        countRect.center = ((520, 835))

        

        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.rectangle.collidepoint(event.pos):
                        #print("Clicked within the puzzle area.")  # Debug statement
                        game.puzzleClicked(event.pos)
                    elif optionsRect.collidepoint(event.pos):
                        #print("Clicked within the options area.")  # Debug statement
                        optionsScreen(game, currentImage)
                    elif pygame.Rect(250, 630, 400, 47).collidepoint(event.pos):
                        #print("Clicked within the specific rectangle area.")  # Debug statement
                        running = False
                    elif pygame.Rect(250, 697, 400, 47).collidepoint(event.pos):
                        #print("Clicked within another specific rectangle area.")  # Debug statement
                        saveGame(game, currentImage)


        # fill the screen with a color to wipe away anything from last frame
        screen.fill(backGroundColor)

        if pygame.draw.rect(screen, textColor, pygame.Rect(35, 40, 120, 47),  0, 3).collidepoint(pygame.mouse.get_pos()):
            optionsText = optionsFont.render('Options', True, 'yellow')  
        
        # RENDER YOUR GAME HERE
        pygame.display.set_caption('Puzzle Blast')
        game.refresh()
        screen.blit(optionsText, optionsRect)
        screen.blit(moveText, moveRect)
        screen.blit(countText, countRect)
        if game.winConfig() == True:
            game.showFullPhoto()
            winScreen(game, currentImage)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

startScreen()

pygame.quit()

