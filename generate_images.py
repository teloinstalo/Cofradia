from PIL import Image, ImageEnhance
import os

BASE_DIR = "/home/juanjo/Documentos/1/35/web-cofradia"
IMG_OUT = os.path.join(BASE_DIR, "img")
os.makedirs(IMG_OUT, exist_ok=True)

# Load base images
icono = Image.open(os.path.join(BASE_DIR, "Icono.png")).convert("RGBA")
productos = Image.open(os.path.join(BASE_DIR, "productos1.jpeg")).convert("RGB")

def resize_logo(img, size):
    img_resized = img.copy()
    img_resized.thumbnail((size, size), Image.Resampling.LANCZOS)
    square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    x = (size - img_resized.width) // 2
    y = (size - img_resized.height) // 2
    square.paste(img_resized, (x, y), img_resized)
    return square

# Logo variants
logo_configs = [
    ("favicon.png", 32),
    ("logo-50.png", 50),
    ("logo-60.png", 60),
    ("logo-120.png", 120),
    ("logo-200.png", 200),
]

for name, size in logo_configs:
    out = resize_logo(icono, size)
    out_path = os.path.join(IMG_OUT, name)
    out.save(out_path)
    print(f"Created {out_path} ({size}x{size})")

# Product images with slight variations
product_configs = [
    ("prod-camiseta.jpg", None, None),   # original
    ("prod-taza.jpg", 0.9, None),        # slightly darker
    ("prod-llavero.jpg", 1.15, None),    # slightly brighter
    ("prod-postal.jpg", None, 1.2),      # higher contrast
    ("prod-pulsera.jpg", 0.85, 1.3),     # darker and more contrast
    ("prod-medalla.jpg", 1.1, 1.1),      # brighter + contrast
]

prod_base = productos.resize((400, 400), Image.Resampling.LANCZOS)

for name, brightness_factor, contrast_factor in product_configs:
    img = prod_base.copy()
    if brightness_factor is not None:
        img = ImageEnhance.Brightness(img).enhance(brightness_factor)
    if contrast_factor is not None:
        img = ImageEnhance.Contrast(img).enhance(contrast_factor)
    out_path = os.path.join(IMG_OUT, name)
    img.save(out_path, "JPEG", quality=90, optimize=True)
    print(f"Created {out_path}")

print("\nAll images generated successfully!")
