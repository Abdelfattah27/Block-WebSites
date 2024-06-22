# Website Blocker

This project allows you to block any website by adding it to the hosts file, making it unreachable. The application is built using Python and Tkinter for the graphical user interface (GUI). The project is packaged into an executable file using PyInstaller.

## Features

- Block any website by entering its URL or hostname.
- Simple and user-friendly GUI.
- Provides feedback for successful or failed operations.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## How to Use

### Running the Executable

1. Download the executable file from the `dist` folder.
2. Run the executable file (`filter.exe`) **as administrator**.
3. Enter the URL or hostname of the website you want to block in the input field.
4. Click on the "Block Website" button.

### Running from Source

1. Clone the repository.
2. Install the required packages:
    ```sh
    pip install tk
    ```
3. Run the script from cmd as administrator:
    ```sh
    python filter.py
    ```

## Packaging the Application

To create an executable file, you can use PyInstaller. Follow these steps:

1. Install PyInstaller:
    ```sh
    pip install pyinstaller
    ```
2. Run PyInstaller with the following command:
    ```sh
    pyinstaller --onefile --windowed filter.py
    ```
3. The executable file will be created in the `dist` folder.

## Code Explanation

### Main Functions

- **is_valid_hostname(hostname)**: Validates the hostname.
- **add_to_hosts(address, ip_address="192.168.1.1", initial=False)**: Adds the specified address to the hosts file.
- **on_submit()**: Handles the submission of the input address.

### GUI Setup

- The GUI is created using Tkinter, with a simple design for entering the URL/hostname and blocking it.

## Note

- This program requires administrative privileges to modify the hosts file. Run the program as an administrator.
- The default IP address used for blocking is `192.168.1.1`. You can change it as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
