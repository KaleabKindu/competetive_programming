class Solution:
    def simplifyPath(self, path: str) -> str:
        path = "/".join(path.split('//'))
        path = path.split('/')
        spath = []
        for directory in path:
            if directory == '..':
                if spath: spath.pop()
                continue
            elif directory != '.' and directory != '':
                spath.append(directory)
        
        return '/' + "/".join(spath)