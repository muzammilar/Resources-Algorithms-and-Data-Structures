package main

// TrieNode represents a node in the Trie.
type TrieNode struct {
	children map[rune]*TrieNode
	isEnd    bool
}

// Trie represents the Trie data structure.
type Trie struct {
	root *TrieNode
}

// Constructor to create a new Trie.
func Constructor() Trie {
	return Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
}

// Insert inserts a word into the Trie.
func (t *Trie) Insert(word string) {
	node := t.root
	for _, ch := range word {
		if _, exists := node.children[ch]; !exists {
			node.children[ch] = &TrieNode{children: make(map[rune]*TrieNode)}
		}
		node = node.children[ch]
	}
	node.isEnd = true
}

// Search checks if a word exists in the Trie.
func (t *Trie) Search(word string) bool {
	node := t.root
	for _, ch := range word {
		if _, exists := node.children[ch]; !exists {
			return false
		}
		node = node.children[ch]
	}
	return node.isEnd
}

// StartsWith checks if there is any word in the Trie that starts with the given prefix.
func (t *Trie) StartsWith(prefix string) bool {
	node := t.root
	for _, ch := range prefix {
		if _, exists := node.children[ch]; !exists {
			return false
		}
		node = node.children[ch]
	}
	return true
}

// Main function (commented out by default)
// func main() {
//     trie := Constructor()
//     trie.Insert("apple")
//     fmt.Println(trie.Search("apple"))   // true
//     fmt.Println(trie.Search("app"))     // false
//     fmt.Println(trie.StartsWith("app")) // true
//     trie.Insert("app")
//     fmt.Println(trie.Search("app"))     // true
// }
