from matplotlib import pyplot as plt

# Calories
cal_x = [ 0, 50, 85, 145, 193, 212, 200, 285]

# Times Cooked
cooked_y = [1, 2, 3, 3, 5, 7, 10, 15]
plt.plot(cal_x, cooked_y, linestyle='--', label='Popularity')

plt.xlabel('Calories')
plt.ylabel('Popularity')
plt.title('Popularity by Calories')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('static/img/popbycal.png')

plt.show()