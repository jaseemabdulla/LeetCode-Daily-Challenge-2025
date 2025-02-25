def numOfSubarrays(arr):
    res = 0
    odd = 0
    even = 0
    csum = 0
    for num in arr:
        csum += num
        if csum % 2:
            res += 1 + even
            odd += 1
        else:
            res += odd
            even += 1
    return res % (10**9 + 7)
