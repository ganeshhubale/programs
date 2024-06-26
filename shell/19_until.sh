#!/bin/bash

a=10

#Run till the condition is failing

until [[ $a -eq 1 ]]
do
	echo "Value of a is $a"
	let a--
done
