import re

def formatter_brute(string, *args):
    for i, argument in enumerate(args):
        string = re.sub("\{" + str(i) + "\}", argument, string)
    return string

def formatter(string, *args):
    #tags = re.findall( r'\{(\d)\}', string)
    for word in string.split():
        print word
    #for i, argument in enumerate(args):
    #    string = re.sub("\{" + str(i) + "\}", argument, string)
    #return string

print formatter('Hello {0} {1}', 'Mr.', 'X')
print formatter('{1}_{0}', '{1}', '{0}')
