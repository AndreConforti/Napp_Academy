package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	rand.Seed(time.Now().Unix())
	letters := [] string{}
	consonants := [] string{}
	count := 0

    //Generate a random character between lowercase a to z
    for i := 0; i < 10; i++ {
		randomChar := 'a' + rune(rand.Intn(26))
		letters = append(letters, string(randomChar))
		switch string(randomChar){
		case "a":
		case "e":
		case "i":
		case "o":
		case "u":
			continue
		default:
			consonants = append(consonants, string(randomChar))
			count += 1
		}
	}
	fmt.Println(letters)
	fmt.Println("Foram encontradas", count, "consoantes. São elas: ", consonants)
}
