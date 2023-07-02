from textwrap import dedent
from html5tagger import Document, E, Builder, HTML


class SlidesPage:
    def __init__(self, content: str, style: str) -> None:
        self.doc = Document(
            title="AMH Slides",
            lang="en",
            charset="utf-8",
            _urls=[
                "/reveal/reset.css",
                "/reveal/reveal.css",
                "/reveal/theme/night.css",
                "/plugin/highlight/monokai.css",
            ],
        )
        self.content = HTML(content)
        self.style = style
        self._build()

    def __str__(self) -> str:
        return str(self.doc)

    def _build(self) -> None:
        self._head()
        self._body()

    def _head(self) -> None:
        self.doc.head(
            E.meta(
                name="viewport",
                content=(
                    "width=device-width, initial-scale=1.0, "
                    "maximum-scale=1.0, user-scalable=no"
                ),
            ),
            self._style(),
        )

    def _style(self) -> Builder:
        builder = Builder("StyleBuilder")
        builder.style(self.style)
        return builder

    def _body(self) -> None:
        self.doc.body(self._slides(), self._scripts())

    def _slides(self) -> Builder:
        builder = Builder("SlidesBuilder")
        builder.div(
            E.div(
                E.section(
                    E.script(
                        self.content,
                        type="text/template",
                    ),
                    data_markdown=True,
                ),
                class_="slides",
            ),
            class_="reveal",
        )
        return builder

    def _scripts(self) -> Builder:
        builder = Builder("ScriptsBuilder")
        # fmt: off
        builder. \
            script(src="/reveal/reveal.js"). \
            script(src="/plugin/notes/notes.js"). \
            script(src="/plugin/markdown/markdown.js"). \
            script(src="/plugin/highlight/highlight.js"). \
            script(
                dedent(
                    """
                    Reveal.initialize({
                        controls: false,
                        hash: true,
                        plugins: [
                            RevealMarkdown,
                            RevealHighlight,
                            RevealNotes
                        ],
                        totalTime: 2885
                    });
                    """
                )
            )
        # fmt: on
        return builder
