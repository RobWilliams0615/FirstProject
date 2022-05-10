# user_input = input("Enter your name: ")

# Python 3.6 and earlier
#message = "Hello %s!" % user_input


# 3.6 or later
#message = f"Hello {user_input}!"
# print(message)


# string formatting with multiple variables

firstname = input("Enter your First Name: ")
lastname = input("Enter your Last Name: ")

message = f"Hello {firstname} {lastname}"

print(message)
