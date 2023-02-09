class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(' ')
        answer = []
        answer.append(date[-1])
        month = {"Jan":'01', "Feb":'02', "Mar":'03',
                 "Apr":'04', "May":'05', "Jun":'06',
                 "Jul":'07', "Aug":'08', "Sep":'09', 
                 "Oct":'10', "Nov":'11', "Dec":'12'}
        answer.append(month[date[1]])
        
        if len(date[0]) == 4:
            answer.append(date[0][0:2])
        else:
            answer.append('0' + date[0][0])
        return "-".join(answer)