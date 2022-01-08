class RecentCounter:

    def __init__(self):
        self.req=[]

    def ping(self, t: int) -> int:
        self.req.append(t)
        while len(self.req)!=0 and t - self.req[0] > 3000:
            self.req.pop(0)
            
        return len(self.req)
