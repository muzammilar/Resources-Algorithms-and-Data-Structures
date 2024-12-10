# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

class Stack(list): # create your own class
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self

def solution(S):
    stck = Stack()
    translation_dict = {"}":"{", ")":"(", "]":"["}
    braces = set([translation_dict[x] for x in translation_dict])
    for s in S:
        if s in braces:
            stck.push(s)
        if s not in translation_dict:
            continue
        if stck.isEmpty():
            return 0
        if stck.pop() != translation_dict[s]:
            return 0
    if not stck.isEmpty(): # it should be empty at end
        return 0
    return 1
"""
A string S consisting of N characters is considered to be properly nested if any of the following conditio

ns is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    int solution(char *S);

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

        N is an integer within the range [0..200,000];
        string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""