"""
While the real Perseverance rover is having fun on Mars, we imagine an alternative version that scouts out an NxN grid of Mars according to the following rules:

Surveying a cell is possible only if all its upper neighbors were already explored. The upper neighbors of (a,b) are defined as (a-1,b-1), (a-1,b), (a-1,b+1). Cells that are not on the NxN grid do not need to be surveyed first.
Each cell has a "score" between 0-255 points, indicating how valuable it is to explore it.
Exploring a cell also requires rover maintenance, equivalent to a "cost" of 128 points.
The goal of the rover is to earn the maximum score possible from the grid. This means choosing which cells to explore that satisfy condition 1, such that the total score gained, considering 2 and 3, is the maximum score possible.

We represent the grid as an NxN array of numbers given in hexadecimal format.
As an example, consider the following 4x4 grid representation:

13 92 49 EC
BD 31 E8 FF
09 DD BE DE
C9 5A 1D 36

For example, the value -109 in cell (0,0) is obtained by converting 13 in hexadecimal notion to 16+3=19 and subtracting 128, obtaining -109.
Similarly, the value 18 in (0,1) is obtained by converting 92 to 9*16+2=146 and subtracting 128.

For the grid above, the optimal score is 424, and can be achieved via the following set:

[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
Your goal: Find the maximum score and a set of cells achieving it for the following 20x20 grid:
"""

grid = """BC E6 56 29 99 95 AE 27 9F 89 88 8F BC B4 2A 71 44 7F AF 96
72 57 13 DD 08 44 9E A0 13 09 3F D5 AA 06 5E DB E1 EF 14 0B
42 B8 F3 8E 58 F0 FA 7F 7C BD FF AF DB D9 13 3E 5D D4 30 FB
60 CA B4 A1 73 E4 31 B5 B3 0C 85 DD 27 42 4F D0 11 09 28 39
1B 40 7C B1 01 79 52 53 65 65 BE 0F 4A 43 CD D7 A6 FE 7F 51
25 AB CC 20 F9 CC 7F 3B 4F 22 9C 72 F5 FE F9 BF A5 58 1F C7
EA B2 E4 F8 72 7B 80 A2 D7 C1 4F 46 D1 5E FA AB 12 40 82 7E
52 BF 4D 37 C6 5F 3D EF 56 11 D2 69 A4 02 0D 58 11 A7 9E 06
F6 B2 60 AF 83 08 4E 11 71 27 60 6F 9E 0A D3 19 20 F6 A3 40
B7 26 1B 3A 18 FE E3 3C FB DA 7E 78 CA 49 F3 FE 14 86 53 E9
1A 19 54 BD 1A 55 20 3B 59 42 8C 07 BA C5 27 A6 31 87 2A E2
36 82 E0 14 B6 09 C9 F5 57 5B 16 1A FA 1C 8A B2 DB F2 41 52
87 AC 9F CC 65 0A 4C 6F 87 FD 30 7D B4 FA CB 6D 03 64 CD 19
DC 22 FB B1 32 98 75 62 EF 1A 14 DC 5E 0A A2 ED 12 B5 CA C0
05 BE F3 1F CB B7 8A 8F 62 BA 11 12 A0 F6 79 FC 4D 97 74 4A
3C B9 0A 92 5E 8A DD A6 09 FF 68 82 F2 EE 9F 17 D2 D5 5C 72
76 CD 8D 05 61 BB 41 94 F9 FD 5C 72 71 21 54 3F 3B 32 E6 8F
45 3F 00 43 BB 07 1D 85 FC E2 24 CE 76 2C 96 40 10 FB 64 88
FB 89 D1 E3 81 0C E1 4C 37 B2 1D 60 40 D1 A5 2D 3B E4 85 87
E5 D7 05 D7 7D 9C C9 F5 70 0B 17 7B EF 18 83 46 79 0D 49 59"""

## uncomment for testing
# grid = """13 92 49 EC
# BD 31 E8 FF
# 09 DD BE DE
# C9 5A 1D 36"""


"""
Solution approach:

Imagine the frontier of the explored cells.

If the deepest row that hax been explored in column i is r_i,
then, in column i+1, r_i-1 *must* have been explored, while
r_i+2 *cannot* have been explored.

This admits a simple sweepline dynamic programming solution.

Sweep through the columns, for each column, c, for each row, r, in c,
calculate the optimal value of the subproblem of what the maximum
score is on columns 0 through c for any valid set of cells such that
the last row explored in c is r.

This is just the sum of the values in c up to row r, plus the max of
the memoized values in [r-1, c-1], [r, c-1], and [r+1, c-1].

To then find the optimal set of cells for the whole grid, 
we find the highest memoized value for the last column, and sweep back
the other direction, determining whether this value came from
[r-1, c-1], [r, c-1], or [r+1, c-1].

"""

grid = [[int(x, 16) - 128 for x in g.split()] for g in grid.split("\n")]
# print(grid)

(rows, cols) = (len(grid), len(grid[0]))

memo = []

curr_col = [(0, None)]
runsum = 0

for row in range(rows):
    runsum += grid[row][0]
    curr_col.append((runsum, None))

memo.append(curr_col)

for col in range(1, cols):
    curr_col = []
    runsum = 0
    for row in range(rows+1):
        if row > 0:
            runsum += grid[row-1][col]
        prev_cands = range(max(row-1, 0), min(row+2, rows+1))
        best = -257
        best_cand = None
        for cand in prev_cands:
            if memo[-1][cand][0] > best:
                best = memo[-1][cand][0]
                best_cand = cand
        curr_col.append((runsum + best, best_cand))
    memo.append(curr_col)

best = -257
best_row = None
for i in range(rows+1):
    if memo[-1][i][0] >= best:
        best = memo[-1][i][0]
        best_row = i

# best_row = 11
# best = memo[-1][best_row][0]


results = []

print("best score is " + str(best))

for col in range(cols-1, -1, -1):
    for row in range(best_row):
        results.append((row, col))
    best_row = memo[col][best_row][1]

print("the following cells achieve the best score")
print(sorted(results))

print("")
print("")
print("resulting grid looks like")
print("")

whole_grid_sum = 0
results_sum = 0

for row in range(rows):
    to_print = []
    for col in range(cols):
        whole_grid_sum += grid[row][col]
        if (row, col) in results:
            to_print.append("{:2x}".format(grid[row][col] + 128))
            results_sum += grid[row][col]
        else:
            to_print.append("__")
    print(" ".join(to_print))

for row in range(rows):
    to_print = []
    for col in range(cols):
        if (row, col) not in results:
            to_print.append("{:2x}".format(grid[row][col] + 128))
        else:
            to_print.append("__")
    print(" ".join(to_print))

print("")
print("whole grid summed to " + str(whole_grid_sum))
print("selected cells summed to " + str(results_sum))

"""
And here we create a visualization of the costs of each cell overlaid
with the boundary of the optimal set of cells to explore.

If the image processing lib PIL does not exist on this system, then this
part exits out without producing a visualization.
"""


try:
    from PIL import Image

    scale = 15

    line_thick = 3

    im = Image.new("RGB", (scale * rows, scale * cols))

    tr = lambda a,b: (b, a)
    for row in range(rows):
        for col in range(cols):
            rgb = grid[row][col] + 128
            rgb = (rgb, rgb, rgb)
            if rgb[0] > 128:
                rgb = (min(255, rgb[0] + 20), rgb[1], max(0, rgb[2] - 20))
            elif rgb[0] < 128:
                rgb = (max(0, rgb[0] - 20), rgb[1], min(255, rgb[2] + 20))
            top_line = False
            if (row - 1, col) in results and not (row, col) in results:
                top_line = True
            left_line = False
            if (row, col-1) in results and not (row, col) in results:
                left_line = True
            if (row, col) in results and not (row, col-1) in results:
                left_line = True
            for c in range(scale*col, scale*(col + 1)):
                for r in range(scale*row , scale * (row + 1)):
                    is_line = False
                    if c < scale*col + line_thick:
                        is_line = is_line or left_line
                    if r < scale*row + line_thick:
                        is_line = is_line or top_line
                    if is_line:
                        im.putpixel(tr(r, c), (255,0,0))
                    else:
                        im.putpixel(tr(r, c), rgb)

    im.save("viz.png")

except:
    print("Could not produce visualization image : no PIL")
