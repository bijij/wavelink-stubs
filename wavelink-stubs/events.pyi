from typing import Generic, TypeVar

from discord.ext.commands import Context

from .player import Player, Track

__all__ = ('TrackEnd',
           'TrackException',
           'TrackStuck',
           'TrackStart',
           'WebsocketClosed')


CtxT = TypeVar('CtxT', bound=Context)

class TrackEnd(Generic[CtxT]):
    player: Player[CtxT]
    track: Track
    reason: str


class TrackException(Generic[CtxT]):
    player: Player[CtxT]
    track: Track
    error: str


class TrackStuck(Generic[CtxT]):
    player: Player[CtxT]
    track: Track
    threshold: int


class TrackStart(Generic[CtxT]):
    player: Player[CtxT]
    track: Track


class WebsocketClosed(Generic[CtxT]):
    player: Player[CtxT]
    reason: str
    code: int
    guild_id: int
