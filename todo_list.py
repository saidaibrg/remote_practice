from datetime import date

today=date.today()
print("Today is " + str(today)+".")
task_list=[]
task=raw_input("Enter a task: ")
task_list.append(task)
print("Your tasks for today are:")
print(task_list)