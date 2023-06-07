#!/bin/python3
import sys
import pandas as pd
from math import log10
import seaborn as sns
import matplotlib.pyplot as plt


def truncate_krechetov_format(line):
    if "[" in line:
        return line[:line.index("[")]
    
    if line.count(".") > 1 or "faa" in line:
        return line[:line.rindex(".")]

    return line
    
def prepare_dataset(filename):
    evalues = open(filename, "r")
    elines = evalues.readlines()
    evalues.close()

    dataframe = pd.DataFrame(columns=["Organism", "Protein", "-log(e-value)"])
    for line in elines:
        _split = line.split()
        hits = _split[-1]
        org_prot = _split[0]

        org = org_prot.split("-")[1]
        prot = org_prot.split("-")[-1]
        org = truncate_krechetov_format(org)
        prot = truncate_krechetov_format(prot)

        #if evalue=="0.0":
        #   evalue = '1.0e-300'
        #log_evalue = -log10(float(evalue))
        dataframe.loc[len(dataframe.index)] = [org, prot, float(hits)]

    pivot = pd.pivot_table(dataframe, values="-log(e-value)", index="Protein", columns="Organism")
    column_order = ['human', 'mouse', 'zebrafish', 'drosophila', 'c.elegans', 'ciliate', 'yeast', 'methanocaldococcus', 'thermococcus', 'e.coli', 'tuberculosis']
    pivot = pivot.reindex(column_order, axis=1)

    return pivot

def create_heatmap(dataframe):
    fig, ax = plt.subplots(figsize=(14,14)) 
    #cmap = sns.color_palette("mako", reverse=True)
    
    hmap = sns.heatmap(data=dataframe, ax=ax, cmap="mako_r")
    fig = hmap.get_figure()
    fig.savefig("out-h.jpg", format="jpg", dpi=500) 

df = prepare_dataset(sys.argv[1])
create_heatmap(df)
print(df)
