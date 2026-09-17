class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[current]

            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]

                current = next_index
                count += 1

                if current == start:
                    break

            start += 1