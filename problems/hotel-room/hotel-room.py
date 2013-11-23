from math import sqrt

def divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            divisors.append(n)
    return divisors

def subsets(l):
    for start in range(len(l)-1):
        for end in range(start+1, len(l)-1):
            yield l[start:end+1]

def get_room_nr(rooms):
    for roomnr in range(1,rooms+1):
        div = divisors(roomnr)
        if sum(div) <= roomnr:
            continue

        found = False
        for s in  subsets(div):
            if sum(s) == roomnr:
                found = True
                break
        if not found:
            return roomnr

print get_room_nr(100)

