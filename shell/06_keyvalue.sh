#!/bin/zsh

# how to store key valuen in array

declare -A myArray

myArray=( [name]=Priya [age]=34 [marks]=99 )

echo "Name is ${myArray[name]}"
