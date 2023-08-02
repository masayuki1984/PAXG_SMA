import requests
import datetime
import time
import json
from pybit.unified_trading import HTTP
from config import ByBitBotConfig

symbol = ByBitBotConfig.symbol
order_size = ByBitBotConfig.order_size
api_key = ByBitBotConfig.api_key
secret_key = ByBitBotConfig.api_secret
interval = ByBitBotConfig.interval
period = ByBitBotConfig.period
threshold_range = ByBitBotConfig.threshold_range

class ByBitBot:
    """
    ByBitボットのクラス。注文処理をおこなう。
    毎分単純移動平均線を更新し、売買シグナルが発生するかを確認する。

    Attributes
    ----------
    symbol : str
        暗号通貨のシンボル名
    server_minute : int
        Bybitサーバーの現在分
    server_second : int
        Bybitサーバーの現在秒
    order_size : int
        発注サイズ(USDT)
    api_key : str
        BybitのAPIキー
    api_secret : str
        BybitのAPIシークレットキー
    interval : int
        処理対象となるbar(足)の期間
    period : int
        移動平均線で利用するbar(足)の数
    threshold_range : float
        Long/Shortの判断となる閾値の係数
    """

    def __init__(self, symbol: str, order_size: int, api_key: str, api_secret: str, interval: int, period: int, threshold_range: float):
        """
        ByBitクラスの初期化処理

        Parameters
        ----------
        symbol : str
            暗号通貨のシンボル名
        order_size : int
            発注サイズ(USDT)
        api_key : str
            BybitのAPIキー
        api_secret : str
            BybitのAPIシークレットキー
        interval : int
            処理対象となるbar(足)の期間
        period : int
            移動平均線で利用するbar(足)の数
        threshold_range : float
            Long/Shortの判断となる閾値の係数
        """
        # HTTPセッションの初期化
        self.session = HTTP(
            testnet = False,
            api_key = api_key,
            api_secret = api_secret,
        )
        self.server_minute = 0
        self.server_second = 0
        self.symbol = symbol
        self.order_size = order_size
        self.interval = interval
        self.period = period
        self.threshold_range = threshold_range

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

    def get_bybit_kline(self, start_time: int, end_time: int):
        """
        引数で渡された期間のヒストリカルデータを取得する

        Parameters
        ----------
        start_time : int
            ヒストリカルデータを取得する開始期間
        end_time : int
            ヒストリカルデータを取得する終了期間
        
        Returns
        historical_data : list
            指定期間のヒストリカルデータ
        """
        historical_data = self.session.get_kline(
            category="linear",
            symbol=self.symbol,
            interval=self.interval,
            start=start_time,
            end=end_time,
            limit=self.interval*self.period
        )
        return historical_data["result"]["list"]
        

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
    
            # SMA期間のohlcを取得する
            temp_end_time = datetime.datetime.now()
            temp_start_time = temp_end_time + datetime.timedelta(minutes=-(self.interval*self.period))
            start_time = int(str(int(temp_start_time.timestamp())) + '000')
            end_time = int(str(int(temp_end_time.timestamp())) + '000')
            
            historical_data = self.get_bybit_kline(start_time, end_time)
            
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
    system = ByBitBot(symbol, order_size, api_key, secret_key, interval, period, threshold_range)
    system.start_bot()