from qrcode.console_scripts import error_correction
from PIL import Image, ImageDraw


def QRKodDosyasıOlustur(veri,dosyaAdı):
    import qrcode
    qr=qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 12,
        border = 4,
    )
    qr.add_data(veri)
    qr.make(fit=True)

    img=qr.make_image()
    img.save(dosyaAdı)

veri = "Bu kitap ile Python programlama öğrenilir."
QRKodDosyasıOlustur(veri,"karekod.jpg")