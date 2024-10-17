import numpy as np, cv2

def make_palette(rows):
    hue = np.arange(0, rows) * 180 / rows  # hue 값 리스트 계산
    hsv = [[(h, 255, 255)] for h in hue]    # (hue, 255, 255) 화소값 계산
    hsv = np.array(hsv, np.uint8)           # numpy 행렬의 uint8형 변환
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  # HSV 컬러 -> BGR 컬러

def draw_histo_hue(hist, shape=(200, 360, 3)):
    hsv_palette = make_palette(hist.shape[0])  # 색상 팔레트 생성
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)  # 정규화

    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        color = tuple(map(int, hsv_palette[i][0]))  # 정수형 튜플로 변환
        cv2.rectangle(hist_img, (x, 0, w, int(h)), color, cv2.FILLED)  # 팔레트 색으로 그리기

    return cv2.flip(hist_img, 0)  # 상하 반전

# 이미지 읽기
image = cv2.imread("images/hue_hist.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# BGR 컬러 -> HSV 컬러
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Hue 채널 히스토그램 계산
hue_hist = cv2.calcHist([hsv_img], [0], None, [18], [0, 180])
# 히스토그램 그래프 생성
hue_hist_img = draw_histo_hue(hue_hist, (200, 360, 3))

cv2.imshow("image",image)
cv2.imshow("hue_hist",hue_hist_img)
cv2.waitKey(0)