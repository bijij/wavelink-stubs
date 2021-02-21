from .player import Player, Track


class TrackEnd:
    player: Player
    track: Track
    reason: str


class TrackException:
    player: Player
    track: Track
    error: str


class TrackStuck:
    player: Player
    track: Track
    threshold: int


class TrackStart:
    player: Player
    track: Track


class WebsocketClosed:
    player: Player
    reason: str
    code: int
    guild_id: int
