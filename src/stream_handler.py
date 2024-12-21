import socket
import cv2
import numpy as np

# Connect to the drone’s video stream (UDP port 1234)
drone_ip = 192.168.1.100  # Update with your drone’s IP
video_port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to handle and display the video stream
def handle_video_stream():
    print("Starting video stream...")
    while True:
        # Receive the video stream packet
        data, _ = sock.recvfrom(65536)  # Adjust buffer size as needed
        # Assuming the data is in H264 format or another compressed format
        frame = np.frombuffer(data, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        
        if frame is not None:
            cv2.imshow("Drone Video Stream", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        handle_video_stream()
    except KeyboardInterrupt:
        print("Video stream interrupted.")
