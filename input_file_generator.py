import random
import time
import sys

# Default generator parameters
max_rand_num = 18446744073709551615  # i.e 2^64-1, maximum unsigned 64-bit value

full_file_size = 44000  # resulting file size in megabytes (decimal)
half_file_size = full_file_size / 2
short_file_size = full_file_size / 16
s_short_file_size = full_file_size / 256
file_sizes = [full_file_size, half_file_size, short_file_size, s_short_file_size]

chunks_num = 10  # write to the file in specified number of chunks


def generator(file_size):
    byte_buffer_size = (file_size / chunks_num) * 1000000  # converting megabytes into bytes (decimal)

    keysBuffer = list()
    totalKeyCounter = 0
    byteIterator = 0

    startingTime = time.time()
    numFile = open("data.in", "w", encoding="utf-8")

    for bufferIterator in range(chunks_num):
        while byteIterator <= byte_buffer_size:
            string = str(random.randint(0, max_rand_num)) + "\n"
            keysBuffer.append(string)
            byteIterator += len(string.encode("utf8"))
            totalKeyCounter += 1

        joinedBuffer = ''.join(keysBuffer)
        numFile.write(joinedBuffer)
        print("Wrote a buffer number " + str(bufferIterator) + " with size " +
              str(sys.getsizeof(joinedBuffer)) + " bytes to the file")
        byteIterator = 0
        keysBuffer.clear()

    numFile.close()

    totalTime = time.time() - startingTime
    print("Created " + str(totalKeyCounter) + " keys in " + str(totalTime) + " seconds")

    # Less optimized version that chains strings
    #
    # for bufferIterator in range(chunks_num):
    #     while sys.getsizeof(keysBuffer) <= byte_buffer_size:
    #         randNumber = random.randint(0, max_rand_num)
    #         keysBuffer += str(randNumber) + "\n"
    #         totalKeyCounter += 1
    #
    #     numFile.write(keysBuffer)
    #     print("Wrote a buffer number " + str(bufferIterator) + " with size " +
    #           str(sys.getsizeof(keysBuffer)) + " bytes to the file")
    #     print("Total file size is " + str(os.path.getsize("data.in") / 1000000) + " MB")
    #     keysBuffer = ""


def main():
    size_input = int(input("""
    What kind of file size would you like?\n
    Press:
    0 - for full size
    1 - for half size
    2 - short size
    3 - super short size
    """))

    print("Creating a file with " + str(file_sizes[size_input]) + " MB size in " + str(chunks_num) + " chunks, please wait!")

    if 0 <= size_input <= 3:
        generator(file_sizes[size_input])
    else:
        print("Invalid input!")


if __name__ == '__main__':
    main()
