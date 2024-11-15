# YouTube Downloader

This repository provides a multithreaded Python tool for downloading YouTube videos as video or audio-only files, supporting individual videos or entire channels. Built with [yt_dlp](https://github.com/yt-dlp/yt-dlp), it allows users to select download options, specify output paths, and leverages multithreading for faster performance, making it an efficient tool for offline access and archiving while complying with YouTube’s terms of service.

## Features

- **Video and Audio Downloads**: Choose between downloading full videos or audio-only files.
- **Channel Support**: Download all videos from a specified YouTube channel.
- **Multithreading**: Speed up download processes with multithreaded support.

## Setup

### Prerequisites

- Python 3.11 or higher
- Compatible GPUs (for multi-GPU support)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/cowcheng/youtube-downloader.git
cd youtube-downloader
```

2. Create a virtual environment:

```bash
python3.11 -m venv .venv
```

3. Activate the virtual environment:

   1. On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   2. On macOS and Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Upgrade pip, wheel, and setuptools:

```bash
pip install -U pip wheel setuptools
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the downloader, use the following command:

```bash
python main.py --channel_id <channel_id> --saving_path <output_directory> --save_audio_only
```

### Command-Line Arguments

- `--channel_id`: The ID of the YouTube channel you want to download from.
- `--saving_path`: Path to the directory where the downloaded files will be saved.
- `--save_audio_only`: Optional flag to download audio-only files instead of full videos.

## Workflow

1. **Initialize the Downloader**: The tool starts by reading the specified channel ID and output path.
2. **Select Download Mode**: Users can choose to download either full videos or audio-only files.
3. **Multithreaded Processing**: The downloader uses multiple threads to manage and accelerate download tasks, making it efficient even for large playlists or channels.
4. **Save Files**: The tool saves each downloaded file to the specified output directory, organizing files for easy access.

## Note

- YouTube’s Terms of Service: Please use this tool responsibly and ensure that your downloads comply with YouTube's terms of service and copyright laws.
- Performance Consideration: Multithreading and large downloads can be resource-intensive. Ensure your system has sufficient memory and network bandwidth for optimal performance.

## License

Please ensure usage of this tool complies with YouTube’s terms of service and copyright laws.
