from PIL import Image

input_path = "/mnt/data/Captura de tela 2025-08-08 172505.png"

img = Image.open(input_path)

size_classic = (200, 200)   # Quadrado
size_featured = (680, 383)  # Retângulo 16:9

def resize_with_padding(image, target_size, fill_color=(0, 0, 0)):
    ratio = min(target_size[0] / image.width, target_size[1] / image.height)
    new_size = (int(image.width * ratio), int(image.height * ratio))
    resized_img = image.resize(new_size, Image.LANCZOS)
    
    new_img = Image.new("RGB", target_size, fill_color)
    new_img.paste(resized_img, ((target_size[0] - new_size[0]) // 2,
                                (target_size[1] - new_size[1]) // 2))
    return new_img

classic_img = resize_with_padding(img, size_classic)
featured_img = resize_with_padding(img, size_featured)

classic_path = "/mnt/data/linktree_thumbnail_classic_200x200.png"
featured_path = "/mnt/data/linktree_thumbnail_featured_680x383.png"

classic_img.save(classic_path)
featured_img.save(featured_path)

(classic_path, featured_path)
