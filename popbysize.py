from matplotlib import pyplot as plt

# Serving amount
size_x = [1, 1, 1, 3, 4, 4, 5, 5]

# Popularity
cooked_y = [1, 2, 3, 3, 5, 7, 10, 15]
plt.plot(size_x, cooked_y, color='#444444', label='Popularity')

plt.xlabel('Serving amount')
plt.ylabel('Popularity')
plt.title('Popularity by Serving amount')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig('static/img/popbysize.png')

plt.show()