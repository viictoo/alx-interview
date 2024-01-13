#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
"""


# Passes All Checks
# def canUnlockAll(boxes):
#     """Depth-first search version"""
#     visited = {0: True}
#     stack = [0]
#     while stack:
#         count = 0
#         idx = stack.pop()
#         for key in boxes[idx]:
#             if key not in visited and key < len(boxes):
#                 visited[key] = True
#                 stack.append(key)
#     print(len(visited))
#     return len(visited) == len(boxes)

def canUnlockAll(boxes):
    """brute force through each box"""
    if not boxes:
        return False
    size, visited, idx = len(boxes), {}, 0

    for box in boxes:
        if len(box) == 0 or idx == 0:
            visited[idx] = -1
        for key in box:
            if key < size and key != idx:
                visited[key] = key
        if len(visited) == size:
            return True
        idx += 1
    return False


if __name__ == "__main__":
    boxes = [[], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[0, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print(canUnlockAll(boxes))
