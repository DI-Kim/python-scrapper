playing = True

while playing:
  first_number = int(input("Choose a number:\n"))
  second_number = int(input("Choose another one:\n"))

  selected_operation = input('''Choose an operation
        Options are: +, -, * or /.
        Write 'exit' to finish.
''')

  if selected_operation == 'exit':
    playing = False
  elif selected_operation == '+':
    print(f'Result: {first_number + second_number}')
  elif selected_operation == '-':
    print(f'Result: {first_number - second_number}')
  elif selected_operation == '*':
    print(f'Result: {first_number * second_number}')
  elif selected_operation == '/':
    print(f'Result: {first_number / second_number}')
