class TestRunner:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self):
        passing = []
        failing = []

        for test in self.tests:

            passed = True

            try:
                print('STARTING: ' + test.name)
                if hasattr(test, 'setup'):
                    test.setup()
                test.run()
            except Exception as e:
                passed = False
                if not isinstance(e, AssertionError):
                    print('EXCEPTION: ' + str(e))

            try:
                if hasattr(test, 'cleanup'):
                    test.cleanup()
            except Exception as e:
                passed = False
                print('CLEANUP EXCEPTION: ' + str(e))

            if passed:
                passing.append(test)
            else:
                failing.append(test)

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
