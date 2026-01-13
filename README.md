# 👻 Snapchat Uploader

Snapchat Uploader is a small Python-based utility for working with Snapchat
content through official HTTP interfaces.

The project focuses on simplicity and transparency, providing a predictable
way to send text and media content without relying on browser-level behavior.

---

## 🧭 What This Project Does

This repository offers a command-line tool and a Python module that help you
prepare and publish content to Snapchat in a structured way.

It is built to be:

- 🧱 easy to understand  
- 🧩 modular by design  
- 🪶 lightweight in dependencies  
- 📐 consistent in behavior  

The codebase is intentionally kept compact and readable.

---

## 📸 Content Capabilities

The uploader supports the following content formats:

- ✏️ Plain text messages  
- 🖼 Images provided via public URLs  
- 🎬 Videos provided via public URLs  

Text can be used on its own or together with media where applicable.

---

## 🛠 Technical Approach

- 📡 Communicates via official Snapchat HTTP endpoints
- 🚫 Does not interact with user interfaces
- 🔐 Configuration is handled through environment variables
- 🧪 Favors explicit execution and clear errors
- 🔄 Components can be reused independently

This approach helps keep the project stable and easy to adapt.

# 🚦 Runtime Behavior

- ❗ Network or API issues are surfaced immediately
- 🔍 Missing configuration is detected at startup
- 🧪 Invalid CLI usage results in clear feedback


# 🧩 Future Extensions

- 📂 Support for local media files
- 🕓 Scheduled content publishing
- 📚 Multi-item publishing workflows
- 🔗 Integration with external content sources
- 🔐 Expanded authorization handling

---

## ⚙️ System Requirements

To use this project, you will need:

- 🐍 Python version 3.9 or newer  
- 🔑 A valid Snapchat API access token  
- 👤 A Snapchat account identifier  
 
📕 Send text content
python cli.py --text "Hello Snapchat"

🖼 Send an image
python cli.py \
  --image https://example.com/image.jpg \
  --text "Image description"

🎬 Send a video
python cli.py \
  --video https://example.com/video.mp4 \
  --text "Video description"



