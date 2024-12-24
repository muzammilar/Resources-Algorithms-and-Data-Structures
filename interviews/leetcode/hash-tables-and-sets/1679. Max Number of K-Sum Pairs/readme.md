### 1679. Max Number of K-Sum Pairs

You are given an array of integers `nums` and an integer `k`. Your task is to find the maximum number of distinct pairs (i, j) such that:

* `nums[i] + nums[j] == k`
* `i < j` (the pair should be distinct)


#### Solutions

* Use hash table. It has `O(n)` time and `O(n)` memory complexity.
* Sort the data and iterate using two pointers. It has `O(1)` memory but `O(n*log(n))` time complexity.
