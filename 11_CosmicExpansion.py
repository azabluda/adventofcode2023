# https://adventofcode.com/2023/day/11
# Day 11: Cosmic Expansion

from bisect import bisect_left
from itertools import combinations

def cosmic_expansion(data):
    G = [(i, j) for i, row in enumerate(data.split('\n'))
                for j, val in enumerate(row) if val == '#']
    for n in 2, 10, 100, 1_000_000:
        res = 0
        for i in 0, 1:
            X = sorted(x[i] for x in G)
            U = list(set(X))
            for a, b in combinations(X, 2):
                d = bisect_left(U, b) - bisect_left(U, a)
                res += n * (b - a - d) + d
        yield res


def inputs():

    yield """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

    yield """
...........................#.......#.....................#................#.......................................#.............#...........
..................................................#...........................................#.......................................#.....
........#....................................#....................................#.......................#.................................
........................................................................................................................#...................
#...................#.......................................#...............................................................................
...............#.......................................................................#...........#...........#............#...............
........................................................#...........................................................................#.......
..............................................#.....................#...................................#...................................
.............................#......#.....................................#.................................................................
.......................#...........................#............................................#.................#.........................
.....#.....................................................................................................................................#
...........#......#...............................................#..............................................................#..........
.......................................................................................#...................#................................
..............................#........................#....................................................................#...............
.................................................#..........#......................................#........................................
........#................................#...................................................#..........#.....#......#......................
.........................#.........................................................................................................#........
............#.................................................................#.........#...................................................
....................#.......................................................................................................................
............................................#.............#.................................................................................
..............................#.....#...........................................................#........................................#..
#.........#........................................#............#................................................................#..........
.........................................................................................................#..................................
..................#.....................................#..............................#.............................#.......#..............
...........................#..............................................#.................................................................
...........................................................................................#......#.........................................
.......................#.......#..................#..........#....................................................................#......#..
.....#.............................................................#............................................#...........................
....................................#............................................#......................................#...................
.....................................................................................................................................#......
..............#.............................#.......#....................................#..................................................
.........#......................................................#.................................................#...........#.............
............................................................................................................................................
.#.....................................................................#..........#....................#....................................
..................................#....................................................................................................#....
...........#.........#............................#......#........................................#.........................................
................................................................................................................................#...........
..............................................................................................#.............................................
......................................#..............#.......................................................#...........#..................
....#............#.........................................#................................................................................
............#..............#.............................................................#..................................................
...............................................#...................................................#..........................#............#
..................................#.........................................................................................................
........................................................................#...........#...............................#.....#.................
#.........#..............#..................................................................................................................
.......................................................................................................................................#....
................#..........................................#................#................#.................#..................#.........
...................................................................#........................................................................
................................................#....................................................#......................................
.....................................................#..........................................#...........................................
..........................#.................................................................................................................
.....#.....#.....................................................................#.......#..............................#...................
.....................#........................#...............................................................#................#............
................................#........#............................................................#.....................................
.................................................................................................#................#.........................
..................................................................#.................................................................#.......
............................................................................................................................................
................................................#.....#.................#................#....................................#.............
......................#.....................................................................................#........#..................#...
..........#........................#................................................#.......................................................
....#.............#...................................................................................#...........................#.........
.........................................#..................................................#.....................#.........................
............................................................................................................................................
..........................#..................#..........................#.................................................#.................
.......................................................................................#......................#.............................
................................#......#.....................#................................#......................#..................#...
............................................................................................................................................
........#.........#.................................................................#.......................................#......#........
..........................................#........#........................................................................................
............................................................................................................................................
...............................................................................................#.......................#....................
............................#............................................................................#.................................#
............................................................................................................................................
......#...........#...................................#........#........#...................................................................
....................................................................................#.........................................#.............
.......................................#.........#......................................................................#...................
............................................................................................................................................
..............................#..................................................................................#..........................
.......................#......................................................#................#............................................
........#..........................................................#..................#................#...........................#........
.............#.....#................#.......................................................................................................
.........................................#...............................#.....................................#............................
.#...........................................................#...................#..................#.......................................
...........................#.................#............................................................................#.................
.......................................................#..................................................#.........#.....................#.
......................................................................................#........#............................................
......#.........#.................#............................#................................................................#...........
..........................................................................#.................................................................
...........#.........#.........................................................................................#............................
...........................................#..............#.................................................................#...............
.....................................................#.............#...................................................................#....
....#.........#.................#................................................................................................#..........
.......................#.......................................................#..................#........#............#...................
......................................#..................................#...................#..............................................
.......#.....................................#......................................................................#.......................
..#..........................#...........................#..........................#.......................................................
...........#.............................................................................#......................#......................#....
...............................................................#.........................................#..................#...............
.................#......................#........#...............................#..........................................................
......................#.......................................................................#......#..............................#.......
............................#......#......................#.................................................................................
...........................................#.............................#..........................................#.....#.................
...........#......................................................................................#.....................................#...
.......................................................#..........#....................................#.......#.................#..........
...............................#........................................................#...................................................
..#.....#.............................#................................#....................................................................
..................................................#...........................#.............................#...............................
.............................................................................................#.....#........................................
...............#........................................#.............................................................#.....................
#....................#...........#..........................................................................................................
............................#..............#..............................#.......................................................#.........
.....................................................................................#......................................................
.................#...........................................................................................#..............................
.........#..............#............................................................................................#...................#..
....................................#................#..............................................#.......................................
...............................#.........#.................#...................#.........................#..................#...............
#.............................................#........................................#....................................................
......................................................................#..........................................#..........................
.............#...............................................................................#........#...............................#.....
...#............................................................#............................................#..........#..................#
...................................................#........................................................................................
..........................................#..............................#..................................................#...............
.............................................................#....................#.....................................................#...
.....................#..............#..................#................................................#...................................
.......#.......................#........................................................#.......#..............#.................#..........
..........................................................................................................................#.................
...#.......................................#....................#...................#.......................................................
..................#.........................................................................................................................
...........................#...........#...................................................................#......#.........................
................................#.............#....................#........................................................................
.........................................................................................#.......#..........................................
.......#.....................................................#................................................................#...........#.
..................................................#.......................#.................................................................
.............#...................................................................................................#...................#......
............................#.........#................#.............................#................#.....................................
......................#.......................................................................#...........................#.................
............................................................................................................................................
.............................................................................................................#.......#............#.........
.......#...........#.....#.....#.............................#..............................................................................
.............#...............................#..........#..........................................#......................................#.
"""

for data in inputs():
    print(*cosmic_expansion(data.strip()))