def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box (box 0)
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

