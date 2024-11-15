import os
from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm

from downloader.downloader import YoutubeDownloader
from downloader.utils import logger


class YoutubeVideoDownloadEngine:
    def __init__(
        self,
        channel_id: str,
        saving_path: str,
        _save_audio_only: bool,
    ) -> None:
        """
        Initializes the Youtube Video Downloader Engine.

        Args:
            channel_id (str): The ID of the YouTube channel to download videos from.
            saving_path (str): The directory path where downloaded videos will be saved.
            _save_audio_only (bool): If set to True, only audio will be downloaded; otherwise, video will be downloaded.
        """
        self.num_workers = min(8, os.cpu_count())

        logger.info(msg="Initializing Youtube Video Downloader Engine")
        logger.info(msg=f"Number of workers: {self.num_workers}")


        logger.info(msg="Initializing YoutubeDownloader")
        logger.info(msg=f"Channel ID: {channel_id}")
        logger.info(msg=f"Saving path: {saving_path}")
        logger.info(msg=f"Save audio only: {_save_audio_only}")

        self.downloader = YoutubeDownloader(
            channel_id=channel_id,
            saving_path=saving_path,
            _save_audio_only=_save_audio_only,
        )

    def run(
        self,
    ) -> None:
        """
        Executes the video download process.

        This method logs the start and completion of the download process, and utilizes a ThreadPoolExecutor
        to concurrently download videos from the channel's video URL list, displaying a progress bar during
        the download.
        """

        logger.info(msg="Start downloading videos.........")
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            list(
                tqdm(
                    iterable=executor.map(
                        self.downloader.download,
                        range(len(self.downloader.channel_video_url_list)),
                    ),
                    total=len(self.downloader.channel_video_url_list),
                )
            )
        logger.info(msg="Finished downloading videos.........")
