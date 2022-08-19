package main

import (
	"fmt"
	"time"
)


func main() {
	
	t := time.Now()
	fmt.Printf("%T\n", t)
	
	fmt.Println(t.Hour(), t.Minute())

}

