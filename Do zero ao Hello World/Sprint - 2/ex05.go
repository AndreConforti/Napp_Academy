// Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {

	numbers := [] int{}
	even := [] int{}
	odd := [] int{}

    for i := 0; i < 20; i++ {
		number:= rand.Intn(10)
		numbers = append(numbers, number)
		if number % 2 == 0{
			even = append(even, number)
		} else {
			odd = append(odd, number)
		}
	}

	sort.Ints(numbers)
	sort.Ints(even)
	sort.Ints(odd)

	fmt.Println("Números: ", numbers)
	fmt.Println("Pares  : ", even)
	fmt.Println("Ímpares: ", odd)
}
