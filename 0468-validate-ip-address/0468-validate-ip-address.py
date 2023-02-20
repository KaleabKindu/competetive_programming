class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(s):
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or int(part) > 255 or (len(part) > 1 and part[0] == '0'):
                    return False
            return True
        
        def is_valid_ipv6(s):
            parts = s.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not part or len(part) > 4 or not all(c in string.hexdigits for c in part):
                    return False
            return True
        
        if is_valid_ipv4(queryIP):
            return "IPv4"
        elif is_valid_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
#         if '.' in queryIP:
#             nums=queryIP.split('.')
#             for num in nums:
#                 if num[0] == '0' or not 0 <= int(num) <= 255:
#                     return "Neither"
#             return 'IPv4'
            
#         else:
#             nums = queryIP.split(':')
#             for num in nums:
#                 alpha = True
#                 for char in num:
#                     if not char.isalnum():
#                         alpha = False
#                 if not 1 <= len(num) <= 4 or not alpha:
#                     return 'Neither'
#             return 'IPv6'