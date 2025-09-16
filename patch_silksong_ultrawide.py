import argparse, shutil
from pathlib import Path

PATTERN = bytes([0x11, 0x11, 0x19, 0x40])
REPLACE  = bytes([0x00, 0x00, 0x20, 0x41])

def patch(path: Path, force: bool=False, backup: bool=True, dry_run: bool=False):
    data = path.read_bytes()

    if PATTERN not in data and REPLACE in data:
        print("Already patched; nothing to do.")
        return

    count = data.count(PATTERN)
    if count != 3 and not force:
        raise SystemExit(f"Expected 3 occurrences, found {count}. Use --force if intentional.")

    if dry_run:
        print(f"Would patch {count} occurrence(s). (dry run)")
        return

    if backup:
        bak = path.with_suffix(path.suffix + ".bak")
        if not bak.exists():
            shutil.copy2(path, bak)
            print(f"Backup created: {bak.name}")
        else:
            print(f"Backup exists: {bak.name}")

    patched = data.replace(PATTERN, REPLACE)
    path.write_bytes(patched)
    print(f"Patched {count} occurrence(s).")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Hollow Knight: Silksong - Ultrawide Fix")
    ap.add_argument("dll", type=Path, help="Path to Assembly-CSharp.dll")
    ap.add_argument("--force", action="store_true", help="Patch even if occurrence count != 3")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backup")
    ap.add_argument("--dry-run", action="store_true", help="Scan only; don't modify the file")
    args = ap.parse_args()
    patch(args.dll, force=args.force, backup=not args.no_backup, dry_run=args.dry_run)