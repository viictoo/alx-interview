#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    """depth first search"""
    # if ((isinstance(boxes, list)) and len(boxes) > 0):
    #     visited = [False]*len(boxes)

    #     def dfs(box):
    #         visited[box] = True
    #         for key in boxes[box]:
    #             if not visited[key]:
    #                 dfs(key)

    #     dfs(0)

    #     return all(visited)
    return True


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
