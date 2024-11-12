"""
Author: Keerthik Muruganandam
Topic: Rosalind.info Bioinformatics Stronghold Solutions
Language: Python
"""
################ PROBLEM SOLNS ###################
from scipy.special import comb
from collections import defaultdict
import math

def subs(s, t):
    loc = []
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            loc.append(i)
    for j in loc:
        print(j, end=" ")

def prot(s): # NEED TO COMPLETE THE CODON TABLE
    codontab = {
        "UUU": "F",
        "UUC": "F",
        "UUA": "L",
        "UUG": "L",
        "UCU": "S",
        "UCC": "S",
        "UCA": "S",
        "UCG": "S",
        "UAU": "Y",
        "UAC": "Y",
        "UAA": "*",
        "UAG": "*",
        "UGU": "C",
        "UGC": "C",
        "UGA": "*",
        "UGG": "W",
        "CUU": "L",
        "CUC": "L",
        "CUA":"L",
        "CUG":"L",
        "CCU": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAU": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGU": "R",
        "CGC": "R",
        "CGG": "R",
        "CGA": "R",
        "AUU": "I",
        "AUC": "I",
        "AUA": "I",
        "AUG": "M",
        "ACU": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAU": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGU": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GUU": "V",
        "GUG": "V",
        "GUA": "V",
        "GUC": "V",
        "GCU": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAU": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGU": "G",
        "GGG": "G",
        "GGC": "G",
        "GGA": "G"
    }
    ls = [s[i:i+3] for i in range(0, len(s), 3)]
    o = ""
    for i in ls:
        if codontab[i] == "*":
            break
        else:
            o = o + codontab[i]

    return o

def gc():
    f = open("datasets/rosalind_gc.txt", "r")
    lines = []
    running_string = ""
    for line in f:
        if line[0] == ">":
            if running_string != "":
                lines.append(running_string)
            lines.append(line.strip())
            running_string = ""
        else:
            running_string += line.strip()
    lines.append(running_string)

    max_gc = 0
    max_str = ""

    for i in range(0, len(lines), 2):
        gc_count = 0
        length = len(lines[i+1])
        for j in lines[i+1]:
            if j == "G" or j == "C":
                gc_count += 1

        if gc_count / length > max_gc:
            max_gc = gc_count / length
            max_str = lines[i]

    o = open("outputs/rosalind_gc.txt", "w")
    o.write(max_str[1:]+ '\n')
    o.write(str(max_gc*100))
    o.close()

def fib():
    f, o = file_open("fib")
    nk = [int(i) for i in parse(f)]
    memo = [0] * nk[0]
    memo[0] = 1
    memo[1] = 1
    for i in range(nk[0]):
        if i == 0 or i == 1:
            pass
        else:
            memo[i] = memo[i-1] + nk[1]*memo[i-2]

    o.write(str(memo[-1]))
    o.close()

def fibd():
    f, o = file_open("fibd")
    nm = [int(i) for i in parse(f)]

    babies = [0] * nm[0]
    adults = [0] * nm[0]

    for i in range(nm[0]):
        if i == 0:
            babies[i] = 1
        elif i == 1:
            adults[i] = 1
        else:
            adults[i] = babies[i-1] + adults[i-1] - babies[i-nm[1]]
            babies[i] = adults[i-1]

    o.write(str(adults[-1]+babies[-1]))
    o.close()

def prtm():
    f, o = file_open("prtm")
    mtable = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }
    prt = f.readline().strip("\n")
    m = 0.0
    for i in prt:
        m += mtable[i]

    o.write(str(m))
    o.close()

def iprb():
    f, o = file_open("iprb")
    pop = [int(i) for i in parse(f)]
    total_pop =pop[0] + pop[1] + pop[2]
    combos = comb(total_pop, 2)
    valid_combos = comb(pop[0], 2) + pop[0]*pop[1] + pop[0]*pop[2] + 0.5*pop[1]*pop[2] + 0.75*comb(pop[1], 2)
    o.write(str(valid_combos/combos))
    o.close()

def iev():
    f, o = file_open("iev")
    pop = [int(i) for i in parse(f)]
    ex = 0

    for i in range(6):
        match i:
            case 0:
                prob = 1
            case 1:
                prob = 1
            case 2:
                prob = 1
            case 3:
                prob = 0.75
            case 4:
                prob = 0.5
            case 5:
                prob = 0
            case _:
                prob = 0
        ex += 2*prob*pop[i]

    o.write(str(ex))
    o.close()

def mrna():
    codontab = {
        "F": 2,
        "L": 2,
        "S": 4,
        "Y": 2,
        "C": 2,
        "W": 1,
        "L": 4,
        "P": 4,
        "H": 2,
        "Q": 2,
        "R": 4,
        "I": 3,
        "M": 1,
        "T": 4,
        "N": 2,
        "K": 2,
        "S": 2,
        "R": 2,
        "V": 4,
        "A": 4,
        "D": 2,
        "E": 2,
        "G": 4
    }

    f, o = file_open("mrna")
    protein = f.readline().strip("\n")
    combos = 3

    for i in protein:
        combos = (combos * codontab[i])

    o.write(str(combos % 1000000))
    o.close()

def grph():
    f, o = file_open("grph")
    lines = []

    for line in f.readlines():
        if line[0] == ">":
            lines.append(line.strip("\n").strip(">"))
            lines.append("")
        else:
            lines[-1] += line.strip("\n")

    for seq in range(0, len(lines), 2):
        for pair in range(0, len(lines), 2):
            if seq != pair:
                if lines[seq+1][-3:] == lines[pair+1][0:3]:
                    o.write(lines[seq]+" "+lines[pair]+"\n")

    o.close()

def cons():
    # Setting up I/O & data handling
    f, o = file_open("cons")
    names, seqs = fasta(f, "two")
    cons = ""
    nums = defaultdict(list)

    # Processing data
    for i in range(len(seqs[0])):
        a, c, g, t = 0, 0, 0, 0
        for seq in seqs:
            if seq[i] == "A":
                a += 1
            elif seq[i] == "C":
                c += 1
            elif seq[i] == "G":
                g += 1
            else:
                t += 1

        # Creating consensus string
        common = max(a, c, g, t)
        if a == common:
            cons += "A"
        elif c == common:
            cons += "C"
        elif g == common:
            cons += "G"
        elif t == common:
            cons += "T"
        # Creating profile matrix
        nums['A'].append(a)
        nums['C'].append(c)
        nums['G'].append(g)
        nums['T'].append(t)

    # Writing output
    o.write(cons+"\n")
    for key, value in nums.items():
        o.write(key + ":")
        for i in value:
            o.write(" " + str(i))
        o.write("\n")

def perm(**kwargs):
    f, o = file_open("perm")
    n = int(parse(f)[0])
    ls = kwargs.get("ls", [i+1 for i in range(n)])

    for i in range(n):


    return perm(ls = ls.remove(c))

################ FILE HELPER ###################
def file_open(name):
        return open("datasets/rosalind_"+name+".txt", "r"), open("outputs/rosalind_"+name+".txt", "w")
def parse(f):
    return f.readline().strip("\n").split()
def fasta(f, type):
    match type:
        case "one":
            ls = []
            for line in f.readlines():
                if line[0] == ">":
                    ls.append(line.strip("\n").strip(">"))
                    ls.append("")
                else:
                    ls[-1] += line.strip("\n")
            return ls
        case "two":
            ls1, ls2 = [], []
            for line in f.readlines():
                if line[0] == ">":
                    ls1.append(line.strip("\n").strip(">"))
                    ls2.append("")
                else:
                    ls2[-1] += line.strip("\n")
            return ls1, ls2
        case "dict":
            dict = {}

    return []

################ MAIN RUN ###################
if __name__ == '__main__':
    # perm()
    # subs(s, t)
    # prot(s)
    # gc()
    # fib()
    # fibd()
    # prtm()
    # iprb()
    # iev()
    # mrna()
    # grph()
    cons()
