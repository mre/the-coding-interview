import sys, time

def get_data():
    numcases = int(sys.stdin.readline())
    for case in range(1,numcases+1):
        data = []
        while True:
            line = sys.stdin.readline().strip()
            if line:
                data.append(line)
            else:
                break
        yield (case, data)


def main():
    for case, data in get_data():
        #blub
