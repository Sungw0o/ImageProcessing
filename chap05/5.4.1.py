import numpy as np, cv2

# 명암도 영상 읽기
image1 = cv2.imread("images/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 차분 연산
dif_img1 = cv2.subtract(image1, image2)                     # 기본 차분 연산 (음수 고려 안 함)
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2)) # 음수 보존을 위해 16비트로 변환
abs_dif1 = np.absolute(dif_img2).astype('uint8')     # 차분 절대값, float32 스케일로 변환
abs_dif2 = cv2.absdiff(image1, image2)                      # 절대값 차분

# 관심 영역(ROI) 설정 및 출력
x, y, w, h = 100, 100, 7, 3
print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y+h, x:x+w])
print("[dif_img2(roi) int16]  = \n%s\n" % dif_img2[y:y+h, x:x+w])
print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y+h, x:x+w])
print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y+h, x:x+w])

# Matplotlib으로 이미지 출력
titles = ['image1', 'image2', 'dif_img1', 'dif_img2', 'abs_dif1', 'abs_dif2']
images = [image1, image2, dif_img1, dif_img2, abs_dif1, abs_dif2]
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)