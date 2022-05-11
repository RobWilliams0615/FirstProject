store_ratings = [6.4, 7.5, 8.3, 9.0, 9.5, 7.3, 6.5, 9.5]


for rating in store_ratings:
    print(round(rating))

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

# for loop over a function


def liters_to_oz(L):
    return L * 33.814


for liters in [1, 3, 5, 7.8]:
    print(liters_to_oz(liters))
