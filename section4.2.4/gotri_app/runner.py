class TestRunner:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self):
        for test in self.tests:
            test.run()
