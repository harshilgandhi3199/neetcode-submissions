import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        sorted_map = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))

        count = 0
        for key in sorted_map.keys():
            output.append(key)
            count += 1
            if count == k:
                break

        return output