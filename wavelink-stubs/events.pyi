from typing import Any

from .player import Player, Track

__all__ = ('TrackEnd',
           'TrackException',
           'TrackStuck',
           'TrackStart',
           'WebsocketClosed')


class TrackEnd:
    player: Player[Any, Any]
    track: Track
    reason: str


class TrackException:
    player: Player[Any, Any]
    track: Track
    error: str


class TrackStuck:
    player: Player[Any, Any]
    track: Track
    threshold: int


class TrackStart:
    player: Player[Any, Any]
    track: Track


class WebsocketClosed:
    player: Player[Any, Any]
    reason: str
    code: int
    guild_id: int
