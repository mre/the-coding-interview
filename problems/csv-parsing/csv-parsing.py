
def to_csv(tokens):
    csv = []
    for t in tokens.split("'"):
        try:
            val = int(t)
            csv.append(val)
        except:
            csv.append(str(t))
    return csv

print to_csv('2,6,3,2,5')
print to_csv('"pears","apples","walnuts","grapes","cheese,cake"')
