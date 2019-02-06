from graphics import *


class Hand(Line):
    def __int__(self):
        Line.value
        self.value = 0
        self.max_value = 60
        self.hand = Rectangle(Point(0,0), Point(0,0))

    def draw(self,win):
        self.hand.draw(win)


class HourHand(Hand):
    def __int__(self):
        self.max_value = 12


class MinuteHand(Hand):
    pass


class SecondHand(Hand):
    def _int_(self):
        self.color ='red'


class analog():
        def __init__(self):
            self.win = None
            self.face = Circle(Point(250, 250), 200)
            self.face.setFill('lightgray')
            self.face.setWidth(5)
            self.hour_hand = HourHand()
            self.minute_hand = MinuteHand()
            self.second_hand = SecondHand()
            self.second_hand = None

        def draw(self,win):
            self.win = win
            self.face.draw(win)
            # self.hour_hand.draw(win)
            # self.mintue_hand.draw(win)
            # self.second_hand.draw(win)


        def animate(self):
            self.win.after(250, self.animate)

if __name__=="__main__":
    Clock = analog()

    win= GraphWin('Clock', 500,500)
    Clock.draw(win)
    Clock.animate()
    win.mainloop()