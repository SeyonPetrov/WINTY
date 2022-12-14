import pygame
import random

WH = pygame.Color('white')
RD = pygame.Color('red')
BL = pygame.Color('blue')
CELLS = {}  # создаем словарь для записи данных о клетках


class Board:
    # создание поля
    def __init__(self, wid, heig):
        self.width = wid
        self.height = heig
        self.board = []
        for _ in range(heig):
            prom = []
            for _ in range(wid):
                prom.append(random.randint(1, 2))
            self.board.append(prom)
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_board_cell(self, coord):  # меняем значения в таблице
        if coord is None:  # полчаем координаты и проверяем на явственность
            return None
        else:
            for x in range(self.height):  # меняем значения в таблице в соответсвии
                if self.board[x][coord[0]] == 1:  # с условием
                    self.board[x][coord[0]] = 2  # 0 == black
                else:
                    self.board[x][coord[0]] = 1  # 1 == white
            for z in range(self.width):
                if self.board[coord[1]][z] == 1:
                    self.board[coord[1]][z] = 2
                else:
                    self.board[coord[1]][z] = 1
            if self.board[coord[1]][coord[0]] == 1:
                self.board[coord[1]][coord[0]] = 2
            else:
                self.board[coord[1]][coord[0]] = 1

    def render(self, scrn):
        m = self.top  # задаем y

        for i in range(self.height):
            n = self.left  # задаем x
            for j in range(self.width):  # рисуем клеточку за клеточкой

                pygame.draw.rect(scrn, WH, (n, m, self.cell_size, self.cell_size), 1)
                CELLS[(j, i)] = (n, m, n + self.cell_size, m + self.cell_size)  # записываем данные о каждой клетке
                n += self.cell_size  # меняем координаты, чтобы клеточки встали на свои места

            m += self.cell_size

        for i in range(self.height):
            for j in range(self.width):
                cell_area = CELLS[(j, i)]
                n = cell_area[0] + ((cell_area[2] - cell_area[0]) * 0.5)
                m = cell_area[1] + ((cell_area[3] - cell_area[1]) * 0.5)
                radius = ((cell_area[2] - cell_area[0]) * 0.5) - 2

                if self.board[i][j] == 1:
                    color = RD
                else:
                    color = BL

                pygame.draw.circle(scrn, color, (int(n), int(m)), int(radius))

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

    def on_click(self, cell_poz):  # запускаем функцию для смены значений в таблице
        self.set_board_cell(cell_poz)

    def get_click(self, m_poz):  #
        coords = self.get_cell(m_poz)
        self.on_click(coords)


if __name__ == '__main__':
    num = int(input())
    board = Board(num, num)
    board.set_view(100, 100, 50)

    pygame.init()
    size = width, height = 800, 800
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
