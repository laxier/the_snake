from random import choice, randint
import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class Snake:
    """The snake."""

    def __init__(self) -> None:
        self.body = [(randint(0,GRID_WIDTH), randint(0,GRID_HEIGHT))]
        self.color = SNAKE_COLOR

    def update(self) -> None:
        self.draw()

    def draw(self) -> None:
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0] * GRID_SIZE, 
                                                  segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Apple:
    """The apple."""

    def __init__(self, snake_body) -> None:
        self.location = self.spawn_apple(snake_body)
        self.color = APPLE_COLOR
    
    def spawn_apple(self, snake_body):
        while True:
            x = randint(0, GRID_WIDTH - 1)
            y = randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                return (x, y)
            
    def update(self) -> None:
        self.draw()

    def draw(self) -> None:
        pygame.draw.rect(screen, self.color, (self.location[0] * GRID_SIZE, 
                                              self.location[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))



def main():
    # Инициализация PyGame:
    pygame.init()
    snake = Snake()
    apple = Apple(snake.body)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(SPEED)
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.update()
        apple.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()


# Метод draw класса Apple
# def draw(self):
#     rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, rect)
#     pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
# def draw(self):
#     for position in self.positions[:-1]:
#         rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
#         pygame.draw.rect(screen, self.body_color, rect)
#         pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

#     # Отрисовка головы змейки
#     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, head_rect)
#     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
#         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
