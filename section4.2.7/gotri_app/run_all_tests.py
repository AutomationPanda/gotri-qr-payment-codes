from runner import TestRunner
from test_qrcodes import TestQRCodeGeneration
from test_scan_path import TestQRCodeScanPath

test_runner = TestRunner()
test_runner.add(TestQRCodeGeneration())
test_runner.add(TestQRCodeScanPath())
test_runner.run()
