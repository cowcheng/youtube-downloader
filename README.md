# YouTube Downloader

This repository provides a Python-based, multithreaded tool to download YouTube videos with audio or as audio-only files, supporting entire channels. Built with `yt_dlp`, it offers users the choice between video or audio downloads and uses multithreading for faster performance. Users can specify an output path for saved files, making it an efficient solution for archiving or offline access while adhering to YouTube’s terms of service.

## Setup

1. **Create a virtual environment using Python 3.11:**

   ```bash
   python3.11 -m venv venv
   ```

2. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Upgrade pip, wheel, and setuptools:**

   ```bash
   pip install -U pip wheel setuptools
   ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the downloader with the following command:

```bash
python main.py --channel_id RainIsHere --saving_path ./youtube_RainIsHere --save_audio_only
```
