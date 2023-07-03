import cv2
from pyzbar import pyzbar
from datetime import datetime
import pandas as pd
import pygame
import time

# Initialize the pygame mixer
pygame.mixer.init()
beep= r"S:\Learning\barcode\barcode\assests\beep.wav"
pygame.mixer.music.load(beep)



def play_sound():
    # Play the sound file
    pygame.mixer.music.play()


def scan_barcodes():
    # Initialize the video capture device
    cap = cv2.VideoCapture(1)

    barcode_data_list = []
    timestamp_list = []

    # Load existing data from the Excel file, if it exists
    try:
        df_existing = pd.read_excel('scanned_barcodes.xlsx')
        barcode_data_list = df_existing['Barcode'].tolist()
        timestamp_list = df_existing['Timestamp'].tolist()
    except FileNotFoundError:
        pass

    last_scan_time = time.time()

    while True:
        # Read a frame from the video capture
        _, frame = cap.read()

        # Find and decode barcodes in the frame
        barcodes = pyzbar.decode(frame)

        current_time = time.time()

        for barcode in barcodes:
            # Check if enough time has passed since the last scan
            if current_time - last_scan_time >= 3:
                # Extract the barcode data from the decoded object
                barcode_data = barcode.data.decode("utf-8")

                # Generate a timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Append the barcode data and timestamp to the respective lists
                barcode_data_list.append(barcode_data)
                timestamp_list.append(timestamp)

                # Play the sound
                play_sound()

                # Print the barcode data and timestamp
                print(f"Barcode: {barcode_data}")
                print(f"Timestamp: {timestamp}")
                print("")

                # Update the last scan time
                last_scan_time = current_time

        # Display the frame
        cv2.imshow("Barcode Scanner", frame)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture device and close windows
    cap.release()
    cv2.destroyAllWindows()

    # Create a DataFrame from the barcode data and timestamp lists
    data = {'Barcode': barcode_data_list, 'Timestamp': timestamp_list}
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel('scanned_barcodes.xlsx', index=False)
    print("Data saved to scanned_barcodes.xlsx")

# Call the function to start scanning barcodes
scan_barcodes()
