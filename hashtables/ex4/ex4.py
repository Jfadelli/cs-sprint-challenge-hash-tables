def has_negatives(a):
    nums, result = set(), []
    for i in a:
        neg = 0 - i
        if neg in nums:
            result.append(abs(neg))
        else:
            nums.add(i)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))