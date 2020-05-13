import os


def main():
    pipeOutput = '/tmp/msm'
    lines = ""
    fifo = open(pipeOutput, 'r')  # abro "pipe" pal msm
    lines = fifo.readlines()
    fifo.close()

    r, w = os.pipe()
    child = os.fork()

    if child:
        # PADRE
        os.close(r)
        write = open(w, 'w')  # arch escribe en "pipe"
        write.writelines(lines)
        write.flush()
        write.close()

    else:
        os.close(w)
        read = open(r, 'r')  # arch lee del "pipe"
        msm = read.readlines()
        print("msm env: ")
        for line in msm:
            print(line)


if __name__ == '__main__':
    main()
