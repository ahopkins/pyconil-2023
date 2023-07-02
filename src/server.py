from pathlib import Path
from presentation.factory import create_app

BASE_DIR = Path(__file__).parent
SLIDES_PATH = BASE_DIR / "slides.md"
CSS_PATH = BASE_DIR / "style.css"

app = create_app(SLIDES_PATH, CSS_PATH)


if __name__ == "__main__":
    app.run(port=9999, auto_reload=True, reload_dir=[str(BASE_DIR)])
