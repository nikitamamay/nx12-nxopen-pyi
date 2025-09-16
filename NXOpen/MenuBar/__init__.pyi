# module 'NXOpen.MenuBar'
#
# Automatically generated 2025-06-09T14:38:47.036775
#
"""Default documentation for NXOpen.MenuBar."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class MenuButtonTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MenuButtonType():
    """
    Available button types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CascadeButton", " - "
       "PushButton", " - "
       "ToggleButton", " - "
       "Separator", " - "
       "ApplicationButton", " - "
       "NullButton", " - "
    """
    CascadeButton = 0  # MenuButtonTypeMemberType
    PushButton = 1  # MenuButtonTypeMemberType
    ToggleButton = 2  # MenuButtonTypeMemberType
    Separator = 3  # MenuButtonTypeMemberType
    ApplicationButton = 4  # MenuButtonTypeMemberType
    NullButton = 5  # MenuButtonTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MenuButtonSensitivityStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MenuButtonSensitivityStatus():
    """
    Sensitivity Status 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sensitive", "The button is sensitive."
       "Insensitive", "The button is insensitive."
    """
    Sensitive = 0  # MenuButtonSensitivityStatusMemberType
    Insensitive = 1  # MenuButtonSensitivityStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MenuButtonToggleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MenuButtonToggle():
    """
    Toggle Status 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "On", "The toggle is on."
       "Off", "The toggle is off."
    """
    On = 0  # MenuButtonToggleMemberType
    Off = 1  # MenuButtonToggleMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MenuButton(NXOpen.TransientObject):
    """
    Implements the Object for Menu Buttons   
    
    .. versionadded:: NX6.0.0
    """
    
    class Type():
        """
        Available button types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CascadeButton", " - "
           "PushButton", " - "
           "ToggleButton", " - "
           "Separator", " - "
           "ApplicationButton", " - "
           "NullButton", " - "
        """
        CascadeButton = 0  # MenuButtonTypeMemberType
        PushButton = 1  # MenuButtonTypeMemberType
        ToggleButton = 2  # MenuButtonTypeMemberType
        Separator = 3  # MenuButtonTypeMemberType
        ApplicationButton = 4  # MenuButtonTypeMemberType
        NullButton = 5  # MenuButtonTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SensitivityStatus():
        """
        Sensitivity Status 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sensitive", "The button is sensitive."
           "Insensitive", "The button is insensitive."
        """
        Sensitive = 0  # MenuButtonSensitivityStatusMemberType
        Insensitive = 1  # MenuButtonSensitivityStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Toggle():
        """
        Toggle Status 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "On", "The toggle is on."
           "Off", "The toggle is off."
        """
        On = 0  # MenuButtonToggleMemberType
        Off = 1  # MenuButtonToggleMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is
        called, it is illegal to use the object.  In .NET and Java,
        his method is automatically called when the object is
        deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    ButtonId: int = ...
    """
    Returns  the identifier of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtonId`` 
    
    :returns:  The identifier used for the button  
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ButtonName: str = ...
    """
    Returns  the name of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtonName`` 
    
    :returns:  The name of the button  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ButtonSensitivity: MenuButtonSensitivityStatus = ...
    """
    Returns or sets  the sensitivity of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtonSensitivity`` 
    
    :returns:  The sensitivity of the button  
    :rtype: :py:class:`NXOpen.MenuBar.MenuButtonSensitivityStatus` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ButtonSensitivity`` 
    
    :param sensitivity: 
    :type sensitivity: :py:class:`NXOpen.MenuBar.MenuButtonSensitivityStatus` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ButtonType: MenuButtonType = ...
    """
    Returns  the type of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtonType`` 
    
    :returns:  The type of the button  
    :rtype: :py:class:`NXOpen.MenuBar.MenuButtonType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ButtonTypeName: str = ...
    """
    Returns  the type name of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtonTypeName`` 
    
    :returns:  The type name of the button  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ToggleStatus: MenuButtonToggle = ...
    """
    Returns or sets  the toggle status of the button.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToggleStatus`` 
    
    :returns:  The toggle status of the button  
    :rtype: :py:class:`NXOpen.MenuBar.MenuButtonToggle` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToggleStatus`` 
    
    :param toggleStatus:     
    :type toggleStatus: :py:class:`NXOpen.MenuBar.MenuButtonToggle` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class MenuBarManagerCallbackStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MenuBarManagerCallbackStatus():
    """
    Return values for action callbacks 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Continue", "Continue performing the menu item's actions."
       "Cancel", "User interaction requested inhibiting the menu item's actions."
       "OverrideStandard", "Inhibit further actions because a pre action took the place of the standard action for a standard NX menu item."
       "Warning", "Inhibit further actions because a warning condition was raised."
       "Error", "Inhibit further actions because a error condition was raised."
    """
    Continue = 0  # MenuBarManagerCallbackStatusMemberType
    Cancel = 1  # MenuBarManagerCallbackStatusMemberType
    OverrideStandard = 2  # MenuBarManagerCallbackStatusMemberType
    Warning = 3  # MenuBarManagerCallbackStatusMemberType
    Error = 4  # MenuBarManagerCallbackStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MenuBarManager():
    """
    Interface for the MenuBarManager object   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.UI`
    
    .. versionadded:: NX6.0.0
    """
    
    class CallbackStatus():
        """
        Return values for action callbacks 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Continue", "Continue performing the menu item's actions."
           "Cancel", "User interaction requested inhibiting the menu item's actions."
           "OverrideStandard", "Inhibit further actions because a pre action took the place of the standard action for a standard NX menu item."
           "Warning", "Inhibit further actions because a warning condition was raised."
           "Error", "Inhibit further actions because a error condition was raised."
        """
        Continue = 0  # MenuBarManagerCallbackStatusMemberType
        Cancel = 1  # MenuBarManagerCallbackStatusMemberType
        OverrideStandard = 2  # MenuBarManagerCallbackStatusMemberType
        Warning = 3  # MenuBarManagerCallbackStatusMemberType
        Error = 4  # MenuBarManagerCallbackStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddMenuAction(self, name: str, actionCallback: typing.Callable) -> None:
        """
        Adds the action callback.  
        
        Signature ``AddMenuAction(name, actionCallback)`` 
        
        :param name:  The name of the action.  This name must match the string used in the .men file.  
        :type name: str 
        :param actionCallback:  The method to execute for this action  
        :type actionCallback: CallableObject 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetButtonFromName(self, name: str) -> MenuButton:
        """
        Finds the MenuButton associated with the given name  
        
        Signature ``GetButtonFromName(name)`` 
        
        :param name:  The name of the button.  This name must match the button name used in the .men file.  
        :type name: str 
        :returns:  The button associated with the given name  
        :rtype: :py:class:`NXOpen.MenuBar.MenuButton` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RegisterApplication(self, name: str, initializeCallback: typing.Callable, enterCallback: typing.Callable, exitCallback: typing.Callable, supportsDrawings: bool, supportsDesignInContext: bool, supportsUndo: bool) -> int:
        """
        Registers the application
        
        Signature ``RegisterApplication(name, initializeCallback, enterCallback, exitCallback, supportsDrawings, supportsDesignInContext, supportsUndo)`` 
        
        :param name:  The name of the application.  This name must match the string used in the .men file.  
        :type name: str 
        :param initializeCallback:  The method used to initialize the application  
        :type initializeCallback: CallableObject 
        :param enterCallback:  The method called when entering the application  
        :type enterCallback: CallableObject 
        :param exitCallback:  The method called when exiting the application  
        :type exitCallback: CallableObject 
        :param supportsDrawings:  Does this application support drawings?  
        :type supportsDrawings: bool 
        :param supportsDesignInContext:  Does this application support design in context?  
        :type supportsDesignInContext: bool 
        :param supportsUndo:  Does this application support undo?  
        :type supportsUndo: bool 
        :returns:  Unique identifier for the registered application  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ApplicationSwitchRequest(self, applicationName: str) -> None:
        """
        Registers a request to switch to specified application and open the corresponding user environment.  
        
        When the running journal or program finishes, the system will attempt to switch into the target application.
        The current application does not change immediately. The argument is an application button name as specified
        and registered in the ug_main.men file. For example specify UG_APP_MODELING to try to enter the modeling application.
        Button names registered for custom application as described in "Adding Custom Applications to NX" chapter of the NX Open
        Programmer's Guide can also be used.
        
        Signature ``ApplicationSwitchRequest(applicationName)`` 
        
        :param applicationName:  Button name of requested application  
        :type applicationName: str 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Session.ApplicationSwitchImmediate` instead.
        
        License requirements: None.
        """
        ...
    
    
    def RegisterConfigureContextMenuCallback(self, name: str, description: str, configurePopupMenu: typing.Callable) -> int:
        """
        Registers a callback that is called whenever a customizable context
        menu is about to be displayed.  
        
        Each callback is registered with a short name and a longer
        description which is used to identify the callback for debugging
        purposes.
        
        Signature ``RegisterConfigureContextMenuCallback(name, description, configurePopupMenu)`` 
        
        :param name:  A short string identifying the callback  
        :type name: str 
        :param description:  A longer string describing the operation of the callback  
        :type description: str 
        :param configurePopupMenu:  Callback to register  
        :type configurePopupMenu: CallableObject 
        :returns:  Identifier of registered callback  
        :rtype: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def UnregisterConfigureContextMenuCallback(self, id: int) -> None:
        """
        Unregisters a callback for customizing context menus.  
        
        Signature ``UnregisterConfigureContextMenuCallback(id)`` 
        
        :param id:  Identifier for callback to unregister  
        :type id: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


class ContextMenuEntryTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContextMenuEntryType():
    """
    Specifies the type of the menu entry. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Submenu", "Has an attached menu structure containing more entries."
       "PushButton", "Has a command that is run when this entry is activated."
       "ToggleButton", "Displays an On/Off state."
       "Separator", "A visual divider between sections of the menu."
       "Label", "A label often used to divide and provide context to sub-groups of commands."
    """
    Submenu = 0  # ContextMenuEntryTypeMemberType
    PushButton = 1  # ContextMenuEntryTypeMemberType
    ToggleButton = 2  # ContextMenuEntryTypeMemberType
    Separator = 3  # ContextMenuEntryTypeMemberType
    Label = 4  # ContextMenuEntryTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ContextMenuEntry(NXOpen.TransientObject):
    """
    Represents an entry on a context menu.  
    
    .. versionadded:: NX8.5.0
    """
    
    class Type():
        """
        Specifies the type of the menu entry. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Submenu", "Has an attached menu structure containing more entries."
           "PushButton", "Has a command that is run when this entry is activated."
           "ToggleButton", "Displays an On/Off state."
           "Separator", "A visual divider between sections of the menu."
           "Label", "A label often used to divide and provide context to sub-groups of commands."
        """
        Submenu = 0  # ContextMenuEntryTypeMemberType
        PushButton = 1  # ContextMenuEntryTypeMemberType
        ToggleButton = 2  # ContextMenuEntryTypeMemberType
        Separator = 3  # ContextMenuEntryTypeMemberType
        Label = 4  # ContextMenuEntryTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    EntryType: ContextMenuEntryType = ...
    """
    Returns  the type of this menu entry.  
    
    <hr>
    
    Getter Method
    
    Signature ``EntryType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MenuBar.ContextMenuEntryType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsDefault: bool = ...
    """
    Returns  true if this entry is the default action for the menu.  
    
    A menu entry is marked as
    the default for the menu when it corresponds to the double-click 
    action.
    
    <hr>
    
    Getter Method
    
    Signature ``IsDefault`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsHidden: bool = ...
    """
    Returns  true if this entry is hidden on the menu.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsHidden`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    IsSensitive: bool = ...
    """
    Returns  true if the command corresponding to this entry can be run.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsSensitive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Label: str = ...
    """
    Returns  the label of this menu entry.  
    
    <hr>
    
    Getter Method
    
    Signature ``Label`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Name: str = ...
    """
    Returns  the name of this menu entry.  
    
    Some entries on the context menu may correspond to buttons on the menu bar.
    For these entries, the name that is returned is the name of that 
    :py:class:`MenuBar.MenuButton` object.
    
    For all other entries which do not correspond to a menu bar button, the
    name that is returned has no specific meaning. However, for any individual 
    action within any specific context menu, the name that is assigned to
    that action will not change.
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class MenuButtonEvent(NXOpen.TransientObject):
    """
    Implements the Event Object for Menu Buttons   
    
    .. versionadded:: NX6.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is
        called, it is illegal to use the object.  In .NET and Java,
        his method is automatically called when the object is
        deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMenuAncestors(self) -> 'list[str]':
        """
        Get the ancestors of the active button.  
        
        Signature ``GetMenuAncestors()`` 
        
        :returns:  The ancestors that caused the event to fire  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    ActiveButton: MenuButton = ...
    """
    Returns  the activated MenuButton.  
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveButton`` 
    
    :returns:  The button that caused the event to fire  
    :rtype: :py:class:`NXOpen.MenuBar.MenuButton` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ApplicationId: int = ...
    """
    Returns  the activated MenuButton's owning application identifier.  
    
    <hr>
    
    Getter Method
    
    Signature ``ApplicationId`` 
    
    :returns:  The id of the application which owns the active button  
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MenuBarName: str = ...
    """
    Returns  the name of the menu bar.  
    
    <hr>
    
    Getter Method
    
    Signature ``MenuBarName`` 
    
    :returns:  The name of the menu bar that caused the event to fire  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class ContextMenuProperties(NXOpen.TransientObject):
    """
    Provides information about the MenuBar.  
    
    ContextMenu object being customized. 
    
    .. versionadded:: NX8.5.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    Context: str = ...
    """
    Returns  a description for the context for which the menu was created 
    
    <hr>
    
    Getter Method
    
    Signature ``Context`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Location: str = ...
    """
    Returns  the location where the context menu will be displayed 
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


class ContextMenu(NXOpen.TransientObject):
    """
    Represents a Context Menu   
    
    .. versionadded:: NX8.5.0
    """
    
    def GetEntry(self, index: int) -> ContextMenuEntry:
        """
        Returns the :py:class:`MenuBar.ContextMenuEntry` at the specified index in the menu.  
        
        Signature ``GetEntry(index)`` 
        
        :param index:  index of menu entry to return  
        :type index: int 
        :returns:  the menu entry at this position  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSubmenu(self, index: int) -> ContextMenu:
        """
        Returns the submenu for the entry at the specified index in the menu.  
        
        The menu entry at this index must be of type 
        :py:class:`MenuBar.ContextMenuEntryType.Submenu <MenuBar.ContextMenuEntryType>`.
        
        Signature ``GetSubmenu(index)`` 
        
        :param index:  index of submenu to return  
        :type index: int 
        :returns:  the submenu at this position  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenu` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def HasEntryWithName(self, name: str) -> bool:
        """
        Indicates whether or not this menu contains a 
        :py:class:`MenuBar.ContextMenuEntry` which 
        has the given name.  
        
        Signature ``HasEntryWithName(name)`` 
        
        :param name:  name of menu entry to search for  
        :type name: str 
        :returns:  the menu entry with this name  
        :rtype: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEntryWithName(self, name: str) -> ContextMenuEntry:
        """
        Given the name of a menu entry, returns the first
        :py:class:`MenuBar.ContextMenuEntry` in this menu which
        matches.  
        
        Signature ``GetEntryWithName(name)`` 
        
        :param name:  name of menu entry to search for  
        :type name: str 
        :returns:  the menu entry with this name  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIndexOfEntry(self, entry: ContextMenuEntry) -> int:
        """
        Returns the index of the :py:class:`MenuBar.ContextMenuEntry`
        object within this menu.  
        
        Signature ``GetIndexOfEntry(entry)`` 
        
        :param entry:  an entry in the menu  
        :type entry: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        :returns:  the index for that menu entry  
        :rtype: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AddMenuButton(self, button: MenuButton, index: int) -> ContextMenuEntry:
        """
        Adds a menu bar button to the context menu.  
        
        Use 
        :py:meth:`MenuBar.MenuBarManager.GetButtonFromName` 
        to find the button to add to the menu.
        
        Signature ``AddMenuButton(button, index)`` 
        
        :param button:  the menu bar button to add to the menu  
        :type button: :py:class:`NXOpen.MenuBar.MenuButton` 
        :param index:  position at which to create the new button. Use -1 to add the button to the end of the menu.  
        :type index: int 
        :returns:  the new menu entry  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AddSeparator(self, index: int) -> None:
        """
        Adds a separator to the context menu.  
        
        Signature ``AddSeparator(index)`` 
        
        :param index:  position at which to create the separator. Use -1 to add the separator to the end of the menu.  
        :type index: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AddMenuLabel(self, label: str, index: int) -> ContextMenuEntry:
        """
        Adds a label to the context menu.  
        
        Signature ``AddMenuLabel(label, index)`` 
        
        :param label:  label for the label entry  
        :type label: str 
        :param index:  position at which to create the label entry. Use -1 to add the label to the end of the menu.  
        :type index: int 
        :returns:  the new menu entry  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddSubmenu(self, label: str, index: int) -> ContextMenu:
        """
        Adds a submenu to the context menu.  
        
        Signature ``AddSubmenu(label, index)`` 
        
        :param label:  label for the cascade menu  
        :type label: str 
        :param index:  position at which to create the sub-menu. Use -1 to add the sub-menu to the end of the menu.  
        :type index: int 
        :returns:  the new submenu  
        :rtype: :py:class:`NXOpen.MenuBar.ContextMenu` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultEntry(self, entry: ContextMenuEntry) -> None:
        """
        Makes a specified menu entry the default for the menu.  
        
        This entry will be displayed in bold text on the menu. It will be the action
        that is performed in response to a double-click event in the UI.
        
        The menu entry must have a type of :py:class:`MenuBar.ContextMenuEntryType.PushButton <MenuBar.ContextMenuEntryType>`
        or :py:class:`MenuBar.ContextMenuEntryType.ToggleButton <MenuBar.ContextMenuEntryType>`. 
        
        Signature ``SetDefaultEntry(entry)`` 
        
        :param entry:  the menu entry to become the default for the menu  
        :type entry: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def HideEntry(self, entry: ContextMenuEntry) -> None:
        """
        Prevents the indicated menu entry from being shown on the menu.  
        
        Signature ``HideEntry(entry)`` 
        
        :param entry:  the menu entry to hide  
        :type entry: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveEntry(self, entry: ContextMenuEntry, index: int) -> None:
        """
        Reorders the menu to move a menu entry to a new position in the list.  
        
        Signature ``MoveEntry(entry, index)`` 
        
        :param entry:  the menu entry to be moved  
        :type entry: :py:class:`NXOpen.MenuBar.ContextMenuEntry` 
        :param index:  the new position  
        :type index: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is called,
        it is illegal to use the object.  In .NET, this method is automatically
        called when the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    NumberOfEntries: int = ...
    """
    Returns  the number of :py:class:`MenuBar.ContextMenuEntry` objects in this menu.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfEntries`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """


