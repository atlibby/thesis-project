import serial
import csv
import subprocess
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def read_temp():
    result = subprocess.run(['python3', 'src/tmp102_reader.py'], capture_output=True, text=True)
    return result.stdout.strip()

with open('/home/andrew-libby/VS Code Projects/PlatformIO/Projects/keyestudio_prototype_v1/sensor data/tmp102_readings.csv', 'a') as f:
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            temp = read_temp()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer = csv.writer(f)
            writer.writerow([timestamp, line, temp])
            f.flush()