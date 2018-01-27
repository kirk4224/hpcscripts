#!/usr/bin/python
from math import sqrt, floor
from texttable import Texttable

### Inputs
print "====== HPL calculator ======"
print "Return suggested HPL benchmark parameters according to system specifications."
print "Please type in your specifications."
num_of_nodes = int(raw_input("1/5.Number of Nodes(e.g.30):") or 30)
# print "Number of Nodes: " + str(num_of_nodes)
core_per_node = int(raw_input("2/5.Cores per Node(e.g.24):") or 24)
# print "Cores per Node: " + str(core_per_node)
spd_per_core = float(raw_input("3/5.Speed Per Core(GHz)(e.g.2.3):") or 2.3)
spd_per_core = 1024 * spd_per_core
# print "Speed Per Core: " + str(spd_per_core)
mem_per_node = int(raw_input("4/5.Memory per Node(GB)(e.g.64):") or 64)
# print "Memory per Node: " + str(mem_per_node)
ops_per_cycle = int(raw_input("5/5.Operations per Cycle(e.g.16):") or 16)
# print "Operations per Cycle: " + str(ops_per_cycle)
# part 1 total cores
print "########## Results ##############"
print "### Part I"
total_cores = num_of_nodes * core_per_node
total_mem = num_of_nodes * mem_per_node
print "Total Number of Cores: " + str(total_cores)
print "Total Memory(GB): " + str(total_mem)
# part 2 theoretical peak performance
print "### Part II"
peakperf = total_cores * spd_per_core / 1024 * ops_per_cycle
print "Peak Performance(GFlops): "
percentage = (range(70, 101, 2))
performance = []
for p in percentage:
    performance.append(int(p * peakperf / 100))
table = Texttable(max_width=200)
percentage = (map(lambda x: str(x) + '%', percentage))
table.add_rows([percentage, performance])
print table.draw()
# part 3 P & Q
print "### Part III"
P = 1
Q = total_cores / P
print "Possible P & Q combinations:"
while P < Q:
    print "P=%s x Q=%s" % (P, Q)
    P = P * 2
    Q = total_cores / P
# part 4 N & NB
print "### Part IV"
table = Texttable(max_width=200)
tablevalue = []
NB = list(range(96, 257, 8))
mem_percentage = list(range(80, 101, 2))
N = list()
print "Range of NB:"
print NB
print "Range of Memory Percentage(%):"
print mem_percentage
print "Suggested Parameter for HPL benchmark:"
tablevalue.append(["Memory\\NB"] + NB)
for mem in mem_percentage:
    N = []
    for nb in NB:
        n = floor(sqrt(total_mem * 1024 * 1024 * 1024 / 8) * mem / 100)
        n = floor(n / nb)
        n = int(n * nb)
        N.append(n)
    tablevalue.append([str(mem) + "%"] + N)
table.add_rows(tablevalue)
print table.draw()
