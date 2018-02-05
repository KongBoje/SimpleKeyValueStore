import pickle
import os

input_file = open("myNumberFile.db", "rb")

numberDict = pickle.load(input_file)

for key, value in numberDict.items():
        print('Key:', key, 'Value:', numberDict[key])

#print 'read 1st key and value:', numberDict.items()[0]
print('Number of elements in the db file:', len(numberDict))

input_file.close()

