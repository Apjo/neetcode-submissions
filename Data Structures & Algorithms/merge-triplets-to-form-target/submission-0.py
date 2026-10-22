class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #is it given that all elements of target arr will be in the triplets? if not immediately ret a False
        #the triplets should not contains a num > than the numbers in target, if it does we ignore that triplet
        all_seen = set()
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            else:
                for k, v in enumerate(trip):
                    if v == target[k]:
                        all_seen.add(k)



        return len(all_seen) == 3