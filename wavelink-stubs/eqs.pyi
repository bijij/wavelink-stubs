from typing import List, Tuple, Type, TypedDict, TypeVar


class EqualizerBand(TypedDict):
    band: int
    gain: float


T = TypeVar('T', bound=Equalizer)


class Equalizer:
    eq: List[EqualizerBand]
    raw: List[Tuple[int, float]]

    def __init__(
        self, *, levels: List[Tuple[int, float]], name: str = ...) -> None: ...

    @property
    def name(self) -> str: ...

    @classmethod
    def build(cls: Type[T], *,
              levels: List[Tuple[int, float]], name: str = ...) -> T: ...

    @classmethod
    def flat(cls: Type[T]) -> T: ...

    @classmethod
    def boost(cls: Type[T]) -> T: ...

    @classmethod
    def metal(cls: Type[T]) -> T: ...

    @classmethod
    def piano(cls: Type[T]) -> T: ...
