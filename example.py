from random import randint

print("welcom to Python Casino!")

pc_choice = randint(1, 100)

playing = True

while playing:
  user_choice = int(input('choose your number (1 - 100):'))

  if user_choice == pc_choice:
    playing = False
    print('You won!')
  elif user_choice > pc_choice:
    print('Lower!')
  elif user_choice < pc_choice:
    print('Higher!')
    