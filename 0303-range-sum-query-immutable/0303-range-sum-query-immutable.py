class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.n = len(nums) - 1
        self.tree = [0 for i in range(4*len(nums))]
        self.build(0, 0, self.n)
        
    def build(self,node, l, r):
        if l == r:
            self.tree[node] = self.array[l]
        else:
            mid = (l + r)//2

            self.build(2*node + 1, l, mid)
            self.build(2*node + 2, mid + 1, r)

            self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]
        

    def sumRange(self, left: int, right: int) -> int:
        def query(node = 0, l = 0, r = self.n):
            if right < l or left > r:
                return 0
            if left <= l and r <= right:
                return self.tree[node]
            mid = (l + r)//2
            _left = query(2*node + 1, l, mid)
            _right = query(2*node + 2, mid + 1, r)
            
            return _left + _right
        return query()
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)