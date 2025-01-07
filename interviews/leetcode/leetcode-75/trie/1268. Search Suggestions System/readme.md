### 1268. Search Suggestions System

Given a list of products and a search word, implement a system to suggest products as the user types.

- Implement the following method:
  - `suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]`: Given a list of `products` and a `searchWord`, return a list of list of product suggestions where each list of suggestions corresponds to a prefix of the `searchWord`.

### Approach - Trie:

To efficiently handle the search and suggestion process, we can utilize a **Prefix Trie**. This approach helps in storing products and retrieving suggestions based on prefixes efficiently.

1. **Construct a Trie**: Build a Trie structure from the list of products.
2. **Insert Products into the Trie**: Insert each product in the sorted order into the Trie.
3. **Suggest Products**: For each prefix of the search word, traverse the Trie and collect up to 3 suggestions.
4. **Prefix Search**: Use the Trie to find words starting with each prefix efficiently.

#### Time Complexity:
- **Inserting Products**: O(n * m), where `n` is the number of products and `m` is the length of the average product.
- **Searching for Prefixes**: O(m), where `m` is the length of the search word.
- For each prefix, the Trie search is O(m), and generating suggestions is O(3) for each prefix.

#### Space Complexity:
- O(n * m) for storing the Trie, where `n` is the number of products and `m` is the length of the average product.


#### Approach - String:

1. **Sort Products**: Begin by sorting the product list. Sorting ensures that when we search for a prefix, the suggested products are always in lexicographical order.
2. **Iterate Over Search Word Prefixes**: For each prefix of the search word, we check if there are any products in the list that start with the given prefix.
3. **Use Binary Search for Efficiency**: Use a binary search to find the first product that starts with the current prefix.
4. **Store Suggestions**: For each prefix, store the top three suggestions (if available).

#### Time Complexity:
- Sorting the products: O(n * log n), where `n` is the number of products.
- For each prefix, we perform a binary search, which takes O(log n) time. For `m` prefixes, the total time is O(m * log n).

#### Space Complexity:
- O(n) for storing the sorted products and the suggestions.
