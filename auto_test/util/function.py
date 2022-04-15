import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
###启动浏览器
class browser():
    ###启动
    def launch(url):
        ###启动参数
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        ###启动
        browser = webdriver.Chrome(chrome_options=options)
        browser.get(url)
        return browser

###调用钉钉api
class DingTalk_Base(object):
    def __init__(self):
        self.__headers = {'Content-Type': 'application/json;charset=utf-8'}
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, config.ding().secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        urll=config.ding().webhook+'&timestamp={}&sign={}'
        self.url =urll.format(timestamp, sign)

    def send_msg(self, text):
        json_text = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": [
                    ""
                ],
                "isAtAll": False
            }
        }
        return requests.post(self.url, json.dumps(json_text), headers=self.__headers).content

class DingTalk_Disaster(DingTalk_Base):
    def __init__(self):
        super(DingTalk_Disaster, self).__init__()


logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename='chuz_exp.log',
                            filemode='a',
                            format=
                            '%(asctime)s    %(message)s'
                            # 日志格式
                            )