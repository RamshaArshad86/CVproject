import cv2

"""
This method take image filename in parameter and return the 2d array
"""

def image_reader(filename):
    """

    :param filename: image name ex: .png jpg
    :return : the 2d array
    """
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    return image
"""
This method apply bilateral filter on image matrix and save as a result image

"""
def bilateral_filter(image_matrix):
    """

    :param image_matrix: the read image in the form of matrx
    :return:
    """
    Windowname="After Bilateral Filter"
    #-------------- bilateralFilter is applied on the image
    filtered1 = cv2.bilateralFilter(src=image_matrix,d=5,sigmaColor=20,sigmaSpace=30)
    #----------------------- Display as well as write the imae--------------------#
    cv2.imshow(Windowname,filtered1)
    cv2.imwrite("result.png",filtered1)
    #-------Close while press any key----------#
    cv2.waitKey(0)
    cv2.destroyWindow(Windowname)


if __name__ == '__main__':
    filename="test.png"
    reader=image_reader(filename)
    bilateral_filter(reader)
+











































+