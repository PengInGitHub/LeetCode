package LengthOfLastWord

import (
	"strings"
)

func lengthOfLastWord(s string) int {
	bytes := []byte(s)
	lastIndex := len(bytes) - 1
	for i := len(bytes) - 1; i >= 0; i-- {
		if bytes[i] != ' ' {
			lastIndex = i
			break
		}
	}
	bytes = bytes[:lastIndex+1]
	for i := len(bytes) - 1; i >= 0; i-- {
		if bytes[i] == ' ' {
			return len(bytes) - 1 - i
		}
	}
	return len(bytes)
}

func lengthOfLastWordUpdate(s string) int {
	if strings.Contains(s, " ") {
		if s == " " {
			return 0
		}
		s = strings.TrimSpace(s)
		return len(s[strings.LastIndex(s, " ")+1:])
	}
	return len(s)
}

//resource
//https://stackoverflow.com/questions/45266784/go-test-string-contains-substring
//https://stackoverflow.com/questions/22688010/how-to-trim-leading-and-trailing-white-spaces-of-a-string
