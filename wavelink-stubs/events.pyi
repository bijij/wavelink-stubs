from typing import Any

from .player import Player, Track

__all__ = ('TrackEnd',
           'TrackException',
           'TrackStuck',
           'TrackStart',
           'WebsocketClosed')


class TrackEnd:
    player: Player[Any]
    track: Track
    reason: str


class TrackException:
    player: Player[Any]
    track: Track
    error: str


class TrackStuck:
    player: Player[Any]
    track: Track
    threshold: int


class TrackStart:
    player: Player[Any]
    track: Track


class WebsocketClosed:
    player: Player[Any]
    reason: str
    code: int
    guild_id: int
