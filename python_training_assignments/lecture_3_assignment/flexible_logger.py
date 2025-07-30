"""
Assignment 3: Flexible Logger
"""

import datetime

def log_message(*msgs, **opts):
    message = " ".join(msgs)

    if opts.get('timestamp') is True:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] {message}"

    file_path = opts.get('file')
    if file_path:
        try:
            with open(file_path, 'a') as file:
                file.write(message + "\n")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
    else:
        print(message)

def main():
    """Main function to test the flexible logger."""
    log_message("This is a test message by me", timestamp=True, file="log.txt")
    log_message("Another message without timestamp", file="log.txt")
    log_message("Message with timestamp only", timestamp=True)
    log_message("Message without file or timestamp")

if __name__ == "__main__":
    main()