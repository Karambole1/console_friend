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


class TestName(unittest.TestCase):
    def test_set_name(self):
        friend = ConsoleFriend()
        friend.set_name("Леня")
        self.assertEqual(friend.name, "Леня")


class TestRespond(unittest.TestCase):
    def setUp(self):
        self.friend = ConsoleFriend()

    def test_respond_how_are_you(self):
        response = self.friend.respond("как дела?")
        self.assertIn("хорошо", response.lower())

    def test_respond_about_day(self):
        response = self.friend.respond("как прошел день?")
        self.assertIn("да как обычно", response.lower())

    def test_respond_about_users_day(self):
        response = self.friend.respond("нормально")
        self.assertIn("уверен", response.lower())

    def test_bye_message(self):
        response = self.friend.respond("пока")
        self.assertIn("еще спишемся", response.lower())


if __name__ == "__main__":
    unittest.main()