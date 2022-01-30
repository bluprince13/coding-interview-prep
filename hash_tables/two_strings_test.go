package codingInterviewPrep

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func twoStrings(s1 string, s2 string) string {
	for _, letter := range s2 {
		if !strings.Contains(s1, string(letter)) {
			return "NO"
		}
	}
	return "YES"
}

func TestTwoStringsReturnsNO(t *testing.T) {
	received := twoStrings("hello", "world")
	assert.Equal(t, received, "NO")
}

func TestTwoStringsReturnsYES(t *testing.T) {
	received := twoStrings("hello", "hol")
	assert.Equal(t, received, "YES")
}
