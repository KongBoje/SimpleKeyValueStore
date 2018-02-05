import pickle
import sys
import os

def main(argv):
    input_file = open("myNumberFile.db", "rb")

    numberDict = pickle.load(input_file)

    for key, value in numberDict.items():
        if sys.argv[1] == key:
            print('Key: {}'.format(key))
            print('Value: {}'.format(value))

if __name__ == "__main__":
    main(sys.argv[1:])