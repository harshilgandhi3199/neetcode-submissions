class Solution:
    # Dict -> list -> sort -> pop k numbers
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])

        arr.sort()

        result = []
        for _ in range(k):
            result.append(arr.pop()[1])

        return result