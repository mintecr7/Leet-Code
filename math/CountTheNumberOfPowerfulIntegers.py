class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        power_int = 0
        
        checked = False 
        count = 1
        while True:
            if count > limit:
               break
            if not checked:
              if int(s) >=  start and int(s)<= finish:
                power_int += 1
                print("wtf")
              checked = True
              
            else:
                power = str(count) + s
                if int(power) >=  start and int(power)<= finish:
                  power_int +=1 
                  count += 1
                elif int(power) > finish:
                   break
        return power_int


start = 15
finish = 215 
limit = 6
s = "10"

a = Solution()


ans = a.numberOfPowerfulInt(start, finish, limit, s)

print(ans)