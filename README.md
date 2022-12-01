# Advent of Code 2022
Marc Sances answers

## Exercise 1

### First question

A simple linear search with a basic comparison. Nothing too fancy.

Time complexity O(n), space complexity O(1).

### Second question

Instead of creating a list, sorting it and calling it a day, since we only check for three elves, I went
for a more efficient way, by keeping track of the three highest numbers and simply swapping.

This way the complexity will stay linear even when the set grows more.

Time complexity O(n), space complexity O(1).