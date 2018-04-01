import unittest
from pd import cvt2grayscale
from pd_updated import cvt2grayscale_v1
import numpy as np

class Test_pd_methods(unittest.TestCase):


	def test_cvt2grayscale_v1(self):
		testImage = np.fromfile("testImage1.raw", dtype='uint8', sep="")
		self.assertTrue((cvt2grayscale_v1(testImage)==cvt2grayscale(testImage)).all())

if __name__ == '__main__':
	unittest.main()
