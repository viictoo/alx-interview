#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
"""


# def canUnlockAll(boxes):
#     """depth first search"""
#     if ((isinstance(boxes, list)) and len(boxes) > 0):
#         visited = [False]*len(boxes)

#         def dfs(box):
#             visited[box] = True
#             for key in boxes[box]:
#                 if key == 0:
#                     visited[box] = True
#                 if not visited[key]:
#                     dfs(key)

#         dfs(0)

#         return all(visited)
#     return False

# def canUnlockAll(boxes):
#     """brute force through each box"""
#     if not boxes:
#         return False
#     size, visited, idx = len(boxes), {}, 0

#     for box in boxes:
#         if len(box) == 0 or idx == 0:
#             visited[idx] = -1
#         for key in box:
#             if key < size and key != idx:
#                 visited[key] = key
#         if len(visited) == size:
#             return True
#         idx += 1
#     return False
def append_to_array(src, boxes_len, boxes, arr_to_append):
    """ Append keys to array """
    for key in src:
        if key < boxes_len and key > 0:
            if key not in arr_to_append:
                arr_to_append.append(key)
            for k in boxes[key]:
                if k not in arr_to_append:
                    arr_to_append.append(k)


def canUnlockAll(boxes):
    """ Can Unlock All

        Args:
            boxes: a list of lists
    """
    boxes_len = len(boxes)



    unloced_keys = [0]

    for i in range(boxes_len):
        if i in unloced_keys:
            append_to_array(boxes[i], boxes_len, boxes, unloced_keys)

    if not all(i in unloced_keys for i in range(boxes_len)):
        return (False)

    return (True)


if __name__ == "__main__":
    boxes = [[], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[0, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
