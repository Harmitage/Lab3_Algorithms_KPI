import time

inputFileName = "data.in"
outputFileName = "data.out"


def prepareList():
    inputList = open(inputFileName, "r", encoding="utf-8").readlines()
    # making tuples (number, index) to save the original index position
    inputList = [(int(number), index) for index, number in enumerate(inputList)]

    return inputList


def writeList(inputList):
    outputFile = open(outputFileName, "w", encoding="utf-8")

    inputList = '\n'.join([(str(tup).strip("()")) for tup in inputList])

    outputFile.write(str(inputList))
    outputFile.close()


def findPivot(inputList, start, end):
    midIndex = int((start + end) / 2)

    if inputList[start][0] < inputList[midIndex][0] < inputList[end][0]:
        return midIndex
    elif inputList[midIndex][0] < inputList[start][0] < inputList[end][0]:
        return start
    else:
        return end


def quickSort(inputList, startInd, endInd):
    if (endInd - startInd) > 0:
        dividerInd = startInd
        pivotInd = endInd
        for i in range(startInd, endInd):
            if inputList[i][0] < inputList[pivotInd][0]:
                inputList[i], inputList[dividerInd] = inputList[dividerInd], inputList[i]
                dividerInd += 1

        inputList[pivotInd], inputList[dividerInd] = inputList[dividerInd], inputList[pivotInd]

        quickSort(inputList, startInd, dividerInd - 1)
        quickSort(inputList, dividerInd + 1, endInd)


def insertSort(inputList):

    for i in range(1, len(inputList)):
        value = inputList[i]
        n = i-1
        while value[0] < inputList[n][0] and n >= 0:
            inputList[n+1] = inputList[n]
            n -= 1

        inputList[n+1] = value


def customSort():
    pass


def main():
    startingTime = time.time()

    inputList = prepareList()

    insertSort(inputList)
    #quickSort(inputList, 0, len(inputList)-1)

    writeList(inputList)

    totalTime = time.time() - startingTime

    print("Sorted the file in " + str(totalTime) + " seconds")


if __name__ == '__main__':
    main()