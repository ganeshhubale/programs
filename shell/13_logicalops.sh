#!/bin/bash
# AND operator

print -n "what is your age?"
read age

print -n "your country?"
read country

if [[ $age -ge 18 ]] && [[ $country == "India" ]]
then
	echo "You can vote"
else
	echo "you can not vote"
fi
