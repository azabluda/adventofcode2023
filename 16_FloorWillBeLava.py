# https://adventofcode.com/2023/day/16
# Day 16: The Floor Will Be Lava

def floor_will_be_lava(data):
    lines = data.split('\n')
    m, n = len(lines) - 1, len(lines[0]) - 1
    A = {r + 1j * c: val
         for r, row in enumerate(lines)
         for c, val in enumerate(row)}
    B = [(r, 1j) for r in range(m + 1)] + \
        [(r + n * 1j, -1j) for r in range(m + 1)] + \
        [(c * 1j, 1) for c in range(n + 1)] + \
        [(m + c * 1j, -1) for c in range(n + 1)]
    part1 = part2 = 0
    for start in B[::-1]:
        vis, res = set(), set()
        bfs = [start]
        for posdir in bfs:
            pos, dir = posdir
            if posdir in vis: continue
            if pos not in A: continue
            vis.add(posdir)
            res.add(pos)
            ndir = [1, -1] if A[pos] == '|' and dir.imag else \
                   [1j, -1j] if A[pos] == '-' and dir.real else \
                   [dir * [-1j, 1j][not dir.real]] if A[pos] == '/' else \
                   [dir * [-1j, 1j][not dir.imag]] if A[pos] == '\\' else \
                   [dir]
            bfs += ((pos + d, d) for d in ndir)
        part1 = len(res)
        part2 = max(part2, len(res))
    return part1, part2


def inputs():

    yield r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

    yield r"""
\..../...................-......|..........|...-|.-.............|...................\/......-.................
../|....|.......-...............\....\...........-...............|.......|...........-........................
............................\........../|........./.......................................\.........|....|./||
..................\.//.............-.......\..-.|.......\.......\.............................-..-....|.......
../....\......|.|......|.....|./.-...|......-................//......|.../..-........\............\...........
...|...-.....\...............-.../.................|...............\-................/|...............\.......
|............................./...\.........\.............-....../-..|......|.|.../................\..........
.............-.|.../................|....................../................../..............................-
.......\.\....../.....|...........................-............/..-........-........................\......-..
.....-.\................-.....|\....-....|..../....|.....|.\............./.../.....\...............|....|.....
....|............................/............-|..|.........................-....................-....\.......
|....../......../../............................../....|......\..\....\\./.|................/......\......-./\
........-........./|............................./....\....-................../...|........|........-.........
..........\......./..................|..../.........../.........../........../...................|.-.\.......\
................-..........\....................................../.........\\........-...--..........|..\....
.-./...\......................\...../...\.\../.......|....................-...............\.-....\......./\..\
.......................-.......\..............................\............................\.|...-............
.......|...-..........-........-.......\.........././.-..|..../.....................\.........................
.....................\..|...../........\.....\\\..........\........................-............\..\...\......
....|.................|.........|.................................../.............-...........................
......................|................../....\..|...................-.\.......-\.........................|...
........-.........|.......\.................|................-..|../|\............../......................../
............|.\.................\..-...\.../...-....\...\...........|../..\........\.-........................
......./..............-..//................-.............../................/...-.......-......-............|.
........\|...\......-....|...........\....\./..........-......\......../..-...-...|........|/................\
....\....-../......-..................................|..\/../....-.....|...............\.-.....\............|
...................|..................|...........\............./.......-.......................\..\-../../...
....-..............-..\/.|.......................\.................../......|..-..\......|.........-/.........
........................./..\-..-.|..........-.....-............................\...................../.......
...../../..../....|...|..|...|.......\..\...\........-..../.../......................-....../..\..............
..........\.......\.....|.../.........../....|./.../......-..../.....|-...||......./..........|...\...........
...............................................-.........\.....|..................\|......................\...
.....................................\..................--......-........................-.//-....../-.-.....|
........../..../.....|....\........................|.................................../............./...-/...
........................-............./....-....-...-...........-..............|..............................
......|.....|........-./...\........|......................|........|.......|...-.....|.......................
..-.......-....../.............-..\...................................|.........|..........|............./....
.............................|.....\...........................././|......|................-....-.............
........../..................-..........\....\..../.....\.................-...........|.......................
................../..-......................|...........-|..............-......|......................-.......
-...........-..........|........-.......|\.././.|............................-/.|...........-/...............\
.../..-..........................--.........|...|.|...................................-|...\........|.........
........|.......-............|.........--.........-......./..../........-........\....../..../...........-....
..............-.............../...........................-................./......--..\..../.................
.......................--...........\..............\.......-.......-..|/.....\....-/......../........-........
.............|......|...............-...................\...............\..-.....................|.\.........\
.....\.-....\............\........|........|....\..............\............................................./
............................../...............././.......\.....\..........\|......-......|....|...........|...
................|............/.....|.........|.......\...../...|....-........|................................
./...\............\............|..-....\...\........................\..........\......\.-........../.....\....
.......-...|../..|..-.......-............................................-.....\.........-........../../......
...../.......-......../|..............|...................\......|............/|..........|..|...../..-...|..-
....-.........../../....../\.................................\./.....................-...........-............
.....|....................|.....|.......-..-.........\........|..............|...............-|.|....-/..-....
.\|............-../..\.\.....|....../...|.............\.............................................\.........
........|........../...\....-.......\..\.|-...........|./|./..........\|........--...\........\../............
\..-..-......./.\....../....\..|.........\-...-||/...-...\....\.......-.\.......-................\...\.....\..
................................\............../..-.......................-............./.....................
\............................/...........-......\..-.......-.........../............|...............|.........
......|..|........\.........................../.......-.............-.................../.....................
..........................|......|.../..........................\..................................-......-...
../...................-.........|...\...........-.|/..........|........-.-.................|.......|.........\
........................../......../..................\...........|......\.......................-............
...../..../\.../|....\....................................|....|......................|.........\...........-.
.|...../.....-.....................................|........||........|...........................//..........
........................\............|.............-..........................-......../..............|.......
...................\.........-.........\..........|......................../\...-......................\|.....
........././...........|.|..................../.....................-.............................-.|.|...-...
.-................................................-................-..\........-................../.\....|...|
.................../.|......\..\.\./.\.............|.......................................|..................
...............|............\\.....-..-.........\.....\-|..../............|\.......|.....\.\...../......\.....
...-.............../..........\.....-..|....../......................-.....\.................../.\...........\
...................-.....................................\....\....../....|..\...-................\......-....
.|..-............\........|.....|.\....\......-............\.|....|.\..............\|.|/...\.........|....../.
........../...........|.-/...\......./../.............../.\/......-/........................./......\..|......
........|......................................\..................|............................/........-.-...
...\....../................/...................\../...\\...................\.......|.................-........
.....................................|.........../.\..--.........|\..........|.....-..................|...\...
.../...........\-..-....................\.-..-..........................-........|..../.......................
.........../-.../.............../.\................-.-..\.......\/............\......../...\\\......../.......
.......-..\...\.....\..\...........................|..\.......//..................../../.........|.........-..
......./............../...../.............../............/...../.............\......-...........\...-|.......-
..|......\....................../..................\..................|.....................-....\............
../........................\............/.../...............|............-......................./............
.-...../......\............\............|..........................\../.....\.....................-|.../......
...........|.......\....\.............................\.....................--.....|......................../.
...|......./-.........................../.\......................|................|......|....|../...../......
...-............./..../................-......-....\\..|\...........|...................../....\|.\.-.....-...
............./..//...........|...\|........-/..../.............|......................../.../.................
......\........|........\...\.\........../..../..-.....-......./..|............-......................-.......
....-./............|......|........................./.........\......................................\........
...................................-.........-..../....|../...........\..-....-.|..................../...././.
-...........|.-.......|.../.................|......./.....\..\......|.................................\....\..
......\.....................-....................-......................................|.....................
................................\.......-...........|\......................./..........\-..-................|
....../......|..................\.....|....\...........\...........................................\.......|..
..............-..\..|\.../............\..\.....-.....|.|\......\...................|.........\...........-....
.-.-..\....././.........\.|...-....\....|....|............|..................../.............\................
...|..................................................-.............\../......................................
\................-....................-./.........../.......\./..\|..|....../..-\.-...\..../.....-....|.......
................|.................\|./................-..././\......../...................|....|....|.........
........-...............................................\........................\.........................../
....../..............................\....\...|........\.-........\...............|..../.........../...|......
../....................................|...|...............................\.\..|.............................
...|/|............|............/..........................\.......\.......-.../..--../...........\|...........
.......-..........\...........\/.....-./../................|.|........\\.................................-....
..|..\............\...|........../................................../...................|.\.............-.....
....-.......\/................../....|................-.././..|.........-..........\.|.........../...../..|...
/../.|..............||...\..........\....-.../.....\-..........-.......-........................-.../...\.....
../.|....|......../........-...........................\\......................\...................-..........
"""

for data in inputs():
    print(*floor_will_be_lava(data.strip()))