/*Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
*/
package main

import (
	"fmt"
)

func main() {

	numbers := []int{}
	var value int

	for true {
		fmt.Print("Digite um valor: ")
		fmt.Scanln(&value)
		if value < 0 {
			break
		} else {
			numbers = append(numbers, value)
		}
	}

	fmt.Println("a - Quantidade de valores que foram lidos : ", len(numbers))
	fmt.Println("b - Valores que foram informados..........: ", numbers)
	for i, j := 0, len(numbers)-1; i < j; i, j = i+1, j-1 {
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	fmt.Println("c - Valores na ordem inversa..............: ", numbers)
	sum := 0
	for i := range numbers {
		sum += i
	}
	fmt.Println("d - Soma dos valores......................: ", sum)
	avg := sum / len(numbers)
	fmt.Println("e - Média dos valores.....................: ", avg)
	upToAvg := 0
	for i := range numbers {}
	fmt.Println("f - Quantidade de valores acima da média..: ", len(numbers))
	fmt.Println("g - Quantidade de valores abaixo de 7.....: ", len(numbers))

}
