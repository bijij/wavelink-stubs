from asyncio import AbstractEventLoop
from aiohttp import ClientSession
from typing import Any, Callable, Dict, List, Optional, Union, Type, TypeVar, overload

from .player import Player, Track, TrackPlaylist
from .node import Node

from discord.ext.commands.bot import BotBase
from discord.ext.commands.context import Context

CtxT = TypeVar('CtxT', bound=Context)

T = TypeVar('T', bound=Player)

class Client:
    bot: BotBase[Any]
    loop: AbstractEventLoop
    session: ClientSession

    def __init__(self, Bot: BotBase[CtxT]) -> None: ...

    @property
    def shard_count(self) -> int: ...

    @property
    def user_id(self) -> int: ...

    @property
    def players(self) -> Dict[int, Player]: ...

    async def get_tracks(
        self, query: str, *, retry_on_failure: bool) -> Optional[Union[TrackPlaylist, List[Track]]]: ...

    async def build_track(self, identifier: str) -> Track: ...

    def get_node(self, identifier: str) -> Optional[Node]: ...

    def get_best_node(self) -> Optional[Node]: ...

    def get_node_by_region(self, region: str) -> Optional[Node]: ...

    def get_node_by_shard(self, shard_id: int) -> Optional[Node]: ...

    @overload
    def get_player(self, guild_id: int, *,
                   cls: Type[T], node_id: Optional[str], **kwargs: Any) -> T: ...

    @overload
    def get_player(self, guild_id: int, *,
                   node_id: Optional[str], **kwargs: Any) -> Player: ...

    async def initiate_node(self, host: str, port: int, *, rest_uri: str, password: str, region: str,
                            indentifier: str, shard_id: Optional[int], secure: bool, heartbeat: Optional[float]) -> Node: ...

    async def destroy_node(self, *, identifier: str) -> None: ...

    # async def update_handler

    def set_serializer(
        self, serializer_function: Callable[[Any], str]) -> None: ...
