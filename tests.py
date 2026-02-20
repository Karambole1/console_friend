import unittest
from friend import ConsoleFriend


class TestFriendCreation(unittest.TestCase):
    def test_friend_can_be_created(self):
        friend = ConsoleFriend()
        self.assertIsNotNone(friend)


if __name__ == "__main__":
    unittest.main()