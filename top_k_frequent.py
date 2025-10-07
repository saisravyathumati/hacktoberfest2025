from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter k: "))
    print(top_k_frequent(nums, k))
