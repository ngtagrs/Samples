package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Record struct {
	Col1 string
	Col2 string
	Col3 string
}

func main() {
	// Open the file
	file, err := os.Open("test.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read the file line by line
	scanner := bufio.NewScanner(file)

	// Skip the header line
	scanner.Scan()

	var records []Record
	for scanner.Scan() {
		// Split each line by the delimiter '|'
		line := scanner.Text()
		fields := strings.Split(line, "|")

		// Create a new Record and append to the slice
		record := Record{
			Col1: fields[0],
			Col2: fields[1],
			Col3: fields[2],
		}
		records = append(records, record)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	// Print out the records
	for _, record := range records {
		fmt.Printf("Col1: %s, Col2: %s, Col3: %s\n", record.Col1, record.Col2, record.Col3)
	}
}
