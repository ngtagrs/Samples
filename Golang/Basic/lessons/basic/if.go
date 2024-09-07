package main

import "fmt"

func by2(num int) string {
	if num%2 == 0 {
		return "ok"
	} else {
		return "no"
	}
}

func main() {
	result := by2(10)
	if result == "ok" {
		fmt.Println("great")
	}

	if result2 := by2(10); result2 == "ok" {
		fmt.Println("great")
	}

	// num := 4
	// if num%2 == 0 {
	// 	fmt.Println("by 2")
	// } else if num%3 == 0 {
	// 	fmt.Println("by 3")
	// } else {
	// 	fmt.Println("dlse")
	// }

	x, y := 10, 10
	if x == 10 && y == 10 {
		fmt.Println("&&")
	}

	if x == 10 || y == 10 {
		fmt.Println("||")
	}
}
