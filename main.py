import tkinter as tk


HIGHLIGHTED = 0
MATCHES_IN = 0
DRAW_RESP = False
DELETE_RESP = True
_FROM = None
_TO = None
lvl = 0


class Match:
    def __init__(self, x, y, up, tag, hl=False):
        self.drown = True
        self.hl = hl
        self.x = x
        self.y = y
        self.up = up
        self.tag = tag
        if self.up:
            self.fig1 = canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, fill='black', tags=self.tag)
            self.fig2 = canvas.create_rectangle(self.x, self.y + 5, self.x + 5, self.y + 100, fill='yellow', tags=self.tag)
        else:
            self.fig1 = canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, fill='black', tags=self.tag)
            self.fig2 = canvas.create_rectangle(self.x + 5, self.y, self.x + 100, self.y + 5, fill='yellow', tags=self.tag)

    def highlight(self, on=True):
        if on:
            if self.up:
                res = canvas.create_rectangle(self.x - 1, self.y - 1, self.x + 6, self.y + 101)
            else:
                res = canvas.create_rectangle(self.x - 1, self.y - 1, self.x + 101, self.y + 6)
            self.hl = res
        else:
            canvas.delete(self.hl)

    def delete_match(self, player=False):
        if not player:
            if self.drown:
                canvas.delete(self.fig1, self.fig2)
                self.drown = False
        else:
            global DELETE_RESP, MATCHES_IN, _FROM, _TO
            if _TO != self and _TO is not None:
                return
            if MATCHES_IN == 1:
                DELETE_RESP = False
            else:
                DELETE_RESP = True
            if self.drown and DELETE_RESP:
                canvas.delete(self.fig1, self.fig2)
                self.drown = False
                if _FROM is None:
                    _FROM = self
                MATCHES_IN += 1
            spichek_vzyato.config(text=f'Спичек взято: {MATCHES_IN}')

    def draw_match(self):
        global DRAW_RESP, MATCHES_IN, _FROM, _TO, lvl
        if MATCHES_IN == 0:
            DRAW_RESP = False
        else:
            DRAW_RESP = True
        if not self.drown and DRAW_RESP:
            if self.up:
                self.fig1 = canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, fill='black', tags=self.tag)
                self.fig2 = canvas.create_rectangle(self.x, self.y + 5, self.x + 5, self.y + 100, fill='yellow',
                                                    tags=self.tag)
            else:
                self.fig1 = canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 5, fill='black', tags=self.tag)
                self.fig2 = canvas.create_rectangle(self.x + 5, self.y, self.x + 100, self.y + 5, fill='yellow',
                                                    tags=self.tag)
            self.drown = True
            _TO = self
            if _TO == _FROM:
                _FROM = None
                _TO = None
            MATCHES_IN -= 1
            if lvl == 1 and matches_arr[13].drown and not matches_arr[14].drown:
                win.grid(row=7)
            elif lvl == 2 and matches_arr[8].drown and not matches_arr[18].drown:
                win.grid(row=7)
            elif lvl == 3 and matches_arr[18].drown and not matches_arr[8].drown:
                win.grid(row=7)
            elif lvl == 4 and matches_arr[8].drown and not matches_arr[9].drown:
                win.grid(row=7)
            elif lvl == 5 and matches_arr[11].drown and not matches_arr[10].drown:
                win.grid(row=7)
            elif lvl == 0:
                win.grid_forget()
            spichek_vzyato.config(text=f'Спичек взято: {MATCHES_IN}')


def get_prev_match(i):
    el = matches_arr[i]
    for prev, cur in list(zip(matches_arr, matches_arr[1:])) + [(matches_arr[-1], matches_arr[0])]:
        if el == cur:
            return prev


def get_next_match(i):
    el = matches_arr[i]
    for cur, next_elem in zip(matches_arr, matches_arr[1:] + [matches_arr[0]]):
        if el == cur:
            return next_elem


def draw_0(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    m4.delete_match()
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_1(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    m1.delete_match()
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    m2.delete_match()
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    m4.delete_match()
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)
    m7.delete_match()


def draw_2(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    m2.delete_match()
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    m6.delete_match()
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_3(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    m2.delete_match()
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_4(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    m1.delete_match()
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)
    m7.delete_match()


def draw_5(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    m3.delete_match()
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_6(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    m3.delete_match()
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_7(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    m2.delete_match()
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    m4.delete_match()
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)
    m7.delete_match()


def draw_8(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_9(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m1 = Match(10 + k, 10, False, '0' + str(c))
    matches_arr.append(m1)
    c += 1
    m2 = Match(5 + k, 17, True, '1' + str(c))
    matches_arr.append(m2)
    c += 1
    m3 = Match(110 + k, 17, True, '1' + str(c))
    matches_arr.append(m3)
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(5 + k, 120, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()
    c += 1
    m6 = Match(110 + k, 120, True, '3' + str(c))
    matches_arr.append(m6)
    c += 1
    m7 = Match(10 + k, 223, False, '4' + str(c))
    matches_arr.append(m7)


def draw_plus(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    c += 1
    m5 = Match(60 + k, 70, True, '3' + str(c))
    matches_arr.append(m5)


def draw_minus(pos):
    global c
    k = (pos - 1) * 120
    c += 1
    m4 = Match(10 + k, 117, False, '2' + str(c))
    matches_arr.append(m4)
    m5 = Match(60 + k, 70, True, '3' + str(c))
    matches_arr.append(m5)
    m5.delete_match()


def draw_eq():
    canvas.create_rectangle(370, 100, 375, 105, fill='black')
    canvas.create_rectangle(375, 100, 470, 105, fill='yellow')
    canvas.create_rectangle(370, 120, 375, 125, fill='black')
    canvas.create_rectangle(375, 120, 470, 125, fill='yellow')


def highlight_move(direction):
    global HIGHLIGHTED
    i = HIGHLIGHTED
    if direction == 'left':
        matches_arr[i].highlight(on=False)
        get_prev_match(i).highlight()
        if HIGHLIGHTED == 0:
            HIGHLIGHTED = len(matches_arr) - 1
        else:
            HIGHLIGHTED -= 1
    elif direction == 'right':
        matches_arr[i].highlight(on=False)
        get_next_match(i).highlight()
        if HIGHLIGHTED == len(matches_arr) - 1:
            HIGHLIGHTED = 0
        else:
            HIGHLIGHTED += 1


def start():
    global matches_arr, c, HIGHLIGHTED, MATCHES_IN, DELETE_RESP, DRAW_RESP, _FROM, _TO
    c = 0
    HIGHLIGHTED = 0
    MATCHES_IN = 0
    DRAW_RESP = False
    DELETE_RESP = True
    _FROM = None
    _TO = None
    matches_arr = []
    canvas.delete("all")
    btn1.grid_forget()
    btn2.grid_forget()
    btn3.grid_forget()
    btn4.grid_forget()
    btn5.grid_forget()
    canvas.grid(row=2, columnspan=5)
    btnm.grid(row=3)
    spichek_vzyato.config(text=f'Спичек взято: {MATCHES_IN}')
    spichek_vzyato.grid(row=0, column=2)


def main_menu():
    btn1.grid(row=4, column=0)
    btn2.grid(row=4, column=1)
    btn3.grid(row=4, column=2)
    btn4.grid(row=4, column=3)
    btn5.grid(row=4, column=4)
    menu_l.grid(row=6, columnspan=5)


def lvl1():
    global lvl
    win.grid_forget()
    lvl = 1
    start()
    draw_0(1)
    draw_plus(2)
    draw_3(3)
    draw_eq()
    draw_2(5)
    matches_arr[0].highlight()


def lvl2():
    global lvl
    win.grid_forget()
    lvl = 2
    start()
    draw_5(1)
    draw_minus(2)
    draw_1(3)
    draw_eq()
    draw_8(5)
    matches_arr[0].highlight()


def lvl3():
    global lvl
    win.grid_forget()
    lvl = 3
    start()
    draw_9(1)
    draw_plus(2)
    draw_0(3)
    draw_eq()
    draw_5(5)
    matches_arr[0].highlight()


def lvl4():
    global lvl
    win.grid_forget()
    lvl = 4
    start()
    draw_3(1)
    draw_minus(2)
    draw_7(3)
    draw_eq()
    draw_4(5)
    matches_arr[0].highlight()


def lvl5():
    global lvl
    win.grid_forget()
    lvl = 5
    start()
    draw_5(1)
    draw_plus(2)
    draw_5(3)
    draw_eq()
    draw_8(5)
    matches_arr[0].highlight()


root = tk.Tk()
root.title('Переставьте одну спичку, чтобы получить верное равенство')
matches_arr = []
btn1 = tk.Button(command=lvl1, text='lvl1')
btn2 = tk.Button(command=lvl2, text='lvl2')
btn3 = tk.Button(command=lvl3, text='lvl3')
btn4 = tk.Button(command=lvl4, text='lvl4')
btn5 = tk.Button(command=lvl5, text='lvl5')
btnm = tk.Button(command=main_menu, text='menu')
menu_l = tk.Label(text='Управление: w - убрать спичку, s - поставить, a, d - выбрать спички')
main_menu()
canvas = tk.Canvas(width=600, height=300, bg='green')
spichek_vzyato = tk.Label(text=f'Спичек взято: {MATCHES_IN}')
c = 0
win = tk.Label(text='Верно!')
root.bind('<s>', lambda event: matches_arr[HIGHLIGHTED].draw_match())
root.bind('<w>', lambda event: matches_arr[HIGHLIGHTED].delete_match(True))
root.bind('<a>', lambda event: highlight_move('left'))
root.bind('<d>', lambda event: highlight_move('right'))
root.mainloop()
