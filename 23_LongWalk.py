# https://adventofcode.com/2023/day/23
# Day 23: A Long Walk

def long_walk(data):
    lines = data.split('\n')
    s, e = 1j, (1 + 1j) * (len(lines) - 1) - 1j
    A = {r + 1j * c: val
         for r, row in enumerate(lines)
         for c, val in enumerate(row)}
    def wasd(u):
        V = (u + 1j ** i for i in range(4))
        return [v for v in V if A.get(v, '#') != '#']
    def is_junction(p):
        return A[p] != '#' and len(wasd(p)) > 2
    def is_blocked(w, v):
        i = 'v>^<'.find(A[w])
        return i >= 0 and w - v != 1j ** i
    V = {s, e, *filter(is_junction, A)}
    for part in 1, 2:
        G = {u:{} for u in V}
        for u in V:
            bfs, vis = [(u, 0)], {u}
            for v, d in bfs:
                for w in wasd(v):
                    if w in vis: continue
                    if part == 1 and is_blocked(w, v): continue
                    vis.add(w)
                    if w in V: G[u][w] = d + 1
                    else: bfs += (w, d + 1),
        def dfs(u, path, ln):
            if u == e: return ln
            if u in path: return 0
            return max(dfs(v, path | {u}, ln + G[u][v]) for v in G[u])
        yield dfs(s, set(), 0)


def inputs():
    yield """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

    yield """
#.###########################################################################################################################################
#.###.....#.........###...#...#...#####...#...#.......#...###...#.............#.......#.....#...#...#...#...#.............###...#...#...#...#
#.###.###.#.#######.###.#.#.#.#.#.#####.#.#.#.#.#####.#.#.###.#.#.###########.#.#####.#.###.#.#.#.#.#.#.#.#.#.###########.###.#.#.#.#.#.#.#.#
#.#...#...#.#.......#...#...#...#...#...#...#...#.....#.#.###.#.#.........#...#.#.....#...#.#.#.#.#.#.#.#.#.#...........#.#...#.#.#.#.#.#.#.#
#.#.###.###.#.#######.#############.#.###########.#####.#.###.#.#########.#.###.#.#######.#.#.#.#.#.#.#.#.#.###########.#.#.###.#.#.#.#.#.#.#
#.#.#...#...#...#...#...#...........#...........#.###...#.#...#.>.>.#...#.#...#.#...>.>.#.#.#.#.#.#.#.#.#.#.#...#...###.#.#.#...#.#.#.#...#.#
#.#.#.###.#####.#.#.###.#.#####################.#.###.###.#.#####v#.#.#.#.###.#.#####v#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.###.#.#.#####.#
#...#...#.#.....#.#.###.#.#...#.......###...###.#.#...###...#.....#.#.#.#...#...###...#...#...#.#.#.#.#...#.#.#.#.#.#...#.#.#...#.#...#...#.#
#######.#.#.#####.#.###.#.#.#.#.#####.###.#.###.#.#.#########.#####.#.#.###.#######.###########.#.#.#.#####.#.#.#.#.#.###.#.###.#.#####.#.#.#
#.......#.#.###...#...#.#.#.#.#.....#.#...#...#.#.#.......###.#...#.#.#...#.#.....#.........#...#.#.#.#.....#.#.#.#.#.#...#...#...###...#.#.#
#.#######.#.###.#####.#.#.#.#.#####.#.#.#####.#.#.#######.###.#.#.#.#.###.#.#.###.#########.#.###.#.#.#.#####.#.#.#.#.#.#####.#######.###.#.#
#.#.....#.#.....#.....#.#.#.#.#.....#.#.....#.#.#.#.....#...#...#.#.#...#...#...#.#.......#.#.#...#...#.....#.#...#.#.#.......#...#...###...#
#.#.###.#.#######.#####.#.#.#.#.#####.#####.#.#.#.#.###.###.#####.#.###.#######.#.#.#####.#.#.#.###########.#.#####.#.#########.#.#.#########
#...###...#.......#...#.#.#.#.#.#.....###...#.#.#...###.....#...#.#.....#...#...#.#.....#.#.#.#...#.........#.....#...#.......#.#...###.....#
###########v#######.#.#.#.#.#.#.#.#######.###.#.#############.#.#.#######.#.#.###.#####.#.#.#.###.#.#############.#####.#####.#.#######.###.#
###...#...#.>.#.....#.#.#.#.#.#.#.>.>.#...#...#...#...........#...###.....#.#...#.#...#.#.#.#.#...#.....#.>.>.....#...#.....#.#.........#...#
###.#.#.#.#v#.#.#####.#.#.#.#.#.###v#.#.###.#####.#.#################.#####.###.#.#.#.#.#.#.#.#.#######.#.#v#######.#.#####.#.###########.###
#...#...#...#.#...#...#.#.#.#.#.#...#...###...#...#...#...#.........#.#...#.....#...#...#...#...###...#.#.#.........#...#...#.............###
#.###########.###.#.###.#.#.#.#.#.###########.#.#####.#.#.#.#######.#.#.#.#########################.#.#.#.#############.#.###################
#...#.......#.#...#.....#.#.#...#.#...#...###...#...#...#...#.......#...#.............#...#.........#.#...#...#.....#...#...#.....#.........#
###.#.#####.#.#.#########.#.#####.#.#.#.#.#######.#.#########.#######################.#.#.#.#########.#####.#.#.###.#.#####.#.###.#.#######.#
#...#.#.....#...###...###...###...#.#...#.........#...#.......#...###.................#.#.#.........#.......#.#...#...#####...###...#...#...#
#.###.#.###########.#.#########.###.#################.#.#######.#.###.#################.#.#########.#########.###.###################.#.#.###
#.#...#.#...#...#...#.........#.....###...........#...#.........#...#.....#...#...###...#.#...#...#.........#.#...#.....#...#...#...#.#...###
#.#.###.#.#.#.#.#.###########.#########.#########.#.###############.#####.#.#.#.#.###.###.#.#.#.#.#########.#.#.###.###.#.#.#.#.#.#.#.#######
#...###.#.#.#.#...#...........#.........#.....###...###.............#...#...#...#...#.#...#.#.#.#.###...#...#.#...#...#.#.#.#.#.#.#.#.#...###
#######.#.#.#.#####.###########.#########.###.#########.#############.#.###########.#.#.###.#.#.#.###.#.#.###.###.###.#.#.#.#.#.#.#.#.#.#.###
#.......#.#.#.....#...#.....###...........#...#...#...#.........#...#.#...###.......#.#.###.#.#.#.#...#...###.....###.#...#...#...#...#.#...#
#.#######.#.#####.###.#.###.###############.###.#.#.#.#########.#.#.#.###.###.#######.#.###.#.#.#.#v#################.#################.###.#
#.......#.#.#.....#...#.#...#...#...#...#...#...#.#.#...#.......#.#.#...#.....###...#.#.#...#...#.>.>.#...###...###...#...#.............#...#
#######.#.#.#.#####v###.#.###.#.#.#.#.#.#v###.###.#.###.#.#######.#.###.#########.#.#.#.#.#########v#.#.#.###.#.###.###.#.#.#############.###
#.....#...#...#...#.>.#.#.#...#.#.#.#.#.>.>.#...#.#.#...#.....###.#...#.......###.#.#.#.#...#.......#...#.....#...#.....#.#.#.............###
#.###.#########.#.#v#.#.#.#.###.#.#.#.###v#.###.#.#.#.#######v###.###.#######.###.#.#.#.###.#.###################.#######.#.#.###############
#...#.#...#...#.#.#.#.#.#.#...#.#.#...#...#...#.#.#.#...#...>.>.#.#...#...###.#...#.#.#.#...#.#.....###...........#.....#...#...........#####
###.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#####.#####.#.#.#.###.#.###v#.#.#.###.#.###v#.###.#.#.#.###.#.###.###.###########.###.###############.#####
#...#.#.#.#.#...#...#...#.#...#.#.###...#####...#.#...#.#.###.#.#.#...#.#.#.>.>.###.#.#.#...#...###...#...###...###...#.#.............#.....#
#.###.#.#.#.#############.#.###.#.###.###########.###.#.#.###.#.#.###.#.#.#.#v#####.#.#.###.#########.###.###.#.#####.#.#.###########.#####.#
#...#.#.#.#...#.........#.#.#...#...#.......#.....#...#...#...#...###...#...#.....#.#.#.#...###.......###...#.#...#...#.#.........###.......#
###.#.#.#.###.#.#######.#.#.#.#####.#######.#.#####.#######.#####################.#.#.#.#.#####.###########.#.###.#.###.#########.###########
#...#...#.###...#...#...#...#.....#.#.......#...#...#.....#.........#.............#...#.#.#.....#...#...###...#...#...#.#...#...#.....#######
#.#######.#######.#.#.###########.#.#.#########.#.###.###.#########.#.#################.#.#.#####.#.#.#.#######.#####.#.#.#.#.#.#####.#######
#...#...#.#...#...#.#...#...#...#...#.........#.#.###...#.......#...#.........#.......#...#.......#...#.....###.#.....#.#.#.#.#.#...#.......#
###.#.#.#.#.#.#.###.###.#.#.#.#.#############.#.#.#####.#######.#.###########.#.#####.#####################.###.#.#####.#.#.#.#.#v#.#######.#
#...#.#.#...#...###.....#.#...#.............#.#.#.#.....#.....#...#...#.......#.#.....###...............#...#...#.....#.#.#...#.>.#.#.......#
#.###.#.#################.#################.#.#.#.#.#####.###.#####.#.#.#######.#.#######.#############.#.###.#######.#.#.#######v#.#.#######
#.....#.................#...#.....#.......#.#.#.#.#.#.....###.......#.#.........#.......#.............#.#.###...#...#.#.#.#.......#...###...#
#######################.###.#.###.#.#####.#.#.#.#.#.#.###############.#################.#############.#.#.#####.#.#.#.#.#.#.#############.#.#
#.......................###...#...#.#.....#.#.#.#.#.#.#...............#...........#.....#.............#...#.....#.#.#.#.#.#...#...#.......#.#
#.#############################.###.#.#####.#.#.#.#.#.#.###############.#########.#.#####.#################.#####.#.#.#.#.###.#.#.#.#######.#
#...........................#...#...#.....#...#.#.#...#...............#.........#.#.....#.#...............#.....#.#.#.#.#.###...#...#.......#
###########################.#.###.#######.#####.#.###################.#########.#.#####.#.#.#############.#####.#.#.#.#.#.###########.#######
#...#.....#.....#...#.....#.#.....#...#...#...#...###...#...#.........###...#...#...#...#...#.............#.....#.#...#...#.........#.......#
#.#.#.###.#.###.#.#.#.###.#.#######.#.#.###.#.#######.#.#.#.#.###########.#.#.#####.#.#######.#############.#####.#########.#######.#######.#
#.#.#...#.#...#...#.#...#.#.#.......#...#...#.#.....#.#...#.#.....#...#...#...#...#...###...#.............#.......#.....#...#.....#...#.....#
#.#.###.#.###.#####.###.#.#.#.###########.###.#.###.#.#####.#####.#.#.#.#######.#.#######.#.#############.#########.###.#.###.###.###.#.#####
#.#.....#...#.....#.....#...#.............#...#...#.#...#...###...#.#.#.........#...#.....#...#...........#...#...#...#.#.....###...#...#...#
#.#########.#####.#########################.#####.#.###.#.#####.###.#.#############.#.#######.#.###########.#.#.#.###.#.###########.#####.#.#
#.........#.#.....#...#...#...#.............#...#.#.#...#.#...#.....#.#...###.......#...#.....#.......#...#.#.#.#.#...#.#...###...#.....#.#.#
#########.#.#.#####.#.#.#.#.#.#.#############.#.#.#.#.###.#.#.#######.#.#.###.#########.#.###########.#.#.#.#.#.#.#.###.#.#.###.#.#####.#.#.#
#.....#...#.#.....#.#.#.#.#.#.#.........#...#.#.#.#.#...#.#.#.#.......#.#.#...#...#...#.#.#...#...#...#.#.#.#.#.#.#...#.#.#.###.#.#.....#.#.#
#.###.#.###.#####.#.#.#.#.#.#.#########.#.#.#.#.#.#.###.#.#.#.#v#######.#.#.###.#.#.#.#.#.#.#.#.#.#v###.#.#.#.#.#.###.#.#.#.###.#.#v#####.#.#
#...#...###.......#.#.#.#.#.#.#...#.....#.#...#.#.#.#...#.#.#.>.>.....#.#.#...#.#...#.#.#.#.#...#.>.>...#.#.#.#.#.#...#.#.#...#.#.>.#.....#.#
###.###############.#.#.#.#.#.#.#.#.#####.#####.#.#.#.###.#.###v#####.#.#.###.#.#####.#.#.#.#######v#####.#.#.#.#.#.###.#.###.#.###v#.#####.#
#...#...###.....#...#...#.#.#.#.#...#...#.....#.#.#.#.#...#...#...###...#...#.#...#...#.#.#...#...#.....#.#.#...#.#.###.#.#...#.#...#.#.....#
#.###.#v###.###.#.#######.#.#.#.#####.#.#####.#.#.#.#.#.#####.###.#########.#v###.#.###.#.###.#.#.#####.#.#.#####.#.###.#.#.###.#.###.#.#####
#.....#.>.#.#...#.....#...#.#.#.......#.###...#.#.#.#.#...#...###...#...###.>.>...#.....#.#...#.#.......#.#.#.....#.#...#.#.....#...#.#.#...#
#######v#.#.#.#######.#.###.#.#########v###.###.#.#.#.###.#.#######.#.#.#####v###########.#.###.#########.#.#.#####.#.###.#########.#.#.#.#.#
#.......#...#.#...#...#...#.#...#...#.>.>.#...#...#...#...#...#...#...#.#...#.........###...###.....#...#...#.....#.#...#.###...###...#...#.#
#.###########.#.#.#.#####.#.###.#.#.#.#v#.###.#########.#####.#.#.#####.#.#.#########.#############.#.#.#########.#.###.#.###.#.###########.#
#.....#...###...#...###...#...#.#.#...#.#...#.........#.......#.#.#.....#.#...........#.......#.....#.#.........#.#.#...#.#...#.#...###...#.#
#####.#.#.#############.#####.#.#.#####.###.#########.#########.#.#.#####.#############.#####.#.#####.#########.#.#.#.###.#.###.#.#.###.#.#.#
#.....#.#.............#.......#...#...#...#.#.....#...#...#...#.#.#.....#.....#.....#...#.....#.......#.......#.#...#.....#...#...#.....#...#
#.#####.#############.#############.#.###.#.#.###.#.###.#.#.#.#.#.#####.#####.#.###.#.###.#############.#####.#.#############.###############
#.....#.#...........#.#.....###.....#.....#.#...#...#...#...#...#.....#.###...#...#.#...#.#.....###.....#...#...#.....#.......#.............#
#####.#.#.#########.#.#.###.###.###########.###.#####.###############.#.###v#####.#.###.#.#.###.###.#####.#.#####.###.#.#######.###########.#
#.....#.#...###...#...#...#...#...........#...#.#...#...#...#...#...#...#.>.>.....#.#...#.#...#...#.......#.#...#.#...#.....#...#...###...#.#
#.#####.###.###.#.#######.###.###########.###.#.#.#.###.#.#.#.#.#.#.#####.#v#######.#.###.###.###.#########.#.#.#.#.#######.#.###.#.###.#.#.#
#.......###...#.#...###...#...#...........###...#.#...#...#...#...#.#.....#.#.......#...#...#.#...###.......#.#.#.#.#...###...#...#.....#.#.#
#############.#.###v###.###.###.#################.###.#############.#.#####.#.#########.###.#.#.#####.#######.#.#.#.#.#.#######.#########.#.#
###...#######...###.>...#...###...#.......#...###.#...#.......#...#.#.....#.#...#.......#...#.#.#...#...#...#.#.#.#.#.#.#...###.........#.#.#
###.#.#############v#####.#######.#.#####.#.#.###.#.###.#####.#.#.#.#####.#.###.#.#######.###.#.#.#.###v#.#.#.#.#.#.#.#.#.#.###########.#.#.#
#...#...#.........#.....#...#...#...#...#.#.#...#.#...#.....#...#...#.....#...#.#.....#...#...#.#.#...>.>.#.#.#.#.#.#.#.#.#.###.........#...#
#.#####.#.#######.#####.###.#.#.#####.#.#.#.###.#.###.#####.#########.#######.#.#####.#.###.###.#.#####v###.#.#.#.#.#.#.#.#.###.#############
#.....#.#.......#.......###...#.#.....#.#.#.#...#.#...#...#.#.......#.....#...#...#...#...#...#...###...###...#...#.#.#.#.#...#.............#
#####.#.#######.###############.#.#####.#.#.#.###.#.###.#.#.#.#####.#####.#.#####.#.#####.###.#######.#############.#.#.#.###.#############.#
#.....#...#...#.#.......#...#...#.....#...#.#.#...#...#.#.#...#...#...#...#.#...#.#.#...#.#...###.....###...###.....#.#.#.#...#...#...#...#.#
#.#######.#.#.#.#.#####.#.#.#.#######.#####.#.#.#####.#.#.#####.#.###.#.###.#.#.#.#.#.#.#.#.#####.#######.#.###.#####.#.#.#.###.#.#.#.#v#.#.#
#.#.....#...#...#.#.....#.#...#...###.#...#.#.#...#...#.#.#...#.#.#...#...#...#.#...#.#.#...#...#.......#.#.....#...#.#.#.#...#.#...#.>.#.#.#
#.#.###.#########.#.#####.#####.#.###v#.#.#.#.###.#.###.#.#.#.#.#.#v#####.#####.#####.#.#####.#.#######.#.#######.#.#.#.#.###.#.#######v#.#.#
#.#.#...#...#.....#...#...#...#.#...>.>.#.#.#.#...#.#...#.#.#.#.#.>.>.....#.....#.....#.#.....#.........#.......#.#.#.#.#...#.#.###...#.#...#
#.#.#.###.#.#.#######.#.###.#.#.#####v###.#.#.#.###.#.###.#.#.#.###v#######.#####.#####.#.#####################.#.#.#.#.###.#.#.###.#.#.#####
#...#.....#...#.......#.....#.#.#.....###.#.#.#...#.#.#...#.#.#...#.......#.....#...#...#.#...#...#...#.....###...#.#.#...#.#...#...#.#.....#
###############.#############.#.#.#######.#.#.###.#.#.#.###.#.###.#######.#####.###.#.###.#.#.#.#.#.#.#.###.#######.#.###.#.#####.###.#####.#
#.............#.....#...#...#...#.......#.#.#.#...#...#...#.#.#...#.....#.#...#.....#...#...#.#.#.#.#...#...#.....#...###.#.#...#...#.#...#.#
#.###########.#####.#.#.#.#.###########.#.#.#.#.#########.#.#.#.###.###.#.#.#.#########.#####.#.#.#.#####.###.###.#######.#.#.#.###.#.#.#.#.#
#.#.........#.......#.#.#.#.#...#...#...#.#.#.#...#.......#.#...#...###.#.#.#...........#...#...#...#...#...#...#.###...#...#.#.#...#.#.#...#
#.#.#######.#########.#.#.#.#.#.#.#.#.###.#.#.###.#.#######.#####.#####.#.#.#############.#.#########.#.###.###.#.###.#.#####.#.#.###.#.#####
#...#...#...#...#...#.#.#.#.#.#...#...###...#.....#...#...#.#...#.....#.#.#.#.............#.#.....#...#.....#...#...#.#...#...#.#...#...#...#
#####.#.#.###.#.#.#v#.#.#.#.#v#######################.#.#.#.#.#.#####.#.#.#.#.#############.#.###.#.#########.#####.#.###.#.###.###.#####.#.#
#.....#...#...#...#.>.#...#.>.>.......#...#.........#.#.#...#.#.......#.#.#...#...#.........#...#.#...#.....#.....#.#.#...#...#...#.......#.#
#.#########.#######v#########v#######.#.#.#.#######.#.#.#####.#########.#.#####.#.#.###########.#.###.#.###.#####.#.#.#.#####v###.#########.#
#...........###.....#...#.....#.......#.#.#.......#.#...###...#.....###.#.#.....#...#...#.......#.....#...#.#...#.#.#.#...#.>.###.#.......#.#
###############.#####.#.#.#####.#######.#.#######.#.#######.###.###.###.#.#.#########.#.#.###############.#.#.#.#.#.#.###.#.#v###.#.#####.#.#
#.....#...#.....#.....#.#.....#...#...#.#.#.......#...#...#.....###...#...#.........#.#.#.#.....#.....###.#.#.#.#.#.#.###...#...#.#.....#...#
#.###.#.#.#.#####.#####.#####.###.#.#.#.#.#.#########.#.#.###########.#############.#.#.#.#.###.#.###.###.#.#.#.#.#.#.#########.#.#####.#####
#...#.#.#.#.......#...#.#.....#...#.#.#.#.#.....#.....#.#...#...#.....#...#.........#.#.#...###...#...#...#.#.#.#.#.#.#.........#.#...#.....#
###.#.#.#.#########.#.#.#.#####.###.#.#.#.#####.#.#####.###.#.#.#.#####.#.#v#########.#.###########.###.###.#.#.#.#.#.#.#########.#.#.#####.#
#...#...#.#.....#...#...#.....#...#.#.#.#.#...#.#.#...#.#...#.#.#...#...#.>.>.#...###.#.#...#...###...#...#.#.#.#.#.#.#.....#...#...#.......#
#.#######.#.###.#.###########.###.#.#.#.#.#.#.#.#.#.#.#.#.###.#.###v#.#####v#.#.#.###.#.#.#.#.#.#####v###.#.#.#.#.#.#.#####.#.#.#############
#.......#.#...#.#.......#.....###...#...#.#.#.#.#.#.#.#.#...#.#.#.>.>.###...#...#...#.#...#.#.#.#...>.>...#...#...#...###...#.#...###...#####
#######.#.###.#.#######.#.###############.#.#.#.#.#.#.#.###.#.#.#.#v#####.#########.#.#####.#.#.#.###v###################.###.###.###.#.#####
#.......#.....#.........#.....#...#...###...#.#.#...#...#...#.#...#.....#.......#...#.....#.#.#...###.....#...###...#...#...#.###.....#.....#
#.###########################.#.#.#.#.#######.#.#########.###.#########.#######.#.#######.#.#.###########.#.#.###.#.#.#.###.#.#############.#
#...................#...###...#.#.#.#.#.....#.#.#.........#...#.........#.......#.....#...#.#.#...........#.#.#...#...#.###...#.............#
###################.#.#.###.###.#.#.#.#.###.#.#.#.#########.###.#########.###########.#.###.#.#.###########.#.#.#######.#######.#############
#.........#.........#.#...#...#.#.#.#.#.#...#...#.......#...###.........#.........###...#...#.#...#...#.....#.#.#...#...#.....#.........#...#
#.#######.#.#########.###.###.#.#.#.#.#.#.#############.#.#############.#########.#######.###.###.#.#.#.#####.#.#.#.#.###.###.#########.#.#.#
#.......#...#####...#.#...#...#.#...#.#.#.#...#...#.....#...#...#...#...#.........#.....#.....###...#...#.....#.#.#.#...#...#...........#.#.#
#######.#########.#.#.#.###.###.#####.#.#.#.#.#.#.#.#######.#.#.#.#.#.###.#########.###.#################.#####.#.#.###.###.#############.#.#
#...###.........#.#...#...#.....#...#...#...#...#.#...#...#.#.#...#...###.........#.#...#...###...#...#...#...#.#.#.....###...........###.#.#
#.#.###########.#.#######.#######.#.#############.###.#.#.#.#.###################.#.#.###.#.###.#.#.#.#.###.#.#.#.###################.###.#.#
#.#.............#.......#.....###.#.#.............#...#.#.#.#.............###...#...#...#.#.....#...#.#...#.#...#...#.....#...###.....#...#.#
#.#####################.#####.###.#.#.#############.###.#.#.#############.###.#.#######.#.###########.###.#.#######.#.###.#.#.###v#####.###.#
#...#.......#######...#.#.....#...#.#.............#...#.#...#...........#.#...#...#.....#...........#.#...#.#.......#.#...#.#.#.>.#...#.#...#
###.#.#####.#######.#.#.#.#####.###.#############.###.#.#####.#########.#.#.#####.#.###############.#.#.###.#.#######.#.###.#.#.#v#.#.#.#.###
###...#...#.....#...#.#.#.#...#.#...#...#.........###...#...#.........#...#.....#...###...#...#...#.#.#.....#.....###.#.#...#.#.#.#.#...#...#
#######.#.#####.#.###.#.#.#.#.#.#.###.#.#v###############.#.#########.#########.#######.#.#.#.#.#.#.#.###########v###.#.#.###.#.#.#.#######.#
#...#...#.......#...#.#.#...#.#.#...#.#.>.>.###...#...#...#.###.......###.......#...###.#...#.#.#.#.#.#...#...#.>.>...#.#...#.#.#.#.#.......#
#.#.#.#############.#.#.#####.#.###.#.#####.###.#.#.#.#.###.###.#########.#######.#.###.#####.#.#.#.#.#.#.#.#.#.#######.###.#.#.#.#.#.#######
#.#.#.........#...#.#.#.....#.#.###...#####...#.#.#.#.#...#...#.....#...#.....###.#...#.....#.#.#...#...#.#.#.#.#.......#...#.#.#.#.#.#.....#
#.#.#########.#.#.#.#.#####.#.#.#############.#.#.#.#.###.###.#####.#.#.#####.###.###.#####.#.#.#########.#.#.#.#.#######.###.#.#.#.#.#.###.#
#.#...........#.#...#.......#.#...#...###.....#.#.#.#.###.#...#.....#.#...#...#...#...#...#.#.#.........#.#.#.#.#...#...#.###...#...#...###.#
#.#############.#############.###.#.#.###.#####.#.#.#.###.#.###.#####.###.#.###.###.###.#.#.#.#########.#.#.#.#.###.#.#.#.#################.#
#.#...#...#...#...........###.....#.#.....#...#.#...#.#...#...#.....#.#...#...#...#...#.#.#.#...#...#...#.#.#.#.###.#.#.#.......###.........#
#.#.#.#.#.#.#.###########.#########.#######.#.#.#####.#.#####.#####.#.#.#####v###.###.#.#.#.###.#.#.#.###.#.#.#.###.#.#.#######.###.#########
#.#.#...#.#.#...#.......#.....#.....#.....#.#.#.#.....#...#...###...#.#...#.>.>...#...#.#.#...#.#.#...###...#.#...#...#.#.......#...#.......#
#.#.#####.#.###.#.#####.#####.#.#####.###.#.#.#.#.#######.#.#####v###.###.#.#######.###.#.###.#.#.###########.###.#####.#.#######.###.#####.#
#.#.#.....#...#.#.....#.#...#.#.#...#...#.#.#.#.#.#...#...#.#...>.>.#.###.#.....#...#...#.#...#.#...#.........#...#.....#.......#.#...#.....#
#.#.#.#######.#.#####.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#.###.#.#####.#.###.#####.#.###.###.#.###.###.#.#########.###.###########.#.#.###.#####
#...#.........#.......#...#...#...#.....#...#...#...#...###...#####...###.......#.....###...###.....#...........###.............#...###.....#
###########################################################################################################################################.#
"""

for data in inputs():
    print(*long_walk(data.strip()))
