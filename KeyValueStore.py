import pickle

def main():

    def write():
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

    def read():
        input_file = open("myNumberFile.db", "rb")

        numberDict = pickle.load(input_file)

        for key, value in numberDict.items():
                print('Key:', key, 'Value:', numberDict[key])

        print('Number of elements in the db file:', len(numberDict))

        input_file.close()
    
    write()
    read()

if __name__ == "__main__":
    main()