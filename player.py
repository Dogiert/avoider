import pygame
import board_objects

class Player(board_objects.Square_object):
    def __init__(self, side_dimension: int = 10, position_x = 300, position_y = 300, player_color: str = 'darkgreen') -> None:
        super().__init__(side_dimension, position_x, position_y)
        self.player_color = pygame.color.THECOLORS[player_color]

    def create_player_square(self, display):
        surface = display.draw_board()
        pygame.draw.rect(surface, self.player_color, (self.position_x, self.position_y, self.side_dimension, self.side_dimension))

    def player_move_down(self):
        self.position_y += 20