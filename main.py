from downloader import utils
from downloader.engine import YoutubeVideoDownloadEngine

if __name__ == "__main__":
    args = utils.parse_args()
    engine = YoutubeVideoDownloadEngine(
        channel_id=args.channel_id,
        saving_path=args.saving_path,
        _save_audio_only=args.save_audio_only,
    ).run()
