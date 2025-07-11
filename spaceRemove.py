# remove space from an integer
def remove_spaces(s):
    return s.replace(" ", "")

user_input = input("input a str:")
result = remove_spaces(user_input)
print("here yer go:", result)