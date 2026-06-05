class Twitter:
        def __init__(self):
            self.user_to_tweets = collections.defaultdict(list)
            self.user_to_followers = collections.defaultdict(set)
            self.UserTweet = collections.namedtuple("UserTweet", ["ts", "tweetId"])
            self.ts = 0

        def postTweet(self, userId: int, tweetId: int) -> None:
            user_tweet = self.UserTweet(ts=self.ts, tweetId=tweetId)
            self.user_to_tweets[userId].append(user_tweet)
            self.ts += 1

        def getNewsFeed(self, userId: int) -> List[int]:
            h = []
            curr_followers = self.user_to_followers[userId]

            all_userids = set()
            all_userids.add(userId)
            all_userids.update(curr_followers)

            # for userid in all users:
            # fetch their tweets
            # for userid's post dump into a pq sorted on ts in a MIN heap
            # if the len of MIN heap > 10, poll
            for userid in all_userids:
                all_tweets = self.user_to_tweets[userid]
                for tweet in all_tweets:
                    heapq.heappush(h, (tweet.ts, tweet.tweetId))
                    if len(h) > 10:
                        heapq.heappop(h)
            
            # once done with all users, the pq will contain all 10 most recent tweetids
            res = []
            while h:
                _, tweetid = heapq.heappop(h)
                res.append(tweetid)
            
            #return those as a list
            res.reverse() #O(n) in place
            return res

        def follow(self, followerId: int, followeeId: int) -> None:
            self.user_to_followers[followerId].add(followeeId)
            return None

        def unfollow(self, followerId: int, followeeId: int) -> None:
            current_followees = self.user_to_followers[followerId]
            if current_followees:
                current_followees.remove(followeeId)
            return None