#!/bin/bash

# script to show how to use parameter

a=10
name="ganesh"
age=28

echo "My name is ${name} and my age is $age. My jersey number is $a"

name="ramesh"
echo "My name is ${name} and my age is $age. My jersey number is $a"

# store linux cmmands values
HOSTNAME=$(hostname)
echo "$HOSTNAME"
