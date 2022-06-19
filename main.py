help = """
help - напечатать справку по команде
add - добавить задачу в список
  today - сегодня
  tomorrow - завта
  other - любой другой день
show - вывести все добавленные задачи
exit - выход
random - добавляет случайную задачу на дату сегодня\n"""

run = True
date = None
command = None
task = None
tasks = {}

def add_todo(date, task):     
    if date in tasks:
      tasks[date].append(task)
    else:
      tasks[date] = []
      tasks[date].append(task)
    print("Задача добавлена")

while run:
  command = input("Enter command: ")
  if command == "help":
    print(help)
  elif command == "show":
    data = input("Введите дату для отображения: ")
    if date in tasks:
      for task in tasks[date]:
        print('- ', task)
  elif command == "add":
    date = input("Введите дату: ")
    task = input("Ведите задачу: ")
    add_todo(date, task)
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Unknown team")
    print("До свидания!")
    break
    
    
  