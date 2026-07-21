class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        count_lst = [[] for i in range(len(nums) + 1)]

        ret_lst = []

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for key, val in hashmap.items():
            count_lst[val].append(key)

        for i in range(len(count_lst) - 1, 0, -1):
            for j in count_lst[i]:
                ret_lst.append(j)

                if len(ret_lst) == k:
                    return ret_lst

        return []