import mitmproxy.http
import re
import msg_pb2
import payload_pb2
import userinfo_pb2
from datetime import datetime
import json
import threading


class Dealer:
    def __init__(self):
        self._num = 0
        self._start = datetime.now()
        self._minute = self._start.minute
        self._viewer = list()
        self._comment = 0
        self._filename = "../storage/" + datetime.strftime(datetime.now(), "%Y-%m-%d") + ".json"

    #   需要修改请求时可以使用
    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     if flow.request.host == "webcast.amemv.com" \
    #             and re.match("^/webcast/im/fetch.*$", flow.request.path):
    #         print("catch!")cd
    #         print(flow.response)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 每分钟储存一次记录
        now = datetime.now()
        if now.minute != self._minute and len(self._viewer) > 0:
            with open(self._filename, "a") as f:
                json.dump({
                    "viewer": int(sum(self._viewer) / len(self._viewer)),
                    "comment": self._comment,
                    "time": now.strftime("%d %H%M")
                }, f)
                f.write("\n")
            self._minute = now.minute
            self._viewer = list()
            self._comment = 0
            print("存储记录啦")
        if flow.request.host == "webcast.amemv.com" \
                and re.match("^/webcast/im/fetch.*$", flow.request.path):
            msg = msg_pb2.Response()
            msg.ParseFromString(flow.response.content)
            for x in msg.messages:
                # print(x.method)
                if x.method == "WebcastChatMessage":
                    payload = payload_pb2.Detail()
                    payload.ParseFromString(x.payload)
                    user = payload.info
                    t1 = threading.Thread(target=save_comment, args=(user.username, user.userId1, payload.chatMessage))
                    t1.start()
                    print("%s(%s | %s) : %s" % (user.username, user.userId1, user.userId2, payload.chatMessage))
                    self._comment += 1

                # 点赞真不真？
                elif x.method == "WebcastLikeMessage":
                    pass
                # 到底有几个人？
                elif x.method == "WebcastRoomUserSeqMessage":
                    user_info = userinfo_pb2.userResponse()
                    user_info.ParseFromString(x.payload)
                    self._viewer.append(user_info.total)
                    print("直播间人数 %d" % user_info.total)


lock = threading.Lock()


def save_comment(userid, username, comment):
    lock.acquire()
    try:
        with open("../storage/" + "comment.log", "a") as file:
            file.write(u"%s:%s:%s\n" % (userid, username, comment))
    finally:
        lock.release()


addons = [
    Dealer()
]
