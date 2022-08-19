// Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

package main

import 
	"fmt"

func main() {

	month := [] string {"Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"}
	temperatures := [] float64{}
	aboveAvg := [] string{}
	var temp float64
	avg := 0.0
	
	for _, v := range month{
		fmt.Print("Temperatura para o mês de ", v, " : ")
		fmt.Scanln(&temp)
		temperatures = append(temperatures, temp)
	}

	for _, v := range temperatures {
		avg += v
	}

	avg = avg / float64(len(temperatures))

	for k, v := range temperatures {
		if v > avg{
			aboveAvg = append(aboveAvg, month[k])
		}
	}

	fmt.Println(avg)
	fmt.Print("Os meses com temperatura acima da média são: ")
	for k, v := range aboveAvg {
		fmt.Print(k + 1, " - ", v, ", ")
	}

	


}