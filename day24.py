# For example, suppose you had the following components:

# 0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10
# With them, you could make the following valid bridges:

# 0/1
# 0/1--10/1
# 0/1--10/1--9/10
# 0/2
# 0/2--2/3
# 0/2--2/3--3/4
# 0/2--2/3--3/5
# 0/2--2/2
# 0/2--2/2--2/3
# 0/2--2/2--2/3--3/4
# 0/2--2/2--2/3--3/5
# (Note how, as shown by 10/1, order of ports within a component doesn't matter. However, you may only use each port on a component once.)

# Of these bridges, the strongest one is 0/1--10/1--9/10
# it has a strength of 0+1 + 1+10 + 10+9 = 31.
