package main

import "testing"

func TestExamples(t *testing.T) {
	if combinations(5, 3) != 10 {
		t.Errorf("Incorrect number of combinations")
	}
	if combinations(23, 10) != 1144066 {
		t.Errorf("Incorrect number of combinations")
	}
}
