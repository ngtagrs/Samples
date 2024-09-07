package main

import "fmt"

func main() {
	m := map[string]int{
		"apple":  200,
		"banana": 300,
		"grapes": 150,
		"orange": 80,
		"papaya": 500,
		"kiwi":   90,
	}

	ans := 0
	for _, v := range m {
		ans += v
	}
	fmt.Println(ans)
}
