with open('notepad.txt', 'w') as notepad_file:
	while True:
		user_input = input()
		if user_input == 'exit':
			break
		notepad_file.write(user_input + '\n')