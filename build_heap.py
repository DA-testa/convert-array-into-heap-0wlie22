# python3


def build_heap(data):
    n = len(data)
    swaps = []

    # Starting from the last non-leaf node
    for i in range(n // 2, -1, -1):
        current = i

        # Sift down the current node until it reaches its correct position
        while current * 2 + 1 < n:
            left = current * 2 + 1
            right = current * 2 + 2 if current * 2 + 2 < n else left
            j = left if data[left] < data[right] else right

            if data[current] <= data[j]:
                break

            swaps.append((current, j))
            data[current], data[j] = data[j], data[current]
            current = j

    return swaps


def main():
    # Input source and data
    source = input().strip()
    if source == 'K':
        n = int(input())
        data = list(map(int, input().split()))
    elif source == 'F':
        with open(input().strip(), 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    else:
        raise ValueError("Invalid input source")

    # Check data length
    assert len(data) == n

    # Build heap and output swaps
    swaps = build_heap(data)
    assert len(swaps) <= 4 * n
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
