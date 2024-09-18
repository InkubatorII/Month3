import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определяем фигуры тетриса
TETROMINOS = [
    [[1, 1, 1],
     [0, 1, 0]],  # T-образная фигура

    [[1, 1],
     [1, 1]],    # Квадрат

    [[1, 1, 1, 1]],  # Прямая линия

    [[1, 1, 0],
     [0, 1, 1]],  # Z-образная

    [[0, 1, 1],
     [1, 1, 0]]   # Обратная Z-образная
]

# Функция для генерации случайной фигуры
def new_tetromino():
    return random.choice(TETROMINOS)

# Функция для рисования сетки
def draw_grid(surface):
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.rect(surface, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)

# Главный игровой цикл
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Текущая фигура
    current_tetromino = new_tetromino()
    tetromino_x, tetromino_y = GRID_WIDTH // 2, 0

    running = True
    while running:
        screen.fill(BLACK)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino_x -= 1
                if event.key == pygame.K_RIGHT:
                    tetromino_x += 1
                if event.key == pygame.K_DOWN:
                    tetromino_y += 1

        # Отображение фигуры
        for y, row in enumerate(current_tetromino):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, BLUE,
                        (tetromino_x * GRID_SIZE + x * GRID_SIZE,
                         tetromino_y * GRID_SIZE + y * GRID_SIZE,
                         GRID_SIZE, GRID_SIZE))

        # Рисуем сетку
        draw_grid(screen)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
