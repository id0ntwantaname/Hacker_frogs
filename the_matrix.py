import random, shutil, sys, time, bext

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['𓆏','𓆏']

DENSITY = 0.02

WIDTH = shutil.get_terminal_size()[0]-1

print("You are about to enter the matrix \n use Ctrl+C to quit")
time.sleep(0.02)

try:
    comlumns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if comlumns[i] == 0:
                if random.random() <= DENSITY:
                #Restarts the stream in this column
                    comlumns[i] = random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)

            if comlumns[i] >0:
                print(random.choice(STREAM_CHARS), end="")
                comlumns[i] -=1
            else:
                bext.fg("green")
                print(" ", end=" ")

        print()
        sys.stdout.flush()
        time.sleep(0)


except KeyboardInterrupt:
    sys.exit
