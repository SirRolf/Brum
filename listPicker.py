from random import randint

def RandomList(aList, chances):
    package = aList
    result = 0
    maxScore = 0
    catagory = 0
    for i in chances:
        maxScore += i

    score = randint(0, maxScore)
    # check in what catagory score lands
    for i in chances:
        catagory += i
        if catagory >= score:
            package = aList[result]
            return package
        result += 1
