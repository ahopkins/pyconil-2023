from sanic import Sanic, Request, html
from .slides import SlidesPage


def setup_view(app: Sanic) -> None:
    @app.get("/")
    async def handler(request: Request, slides: SlidesPage):
        return html(str(slides))

    for name in ("reveal", "plugin", "images"):
        app.static(f"/{name}", f"./{name}", name=name)
