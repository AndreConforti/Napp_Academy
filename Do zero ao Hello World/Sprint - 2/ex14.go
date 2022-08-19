/*Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". 
aso contrário, ele será classificado como "Inocente"*/

package main

import (
	"fmt"
		"strings"
)

func main(){

	classification := [] string{}
	var question string
	var reu string

	fmt.Println("Responda \"S\" para \"SIM\" ou \"N\" para \"NÃO\"\n")
	fmt.Print("Telefonou para a vítima? ")
	fmt.Scanln(&question)
	question = strings.ToUpper(question)
	if question == "S"{
		classification = append(classification, question)
	}
	fmt.Print("Esteve no local do crime? ")
	fmt.Scanln(&question)
	question = strings.ToUpper(question)
	if question == "S"{
		classification = append(classification, question)
	}
	fmt.Print("Mora perto da vítima? ")
	fmt.Scanln(&question)
	question = strings.ToUpper(question)
	if question == "S"{
		classification = append(classification, question)
	}
	fmt.Print("Devia para a vítima? ")
	fmt.Scanln(&question)
	question = strings.ToUpper(question)
	if question == "S"{
		classification = append(classification, question)
	}
	fmt.Print("Já trabalhou com a vítima? ")
	fmt.Scanln(&question)
	question = strings.ToUpper(question)
	if question == "S"{
		classification = append(classification, question)
	}

	if len(classification) == 2{
		reu = "Susteito"
	} else if len(classification) == 3 || len(classification) == 4{
		reu = "Cúmplice"
	} else if len(classification) == 5 {
		reu = "Assassino"
	} 	else {
		reu = "Inocente" 
	}
		
	fmt.Println(classification)
	fmt.Println("Diante das respostas, o réu foi considerado: ", reu)
}