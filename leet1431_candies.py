class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        can_max=max(candies)
        out=[]
        for i in range(int(len(candies))):
            out.append(candies[i]+extraCandies >= can_max)
        return(out)
