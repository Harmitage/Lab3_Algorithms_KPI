import random
import time
import os

# Default generator parameters
max_rand_num = 18446744073709551615  # i.e 2^64-1, maximum unsigned 64-bit value

full_file_size = 45056  # resulting file size in megabytes (binary)
half_file_size = full_file_size / 2
short_file_size = full_file_size / 16
s_short_file_size = full_file_size / 256
file_sizes = [full_file_size, half_file_size, short_file_size, s_short_file_size]


def generator(file_size):
    file_size_in_bytes = file_size * 1048576  # converting megabytes into bytes (binary)

    keyCounter = 0
    startingTime = time.time()

    numFile = open("data.in", "w")
    while os.path.getsize("data.in") <= file_size_in_bytes:
        randNumber = random.randint(0, max_rand_num)
        numFile.write(str(randNumber) + "\n")
        keyCounter += 1
    numFile.close()

    totalTime = time.time() - startingTime
    print("Created " + str(keyCounter) + " keys in " + str(totalTime) + " seconds.")


def main():
    size_input = int(input("""
    What kind of file size would you like?\n
    Press:
    0 - for full size
    1 - for half size
    2 - short size
    3 - super short size
    """))

    if 0 <= size_input <= 3:
        generator(file_sizes[size_input])
    else:
        print("Invalid input!")


if __name__ == '__main__':
    main()
