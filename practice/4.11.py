import cv2

# 컬러 이미지 파일 읽기 (예시: 'input_image.jpg' 파일)
image = cv2.imread('input_image.jpg', cv2.IMREAD_COLOR)

# 파일이 제대로 읽혔는지 확인
if image is None:
    print("파일을 읽을 수 없습니다.")
else:
    # JPEG 형식으로 저장 (최고 화질: 품질 100)
    cv2.imwrite('test.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print("test.jpg 파일이 저장되었습니다 (최고 화질).")

    # PNG 형식으로 저장 (최고 압축: 압축 레벨 0)
    cv2.imwrite('test.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print("test.png 파일이 저장되었습니다 (최고 화질).")
