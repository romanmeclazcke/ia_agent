
from collections.abc import Mapping
from langchain.tools import ToolRuntime, tool


def _extract_context(runtime: ToolRuntime):
    if runtime.context is not None:
        return runtime.context
    config = getattr(runtime, "config", None)
    if not isinstance(config, Mapping):
        return None
    configurable = config.get("configurable", {})
    if isinstance(configurable, Mapping):
        return configurable.get("context")
    return None

def _get_context_value(context, key: str) -> str:
    if context is None:
        return ""
    if isinstance(context, dict):
        return str(context.get(key, ""))
    return str(getattr(context, key, ""))


@tool
def get_colour(runtime: ToolRuntime, which: str = "favourite") -> str:  #which represent if favourite or least_favourite color,
    """Return favourite or least_favourite color from the user's context."""
    context = _extract_context(runtime)
    normalized = which.strip().lower()
    if "least" in normalized:
        return _get_context_value(context, "least_favourite_color")
    return _get_context_value(context, "favourite_color")
