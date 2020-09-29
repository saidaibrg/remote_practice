from datetime import date

today=date.today()
print("Today is " + str(today)+".")
task_list=[]
task=raw_input("Enter a task: ")
task_list.append(task)
print("Your tasks for today are:")
#Printing the task list without brackets usuing .join(list) function 
print(",".join(task_list))