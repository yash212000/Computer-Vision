# import matplotlib.pylab as plt
# import cv2
# import numpy as np
#
#
# def region_of_interest(img, vertices):
#     mask = np.zeros_like(img)
#     # channel_count = img.shape[2]
#     match_mask_color = 255
#     cv2.fillPoly(mask, vertices, match_mask_color)
#     masked_image = cv2.bitwise_and(img, mask)
#     return masked_image
#
#
# def draw_the_lines(img, lines):
#     img = np.copy(img)
#     blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
#
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)
#
#     img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
#     return img
#
#
# image = cv2.imread('road.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# print(image.shape)
# height = image.shape[0]
# width = image.shape[1]
# region_of_interest_vertices = [
#     (0, height),
#     (width / 2, height / 2),
#     (width, height)
# ]
# gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# canny_image = cv2.Canny(gray_image, 100, 200)
# cropped_image = region_of_interest(canny_image,
#                                    np.array([region_of_interest_vertices], np.int32), )
# lines = cv2.HoughLinesP(cropped_image,
#                         rho=6,
#                         theta=np.pi / 180,
#                         threshold=160,
#                         lines=np.array([]),
#                         minLineLength=40,
#                         maxLineGap=25)
# image_with_lines = draw_the_lines(image, lines)
# plt.imshow(image_with_lines)
# plt.show()



# import cv2
# import dlib
# from scipy.spatial import distance
#
#
# def calculate_EAR(eye):
#     A = distance.euclidean(eye[1], eye[5])
#     B = distance.euclidean(eye[2], eye[4])
#     C = distance.euclidean(eye[0], eye[3])
#     ear_aspect_ratio = (A + B) / (2.0 * C)
#     return ear_aspect_ratio
#
#
# cap = cv2.VideoCapture(0)
# hog_face_detector = dlib.get_frontal_face_detector()
# dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#
# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     faces = hog_face_detector(gray)
#     for face in faces:
#
#         face_landmarks = dlib_facelandmark(gray, face)
#         leftEye = []
#         rightEye = []
#
#         for n in range(36, 42):
#             x = face_landmarks.part(n).x
#             y = face_landmarks.part(n).y
#             leftEye.append((x, y))
#             next_point = n + 1
#             if n == 41:
#                 next_point = 36
#             x2 = face_landmarks.part(next_point).x
#             y2 = face_landmarks.part(next_point).y
#             cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
#
#         for n in range(42, 48):
#             x = face_landmarks.part(n).x
#             y = face_landmarks.part(n).y
#             rightEye.append((x, y))
#             next_point = n + 1
#             if n == 47:
#                 next_point = 42
#             x2 = face_landmarks.part(next_point).x
#             y2 = face_landmarks.part(next_point).y
#             cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
#
#         left_ear = calculate_EAR(leftEye)
#         right_ear = calculate_EAR(rightEye)
#
#         EAR = (left_ear + right_ear) / 2
#         EAR = round(EAR, 2)
#         if EAR < 0.26:
#             cv2.putText(frame, "DROWSY", (20, 100),
#                         cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
#             cv2.putText(frame, "Are you Sleepy?", (20, 400),
#                         cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
#             print("Drowsy")
#         print(EAR)
#
#     cv2.imshow("Are you Sleepy", frame)
#
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()
# import cv2
# import dlib
# from scipy.spatial import distance
#
#
# def calculate_EAR(eye):
#     A = distance.euclidean(eye[1], eye[5])
#     B = distance.euclidean(eye[2], eye[4])
#     C = distance.euclidean(eye[0], eye[3])
#     ear_aspect_ratio = (A + B) / (2.0 * C)
#     return ear_aspect_ratio
#
#
# cap = cv2.VideoCapture(0)
# hog_face_detector = dlib.get_frontal_face_detector()
# dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#
# while True:
#     _, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     faces = hog_face_detector(gray)
#     for face in faces:
#
#         face_landmarks = dlib_facelandmark(gray, face)
#         leftEye = []
#         rightEye = []
#
#         for n in range(36, 42):
#             x = face_landmarks.part(n).x
#             y = face_landmarks.part(n).y
#             leftEye.append((x, y))
#             next_point = n + 1
#             if n == 41:
#                 next_point = 36
#             x2 = face_landmarks.part(next_point).x
#             y2 = face_landmarks.part(next_point).y
#             cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
#
#         for n in range(42, 48):
#             x = face_landmarks.part(n).x
#             y = face_landmarks.part(n).y
#             rightEye.append((x, y))
#             next_point = n + 1
#             if n == 47:
#                 next_point = 42
#             x2 = face_landmarks.part(next_point).x
#             y2 = face_landmarks.part(next_point).y
#             cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
#
#         left_ear = calculate_EAR(leftEye)
#         right_ear = calculate_EAR(rightEye)
#
#         EAR = (left_ear + right_ear) / 2
#         EAR = round(EAR, 2)
#         if EAR < 0.26:
#             cv2.putText(frame, "DROWSY", (20, 100),
#                         cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
#             cv2.putText(frame, "Are you Sleepy?", (20, 400),
#                         cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
#             print("Drowsy")
#         print(EAR)
#
#     cv2.imshow("Are you Sleepy", frame)
#
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()