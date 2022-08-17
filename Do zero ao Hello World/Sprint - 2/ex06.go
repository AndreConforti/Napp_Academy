package main

import "fmt"



func main(){

	generalAvg := [] float32{}
	count := 0
	var nota1, nota2, nota3, nota4 float32

	for i := 0; i < 10; i++{

		fmt.Println("\nAluno ", i + 1)
		fmt.Print("1ª nota: ")
		fmt.Scanln(&nota1)
		fmt.Print("2ª nota: ")
		fmt.Scanln(&nota2)
		fmt.Print("3ª nota: ")
		fmt.Scanln(&nota3)
		fmt.Print("4ª nota: ")
		fmt.Scanln(&nota4)
		avg := (nota1 + nota2 + nota3 + nota4) / 4
		generalAvg = append(generalAvg, avg)
		if avg >= 7{
			count += 1
		}
		fmt.Println(avg)
	}
	fmt.Println("As médias das notas apresentadas foram: ", generalAvg, " e o total de notas maior ou igual a 7 é ", count)
}