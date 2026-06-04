class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival_times = [(target - position[i])/ speed[i] for i in range(len(position))]
        temp = sorted(zip(arrival_times, position), reverse=True)
        # stk=[]
        num_fleet=0
        ans=-1
        for rec in temp:
            if rec[1] > ans:
                ans=rec[1]
                num_fleet+=1
        return num_fleet