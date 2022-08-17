package main

import "fmt"

func main(){

	var nota1, nota2, nota3, nota4 float32
	fmt.Print("1ª nota: ")
	fmt.Scanln(&nota1)
	fmt.Print("2ª nota: ")
	fmt.Scanln(&nota2)
	fmt.Print("3ª nota: ")
	fmt.Scanln(&nota3)
	fmt.Print("4ª nota: ")
	fmt.Scanln(&nota4)

	notas := []float32 {nota1, nota2, nota3, nota4}

	media := (nota1 + nota2 + nota3 + nota4) / 4

	fmt.Printf("As notas apresentadas foram: %f\n", notas)
	fmt.Println("A média é de ", media)
}