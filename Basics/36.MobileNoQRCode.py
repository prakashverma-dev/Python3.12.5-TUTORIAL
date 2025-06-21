import qrcode
from PIL import Image, ImageDraw, ImageFont

# Your mobile number
mobile_number = "+911234567890"
qr_data = f"tel:{mobile_number}"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Add label below QR
# Define font and size
try:
    font = ImageFont.truetype("arial.ttf", 20)  # Windows usually has this
except IOError:
    font = ImageFont.load_default()  # Fallback for non-Windows

# Calculate new image size to fit text
text = mobile_number
text_width, text_height = font.getsize(text)

# Create new image with extra space for text
new_img_height = qr_img.size[1] + text_height + 10
new_img = Image.new("RGB", (qr_img.size[0], new_img_height), "white")

# Paste the QR code onto new image
new_img.paste(qr_img, (0, 0))

# Draw text centered below QR
draw = ImageDraw.Draw(new_img)
text_x = (qr_img.size[0] - text_width) // 2
text_y = qr_img.size[1] + 5
draw.text((text_x, text_y), text, font=font, fill="black")

# Save or display the result
new_img.save("mobile_qr_with_label.png")
new_img.show()
