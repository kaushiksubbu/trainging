class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        z_cnt=flowerbed.count(0)
        open_cnt=0
        if (z_cnt >= n+2):
            for i in range(int(l)):
                nxt1 = int(i)+1
                nxt2 = nxt1+1
                if (flowerbed[i] == 0):
                    if(
                        flowerbed[nxt1] != 1 
                        and 
                        (nxt2 <= int(l) and flowerbed[nxt2] == 0)
                    ):
                        open_cnt+=1
            if (open_cnt>=n):
                return(True)
        else:
            return(False)
