import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 200
HEIGHT = 200

change = 0
time = 0

class tea_template:
    def __init__(self, avans, mes):
        self.avans = 0
        self.mes = ' '

    def put(self, money):
        self.avans += money

    def choice(self, lemon):
        global change
        if not lemon:
            if self.avans >= 4:
                self.mes = 'Ваш чай готов'
                self.avans -= 4
                change = self.avans
                self.avans = 0
                timer.start()

                return (self.avans)

            else:
                self.mes = 'Недостаточно средств'
                change = 0
                timer.start()

        if lemon:
            if self.avans >= 3:
                self.mes = 'Ваш чай готов'
                self.avans -= 3
                change = self.avans
                self.avans = 0
                timer.start()

                return (self.avans)

            else:
                self.mes = 'Недостаточно средств'
                change = 0
                timer.start()

    def text(self):
        return(self.mes)


def put1():
    global time
    me.put(1)
    time = 0
    change = 0

def put2():
    global time
    me.put(2)
    time = 0
    change = 0

def put5():
    global time
    me.put(5)
    time = 0
    change = 0

def get_tea():
    global change
    me.choice(True)

def get_tea_lemon():
    global change
    me.choice(False)

def tick():
    global time
    time += 1

def draw(canvas):

    if time >= 5:
        me.mes = 'Внесите аванс'

    canvas.draw_text("Аванс : "+str(me.avans)+" руб.", [10, HEIGHT / 4], 18, 'Black')
    canvas.draw_text(str(me.text()), [10, HEIGHT / 2], 18, 'Black')

    if change > 0:
        canvas.draw_text("Сдача : "+str(change)+" руб.", [10, 3 * HEIGHT / 4], 18, 'Black')


frame = simplegui.create_frame("Чайный автомат", WIDTH, HEIGHT, 200)
frame.add_label("Опущены:", 200)
frame.add_button("1 руб.", put1)
frame.add_button("2 руб.", put2)
frame.add_button("5 руб.", put5)
me = tea_template(0, ' ')
frame.add_label("", 200)
frame.add_label("Налить:", 200)
frame.add_button("Чай (3 руб.)", get_tea)
frame.add_button("Чай c лимоном (4 руб.)", get_tea_lemon)
timer = simplegui.create_timer(1000, tick)
timer.start()
frame.set_canvas_background("White")

frame.set_draw_handler(draw)

frame.start()
