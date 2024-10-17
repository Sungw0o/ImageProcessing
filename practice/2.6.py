import cv2
import numpy as np

# 500x500 크기의 검은색 배경 영상 생성 (배경이 모두 0인 배열)
black_image = np.zeros((300, 400,), np.uint8)


# 윈도우에 영상 출력
cv2.imshow("Black Background", black_image)

# 사용자가 키를 누를 때까지 대기
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()
