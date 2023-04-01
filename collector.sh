#!/bin/bash

users_file="user_actions.csv"
init_file="victims.csv"

echo "Date,Time,Username,IP Address,Event" > "$users_file"
echo "Date,Time,Username,External Address,Internal Address,Computername" > "$init_file"

find . -name "*.log" -print0 | while read -d $'\0' file
do
    python3 database-collector.py "$file" >> "$users_file"
    python3 attack-collector.py "$file" >> "$init_file"
done

python3 sorter-by-time.py "$users_file"
python3 gen-graf.py "$users_file" "user_actions.html"
python3 sort-all-values.py "$init_file" "sorted_attack.csv"
