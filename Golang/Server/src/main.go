package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
)

type Position struct {
	id    int
	name  string
	value float64
}

func load_data(file_path string) []Position {
	file, err := os.Open(file_path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	r := csv.NewReader(file)
	rows, err := r.ReadAll() // csvを一度に全て読み込む
	if err != nil {
		log.Fatal(err)
	}

	positions := make([]Position, 0)
	for _, row := range rows {
		position := Position{}
		position.id, _ = strconv.Atoi(row[0])
		position.name = row[1]
		position.value, _ = strconv.ParseFloat(row[2], 64)
		positions = append(positions, position)
	}

	return positions
}

func data_handler(w http.ResponseWriter, r *http.Request) {
	positions := load_data("./data/test.csv")
	sm := 0
	for _, position := range positions {
		sm += int(position.value)
	}
	_, err := w.Write([]byte(strconv.Itoa(sm)))
	if err != nil {
		log.Fatal(err)
	}
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	hello := []byte("Hello World!!!")
	_, err := w.Write(hello)
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	http.HandleFunc("/hello", helloHandler)
	http.HandleFunc("/positions", data_handler)
	fmt.Println("Server Start Up........")
	log.Fatal(http.ListenAndServe("localhost:8080", nil))
}
