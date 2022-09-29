package main

import (
	
	"fmt"
)

func main(){

	var name  string
	var media float64
	var nota1, nota2, nota3, nota4, nota5 float32

	type saltos struct{
		salto1 float64
		salto2 float64
		salto3 float64
		salto4 float64
		salto5 float64
	}

	type atleta struct{
		name string
		media float64
		saltos []saltos
	}

	
	fmt.Print("Nome do atleta: ")
	fmt.Scanln(&name)
	fmt.Print("1º salto: ")
	fmt.Scanln(&nota1)
	fmt.Print("2º salto: ")
	fmt.Scanln(&nota2)
	fmt.Print("3º salto: ")
	fmt.Scanln(&nota3)
	fmt.Print("4º salto: ")
	fmt.Scanln(&nota4)
	fmt.Print("5º salto: ")
	fmt.Scanln(&nota5)
	competidor := saltos{float64(nota1), float64(nota2), float64(nota3), float64(nota4), float64(nota5)}
	media = (float64(nota1) + float64(nota2) + float64(nota3) + float64(nota4) + float64(nota5)) / 5
	atleta1 := atleta{
		name: name,
		media: media,
		saltos: []saltos{},
	}

	fmt.Println(competidor)
	fmt.Println("Atleta: ", atleta1.name)
	fmt.Println("Saltos: ", atleta1.saltos)
	fmt.Println("Média: ", atleta1.media)
	
} 