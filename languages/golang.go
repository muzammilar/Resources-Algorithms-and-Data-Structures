



func vowelSearch() {
	var s string = "apple"

	// Convert string to a slice for easier manipulation
	str := []rune(s)

	// Function to check if a character is a vowel
	isVowel := func(ch rune) bool {
		return strings.ContainsRune("aeiouAEIOU", ch)
	}

}



func stringBuilder(word1 string, word2 string) string {

	totLen := len(word1) + len(word2

	// use a string builder
	var sb strings.Builder

	// set the length to the total length since it's known
	sb.Grow(totLen)

	// iterate over both strings
	for i := 0; i < minLen; i++ {
		sb.WriteByte(word1[i])
		sb.WriteByte(word2[i])
	}

	return sb.String()
}


func dateParser() {

	// date format for parsing _2 means that there could be something before the date
	dateFmt := "_2 Jan 2006"

	// parse the date
	t, err := time.Parse(dateFmt, dateFmt)

	// format the date
	time.Format(dateFmt, t)
}
