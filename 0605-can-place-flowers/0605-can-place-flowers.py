class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 1
        if len(flowerbed)>=2:
            if flowerbed[0] == 0 and flowerbed[1]==0:
                flowerbed[0] = 1
                count += 1
        #count
        while i < (len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1]== 0:
                print(i)    
                flowerbed[i] = 1
                count += 1
            i+=1  
        print(flowerbed)     
        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            flowerbed[len(flowerbed)-1] = 1
            count +=1 
        print(count)
        print(flowerbed)    
        if count >= n:
            return True
        return False    