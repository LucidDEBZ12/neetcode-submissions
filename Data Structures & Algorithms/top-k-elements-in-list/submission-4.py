from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        count_list = [[] for i in range(len(nums) + 1)]

        ret_list = []

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for key, val in hashmap.items():
            count_list[val].append(key)

        for i in range(len(count_list) - 1, 0, -1):
            for j in count_list[i]:
                ret_list.append(j)

                if len(ret_list) == k:
                    return ret_list

        return []      
            