package main

import "fmt"

func f1(params ...int) {
	fmt.Println(len(params), params)
	for _, param := range params {
		fmt.Println(param)
	}
}

func main() {
	f1(10, 20)
	f1(10, 20, 30)

	s := []int{1, 2, 3}
	fmt.Println(s)

	f1(s...)
}
