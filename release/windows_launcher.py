"""Windows entry point used to demonstrate an executable release asset."""

import sys
from pathlib import Path

from streamlit.web import cli as streamlit_cli


def main() -> None:
    """Start the bundled Streamlit application on the local computer."""
    source_root = Path(__file__).resolve().parents[1]
    bundle_root = Path(getattr(sys, "_MEIPASS", source_root))
    application = bundle_root / "src" / "app.py"
    sys.argv = [
        "streamlit",
        "run",
        str(application),
        "--server.address=127.0.0.1",
        "--server.port=8501",
    ]
    raise SystemExit(streamlit_cli.main())


if __name__ == "__main__":
    main()
