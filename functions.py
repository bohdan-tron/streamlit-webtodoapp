def showTodos(where='todos.txt'):
	"""
		Prints the todos in the terminal
 	"""
	with open(where, 'r') as file:
		todos = file.readlines()

	for index, item in enumerate(todos):
		item = item.strip('\n')
		row = f"{index + 1}. {item}"
		print(row)


def getTodos(where='todos.txt'):
	with open(where, 'r', encoding='utf-8') as file:
		todos = file.readlines()
	return todos


def postTodos(todos, where='todos.txt'):
	with open(where, 'w', encoding='utf-8') as file:
		file.writelines(todos)


if __name__ == "___main__":
	print("hello")

