package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main(){
	numbers := []int {}
	for i:= 0; i < 5; i++ {
		numbers = append(numbers, rand.Intn(8))
	}
sort.Ints(numbers)
fmt.Println(numbers)
}