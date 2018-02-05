import pickle

output_file = open("myNumberFile.db", "wb")

numberDict = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}

pickle.dump(numberDict, output_file)

output_file.close()