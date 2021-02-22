from typing import Any, Dict, Optional, List, TYPE_CHECKING, TypeVar

from discord.ext.commands.bot import BotBase
from discord.ext.commands.context import Context

from .eqs import Equalizer

if TYPE_CHECKING:
    from .node import Node

CtxT = TypeVar('CtxT', bound=Context)


class Track:
    id: str
    info: Dict[str, Any]
    title: str
    identifier: Optional[str]
    ytid: Optional[str]
    length: int
    duration: int
    uri: Optional[str]
    author: Optional[str]
    is_stream: bool
    thumb: Optional[str]

    @property
    def is_dead(self) -> bool: ...


class TrackPlaylist:
    data: Dict[str, Any]
    tracks: List[Track]


class Player:

    def __init__(self, bot: BotBase[CtxT], guild_id: int,
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

    async def disconnect(self) -> None: ...

    async def play(self, track: Track, *, replace: bool,
                   start: int, end: int) -> None: ...

    async def stop(self) -> None: ...

    async def destroy(self) -> None: ...

    async def set_eq(self, equalizer: Equalizer) -> None: ...

    async def set_equalizer(self, equalizer: Equalizer) -> None: ...

    async def set_pause(self, pause: bool) -> None: ...

    async def set_volume(self, vol: int) -> None: ...

    async def seek(self, position: int) -> None: ...

    async def change_node(self, identifier: str) -> None: ...
