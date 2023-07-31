import requests
import datetime
import time
import json
from pybit.unified_trading import HTTP
from config import ByBitBotConfig

order_size = ByBitBotConfig.order_size
api_key = ByBitBotConfig.api_key
secret_key = ByBitBotConfig.api_secret
bar_num = ByBitBotConfig.bar_num
period = ByBitBotConfig.period
threshold_range = ByBitBotConfig.threshold_range

class ByBitBot:
    """
    ByBitボットのクラス。注文処理をおこなう。
    毎分単純移動平均線を更新し、売買シグナルが発生するかを確認する。
    """

    def __init__(self, order_size: int, api_key: str, api_secret: str, bar_num: int, period: int, threshold_range: float):
        """
        ByBitクラスの初期化処理

        Parameters
        ----------
        order_size : int
            発注サイズ(USDT)
        api_key : str
            BybitのAPIキー
        api_secret : str
            BybitのAPIシークレットキー
        bar_num : int
            処理対象となるbar(足)の期間
        period : int
            移動平均線で利用するbar(足)の数
        threshold_range : float
            Long/Shortの判断となる閾値の係数
        """
        # HTTPセッションの初期化
        session = HTTP(
            testnet = False,
            api_key = api_key,
            api_secret = api_secret,
        )
        self.server_minute = 0
        self.server_second = 0
        self.order_size = order_size
        self.bar_num = bar_num
        self.period = period
        self.threshold_range = threshold_range
        print(self.server_minute, self.server_second)

    def get_bybit_server_time(self):
        """
        Bybitのサーバータイムを取得する

        Returns
        -------
        dt.minute : int
            Bybitサーバタイムの現在分
        dt.second : int
            Bybitサーバタイムの現在秒
        """
        url = 'https://api.bybit.com'
        endpoint = '/v5/market/time'
        res = requests.get(url + endpoint)
        res_dict = json.loads(res.text)
        bybit_unixtime = res_dict["result"]["timeSecond"]
        dt = datetime.datetime.fromtimestamp(int(bybit_unixtime))
        return dt.minute, dt.second

    def check_position(self):
        """
        現在の保有ポジションを確認する
        """
        pass

    def calculate_sma(self, period: int):
        """
        パラメータ値の単純移動平均線を算出する

        Parameters
        ----------
        period : int
            単純移動平均線の期間

        Returns
        -------


        """
        pass

    def buy_sell_decision(self, previous_close_price: int, buy_threshold: float, sell_threshold: float):
        """
        PAXG/GOLDが単純移動平均線を基準とした閾値を超えた際に売買をおこなう

        Parameters
        ----------
        previous_close_price : int
            直近の終値
        buy_threshold : float
            価格が「SMA * buy_threshold」の計算値以下になったらLong判断をおこなう
        sell_threshold : float
            価格が「SMA * sell_threshold」の計算値以上になったらShort判断をおこなう
        
        Returns
        -------
        amount : int
            Long判断:1, Short判断:-1, Other:0
        """
        pass

    def order():
        """
        
        """
        pass

    def start_bot(self):
        self.server_minute, self.server_second = self.get_bybit_server_time()
        while True:
            # Bybitサーバータイムを取得して1分経過したことを確認
            new_minute, new_second = self.get_bybit_server_time()
            if self.server_minute == new_minute:
                sleep_second = max(1, 60 - new_second)
                time.sleep(sleep_second)
                continue

            # サーバータイムの分と秒を更新
            self.server_minute = new_minute
    
            # ccxtで○分足を取得する
            
            # 移動平均線を計算する
            #calculate_sma(self.period)
    
            # 売買判断をおこなう
            #previous_close_price = ○分足の直前の終値
            #buy_threshold = 移動平均線の直近の値 * self.threshold_range
            #sell_threshold = 移動平均線の直近の値 * self.threshold_range
            #buy_sell_direction = buy_sell_decision(previous_close_price, buy_threshold、sell_threshold)
            
            # 売買を行う場合の処理
            #if buy_sell_direction != 0:
                # 現在の保有ポジションを確認する
                #quantity_held = check_position()
                
                # 保有ポジションがある場合にはポジションを手仕舞う
                #[保有ポジションを閉じる処理]

                # 成行注文をおこなう
                #order_quantity = self.order_size * buy_sell_direction
                #order(order_quantity)
    


if __name__ == '__main__':
    system = ByBitBot(order_size, api_key, secret_key, bar_num, period, threshold_range)
    system.start_bot()