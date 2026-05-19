class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1; zeroct = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeroct += 1
                if zeroct > 1:
                    product = 0; break

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = int(product / nums[i]) if zeroct == 0 else 0
            else:
                nums[i] = product if zeroct <= 1 else 0
        return nums    