from typing import Any, Callable, Generic, Optional, TypeVar

from discord.ext.commands import Context

from .events import *
from .node import Node

CtxT = TypeVar('CtxT', bound=Context)
ListenerT = TypeVar('ListenerT', bound=Callable[..., Any])

class WavelinkMixin(Generic[CtxT]):

    async def on_wavelink_error(
        self, listener: str, error: Exception) -> None: ...

    async def on_node_ready(self, node: Node) -> None: ...

    async def on_track_start(
        self, node: Node, payload: TrackStart[CtxT]) -> None: ...

    async def on_track_end(self, node: Node, payload: TrackEnd[CtxT]) -> None: ...

    async def on_track_stuck(
        self, node: Node, payload: TrackStuck[CtxT]) -> None: ...

    async def on_track_exception(
        self, node: Node, payload: TrackException[CtxT]) -> None: ...

    async def on_websocket_closed(
        self, node: Node, payload: WebsocketClosed[CtxT]) -> None: ...

    @staticmethod
    def listener(event: Optional[str] = ...) -> Callable[[ListenerT], ListenerT]: ...
