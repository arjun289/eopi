class Solution:
    def twoSum(self, nums, target):
        manage_hash = {}

        if nums == []:
            return None

        for index, value in nums:
            result = target - value
            if result in manage_hash:
                return [index, manage_hash[result]]
            else:
                manage_hash[value] = index

        return None


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    sol = Solution()
    result = sol.twoSum(arr, 9)
    print(result)
