def main():
    filename = input("File name: ").strip().lower()

    # Extract extension after last dot
    if "." in filename:
        ext = filename.rsplit(".", 1)[-1]
    else:
        ext = ""

    # Media type lookup
    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    print(media_types.get(ext, "application/octet-stream"))


if __name__ == "__main__":
    main()

