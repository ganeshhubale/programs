package main

import (
	"fmt"
)

// can't redeclare variable but can do shadowing
// all variables must be used

// visibility
//1. lower case first lterr for package scope
//2. upper case first letter to export
// 3. no private scope

var k int = 454 

// Concept - 'shadowing' k variable. It gives precendnce to func scope k var
// dont just declare variable. you will get compile time error.
// kk :=5 ==> ./variable.go:12:1: syntax error: non-declaration statement outside function body

func main(){
	k := 33
	fmt.Printf("%v, %T", k,k)
	var i int
	var j int = 45
	fmt.Println()
	fmt.Println(i, j)
}
