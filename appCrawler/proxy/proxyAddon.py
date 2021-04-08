import mitmproxy.http
from mitmproxy import ctx


class Dealer:
    def __init__(self):
        self.num = 0

    def request(self):
        self.num += 1
        ctx.log.info("%s request(s) catched! " % self.num)


addons = [
    Dealer()
]
