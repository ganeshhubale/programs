#!/bin/bash

print -n "what are your marks?"
read marks

if [[ $marks -ge 75 ]]
then
	echo "first class"
elif [[ $marks -gt 35 ]]
then
	echo "pass"
else
	echo "fail"
fi
