# def sim_karta(n):
#     print(n)
#     if n==90 or n==91:
#         return 'Beeline'
#     elif n==89 or n==88:
#         return 'Uzmobile'
#     elif n==94 or n==95:
#         return 'Usell'
# n=input()
# k=int(n[4:6])
# print(sim_karta(k))



# n=input()
# k=n[:2]
# d={
#     '01':"Toshkent",
#     '10':"Navoiy",
#     '11':"Andijon",
#     '70':"Namangan",
#     '55':"Qashqadaryo",
#     '44':"Surxandaryo",
#     '33':"Buxoro",
#     '22':"Samarqand",
#     '98':"Xorazm",
# }
# print(d[k])
mplayer -vo caca 'https://youtu.be/xEQYL1tplnY?list=RDMMxEQYL1tplnY'
mpv --vo=caca 'https://youtu.be/xEQYL1tplnY?list=RDMMxEQYL1tplnY'





import cv2

# Video faylini o‘qing
video_path = 'video13.mp4'  # Bu yerga o‘zingizning video faylingiz nomini qo‘ying
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video faylini ochib bo'lmadi!")
    exit()

# Video oynasi uchun nom
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Har bir kadrni ko'rsatish
    cv2.imshow('Video', frame)

    # 'q' tugmasini bosish orqali video to'xtatiladi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Resurslarni tozalash
cap.release()
cv2.destroyAllWindows()



