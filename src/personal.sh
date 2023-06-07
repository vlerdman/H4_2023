#!/bin/bash
ls /mnt/storage/project_2023/proteomes/ | grep "faa$" | xargs -I {} -P 11 blastp -query gene.fa  -db /mnt/storage/project_2023/proteomes/{} -out queried-{}  -outfmt 7
ls *.faa | xargs -I {} -P 1 sh -c "echo -n {}' e-value: '; grep -v '#' {} | LC_ALL=C sort -k 11 -g | head -n 1" | awk '{print $1, $2, $13}' | sed "s/.faa/-$GENE_NAME.faa/g" | tee personal-e.txt
ls *.faa | xargs -I {} -P 1 sh -c "echo -n {}' hits: '; grep hits {}" | awk '{print $1, $2,$4}' | sed "s/.faa/-$GENE_NAME.faa/g" | tee personal-h.txt


