# print("Hi, I'm good here")
# # Remove whitespace, capitalize and make every new word capital
# name = input("What's your name champ? ").strip().capitalize().title()
# # Split user's name into first name and last name
# first, last = name.split(" ")

# # greet user
# print("Hello", name)
# print(f"I know that your first name is {first}")

def hello(to="World"):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
