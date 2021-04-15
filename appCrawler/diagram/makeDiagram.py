import matplotlib.pyplot as plt
from datetime import datetime
import json


class Diagram(object):
    def __init__(self, title="Stream Statistics",
                 date=datetime.now().strftime("%Y-%m-%d")):
        self._date = date
        self._title = title

    def draw(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        filename = "./appCrawler/storage/" + self._date + ".json"
        time_list = []
        audience = []
        comment = []
        with open(filename, "r") as file:
            for x in file.readlines():
                data = json.loads(x, object_hook=mapping)
                time_list.append(data.time)
                audience.append(data.audience)
                comment.append(data.comment)
        x = [datetime.strptime(x, "%d %H%M") for x in time_list]
        y1 = audience
        y2 = comment

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y1, '-', color="blue", label=u'观看人数')

        ax2 = ax.twinx()
        ax2.plot(x, y2, '--',color="green", label=u'弹幕数')
        fig.legend(loc=1)

        ax.set_xlabel("时间")
        ax.set_ylabel(u"观看人数")
        ax2.set_ylabel(u"弹幕数")

        plt.grid()
        plt.show()


def mapping(data):
    try:
        crawler = CrawlerData(data['viewer'], data['comment'], data['time'])
    except:
        print("Incorrect data structure")
        print(data)
        return None
    return crawler


class CrawlerData(object):
    def __init__(self, audience, comment, time):
        self._audience = audience
        self._comment = comment
        self._time = time

    @property
    def audience(self):
        return self._audience

    @property
    def comment(self):
        return self._comment

    @property
    def time(self):
        return self._time
