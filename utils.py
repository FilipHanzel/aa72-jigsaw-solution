from pprint import pprint
from typing import Any


def preview_contents(container: Any) -> None:
    """Print a preview of container contents."""

    def _build(container: Any) -> Any:
        if isinstance(container, dict):
            return {key: _build(value) for key, value in container.items()}
        elif isinstance(container, (list, tuple, set)):
            preview = []
            for item in container:
                item_preview = _build(item)
                if item_preview not in preview:
                    preview.append(item_preview)
            return container.__class__(sorted(preview, key=str))
        else:
            return type(container)

    pprint(_build(container))
