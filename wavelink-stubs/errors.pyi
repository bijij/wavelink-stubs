class WavelinkException(Exception):
    ...


class NodeOccupied(WavelinkException):
    ...


class InvalidIDProvided(WavelinkException):
    ...


class ZeroConnectedNodes(WavelinkException):
    ...


class AuthorizationFailure(WavelinkException):
    ...


class BuildTrackError(WavelinkException):
    ...
