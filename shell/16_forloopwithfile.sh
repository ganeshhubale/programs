#!/bin/bash

# Getting values from a file names.txt

FILE="/Users/ganesh/work/learning/shellscripting/myscripts/names.txt"

for name in $(cat $FILE)
do
	echo "Name is $name"
done

