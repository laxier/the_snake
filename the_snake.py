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
SPEED = 10

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
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.color = SNAKE_COLOR
        self.direction = RIGHT
        self.next_direction = None

    def update(self, apple_location) -> bool:
        new_apple = self.move(apple_location)
        self.draw()
        return new_apple
    
    def pop(self) -> None:
        """Add a new segment at the end of the snake's body"""
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    def move(self, apple_location) -> bool:
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        new_head = (
            new_head[0] % GRID_WIDTH,
            new_head[1] % GRID_HEIGHT
        )

        if new_head == apple_location:
            self.pop() 
            return True
        
        # print(new_head, self.body)
        if new_head in self.body:
            print("collided")
            self.body = [new_head]
            return False

        self.body.insert(0, new_head)
        self.body.pop()
        return False  
    
    def draw(self) -> None:
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0] * GRID_SIZE, 
                                                  segment[1] * GRID_SIZE, 
                                                  GRID_SIZE, GRID_SIZE))



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
                                              self.location[1] * GRID_SIZE, 
                                              GRID_SIZE, GRID_SIZE))


def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT
            elif event.key == pygame.K_ESCAPE:  # Проверка на нажатие Esc
                pygame.quit()
                raise SystemExit

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    
    snake = Snake()
    apple = Apple(snake.body)

    while True:
        handle_keys(snake)
        screen.fill(BOARD_BACKGROUND_COLOR)
        
        if snake.update(apple.location):
            apple = Apple(snake.body)
        
        apple.update()
        pygame.display.flip()
        clock.tick(SPEED)
    print("Game Over!")
    pygame.quit()


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
