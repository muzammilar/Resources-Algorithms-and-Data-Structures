import "strings"

func mergeAlternately(word1 string, word2 string) string {

	len1 := len(word1)
	len2 := len(word2)
	totLen := len1 + len2
	minLen := min(len1, len2)
	// use a string builder
	var sb strings.Builder

	// set the length to the total length since it's known
	sb.Grow(totLen)

	// iterate over both strings
	for i := 0; i < minLen; i++ {
		sb.WriteByte(word1[i])
		sb.WriteByte(word2[i])
	}

	// add remaining strings
	remLen := len1 - minLen
	remStr := &word1
	if len2 > minLen {
		remLen = len2 - minLen
		remStr = &word2
	}

	// iterate over remaining string
	for i := minLen; i < minLen+remLen; i++ {
		sb.WriteByte((*remStr)[i])
	}

	return sb.String()
}
