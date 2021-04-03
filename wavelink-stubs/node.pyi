from typing import Any, Callable, Dict, Optional, List, TypeVar, TYPE_CHECKING, Union

from aiohttp import ClientSession

from discord.ext.commands import AutoShardedBot, Bot, Context

if TYPE_CHECKING:
    from .client import Client
    from .player import Track, TrackPlaylist, Player

CtxT = TypeVar('CtxT', bound=Context)


class Node:
    host: str
    port: int
    rest_uri: str
    region: str
    identifier: str

    def __init__(self, host: str, port: int, shards: int, user_id: int, *, client: Client[CtxT], session:  ClientSession, rest_uri: str,
                 password: str, region: str, identifer: str, shard_id: Optional[int] = ..., secure: bool = ...,
                 heartbeat: Optional[float] = ..., dumps: Callable[[Dict[str, Any]], Union[str, bytes]] = ...) -> None: ...

    @property
    def is_available(self) -> bool: ...

    def close(self) -> None: ...

    def open(self) -> None: ...

    @property
    def penalty(self) -> float: ...

    async def connect(self, bot: Union[AutoShardedBot[CtxT], Bot[CtxT]]) -> None: ...

    async def get_tracks(
        self, query: str, *, retry_on_failure: bool = ...) -> Optional[Union[List[Track], TrackPlaylist]]: ...

    async def build_track(self, identifier: str) -> Track: ...

    def get_player(self, guild_id: int) -> Optional[Player[CtxT]]: ...

    async def on_event(self, event: str) -> None: ...

    def set_hook(self, func: Callable[[str], None]) -> None: ...

    async def destroy(self, *, force: bool = ...) -> None: ...
