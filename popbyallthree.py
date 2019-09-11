from matplotlib import pyplot as plt

# Calories
cal_x = [ 0, 50, 85, 145, 193, 212, 200, 285]

# Serving amount
size_y = [1, 1, 1, 3, 4, 4, 5, 5]
plt.plot(cal_x, size_y, label='Serving Amount')

# Time in Minutes
time_y = [0, 0, 3, 3, 3, 10, 15, 15]
plt.plot(cal_x, time_y, label='Time to Cook')

# Times Cooked
cooked_y = [1, 2, 3, 3, 5, 7, 10, 15]
plt.plot(cal_x, cooked_y, linestyle='--', label='Popularity')

plt.xlabel('Calories')
plt.ylabel('Servings & Time & Popularity')
plt.title('Servings & Time & Popularity by Calories')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('static/img/popby.png')

plt.show()