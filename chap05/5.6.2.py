import numpy as np, cv2


# 회전할 라디안 각도 계산
theta = 20 * np.pi / 180 # 20도를 라디안으로 변환
rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]], np.float32)  # 넘파이 행렬 생성, 회전 행렬

# 좌표 설정
pts1 = np.array([(250, 30), (400, 70),
                 (350, 250), (150, 200)], np.float32)

# 좌표 회전, 회전 행렬을 전치 행렬로 사용하여 좌표를 회전함
pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T)

# 좌표 출력 원래 좌표와 회전된 좌표를 쌍으로 출력
for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pts2[%d] = %s" % (i, pt1, i, pt2))

# 영상 생성 및 4개의 좌표 그리기
image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)  # 원래 좌표
cv2.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 3)  # 회전된 좌표

cv2.imshow('image', image)
cv2.waitKey(0)

# 원래의 좌표와 20도 회전된 좌표 간의 차이를 시각적으로 보여줌