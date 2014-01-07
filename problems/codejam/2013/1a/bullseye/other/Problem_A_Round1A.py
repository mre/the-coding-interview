import math


def calc_ans(r, t):
    d = 4*r*r - 4*r + 1 + 8*t + 0.0
    n = int(((1 - 2*r)**2 - d) / (4 * (1 - 2*r - math.sqrt(d))))
    return n


def main():
    filename = 'input_a.in'
    filename_out = 'output_a.txt'
    result_lines = []
    with open(filename, 'r') as input_file:
        t = int(input_file.readline())
        for test_case in xrange(1, t + 1):
            [r, t] = [int(x) for x in input_file.readline().split()]
            ans = calc_ans(r, t)
            line = 'Case #' + str(test_case) + ': ' + str(ans) + '\n'
            result_lines += [line]
    with open(filename_out, 'w') as output_file:
        output_file.writelines(result_lines)


main()
