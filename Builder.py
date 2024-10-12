import qrcode


def get_wifi_details():
    print("Let's create a QR code for your Wi-Fi network.")
    

    ssid = input("Enter your Wi-Fi SSID (network name): ")
    password = input("Enter your Wi-Fi password: ")
    encryption = input("Enter your Wi-Fi encryption type (WPA, WPA2, WEP, or NONE): ").upper()

    if encryption not in ["WPA", "WPA2", "WEP", "NONE"]:
        print("Invalid encryption type. Please use one of the following: WPA, WPA2, WEP, NONE.")
        return None, None, None

    return ssid, password, encryption


def generate_wifi_qr_string(ssid, password, encryption):
    if encryption == "NONE":
        qr_data = f"WIFI:T:;S:{ssid};;"
    else:
        qr_data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    
    return qr_data


def generate_qr_code_image(qr_data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)


    img = qr.make_image(fill='black', back_color='white')
    img_file = "wifi_qr_code.png"
    img.save(img_file)

    return img_file


def generate_wifi_qr():
    ssid, password, encryption = get_wifi_details()
    
    if not ssid or not encryption:  
        print("Failed to generate QR code due to invalid input.")
        return

    qr_data = generate_wifi_qr_string(ssid, password, encryption)
    
 
    img_file = generate_qr_code_image(qr_data)
    print(f"Wi-Fi QR code generated and saved as {img_file}")


if __name__ == "__main__":
    generate_wifi_qr()
