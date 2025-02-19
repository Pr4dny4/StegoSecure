# 🔒StegoSecure🖼️
A Python-based image steganography tool that hides encrypted messages inside images using ROT13 and passcode protection.

## Introduction
This project implements image steganography by embedding a secret message inside an image without altering its appearance. ✨ The message is first encrypted using ROT13 🔐 and then hidden within pixel values of the image. The system also includes password protection for added security. 🔑

## Features
- **🕵️ Hidden Messaging**: Securely embeds a secret message within an image.
- **🛡️ Double Security**: Uses ROT13 encryption along with a passcode for access.
- **🖥️ User-Friendly Interface**: A simple GUI built with Tkinter for encryption and decryption.
- **⚡ Automated Processing**: Encrypts and saves the image with a single click.

## Technologies Used
- **🐍 Python**: Core programming language.
- **🖼️ OpenCV (cv2)**: Image processing and manipulation.
- **🔑 ROT13 (codecs)**: Simple encryption technique.
- **📌 Tkinter**: GUI for user interaction.
- **📂 OS Module**: File handling and execution.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/image-steganography.git
   ```
2. Navigate to the project directory:
   ```sh
   cd image-steganography
   ```
3. Install required dependencies:
   ```sh
   pip install opencv-python tkinter
   ```
4. Run the application:
   ```sh
   python steganography.py
   ```

## Usage
1. **🔏 Encrypt Message**
   - Select an image.
   - Enter a secret message and passcode.
   - Click "Encrypt Image" to hide the message in the image.

2. **🔓 Decrypt Message**
   - Enter the correct passcode.
   - The hidden message is retrieved and decrypted.

## Future Scope 🚀
- 🔐 Implement **AES encryption** for enhanced security.
- 🔍 Improve **steganographic techniques** to prevent detection.
- 🎥 Support **video and audio steganography**.
- ☁️ Enable **cloud integration** for secure storage and sharing.
- 📱 Develop a **mobile application** for real-time encryption.

## Contributing 🤝
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License 📜
This project is licensed under the MIT License.

