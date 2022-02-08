import datetime
import pandas as pd
from . import API

class GlassnodeAPI(API.API):
    '''
    Class that connects to the API of https://glassnode.com/
    In order to access the api, there is need for API key, which you can get from the glassnode website.
    '''
    base_api_path = "https://api.glassnode.com/"
    def __init__(self, key, time_out=60, sleep=5, good_result = [200]):
        super().__init__(time_out, sleep, good_result)
        self.key = key

    def get_dataframe(self, response, column_names, period):
        '''
        Makes a data frame from a response and changes it, so that it contains either daily or weekly data. Also changes the names of columns.
        '''
        df = pd.DataFrame(response)
        df.columns = column_names
        df['time'] = df['time'].apply(datetime.datetime.fromtimestamp)
        if period == 'day':
            pass
        elif period == 'week':
            df = df[df['time'].apply(datetime.date.weekday) == 6]
            df = df.reset_index()
            df = df.drop(['index'],axis=1)
        else:
            raise Exception("The only viable periods are day and week")
        return df

    def get_closing_price(self, coin='btc', period='day'):  
        '''
        Returns dataframe containing either daily (period='day') or weekly (period='week') closing price of a coin (default is bitcoin).
        ''' 
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/price_usd_close', {'a': coin, 'api_key': self.key}),\
                ['time', 'price'], period)

    def get_market_cap(self, coin='btc', period='day'):
        '''
        Returns dataframe containing either daily (period='day') or weekly (period='week') market cap of a coin (default is bitcoin).
        ''' 
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/marketcap_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'market cap'], period)

    def get_realized_price(self, coin='btc', period='day'):
        '''
        Returns dataframe containing either daily (period='day') or weekly (period='week') realized price of a coin (default is bitcoin).
        ''' 
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/price_realized_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'realized price'], period)

    def get_realized_cap(self, coin='btc', period='day'):
        '''
        Returns dataframe containing either daily (period='day') or weekly (period='week') realized cap of coin (default is bitcoin).
        ''' 
        return self.get_dataframe(\
                self.get_response(self.base_api_path+'v1/metrics/market/marketcap_realized_usd', {'a': coin, 'api_key': self.key}),\
                ['time', 'realized cap'], period)

    def get_price_realized_price(self, coin='btc', period='day'):
        '''
        Returns dataframe containing either daily (period='day') or weekly (period='week') closing price and realized price of a coin (default is bitcoin).
        ''' 
        return self.get_closing_price(coin, period).merge(self.get_realized_price(coin, period), on='time')
    

    

