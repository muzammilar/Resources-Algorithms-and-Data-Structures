### 208. Implement Prefix Trie

Implement a Trie (Prefix Tree) with the following operations:

- `insert(word: str)`: Inserts a word into the trie.
- `search(word: str)`: Returns `true` if the word exists in the trie.
- `startsWith(prefix: str)`: Returns `true` if there is any word in the trie that starts with the given prefix.

#### Approach:

A **Trie** (or **Prefix Tree**) is a tree-like data structure used to store strings where each node represents a character of a string. A key insight is that strings with common prefixes will share a common path in the tree.

#### Trie Operations:

1. **Insert Operation**:
   - For inserting a word, we start at the root and traverse each character of the word.
   - At each character, check if the node for that character exists. If not, create a new node.
   - After inserting all characters, mark the last node as representing the end of the word.

2. **Search Operation**:
   - To search for a word, we start at the root and traverse according to the characters of the word.
   - If we successfully reach the end of the word and the last node is marked as a word-ending node, return `true`. Otherwise, return `false`.

3. **Prefix Search Operation**:
   - For checking if a prefix exists, we perform the same traversal as in the search operation but don't require the end of the word to be reached.

#### Time Complexity:
- **Insert**: O(m), where `m` is the length of the word.
- **Search**: O(m), where `m` is the length of the word.
- **Prefix Search**: O(k), where `k` is the length of the prefix.

#### Space Complexity:
- **O(n * m)**, where `n` is the number of words and `m` is the length of the average word in the Trie, as we store each character of each word.
