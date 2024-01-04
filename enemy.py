import pygame
import board_objects

class Enemy(board_objects.Square_object):

    def __init__(self, side_dimension: int = 10, position_x: int = 0, position_y: int = 100, enemy_color: str = 'firebrick3'):
        super().__init__(side_dimension, position_x, position_y)
        self.enemy_color = pygame.color.THECOLORS[enemy_color]
        self.bullet_color = pygame.color.THECOLORS['gold']
        self.bullet_position = [[self.position_x + self.side_dimension, self.position_y]]
        self.bullet_base_speed = 100
        self.bullet_speed_multiplicator = 2

    def create_enemy_square(self, surface):
            pygame.draw.rect(surface, self.enemy_color,(self.position_x, self.position_y, self.side_dimension, self.side_dimension))


    def create_square_bullet(self, surface, delta_time):
        pygame.draw.rect(surface, self.bullet_color,(self.bullet_position[0][0], self.bullet_position[0][1], self.side_dimension, self.side_dimension))
        self.bullet_position[0][0] += self.bullet_base_speed * self.bullet_speed_multiplicator * delta_time