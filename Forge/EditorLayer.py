from Photon import *
from Panels import *

class EditorLayer(Overlay):
    __CurrentScene: Scene
    __CurrentProject: Project
    __AppOnEventFunction: Callable[[Event], bool]
    
    __CommunicationLayer: CommunicationLayer
    
    __Panels: List[Panel]
    
    __dt: float
    
    def __init__(self, appOnEvent: Callable[[Event], bool]) -> None:
        super().__init__("EditorLayer")
        self.__AppOnEventFunction = appOnEvent
    
    def OnInitialize(self):
        self.__CurrentProject = Project(Path("DefaultProject"), "DefaultProject")
        self._EventDispatcher.AddHandler(EventType.KeyPressed, self.OnKeyPress) # type: ignore
        
        self.__Panels = [
            Viewport        (self._EventDispatcher, self.OnEvent),
            
            SceneHierarchy  (self._EventDispatcher, self.OnEvent),
            Properties      (self._EventDispatcher, self.OnEvent),
            
            Console         (self._EventDispatcher, self.OnEvent),
            ContentBrowser  (self._EventDispatcher, self.OnEvent),
            
            DebugProperties (self._EventDispatcher, self.OnEvent),
        ]
        
        self.SetCurrentScene(self.__CurrentProject.GetScene(0))
        self.__dt = 0.0
    
    def SetCurrentScene(self, scene: Scene) -> None:
        self.__CurrentScene = scene
        self.OnEvent(SceneContextChangedEvent(scene))
    
    def OnStart(self): ...

    def OnKeyPress(self, event: KeyPressedEvent) -> bool:
        control = Input.IsKeyPressed(KeyCodes.LEFT_CONTROL) or Input.IsKeyPressed(KeyCodes.RIGHT_CONTROL)
        shift   = Input.IsKeyPressed(KeyCodes.LEFT_SHIFT)   or Input.IsKeyPressed(KeyCodes.RIGHT_SHIFT)
        
        if not control and not shift:
            pass
        
        elif control and not shift:
            if event.KeyCode == KeyCodes.Q:
                self.__AppOnEventFunction(WindowCloseEvent())
        
        elif shift and not control:
            pass
        
        else: # shift and control
            pass
        
        return False

    def OnUpdate(self, dt: float):
        self.__dt = dt
        self.__CurrentScene.OnUpdateEditor(dt)
    
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
        
        for panel in self.__Panels:
            panel.OnGUIRender()

    def ShowMenuBar(self) -> None:
        with imgui.begin_menu_bar():
            if imgui.begin_menu("File"):
                if imgui.menu_item("Quit", "Ctrl+Q", False, True)[0]: # type: ignore
                    self.__AppOnEventFunction(WindowCloseEvent())

                imgui.end_menu()

    def OnGUIEnd(self):
        imgui.end() # This ends the dockspace
