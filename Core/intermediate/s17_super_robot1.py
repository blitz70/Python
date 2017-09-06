class Robot:

    def fetch(self, tool):
        print("Physical movement! Fetching.")

    def move_forward(self, tool):
        print("Physical movement! Moving forward.")

    def move_backward(self, tool):
        print("Physical movement! Moving backward.")

    def replace(self, tool):
        print("Physical movement! Replacing.")


class CleaningRobot(Robot):

    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)

if __name__ == "__main__":
    CleaningRobot().clean("broom")
