# Application component
# Contains command logic
# Calls to DB

from scenario_5_data import *

def commandLogic():
    flag = True
    while (flag):
        command = input("Command: ")
        if (command.lower() == 'exit'):
            flag = False
        elif (command.lower() == 'view'):
            viewPendingTasks()
        elif (command.lower() == 'history'):
            viewCompletedTasks()
        elif (command.lower() == 'add'):
            addTask()
        elif (command.lower() == 'complete'):
            completeTask()
        elif (command.lower() == 'delete'):
            deleteTask()
    print("Bye!")
