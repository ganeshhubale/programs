#!/bin/zsh

# Array

myArray=( 1 2 3.5 4 "ganesh" ram hello 33, 44, 55, 66)

echo " All the values in array -> ${myArray[*]}"
echo "Value in array - ${myArray[1]}"

echo "length of the array -> ${#myArray[*]}"

# all the values after first position
echo "Value after first position ${myArray[*]:1}"

# range of values means index 3 se next 2 values print 
echo "values from 3 to 5 -> ${myArray[*]:3:2}"

# update the areayw tih new values

myArray+=( New 30 40 )

echo "my new array ->  ${myArray[*]}"
