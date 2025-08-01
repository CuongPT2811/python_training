"""
Assignment 3: Flexible Logger
"""

import datetime

def log_message(*msgs, **opts):
    """
    Flexible logger function with two parameter
    - *msgs: Accepts any number of positional string arguments, which will be joined into a single message.
    - **opts: Accepts keyword arguments for defined options:
        - timestamp (bool): If True, prepend the current time to the message.
        - file (str): If provided, write the message to the specified file; otherwise print to console.
    """
     #Join the positional arguments into a string message, seperated by spaces
    message = " ".join(msgs)

    if opts.get('timestamp') is True:
        #If opts get 'timestamp', and it's True, prepend time to message
        #[HH:MM:SS]
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")  
        message = f"[{timestamp}] {message}"

    #If opts get 'file', write the message to the specified file
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
    """Main function to test the flexible logger"""
    log_message("This is a", "test message", "by me", timestamp=True, file="log.txt")
    log_message("Another message without timestamp.", "Hey isn't it nice?", file="log.txt")
    log_message("Message", "with", "timestamp only", timestamp=True)
    log_message("Message without", "file or timestamp")

if __name__ == "__main__":
    main()