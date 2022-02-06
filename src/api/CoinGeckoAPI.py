import datetime
import pandas as pd
from . import API

class CoinGeckoAPI(API.API):
    base_api_path = "https://api.coingecko.com/api/v3/"
    def __init__(self, time_out=60, sleep=5, good_result = [200]):
        super().__init__(time_out, sleep, good_result)
    
    def endpoint_price_market_cap_volume(self, date_time_from, date_time_to):
        return f"{self.base_api_path}coins/bitcoin/market_chart/range?vs_currency=usd&from={self.unit_timestamp(date_time_from)}&to={self.unit_timestamp(date_time_to)}"
    
    def get_closing_prices(self, _date_time_from, _date_time_to, period):
        '''
        _date_time_to is exclusive
        '''
        if _date_time_from > _date_time_to:
            raise Exception("_date_time_to is bigger than _date_time_from")
        if period == 'day':
            date_time_from = datetime.datetime(year=_date_time_from.year, month=_date_time_from.month, day=_date_time_from.day)
            date_time_to = datetime.datetime(year=_date_time_to.year, month=_date_time_to.month, day=_date_time_to.day)
            prices = [(i,j) for i,j in self.get_response(self.endpoint_price_market_cap_volume(date_time_from, date_time_to))['prices']]
        elif period == 'week':
            date_time_from = datetime.datetime(year=_date_time_from.year, month=_date_time_from.month, day=_date_time_from.day) + datetime.timedelta(days = 6 - datetime.date.weekday(_date_time_from))
            date_time_to = datetime.datetime(year=_date_time_to.year, month=_date_time_to.month, day=_date_time_to.day) + datetime.timedelta(days = 6 - datetime.date.weekday(_date_time_to))
            prices = [(i,j) for i,j in self.get_response(self.endpoint_price_market_cap_volume(date_time_from, date_time_to))['prices'] if datetime.datetime.weekday(datetime.datetime.fromtimestamp(i/1000)) == 6]
        else:
            raise Exception("The only viable periods are day and week")
        df = pd.DataFrame(columns=['date','price'])
        df.loc[len(df)] = prices[0]
        for i,j in prices:
            if datetime.datetime.fromtimestamp(i/1000).day == date_time_from.day and datetime.datetime.fromtimestamp(i/1000).month == date_time_from.month and datetime.datetime.fromtimestamp(i/1000).year == date_time_from.year:
                df.loc[len(df)-1] = [datetime.datetime.fromtimestamp(i/1000),j]
            else:
                date_time_from = datetime.datetime.fromtimestamp(i/1000)
                df.loc[len(df)] = [datetime.datetime.fromtimestamp(i/1000),j]
        return df