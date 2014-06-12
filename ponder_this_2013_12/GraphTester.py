from itertools import permutations

class Graph:
    def __init__(self, n):
        self.size = n

    def toString(self):
        result = ""
        for i in range(0, self.size):
            neighbors = self.neighbors(i)
            for j in range(0, self.size):
                if j in neighbors:
                   result += "1 "
                else:
                    result += "0 "
            result += "\n"
        return result

    def test(self):
        num_with_gifts = 0
        total = 0
        for p in permutations(range(0, self.size)):
            gifted = [0 for i in range(0, self.size)]
            for i in range(0, self.size):
                neighbors = self.neighbors(i)
                giftedID = max([p[j] for j in neighbors])
                giftedCoworker = [j for j in neighbors if p[j] == giftedID][0]
                gifted[giftedCoworker] = 1
            total += len(gifted)
            num_with_gifts += sum(gifted)
        indicator = num_with_gifts * 16 - \
            total * 9
        ratio = num_with_gifts / (1.0 * total)
        return (num_with_gifts, total, indicator, ratio)

class LinearGraph(Graph):
    def __init__(self, n):
        self.size = n

    def neighbors(self, i):
        return [j for j in range(i-1, i+2) if j >= 0 and j < self.size]

class CycleGraph(Graph):
    def __init__(self, n):
        self.size = n

    def neighbors(self, i):
        return [((j + self.size) % self.size) for j in range(i-1, i+2)]

class HyperCube(Graph):
    def __init__(self, n):
        self.size = 2 ** n
        self.dimension = n
    def neighbors(self, i):
        return [(i ^ (1 << j)) for j in range(0, self.dimension)]

class Star(Graph):
    def __init__(self, n):
        self.size = n
    def neighbors(self, i):
        if i == 0:
            return range(0, self.size)
        return [0, i]

if __name__ == "__main__":
    print "The 'star' graph on 4 nodes satisfies the necessary condition"
    g = Star(4)
    print "Below are some statistics computed by iterating over all permuations"
    print "of possible employee 'ID' rankings"
    print ""
    result = g.test()
    print "number of people with gifts over all permutations : " + str(result[0])
    print "total number of people over all permutations : " + str(result[1])
    print "indicator (negative iff ratio of previous quantities is < 9/16) : " \
        + str(result[2])
    print "numerically-computed ratio of gifted employees to non-gifted : " + \
        str(result[3])
    print ""
    print "The adjacency matrix for the graph is"
    print ""
    print g.toString()



