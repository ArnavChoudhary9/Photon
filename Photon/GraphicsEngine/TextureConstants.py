class TextureConstants:
    class Format:
        RGB: int = 00
        RGBA: int = 1
        RED_INTEGER: int = 2
        DEPTH_STENCIL: int = 3

    class Size:
        RGB8: int = 10
        RGB16: int = 11
        RGBA8: int = 12
        RGBA16: int = 13
        DEPTH24STENCIL8: int = 14
        R32I: int = 15

    class DataType:
        UNSIGNED_BYTE: int = 20
        UNSIGNED_INT_24_8: int = 21

    class WrapMode:
        REPEAT: int = 30
        MIRRORED_REPEAT: int = 31
        CLAMP_TO_EDGE: int = 32
        CLAMP_TO_BORDER: int = 33

    class Filter:
        LINEAR: int = 40
        NEAREST: int = 41
        MIPMAP_LINEAR: int = 42
