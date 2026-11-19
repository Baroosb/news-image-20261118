#!/usr/bin/env python3
import os
import sys
import hashlib
import pathlib
import stat

EXPECTED_BYTES = 273446
EXPECTED_SHA256 = "dfa9ecaa02b7348e1e143ab4ec3f4f1c97012242d77b530f1132666fe6acb25c"

def main():
    script_dir = pathlib.Path(__file__).parent
    src_path = script_dir / "frontpage.jpg"

    if not src_path.exists():
        raise SystemExit(f"Error: {src_path} does not exist.")

    data = src_path.read_bytes()
    actual_bytes = len(data)
    if actual_bytes != EXPECTED_BYTES:
        raise SystemExit(f"Error: byte size mismatch: expected {EXPECTED_BYTES}, got {actual_bytes}")

    actual_sha256 = hashlib.sha256(data).hexdigest()
    if actual_sha256 != EXPECTED_SHA256:
        raise SystemExit(f"Error: SHA256 mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}")

    # Check JPEG markers
    if len(data) < 2 or data[0:2] != b'\xff\xd8':
        raise SystemExit("Error: invalid JPEG SOI marker")
    if data[-2:] != b'\xff\xd9':
        raise SystemExit("Error: invalid JPEG EOI marker")

    # Walk segments to find SOF0 or SOF2
    width, height = None, None
    i = 2
    while i < len(data) - 1:
        while i < len(data) and data[i] != 0xff:
            i += 1
        if i >= len(data) - 1:
            break
        while i < len(data) and data[i] == 0xff:
            i += 1
        if i >= len(data):
            break
        marker = data[i]
        i += 1

        # Standalone markers without length
        if marker in (0xd0, 0xd1, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xd9, 0x01, 0x00):
            continue

        if i + 2 > len(data):
            break
        length = int.from_bytes(data[i:i+2], 'big')
        
        # SOF0 (Baseline DCT) = 0xc0, SOF2 (Progressive DCT) = 0xc2
        if marker in (0xc0, 0xc2):
            if i + 7 <= len(data):
                # precision = data[i+2]
                height = int.from_bytes(data[i+3:i+5], 'big')
                width = int.from_bytes(data[i+5:i+7], 'big')
                break
        i += length

    if width is None or height is None:
        raise SystemExit("Error: could not find SOF0/SOF2 segment in JPEG")

    if width > 1024 or height > 1024:
        raise SystemExit(f"Error: dimensions {width}x{height} exceed maximum allowed dimension of 1024")

    # Determine output directory
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    out_dir = pathlib.Path(out_dir_env) if out_dir_env else pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / "entry.png"
    out_file.write_bytes(data)
    os.chmod(out_file, 0o644)

    # Re-read and re-verify
    re_data = out_file.read_bytes()
    re_bytes = len(re_data)
    if re_bytes != EXPECTED_BYTES:
        raise SystemExit(f"Error: re-read byte size mismatch: expected {EXPECTED_BYTES}, got {re_bytes}")

    re_sha256 = hashlib.sha256(re_data).hexdigest()
    if re_sha256 != EXPECTED_SHA256:
        raise SystemExit(f"Error: re-read SHA256 mismatch: expected {EXPECTED_SHA256}, got {re_sha256}")

    # Verify permission bits (Step 3 requirement)
    st = out_file.stat()
    mode = stat.S_IMODE(st.st_mode)
    if mode != 0o644:
        raise SystemExit(f"Error: permission bits mismatch: expected 0o644, got {oct(mode)}")

    print(f"Successfully processed frontpage.jpg: dimensions {width}x{height}, byte count {actual_bytes}")

if __name__ == "__main__":
    main()
