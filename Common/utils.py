import numpy as np, cv2

def print_matInfo(name, image):  # 행렬 정보 출력 함수
    if image.dtype == 'uint8':
        mat_type = 'CV_8U'
    elif image.dtype == 'int8':
        mat_type = 'CV_8S'
    elif image.dtype == 'uint16':
        mat_type = 'CV_16U'
    elif image.dtype == 'int16':
        mat_type = 'CV_16S'
    elif image.dtype == 'float32':
        mat_type = 'CV_32F'
    elif image.dtype == 'float64':
        mat_type = 'CV_64F'

    nchannel = 3 if image.ndim == 3 else 1

    # depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))


# def put_string(frame, text, pt, value, color=(120, 200, 90)):  # 문자열 출력 함수 - 그림자 효과
#     text += str(value)
#     shade = (pt[0] + 2, pt[1] + 2)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)   # 그림자 효과
#     cv2.putText(frame, text, pt, font,0.7, color,2)
#
#
# capture = cv2.VideoCapture(0)  # 0번 카메라 연결
#
#
# if capture.isOpened() == False:
#     raise Exception("카메라 연결 안됨")

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