# 🚀 LeetCode 45 — Jump Game II

<p align="center">

<img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/Pattern-Greedy%20%7C%20Array-success?style=for-the-badge">

<img src="https://img.shields.io/badge/Status-Solved-brightgreen?style=for-the-badge">

</p>

---

# 📖 Problem Statement

You are given an integer array `nums`, where each element represents the **maximum jump length** from that position.

Return the **minimum number of jumps** required to reach the last index.

It is guaranteed that you can always reach the last index.

---

# 🧠 Pattern Used

* Greedy
* Array

---

# 💡 Intuition

Instead of checking every possible path, process the array level by level.

Treat the current reachable range as one **jump**. While exploring that range, determine the **farthest position** that can be reached for the next jump.

This approach is similar to **Breadth-First Search (BFS)** but uses only constant extra space.

---

# 🚀 Key Insight

For every index inside the current range:

```text
Reach = Current Index + nums[Current Index]
```

Keep updating the farthest reachable position.

Once the current range is completely explored:

* Increase the jump count.
* Move to the next reachable range.

---

# 🏗️ Example

Input

```text
nums = [2,3,1,1,4]
```

Traversal

```text
Index :     0   1   2   3   4
Value :     2   3   1   1   4

Jump 1
Current Range:
[0]

Reach:
2

Next Range:
[1...2]

------------------------

Jump 2

Explore:
1 → Reach = 4
2 → Reach = 3

Farthest = 4

Destination Reached
```

Output

```text
2
```

Path

```text
0 → 1 → 4
```

---

# ⚙️ Algorithm

```text
Initialize

left = 0
right = 0
jumps = 0

While right < last index

    Find the farthest reachable index
    inside the current range

    Move to the next range

    Increase jump count

Return jumps
```

---

# 💻 Python Solution

```python
class Solution(object):
    def jump(self, nums):

        left = 0
        right = 0
        jumps = 0

        while right < len(nums) - 1:

            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest

            jumps += 1

        return jumps
```

---

# 🔍 Dry Run

Input

```python
nums = [2,3,1,1,4]
```

### Jump 1

```text
Current Range

[0]

Reach

0 + 2 = 2

Next Range

[1...2]
```

---

### Jump 2

```text
Index 1

1 + 3 = 4

Index 2

2 + 1 = 3

Farthest = 4
```

Reached the last index.

Answer

```text
2
```

---

# 📊 Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------: |
| Array Traversal  |       O(n) |
| Time Complexity  |   **O(n)** |
| Space Complexity |   **O(1)** |

---

# 🎯 Key Learning

* ✅ Learned the **Greedy Range Expansion** technique.
* ✅ Understood how one range represents one jump.
* ✅ Used the farthest reachable position to determine the next range.
* ✅ Solved the problem in linear time with constant extra space.
* ✅ Explored a BFS-like strategy without using a queue.

---

# 🔗 Related Problems

* Jump Game
* Trapping Rain Water
* Gas Station
* Partition Labels
* Minimum Number of Refueling Stops

---

# ⭐ Conclusion

Jump Game II is a classic Greedy interview problem that demonstrates how expanding the reachable range at each step leads to the minimum number of jumps. By processing one reachable range at a time and selecting the farthest possible reach for the next jump, the algorithm achieves an optimal **O(n)** solution using **O(1)** extra space.
