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

def addPosition():
    positionName = input("Please enter the name of the position: ")
    positionPay = input("Please input the amount of pay this position gives: ")
    values = (positionName, positionPay)
    cursor.execute("INSERT INTO positions (name, pay) VALUES (?,?)", values)
    connection.commit()

add = input("Add Employee?(y/n)")
if add == "y":
    addEmployee()
displayEmployees()

add = input("Add Position?(y/n)")
if add == "y":
    addPosition()
displayPositions()


connection.close()