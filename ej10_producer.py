import sys


def main():
    pipeInput = '/tmp/msm'
    msm = sys.argv[1:]

    fifo = open(pipeInput, "w")
    for line in msm:
        fifo.write(line)
    fifo.flush()
    fifo.close()
    print("msm en p: ")
    for line in sys.argv[1:]:
        print(line)


if __name__ == '__main__':
    main()
