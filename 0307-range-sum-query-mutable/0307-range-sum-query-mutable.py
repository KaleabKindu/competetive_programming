class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.segmentTree = [0 for i in range(4*len(nums))]
        self.n = len(nums)
        self.build(0,0, len(nums) - 1)
    
    def build(self, i, l, r):
        if l == r:
            self.segmentTree[i] = self.array[l]
        else:     
            mid = (l + r)//2

            self.build(2*i + 1, l, mid)

            self.build(2*i + 2, mid + 1, r)

            self.segmentTree[i] = self.segmentTree[2*i + 1] + self.segmentTree[2*i + 2]

        

    def update(self, index: int, val: int) -> None:
        def update(i = 0, l = 0, r = self.n - 1):
            if l == r:
                self.segmentTree[i] = val 
                self.array[index] = val
            else:     
                mid = (l + r)//2
                if l <= index <= mid:
                    update(2*i + 1, l, mid)
                elif mid + 1 <= index <= r:
                    update(2*i + 2, mid + 1, r)
                self.segmentTree[i] = self.segmentTree[2*i + 1] + self.segmentTree[2*i + 2]
            
        update()

    def sumRange(self, left: int, right: int) -> int:
        def query(i = 0, l = 0, r = self.n - 1):
            if right < l or r < left:
                return 0
            if left <= l and r <= right:
                return self.segmentTree[i]
            mid = (l + r)//2
            _left = query(2*i + 1, l, mid)
            _right = query(2*i + 2, mid + 1, r)
            
            return _left + _right
        return query()
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)