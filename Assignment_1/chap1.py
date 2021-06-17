import cv2


img1 = cv2.imread("blurred.jpg")

element_structure = cv2.getStructuringElement(
            shape=cv2.MORPH_RECT, ksize=(22, 3))


def preprocess(input_img):
    imgBlurred = cv2.GaussianBlur(input_img, (7, 7), 0)

    # convert to gray
    gray = cv2.cvtColor(imgBlurred,
                        cv2.COLOR_BGR2GRAY)

    # sobelX to get the vertical edges
    sobelx = cv2.Sobel(gray, cv2.CV_8U,
                       1, 0, ksize=3)
    # otsu's thresholding
    ret2, threshold_img = cv2.threshold(sobelx, 0, 255,
                                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    element = element_structure
    morph_n_thresholded_img = threshold_img.copy()
    cv2.morphologyEx(src=threshold_img,
                     op=cv2.MORPH_CLOSE,
                     kernel=element,
                     dst=morph_n_thresholded_img)

    return morph_n_thresholded_img


def extract_contours(after_preprocess):
    contours, aa = cv2.findContours(after_preprocess,
                                      mode=cv2.RETR_EXTERNAL,
                                      method=cv2.CHAIN_APPROX_SIMPLE)     #simple ====none
    return contours


after_prep = preprocess(img1)
gh = extract_contours(after_prep)
imh = cv2.drawContours(img1,gh,-1,(0,255,0),2)
cv2.imshow("ff",imh)
cv2.waitKey(0)
