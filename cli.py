import argparse
from snapchat_uploader.uploader import SnapchatUploader


def main():
    parser = argparse.ArgumentParser(description="Snapchat Uploader")

    parser.add_argument("--text", help="Text content")
    parser.add_argument("--image", help="Image URL")
    parser.add_argument("--video", help="Video URL")

    args = parser.parse_args()
    uploader = SnapchatUploader()

    if args.image:
        result = uploader.post_image(args.image, args.text)
    elif args.video:
        result = uploader.post_video(args.video, args.text)
    elif args.text:
        result = uploader.post_text(args.text)
    else:
        parser.error("No content provided")

    print("Done:")
    print(result)


if __name__ == "__main__":
    main()
