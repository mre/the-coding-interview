def main():
    with open("B-tiny-practice.in") as f:
        lines = [line.rstrip() for line in f.readlines()]
        testcases = int(lines[0])
        lines = lines[1:]
        for testcase in range(testcases):
            H, W = map(int, lines[0].split())
            print H, W


        #print("Case #{nr}: {count}".format(nr=i+1, count=len(valid)))

if __name__ == "__main__":
    main()
