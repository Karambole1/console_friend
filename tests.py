import unittest
from friend import ConsoleFriend


class TestFriendCreation(unittest.TestCase):
    def test_friend_can_be_created(self):
        friend = ConsoleFriend()
        self.assertIsNotNone(friend)


class TestGreeting(unittest.TestCase):
    def test_greet_returns_string(self):
        friend = ConsoleFriend()
        self.assertEqual(friend.greet(), "я твой консольный друг, привет)")


if __name__ == "__main__":
    unittest.main()