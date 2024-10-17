import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)  # 흰색 배경의 히스토그램 이미지 생성
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)  # 히스토그램 정규화
    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))  # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h))  # 사각형 영역
        cv2.rectangle(hist_img, roi, 150, -1)  # 히스토그램 막대 그리기
        cv2.rectangle(hist_img, roi, 0, 1)  # 막대 경계 그리기

    return cv2.flip(hist_img, 0)  # 영상 상하 뒤집기 후 반환