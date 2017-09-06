# unittest

from Core.intermediate.super_robot1 import Robot, CleaningRobot
import unittest


class MockBot(Robot):

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append("fetching {}".format(tool))

    def move_forward(self, tool):
        self.tasks.append("forward {}".format(tool))

    def move_backward(self, tool):
        self.tasks.append("backward {}".format(tool))

    def replace(self, tool):
        self.tasks.append("replacing {}".format(tool))


class MockedCleaningRobot(CleaningRobot, MockBot):
    pass


class TestCleaningRobot(unittest.TestCase):

    def test_clean(self):
        t = MockedCleaningRobot()
        t.clean("mop")
        expected = (["fetching mop"] + ["forward mop", "backward mop"]*10 + ["replacing mop"])
        self.assertEqual(t.tasks, expected)

if __name__ == "__main__":
    unittest.main()
