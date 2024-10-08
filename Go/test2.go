package main

import (
	"fmt"
)

// declare multiple constanta
const (
	A int = 1
	B     = 3.14
	C     = "Hi!"
)

func test() {
	//bisa pake x:=2
	var student1 string
	student1 = "John"
	fmt.Println(student1)
	// var arr1 = [...]int{1, 2, 3}
	// arr2 := [...]int{4, 5, 6, 7, 8}
}

func print_fmt() {
	var i = 15.5
	var txt = "Hello World!"
	/*v: default format
	#v: Go-syntax format
	%T: type of the value
	%%: print %
	*/
	fmt.Printf("%v\n", i)
	fmt.Printf("%#v\n", i)
	fmt.Printf("%v%%\n", i)
	fmt.Printf("%T\n", i)

	fmt.Printf("%v\n", txt)
	fmt.Printf("%#v\n", txt)
	fmt.Printf("%T\n", txt)
}

func loop_ex() {
	for i := 0; i < 5; i++ {
		if i == 3 {
			break
		}
		fmt.Println(i)
	}
	fruits := [3]string{"apple", "orange", "banana"}
	for idx, val := range fruits {
		fmt.Printf("%v\t%v\n", idx, val)
	}
	for _, val := range fruits {
		fmt.Printf("%v\n", val)
	}
}

func struct_ex() {
	type Person struct {
		name   string
		age    int
		job    string
		salary int
	}

	var pers1 Person

	// Pers1 specification
	pers1.name = "Hege"
	pers1.age = 45
	pers1.job = "Teacher"
	pers1.salary = 6000
}

func map_ex() {
	var a = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
	b := map[string]int{"Oslo": 1, "Bergen": 2, "Trondheim": 3, "Stavanger": 4}

	fmt.Printf("a\t%v\n", a)
	fmt.Printf("b\t%v\n", b)
}

func Solution(n int) int {
	var sum_f = [...]int{1, 2, 3, 4}
	var sum_n = 0
	for i := 1; i <= len(sum_f); i++ {
		sum_n += sum_f[i]
	}
	//Insert your code here
	//numbers := make([]int, length)
	return sum_n
}

func main() {
	fmt.Println("Subscribe now")
	// Solution(6)
}
