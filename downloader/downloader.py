import os

from yt_dlp import YoutubeDL


class YoutubeDownloader:
    def __init__(
        self,
        channel_id: str,
        saving_path: str,
        _save_audio_only: bool,
    ) -> None:
        """
        Initialize the YoutubeDownloader.

        Args:
            channel_id (str): The YouTube channel ID to download videos from.
            saving_path (str): The file system path where downloaded content will be saved.
            _save_audio_only (bool): Flag indicating whether to save only audio.

        Returns:
            None
        """

        os.makedirs(
            name=saving_path,
            exist_ok=True,
        )
        self.ydl_opts = {
            "format": "140" if _save_audio_only else "399",
            "outtmpl": f"{saving_path}/%(id)s.%(ext)s",
            "ignoreerrors": True,
            "extract_flat": "in_playlist",
            "noplaylist": True,
            "retries": 3,
            "quiet": True,
        }
        channel_url = f"https://www.youtube.com/@{channel_id}/videos"
        with YoutubeDL(params=self.ydl_opts) as ydl:
            channel_info = ydl.extract_info(
                url=channel_url,
                download=False,
            )
        self.channel_video_url_list = [e["url"] for e in channel_info["entries"]]

    def download(
        self,
        idx: int,
    ) -> None:
        """
        Downloads a video from the channel's video list based on the provided index.

        Parameters:
            idx (int): The index of the video URL in the channel_video_url_list to download.

        Returns:
            None
        """

        with YoutubeDL(params=self.ydl_opts) as ydl:
            ydl.download(url_list=[self.channel_video_url_list[idx]])
