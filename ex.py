import itertools
def braStr(string1):
    return '(' + string1 + ')'

def steps(input,list1 = []):
    if len(input)==2:
        list1.append(braStr(input[0]+ '+' + input[1]))
        list1.append(braStr(input[0]+ '-' + input[1]))
        list1.append(braStr(input[0]+ '*' + input[1]))
        list1.append(braStr(input[0]+ '/' + input[1]))
    else:
        for e in itertools.permutations(input):
            steps((braStr(e[0]+ '+' + e[1]),) + e[2:],list1)
            steps((braStr(e[0]+ '-' + e[1]),) + e[2:],list1)
            steps((braStr(e[0]+ '*' + e[1]),) + e[2:],list1)
            steps((braStr(e[0]+ '/' + e[1]),) + e[2:],list1)

while True:
    cards = raw_input("Please enter the 4 cards: ").split()
    if len(cards) != 4:
        print "you need 4 cards to begin!"

    list1 = []
    steps(cards,list1)
    result = False
    for e in list1:
        try:
            if eval(e) == 24:
                print e + '=', eval(e)
                result = True
        except:
            continue
    if result is False:
        print 'No way'