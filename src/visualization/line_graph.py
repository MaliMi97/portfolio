import matplotlib.pyplot as plt

def with_price_in_background(time, price, width=5, height=5, _fontsize=40):
    fig = plt.figure(facecolor='white')
    ax = fig.add_axes([0,0,width,height])
    ax_background = ax.twinx()
    ax_background.plot(time,price,color='black')
    ax_background.set_ylabel('price', fontsize=_fontsize)
    ax_background.tick_params(axis='y', labelsize=_fontsize)
    ax_background.semilogy()
    ax_background.set_xlabel('time', fontsize=_fontsize)
    ax_background.tick_params(axis='x', labelsize=_fontsize)
    return (fig, ax, ax_background)