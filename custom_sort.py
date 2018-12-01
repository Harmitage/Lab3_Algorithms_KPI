import os
import heapq

inputFileName = "data.in"
outputFileName = "data.out"

chunkSize = 10000
chunkNameFormat = 'chunk{0}.temp'


class FileDivider:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.chunk_file_names = []

    def chunk_write(self, data, chunk_num):
        filename = chunkNameFormat.format(chunk_num)
        file = open(filename, 'w')
        file.write(data + '\n')
        file.close()
        self.chunk_file_names.append(filename)

    def return_chunk_names(self):
        return self.chunk_file_names

    def divide(self, block_size):
        file = open(self.input_file_name, 'r')
        linesNum = 1
        fileNum = 0

        while True:
            inputList = file.readlines(block_size)
            lines = [(int(number), index + linesNum) for index, number in enumerate(inputList)]

            if not lines:
                break

            lines.sort()

            self.chunk_write('\n'.join([(str(tup).strip("()")) for tup in lines]), fileNum)
            print("Created temporary sorted chunk number " + str(fileNum))
            linesNum += len(lines)
            fileNum += 1

    def delete_temp_files(self):
        for file_name in self.chunk_file_names:
            os.remove(file_name)


class FileCombiner:
    def __init__(self, output_file_name):
        self.heap = []
        self.output_file_name = output_file_name
        self.output_file = open(self.output_file_name, 'w+')

    def strip_line(self, line):
        return line.split(', ')

    def combine(self, input_files):
        opened_file_list = []
        [opened_file_list.append(open(file__, 'r')) for file__ in input_files]

        for temp_file in opened_file_list:
            line = self.strip_line(temp_file.readline())
            heapq.heappush(self.heap, (int(line[0]), line[1], temp_file))

        while self.heap:
            smallest_str = heapq.heappop(self.heap)
            self.output_file.write(str(smallest_str[0]) + ", " + str(smallest_str[1]))
            read_line = smallest_str[2].readline()
            if len(read_line) != 0:
                heapq.heappush(self.heap, (int(self.strip_line(read_line)[0]), self.strip_line(read_line)[1],
                                           smallest_str[2]))

        [temp_file.close() for temp_file in opened_file_list]
        self.output_file.close()


def main():

    divider = FileDivider(inputFileName)
    divider.divide(chunkSize)

    combiner = FileCombiner(outputFileName)
    combiner.combine(divider.return_chunk_names())

    divider.delete_temp_files()


if __name__ == '__main__':
    main()