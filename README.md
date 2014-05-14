**pycallgraph26**
=================

This is a modified version of the pycallgraph module (based on v1.01) to make it work in Python 2.6.

Pycallgraph visualizes function calls as graph images and is great for profiling an application (or parts of it).

It has been created by [Gerald Kaszuba](http://geraldkaszuba.com) and is avalaible for Python 2.7+ and 3.3+ from: http://pycallgraph.slowchop.com/en/master/

Modifications:
--------------
- Added indices to all format commands.
- Downloaded and included 2.6 versions of *ordereddict* and *argparse*.
- Fixed some impport statements.
- Removed all unneeded files of the package.

Installation:
-------------
- Make sure you have [graphviz](http://www.graphviz.org) installed and the dot command can be found in your PATH environment variable.
- Download and extract *pycallgraph26*.

Commandline usage:
------------------
- CD to the extracted *pycallgraph26* directory.
- On a bash use **launch_pycallgraph**.
- On a Windows commandline use **python launch_pycallgraph** or **launch_pycallgraph.bat**
- Use commandline flags as described here: http://pycallgraph.slowchop.com/en/master/guide/command_line_usage.html#command-line-usage


In-code usage:
--------------
Make sure the *pycallgraph26* folder is found in your sys.path and use the pycallgraph API as described here:
http://pycallgraph.slowchop.com/en/master/index.html#quick-start