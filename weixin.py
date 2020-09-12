import requests
import json
import time
import pandas as pd
import ast

'''
企业微信建立第三方应用，通过第三方应用发送消息
def _get_access_token(self)      内置的函数，获取access_token
def get_access_token(self)       通过判断超时，避免重复获取access_token
def send_msg(self, touser, content)   发送消息
'''


class weixin(object):
    def __init__(self):
        self.corpid = self._get_interface_data()['corpid']
        self.secret = self._get_interface_data()['secret']
        self.agentid = self._get_interface_data()['agentid']
        self.addressbook = pd.read_excel(".\\tmp\\addressbook.xlsx", skiprows=8, index_col="姓名")

    # 获取接口数据
    def _get_interface_data(self):
        with open('.//tmp//interface_data.conf', 'r') as f:
            result=ast.literal_eval(f.read())
        return result


    # 获取access_token
    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.corpid,
                  'corpsecret': self.secret,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        return data["access_token"]

    # 获取access_token
    def get_access_token(self):
        try:
            with open('.//tmp//access_token.conf', 'r') as f:
                t, access_token = f.read().split()
        except Exception:
            with open('.//tmp//access_token.conf', 'w') as f:
                access_token = self._get_access_token()
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('.//tmp//access_token.conf', 'w') as f:
                    access_token = self._get_access_token()
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token

    # 获取userid
    def _get_userid(self, usrname):
        userid = self.addressbook.loc[usrname][0]
        return userid

    # 发送消息
    def send_msg(self, usrname, content):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        touser = self._get_userid(usrname)
        send_values = {
            "touser": touser,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": content
            },
            "safe": "1"
        }
        send_msges = (bytes(json.dumps(send_values), 'utf-8'))
        response = requests.post(send_url, send_msges)
        response = response.json()
        return response["errmsg"]

if __name__ == '__main__':
    corpid = 'ww04a727bae922b603'
    secret = 'LRscPQv4flpwOHm2t_IND9yv3GMPSsy10fVjEGZTI_Y'
    agentid = '1000016'
    winxin = weixin().get_access_token()

