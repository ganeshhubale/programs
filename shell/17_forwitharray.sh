#!/bin/zsh

myArray=( 1 2 3 4 hello hi )
length=${#myArray[*]}

# in zsh indexing starts from 1 in array
for (( i=1;i<=$length;i++ ))
do
	echo "Value of array is ${myArray[$i]}"
done
