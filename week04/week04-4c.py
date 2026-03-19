        #week04-4c
        H=Counter(nums)
        for nn in nums:
            if nn %2==0 and H[nn]==1:
                return nn
