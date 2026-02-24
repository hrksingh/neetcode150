import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
    Twitter system that supports posting tweets, following users, and retrieving news feeds.

    Data Structures:
    - count: decreasing counter to track tweet order (earlier tweets have higher counts)
    - followMap: maps userId to set of followeeIds they follow
    - tweetMap: maps userId to list of [count, tweetId] pairs for their tweets
    """

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Post a tweet by userId with given tweetId. Decrements count to maintain order."""
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve up to 10 most recent tweets from user and all users they follow.
        Uses a min-heap to efficiently merge sorted tweet streams.
        """
        # User automatically follows themselves
        self.followMap[userId].add(userId)
        min_heap = []

        # Initialize heap with most recent tweet from each followed user
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))

        # Extract up to 10 most recent tweets using min-heap
        res = []
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            # Push next tweet from same followee if available
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """followerId starts following followeeId."""
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """followerId stops following followeeId."""
        self.followMap[followerId].discard(followeeId)


if __name__ == "__main__":
    import json

    ops = [
        "Twitter",
        "postTweet",
        "postTweet",
        "getNewsFeed",
        "getNewsFeed",
        "follow",
        "getNewsFeed",
        "getNewsFeed",
        "unfollow",
        "getNewsFeed",
    ]
    args = [[], [1, 10], [2, 20], [1], [2], [1, 2], [1], [2], [1, 2], [1]]

    results = []
    twitter: Twitter = Twitter()
    for op, a in zip(ops, args):
        if op == "Twitter":
            results.append(None)
        elif op == "postTweet":
            twitter.postTweet(a[0], a[1])
            results.append(None)
        elif op == "getNewsFeed":
            results.append(twitter.getNewsFeed(a[0]))
        elif op == "follow":
            twitter.follow(a[0], a[1])
            results.append(None)
        elif op == "unfollow":
            twitter.unfollow(a[0], a[1])
            results.append(None)

    print(json.dumps(results))
