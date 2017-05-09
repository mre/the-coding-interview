def byte_format(n, roundto=2):
    """
    Runtime: O(n)
    """
    units = ["B", "KB", "MB", "GB", "TB", "PB"]  # ...
    id = 0
    factor = 1024  # or 1000
    while n > factor:
        n = float(n) / factor
        id += 1
    n = "%.{0}f".format(roundto) % n
    return "{0} {1}".format(n, units[id])


print byte_format(156833213)  # "149.57 MB"
print byte_format(8101)      # "7.91 KB"
print byte_format(12331, 3)  # "12.042 KB"
