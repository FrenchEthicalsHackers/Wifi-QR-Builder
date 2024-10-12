
# Wi-Fi QR Code Generator

This Python script creates a QR code for your Wi-Fi credentials. Simply input your SSID, password, and encryption type, and it generates a QR code image (`wifi_qr_code.png`) that others can scan to connect to your Wi-Fi network easily.

## Features
- Supports WPA, WPA2, WEP, or no encryption.
- Saves the QR code as an image file.

## Requirements
- Python 3.x
- `qrcode` library (installable via pip)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/FrenchEthicalsHackers/Wifi-QR-Builder.git
   cd Wifi-QR-Builder
   ```
2. Install the required library:
   ```bash
   pip install qrcode
   pip install Pillow
   ```
3. Run the script:
   ```bash
   python Builder.py
   ```
4. Enter your Wi-Fi details when prompted. The QR code will be saved as `wifi_qr_code.png`.

## License
This project is licensed under the MIT License.
