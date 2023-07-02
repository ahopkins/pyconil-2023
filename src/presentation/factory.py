from sanic import Sanic
from .slides import SlidesPage
from pathlib import Path

from .livereload import setup_livereload
from .view import setup_view


def create_app(slides_path: Path, css_path: Path) -> Sanic:
    app = Sanic("AMH-PyConIL-Slides")

    @app.before_server_start
    async def setup_slides(app: Sanic) -> None:
        app.ext.dependency(
            SlidesPage(
                slides_path.read_text(encoding="utf-8"),
                css_path.read_text(encoding="utf-8"),
            )
        )

    setup_view(app)
    setup_livereload(app)

    return app
