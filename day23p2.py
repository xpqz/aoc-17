"""
Part 2: run to completion for a = 1.

Code consists of a set of crude, deeply nested loops. We can optimised
some of them.

{{ init a = 1 }}

0:  set b 79
1:  set c b
2:  jnz a 2         IF a != 0: GOTO L1
3:  jnz 1 5         GOTO L2
4:  mul b 100       L1
5:  sub b -100000
6:  set c b
7:  sub c -17000
8:  set f 1         L2
9:  set d 2
10: set e 2         L5

11: set g d         L4
12: mul g e
13: sub g b
14: jnz g 2         IF g != 0: GOTO L3
15: set f 0
16: sub e -1        L3
17: set g e
18: sub g b
19: jnz g -8        IF g != 0: GOTO L4

20: sub d -1
21: set g d
22: sub g b         L6
23: jnz g -13       IF g != 0: GOTO L5
24: jnz f 2         IF f != 0: GOTO L6
25: sub h -1
26: set g b         L7
27: sub g c
28: jnz g 2         IF g != 0: GOTO L8
29: jnz 1 3         GOTO END
30: sub b -17       L8
31: jnz 1 -23       GOTO L2

END

The innermost (L4) loop (addresses 11-19) can be directly
translated to Python as:

def L4(regs):
    while True:
        regs["g"] = regs["d"]
        regs["g"] *= regs["e"]
        regs["g"] -= regs["b"]

        if regs["g"] == 0:
            regs["f"] = 0
        regs["e"] += 1

        regs["g"] = regs["e"]
        regs["g"] -= regs["b"]

        if regs["g"] == 0:
            break

where only g, f and e changes. The g value is always 0
after the loop terminates. The value of e is always b.
The f value is either unchanged, or set to 0.

If we refactor the code a bit further, we get to

def L4(regs):
    while True:
        regs["g"] = regs["d"] * regs["e"] - regs["b"]

        if regs["g"] == 0:
            regs["f"] = 0

        regs["e"] += 1

        regs["g"] = regs["e"] - regs["b"]

        if regs["g"] == 0:
            break

which means that f is 0 if and only if d*e = b, or in other
words if b/d is an integer in the range [1, b). The whole L4
loop can be removed and replaced with:

def L4(regs):
    if regs["b"] % regs["d"] == 0:
        v = regs["b"] // regs["d"]
        if v >= regs["e"] and v < regs["b"]:
            regs["f"] = 0

    regs["e"] = regs["b"]
    regs["g"] = 0

We could optimise out the L5 loop the same way, but with L4
removed the program runs in a few minutes.
"""

regs = {}

regs["b"] = 79
regs["c"] = regs["b"]
regs["b"] *= 100
regs["b"] -= - 100000
regs["c"] = regs["b"]
regs["c"] -= - 17000
regs["h"] = 0
regs["d"] = 0
regs["f"] = 0
regs["e"] = 0
regs["g"] = 0

while True:
    regs["f"] = 1
    regs["d"] = 2

    while True:
        regs["e"] = 2

        # L4 loop, reduced
        if regs["b"] % regs["d"] == 0:
            v = regs["b"] // regs["d"]
            if v >= regs["e"] and v < regs["b"]:
                regs["f"] = 0
        # end L4 loop

        regs["e"] = regs["b"]
        regs["g"] = 0

        regs["d"] += 1
        regs["g"] = regs["d"]
        regs["g"] -= regs["b"]

        if regs["g"] == 0:
            break

    if regs["f"] == 0:
        regs["h"] += 1
    regs["g"] = regs["b"]
    regs["g"] -= regs["c"]

    if regs["g"] == 0:
        break

    regs["b"] -= -17

print(regs["h"])
