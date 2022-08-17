package main

import "fmt"

func main(){

	age := [] int32{}
	height := [] float32{}
	var agePerson int
	var heightPerson float32

	for i := 0; i < 5; i++{

		fmt.Print("\nIdade da ", i + 1, "ª pessoa: ")
		fmt.Scanln(&agePerson)
		age = append(age, int32(agePerson))
		fmt.Print("Altura da ", i + 1, "ª pessoa: ")
		fmt.Scanln(&heightPerson)
		height = append(height, heightPerson)
	}
	
	fmt.Println(age, height)

	for i, j := 0, len(age)-1; i < j; i, j = i+1, j-1 {
		age[i], age[j] = age[j], age[i]
	}
	for i, j := 0, len(height)-1; i < j; i, j = i+1, j-1 {
		height[i], height[j] = height[j], height[i]
	}
	
	fmt.Println(age, height)
	


}