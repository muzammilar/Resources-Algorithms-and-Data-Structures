
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):
    n = len(S)
    score = {'A':1,'C':2,'G':3, 'T':4}
    apearence_dict = {x:[0 for i in xrange(n+1)] for x in score}

    for i in range(1,n+1):
        s = S[i-1]
        for code in score:
            apearence_dict[code][i] = apearence_dict[code][i-1] # this works since initally i-1=-1 and -1th index val is 0
            if s == code:
                apearence_dict[s][i] += 1 # this works since initally i-1=-1 and -1th index val is 0

    pqlen = len(P)
    results = []
    for i in range(pqlen):
        p, q = P[i], Q[i] + 1
        x = min([score[code] for code in score if (apearence_dict[code][q] - apearence_dict[code][p] > 0)]) 
        results.append(x)
    return results

    
# Explaination:
"""
The sums you need to keep are how many times each letter has appeared. You need to keep one sum sequence for each letter. (In actuality you don't need a prefix sum for T because if A, C, or G does not appear, you can assume T. Explained in more detail in the example below.)

So, for the example in the problem statement, CAGCCTA, you end up with three prefix sum arrays that have the following values:

A: 0 1 1 1 1 1 2
C: 1 1 1 2 3 3 3
G: 0 0 1 1 1 1 1

Look at the A prefix sum array. The value in each position corresponds to how many times that letter has appeared so far. So, for postion 0, A has not appeared yet, C has appeared once, and G has not appeared yet. At position 5, A has appeared once (and we can see from the prefix sum for A that it first appeared at position 1), C has appeared three times, and G has appeared once.

With these arrays, we can now determine whether a given letter appeared or not between any two positions. So, we check A first, then C, and then G. If none of them appeared then we know that only T appeared, which is the reason we do not need a prefix sum to count the T occurrences.

For example, consider the range 2 to 4 as in the problem statement. We can see from the sums for A that a single A has already appeared when the range starts, and only a single A has appeared at the end of the range. Thus, there could not have been an A in 2 to 4. Now we check C. At the start of the range there has been a single C appear, but at the end of the range there have been three. Thus, there must have been at least one C from 2 to 4, and we can conclude that the minimal impact factor for 2 to 4 is 2.    
"""

# Question:    
"""


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty zero-indexed string S consisting of N characters and two non-empty zero-indexed arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

        a Results structure (in C), or
        a vector of integers (in C++), or
        a Results record (in Pascal), or
        an array of integers (in any other programming language).

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Assume that:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

Complexity:

        expected worst-case time complexity is O(N+M);
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
Copyright 2009–2017 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited. 
"""