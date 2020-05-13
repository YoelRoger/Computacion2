#!/usr/bin/python
import sys
import os


def main():
    pipeInput = '/tmp/msm'
    msm = str(sys.argv[1:])

    fifo_file = open(pipeInput, "w")
    fifo_file.write(msm)
    fifo_file.flush()
    fifo_file.close()
    print("msm en fifo:" + msm)

    if not os.path.exists(pipeInput):
        os.mkfifo(pipeInput)


if __name__ == '__main__':
    main()
