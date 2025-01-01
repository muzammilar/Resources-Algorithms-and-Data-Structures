### 11. Container With Most Water

You are given an array of non-negative integers `height[]` where each element represents the height of a vertical line at that index. The width of each line is `1`. You need to find two lines such that together they form a container that holds the most water.

The container’s water capacity is determined by the shorter of the two lines (because the water would spill over if the shorter line is exceeded) and the horizontal distance between them. More formally, the amount of water a container can store is given by:

```
Area=min(height[i], height[j])×(j−i)
```

Where `i` and `j` are indices of the two lines. Your task is to find the maximum area of water that can be contained.
