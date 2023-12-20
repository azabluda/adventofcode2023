# https://adventofcode.com/2023/day/20
# Day 20: Pulse Propagation

from itertools import count
from math import lcm

def pulse_propagation(data):
    res = [0, 0]
    nexts, fs, cs, types = {}, {}, {}, {}
    for line in data.split('\n'):
        module, dests = line.split(' -> ')
        nexts[module[1:]] = dests.split(', ')
        types[module[1:]] = module[0]
    for input, modules in nexts.items():
        for module in modules:
            cs.setdefault(module, {})
            cs[module][input] = False
    part2 = {m:0 for m in ['sg', 'lm', 'dh', 'db']} # observation!
    for presses in count(1):
        res[False] += 1
        cur = [('button', 'roadcaster', False)]
        while cur:
            cur, pre = [], cur
            for input, module, signal in pre:
                send = None
                if signal and not part2.get(input, -1):
                    part2[input] = presses
                    if all(part2.values()):
                        yield lcm(*part2.values()) # part 2
                        return
                if module not in types:
                    continue
                if types[module] == 'b':
                    send = False
                if types[module] == '%' and not signal:
                    fs[module] = not fs.get(module, False)
                    send = fs[module]
                if types[module] == '&':
                    cs[module][input] = signal
                    send = not all(cs[module].values())
                if send != None:
                    cur += ((module, nxt, send) for nxt in nexts[module])
                    res[send] += len(nexts[module])
        if presses == 1000:
            yield res[0] * res[1] # part 1
            if 'rx' not in cs: return


def inputs():

    yield r"""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

    yield r"""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

    yield r"""
%sf -> pz, gj
%zh -> bc, st
%hk -> bc
&bc -> mn, zl, xb, mm, dh, hv, gz
%st -> bc, mm
%gv -> xf, qq
%hv -> xb
%nd -> gj, tr
%zx -> bx, ms
%sc -> ks, gj
%gr -> hn
%pl -> qq, rh
%qc -> sf, gj
%xr -> sc, gj
%zl -> zh
&gj -> ks, ld, sg, xr
%dg -> ll, bx
%nf -> bc, tg
%lz -> cv, qq
%nq -> dg, bx
%rh -> qq, lp
%xf -> qq, qj
%ms -> bx, xh
%mn -> bc, hv
&jm -> rx
%xh -> vt, bx
%pz -> gj
%vq -> bt
%gz -> nf
%bt -> gr
&sg -> jm
%fr -> bx, tb
&lm -> jm
%ld -> cl
%cv -> vq
%cl -> gj, jf
%tr -> gj, sz
%sz -> gj, ld
%dx -> hk, bc
%lr -> bx, fr
%vt -> lr, bx
%ll -> zx
broadcaster -> pl, xr, mn, xc
%lp -> lz
%mm -> gz
&qq -> lm, gr, cv, vq, lp, pl, bt
%xb -> zl
&bx -> ll, xc, db
%tb -> bx
%hn -> gv, qq
%jf -> qc, gj
%qj -> qq
%xc -> bx, pm
%tg -> bc, dx
&dh -> jm
%ks -> nd
&db -> jm
%pm -> bx, nq
"""

for data in inputs():
    print(*pulse_propagation(data.strip()))
