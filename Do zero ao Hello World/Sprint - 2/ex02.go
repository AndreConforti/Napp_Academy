package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main(){
	numbers := []int {}
	for i:= 0; i < 10; i++ {
		numbers = append(numbers, rand.Intn(9))
	}
sort.Ints(numbers)
fmt.Println(numbers)
}