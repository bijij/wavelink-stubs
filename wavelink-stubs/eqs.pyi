from typing import List, Tuple, Type, TypedDict, TypeVar


class EqualizerBand(TypedDict):
    band: int
    gain: float


EqualizerT = TypeVar('EqualizerT', bound=Equalizer)


class Equalizer:
    eq: List[EqualizerBand]
    raw: List[Tuple[int, float]]

    def __init__(
        self, *, levels: List[Tuple[int, float]], name: str = ...) -> None: ...

    @property
    def name(self) -> str: ...

    @classmethod
    def build(cls: Type[EqualizerT], *,
              levels: List[Tuple[int, float]], name: str = ...) -> EqualizerT: ...

    @classmethod
    def flat(cls: Type[EqualizerT]) -> EqualizerT: ...

    @classmethod
    def boost(cls: Type[EqualizerT]) -> EqualizerT: ...

    @classmethod
    def metal(cls: Type[EqualizerT]) -> EqualizerT: ...

    @classmethod
    def piano(cls: Type[EqualizerT]) -> EqualizerT: ...
