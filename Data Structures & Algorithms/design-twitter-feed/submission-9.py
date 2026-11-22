class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = self.posts[userId][-10:]

        fol = self.following.get(userId)
        if fol:
            for f in list(fol): 
                feeds += self.posts[f][-10:]

        feeds.sort(reverse=True)
        return [p for _, p in feeds[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: 
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: 
            self.following[followerId].discard(followeeId)
