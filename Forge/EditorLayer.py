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
        self.__CommunicationLayer = CommunicationLayer()
        
        self.__Panels = [
            Viewport        (self.__CommunicationLayer),
            
            SceneHierarchy  (self.__CommunicationLayer),
            Properties      (self.__CommunicationLayer),
            
            Console         (self.__CommunicationLayer),
            ContentBrowser  (self.__CommunicationLayer),
            
            DebugProperties (self.__CommunicationLayer),
        ]
        
        self.SetCurrentScene(self.__CurrentProject.GetScene(0))
        self.__dt = 0.0
    
    def SetCurrentScene(self, scene: Scene) -> None:
        self.__CurrentScene = scene
        self.__CommunicationLayer.PublishEvent(SceneContextChangedEvent(scene))
    
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
        dockspaceFlags = imgui.DockNodeFlags_.none

        windowFlags = imgui.WindowFlags_.menu_bar | imgui.WindowFlags_.no_docking # type: ignore
        if optFullscreen:
            viewport = imgui.get_main_viewport()
            imgui.set_next_window_pos(viewport.pos)
            imgui.set_next_window_size(viewport.size)

            imgui.push_style_var(imgui.StyleVar_.window_rounding, 0.0) # type: ignore
            imgui.push_style_var(imgui.StyleVar_.window_border_size, 0.0) # type: ignore

            windowFlags |= imgui.WindowFlags_.no_title_bar | imgui.WindowFlags_.no_collapse | imgui.WindowFlags_.no_resize | imgui.WindowFlags_.no_move # type: ignore
            windowFlags |= imgui.WindowFlags_.no_bring_to_front_on_focus | imgui.WindowFlags_.no_nav_focus # type: ignore

        if dockspaceFlags & imgui.DockNodeFlags_.passthru_central_node: # type: ignore
            windowFlags |= imgui.WindowFlags_.no_background

        imgui.push_style_var(imgui.StyleVar_.window_padding, ImVec2(0.0, 0.0)) # type: ignore
        
        # This begins the dockspace
        imgui.begin("Dockspace", True, windowFlags)
        imgui.pop_style_var()

        if optFullscreen:
            imgui.pop_style_var(2)
        
        io = imgui.get_io()
        if io.config_flags & imgui.ConfigFlags_.docking_enable: # type: ignore
            dockspaceID = imgui.get_id("DockSpace")
            imgui.dock_space(dockspaceID, (0.0, 0.0), dockspaceFlags) # type: ignore

    def OnGUIRender(self):
        self.ShowMenuBar()
        
        for panel in self.__Panels:
            panel.OnGUIRender()

    def ShowMenuBar(self) -> None:
        with imgui_ctx.begin_menu_bar():
            if imgui.begin_menu("File"):
                if imgui.menu_item("Quit", "Ctrl+Q", False, True)[0]: # type: ignore
                    self.__AppOnEventFunction(WindowCloseEvent())

                imgui.end_menu()

    def OnGUIEnd(self):
        imgui.end() # This ends the dockspace
