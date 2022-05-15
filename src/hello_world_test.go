package codingInterviewPrep

import (
	"fmt"
	"testing"

	"github.com/google/go-cmp/cmp"
)

func SayHello(name string) string {
	return fmt.Sprintf("Hello %s", name)
}

func TestSplit(t *testing.T) {
	testdata := map[string]struct {
		input string
		want  string
	}{
		"boy name":  {input: "Vipin", want: "Hello Vipin"},
		"girl name": {input: "Geethu", want: "Hello Geethu"},
	}

	for name, tc := range testdata {
		t.Run(name, func(t *testing.T) {
			got := SayHello(tc.input)
			diff := cmp.Diff(tc.want, got)
			if diff != "" {
				t.Fatalf(diff)
			}
		})
	}
}
