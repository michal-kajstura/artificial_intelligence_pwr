from Assignment_3.connect4.gui import GUI

_COLOR = (0, 0, 255)
COLUMN_COUNT = 7
ROW_COUNT = 6
SQUARESIZE = 100

TEXT_COLOR = (255, 255, 255)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

gui = GUI(width, height)
gui.display_menu()
