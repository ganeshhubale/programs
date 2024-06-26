#!/bin/bash

while IFS="," read name age company
do
	echo "Name is $name"
	echo "Age is $age"
	echo "Company is $company"
done < test.csv
