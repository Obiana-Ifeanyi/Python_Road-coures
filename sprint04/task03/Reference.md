
How do I create a connection to the database?
To create a connection to the database, you need the following login information

.Host
.Hostname
.Database username
.Password

# Note: You can only make a connection to the database when your website is hosted on our servers.



Web-Sites resources

'https://www.youtube.com/watch?v=byHcYRpMgI4'


What is a relational database?
'https://www.oracle.com/database/what-is-a-relational-database/'

What is SQL?
'https://www.w3schools.com/sql/default.asp'

What are the pros and cons of SQL?
'https://www.geeksforgeeks.org/advantages-and-disadvantages-of-sql/'

What is a query?
'https://www.hostinger.com/tutorials/what-is-a-query#:~:text=In%20standard%20English%2C%20a%20query,the%20database%20understand%20the%20instruction.'

How to create a connection to a database?
'https://www.tutorialspoint.com/python_data_access/python_mysql_create_database.htm'

How to install mysql?
'https://www.mysqltutorial.org/install-mysql/'
'https://www.mysqltutorial.org/install-mysql-ubuntu/'



What is a cursor object in sqlite3?
    The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database.
    Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
    You can create Cursor object using the cursor() method of the Connection object/class.

    Example
    import mysql.connector

    #establishing the connection
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='mydb')

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    'https://www.geeksforgeeks.org/python-sqlite-cursor-object/#:~:text=It%20is%20an%20object%20that,giving%20connection%20to%20SQLite%20database.'



Python Data Access
'https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm'
'https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm'
'https://www.geeksforgeeks.org/how-to-execute-a-sqlite-statement-in-python/'
'https://www.geeksforgeeks.org/how-to-execute-a-script-in-sqlite-using-python/'
'https://www.geeksforgeeks.org/how-to-execute-many-sqlite-statements-in-python/'

How to create a connection to a database?
    connection = sqlite3.connect()


How to close a connection to a database?
    connection.close()

How to execute a SQL statement using sqlite3?  
    connection.execute(<action>)
    cursor.execute(<action>)
    # note: an execute function is used to execute the action after being defined
