import time, os
def generateQRCode(base, data, size):
    """
    Generates a QR code from the given data.
    :param data: The data to be encoded.
    :param size: The size of the QR code.
    :return: The QR code as a string.
    """
    from qrcode import QRCode
    qr = QRCode(version=1, box_size=size, border=0)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    filename = str(round(time.time() * 1000))+'.png'
    url = os.path.join(base, 'media', filename)
    img.save(url)
    return filename