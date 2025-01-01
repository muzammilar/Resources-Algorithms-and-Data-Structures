### 2130. Maximum Twin Sum of a Linked List

Given the head of a singly linked list, find the maximum twin sum of the list. A twin sum is defined as the sum of a node and its corresponding twin node in the second half of the list (starting from the end).

* Split the list into two halves. The first half consists of nodes at the first half of the list, and the second half consists of nodes in reverse order.
* For each node in the first half, pair it with the corresponding node in the second half and calculate their sum.
* Return the maximum twin sum.
