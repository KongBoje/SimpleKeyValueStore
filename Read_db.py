import pickle

input_file = open("myNumberFile.db", "rb")

numberDict = pickle.load(input_file)

for key, value in numberDict.items():
        print('Key:', key, 'Value:', numberDict[key])

#print 'read 1st key and value:', numberDict.items()[0]

input_file.close()

