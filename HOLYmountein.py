import pygame

WH = pygame.Color('white')  # задаем необходимые цвета
RD = pygame.Color('red')
BL = pygame.Color('blue')
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

        self.count = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_board_cell(self, coord):  # метод для смены данных в таблице
        if coord is None:  # которая служит носителем цвета для каждой клетки доски
            return None
        else:
            n, m = coord[0], coord[1]
            if not self.board[coord[1]][coord[0]]:
                self.count += 1  # переменная для чередования
                if self.count % 2 == 0:  # определяем фигуру по четности нажатия на ЛКМ
                    self.board[m][n] = 1
                    return 1
                else:
                    self.board[m][n] = 2
                    return 2

    def render(self, scrn):
        m = self.top  # задаем y

        for i in range(self.height):
            n = self.left  # задаем x
            for j in range(self.width):  # рисуем клеточку за клеточкой
                pygame.draw.rect(scrn, WH, (n, m, self.cell_size, self.cell_size), 1)
                CELLS[(j, i)] = (n, m, n + self.cell_size, m + self.cell_size)  # записываем данные о каждой клетке
                n += self.cell_size  # меняем координаты, чтобы клеточки встали на свои места
            m += self.cell_size

    def cross_cir_draw(self, coord, icon, scrn):  # рисуем крестик или нолик
        if icon:
            cell_area = CELLS[coord]  # берем данные о клетке, на которую нажили
            # и на основе этих данных высчитываем положение и размеры фигуры
            if icon == 2:  # рисуем нолик
                n = cell_area[0] + ((cell_area[2] - cell_area[0]) * 0.5)  # высчитываем необходимые величины
                m = cell_area[1] + ((cell_area[3] - cell_area[1]) * 0.5)
                radius = ((cell_area[2] - cell_area[0]) * 0.5) - 2
                pygame.draw.circle(scrn, RD, (int(n), int(m)), int(radius), width=3)  # и отрисовываем

            if icon == 1:  # рисуем крестик
                n = cell_area[0] + 2
                m = cell_area[1] + 2
                n1 = n + (cell_area[2] - cell_area[0]) - 4
                m1 = m + (cell_area[3] - cell_area[1]) - 4
                pygame.draw.line(scrn, BL, (n, m), (n1, m1), width=3)  # задал большую ширину линии для большей
                pygame.draw.line(scrn, BL, (n1, m), (n, m1), width=3)  # видимости

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

    def on_click(self, cell_poz, scrn):
        n = self.set_board_cell(cell_poz)  # узнаем из таблицы, какую фигуру рисовать
        self.cross_cir_draw(cell_poz, n, scrn)  # запускаем отрисовку

    def get_click(self, m_poz, scrn):  # получаем сигнал для отрисовки и запускаем процесс подготовки к рисованию
        coords = self.get_cell(m_poz)
        self.on_click(coords, scrn)


if __name__ == '__main__':
    board = Board(5, 7)
    board.set_view(100, 100, 50)

    pygame.init()
    size = width, height = 450, 600
    screen = pygame.display.set_mode(size)
    run = True
    clock = pygame.time.Clock()
    go = False
    pos = (0, 0)

    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                go = True  # ловим сигнал и его положение на плоскости
                pos = pygame.mouse.get_pos()

        board.render(screen)
        if go:  # даем сигнал методам, чтоб начали процесс отрисовки
            board.get_click(pos, screen)
            go = False
        pygame.display.flip()

    pygame.quit()
