
DESCRIPTION

Create a script with function a html_save() that:
     • takes a URL as the ﬁrst argument and a ﬁle path (either absolute or relative)
       as the second

     • validates the URL that is passed to it using a validation regex.

     Note: the URL validation must cover all the different parts of the address (scheme, domain, port, etc.)
     and their different variations. Also, pay attention that some URL parts are required and some are optional.
     There is a list of valid and invalid URLs in the resources for you to test your code with.

     • if the request has succeeded, downloads and saves the web page content located at
       the provided URL to the speciﬁed ﬁle. Otherwise, the function prints the message 'Request failed' using print_stderr()
       (this function is described further).

     • logs the execution of each step

All errors and information during the process must be printed to either the stderr or stdout respectively.


For that purpose, create a ﬁle-module helper.py that contains two functions:
     • print_stderr() prints a given error message to stderr in the format 'ERROR| [message].' and exits the program

     • print_stdout() prints a given info message to stdout in the format 'INFO| [message].'


Don't forget to catch all errors that may happen when making a request.
Print them using the print_stderr() function.

In this task you must use re , requests, and your own helper modules.
