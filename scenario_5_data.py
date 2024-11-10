# Database Component
# Connects to the database and executes queries

import sqlite3

def viewPendingTasks():
    connection = sqlite3.connect('task_list_db.sqlite')

    cursor = connection.cursor()
    # Execute a SELECT statement to fetch all rows
    cursor.execute('SELECT description FROM Task')
    # Fetch all results from executed query
    rows = cursor.fetchall()
    
    for index, row in enumerate(rows, start=1):
        print(f"{index}. {row[0]}")
    print()

    connection.close()

def viewCompletedTasks():
    connection = sqlite3.connect('task_list_db.sqlite')
    cursor = connection.cursor()    

    # view completed tasks
    cursor.execute("""
        SELECT description
        FROM Task
        WHERE completed = 1
    """
    )
    # Fetch all results from executed query
    rows = cursor.fetchall()
    for index, row in enumerate(rows, start=1):
        print(f"{index}. {row[0]} (DONE!)")
    print()
    
    connection.close()

def addTask(new_task):
    connection = sqlite3.connect('task_list_db.sqlite')
    cursor = connection.cursor()       
    
    # add new provided task to db
    cursor.execute("INSERT INTO Task (description, completed) VALUES (?, ?)", (new_task, 0))
    # Commit changes
    connection.commit()

    cursor.execute('SELECT description FROM Task')
    # Fetch all results from executed query
    rows = cursor.fetchall()

    for index, row in enumerate(rows, start=1):
        print(f"{index}. {row[0]}")
    print()

    connection.close()

def completeTask(completed_task):
    connection = sqlite3.connect('task_list_db.sqlite')
    cursor = connection.cursor()       
    
    cursor.execute("UPDATE Task SET completed = ? WHERE description = ?", (1, completed_task))
    connection.commit()

    connection.close()

def deleteTask(task_to_delete):
    connection = sqlite3.connect('task_list_db.sqlite')
    cursor = connection.cursor()      
    
    cursor.execute("DELETE FROM Task WHERE description = ?", (task_to_delete,))
    connection.commit()

    connection.close()