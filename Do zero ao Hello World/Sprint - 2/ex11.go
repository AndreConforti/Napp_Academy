// Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
package main

import (
	"fmt"
	"math/rand"
)

func main() {

	vectorA := [] int{}
	vectorB := [] int{}
	vectorC := [] int{}
	vectorD := [] int{}

    for i := 0; i < 10; i++ {
		numberA := rand.Intn(10)
		vectorA = append(vectorA, numberA)
		vectorD = append(vectorD, numberA)
		numberB := rand.Intn(10)
		vectorB = append(vectorB, numberB)
		vectorD = append(vectorD, numberB)
		numberC := rand.Intn(10)
		vectorC = append(vectorC, numberC)
		vectorD = append(vectorD, numberC)		
	}
	fmt.Println(vectorA)
	fmt.Println(vectorB)
	fmt.Println(vectorC)
	fmt.Println(vectorD)
}
