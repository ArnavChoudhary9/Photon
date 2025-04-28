from ..Layers import Overlay
from ..Events import *
from ..GraphicsEngine import Window

from imgui_bundle import imgui, imgui_ctx, glfw_utils
from imgui_bundle.python_backends.glfw_backend import GlfwRenderer
import glfw

import importlib.resources

class GUIInitializer(Overlay):
    __BlockEvents: bool = False

    def __init__(self, window: Window) -> None:
        super().__init__("GUIInitializer")
        self.__Renderer = GlfwRenderer(window.NativeWindow, False)

    def OnInitialize(self) -> None:        
        imgui.create_context()
        io = imgui.get_io()
        self.__IO = io

        io.config_flags |= imgui.ConfigFlags_.nav_enable_keyboard # type: ignore
        io.config_flags |= imgui.ConfigFlags_.docking_enable # type: ignore
        io.config_flags |= imgui.ConfigFlags_.viewports_enable # type: ignore

        # with importlib.resources.path("Photon.Resources.Fonts.opensans", "OpenSans-Regular.ttf") as font_path:
        #     io.fonts.add_font_from_file_ttf(str(font_path), 18.0)

        imgui.style_colors_dark()

        style = imgui.get_style()
        if io.config_flags & imgui.ConfigFlags_.viewports_enable: # type: ignore
            style.window_rounding = 0.0
            bgColor = style.color_(imgui.Col_.window_bg) # type: ignore
            style.set_color_(imgui.Col_.window_bg, imgui.ImVec4(bgColor.x, bgColor.y, bgColor.z, 1.0)) # type: ignore

        # glfw.set_mouse_button_callback(window, mouse_button_callback)
        # glfw.set_cursor_pos_callback(window, cursor_position_callback)
        # glfw.set_scroll_callback(window, scroll_callback)
        # glfw.set_key_callback(window, key_callback)
        # glfw.set_char_callback(window, char_callback)

        self._EventDispatcher.AddHandler(EventType.MouseButtonPressed, self.mouse_button_callback) # type: ignore

        # self._EventDispatcher.AddHandler( EventType.KeyPressed    , self.__KeyboardPressCallback    ) # type: ignore
        # self._EventDispatcher.AddHandler( EventType.KeyReleased   , self.__KeyboardReleasedCallback ) # type: ignore
        # self._EventDispatcher.AddHandler( EventType.CharInput     , self.__CharInputCallback        ) # type: ignore
        # self._EventDispatcher.AddHandler( EventType.WindowResize  , self.__WindowResizeCallback     ) # type: ignore
        # self._EventDispatcher.AddHandler( EventType.MouseScrolled , self.__MouseScrollCallback      ) # type: ignore

    def OnDestroy(self) -> None:
        self.__Renderer.shutdown()

    def OnStart(self) -> None: pass
    def OnUpdate(self, dt: float) -> None: pass
    def OnStop(self) -> None: pass

    #-----------------EVENTS-----------------
    def OnEvent(self, event: Event) -> bool: return self._EventDispatcher.Dispatch(event)        
    def mouse_button_callback(self, event: MouseButtonPressedEvent) -> bool:
        imgui.get_io().mouse_down[event.ButtonCode] = True
        return True

    # Callback for mouse position
    def cursor_position_callback(window, xpos, ypos):
        io = imgui.get_io()
        io.mouse_pos = xpos, ypos

    # Callback for mouse scroll
    def scroll_callback(window, xoffset, yoffset):
        io = imgui.get_io()
        io.mouse_wheel = yoffset

    # Callback for keyboard input
    def key_callback(window, key, scancode, action, mods):
        io = imgui.get_io()
        if action == glfw.PRESS:
            io.keys_down[key] = True
        elif action == glfw.RELEASE:
            io.keys_down[key] = False

        io.key_ctrl = io.keys_down[glfw.KEY_LEFT_CONTROL] or io.keys_down[glfw.KEY_RIGHT_CONTROL]
        io.key_shift = io.keys_down[glfw.KEY_LEFT_SHIFT] or io.keys_down[glfw.KEY_RIGHT_SHIFT]
        io.key_alt = io.keys_down[glfw.KEY_LEFT_ALT] or io.keys_down[glfw.KEY_RIGHT_ALT]
        io.key_super = io.keys_down[glfw.KEY_LEFT_SUPER] or io.keys_down[glfw.KEY_RIGHT_SUPER]

    # Callback for character input
    def char_callback(window, char):
        io = imgui.get_io()
        io.add_input_character(char)
    #----------------------------------------

    def BlockEvents(self, block: bool) -> None: self.__BlockEvents = block

    def OnGUIStart(self) -> None:
        self.__Renderer.process_inputs()
        imgui.new_frame()

    def OnGUIRender(self) -> None: pass

    def OnGUIEnd(self) -> None:
        imgui.render()
        self.__Renderer.render(imgui.get_draw_data())

        io = imgui.get_io()
        if io.config_flags & imgui.ConfigFlags_.viewports_enable:  # type: ignore
            backup_current_context = glfw.get_current_context()
            imgui.update_platform_windows()
            imgui.render_platform_windows_default()  # type: ignore
            glfw.make_context_current(backup_current_context)
