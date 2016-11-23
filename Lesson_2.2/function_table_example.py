def add_visit():
	pass

def predict_visit():
	pass

def remove_visit():
	pass

def stop_program():
	pass

function_table = {
	'v': add_visit,
	'p': predict_visit,
	'r': remove_visit,
	'e': stop_program
}

# вариант 1
while True:
	user_input = input()
	if user_input not in [function_table.keys()]:
		continue
	function_table[user_input]()

# вариант 2
while True:
	user_input = input()
	func = function_table.get(user_input)
	if func is None:
		continue
	else:
		func()


	
