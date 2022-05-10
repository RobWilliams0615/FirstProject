def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


class1_grades = {"Tom": 90.5, "Dan": 80.7, "Lisa": 75.8}
# print(mean(class1_grades))


def temp(value):
    if value > 7:
        return "Warm"
    else:
        return "Cold"


# print(temp(7))


def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False


# print(foo('hellofishy'))


def temperature(value):
    if value > 25:
        return("Hot")
    elif 25 >= value >= 15:
        return("Warm")
    else:
        return("Cold")


print(temperature(-5))
