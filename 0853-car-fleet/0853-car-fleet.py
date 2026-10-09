class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        combined = []
        for i in range(n):
            combined.append([position[i], speed[i]])

        combined.sort(reverse = True)
           
        leadingcarposition = combined[0][0]
        leadingcarspeed = combined[0][1]
        time_to_target = (target - leadingcarposition) / leadingcarspeed
        combined[0][0] = time_to_target
        
        for i in range(1,n):
            currentcarpos = (target - combined[i][0]) / combined[i][1]
            prevcarpos = combined[i-1][0]

            if currentcarpos<=prevcarpos:
                combined[i][0] = prevcarpos
            else:
                combined[i][0] = currentcarpos

 
        result = [x[0] for x in combined]     
 
        fleets = 1
        i = 1
        while i<(len(result)):
            if result[i]==result[i-1]:                
                i+=1
            else:
                i+=1
                fleets+=1     
        return fleets  