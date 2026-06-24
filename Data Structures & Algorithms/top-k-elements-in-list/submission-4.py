class Solution:
    # Bucket Sort solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # build a freq map
    # create groups freq. freq[i] = all numbers that have freq i
    # start gathering numbers in result from descending order of freq groups
    # stop when you have k numbers in the result list.
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        freq = [[] for _ in range(len(nums))]
        for num, count in freq_map.items():
            freq[count - 1].append(num)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            result.extend(freq[i])
            if len(result) >= k:
                break

        return result[:k]
