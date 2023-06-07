#!/bin/bash
cp /mnt/storage/project_2023/histones/* .
ls *.fasta | xargs -I {} -P 1 sh -c "tr -d '\r' < {} | tr -d '\n' | sed 's/>/\n>/g' | sort -R  | head -n1 | awk -F ']' '{print $3}' > {}-random.faa"
ls *.faa | xargs -I {} -P 1 awk -F "]" '{print $NF > $1}' {}
for f in *\ *; do mv "$f" "${f// /_}"; done
for f in $(ls); do mv "$f" "${f//>/_}" 2>/dev/null; done
ls | grep organism | xargs -I {} -P 44 sh -c 'for i in $(cd /mnt/storage/project_2023/proteomes && ls -1 *.faa && cd - > /dev/null); do blastp -query "{}"  -db /mnt/storage/project_2023/proteomes/$i -out "queried-$i-{}"  -outfmt 7; done'
total=$(ls | grep organism | grep queried |  wc -l)
if [[ "$total" != 44 ]]; then
  echo "Remove everyting generated ny this and start over. Random does not favor you"
  exit 1
fi
ls | grep organism | grep queried | xargs -I {} -P 1 sh -c "echo -n {}' e-value: '; grep -v '#' '{}' | LC_ALL=C sort -k 11 -g | head -n 1" | awk '{print $1, $2, $13}' | tee random.txt


