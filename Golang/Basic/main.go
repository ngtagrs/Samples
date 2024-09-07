package main

import (
	"basic/mylib"
	"basic/mylib/under"
	"fmt"
)

func main() {
	s := []int{1, 2, 3, 4, 5}
	fmt.Println(mylib.Average(s))
	under.Hello()
}
