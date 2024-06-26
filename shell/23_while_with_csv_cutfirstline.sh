#!/bin/bash

cat test.csv | awk 'NR!=1 {print}' | while IFS="," read name age company
do
	echo "Name is $name"
done
