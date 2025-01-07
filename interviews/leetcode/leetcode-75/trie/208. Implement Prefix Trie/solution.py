class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            node.children.setdefault(ch, TrieNode())
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Main function (commented out by default)
# def main():
#     trie = Trie()
#     trie.insert("apple")
#     print(trie.search("apple"))   # true
#     print(trie.search("app"))     # false
#     print(trie.startsWith("app")) # true
#     trie.insert("app")
#     print(trie.search("app"))     # true
