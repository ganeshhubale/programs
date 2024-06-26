#!/bin/bash

#if user not giving arguments then no use of code lines.hence exit the script if no arg

if [[ $# -eq 0 ]]
then
	echo "Please provide the arguments"
	exit 1
fi

echo "First argument is $1"
echo "secod arg is $2"

echo "All the arguments are - $@"
echo "Number of arguments are - $#"

