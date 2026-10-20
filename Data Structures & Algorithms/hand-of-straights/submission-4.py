class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) == 1 and groupSize == 1:
            return True
        
        hand.sort()
        
        freq={}
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        print(freq)

        for h in hand:
            #use the k to be added to a grp num, after adding decrement its freq by 1.
            #when grp_num reaches grp size, reset to 0
            if freq[h] == 0:
                continue
            for i in range(groupSize):
                curr = h + i
                if curr in freq:
                    if freq[curr] == 0:
                        return False
                    freq[curr] -= 1
                else:
                    return False
        return True