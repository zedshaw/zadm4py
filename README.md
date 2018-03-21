Zed's Awesome Debug Macros for Python 3
====

This is an idea I've had for a while to create some tools for helping people debug Python programs quicker.  This is based on what I see a lot of beginner struggle with and also what I find incredibly annoying about debugging Python.  Right now this is a quick hack to just get the basic guts of it working, and below is some of my ideas.

I created a similar set of helper macros for C and they worked well for me, but I believe with Python I can make them even more useful.  Currently this is just a quick layout of what I want, with more work to come as I use this for real things.

This is done in Python 3 since my current Live students need it and they're learning Python 3.

Ideas So Far
====

I have a couple others for on the testing side of things, but for now:

@trace
---

The primary most useful function.  You slap this on a function you're having problems with or working on and it does this:

* Catch an exception and then write out all functions in the stack trace for later tracing.
* Drop into PDB on any exception.  When an exception happens the improved exception handler will stop and offer to do PDB, dump the trace to a data file, and other options.
* Remember that this function caused an exception and drop into PDB *before* it runs.
* Load a relevant data page on an exception and print out possible causes and solutions.  When an exception happens, look up the exception and other relevant information and then display a page explaining what's going on, what could cause it, and how to fix it.
* Simpler tracing of function calls that are having a problem.  You just add a simple @trace() to the function and it will automatically log its calls, stack depth, and where it was called from.  It will also drop into pdb, log the previous stack on exceptions, etc.


@pre
---

* Adds a precondition to the call enforcing that it is met.

@post
---

* Adds a postcondition that ensures a truth about the return value.

@invariant
---

* Basically a test before and after, kind of a combined pre/post condition.

log()
---

Better logging of what's going on. 

* Automatically include local variables but only if they change in value.  
* Automatically indent by stack call level.
* Automatically give the file:lineno on all messages.
* Ability to add other things like process ID?


