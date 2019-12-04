import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import board
import busio

# I2C setupf
from adafruit_cap1188.i2c import CAP1188_I2C
i2c = busio.I2C(board.SCL, board.SDA)
cap = CAP1188_I2C(i2c)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = [0,0,0,0,0,0,0,0]

# This function is called periodically from FuncAnimation
def animate(i ,xs ,ys):
    for i in range(1, 9):
        ys[i-1]=ys[i-1]+(cap[i].value)
        if cap[i].value:
            print("Pin {} touched!".format(i))

    ax.clear()
    bars=('1','2','3','4','5','6','7','8')
    channels = np.arange(len(bars))
    ax.bar(channels, ys, align='center', alpha=0.5)

    # Format plot
    plt.xticks(channels, bars)
    plt.subplots_adjust(bottom=0.30)
    plt.xlabel('Channel number')
    plt.ylabel('Channel touch count')
    plt.title('CAP1188 Channel touch history')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
