class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = [(target - position[i])/ speed[i] for i in range(len(position))]
        temp = sorted(zip(arrival_times, position), reverse=True)
        stk=[]
        for rec in temp:
            if not stk:
                stk.append(rec)
            elif rec[1] > stk[-1][1]:
                stk.append(rec)
        return len(stk)