import mitmproxy.http
import re
import msg_pb2
import payload_pb2


class Dealer:
    def __init__(self):
        self.num = 0

    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     if flow.request.host == "webcast.amemv.com" \
    #             and re.match("^/webcast/im/fetch.*$", flow.request.path):
    #         print("catch!")
    #         print(flow.response)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "webcast.amemv.com" \
                and re.match("^/webcast/im/fetch.*$", flow.request.path):
            msg = msg_pb2.Response()
            msg.ParseFromString(flow.response.content)
            for x in msg.messages:
                # print(x.method)
                if x.method == "WebcastChatMessage":
                    payload = payload_pb2.Detail()
                    payload.ParseFromString(x.payload)
                    user = payload.Type()
                    print(payload.chatMessage)

addons = [
    Dealer()
]
