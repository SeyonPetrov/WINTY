import pygame


WH = pygame.Color('white')
BL = pygame.Color('black')
CELLS = {}  # создаем словарь для записи данных о клетках


class Board:
    # создание поля
    def __init__(self, wid, heig):
        self.width = wid
        self.height = heig
        self.board = [[0] * wid for _ in range(heig)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scrn):
        m = self.top  # задаем х

        for i in range(self.width):
            n = self.left  # задаем у

            for j in range(self.height):  # рисуем клеточку за клеточкой
                pygame.draw.rect(scrn, WH, (m, n, self.cell_size, self.cell_size), 1)
                CELLS[(i, j)] = (m, n, m + self.cell_size, n + self.cell_size)  # записываем данные о каждой клетке
                n += self.cell_size  # меняем координаты, чтобы клеточки встали на свои места

            m += self.cell_size

    @staticmethod
    def get_cell(m_poz):
        x, y = m_poz

        for z in CELLS:  # перебираем клетки по одной
            x1 = CELLS[z][0]  # собираем значения крайних Х и У для выявления области клетки
            x2 = CELLS[z][2]
            y1 = CELLS[z][1]
            y2 = CELLS[z][3]
            if x1 <= x <= x2 and y1 <= y <= y2:  # если курсор в области клетки
                return z  # выводим картеж ее названия

        return None  # выводим текст ошибки если курсор не находится в зоне доски во время нажатия

    @staticmethod
    def on_click(cell_poz):  #
        print(cell_poz)

    def get_click(self, m_poz):  #
        coords = self.get_cell(m_poz)
        self.on_click(coords)


if __name__ == '__main__':
    board = Board(5, 7)
    board.set_view(100, 100, 50)

    pygame.init()
    size = width, height = 500, 700
    screen = pygame.display.set_mode(size)
    run = True
    clock = pygame.time.Clock()
    screen.fill('green')

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed() == (1, 0, 0):  #
                board.get_click(pygame.mouse.get_pos())

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()

    pygame.quit()
