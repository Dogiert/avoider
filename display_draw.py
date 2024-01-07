import pygame

class Display:
    
    def __init__(self, width: int = 400, height: int = 400) -> None:
        self.width = width
        self.height = height
        
    def draw_board(self):
        board = pygame.display.set_mode((self.width, self.height))
        board.fill(pygame.color.THECOLORS['azure2'])
        return board
