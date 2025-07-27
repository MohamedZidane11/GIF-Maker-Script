# 🎬 HTML Typing Animation GIF Generator

A Python script that creates a mesmerizing typing animation GIF showing HTML brackets being typed and deleted in a loop! Perfect for developer portfolios, GitHub profiles, or any web development project.

## ✨ Features

- 🎭 **Smooth typing animation** - Realistic character-by-character typing effect
- 🔄 **Loop animation** - Types "HTML" and then deletes it in reverse
- 🎨 **Customizable colors** - Easy to modify bracket colors and background
- 📐 **Adjustable parameters** - Control size, speed, and font styling
- 🖼️ **High-quality output** - Generates crisp, professional-looking GIFs
- 🧹 **Clean code** - Automatically cleans up temporary files

## 🎯 Demo

The animation cycles through these frames:
```
< > → <H > → <HT > → <HTM > → <HTML> → <HTML|> → <HTML > → <HTM > → <HT > → <H > → < > → (repeat)
```

## 🛠️ Requirements

Install the required packages:

```bash
pip install Pillow imageio
```

## 🚀 Usage

1. **Clone or download** the script
2. **Run the script**:
   ```bash
   python main.py
   ```
3. **Find your GIF** - `code_brackets_typing.gif` will be created in the same directory

## ⚙️ Customization

Easy to customize! Modify these parameters in the script:

```python
# Animation settings
width, height = 400, 400          # 📏 GIF dimensions
bg_color = "white"                # 🎨 Background color
bracket_color = "#00A0C6"         # 🔵 Text color (blue)
font_size = 80                    # 📝 Font size
frame_duration = 0.2              # ⏱️ Speed (seconds per frame)
```

## 🎨 Color Schemes

Try these popular color combinations:

| Theme | Background | Text Color | Description |
|-------|------------|------------|-------------|
| 🌊 Ocean | `"white"` | `"#00A0C6"` | Default blue theme |
| 🌙 Dark Mode | `"#1a1a1a"` | `"#00ff00"` | Terminal green |
| 🔥 Fire | `"black"` | `"#ff6b35"` | Orange accent |
| 💜 Purple | `"#2d1b69"` | `"#a463f2"` | Purple gradient |

## 📁 File Structure

```
your-project/
├── html_typing_animation.py    # 🐍 Main script
├── code_brackets_typing.gif    # 🎬 Generated animation
└── README.md                   # 📖 This file
```

## 🔧 Technical Details

- **Framework**: PIL/Pillow for image generation
- **Animation**: imageio for GIF creation
- **Font handling**: Automatic fallback to system fonts
- **Compatibility**: Works with modern Python 3.x and latest Pillow versions

## 🤝 Contributing

Found a bug? Have an idea for improvement? 

1. 🍴 Fork the repository
2. 🌟 Create your feature branch
3. 💾 Commit your changes
4. 🚀 Push to the branch
5. 🎉 Open a Pull Request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Inspired by classic terminal typing animations
- Perfect for showcasing your web development skills!

---

⭐ **Star this repo** if you found it helpful!

🐛 **Report issues** if you encounter any problems

💡 **Suggest features** for future improvements
