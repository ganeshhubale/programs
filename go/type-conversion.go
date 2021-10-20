package main

import ( "fmt" 
	"strconv"
)

// Type conversion
//1. destinationType(variable)
//2. use strconv package for strings
func main() {
	i := 42
	var j string
	j = strconv.Itoa(i)
	fmt.Printf("%v, %T\n", j, j)

	var x int
	var y float64 = 45.666
	x = int(y)
	fmt.Printf("%v, %T\n", x,x)
}
