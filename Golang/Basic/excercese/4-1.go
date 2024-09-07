package main

import (
	"fmt"
	"math"
)

func main() {
	ans := math.MaxInt
	l := []int{100, 300, 23, 11, 23, 2, 4, 6, 4}
	for _, v := range l {
		if ans > v {
			ans = v
		}
	}
	fmt.Println(ans)
}
