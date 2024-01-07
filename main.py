import pygame
from display_draw import Display
import player
import enemy

pygame.init()

board_width = 600
board_height = 600

clock = pygame.time.Clock()
enemy_list = []
enemy_counter = 0

if __name__ == '__main__':
    direction_of_movement = 0
    game_over = False

    pygame.display.set_caption('Avoider')
    board = Display(board_width, board_height)
    surface = board.draw_board()

    player_square = player.Player()
    if len(enemy_list) == 0:
        enemy_list.append(enemy.Enemy())
    else:
        while len(enemy_list) != enemy_counter:
            enemy_list.append(enemy.Enemy())

    while not game_over:
        surface.fill(pygame.color.THECOLORS['azure2'])
        delta_time = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    direction_of_movement = event.key

        player_square.draw_player(surface)
        enemy_list[0].draw_enemy(surface)
        player_square.player_move(delta_time, direction_of_movement)
        enemy_list[0].draw_bullet(surface, delta_time)
        pygame.display.update()
        # clock.tick(30)
    pygame.quit()
    quit()