import numpy as np
import pandas as pd

'''
This python script contains a function impermanent_loss, which is used to, under certain assumptions, compute the impermanent loss of yield farming.
in_lp and fiat_to_lp are auxiliary functions
'''

def in_lp(x, y, x2_price, y2_price):
    r = x2_price/y2_price
    x2 = np.sqrt(x*y/r)
    y2 = np.sqrt(x*y*r)
    return np.array([x2, y2, x2*x2_price + y2*y2_price])

def fiat_to_lp(fiat, price_x, price_y, x2_price, y2_price):
    return in_lp(fiat*0.5/price_x, fiat*0.5/price_y, x2_price, y2_price)

def impermanent_loss(df, initial_fiat):
    '''
    Computes the impermanent loss of yield farming without rehypothecation. The initial amount of tokens x, y is derived from initial_fiat and the prices
    of tokens x, y in the first row of the dataset.
    Data frame df must have the following columns: time, price_x, price_y
    The function adds additional columns to the dataset and counts the changes of fiat, how much fiat we would have if we had gone all in to token x, y or if we had gone for 50/50 split.
    It also counts how big of a percent of the initial investment we gained or lost.
    '''
    df = df.reindex(columns = df.columns.tolist() + ['fiat', 'x', 'y', 'all in x', 'all in y', '50/50', '% to x', '% to y', "% to 50/50"])
    df['fiat'].at[0] = initial_fiat
    df['x'].at[0] = 0.5*initial_fiat/df['price_x'].loc[0]
    df['y'].at[0] = 0.5*initial_fiat/df['price_y'].loc[0]
    for i in np.arange(1,len(df)):
        aux = fiat_to_lp(df['fiat'].loc[i-1], df['price_x'].loc[i-1], df['price_y'].loc[i-1], df['price_x'].loc[i], df['price_y'].loc[i])
        df['x'].at[i] = aux[0]
        df['y'].at[i] = aux[1]
        df['fiat'].at[i] = aux[2]
    df['all in x'] = df['price_x']*2*df['x'].loc[0]
    df['all in y'] = df['price_y']*2*df['y'].loc[0]
    df['50/50'] = df['price_x']*df['x'].loc[0] + df['price_y']*df['y'].loc[0]
    df['% to x'] = 100*df['fiat']/df['all in x']-100
    df['% to y'] = 100*df['fiat']/df['all in y']-100
    df['% to 50/50'] = 100*df['fiat']/df['50/50']-100
    return df