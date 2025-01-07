package main

import (
	"sort"
)

// TrieNode represents each node in the Trie.
type TrieNode struct {
	children map[rune]*TrieNode
	words    []string
}

// Trie represents the Trie data structure.
type Trie struct {
	root *TrieNode
}

// Constructor creates a new Trie.
func Constructor() Trie {
	return Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
}

// Insert inserts a product into the Trie.
func (t *Trie) Insert(product string) {
	node := t.root
	for _, ch := range product {
		if _, exists := node.children[ch]; !exists {
			node.children[ch] = &TrieNode{children: make(map[rune]*TrieNode)}
		}
		node = node.children[ch]
		// Add the product at each node, to store suggestions
		if len(node.words) < 3 {
			node.words = append(node.words, product)
		}
	}
}

// SuggestedProducts returns a list of suggestions for each prefix.
func suggestedProducts(products []string, searchWord string) [][]string {
	// Sort products lexicographically to maintain the order of suggestions
	sort.Strings(products)

	// Initialize Trie and insert all products
	trie := Constructor()
	for _, product := range products {
		trie.Insert(product)
	}

	var result [][]string
	node := trie.root
	prefix := ""

	// Traverse through each character of searchWord and get suggestions
	for i := 0; i < len(searchWord); i++ {
		prefix += string(searchWord[i])
		if node != nil {
			node = node.children[rune(searchWord[i])]
		}
		if node != nil {
			result = append(result, node.words)
		} else {
			result = append(result, []string{})
		}
	}
	return result
}

// Main function (commented out by default)
// func main() {
//     products := []string{"mobile", "mouse", "moneypot", "monitor", "mousepad"}
//     searchWord := "mouse"
//     result := suggestedProducts(products, searchWord)
//     fmt.Println(result)
// }
