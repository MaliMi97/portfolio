import datetime
import pandas as pd
from . import API

class GlassnodeAPI(API.API):
    base_api_path = "https://api.glassnode.com/"
    def __init__(self, key, time_out=60, sleep=5, good_result = [200]):
        super().__init__(time_out, sleep, good_result)
        self.key = key

    def get_dataframe(self, response, column_names):
        df = pd.DataFrame(response)
        df.columns = column_names
        df['time'] = df['time'].apply(datetime.datetime.fromtimestamp)
        return df

    def get_closing_price(self, coin='btc'):   
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/price_usd_close', {'a': coin, 'api_key': self.key}),\
                ['time', 'price'])

    def get_market_cap(self, coin='btc'):
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/marketcap_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'market cap'])

    def get_realized_price(self, coin='btc'):
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/price_realized_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'realized price'])

    def get_realized_cap(self, coin='btc'):
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/marketcap_realized_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'realized cap'])

    def get_price_realized_price(self, coin='btc'):
        return self.get_closing_price().merge(self.get_realized_price(), on='time')
    

    

