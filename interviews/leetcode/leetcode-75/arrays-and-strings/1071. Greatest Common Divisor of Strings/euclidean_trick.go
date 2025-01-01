package main

func gcdOfStrings(str1 string, str2 string) string {
	// compute length of both
	l1 := len(str1)
	l2 := len(str2)

	// find the gcd of both lengths
	patLen := gcd(l1, l2)

	// find the pattern of both strings
	// this is the length of the shared pattern
	pat := str1[:patLen]

	// compare patterns
	if pat != str2[:patLen] {
		return ""
	}

	// make sure str1 doesn't have any weird pattern
	for i := 0; i < len(str1)/patLen; i++ {
		if pat != str1[i*patLen:(i+1)*patLen] {
			return ""
		}
	}

	// make sure str1 doesn't have any weird pattern
	for i := 0; i < len(str2)/patLen; i++ {
		if pat != str2[i*patLen:(i+1)*patLen] {
			return ""
		}
	}

	// return successful pattern
	return pat
}

func gcd(a, b int) int {
	// base case
	if a == 0 || b == 0 {
		return 0
	}
	// generic case
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
