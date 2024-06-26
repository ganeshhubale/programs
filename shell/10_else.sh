#!/bin/zsh

print -n "Enter marks -- "
read marks

if [[ $marks -gt 35 ]]
then 	
	echo "you are pass"
else
	echo " you are fail"
fi

