package main

import "fmt"

func main() {
	// var p = new(int)
	// fmt.Println(*p)
	// *p++
	// fmt.Println(*p)

	// var p2 *int
	// fmt.Println(p2)

	s := make([]int, 0)
	fmt.Printf("%T\n", s)

	m := make(map[string]int)
	fmt.Printf("%T\n", m)

	var p = new(int)
	fmt.Printf("%T\n", p)
}
