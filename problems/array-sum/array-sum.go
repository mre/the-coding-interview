package main

import (
	"fmt"
	"reflect"
)

func main() {
	var arr []interface{}
	arr = append(arr, 5)

	var arr1 []interface{}
	arr1 = append(arr1, 3)
	arr1 = append(arr1, 4)
	arr1 = append(arr1, arr)

	var arr2 []interface{}
	arr2 = append(arr2, 1)
	arr2 = append(arr2, 2)
	arr2 = append(arr2, arr1)

	fmt.Println(sum(arr2))
}

func sum(arr []interface{}) int {
	var total int

	for _, val := range arr {
		valType := reflect.TypeOf(val)

		switch valType.Kind() {
		case reflect.Slice:
			total += sum(convertToSlice(val))
			break
		default:
			total += val.(int)
		}
	}

	return total
}

func convertToSlice(i interface{}) []interface{} {
	interfaceVal := reflect.ValueOf(i)

	if interfaceVal.Kind() != reflect.Slice {
		return []interface{}{}
	}

	var result []interface{}
	for i := 0; i < interfaceVal.Len(); i++ {
		result = append(result, interfaceVal.Index(i).Interface())
	}

	return result
}

