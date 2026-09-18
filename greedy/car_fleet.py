class Solution:
    def carFleet( self, target: int, position: list[int], speed: list[int]) -> int:

        vector = [ [pos, speed[i]] for i, pos in enumerate(position) ]
        vector.sort(key=lambda x:x[0], reverse = True)

        time = []
        fleet = 1

        for i in vector:
            time.append((target-i[0])/i[1])

        leader = time[0]
        for i in time:
            # print()
            if i > leader:
                fleet+=1
                leader = i



        return fleet








target = 100
position = [0,2,4]
speed = [4,2,1]

a = Solution()
ans = a.carFleet(target, position, speed)
print(ans)
