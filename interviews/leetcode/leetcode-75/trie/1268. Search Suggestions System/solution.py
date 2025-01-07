from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, product: str) -> None:
        node = self.root
        for ch in product:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Add the product to the list of words at each node
            if len(node.words) < 3:
                node.words.append(product)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products lexicographically
        products.sort()

        # Initialize Trie and insert all products
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        node = trie.root
        prefix = ""

        # Traverse through each character of searchWord and get suggestions
        for ch in searchWord:
            prefix += ch
            if node:
                node = node.children.get(ch, None)
            if node:
                result.append(node.words)
            else:
                result.append([])

        return result

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
#     searchWord = "mouse"
#     result = solution.suggestedProducts(products, searchWord)
#     print(result)
