class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # Sort the products lexicographically
        products.sort()

        result = []
        prefix = ""

        # Iterate through each character of searchWord
        for ch in searchWord:
            prefix += ch
            suggestions = []

            # Find products that match the current prefix
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)

            # Store up to 3 suggestions for the current prefix
            result.append(suggestions[:3])

        return result

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     products = ["mobile","mouse","moneypot","monitor","mousepad"]
#     searchWord = "mouse"
#     result = solution.suggestedProducts(products, searchWord)
#     print(result)
