**pycallgraph26**
-------------

This is a modified version of the pycallgraph module to make it work in Python 2.6. 
The original tool for Python 2.7+ and 3.3+ is available here: http://pycallgraph.slowchop.com/en/master/

Modifications: 
--------------
- Added indices to all format commands. 
- Downloaded and included 2.6 versions of *ordereddict* and *argparse*. 
- Fixed some impport statements. 
- Removed all unneeded files of the package. 

Installation: 
-------------
Download and extract. 

Commandline usage: 
------------------
- CD to the extracted *pycallgraph26* directory. 
- On a bash use **launch_pycallgraph**.
- On a Windows commandline use **python launch_pycallgraph** or **launch_pycallgraph.bat** 
- Use commandline flags as described here: http://pycallgraph.slowchop.com/en/master/guide/command_line_usage.html#command-line-usage



In-code usage: 
--------------
Add the pycallgraph26 folder to your sys.path and use the pycallgraph API as described here: 
http://pycallgraph.slowchop.com/en/master/index.html#quick-start 