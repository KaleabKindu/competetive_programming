class AllOne:

    def __init__(self):
        
        self.count=defaultdict(int)
        self.min=[]
        self.max=[]
        

    def inc(self, key: str) -> None:
  
        self.count[key]+=1
        heappush(self.min, [self.count[key], key])
        heappush(self.max, [-self.count[key], key])

    def dec(self, key: str) -> None:
        self.count[key]-=1
        heappush(self.min, [self.count[key], key])
        heappush(self.max, [-self.count[key], key])

    def getMaxKey(self) -> str:
        while self.max:
            most, value = self.max[0]
            if most == 0:
                heappop(self.max)
                continue
            if self.count[value]==-most:
                return value
            heappop(self.max)
        return ''

    def getMinKey(self) -> str:
        while self.min:
            most, value=self.min[0]
            if most==0:
                heappop(self.min)
                continue
                
            if self.count[value]==most:
                return value
            heappop(self.min)
        return ''
        
