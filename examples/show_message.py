from pathlib import Path

asdf

if __name__ == "__main__":
    message = Path(__file__).resolve().parent.parent / "data" / "message.txt"
    print(message.read_text(encoding="utf-8").strip())
