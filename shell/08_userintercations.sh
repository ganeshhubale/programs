#!/bin/zsh

# read userName

# echo "You name is $userName"

# echo "What is your name - "


# This is not supported in zsh

# Read and echo together

#read -p "Your name -> " name
#echo "Your name is $name"
#---

# in zsh you can do this
print -n "your name -> "
read name
echo "your name is $name"
