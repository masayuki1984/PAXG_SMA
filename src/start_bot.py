from pybit.unified_trading import HTTP
from config import ByBitBotConfig

api_key = ByBitBotConfig.apiKey
secret_key = ByBitBotConfig.secretKey

class ByBitBot:
    """
    ByBitボットのクラス。注文処理をおこなう。
    """

    def __init__(api_key, api_secret):
        """
        ByBitクラスの初期化処理

        Parameters
        ----------
        api_key : str
            BybitのAPIキー
        api_secret : str
            BybitのAPIシークレットキー
        """
        # HTTPセッションの初期化
        session = HTTP(
            testnet = False,
            api_key = api_key,
            api_secret = api_secret,
        )

    def check_position():
        """
        現在の保有ポジションを確認する
        """
        pass

    def calculate_sma():
        """
        パラメータ値の単純移動平均線を算出する

        Parameters
        ----------

        Returns
        -------


        """
        pass

    def buy_sell_decision():
        """
        PAXG/GOLDが単純移動平均線を基準とした閾値を超えた際に売買をおこなう

        Parameters
        ----------
        buy_threshold : float
            価格が「SMA * buy_threshold」の計算値以下になったらLong判断をおこなう
        sell_threshold : float
            価格が「SMA * sell_threshold」の計算値以上になったらShort判断をおこなう
        
        Returns
        -------

        """
        pass


if __name__ == '__main__':
    system = ByBitBot(api_key, secret_key)
    system