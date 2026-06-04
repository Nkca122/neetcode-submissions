import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.count = 0  # Acts as a progressive timestamp
        self.userTweets = {}  # userId -> list of (timestamp, tweetId)
        self.userFollows = {}  # followerId -> set of followeeIds
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        # Store positive count. Larger count = more recent tweet
        self.userTweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []  # This will act as a Min-Heap of size 10

        # Gather all users to check (the user themselves + their followees)
        # Using set() as default to match the data structure type
        users = [userId, *(self.userFollows.get(userId, set()))]
        
        for user in users:
            if user in self.userTweets:
                # We only need to look at the last 10 tweets of each user
                for count, tweetId in self.userTweets[user][-10:]:
                    if len(newsFeed) < self.limit:
                        heapq.heappush(newsFeed, (count, tweetId))
                    else:
                        # If the current tweet is NEWER than the oldest in our heap
                        if count > newsFeed[0][0]:
                            heapq.heappop(newsFeed)
                            heapq.heappush(newsFeed, (count, tweetId))
        
        # Pop elements out of the heap (comes out oldest to newest)
        result = []
        while newsFeed:
            result.append(heapq.heappop(newsFeed)[1])
            
        # Reverse the result so the newest tweets are at the front
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.userFollows:
            self.userFollows[followerId] = set()
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows:
            self.userFollows[followerId].discard(followeeId)