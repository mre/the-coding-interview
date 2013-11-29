def format_money(f):
    """
    Runtime: O(n)
    """
    result = []
    i = str(int(f))
    for pos, digit in enumerate(i):
        result.append(digit)
        if pos % 3 == 0 and pos < len(i)-1:
            result.append(" ")
    cents = f - int(f)
    rounded = "%.2f" % cents
    result.append(rounded)
    return "".join(result)

print format_money(2310000.159897) # '2 310 000.16'
print format_money(1600) # '1 600.00'
