from ..Graphic import Graphic
from ..GraphicState import GraphicState
from ..GraphicTyping import TextAlignment, Color


class SubText(Graphic):
    def __init__(self, text: str, alignment: TextAlignment = TextAlignment.LEFT, color: Color = Color.PRIMARY,
                 bold: bool = False, italic: bool = False) -> None:
        self.__text = text
        self.__alignment = alignment
        self.__color = color
        self.__bold = bold
        self.__italic = italic
        super().__init__(None)
        self.__notify()

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value: str) -> None:
        self.__text = value
        self.__notify()

    @property
    def alignment(self) -> TextAlignment:
        return self.__alignment

    @alignment.setter
    def alignment(self, value: TextAlignment) -> None:
        self.__alignment = value
        self.__notify()

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, value: Color) -> None:
        self.__color = value
        self.__notify()

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, value: bool) -> None:
        self.__bold = value
        self.__notify()

    @property
    def italic(self) -> bool:
        return self.__italic

    @italic.setter
    def italic(self, value: bool) -> None:
        self.__italic = value
        self.__notify()

    def get_state(self) -> GraphicState:
        return GraphicState("SubText", super().uuid, text=self.text, alignment=self.alignment, color=self.color, bold=self.bold, italic=self.italic)

    def set_state(self, state: GraphicState) -> None:
        raise ValueError("SubText can not be set by the client")