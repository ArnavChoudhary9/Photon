from Photon import *

class EditorLayer(Overlay):
    __CurrentScene: Scene
    __CurrentProject: Project
    __AppOnEventFunction: Callable[[Event], bool]
    
    __dt: float
    
    def __init__(self, appOnEvent: Callable[[Event], bool]) -> None:
        super().__init__("EditorLayer")
        self.__AppOnEventFunction = appOnEvent
    
    def OnInitialize(self):
        self.__CurrentProject = Project(Path("DefaultProject"), "DefaultProject")
            
        self.__dt = 0.0
    
    def OnStart(self): ...
        
    def OnUpdate(self, dt: float): self.__dt = dt
    
    def OnStop(self):        
        self.__CurrentProject.Save()
    
    def OnDestroy(self): ...
    
    def OnGUIStart(self):
        # Hackey fix
        # TODO: Fix this later
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # type: ignore
        
        optFullscreen = True
        dockspaceFlags = imgui.DOCKNODE_NONE

        windowFlags = imgui.WINDOW_MENU_BAR | imgui.WINDOW_NO_DOCKING
        if optFullscreen:
            viewport = imgui.get_main_viewport()
            imgui.set_next_window_position(*viewport.pos)
            imgui.set_next_window_size(*viewport.size)

            imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0)
            imgui.push_style_var(imgui.STYLE_WINDOW_BORDERSIZE, 0.0)

            windowFlags |= imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_RESIZE | \
                imgui.WINDOW_NO_MOVE
            windowFlags |= imgui.WINDOW_NO_BRING_TO_FRONT_ON_FOCUS | imgui.WINDOW_NO_NAV_FOCUS

        if dockspaceFlags & imgui.DOCKNODE_PASSTHRU_CENTRAL_NODE:
            windowFlags |= imgui.WINDOW_NO_BACKGROUND

        imgui.push_style_var(imgui.STYLE_WINDOW_PADDING, ImVec2(0.0, 0.0))
        # This begins the dockspace
        imgui.begin("Dockspace", True, windowFlags)
        imgui.pop_style_var()

        if optFullscreen:
            imgui.pop_style_var(2)
        
        io = imgui.get_io()
        if io.config_flags & imgui.CONFIG_DOCKING_ENABLE:
            dockspaceID = imgui.get_id("DockSpace")
            imgui.dockspace(dockspaceID, (0.0, 0.0), dockspaceFlags)
        
    def OnGUIRender(self):
        self.ShowMenuBar()
        
        with imgui.begin("Test"):
            imgui.text("Hello, world!")
            imgui.text(f"FPS: {int(1/self.__dt)}")

    def ShowMenuBar(self) -> None:
        with imgui.begin_menu_bar():
            if imgui.begin_menu("File"):
                if imgui.menu_item("Quit", "Ctrl+Q", False, True)[0]: # type: ignore
                    self.__AppOnEventFunction(WindowCloseEvent())

                imgui.end_menu()
    
    def OnGUIEnd(self):
        imgui.end() # This ends the dockspace
