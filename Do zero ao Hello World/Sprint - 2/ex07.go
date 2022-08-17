// Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

package main

import (
	"fmt"
	"math/rand"
)

func main() {

	numbers := [] int{}
	sum := 0
	multi := 1

    for i := 0; i < 5; i++ {
		number := rand.Intn(9)
		numbers = append(numbers, number)
		sum += number
		multi *= number
	}

	fmt.Println("Números: ", numbers)
	fmt.Println("Soma   : ", sum)
	fmt.Println("Multip.: ", multi)
}
