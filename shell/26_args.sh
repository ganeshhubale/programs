#!/bin/bash

# Debugging
set -x
# To access the arguments

echo "First argument is $1"
echo "Second arg is $2"

echo "All the arg are - $@"
echo "Number of arguments - $#"

 # for loop to access the values from args

for filename in $@
do
	echo "Copy file here - $filename"
done

