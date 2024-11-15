import logging
from argparse import ArgumentParser, Namespace

from downloader.configs import LOG_DATEFMT, LOG_FORMAT, LOG_LEVEL

logging.basicConfig(
    format=LOG_FORMAT,
    datefmt=LOG_DATEFMT,
    level=LOG_LEVEL,
)

logger = logging.getLogger(name="YoutubeDownloader")


def parse_args() -> Namespace:
    """
    Parse command-line arguments for the YouTube downloader.

    Returns:
        Namespace: Parsed command-line arguments including:
            channel_id (str): ID of the YouTube channel.
            saving_path (str): Path to save the downloaded videos.
            save_audio_only (bool): Flag indicating whether to save audio only.
    """

    parser = ArgumentParser()
    parser.add_argument(
        "--channel_id",
        type=str,
        required=True,
        help="ID of the YouTube channel",
    )
    parser.add_argument(
        "--saving_path",
        type=str,
        required=True,
        help="Path to save the downloaded videos",
    )
    parser.add_argument(
        "--save_audio_only",
        action="store_true",
        required=True,
        help="Save audio only",
    )
    args = parser.parse_args()
    return args
