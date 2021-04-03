from typing import Any, Dict, Generic, Optional, List, TYPE_CHECKING, TypeVar, Union

from discord.ext.commands import AutoShardedBot, Bot, Context
from discord.ext.commands.context import Context

from .eqs import Equalizer

if TYPE_CHECKING:
    from .node import Node

__all__ = ('Track', 'TrackPlaylist', 'Player')

CtxT = TypeVar('CtxT', bound=Context)


class Track:
    id: str
    info: Dict[str, Any]
    query: Optional[str]
    title: str
    identifier: Optional[str]
    ytid: Optional[str]
    length: int
    duration: int
    uri: Optional[str]
    author: Optional[str]
    is_stream: bool
    thumb: Optional[str]

    def __init__(self, id_: str, info: Dict[str, Any], query: Optional[str] = ...) -> None: ...

    @property
    def is_dead(self) -> bool: ...


class TrackPlaylist:
    data: Dict[str, Any]
    tracks: List[Track]


class Player(Generic[CtxT]):
    bot: Union[AutoShardedBot[CtxT], Bot[CtxT]]
    guild_id: int
    node: Node
    last_update: float
    last_position: float
    position_timestamp: float
    volume: float
    paused: bool
    current: Optional[Track]
    channel_id: Optional[int]


    def __init__(self, bot: Union[AutoShardedBot[CtxT], Bot[CtxT]], guild_id: int,
                 node: Node, **kwargs: Any) -> None: ...

    @property
    def equalizer(self) -> Equalizer: ...

    @property
    def eq(self) -> Equalizer: ...

    @property
    def is_connected(self) -> bool: ...

    @property
    def is_playing(self) -> bool: ...

    @property
    def is_paused(self) -> bool: ...

    @property
    def position(self) -> int: ...

    async def connect(self, channel_id: int) -> None: ...

    async def disconnect(self, *, force: bool = ...) -> None: ...

    async def play(self, track: Track, *, replace: bool = ...,
                   start: int = ..., end: int = ...) -> None: ...

    async def stop(self) -> None: ...

    async def destroy(self, *, force: bool = ...) -> None: ...

    async def set_eq(self, equalizer: Equalizer) -> None: ...

    async def set_equalizer(self, equalizer: Equalizer) -> None: ...

    async def set_pause(self, pause: bool) -> None: ...

    async def set_volume(self, vol: int) -> None: ...

    async def seek(self, position: int = ...) -> None: ...

    async def change_node(self, identifier: Optional[str] = ...) -> None: ...
