import cv2

src1 = cv2.imread('./dog1.jpeg')
src2 = cv2.imread('./dog2.jpeg')
src3 = cv2.imread('./dog3.jpeg')

# 이미지 보여주기
# cv2.imshow('dog1', src1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(src1.shape)


# 잘라내기
# dst = src1[50:100, 50:100]
# cv2.imshow('dog1', src1)
# cv2.imshow('dog', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 사이즈
# 비율 안깨지게 height
# height = int((100*src1.shape[0]) / src1.shape[1])
# size = (100, height)

# dst = cv2.resize(src1, size)

# cv2.imshow('dog1', src1)
# cv2.imshow('scaling', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 다른 파일로 저장하기
# height = int((100*src1.shape[0]) / src1.shape[1])
# size = (100, height)

# dst = cv2.resize(src1, size)
# cv2.imwrite('cuteDog.jpeg', dst)


# 컬러 이미지를 회색조로 변경하기
# img_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


