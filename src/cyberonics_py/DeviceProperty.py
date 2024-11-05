from typing import TypeVar, Generic, Callable, Optional

T = TypeVar('T')

class DeviceProperty(Generic[T]):
    def __init__(self, initial_value: T, mutable: bool) -> None:
        self.__value = initial_value
        self.__mutable = mutable
        self.type = type(initial_value)
        self.__listeners = []

    """
    Adds a listener and returns its ID. This id can be passed to `free_listener` to remove the listener.
    """
    def add_listener(self, listener: Callable[['DeviceProperty[T]'], None]) -> int:
        if not self.__mutable:
            raise AttributeError("Can not listen to immutable property. Set `mutable` to True during initialization to allow listening.")
        self.__listeners.append(listener)
        return len(self.__listeners)

    """
    Removes a listener by its ID.
    """
    def free_listener(self, listener_id: int) -> None:
        if len(self.__listeners) < listener_id or listener_id < 1:
            raise ValueError("Invalid listener ID")
        self.__listeners.pop(listener_id - 1)


    @property
    def mutable(self) -> bool:
        return self.__mutable

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, new_value: T | str) -> None:
        if not self.__mutable:
            raise AttributeError("This property is read-only.")

        if isinstance(new_value, str):
            try:
                new_value = self.type(new_value)
            except ValueError:
                raise ValueError(f"Cannot convert '{new_value}' to {self.type.__name__}")
        else:
            self.__value = new_value
        for listener in self.__listeners:
            listener(self)