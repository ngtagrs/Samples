package main

import "fmt"

func main() {
	m := map[string]int{
		"Mike": 20, 
		"Nancy": 24, 
		"Messi": 30
	}
	fmt.Printf("%T %v\n", m, m)
}
