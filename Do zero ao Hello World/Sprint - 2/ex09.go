// Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

package main

import (
	"fmt"
	"math/rand"
)

func main() {

	sum := 0
	numbers := [] int{}

    for i := 0; i < 10; i++ {
		number := rand.Intn(8)
		fmt.Print(number)
		number *= number
		numbers = append(numbers, number)
		sum += number
	}
	fmt.Println("Números: ", numbers)
	fmt.Println("Soma   : ", sum)
}
