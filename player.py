import pygame
import board_objects

class Player(board_objects.Square_object):
    def __init__(self, side_dimension: int = 10, position_x = 300, position_y = 300, player_color: str = 'darkgreen') -> None:
        super().__init__(side_dimension, position_x, position_y)
        self.player_color = pygame.color.THECOLORS[player_color]
        self.speed = 100
        self.speed_multiplier = 2
    def draw_player(self, surface):
        pygame.draw.rect(surface, self.player_color, (self.position_x, self.position_y, self.side_dimension, self.side_dimension))

    def player_move(self, delta_time, direction_of_movement):
        if direction_of_movement == pygame.K_DOWN:
            self.position_y += self.speed * self.speed_multiplier * delta_time
        elif direction_of_movement == pygame.K_UP:
            self.position_y -= self.speed * self.speed_multiplier * delta_time

    def collison_with_bullet(self, bullet_x, bullet_y, bullet_side_dimension):
        for i in range(bullet_x, bullet_x + bullet_side_dimension):
            for j in range(bullet_y, bullet_y + bullet_side_dimension):
                if self.position_x <= i < self.position_x + self.side_dimension and self.position_y <= j < self.position_y + self.side_dimension:
                    print('Przegrałeś')
                    return True
        return False