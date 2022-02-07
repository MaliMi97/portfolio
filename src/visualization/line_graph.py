from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd

def with_price_in_background(time, price, width=5, height=5, _fontsize=40):
    fig = plt.figure(facecolor='white')
    ax = fig.add_axes([0,0,width,height])
    ax_background = ax.twinx()
    ax_background.plot(time,price,color='black')
    ax_background.set_ylabel('price', fontsize=_fontsize)
    ax_background.tick_params(axis='y', labelsize=_fontsize)
    ax_background.semilogy()
    ax.set_xlabel('time', fontsize=_fontsize)
    ax.tick_params(axis='x', labelsize=_fontsize)
    return (fig, ax, ax_background)

def impermanent_loss_vis(df, x, y, width=5, height=5, _fontsize=40):
    fig = plt.figure(facecolor='white')
    ax = fig.add_axes([0,0,width,height])
    ax.set_ylabel('price', fontsize=_fontsize)
    ax.tick_params(axis='y', labelsize=_fontsize)
    ax.set_xlabel('time', fontsize=_fontsize)
    ax.tick_params(axis='x', labelsize=_fontsize)
    ax.plot(df['time'], df['% to x'], label=f"% to {x}")
    ax.plot(df['time'], df['% to y'], label=f"% to {y}")
    ax.plot(df['time'], df['% to 50/50'], label=f"% to 50/50")
    ax.legend(fontsize=_fontsize)
    plt.show()