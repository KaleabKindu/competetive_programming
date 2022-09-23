class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        files = defaultdict(list)
        for path in paths:
            temp = path.split(' ')
            root = temp[0]
            for file in temp[1:]:
                tmp = file.split('(')
                files[tmp[-1][:-1]].append(str(root) +'/'+ str(tmp[0]))
        return [files[key] for key in files if len(files[key]) > 1]