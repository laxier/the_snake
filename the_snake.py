import random
import pygame

# Константы для размеров поля и сетки
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки
SPEED = 20


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position, color):
        """
        Инициализирует игровой объект.

        :param position: Начальная позиция объекта
        :param color: Цвет объекта
        """
        self.position = position
        self.color = color

    def draw(self, surface):
        """
        Отрисовывает объект на игровой поверхности.

        :param surface: Поверхность для отрисовки
        """
        rect = pygame.Rect(
            self.position[0] * GRID_SIZE,
            self.position[1] * GRID_SIZE,
            GRID_SIZE, GRID_SIZE
        )
        pygame.draw.rect(surface, self.color, rect)


class Apple(GameObject):
    """Класс, представляющий яблоко в игре."""

    def __init__(self):
        """Инициализирует яблоко в случайной позиции."""
        super().__init__(self.randomize_position(), APPLE_COLOR)

    def randomize_position(self):
        """Устанавливает случайную позицию для яблока."""
        return (random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1))


class Snake(GameObject):
    """Класс, представляющий змейку в игре."""

    def __init__(self):
        """Инициализирует змейку в начальном состоянии."""
        start_position = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
        super().__init__(start_position, SNAKE_COLOR)
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Перемещает змейку на одну клетку."""
        head = self.get_head_position()
        x, y = self.direction
        new = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None

    def draw(self, surface):
        """
        Отрисовывает змейку на игровой поверхности.

        :param surface: Поверхность для отрисовки
        """
        for position in self.positions:
            GameObject(position, self.color).draw(surface)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]


def handle_keys(snake):
    """
    Обрабатывает нажатия клавиш для управления змейкой.

    :param snake: Объект змейки
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple = Apple()

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()
        clock.tick(SPEED)


if __name__ == '__main__':
    main()
