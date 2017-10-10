def memoize(f):
    cache = {}

    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    memoizedFunction.cache = cache
    return memoizedFunction


def makePalindromeRecursion(input):
    if len(input) <= 1:
        return input, 0
    if input[0] == input[-1]:
        temp = makePalindromeRecursion(input[1:len(input)-1])
        return input[0] + temp[0] + input[-1], temp[1]
    else:
        i = makePalindromeRecursion(input[:len(input)-1])
        j = makePalindromeRecursion(input[1:len(input)])
        if i[1] < j[1]:
            return input[-1] + i[0] + input[-1], i[1] + 1
        else:
            return input[0] + j[0] + input[0], j[1] + 1


@memoize
def makePalindromeTest(input):
    if len(input) <= 1:
        return input, 0
    if input[0] == input[-1]:
        temp = makePalindromeTest(input[1:len(input)-1])
        return input[0] + temp[0] + input[-1], temp[1]
    else:
        i = makePalindromeTest(input[:len(input)-1])
        j = makePalindromeTest(input[1:len(input)])
        if i[1] < j[1]:
            return input[-1] + i[0] + input[-1], i[1] + 1
        else:
            return input[0] + j[0] + input[0], j[1] + 1


def makePalindromeMemo(input):

    memo = dict()

    def helper(sipt):
        if len(sipt) <= 1:
            return sipt, 0
        if sipt in memo:
            return memo[sipt]
        elif sipt[0] == sipt[-1]:
            middle = sipt[1:len(sipt)-1]
            if middle in memo:
                return sipt[0]+memo[middle][0]+sipt[0],memo[middle][1]
            else:
                temp = helper(middle)
                memo[middle] = (temp[0], temp[1])
            return sipt[0]+memo[middle][0]+sipt[0],memo[middle][1]
        else:
            i = sipt[:len(sipt)-1]
            j = sipt[1:len(sipt)]
            if i in memo:
                i_r = memo[i]
            else:
                i_r = helper(i)
                memo[i] = i_r
            if j in memo:
                j_r = memo[j]
            else:
                j_r = helper(j)
                memo[j] = j_r
            if i_r[1] < j_r[1]:
                memo[sipt] = sipt[-1]+i_r[0]+sipt[-1], i_r[1]+1
                return memo[sipt]
            else:
                memo[sipt] = sipt[0]+j_r[0]+sipt[0], j_r[1]+1
                return memo[sipt]

    ret = helper(input)

    return ret


def main():
    palin = makePalindromeMemo("raecarzkjalsjdakljdakljdakjsdlakjdlakjdlajda")
    print(palin)


if __name__ == "__main__":
    main()