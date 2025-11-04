import pygame
import cv2
import numpy as np 

video = cv2.VideoCapture(0)
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Face Detection App")

# Load and scale the background image
img = pygame.image.load("bg1.png").convert()
img = pygame.transform.scale(img, (800, 600))  # scale to window size

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            break  # 🟢 Stop the loop immediately

    # 🔒 prevent drawing if window closed
    if not pygame.display.get_init():
        break

    ret, frame = video.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        x1, y1 = x + w, y + h  # Bottom-right coordinates

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 1)

        # Top-left corner lines
        cv2.line(frame, (x, y), (x + 30, y), (0, 0, 255), 6)
        cv2.line(frame, (x, y), (x, y + 30), (0, 0, 255), 6)

        # Top-right corner lines
        cv2.line(frame, (x1, y), (x1 - 30, y), (0, 0, 255), 6)
        cv2.line(frame, (x1, y), (x1, y + 30), (0, 0, 255), 6)

        # Bottom-left corner lines
        cv2.line(frame, (x, y1), (x + 30, y1), (0, 0, 255), 6)
        cv2.line(frame, (x, y1), (x, y1 - 30), (0, 0, 255), 6)

        # Bottom-right corner lines
        cv2.line(frame, (x1, y1), (x1 - 30, y1), (0, 0, 255), 6)
        cv2.line(frame, (x1, y1), (x1, y1 - 30), (0, 0, 255), 6)

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    video_surface = pygame.surfarray.make_surface(imgRGB)

    font=pygame.font.Font(None, 40)
    text=font.render("FACE DETECTION: {} FACE DETECTED".format(len(faces)), True, (255, 255, 255))

    video_rect = video_surface.get_rect(center=(400, 300))
    window.blit(img, (0, 0))

    window.blit(video_surface, video_rect)
    pygame.draw.rect(window, (144,238,144), (80,20,640,70),
                     border_top_left_radius=10, border_top_right_radius=10)
    pygame.draw.rect(window, (144,238,144), (80,520,640,70),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)
    window.blit(text, (150, 40))

    pygame.display.update()
