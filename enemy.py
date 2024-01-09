import pygame
import board_objects
import random

class Enemy(board_objects.Square_object):

    def __init__(self, side_dimension: int = 10, position_x: int = 0, position_y: int = 100, enemy_color: str = 'firebrick3'):
        super().__init__(side_dimension, position_x, position_y)
        self.enemy_color = pygame.color.THECOLORS[enemy_color]
        self.bullet_color = pygame.color.THECOLORS['gold']
        self.bullet_positions = [[self.position_x + self.side_dimension, self.position_y]]
        self.bullet_base_speed = 100
        self.bullet_speed_multiplicator = random.randrange(2,14,2)

    def draw_enemy(self, surface):
            pygame.draw.rect(surface, self.enemy_color,(self.position_x, self.position_y, self.side_dimension, self.side_dimension))


    def draw_bullet(self, surface, delta_time, board_width):
        for bullet_position in self.bullet_positions[:]:
            pygame.draw.rect(surface, self.bullet_color,(bullet_position[0], bullet_position[1], self.side_dimension, self.side_dimension))
            bullet_position[0] += self.bullet_base_speed * self.bullet_speed_multiplicator * delta_time
            print(bullet_position)
            if bullet_position[0] > board_width:
                self.bullet_positions.remove(bullet_position)

    def add_bullet(self):
        self.bullet_positions.append([self.position_x + self.side_dimension, self.position_y])
    @classmethod
    def add_new_enemy(cls, side_dimension: int = 10, position_x: int = 0, position_y: int = 200, enemy_color: str = 'firebrick3'):
        position_y = random.randrange(0, 590, 10)
        return cls(side_dimension, position_x, position_y, enemy_color)


