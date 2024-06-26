#!/bin/bash

# cond1 && cond2 || cond3

print -n "what is your age -"
read age

[[ $age -ge 18 ]] && echo "Adult" || echo "Minor"
