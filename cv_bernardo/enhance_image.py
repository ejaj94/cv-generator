import sys
import os
try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageEnhance, ImageFilter

input_path = r"C:\Users\ANGEL RAFAEL\Desktop\WhatsApp Image 2026-07-03 at 19.48.01.jpeg"
output_path = r"C:\Users\ANGEL RAFAEL\.gemini\antigravity\scratch\cv_bernardo\profile.png"

def process_image():
    if not os.path.exists(input_path):
        print(f"Error: Could not find image at {input_path}")
        return

    img = Image.open(input_path)
    
    width, height = img.size
    
    # Crop to focus on the face
    # Given the photo composition, we'll take a square crop starting slightly below the top edge
    crop_size = min(width, int(height * 0.55)) 
    left = (width - crop_size) / 2
    top = height * 0.20 # Start 20% down to avoid too much empty sky
    right = left + crop_size
    bottom = top + crop_size
    
    if bottom > height:
        bottom = height
        top = bottom - crop_size
        
    cropped_img = img.crop((left, top, right, bottom))
    
    # Enhance Image (brightness, contrast, saturation)
    # The original image is slightly washed out / backlit
    enhancer_brightness = ImageEnhance.Brightness(cropped_img)
    img_bright = enhancer_brightness.enhance(1.2)  # +20% brightness
    
    enhancer_contrast = ImageEnhance.Contrast(img_bright)
    img_contrast = enhancer_contrast.enhance(1.15)  # +15% contrast
    
    enhancer_color = ImageEnhance.Color(img_contrast)
    img_color = enhancer_color.enhance(1.2)  # +20% color/saturation
    
    # Slight sharpening to make features clearer
    img_sharp = img_color.filter(ImageFilter.SHARPEN)
    
    # Save the processed image
    img_sharp.save(output_path, "PNG")
    print(f"Success! Image processed and saved to {output_path}")

if __name__ == "__main__":
    process_image()
