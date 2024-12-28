# 🚀 Telegram Forward Bot

A **Telegram bot** built with Python's `telebot` library to **automatically forward** all types of media and messages (photos, documents, audio, video, voice, etc.) from a specific **group chat** to a designated **channel**. 

🔍 This bot logs each forwarded message's **ID** in the console for easy tracking and debugging.

## 📜 Features
- 🚀 Forward messages instantly from a **group chat** to a **channel**.
- 🖼️ Supports media types like **photos**, **documents**, **audio**, **video**, **voice messages**, **stickers**, and **video notes**.
- 🖥️ Displays the **message ID** of each forwarded message in the console for real-time tracking.
- 🤖 Built using the **Python `telebot` library**.

## 🔧 Requirements
- Python 3.6+ 🐍
- `pyTelegramBotAPI` (telebot library) 📦

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-forward-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd telegram-forward-bot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your **Telegram bot API token** to the script. You can get your token by creating a bot on [BotFather](https://core.telegram.org/bots#botfather) and replacing `'YOUR_BOT_API_TOKEN'` in the code.

5. Replace the **group chat ID** and **channel ID** in the script with your own values.

## 📝 How It Works
1. **Start the bot** and let it listen for messages in the specified **group chat**.
2. When a message (photo, document, text, etc.) is sent to the group, the bot **forwards** it automatically to the specified **channel**.
3. The bot also logs the **message ID** in the console every time a message is forwarded.

## 🎯 Use Cases
- **Content Sharing**: Automatically forward shared content from a group to a channel.
- **News Updates**: Send news or announcements to a broader audience.
- **Media Management**: Easily manage media files and forward them to a channel for storage or sharing.

## 🖋️ License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## 📝 Acknowledgements
- Thanks to [Python](https://www.python.org/) for the amazing language.
- Thanks to [telebot](https://github.com/eternnoir/pyTelegramBotAPI) for the easy-to-use library.
```
