def say_hello(name, age):
  print(f"hello {name}, you are a {age} years old")
  
def say_bye():
  print("bye bye")

x = True
while x:
  username = input("enter your name(input 'exit' is go out):")
  age = input("enter your age")
  if username == 'exit':
    x = False
  else:
    say_hello(username, age)