import cv2
from pyzbar import pyzbar
from datetime import datetime
import pandas as pd

def scan_barcodes():
    cap = cv2.VideoCapture(1)
    scanned_barcodes = set()

    barcode_data_dict = []
    timestamp_list= []

    try:
        df_existing= pd.read_excel('scanned_barcode.xlsx')
        barcode_data_list= df_existing['Barcode'].tolist()
        timestamp_list= df_existing['Timestamp'].tolist()
    except FileNotFoundError:
        pass

    while True:
        _, frame = cap.read()
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            if barcode_data not in scanned_barcodes:
                scanned_barcodes.add(barcode_data)
            
            #if barcode_data not in barcode_data_dict:
               # barcode_data_dict[barcode_data]= pd.DataFrame(columns=['Timestamp'])

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            barcode_data_list.append(barcode_data)
            timestamp_list.append(timestamp)
                        
            new_row={'Timestamp': timestamp ,'Employee Name':barcode_data}
            barcode_data_dict[barcode_data] = pd.concat([ barcode_data_dict[barcode_data],pd.DataFrame([new_row])], ignore_index= True)


            print(f"Barcode: {barcode_data}")
            print(f"Timestamp: {timestamp}")
            print(f"Type: {barcode_type}")
            print("")


        cv2.imshow("Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    df_combined = pd.concat(barcode_data_dict.values(), ignore_index = True)
    
    df_combined.to_excel ('scaned_barcode.xlsx', index=False)
    print("Data saved to scanned_barcode.xlsx")

scan_barcodes()
pygame.mixer.init()
beep= r"S:\Learning\barcode\barcode\assests\beep.wav"
pygame.mixer.music.load(beep)



            