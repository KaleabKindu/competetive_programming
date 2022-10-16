class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip = [char for char in s]
        n = len(ip)
        answer = set()
        path = []
        def bk(i = 0):
            if i >= n:
                if len(path) == 4:
                    answer.add('.'.join(path))
                return
            for j in range(1,4):
                bit = "".join(ip[i: i + j])
                if 0 <= int(bit) <= 255 and len(bit) == len(str(int(bit))):
                    path.append(bit)
                    bk(i + j)
                    path.pop()
        bk()       
        return answer
            
                
        