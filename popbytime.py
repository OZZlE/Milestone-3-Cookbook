from matplotlib import pyplot as plt

# Time in Minutes
time_x = [0, 0, 3, 3, 3, 10, 15, 15]

# Popularity
cooked_y = [1, 2, 3, 3, 5, 7, 10, 15]
plt.plot(time_x, cooked_y, color='#444444', label='Popularity')

plt.xlabel('Time')
plt.ylabel('Popularity')
plt.title('Popularity by time to cook')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('static/img/popbytime.png')

plt.show()