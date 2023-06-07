#!/bin/bash
pip install pandas seaborn matplotlib
cat personal-e.txt random.txt > full.txt
./heatmap.py full.txt

