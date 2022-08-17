// Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos
package main

import (
    "fmt"
    "math/rand"

)

func randFloats(min, max float64, n int) []float64 {
    res := make([]float64, n)
    for i := range res {
        res[i] = min + rand.Float64() * (max - min)
    }
    return res
}

func randIntegers(min, max int) int{
	return (rand.Intn(max - min) + min)
}

func main() {

	ages := [] int{}
	heights := [] float64{}
	count := 0

	for i := 0; i < 30; i ++ {
		age := randIntegers(8, 17)
		height := randFloats(1.3, 2, 1)

		ages = append(ages, age)
		heights = append(heights, height...)
	}
	fmt.Println(ages)
	fmt.Println(heights)
	fmt.Println(count)
}