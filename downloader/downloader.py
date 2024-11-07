import os

from yt_dlp import YoutubeDL

from downloader import utils

logger = utils.setup_logger()


class YoutubeDownloader:
    def __init__(
        self,
        channel_id: str,
        saving_path: str,
        _save_audio_only: bool,
    ) -> None:
        """
        Initializes the YoutubeDownloader with the given parameters.
        Args:
            channel_id (str): The ID of the YouTube channel to download videos from.
            saving_path (str): The file system path where downloaded videos/audio will be saved.
            _save_audio_only (bool): If True, only download the audio of the videos.
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
        logger.info(msg="Initializing YoutubeDownloader")
        logger.info(msg=f"Channel ID: {channel_id}")
        logger.info(msg=f"Saving path: {saving_path}")
        logger.info(msg=f"Save audio only: {_save_audio_only}")

    def download(
        self,
        idx: int,
    ) -> None:
        """
        Downloads the video at the specified index from the channel's video URL list.
        Args:
            idx (int): The index of the video to download.
        Returns:
            None
        """
        with YoutubeDL(params=self.ydl_opts) as ydl:
            ydl.download(url_list=[self.channel_video_url_list[idx]])
