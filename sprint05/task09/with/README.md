DESCRIPTION 

Create a script that contains a class called Redirect that can be used as a context manager. 
The class initializer takes a string path to a ﬁle (to which you will redirect the standard stream), 
and a string that speciﬁes what stream(s) to redirect from 
(either 'o' for stdout, 'e' for stderr, or 'oe' for both). 
The class must have the two magic methods that allow the use of the with statement on a class. 
Research what two methods are necessary for that. The Redirect context manager must redirect 
the speciﬁed stream(s) to the ﬁle given as a path when an instance is initialized. 
The ﬁle must be appended to, not overwritten.
