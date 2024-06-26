#!/bin/zsh

myVar="I am ganesh and I am from IT"

myVarLength=${#myVar}
echo "Length of string -> $myVarLength"

<< comment
 This is not supported in zsh
 echo "Upper case ---- ${myVar^^}"
 echo "Lower case ---- ${myVar,,}"
comment

# for zsh lower and upper case
typeset -u upperCaseVar=$myVar
typeset -l lowerCaseVar=$myVar

echo "Upper case ---- $upperCaseVar"
echo "Lower case ---- $lowerCaseVar"

# to replace a string

newVar=${myVar/ganesh/priya}
echo "new Var --- $newVar"

# To slice a string

echo "after slice --- ${newVar:4:6}"
