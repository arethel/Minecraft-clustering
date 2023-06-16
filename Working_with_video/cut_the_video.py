import cv2
import os
import time

def save_frames(video_path, output_folder, start_frame):
    # Проверка и создание папки для сохранения кадров
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Загрузка видео файла
    video_capture = cv2.VideoCapture(video_path)
    
    print(video_capture.isOpened())
    # Инициализация переменных
    frame_count = start_frame
    frame_interval = 3  # Интервал сохранения кадров (в секундах)
    last_save_time = 0

    while True:
        # Чтение текущего кадра
        ret, frame = video_capture.read()
        # Проверка наличия кадра
        if not ret:
            break

        video_capture.set(cv2.CAP_PROP_POS_MSEC, last_save_time*1000)
        filename = f"frame_{frame_count}.jpg"
        filepath = os.path.join(output_folder, filename)
        # Сохранение кадра в файл
        cv2.imwrite(filepath, frame)
        print(f"Saved frame {frame_count}")
        
        last_save_time+=frame_interval
        # Обновление переменных
        frame_count += 1

        # Получение текущего времени
        # current_second = int(video_capture.get(cv2.CAP_PROP_POS_MSEC) // 1000)
        
        # # Проверка интервала сохранения кадров
        # if current_second - last_save_time >= frame_interval:
            
        #     # Формирование имени файла
        #     filename = f"frame_{frame_count}.jpg"
        #     filepath = os.path.join(output_folder, filename)

        #     # Сохранение кадра в файл
        #     cv2.imwrite(filepath, frame)
        #     print(f"Saved frame {frame_count}")

        #     # Обновление переменных
        #     frame_count += 1
        #     last_save_time = current_second

    # Освобождение ресурсов
    video_capture.release()
    return frame_count

# Пример использования
video_path = "Working_with_video/videos/new/videoplayback ("
output_folder = "Working_with_video/cutted_pics"

st_frame = 9651
i = 6
while i <=12:
    st_frame = save_frames(video_path+ str(i)+").mp4", output_folder, st_frame)
    i+=1

