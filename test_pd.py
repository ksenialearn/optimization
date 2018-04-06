import unittest
from pd import cvt2grayscale, smooth_image_with_Gaussian_filter
from pd_updated import cvt2grayscale_v1, smooth_image_with_Gaussian_filter_v1
import numpy as np

class Test_pd_methods(unittest.TestCase):
	row, col = 756, 1008 
	testImage = np.fromfile("testImage1.raw", dtype='uint8', sep="")	
	grayImage = cvt2grayscale_v1(testImage).reshape([row, col])


	def test_cvt2grayscale_v1(self):
		testImage = self.testImage
		self.assertTrue((cvt2grayscale_v1(testImage)==cvt2grayscale(testImage)).all())
	

	def test_smooth_image_with_Gaussian_filter(self):
		grayImage = self.grayImage
		self.assertTrue((smooth_image_with_Gaussian_filter_v1(grayImage))==smooth_image_with_Gaussian_filter(grayImage))


if __name__ == '__main__':
	unittest.main()
