from PIL import Image, ImageDraw, ImageFont
import imageio
import os
import shutil

# Create a temporary directory to store frames
os.makedirs("gif_frames", exist_ok=True)

# Parameters
width, height = 400, 400
bg_color = "white"
bracket_color = "#00A0C6"  # Blue
font_size = 80
cursor_color = "black"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update if needed

# Typing animation frames
texts = ["< >", "<H >", "<HT >", "<HTM >", "<HTML>", "<HTML|>", "<HTML >", "<HTM >", "<HT >", "<H >", "< >", " "]
frames = []
frame_duration = 0.2  # seconds per frame

for i, text in enumerate(texts):
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Fixed: Use textbbox instead of deprecated textsize
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, fill=bracket_color if "<" in text else cursor_color, font=font)

    frame_path = f"gif_frames/frame_{i:02d}.png"
    img.save(frame_path)
    frames.append(imageio.imread(frame_path))

# Save as GIF
imageio.mimsave("code_brackets_typing.gif", frames, duration=frame_duration)

# Clean up temporary files
shutil.rmtree("gif_frames")

print("GIF created successfully: code_brackets_typing.gif")