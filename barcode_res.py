import cv2
from pyzbar import pyzbar
from datetime import datetime
import pandas as pd
import pygame
import time
pygame.mixer.init()
beep= r"S:\Learning\barcode\barcode\assests\beep.wav"
pygame.mixer.music.load(beep)



def play_sound():
    pygame.mixer.music.play()


def scan_barcodes():
    cap = cv2.VideoCapture(1)

    barcode_data_list = []
    timestamp_list = []

    # Load data from previous excel file
    try:
        df_existing = pd.read_excel('scanned_barcodes.xlsx')
        barcode_data_list = df_existing['Barcode'].tolist()
        timestamp_list = df_existing['Timestamp'].tolist()
    except FileNotFoundError:
        pass

    last_scan_time = time.time()

    while True:
        _, frame = cap.read()
        barcodes = pyzbar.decode(frame)
        current_time = time.time()

        for barcode in barcodes:
            if current_time - last_scan_time >= 3:
                barcode_data = barcode.data.decode("utf-8")

                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                barcode_data_list.append(barcode_data)
                timestamp_list.append(timestamp)
                play_sound()
                print(f"Barcode: {barcode_data}")
                print(f"Timestamp: {timestamp}")
                print("")
                last_scan_time = current_time

        cv2.imshow("Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    data = {'Barcode': barcode_data_list, 'Timestamp': timestamp_list}
    df = pd.DataFrame(data)
    df.to_excel('scanned_barcodes.xlsx', index=False)
    print("Data saved to scanned_barcodes.xlsx")

scan_barcodes()
