class TestRunner:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self):
        passing = []
        failing = []

        for test in self.tests:
            try:
                print('STARTING: ' + test.name)
                test.run()
                passing.append(test)
            except Exception as e:
                failing.append(test)
                if not isinstance(e, AssertionError):
                    print('EXCEPTION: ' + str(e))

        print()
        print('=== Test Result Summary ===')

        for test in passing:
            print('PASS: ' + test.name)
        for test in failing:
            print('FAIL: ' + test.name)

        pass_total = len(passing)
        fail_total = len(failing)
        total = pass_total + fail_total

        print(f'{pass_total} PASS, {fail_total} FAIL, {total} TOTAL')