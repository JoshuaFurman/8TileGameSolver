import Puzzle
import pygame

# Global variables for pygame
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
fps = 60
DISPLAYSIZE = 600
CELLSIZE = int(DISPLAYSIZE/3)

# Fill the window with WHITE and draw grid lines
def setBoard(surface):
    surface.fill(WHITE)
    for x in range(0, DISPLAYSIZE, CELLSIZE):
        pygame.draw.line(surface, BLACK, (x, 0), (x, DISPLAYSIZE))
        for y in range(0, DISPLAYSIZE, CELLSIZE):
            pygame.draw.line(surface, BLACK, (0, y), (DISPLAYSIZE, y))

# Pass function a string to display at the top of the window
def printHeader(headline, surface):
    font = pygame.font.Font('freesansbold.ttf', 30)
    cellText = font.render(headline, True, RED, WHITE)
    cellRect = cellText.get_rect()
    cellRect.center = (300, 50)
    surface.blit(cellText, cellRect)

    # This draws a grey box in the cell that is selected
def showClickedCell(mouse_x, mouse_y, surface):
    if 0 < mouse_x < 200 and 0 < mouse_y < 200:
        pygame.draw.rect(surface, GREY, (5,5,190,190))

    elif 0 < mouse_x < 200 and 200 < mouse_y < 400:
        pygame.draw.rect(surface, GREY, (5,205,190,190))

    elif 0 < mouse_x < 200 and 400 < mouse_y < 600:
        pygame.draw.rect(surface, GREY, (5,405,190,190))

    elif 200 < mouse_x < 400 and 0 < mouse_y < 200:
        pygame.draw.rect(surface, GREY, (205,5,190,190))

    elif 200 < mouse_x < 400 and 200 < mouse_y < 400:
        pygame.draw.rect(surface, GREY, (205,205,190,190))

    elif 200 < mouse_x < 400 and 400 < mouse_y < 600:
        pygame.draw.rect(surface, GREY, (205,405,190,190))

    elif 400 < mouse_x < 600 and 0 < mouse_y < 200:
        pygame.draw.rect(surface, GREY, (405,5,190,190))

    elif 400 < mouse_x < 600 and 200 < mouse_y < 400:
        pygame.draw.rect(surface, GREY, (405,205,190,190))

    elif 400 < mouse_x < 600 and 400 < mouse_y < 600:
        pygame.draw.rect(surface, GREY, (405,405,190,190))

# Fill a cell with the input value
def fillArrayUserInput(mouse_x, mouse_y, value, array):
    # Top left cell
    if 0 < mouse_x < 200 and 0 < mouse_y < 200:
        array[0] = int(value) 

    # Middle left cell
    elif 0 < mouse_x < 200 and 200 < mouse_y < 400:
        array[3] = int(value)

    # Bottom left cell
    elif 0 < mouse_x < 200 and 400 < mouse_y < 600:
        array[6] = int(value)

    # Top middle cell
    elif 200 < mouse_x < 400 and 0 < mouse_y < 200:
        array[1] = int(value)

    # Middle middle cell
    elif 200 < mouse_x < 400 and 200 < mouse_y < 400:
        array[4] = int(value)

    # Bottom middle cell
    elif 200 < mouse_x < 400 and 400 < mouse_y < 600:
        array[7] = int(value)

    # Top right cell 
    elif 400 < mouse_x < 600 and 0 < mouse_y < 200:
        array[2] = int(value)
    
    # Middle right cell
    elif 400 < mouse_x < 600 and 200 < mouse_y < 400:
        array[5] = int(value)

    # Bottom right cell
    elif 400 < mouse_x < 600 and 400 < mouse_y < 600:
        array[8] = int(value)

# A helper function for displaying the value in each cell
def displayCell(value, center, surface):
    font = pygame.font.Font('freesansbold.ttf', 64)

    # Make sure the 0 is red so that it stands out
    if value == 0:
        cellText = font.render(str(value), True, RED, WHITE)
    else:
        cellText = font.render(str(value), True, BLACK, WHITE)

    cellRect = cellText.get_rect()
    cellRect.center = center
    surface.blit(cellText, cellRect)

# Display the values in the board
def displayBoard(board_array, surface):
    setBoard(surface)
    # Display top row
    displayCell(board_array[0], (100, 100), surface)
    displayCell(board_array[1], (300, 100), surface)
    displayCell(board_array[2], (500, 100), surface)

    # Display middle row
    displayCell(board_array[3], (100, 300), surface)
    displayCell(board_array[4], (300, 300), surface)
    displayCell(board_array[5], (500, 300), surface)

    # Display bottom row
    displayCell(board_array[6], (100, 500), surface)
    displayCell(board_array[7], (300, 500), surface)
    displayCell(board_array[8], (500, 500), surface)

def main():
    # Initial empty array for the board
    inputArray = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

    # Setup the window that displays the board
    pygame.init() # Initialize pygame
    windowSurface = pygame.display.set_mode((DISPLAYSIZE, DISPLAYSIZE)) # Create pygame window
    clock = pygame.time.Clock() # Set the clock
    pygame.display.set_caption('8-Tile Puzzle Solver') # Set the title of the window

    # Set flags and loop count for slowing the display of the solution
    loopCount = 0
    boardFull = False
    beginFlag = False
    endFlag = False
    solved = False

    # Display the empty board and starting prompt
    displayBoard(inputArray, windowSurface)
    printHeader('Click to select a cell!', windowSurface)

    # main game loop
    while True:
        mouseClick = False
        puzzle = Puzzle.PuzzleState(inputArray)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                mouseClick = True
                selectedTile = False
                displayBoard(inputArray, windowSurface)

                # show selected cell
                if selectedTile == False:
                    showClickedCell(mouseX, mouseY, windowSurface)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    input = 0
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)
                
                elif event.key == pygame.K_1:
                    input = 1
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_2:
                    input = 2
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_3:
                    input = 3
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_4:
                    input = 4
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_5:
                    input = 5
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_6:
                    input = 6
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_7:
                    input = 7
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_8:
                    input = 8
                    fillArrayUserInput(mouseX, mouseY, input, inputArray)
                    displayBoard(inputArray, windowSurface)

                elif event.key == pygame.K_SPACE and beginFlag == False:
                    beginFlag = True

                    if solved == False:
                        # puzzle = Puzzle.PuzzleState(inputArray) # initialize the backend puzzle
                        solutionPath = puzzle.aStar() # return the last TileGameNode object for tracing the path
                        solutionPath.pop(0) # remove the board already being displayed
                        solved = True
                    
                    if endFlag == False:
                        setBoard(windowSurface)

                        # Display the input array
                        displayBoard(inputArray, windowSurface)

        # Begin showing the solution to the puzzle
        if loopCount % 250 == 0 and solved == True:
            if len(solutionPath) != 0:
                displayBoard(solutionPath.pop(0).puzzle_board, windowSurface)
            else:
                printHeader('YOU HAVE SOLVED THE PUZZLE!', windowSurface)
                endFlag = True

        # Checks to see if the board can be solved and isn't currently being solved
        if puzzle.isSolvable() and beginFlag == False:
            printHeader('This can be solved! Press space!', windowSurface)

        loopCount += 1
        clock.tick()
        pygame.display.update()

if __name__ == "__main__":
    main()
