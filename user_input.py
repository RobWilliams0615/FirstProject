def age_quest(age):
    if age >= 21:
        return "You are allowed"
    else:
        return "Not old enough quite yet"


user_input = float(input("Enter Age: "))
print(age_quest(user_input))
