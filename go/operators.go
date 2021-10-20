package main

import(
	"fmt"
)

func main(){
	a := 10 // 1010
	b := 3 // 0011

	fmt.Println(a & b) // 0010
	fmt.Println(a | b) // 1011
	fmt.Println(a ^ b) // 1001
	fmt.Println(a &^ b) // 0100

	// bitshifting
	m := 8 // 2^3

	fmt.Println(m<<3) // 2^3 * 2^3 = 2^6 -->  shift left

	fmt.Println(m>>3) // 2^3 / 2^3 = 2^0 --> sift right
}