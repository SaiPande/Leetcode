class BubbleSortClass:

    def bubblesort(self, nums: list[int])-> list[int]:
        
        for i in range(len(nums)):
            swapped = False

            for j in range(0, len(nums)-i-1):

                if nums[j+1] < nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    swapped = True
            if swapped == False: #optimized as no more elements to swap, list is already sorted
                break        
        return nums            
    

if __name__ == "__main__":
    s = BubbleSortClass()
    lst = [5,8,3,7,3,5,55,12,789,54,234,234,6774]
    t = s.bubblesort(lst)
    print(t)

#PS C:\Users\saipa\OneDrive\Documentos\StatShield> python3 BubbleSortClass.py
[3, 3, 5, 5, 7, 8, 12, 54, 55, 234, 234, 789, 6774]
