#!/bin/bash

# $? is to check status. Anything other than 0 is bad status

print "Which site you want to check?"
read site

ping -c 1 $site &> /dev/null

# sleep 5s
echo $?
if [[ $? -eq 0 ]]
then
	echo "Successfully connected to the $site"
else
	echo "Unable to connect $site"
fi
