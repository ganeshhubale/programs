#!/bin/bash

echo "Please select the option"
echo "a for date"
echo "b for list of scripts"
echo "c for current location"

read choice

case $choice in
	a)
		echo "Today is"
		date;;
	b)ls;;
	c)pwd;;
	*) echo "invalid option"
esac 
