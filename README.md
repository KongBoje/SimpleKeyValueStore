# SimpleKeyValueStore

## Installation and requirements
First of all you need to download python to your pc at this link [Python.org](https://www.python.org/downloads/), hover your mouse over the "Downloads" tab and choose your Operative system.
This is needed for you to be able to compile and execute the files from the command line.

When that is done, clone this project locally to your pc in a directory.

## Execution
1. Go to the directory you cloned or downloaded the files to and open a terminal there.

2. In the terminal you first write "python KeyValueStore.py", which executes the write and read functions in the file (with results showing in the terminal) and creates a binary file called myNumberFile.db.

3. If you try and write xxd myNumberFile.db It'll show you the content inside the binary file.

4. If you want to try and only read a specific key with corresponding value you write "python SpecificValueStoreKey.py 1". You can use the number from 1 to 6 here.


## Ekstra information
Pickle is a module which implements binary protocols for serializing and de-serializing a Python object structure.
It made it quite easy to make a binary file.
