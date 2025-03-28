class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
 #def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#flowerbed = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]  # An example flowerbed (length = 10)
#n = 3  # Example of how many flowers we can add
#flowerbed = [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0]  # Another example of flowerbed (length = 11)
#n = 2  # Number of flowers we can add

        l=len(flowerbed)
        z_cnt=flowerbed.count(0)
        open_cnt=0
        print(l,n,z_cnt)
        if (z_cnt >= n+2):
            for i in range(l-1):
                print(i)
                print(flowerbed[i],flowerbed[i-1],flowerbed[i+1])
                if (flowerbed[i] == 0):
                    if ((flowerbed[i-1] == 0 and flowerbed[i+1] == 0)):
                        open_cnt+=1
                print(open_cnt)
            i+=1
            print(i)

            if (flowerbed[i-1] == 0 and flowerbed[i] == 0):
                open_cnt+=1
            print(open_cnt)


            print(open_cnt>=n)        
        return(open_cnt>=n)
