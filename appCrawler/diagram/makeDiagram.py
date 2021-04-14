import matplotlib.pyplot as plt
from datetime import datetime


class Diagram(object):
    def __init__(self, date, title):
        self._date = date
        self._title = title

    def draw(self):
        time_list = ["14 16:20","14 16:21","14 16:25","14 16:30"]
        x = [datetime.strptime(x, "%d %H:%M") for x in time_list]
        y = [1, 2, 3, 5]
        y2 = [0, 9, 2, 3]
        plt.title(self._title)
        plt.xlabel("Time")
        plt.plot(x, y, "--",color="blue",label="audience")
        plt.plot(x, y2, "-",color="green", label="comments")
        plt.legend()
        plt.show()