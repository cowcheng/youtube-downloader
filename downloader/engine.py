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
            saving_path (str): The path where downloaded videos or audio will be saved.
            _save_audio_only (bool): If True, only audio will be downloaded.
        Returns:
            None
        """
        self.num_workers = min(8, os.cpu_count())
        self.downloader = YoutubeDownloader(
            channel_id=channel_id,
            saving_path=saving_path,
            _save_audio_only=_save_audio_only,
        )
        logger.info(msg="Initializing Youtube Video Downloader Engine")
        logger.info(msg=f"Number of workers: {self.num_workers}")

    def run(
        self,
    ) -> None:
        """
        Executes the video downloading process using a thread pool.
        This method initiates the download of videos from the channel's video URL list.
        It logs the start and completion of the download process. A `ThreadPoolExecutor` is
        used with the specified number of workers to perform downloads concurrently.
        The progress of downloads is displayed using a tqdm progress bar.
        Returns:
            None
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
