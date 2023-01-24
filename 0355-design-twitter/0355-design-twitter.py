class Twitter:

    def __init__(self):
        self.post = defaultdict(list)
        self.posted = []
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append(tweetId)
        self.posted.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        answer = []
        i = len(self.posted) - 1
        while i >= 0 and len(answer) < 10:
            if self.posted[i][0] == userId:
                answer.append(self.posted[i][1])
            elif userId in self.follows[self.posted[i][0]]:
                answer.append(self.posted[i][1])
            i -= 1
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows[followeeId]:
            self.follows[followeeId].remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)