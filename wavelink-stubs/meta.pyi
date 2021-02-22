from typing import Any, Callable

from .events import *
from .node import Node


class WavelinkMixin:

    async def on_wavelink_error(
        self, listener: str, error: Exception) -> None: ...

    async def on_node_ready(self, node: Node) -> None: ...

    async def on_track_start(
        self, node: Node, payload: TrackStart) -> None: ...

    async def on_track_end(self, node: Node, payload: TrackEnd) -> None: ...

    async def on_track_stuck(
        self, node: Node, payload: TrackStuck) -> None: ...

    async def on_track_exception(
        self, node: Node, payload: TrackException) -> None: ...

    async def on_websocket_closed(
        self, node: Node, payload: WebsocketClosed) -> None: ...

    @staticmethod
    def listener(event: str) -> Callable[[], Callable[..., Any]]: ...
