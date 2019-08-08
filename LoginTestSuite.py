import unittest
from LoginUnitTest import LoginUnitTest
import HtmlTestRunner
import os

dir = os.getcwd()
loginUnitTest = unittest.TestLoader().loadTestsFromTestCase(LoginUnitTest)
test_suite = unittest.TestSuite([loginUnitTest])
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)

# run the suite using HTMLTestRunner
runner.run(test_suite)