def threeSum(nums: list[int]):
    res = set()
    inverse = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            sum = -(nums[i] + nums[j])

            if sum in inverse:
                list = [nums[i], nums[j], sum]
                list.sort()
                res.add(tuple(list))

            inverse.add(nums[j])

    print(res)
print(threeSum([-1,0,1,2,-1,-4]))