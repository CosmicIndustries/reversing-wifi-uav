import socket
import time

# Connect to the drone’s AP (IP address and port 8800)
drone_ip = "192.168.1.100"  # Update with your drone’s IP
drone_port = 8800
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_control_packet(packet):
    sock.sendto(packet, (drone_ip, drone_port))

# Define common control packets
takeoff_packet = bytearray([0x66, 0x80, 0x80, 0x80, 0x80, 0x01, 0x01, 0x02, 0x00, 0x99])  # Example: Takeoff command
landing_packet = bytearray([0x66, 0x80, 0x80, 0x80, 0x80, 0x03, 0x02, 0x03, 0x00, 0x99])  # Example: Landing command
camera_tilt_packet = bytearray([0x66, 0x80, 0x80, 0x80, 0x80, 0x04, 0x01, 0x00, 0x00, 0x99])  # Example: Camera tilt command

# Send commands
def takeoff():
    send_control_packet(takeoff_packet)
    print("Takeoff command sent.")

def land():
    send_control_packet(landing_packet)
    print("Landing command sent.")

def tilt_camera():
    send_control_packet(camera_tilt_packet)
    print("Camera tilt command sent.")

# Main loop for controlling the drone
if __name__ == "__main__":
    try:
        takeoff()
        time.sleep(5)  # Drone in air for 5 seconds
        tilt_camera()  # Adjust camera
        time.sleep(5)
        land()  # Command to land
    except KeyboardInterrupt:
        print("Manual control interrupted.")
        land()
