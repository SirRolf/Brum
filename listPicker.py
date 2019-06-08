from random import randint

def RandomList(list, chances):
    package = list
    result = 0
    for i in chances:
        maxScore += i

    score = randint(0, maxScore)
    # check in what catagory score lands
    for i in chances:
        catagory += i
        if catagory >= score:
            package = list[result]
            return package
        result++;
