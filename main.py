import sqlite3

connection = sqlite3.connect('work.db')
cursor = connection.cursor()

#cursor.execute("CREATE TABLE employees (id integer primary key, name text, experience text)")
#cursor.execute("CREATE TABLE positions (id integer primary key, name text, pay float)")


def displayPositions():
    cursor.execute("SELECT * FROM positions")
    print("{:<5} {:<15} {:<15}".format("ID", "Position", "Pay"))
    print("{:<5} {:<15} {:<15}".format("---","---------","----------"))
    for record in cursor.fetchall():
        print("{:<5} {:<15} ${:<15.2f}".format(record[0],record[1],record[2]))

def displayEmployees():
    cursor.execute("SELECT * FROM employees")
    print("{:<5} {:<15} {:<15}".format("ID","Full Name","Experience"))
    print("{:<5} {:<15} {:<15}".format("---","---------","----------"))
    for record in cursor.fetchall():
        print("{:<5} {:<15} {:<15}".format(record[0],record[1],record[2]))

def addEmployee():
    employeeName = input("Please enter the employee's full name: ")
    employeeExperience = input("Please enter the employee's previous experience (Degree, Previous work, etc): ")
    values = (employeeName, employeeExperience)
    cursor.execute("INSERT INTO employees (name, experience) VALUES (?,?)", values)
    connection.commit()
    print("")
    print("Updated list of employees:")
    displayEmployees()

def addPosition():
    positionName = input("Please enter the name of the position: ")
    positionPay = input("Please input the amount of pay this position gives: ")
    values = (positionName, positionPay)
    cursor.execute("INSERT INTO positions (name, pay) VALUES (?,?)", values)
    connection.commit()
    print("")
    print("Updated list of positions:")
    displayPositions()

def editEmployeeName():
    print("")
    displayEmployees()
    employeeID = input("Please input the ID of the employee whose name needs to be changed: ")
    employeeName = input("Please input the new name of the employee: ")
    values = (employeeName, employeeID)
    cursor.execute("UPDATE employees SET name = ? WHERE id = ?", values)
    connection.commit()

    
def editEmployeeExperience():
    print("")
    displayEmployees()
    employeeID = input("Please input the ID of the employee whose experience needs to be changed: ")
    employeeExperience = input("Please input the adjusted experience for the employee: ")
    values = (employeeExperience, employeeID)
    cursor.execute("UPDATE employees SET experience = ? WHERE id = ?", values)
    connection.commit()

def editEmployee():
    print("1) Edit Employee Name")
    print("2) Edit Employee Experience")
    print("3) Cancel Edit")
    editType = input("> ")
    if editType == "1":
        editEmployeeName()
    elif editType == "2":
        editEmployeeExperience()
    else:
        print("")
        return

def editPositionName():
    print("")
    displayPositions()
    positionID = input("Please input the ID of the position that needs to be changed: ")
    positionName = input("Please input the new name of the position: ")
    values = (positionName, positionID)
    cursor.execute("UPDATE positions SET name = ? WHERE id = ?", values)
    connection.commit()


def editPositionPay():
    print("")
    displayPositions()
    positionID = input("Please input the ID of the position that needs to be changed: ")
    positionPay = float(input("Please input the adjusted pay for this position: "))
    values = (positionPay, positionID)
    cursor.execute("UPDATE positions SET pay = ? WHERE id = ?", values)
    connection.commit()


def editPosition():
    print("1) Edit Position Title")
    print("2) Edit Position Pay")
    print("3) Cancel Edit")
    editType = input("> ")
    if editType == "1":
        editPositionName()
    elif editType == "2":
        editPositionPay()
    else:
        print("")
        return

def deleteEmployee():
    print("")
    displayEmployees()
    employeeID = input("Please input the ID of the departing employee: ")
    values = (employeeID,)
    cursor.execute("DELETE FROM employees WHERE id = ?", values)
    connection.commit()

def deletePosition():
    print("")
    displayPositions()
    positionID = input("Please input the ID of the position to be removed: ")
    values = (positionID,)
    cursor.execute("DELETE FROM positions WHERE id = ?", values)
    connection.commit()

userSelect = "1"
while userSelect != "9":
    print("What would you like to do?")
    print("1) Add a New Employee")
    print("2) Add a New Position")
    print("3) Edit an Existing Employee")
    print("4) Edit an Existing Position")
    print("5) Display All Employees")
    print("6) Display All Positions")
    print("7) Remove an Employee")
    print("8) Remove a Position")
    print("9) Quit")
    print("")
    userSelect = input("> ")
    print("")
    if userSelect == "1":
        addEmployee()
        print("")
    elif userSelect == "2":
        addPosition()
        print("")
    elif userSelect == "3":
        editEmployee()
        print("")
    elif userSelect == "4":
        editPosition()
        print("")
    elif userSelect == "5":
        displayEmployees()
        print("")
    elif userSelect == "6":
        displayPositions()
        print("")
    elif userSelect == "7":
        deleteEmployee()
        print("")
    elif userSelect == "8":
        deletePosition()
        print("")

connection.close()