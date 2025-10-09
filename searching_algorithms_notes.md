# Searching Algorithms Notes
[This will contain notes on the searching algorithms in this repoository. To be edited later.]

## Linear Search
The most simplest of searching algorithms that searches through an array and returns the index of the value it searches for. A good implementation
also lets the user know in a simple way if the requested value is not found. You can use print statements, however using -1 to indicate a value that is
not found also works.
It is simple & easy to understand and implement via code. If the array is already sorted, then it is better to use the faster Binary search algorithm.

A big difference between the <b><em>sorting algorithms</em></b> and the <b><em>searching algorithms</em></b> is that the sorting algorithms will modify the array,
but the searching algorithm leaves the array unchanged.

### Time Complexity
If Linear search runs and finds the target value as the first value in the array which has <b><em>n</em></b> values, only one comparison is needed. But if
the search runs through the entire array with <b><em>n</em></b> values without finding the target value, then <b><em>n</em></b> comparisons are needed.
This means that the time complexity for Linear Search is:                                  <b><em>O(n)</em></b>

### Pictures
{Add pictures when found}

## Binary Search
