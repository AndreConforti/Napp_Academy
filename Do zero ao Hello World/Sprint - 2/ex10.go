// Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

package main

import (
	"fmt"
	"math/rand"
)

func main() {

	vectorA := [] int{}
	vectorB := [] int{}
	vectorC := [] int{}

    for i := 0; i < 10; i++ {
		numberA := rand.Intn(10)
		vectorA = append(vectorA, numberA)
		vectorC = append(vectorC, numberA)
		numberB := rand.Intn(10)
		vectorB = append(vectorB, numberB)
		vectorC = append(vectorC, numberB)		
	}
	fmt.Println(vectorA)
	fmt.Println(vectorB)
	fmt.Println(vectorC)
}
