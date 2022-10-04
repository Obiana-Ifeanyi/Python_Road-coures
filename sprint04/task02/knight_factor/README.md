
DESCRIPTION

Create a package with the name generator.
Create the __init__.py ﬁle for the package, where you should import
all necessary packages/modules.

Also, inside the package create two modules: names.py and titles.py. The names module has a function names()
that generates a random name and the titles module has a function titles() that generates a random title from predeﬁned lists.
You can modify the lists or use different ones, as long as there are at least three values in each.

Create a knight_factory.py script and use the package there.
The script must create a knight by generating a name and a title and log the knight's information in the following format:
---- 'Sir [name] the [title]' ----

Generate ﬁve knights.

Also, your script must work with logging (place the logging process in your __init__.py):

    • import the required module

    • create a logger instance

    • use the INFO level messages

    • messages must be printed to the stdout

    • the format of the logs must be: '..::Knight Generator::.. [process]-[levelname][message]' (the process may vary).

There are helpful resources in the SEE ALSO section on how to print meta information that is in square brackets 
