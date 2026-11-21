class Twitter:

    def __init__(self):
        from collections import deque, OrderedDict
        self.following = defaultdict(set)
        self.posts = OrderedDict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.posts.get(userId):
            self.posts[userId].append((self.time, tweetId))
        else: 
            self.posts[userId] = [(self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1

        if self.posts.get(userId): 
            feeds = [(idx, p) for idx, p in self.posts[userId]]
        else: 
            feeds = []

        fol = self.following.get(userId)
        if fol:
            for f in list(fol): 
                feeds += [(idx, p) for idx, p in self.posts[f]]

        feeds.sort(reverse=True)
        return [p for _, p in feeds[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.time += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        self.time += 1
