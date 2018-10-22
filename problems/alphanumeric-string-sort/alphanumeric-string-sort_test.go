package main

import "testing"

func Test_alphanumSort(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "General Scenario : Upper,Lower,Odd and Even",
			args: args{"Sorting0123456789"},
			want: "ginortS0246813579",
		},
		{
			name: "No upper case",
			args: args{"foobar1237348421"},
			want: "abfoor2244811337",
		},
		{
			name: "Only numbers",
			args: args{"90856123456789"},
			want: "02466881355799",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := alphanumSort(tt.args.str); got != tt.want {
				t.Errorf("alphanumSort() = %v, want %v", got, tt.want)
			}
		})
	}
}
