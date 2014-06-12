# Solution finder for Nov 2013 IBM Reseach "Ponder This" challenge
#
# For context, see puzzle description at
# http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/November2013.html
#
# A brief problem description lifted from the above web page follows
#
# A three-dimensional cube has eight vertices, twelve edges, and six faces.
#  Let's call them 0-D, 1-D, and 2-D faces, respectively.
# Denote f(d,k) as the number of k-dimensional faces of an d-dimensional
#  hyper cube, so f(3,1)=12.
# Find three cubes (with different dimensions d1, d2, and d3) such that the
#  number of k1, k2, and k3 dimension faces are the same,
#  i.e. f(d1,k1) = f(d2,k2) = f(d3,k3).
# We are looking for nontrivial solutions, so k1 should be less then d1.
# Bonus: Find more than three.


class SolutionFinder:
    def __init__(self):
        # We let each dth row of self.rows represent the number
        # of k-faces of a d-cube for each k from 0 to d (inclusive)
        #
        # To start, there is exactly 1 0-face (point) of a 0-cube (point)
        self.rows = [[1]]
        #
        # We also want to count the number of distinct k and d for which
        # the number of k-faces of a d-cube matches a given count.
        # The face count is the key of this map, the value is the number of
        # times we've found a d-cube with that (key) many k-faces.
        self.counts = {}
        self.max_count = 1


    # The next function actually computes the number of k-faces of a d-cube
    # and updates the "self.counts" map accordingly
    #
    # So there are two equivalent ways to reason about the number of
    # k-faces in a d-cube.
    #
    # The first is that there are (d choose k) ways to pick the k axis
    # for the face, and there are 2 ** (d - k) positions along the
    # remaining (d - k) dimenions to pick the face.
    #
    # The second is that a d-cube can be constructed by gluing two
    # (d - 1)-cubes, one offset from the other along the dth dimension.
    # Each k-face in the resulting d-cube was either
    #  - A k-face in one of the two (d - 1)-cubes
    # or
    #  - The result of gluing together two (k - 1)-faces, one from each
    #    (d - 1)-cube, each differing only along the d axis.
    #
    # If we let Faces(d, k) be the number of k-faces of a d-cube,
    # the second derivation gives us the formula
    # Faces(d, k) = 2 * Faces(d - 1, k) + 1 * Faces(d - 1, k - 1)
    # which is the form we use here.
    #
    # Amusingly this formula bears a striking similarity to the construction
    # for Pascal's triangle -- which describes the number of
    # k-faces on a d-simplex.
    def nextRow(self):
        # next_row = np.convolve(self.rows[-1], np.array([2,1]))
        next_row = [2 * x[0] + x[1] for x in zip(self.rows[-1] + [0], \
                                                     [0] + self.rows[-1])]
        for item in next_row[:-1]: # eliminate trivial solutions
            self.counts[item] = self.counts.get(item, 0) + 1
            self.max_count = max(self.max_count, self.counts[item])
        self.rows.append(next_row)
        return len(self.rows)

    # What is the maximum d for which we have calculated the number of
    # k-faces of a d-cube?
    def dimensionCalculated(self):
        return len(self.rows) - 1

    def printLatestRow(self):
        print self.rows[-1]

    # Finds all face-counts for which we have found "level" distinct
    # k and d for which there are (face-counts) many k-faces of a d-cube
    def findSolutions(self, level=3):
        return [i for i in self.counts.keys() if self.counts[i] >= level]

    # Find all the combinations of d and k for which there are n
    # k-faces in a d-cube
    def printDCubesWithKFacesEqualTo(self, n):
        num_found = 0
        for d in range(0, len(self.rows)):
            row = self.rows[d]
            for k in range(0, len(row)):
                if (row[k] == n):
                    print "There are " + str(n) + " " + str(k) + \
                        "-faces in a " + str(d) + "-cube"
                    num_found += 1
        print "There are at least " + str(num_found) + " d-cubes with " + \
            str(n) + " k-faces"

if __name__ == "__main__":
    thing = SolutionFinder()
    while len(thing.findSolutions()) < 1: # default parameter is "3"
        thing.nextRow()
        thing.printLatestRow()
    # and so we blithely assume we'll find one. Which we print out.
    thing.printDCubesWithKFacesEqualTo(thing.findSolutions()[0])
    # Let's try for the bonus and look for sequences of 4
    # combinations of d and k all having the same Faces(d, k)
    # The number of dimensions we try to here is somewhat arbitrary.
    while thing.dimensionCalculated() < 1640 and \
            thing.max_count < 4:
        thing.nextRow()
        d = thing.dimensionCalculated()
        if (d % 10) == 0:
            print d
    sols_for_4 = thing.findSolutions(4)
    # thing.printLatestRow()
    for n in sols_for_4:
        thing.printDCubesWithKFacesEqualTo(n)
    if not sols_for_4:
        print "Didn't find solutions for 4 in up to " + \
            str(thing.dimensionCalculated()) + " dimensions"
    for n in thing.findSolutions(3):
        thing.printDCubesWithKFacesEqualTo(n)
