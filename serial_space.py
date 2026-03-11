import argparse
import ctypes
import sys

try:
    import serial  # pyserial
except ImportError:
    print("pyserial is required. Install with: pip install pyserial", file=sys.stderr)
    sys.exit(1)

VK_SPACE = 0x20
KEYEVENTF_KEYUP = 0x0002


def send_space_key():
    """Simulate a spacebar key press on Windows using the WinAPI."""
    user32 = ctypes.windll.user32
    user32.keybd_event(VK_SPACE, 0, 0, 0)  # key down
    user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)  # key up


def listen_and_press(port: str, baudrate: int) -> None:
    """Listen on the serial port and press space when the word 'space' arrives."""
    try:
        with serial.Serial(port=port, baudrate=baudrate, timeout=1) as ser:
            print(f"Listening on {port} at {baudrate} baud. Press Ctrl+C to stop.")
            while True:
                raw = ser.readline()
                if not raw:
                    continue

                text = raw.decode(errors="ignore").strip()
                if text.lower() == "space":
                    send_space_key()
                    print("Received 'space' -> sent space key.")
    except serial.SerialException as exc:
        print(f"Serial error: {exc}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Press the space key whenever 'space' is read from the serial port."
    )
    parser.add_argument("--port", required=True, help="Serial port (e.g. COM3)")
    parser.add_argument("--baud", type=int, default=9600, help="Baud rate (default: 9600)")
    args = parser.parse_args()
    listen_and_press(args.port, args.baud)


if __name__ == "__main__":
    main()
