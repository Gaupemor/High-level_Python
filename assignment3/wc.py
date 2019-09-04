import sys, os

for file in sys.argv[1:]:
    if os.path.isfile(file):
        fileName = file
        numOfLines = numOfWords = numOfChars = 0

        for line in open(fileName, "r").readlines():
            numOfLines += 1
            numOfWords += len(line.replace("/n","").split())
            numOfChars += len(line)

        print(f"{numOfLines} {numOfWords} {numOfChars} {fileName}")
