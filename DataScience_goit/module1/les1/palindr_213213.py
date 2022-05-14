def is_palindrom(data):
    mid = len(data) // 2

    if data[0] == data[-1] and len(data) % 2 == 0:

        f_half = data[:mid]
        s_half = data[mid:]

        for i, b in zip(f_half, s_half[::-1]):
            if i != b:
                return False
        return True
    else:
        return False


print(is_palindrom([1, 2, 3, 4, 5, 5, 4, 4, 2, 1, 2, 34, 51123]))
