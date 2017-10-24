def is_rotation_brute(string, candidate, stop=""):
    if string == candidate:
        return True
    if candidate == stop:
        # Tried all rotations
        return False
    if not stop:
        stop = candidate
    rot = candidate[1:] + candidate[0]
    return is_rotation(string, rot, stop)


def is_rotation(string, candidate):
    for rotation in range(len(candidate)):
        if string == candidate:
            return True
        candidate = candidate[1:] + candidate[0]
    return False


def is_rotation2(original, candidate):
    return len(original) == len(candidate) and candidate in original*2


print is_rotation("ABCD", "ABCD")
print is_rotation("ABCD", "BCDA")
print is_rotation("ABCD", "ACBD")
print is_rotation("ABCD", "BCDA")
