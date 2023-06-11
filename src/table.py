from math import log10
from sys import argv
from heatmap import truncate_krechetov_format

def prepare_table(filename):
    evalues = open(filename, "r")
    elines = evalues.readlines()
    evalues.close()
    

    print('%20s %10s %10s %10s'% ("Organism", "Protein", "E-value", "-log((e-value)"))
    for line in elines:
        _split = line.split()
        evalue = _split[-1]
        org_prot = _split[0]

        org = org_prot.split("-")[1]
        prot = org_prot.split("-")[-1]
        org = truncate_krechetov_format(org)
        prot = truncate_krechetov_format(prot)

        if evalue=="0.0":
            evalue = '1.0e-300'
        evalue = float(evalue)
        log_evalue = -log10(evalue)
        print('%20s %10s %10s %10s'% (org, prot, evalue, log_evalue))

    return 0

prepare_table(argv[1])
