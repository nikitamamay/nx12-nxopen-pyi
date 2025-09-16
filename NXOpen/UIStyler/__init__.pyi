# module 'NXOpen.UIStyler'
#
# Automatically generated 2025-06-09T14:38:48.472832
#
"""Default documentation for NXOpen.UIStyler."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class StylerItemItemTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StylerItemItemType():
    """
    Describes kind of action to be taken from callbac. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InvalidType", "Invalid item"
       "ActionButton", "Action Button item"
       "Dialog", "Dialog item"
       "RadioBox", "Radio Box item"
       "Real", "Real item"
       "ScaleReal", "Real Scale item"
       "Bitmap", "Bitmap item"
       "RowColumn", "Row Column item"
       "ButtonLayout", "Button Layout item"
       "ScrolledWindow", "Scrolled Window item"
       "ColorTool", "Color Item"
       "SelectionBox", "Section Box item"
       "Separator", "Separator item"
       "SingleSelectionList", "Single Selection List item"
       "String", "String item"
       "BeginGroup", "Begin Group item"
       "Integer", "Integer item"
       "ScaleInteger", "Scale item"
       "MultiList", "Multi List item"
       "Label", "Label item"
       "MultiLineText", "Multi-line text item"
       "TabControl", "Tab Control item"
       "OptionMenu", "Option Menu item"
       "Toggle", "Toggle item"
       "OptionToggle", "Option Toggle item"
       "ToolPalette", "Tool Palette item"
       "WideString", "Wide String item"
       "PropertyPage", "Property Page item"
       "CollapsibleGroup", "Callapsible Group item"
    """
    InvalidType = -1  # StylerItemItemTypeMemberType
    ActionButton = 0  # StylerItemItemTypeMemberType
    Dialog = 1  # StylerItemItemTypeMemberType
    RadioBox = 2  # StylerItemItemTypeMemberType
    Real = 3  # StylerItemItemTypeMemberType
    ScaleReal = 4  # StylerItemItemTypeMemberType
    Bitmap = 5  # StylerItemItemTypeMemberType
    RowColumn = 6  # StylerItemItemTypeMemberType
    ButtonLayout = 7  # StylerItemItemTypeMemberType
    ScrolledWindow = 8  # StylerItemItemTypeMemberType
    ColorTool = 9  # StylerItemItemTypeMemberType
    SelectionBox = 10  # StylerItemItemTypeMemberType
    Separator = 11  # StylerItemItemTypeMemberType
    SingleSelectionList = 12  # StylerItemItemTypeMemberType
    String = 13  # StylerItemItemTypeMemberType
    BeginGroup = 14  # StylerItemItemTypeMemberType
    Integer = 15  # StylerItemItemTypeMemberType
    ScaleInteger = 16  # StylerItemItemTypeMemberType
    MultiList = 17  # StylerItemItemTypeMemberType
    Label = 18  # StylerItemItemTypeMemberType
    MultiLineText = 19  # StylerItemItemTypeMemberType
    TabControl = 20  # StylerItemItemTypeMemberType
    OptionMenu = 21  # StylerItemItemTypeMemberType
    Toggle = 22  # StylerItemItemTypeMemberType
    OptionToggle = 23  # StylerItemItemTypeMemberType
    ToolPalette = 24  # StylerItemItemTypeMemberType
    WideString = 25  # StylerItemItemTypeMemberType
    PropertyPage = 26  # StylerItemItemTypeMemberType
    CollapsibleGroup = 27  # StylerItemItemTypeMemberType
    
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
    


class StylerItem(NXOpen.TransientObject):
    """
    Represents a Styler Item   
    
    .. versionadded:: NX5.0.0
    """
    
    class ItemType():
        """
        Describes kind of action to be taken from callbac. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InvalidType", "Invalid item"
           "ActionButton", "Action Button item"
           "Dialog", "Dialog item"
           "RadioBox", "Radio Box item"
           "Real", "Real item"
           "ScaleReal", "Real Scale item"
           "Bitmap", "Bitmap item"
           "RowColumn", "Row Column item"
           "ButtonLayout", "Button Layout item"
           "ScrolledWindow", "Scrolled Window item"
           "ColorTool", "Color Item"
           "SelectionBox", "Section Box item"
           "Separator", "Separator item"
           "SingleSelectionList", "Single Selection List item"
           "String", "String item"
           "BeginGroup", "Begin Group item"
           "Integer", "Integer item"
           "ScaleInteger", "Scale item"
           "MultiList", "Multi List item"
           "Label", "Label item"
           "MultiLineText", "Multi-line text item"
           "TabControl", "Tab Control item"
           "OptionMenu", "Option Menu item"
           "Toggle", "Toggle item"
           "OptionToggle", "Option Toggle item"
           "ToolPalette", "Tool Palette item"
           "WideString", "Wide String item"
           "PropertyPage", "Property Page item"
           "CollapsibleGroup", "Callapsible Group item"
        """
        InvalidType = -1  # StylerItemItemTypeMemberType
        ActionButton = 0  # StylerItemItemTypeMemberType
        Dialog = 1  # StylerItemItemTypeMemberType
        RadioBox = 2  # StylerItemItemTypeMemberType
        Real = 3  # StylerItemItemTypeMemberType
        ScaleReal = 4  # StylerItemItemTypeMemberType
        Bitmap = 5  # StylerItemItemTypeMemberType
        RowColumn = 6  # StylerItemItemTypeMemberType
        ButtonLayout = 7  # StylerItemItemTypeMemberType
        ScrolledWindow = 8  # StylerItemItemTypeMemberType
        ColorTool = 9  # StylerItemItemTypeMemberType
        SelectionBox = 10  # StylerItemItemTypeMemberType
        Separator = 11  # StylerItemItemTypeMemberType
        SingleSelectionList = 12  # StylerItemItemTypeMemberType
        String = 13  # StylerItemItemTypeMemberType
        BeginGroup = 14  # StylerItemItemTypeMemberType
        Integer = 15  # StylerItemItemTypeMemberType
        ScaleInteger = 16  # StylerItemItemTypeMemberType
        MultiList = 17  # StylerItemItemTypeMemberType
        Label = 18  # StylerItemItemTypeMemberType
        MultiLineText = 19  # StylerItemItemTypeMemberType
        TabControl = 20  # StylerItemItemTypeMemberType
        OptionMenu = 21  # StylerItemItemTypeMemberType
        Toggle = 22  # StylerItemItemTypeMemberType
        OptionToggle = 23  # StylerItemItemTypeMemberType
        ToolPalette = 24  # StylerItemItemTypeMemberType
        WideString = 25  # StylerItemItemTypeMemberType
        PropertyPage = 26  # StylerItemItemTypeMemberType
        CollapsibleGroup = 27  # StylerItemItemTypeMemberType
        
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
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET or Java, this 
        method is automatically called when the object is deleted by the 
        garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemType(self) -> StylerItemItemType:
        """
        Gets the dialog item type.  
        
        User can write programs to query this attribute and determine the 
        type of a dialog item in order to determine what further actions should be taken. 
        
        Signature ``GetItemType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.StylerItemItemType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InitializeAttachment(self) -> Attachment:
        """
        Returns initialized dialog item attachment information  
        
        Signature ``InitializeAttachment()`` 
        
        :returns: attachment object 
        :rtype: :py:class:`NXOpen.UIStyler.Attachment` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAttachment(self, attachment: Attachment) -> None:
        """
        Specifies the updated dialog item attachment information 
        
        Signature ``SetAttachment(attachment)`` 
        
        :param attachment: attachment object 
        :type attachment: :py:class:`NXOpen.UIStyler.Attachment` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsEqualTo(self, itemToCompare: StylerItem) -> bool:
        """
        Equates two styler items  
        
        Signature ``IsEqualTo(itemToCompare)`` 
        
        :param itemToCompare:  styler item to compare 
        :type itemToCompare: :py:class:`NXOpen.UIStyler.StylerItem` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class RealItem(StylerItem):
    """
    Represents a Real for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent:  Callback for activate event  
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmap(self, strBitmap: str) -> None:
        """
        Signature ``SetBitmap(strBitmap)`` 
        
        :param strBitmap:  Filename with .ubm, .xpm, or .bmp extension that contains a bitmap definition  
        :type strBitmap: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Set the label 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text label to display on the left side of the text field.  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Sets focus 
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: float = ...
    """
    Returns or sets  the item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  Real value to display in the text field  
    :type itemVal: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class Toggle(StylerItem):
    """
    Represents a Toggle for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers value change callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  True if launch any dialog else False  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Sets the label to display on the right side of the toggle button.  
        
        If the toggle button displays a bitmap, then this text label is used as a popup hint instead
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel: 
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Sets the sensitivity of the toggle button 
        
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex: 
        :type subitemIndex: int 
        :param type: 
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Gets the sensitivity  
        
        Signature ``GetSensitivity()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultAction(self) -> None:
        """
        Indicates that this dialog item should override the accelerator 
        on the second mouse button, which normally accelerates to the OK button.  
        
        When you set this attribute, a click on the second mouse button triggers 
        this dialog item's ON/OFF state and calls the Value Changed callback 
        instead of the action of the OK button.
        
        Signature ``SetDefaultAction()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: bool = ...
    """
    Returns or sets  an item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal: 
    :type itemVal: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the toggle
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class ColorTool(StylerItem):
    """
    Represents a ColorTool for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers value change callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Callback for value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets  the item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  Integer value to display in the text field  
    :type itemVal: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class SelectionBox(StylerItem):
    """
    Represents a SelectionBox for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent:  Activate event  
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if launch new dialog, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDoubleClickHandler(self, doubleclickevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers double click callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDoubleClickHandler(doubleclickevent, isDialogLaunchingEvent)`` 
        
        :param doubleclickevent:  Double click event  
        :type doubleclickevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if launch new dialog, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetListItems(self, values: 'list[str]') -> None:
        """
        Specifies an array of character strings for item names that are used as selectable choices for this dialog item.  
        
        Signature ``SetListItems(values)`` 
        
        :param values:  List of items  
        :type values: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetListItems(self) -> 'list[str]':
        """
        Gets an array of character strings for item names that are used as selectable choices for this dialog item.  
        
        Signature ``GetListItems()`` 
        
        :returns:  List of items  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies the descriptive text string to display below the scrolled list and above the text field.  
        
        It describes the dialog item's usage.
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Label string  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.  
        
        Signature ``DeselectSubItem(subItemIndex)`` 
        
        :param subItemIndex: 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertSubItem(self, subitemIndex: int, multiEntries: 'list[str]') -> None:
        """
        Requests that one or more entries be inserted into the list.  
        
        You can insert entries at the bottom of the list or at any position within the list.
        
        Signature ``InsertSubItem(subitemIndex, multiEntries)`` 
        
        :param subitemIndex:  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list.  
        :type subitemIndex: int 
        :param multiEntries: 
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Append(self, multiEntries: 'list[str]') -> None:
        """
        Appends one or more entries to be inserted into the list 
        
        Signature ``Append(multiEntries)`` 
        
        :param multiEntries: An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list. 
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
        Deletes sub item 
        
        Signature ``DeleteSubItem(subItemIndex)`` 
        
        :param subItemIndex: 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
        Requests that a list entry be scrolled up to the first line in the list.  
        
        Signature ``ShowSubItem(subItemIndex)`` 
        
        :param subItemIndex: 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValue(self, value: int) -> None:
        """
        Sets the value 
        
        Signature ``SetValue(value)`` 
        
        :param value: 
        :type value: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedIndexValue(self) -> int:
        """
        Gets selected index value  
        
        Signature ``GetSelectedIndexValue()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedString(self) -> str:
        """
        Gets selected string  
        
        Signature ``GetSelectedString()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of the selection box
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the selection box
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class RowColumn(StylerItem):
    """
    Represents a RowColumn for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class ToolPalette(StylerItem):
    """
    Represents a ToolPalette for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended use. 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  String label  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex:  Sub item index  
        :type subitemIndex: int 
        :param type:  True if sentivity is set otherwise False  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Gets the sensitivity of the dialog item 
        
        Signature ``GetSensitivity()`` 
        
        :returns:  True if sensitivity is set otherwise False  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefault(self, dialogId: int) -> None:
        """
        Indicates that this dialog item should override the accelerator 
        on the second mouse button, which normally accelerates to the OK button.  
        
        When you set this attribute, a click on the second mouse button triggers
        this dialog item's Activate callback instead of the action of the OK button.
        
        Signature ``SetDefault(dialogId)`` 
        
        :param dialogId: 
        :type dialogId: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets  the currently selected choice for this dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns:  Item value  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  Item value  
    :type itemVal: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class Styler():
    """
    Represents a Uistyler for UI Styler   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.UI`
    
    .. versionadded:: NX5.0.0
    """
    
    def CreateStylerDialog(self, dialogName: str) -> Dialog:
        """
        Creates an NX (UIStyler generated) "bottom" dialog.  
        
        The ".dlg" file can only be generated from the 
        Open UIStyler.  
        
        Signature ``CreateStylerDialog(dialogName)`` 
        
        :param dialogName:  Dialog name  
        :type dialogName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.Dialog` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class PageSwitchData(NXOpen.TransientObject):
    """
    Represents a PageSwitchData for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET or Java, this 
        method is automatically called when the object is deleted by the 
        garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ActivatedPage: int = ...
    """
    Returns  the activated page 
    
    <hr>
    
    Getter Method
    
    Signature ``ActivatedPage`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DeactivatedPage: int = ...
    """
    Returns  the deactivated page 
    
    <hr>
    
    Getter Method
    
    Signature ``DeactivatedPage`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class DialogStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DialogState():
    """
    Represents the dialog state 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ContinueDialog", "Continue the dialog"
       "ExitDialog", "Exit from the dialog"
    """
    ContinueDialog = 0  # DialogStateMemberType
    ExitDialog = 1  # DialogStateMemberType
    
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
    


class IntegerScale(StylerItem):
    """
    Represents a IntegerScale for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers value change callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  True if launch any dialog else False  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDragHandler(self, dragevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers drag callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDragHandler(dragevent, isDialogLaunchingEvent)`` 
        
        :param dragevent: 
        :type dragevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLimits(self, minimumValue: int, maximumValue: int) -> None:
        """
        Specifies the scale's maximum and minimum value.  
        
        Signature ``SetLimits(minimumValue, maximumValue)`` 
        
        :param minimumValue: to set minimum  
        :type minimumValue: int 
        :param maximumValue: to set maximum  
        :type maximumValue: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabels(self, minimumLabel: str, maximumLabel: str) -> None:
        """
        Specifies the text for the minimum and maximum label.  
        
        By default, the system uses the maximum/minimum 
        value as a text label.
        
        Signature ``SetLabels(minimumLabel, maximumLabel)`` 
        
        :param minimumLabel: minimum limit for label  
        :type minimumLabel: str 
        :param maximumLabel: maximum limit for label  
        :type maximumLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal: 
    :type itemVal: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of the dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: TRUE if sensitive, FALSE if insensitive 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: TRUE if sensitive, FALSE if insensitive 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets the visibility of the dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: TRUE if visible, FALSE if invisible 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: TRUE if visible, FALSE if invisible 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class ButtonLayout(StylerItem):
    """
    Represents a Button Layout for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent:  Callback for activate event  
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Sets the sensitivity 
        
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex:  If the entire dialog item should change to the new sensitivity state,         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity         state, set this field to its zero-based index.  
        :type subitemIndex: int 
        :param type:  TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Gets the sensitivity  
        
        Signature ``GetSensitivity()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedIndexValue(self) -> int:
        """
        Gets selected index  
        
        Signature ``GetSelectedIndexValue()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultAction(self) -> None:
        """
        Sets default action 
        
        Signature ``SetDefaultAction()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class WideString(StylerItem):
    """
    Represents a WideString for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended use
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Label string  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: str = ...
    """
    Returns or sets  the string value for this dialog item.  
    
    It can be the initial value that is programmatically defined, or interactively entered by the user. 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemValue: 
    :type itemValue: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of the wide string
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the wide string
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class FileOperationDataFileOperationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FileOperationDataFileOperationType():
    """
    Describes file operation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "New", "New file operation"
       "Open", "Open file operation"
       "Save", "Save file operation"
       "SaveAs", "Save as file operation"
       "SaveAll", "Save all file operation"
       "Close", "Close file operation"
       "Quit", "Quit file operation"
       "SaveAndExit", "Save and Exit file operation"
       "ChangePart", "Chaneg part file operation"
       "Execute", "Execute file operation"
       "Reopen", "Reopen file operation"
       "SaveAllAndClose", "Save all and close file operation"
       "SaveAndClose", "Save and close file operation"
       "SaveAsAndClose", "Save as and close file operation"
    """
    New = 0  # FileOperationDataFileOperationTypeMemberType
    Open = 1  # FileOperationDataFileOperationTypeMemberType
    Save = 2  # FileOperationDataFileOperationTypeMemberType
    SaveAs = 3  # FileOperationDataFileOperationTypeMemberType
    SaveAll = 4  # FileOperationDataFileOperationTypeMemberType
    Close = 5  # FileOperationDataFileOperationTypeMemberType
    Quit = 6  # FileOperationDataFileOperationTypeMemberType
    SaveAndExit = 7  # FileOperationDataFileOperationTypeMemberType
    ChangePart = 8  # FileOperationDataFileOperationTypeMemberType
    Execute = 9  # FileOperationDataFileOperationTypeMemberType
    Reopen = 10  # FileOperationDataFileOperationTypeMemberType
    SaveAllAndClose = 11  # FileOperationDataFileOperationTypeMemberType
    SaveAndClose = 12  # FileOperationDataFileOperationTypeMemberType
    SaveAsAndClose = 13  # FileOperationDataFileOperationTypeMemberType
    
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
    


class FileOperationDataFileOperationStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FileOperationDataFileOperationState():
    """
    Describes file state 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Enter", "Enter file state"
       "Exit", "Exit file state"
    """
    Enter = 0  # FileOperationDataFileOperationStateMemberType
    Exit = 1  # FileOperationDataFileOperationStateMemberType
    
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
    


class FileOperationData(NXOpen.TransientObject):
    """
    Represents a FileOperationData for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    class FileOperationType():
        """
        Describes file operation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "New", "New file operation"
           "Open", "Open file operation"
           "Save", "Save file operation"
           "SaveAs", "Save as file operation"
           "SaveAll", "Save all file operation"
           "Close", "Close file operation"
           "Quit", "Quit file operation"
           "SaveAndExit", "Save and Exit file operation"
           "ChangePart", "Chaneg part file operation"
           "Execute", "Execute file operation"
           "Reopen", "Reopen file operation"
           "SaveAllAndClose", "Save all and close file operation"
           "SaveAndClose", "Save and close file operation"
           "SaveAsAndClose", "Save as and close file operation"
        """
        New = 0  # FileOperationDataFileOperationTypeMemberType
        Open = 1  # FileOperationDataFileOperationTypeMemberType
        Save = 2  # FileOperationDataFileOperationTypeMemberType
        SaveAs = 3  # FileOperationDataFileOperationTypeMemberType
        SaveAll = 4  # FileOperationDataFileOperationTypeMemberType
        Close = 5  # FileOperationDataFileOperationTypeMemberType
        Quit = 6  # FileOperationDataFileOperationTypeMemberType
        SaveAndExit = 7  # FileOperationDataFileOperationTypeMemberType
        ChangePart = 8  # FileOperationDataFileOperationTypeMemberType
        Execute = 9  # FileOperationDataFileOperationTypeMemberType
        Reopen = 10  # FileOperationDataFileOperationTypeMemberType
        SaveAllAndClose = 11  # FileOperationDataFileOperationTypeMemberType
        SaveAndClose = 12  # FileOperationDataFileOperationTypeMemberType
        SaveAsAndClose = 13  # FileOperationDataFileOperationTypeMemberType
        
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
        
    
    
    class FileOperationState():
        """
        Describes file state 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Enter", "Enter file state"
           "Exit", "Exit file state"
        """
        Enter = 0  # FileOperationDataFileOperationStateMemberType
        Exit = 1  # FileOperationDataFileOperationStateMemberType
        
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
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET or Java, this 
        method is automatically called when the object is deleted by the 
        garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    State: FileOperationDataFileOperationState = ...
    """
    Returns  the state 
    
    <hr>
    
    Getter Method
    
    Signature ``State`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.UIStyler.FileOperationDataFileOperationState` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Type: FileOperationDataFileOperationType = ...
    """
    Returns  the file operation type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.UIStyler.FileOperationDataFileOperationType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class AttachmentAttachTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AttachmentAttachType():
    """
    Represents alignment option for Styler Item 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Dialog", "Dialog type"
       "Default", "Default type"
       "NotSet", "None type"
       "NoChange", "No change type"
       "Item", "Item type"
    """
    Dialog = 0  # AttachmentAttachTypeMemberType
    Default = 1  # AttachmentAttachTypeMemberType
    NotSet = 2  # AttachmentAttachTypeMemberType
    NoChange = 3  # AttachmentAttachTypeMemberType
    Item = 4  # AttachmentAttachTypeMemberType
    
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
    


class Attachment(NXOpen.TransientObject):
    """
    Represents an Attachment for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    class AttachType():
        """
        Represents alignment option for Styler Item 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Dialog", "Dialog type"
           "Default", "Default type"
           "NotSet", "None type"
           "NoChange", "No change type"
           "Item", "Item type"
        """
        Dialog = 0  # AttachmentAttachTypeMemberType
        Default = 1  # AttachmentAttachTypeMemberType
        NotSet = 2  # AttachmentAttachTypeMemberType
        NoChange = 3  # AttachmentAttachTypeMemberType
        Item = 4  # AttachmentAttachTypeMemberType
        
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
        Free resources associated with the instance.  
        
        After this method is called, it is illegal to use the object.  
        In .NET or Java, this method is automatically called when 
        the object is deleted by the garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCenter(self, isCenter: bool) -> None:
        """
        Sets whether the dialog item is at the center
        
        Signature ``SetCenter(isCenter)`` 
        
        :param isCenter:  center 
        :type isCenter: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAttachTypeTop(self, attachTypeTop: AttachmentAttachType) -> None:
        """
        Sets the attach type top
        
        Signature ``SetAttachTypeTop(attachTypeTop)`` 
        
        :param attachTypeTop:  attach_type_top  
        :type attachTypeTop: :py:class:`NXOpen.UIStyler.AttachmentAttachType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAttachTypeLeft(self, attachTypeLeft: AttachmentAttachType) -> None:
        """
        Sets the attach type left
        
        Signature ``SetAttachTypeLeft(attachTypeLeft)`` 
        
        :param attachTypeLeft: 
        :type attachTypeLeft: :py:class:`NXOpen.UIStyler.AttachmentAttachType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAttachTypeRight(self, attachTypeRight: AttachmentAttachType) -> None:
        """
        Sets the attach type right
        
        Signature ``SetAttachTypeRight(attachTypeRight)`` 
        
        :param attachTypeRight: 
        :type attachTypeRight: :py:class:`NXOpen.UIStyler.AttachmentAttachType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTopOffset(self, offsetTop: int) -> None:
        """
        Sets the top offset
        
        Signature ``SetTopOffset(offsetTop)`` 
        
        :param offsetTop: 
        :type offsetTop: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLeftOffset(self, offsetLeft: int) -> None:
        """
        Sets the left offset
        
        Signature ``SetLeftOffset(offsetLeft)`` 
        
        :param offsetLeft: 
        :type offsetLeft: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRightOffset(self, offsetRight: int) -> None:
        """
        Sets the right offset
        
        Signature ``SetRightOffset(offsetRight)`` 
        
        :param offsetRight: 
        :type offsetRight: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTopDialogItem(self, topItemIdentifire: str) -> None:
        """
        Sets the top dialog item
        
        Signature ``SetTopDialogItem(topItemIdentifire)`` 
        
        :param topItemIdentifire:  Top item identifier  
        :type topItemIdentifire: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLeftDialogItem(self, leftItemIdentifire: str) -> None:
        """
        Sets the left dialog item
        
        Signature ``SetLeftDialogItem(leftItemIdentifire)`` 
        
        :param leftItemIdentifire:  Left item identifier  
        :type leftItemIdentifire: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetRightDialogItem(self, rightItemIdentifire: str) -> None:
        """
        Sets the right dialog item
        
        Signature ``SetRightDialogItem(rightItemIdentifire)`` 
        
        :param rightItemIdentifire:  Right item identifier  
        :type rightItemIdentifire: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class TabControl(StylerItem):
    """
    Represents a Tab Control for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddSwitchHandler(self, switchevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers switch callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddSwitchHandler(switchevent, isDialogLaunchingEvent)`` 
        
        :param switchevent: 
        :type switchevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Sets focus 
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    PageSwitchData: PageSwitchData = ...
    """
    Returns  the page switch data
    
    <hr>
    
    Getter Method
    
    Signature ``PageSwitchData`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.UIStyler.PageSwitchData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of the dialog item 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class PropertyPage(StylerItem):
    """
    Represents a PropertyPage for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended use. 
        If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel: new label 
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Sets focus 
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of property page.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets the visibility of the dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class StringItem(StylerItem):
    """
    Represents a StringItem for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmap(self, strBitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition.  
        
        The filename must contain a UBM, XPM, or BMP 
        extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
        label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
        mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item.  
        
        Signature ``SetBitmap(strBitmap)`` 
        
        :param strBitmap:  Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition  
        :type strBitmap: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended use. If you specify a bitmap for this dialog item, 
        it uses this text as tooltip text.
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  String label to display on the left side of the text field  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog item.  
        
        When you set sensitivity to False, it grays out the 
        dialog item. This indicates that the dialog item exists but is not active.
        
        Signature ``SetSensitivity(type)`` 
        
        :param type:  TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        To get senstivity of string control 
        
        Signature ``GetSensitivity()`` 
        
        :returns:  TRUE if sensitive, FALSE if insensitive  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus 
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: str = ...
    """
    Returns or sets  the string value for this dialog item.  
    
    It can be the initial value that is programmatically 
    defined, or interactively entered by the user.
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns:  Get the String  value 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  String value  
    :type itemVal: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns:  TRUE if visible, FALSE if invisible  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class DialogItemDialogItemIndexMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DialogItemDialogItemIndex():
    """
    Describes dialog item index 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Ok", "Ok index"
       "Apply", "Apply index"
       "Back", "Back index"
       "Cancel", "Cancel index"
    """
    Ok = 0  # DialogItemDialogItemIndexMemberType
    Apply = 1  # DialogItemDialogItemIndexMemberType
    Back = 2  # DialogItemDialogItemIndexMemberType
    Cancel = 3  # DialogItemDialogItemIndexMemberType
    
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
    


class DialogItem(StylerItem):
    """
    Represents a DialogItem for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    class DialogItemIndex():
        """
        Describes dialog item index 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Ok", "Ok index"
           "Apply", "Apply index"
           "Back", "Back index"
           "Cancel", "Cancel index"
        """
        Ok = 0  # DialogItemDialogItemIndexMemberType
        Apply = 1  # DialogItemDialogItemIndexMemberType
        Back = 2  # DialogItemDialogItemIndexMemberType
        Cancel = 3  # DialogItemDialogItemIndexMemberType
        
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
        
    
    
    def AddConstructHandler(self, constructevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers construct callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddConstructHandler(constructevent, isDialogLaunchingEvent)`` 
        
        :param constructevent: 
        :type constructevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDestructHandler(self, destructevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers destruct callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDestructHandler(destructevent, isDialogLaunchingEvent)`` 
        
        :param destructevent: 
        :type destructevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddOkayHandler(self, okayevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers ok callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddOkayHandler(okayevent, isDialogLaunchingEvent)`` 
        
        :param okayevent: 
        :type okayevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddApplyHandler(self, applyevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers apply callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddApplyHandler(applyevent, isDialogLaunchingEvent)`` 
        
        :param applyevent: 
        :type applyevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPageSwitchHandler(self, switchevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers switch callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddPageSwitchHandler(switchevent, isDialogLaunchingEvent)`` 
        
        :param switchevent: 
        :type switchevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX8.5.3
        
        License requirements: None.
        """
        ...
    
    
    def AddBackHandler(self, backevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers back callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddBackHandler(backevent, isDialogLaunchingEvent)`` 
        
        :param backevent: 
        :type backevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddCancelHandler(self, cancelevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers cancel callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddCancelHandler(cancelevent, isDialogLaunchingEvent)`` 
        
        :param cancelevent: 
        :type cancelevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFileOperationHandler(self, fileoperationevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers file operation callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddFileOperationHandler(fileoperationevent, isDialogLaunchingEvent)`` 
        
        :param fileoperationevent: 
        :type fileoperationevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTitle(self, strLabel: str) -> None:
        """
        Specifies a string to display on the top border of the dialog 
        
        Signature ``SetTitle(strLabel)`` 
        
        :param strLabel: 
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, type: bool) -> None:
        """
        Specifies the sensitivity of the dialog.  
        
        Signature ``SetSensitivity(type)`` 
        
        :param type: TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetNavigationSensitivity(self, subItemIndex: DialogItemDialogItemIndex, type: bool) -> None:
        """
        Specifies the sensitivity of the navigation buttons at the bottom of the dialog.  
        
        If you set the 
        UF_STYLER_BACK_INDEX button to insensitive at creation time, the system does not show the BACK button; 
        Changing the button's sensitivity while the dialog displays does not show the Back button. 
        
        Signature ``SetNavigationSensitivity(subItemIndex, type)`` 
        
        :param subItemIndex:  Sub item index  
        :type subItemIndex: :py:class:`NXOpen.UIStyler.DialogItemDialogItemIndex` 
        :param type:  TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResize(self, type: bool) -> None:
        """
        Specifies wether dialog is allowed to resize 
        
        Signature ``SetResize(type)`` 
        
        :param type: TRUE to allow dialog to resize; FALSE to freeze the dialog size 
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetWidth(self, width: int) -> None:
        """
        Specifies the pixel width for the dialog.  
        
        You can only set this attribute when the 
        Dialog Resize attribute is set to TRUE. You cannot enter a negative number. 
        
        Signature ``SetWidth(width)`` 
        
        :param width: 
        :type width: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectionHandle(self) -> NXOpen.SelectionHandle:
        """
        Gets the selection handle for a given dialog item 
        
        Signature ``GetSelectionHandle()`` 
        
        :returns: Selection handle  
        :rtype: :py:class:`NXOpen.SelectionHandle` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    FileOperationData: FileOperationData = ...
    """
    Returns  the file operation data 
    
    <hr>
    
    Getter Method
    
    Signature ``FileOperationData`` 
    
    :returns: file operation object 
    :rtype: :py:class:`NXOpen.UIStyler.FileOperationData` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class DialogIndexMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DialogIndex():
    """
    Represents indexes 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoSubIndex", "All sub items are selected."
    """
    NoSubIndex = -1  # DialogIndexMemberType
    
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
    


class DialogResponseMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DialogResponse():
    """
    Represents dialog response 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PickResponse", "User response was a selection of objects."
       "Ok", "OK button was selected."
       "Cancel", "Cancel button was selected."
       "Back", "Back button was selected."
       "Apply", "Apply button was selected."
       "Help", "Help button was selected."
       "ObjectSelected", "Object was selected."
       "ObjectSelectedByName", "Object was selected by name."
       "CbTerminate", "Callback routine has terminated."
    """
    PickResponse = 1  # DialogResponseMemberType
    Ok = 2  # DialogResponseMemberType
    Cancel = 3  # DialogResponseMemberType
    Back = 4  # DialogResponseMemberType
    Apply = 5  # DialogResponseMemberType
    Help = 6  # DialogResponseMemberType
    ObjectSelected = 7  # DialogResponseMemberType
    ObjectSelectedByName = 8  # DialogResponseMemberType
    CbTerminate = 9  # DialogResponseMemberType
    
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
    


class IntegerItem(StylerItem):
    """
    Represents a Integer for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmap(self, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition.  
        
        The filename must contain a UBM, XPM, or BMP 
        extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
        label. When a bitmap is present, the system uses the text label as tooltip text when a user places the 
        mouse cursor over the bitmap. We recommend that you use a 16x16 bitmap for this dialog item. 
        
        Signature ``SetBitmap(bitmap)`` 
        
        :param bitmap: Filename with .ubm, .xpm, or .bmp extension that contains bitmap definition 
        :type bitmap: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog 
        item's intended use. If you specify a bitmap for this dialog item, it uses this text as tooltip text. 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  String to display on the left side of the text field. 
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Sets focus 
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets the value obtained from the text field.  
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal: 
    :type itemVal: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of Integer item 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: TRUE if sensitive, FALSE if insensitive 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: TRUE if sensitive, FALSE if insensitive 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: TRUE if the dialog item is sensitive; FALSE if insensitive 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class GroupBox(StylerItem):
    """
    Represents a GroupBox for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text label to display in the top line of the group box frame  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class OptionMenu(StylerItem):
    """
    Represents a OptionMenu for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent:  Callback for activate event  
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmap(self, bitmaps: 'list[str]') -> None:
        """
        Set an array of bitmap filenames 
        
        Signature ``SetBitmap(bitmaps)`` 
        
        :param bitmaps:  An array of one or more bitmap filenames.         If all bitmaps for the option menu reside in the same file, specify an array of just one entry,         which contains the bitmap filename for this attribute. All existing choices for the option menu         remains intact when this attribute is set. Only the bitmaps are changed. Note that the number of         bitmaps must match the number of existing choices.  
        :type bitmaps: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBitmap(self) -> 'list[str]':
        """
        Returns an array of bitmaps  
        
        Signature ``GetBitmap()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Sets label 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text to be set for the descriptive label.  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItems(self, strListArray: 'list[str]') -> None:
        """
        Set an array of items 
        
        Signature ``SetItems(strListArray)`` 
        
        :param strListArray:  An array of new choices to be used for the         dialog item. Note that this removes all existing choices (both text and bitmaps)  
        :type strListArray: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItems(self) -> 'list[str]':
        """
        Returns an array if items  
        
        Signature ``GetItems()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Sets the sensitivity 
        
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex:  If the entire dialog item should change to the new Sensitivity state,         set this field to UF_STYLER_NO_SUB_INDEX. If only one subitem should change to the new sensitivity state,        set this field to its zero-based index.  
        :type subitemIndex: int 
        :param type:  TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Gets the sensitivity  
        
        Signature ``GetSensitivity()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets  the item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param subitemIndex:  Zero-based index indicating the choice to be selected.         It must be in the range of existing choices.  
    :type subitemIndex: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class MultiSelectList(StylerItem):
    """
    Represents a MultiSelectList for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Called when a dialog user selects an entry with a double mouse click or presses Return on 
        a selected item.  
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDoubleClickHandler(self, doubleclickevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers double click callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDoubleClickHandler(doubleclickevent, isDialogLaunchingEvent)`` 
        
        :param doubleclickevent: 
        :type doubleclickevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetListItems(self, itemVal: 'list[str]') -> None:
        """
        Specifies an array of character strings for item names that are used as selectable choices for this 
        dialog item.  
        
        Signature ``SetListItems(itemVal)`` 
        
        :param itemVal: array of character strings for item names 
        :type itemVal: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetListItems(self) -> 'list[str]':
        """
        Gets an array of character strings for item names that are used as selectable choices for this 
        dialog item.  
        
        Signature ``GetListItems()`` 
        
        :returns:  An array of character strings for item names 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelected(self, subIndex: int) -> None:
        """
        Specifies particular list items to be selected.  
        
        Signature ``SetSelected(subIndex)`` 
        
        :param subIndex:  An index of particular list items to be selected  
        :type subIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAllSelected(self) -> None:
        """
        Specifies all list entry to be selected.  
        
        Signature ``SetAllSelected()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllIndicesSelected(self) -> 'list[int]':
        """
        Gets the indices of all selected list entries.  
        
        Signature ``GetAllIndicesSelected()`` 
        
        :returns:  An array of integers for item indices of selected items  
        :rtype: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllNameSelected(self) -> 'list[str]':
        """
        Gets the names of all selected list entries.  
        
        Signature ``GetAllNameSelected()`` 
        
        :returns:  An array of character strings of selected items 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Focus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``Focus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Deselect(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.  
        
        Signature ``Deselect(subItemIndex)`` 
        
        :param subItemIndex:  Index of the list entry to be deselected. 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertSubitems(self, subitemIndex: int, multiEntries: 'list[str]') -> None:
        """
        Signature ``InsertSubitems(subitemIndex, multiEntries)`` 
        
        :param subitemIndex:  Sub item index  
        :type subitemIndex: int 
        :param multiEntries:  An array of items to be inserted  
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Append(self, multiEntries: 'list[str]') -> None:
        """
        Appends one or more entries to be inserted into the list 
        
        Signature ``Append(multiEntries)`` 
        
        :param multiEntries: An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list. 
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteSubitem(self, subItemIndex: int) -> None:
        """
        Deletes sub item 
        
        Signature ``DeleteSubitem(subItemIndex)`` 
        
        :param subItemIndex:  Zero-based index of a list entry to be deleted  
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be scrolled up to the first line in the list 
        
        Signature ``ShowSubItem(subItemIndex)`` 
        
        :param subItemIndex:  Zero-based index of a list entry to be scrolled up                                 to the first line of the list. 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the senstivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets the visibility
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class CollapsibleGroup(StylerItem):
    """
    Represents a Collapsible Group for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Sets label of collapsible group
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text to be set as label  
        :type strLabel: str 
        
        .. versionadded:: NX6.0.5
        
        License requirements: None.
        """
        ...
    
    CollapseState: bool = ...
    """
    Returns or sets the collapse-state
    
    <hr>
    
    Getter Method
    
    Signature ``CollapseState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.5
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CollapseState`` 
    
    :param itemVal: 
    :type itemVal: bool 
    
    .. versionadded:: NX6.0.5
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets the visibility
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.5
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX6.0.5
    
    License requirements: None.
    """


class MultiTextBox(StylerItem):
    """
    Represents a MultiTextBox for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's 
        intended use.
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel: new label string  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemValues(self, values: 'list[str]') -> None:
        """
        Specifies the text for this dialog item.  
        
        It can be programmatically set by APIs supported in 
        different laguages,or interactively entered by the user. 
        
        Signature ``SetItemValues(values)`` 
        
        :param values: array of strings to set the values in multi                                 select List 
        :type values: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemValues(self) -> 'list[str]':
        """
        Specifies the text for this dialog item.  
        
        It can be programmatically get by APIs.  
        
        Signature ``GetItemValues()`` 
        
        :returns:  to get array of strings 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets the sensitivity of the dialog item.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: to get senstivity of dialog  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  to set senstivity of dialog  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: to get visibility of dialog  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: to set visibility of dialog  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class LabelItem(StylerItem):
    """
    Represents a Label for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def SetBitmap(self, bitmapFile: str) -> None:
        """
        Specifies a filename that contains a bitmap definition.  
        
        The filename must contain a UBM, XPM, or BMP extension. 
        When you use this field, the system displays a bitmap for this dialog item 
        instead of a text label. When a bitmap is present, the system uses 
        the text label as tooltip text when a user places the mouse cursor over the bitmap. 
        We recommend that you use a 16x16 bitmap for this dialog item. 
        
        Signature ``SetBitmap(bitmapFile)`` 
        
        :param bitmapFile: 
        :type bitmapFile: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended use.
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel: 
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the seisitivity of the dialog item
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the dialog item
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class DialogItemTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DialogItemType():
    """
    Represents dialog item type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PushButton", " - "
       "DialogItem", " - "
       "RadioBox", " - "
       "RealItem", " - "
       "RealScale", " - "
       "Bitmap", " - "
       "RowColumn", " - "
       "ButtonLayout", " - "
       "ScrolledWindow", " - "
       "ColorTool", " - "
       "SelectionBox", " - "
       "Separator", " - "
       "SingleSelectList", " - "
       "StringItem", " - "
       "GroupBox", " - "
       "IntegerItem", " - "
       "IntegerScale", " - "
       "MultiSelectList", " - "
       "LabelItem", " - "
       "MultiTextBox", " - "
       "TabControl", " - "
       "OptionMenu", " - "
       "Toggle", " - "
       "OptionToggle", " - "
       "ToolPalette", " - "
       "WideString", " - "
       "PropertyPage", " - "
       "CollapsibleGroup", " - "
    """
    PushButton = 0  # DialogItemTypeMemberType
    DialogItem = 1  # DialogItemTypeMemberType
    RadioBox = 2  # DialogItemTypeMemberType
    RealItem = 3  # DialogItemTypeMemberType
    RealScale = 4  # DialogItemTypeMemberType
    Bitmap = 5  # DialogItemTypeMemberType
    RowColumn = 6  # DialogItemTypeMemberType
    ButtonLayout = 7  # DialogItemTypeMemberType
    ScrolledWindow = 8  # DialogItemTypeMemberType
    ColorTool = 9  # DialogItemTypeMemberType
    SelectionBox = 10  # DialogItemTypeMemberType
    Separator = 11  # DialogItemTypeMemberType
    SingleSelectList = 12  # DialogItemTypeMemberType
    StringItem = 13  # DialogItemTypeMemberType
    GroupBox = 14  # DialogItemTypeMemberType
    IntegerItem = 15  # DialogItemTypeMemberType
    IntegerScale = 16  # DialogItemTypeMemberType
    MultiSelectList = 17  # DialogItemTypeMemberType
    LabelItem = 18  # DialogItemTypeMemberType
    MultiTextBox = 19  # DialogItemTypeMemberType
    TabControl = 20  # DialogItemTypeMemberType
    OptionMenu = 21  # DialogItemTypeMemberType
    Toggle = 22  # DialogItemTypeMemberType
    OptionToggle = 23  # DialogItemTypeMemberType
    ToolPalette = 24  # DialogItemTypeMemberType
    WideString = 25  # DialogItemTypeMemberType
    PropertyPage = 26  # DialogItemTypeMemberType
    CollapsibleGroup = 27  # DialogItemTypeMemberType
    
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
    


class Dialog(NXOpen.TransientObject):
    """
    Represents a DialogItem for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    class ItemType():
        """
        Represents dialog item type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PushButton", " - "
           "DialogItem", " - "
           "RadioBox", " - "
           "RealItem", " - "
           "RealScale", " - "
           "Bitmap", " - "
           "RowColumn", " - "
           "ButtonLayout", " - "
           "ScrolledWindow", " - "
           "ColorTool", " - "
           "SelectionBox", " - "
           "Separator", " - "
           "SingleSelectList", " - "
           "StringItem", " - "
           "GroupBox", " - "
           "IntegerItem", " - "
           "IntegerScale", " - "
           "MultiSelectList", " - "
           "LabelItem", " - "
           "MultiTextBox", " - "
           "TabControl", " - "
           "OptionMenu", " - "
           "Toggle", " - "
           "OptionToggle", " - "
           "ToolPalette", " - "
           "WideString", " - "
           "PropertyPage", " - "
           "CollapsibleGroup", " - "
        """
        PushButton = 0  # DialogItemTypeMemberType
        DialogItem = 1  # DialogItemTypeMemberType
        RadioBox = 2  # DialogItemTypeMemberType
        RealItem = 3  # DialogItemTypeMemberType
        RealScale = 4  # DialogItemTypeMemberType
        Bitmap = 5  # DialogItemTypeMemberType
        RowColumn = 6  # DialogItemTypeMemberType
        ButtonLayout = 7  # DialogItemTypeMemberType
        ScrolledWindow = 8  # DialogItemTypeMemberType
        ColorTool = 9  # DialogItemTypeMemberType
        SelectionBox = 10  # DialogItemTypeMemberType
        Separator = 11  # DialogItemTypeMemberType
        SingleSelectList = 12  # DialogItemTypeMemberType
        StringItem = 13  # DialogItemTypeMemberType
        GroupBox = 14  # DialogItemTypeMemberType
        IntegerItem = 15  # DialogItemTypeMemberType
        IntegerScale = 16  # DialogItemTypeMemberType
        MultiSelectList = 17  # DialogItemTypeMemberType
        LabelItem = 18  # DialogItemTypeMemberType
        MultiTextBox = 19  # DialogItemTypeMemberType
        TabControl = 20  # DialogItemTypeMemberType
        OptionMenu = 21  # DialogItemTypeMemberType
        Toggle = 22  # DialogItemTypeMemberType
        OptionToggle = 23  # DialogItemTypeMemberType
        ToolPalette = 24  # DialogItemTypeMemberType
        WideString = 25  # DialogItemTypeMemberType
        PropertyPage = 26  # DialogItemTypeMemberType
        CollapsibleGroup = 27  # DialogItemTypeMemberType
        
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
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET or Java, this 
        method is automatically called when the object is deleted by the 
        garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDialogIndex(self, itemIdentifier: str) -> DialogItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetDialogIndex(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.DialogItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPushButton(self, itemIdentifier: str) -> PushButton:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetPushButton(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.PushButton` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBitmap(self, itemIdentifier: str) -> BitMap:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetBitmap(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.BitMap` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetButtonLayout(self, itemIdentifier: str) -> ButtonLayout:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetButtonLayout(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.ButtonLayout` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColorTool(self, itemIdentifier: str) -> ColorTool:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetColorTool(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.ColorTool` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetGroupBox(self, itemIdentifier: str) -> GroupBox:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetGroupBox(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.GroupBox` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIntegerItem(self, itemIdentifier: str) -> IntegerItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetIntegerItem(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.IntegerItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIntegerScale(self, itemIdentifier: str) -> IntegerScale:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetIntegerScale(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.IntegerScale` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMultiSelectList(self, itemIdentifier: str) -> MultiSelectList:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetMultiSelectList(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.MultiSelectList` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMultiTextBox(self, itemIdentifier: str) -> MultiTextBox:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetMultiTextBox(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.MultiTextBox` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptionMenu(self, itemIdentifier: str) -> OptionMenu:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetOptionMenu(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.OptionMenu` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptionToggle(self, itemIdentifier: str) -> OptionToggle:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetOptionToggle(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.OptionToggle` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPropertyPage(self, itemIdentifier: str) -> PropertyPage:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetPropertyPage(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.PropertyPage` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRadioBox(self, itemIdentifier: str) -> RadioBox:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetRadioBox(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.RadioBox` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRealItem(self, itemIdentifier: str) -> RealItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetRealItem(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.RealItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRealScale(self, itemIdentifier: str) -> RealScale:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetRealScale(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.RealScale` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRowColumn(self, itemIdentifier: str) -> RowColumn:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetRowColumn(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.RowColumn` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetScrolledWindow(self, itemIdentifier: str) -> ScrolledWindow:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetScrolledWindow(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.ScrolledWindow` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectionBox(self, itemIdentifier: str) -> SelectionBox:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetSelectionBox(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.SelectionBox` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSeparator(self, itemIdentifier: str) -> Separator:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetSeparator(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.Separator` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSingleSelectList(self, itemIdentifier: str) -> SingleSelectList:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetSingleSelectList(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.SingleSelectList` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStringItem(self, itemIdentifier: str) -> StringItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetStringItem(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.StringItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTabControl(self, itemIdentifier: str) -> TabControl:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetTabControl(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.TabControl` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetToggle(self, itemIdentifier: str) -> Toggle:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetToggle(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.Toggle` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetToolPalette(self, itemIdentifier: str) -> ToolPalette:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetToolPalette(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.ToolPalette` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLabelItem(self, itemIdentifier: str) -> LabelItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetLabelItem(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.LabelItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCollapsibleGroup(self, itemIdentifier: str) -> CollapsibleGroup:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetCollapsibleGroup(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.CollapsibleGroup` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetWideString(self, itemIdentifier: str) -> WideString:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetWideString(itemIdentifier)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.WideString` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStylerItem(self, itemIdentifier: str, type: DialogItemType) -> StylerItem:
        """
        Gets the dialog item with specified item identifier  
        
        Signature ``GetStylerItem(itemIdentifier, type)`` 
        
        :param itemIdentifier:  Dialog name  
        :type itemIdentifier: str 
        :param type: 
        :type type: :py:class:`NXOpen.UIStyler.DialogItemType` 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.StylerItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDialogItemUsingSelectionHandle(self, select: NXOpen.SelectionHandle) -> StylerItem:
        """
        Gets the dialog item for a selection handle  
        
        Signature ``GetDialogItemUsingSelectionHandle(select)`` 
        
        :param select: Selection handle  
        :type select: :py:class:`NXOpen.SelectionHandle` 
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.StylerItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Show(self) -> DialogResponse:
        """
        Displays an NX (UIStyler generated) "bottom" dialog.  
        
        This dialog 
        is displayed to NX. Show Method can only be called once for the 
        dialog object.Once show method is called :py:meth:`UIStyler.Dialog.GetStylerItem` 
        will create any item
        
        Signature ``Show()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.DialogResponse` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RegisterWithUiMenu(self, isTopDialog: bool) -> None:
        """
        Registers the dialog with a menu item.  
        
        Signature ``RegisterWithUiMenu(isTopDialog)`` 
        
        :param isTopDialog: 
        :type isTopDialog: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class Separator(StylerItem):
    """
    Represents a Separator for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the separator
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class PushButton(StylerItem):
    """
    Represents a PushButton for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmap(self, bitmap: str) -> None:
        """
        Specifies a filename that contains a bitmap definition.  
        
        The filename must contain a UBM, XPM, or BMP 
        extension. When you use this field, the system displays a bitmap for this dialog item instead of a text 
        label. When a bitmap is present, the system uses the text label as a popup hint when a user places the 
        mouse cursor over the bitmap.  
        
        Signature ``SetBitmap(bitmap)`` 
        
        :param bitmap: the bitmap extension  
        :type bitmap: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Specifies descriptive text to display for the dialog item.  
        
        It should describe the dialog item's intended 
        use. If you specify a bitmap for this dialog item, it uses this text as tooltip text.  
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel: the label string  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultAction(self) -> None:
        """
        Sets default action 
        
        Signature ``SetDefaultAction()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the senstivity of dialog.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: senstivity of dialog  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  to set senstivity of dialog  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of dialog.  
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: to get visibility of dialog  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: to set visibility of dialog  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class ScrolledWindow(StylerItem):
    """
    Represents a ScrolledWindow for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    Sensitivity: bool = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class StylerEventReasonMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StylerEventReason():
    """
    Describes callback reason 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoReason", "No reason"
       "ActivateReason", "Activate reason"
       "ValueChangedReason", "Value changed reason"
       "DragReason", "Drag reason"
       "DoubleClickReason", "Double click reason"
       "OkReason", "Ok reason"
       "ApplyReason", "Apply reason"
       "BackReason", "BAck reason"
       "CancelReason", "Cancel reason"
       "ConstructReason", "Construct reason"
       "DestructReason", "Destruct reason"
       "FileopReason", "File operation reason"
       "SwitchReason", "Switch reason"
       "FileOperationReason", "File operation reason"
       "ExitFileOperationReason", "Exit file operation reason"
    """
    NoReason = -1  # StylerEventReasonMemberType
    ActivateReason = 0  # StylerEventReasonMemberType
    ValueChangedReason = 1  # StylerEventReasonMemberType
    DragReason = 2  # StylerEventReasonMemberType
    DoubleClickReason = 3  # StylerEventReasonMemberType
    OkReason = 4  # StylerEventReasonMemberType
    ApplyReason = 5  # StylerEventReasonMemberType
    BackReason = 6  # StylerEventReasonMemberType
    CancelReason = 7  # StylerEventReasonMemberType
    ConstructReason = 8  # StylerEventReasonMemberType
    DestructReason = 9  # StylerEventReasonMemberType
    FileopReason = 10  # StylerEventReasonMemberType
    SwitchReason = 11  # StylerEventReasonMemberType
    FileOperationReason = 12  # StylerEventReasonMemberType
    ExitFileOperationReason = 13  # StylerEventReasonMemberType
    
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
    


class StylerEventIndicatorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StylerEventIndicator():
    """
    Describes indicator value 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoValue", "No value"
       "StringValue", "String value"
       "StringPointerValue", "String pointer value"
       "IntegerValue", "Integer value"
       "IntegerPointerValue", "Integer pointer value"
       "RealValue", "Real value"
       "RealPointerValue", "Real pointer value"
       "SelectionValue", "Selection value"
       "OptionToggleValue", "Option toggle value"
    """
    NoValue = -1  # StylerEventIndicatorMemberType
    StringValue = 0  # StylerEventIndicatorMemberType
    StringPointerValue = 1  # StylerEventIndicatorMemberType
    IntegerValue = 2  # StylerEventIndicatorMemberType
    IntegerPointerValue = 3  # StylerEventIndicatorMemberType
    RealValue = 4  # StylerEventIndicatorMemberType
    RealPointerValue = 5  # StylerEventIndicatorMemberType
    SelectionValue = 6  # StylerEventIndicatorMemberType
    OptionToggleValue = 7  # StylerEventIndicatorMemberType
    
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
    


class StylerEventMiscellaneousMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StylerEventMiscellaneous():
    """
    Describes event index 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoSubIndex", "No sub index"
       "OkIndex", "Ok index"
       "ApplyIndex", "Apply index"
       "BackIndex", "Back index"
       "CancelIndex", "Cancel index"
    """
    NoSubIndex = -1  # StylerEventMiscellaneousMemberType
    OkIndex = 0  # StylerEventMiscellaneousMemberType
    ApplyIndex = 1  # StylerEventMiscellaneousMemberType
    BackIndex = 2  # StylerEventMiscellaneousMemberType
    CancelIndex = 3  # StylerEventMiscellaneousMemberType
    
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
    


class StylerEvent(NXOpen.TransientObject):
    """
    Represents a StylerEvent   
    
    .. versionadded:: NX5.0.0
    """
    
    class Reason():
        """
        Describes callback reason 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoReason", "No reason"
           "ActivateReason", "Activate reason"
           "ValueChangedReason", "Value changed reason"
           "DragReason", "Drag reason"
           "DoubleClickReason", "Double click reason"
           "OkReason", "Ok reason"
           "ApplyReason", "Apply reason"
           "BackReason", "BAck reason"
           "CancelReason", "Cancel reason"
           "ConstructReason", "Construct reason"
           "DestructReason", "Destruct reason"
           "FileopReason", "File operation reason"
           "SwitchReason", "Switch reason"
           "FileOperationReason", "File operation reason"
           "ExitFileOperationReason", "Exit file operation reason"
        """
        NoReason = -1  # StylerEventReasonMemberType
        ActivateReason = 0  # StylerEventReasonMemberType
        ValueChangedReason = 1  # StylerEventReasonMemberType
        DragReason = 2  # StylerEventReasonMemberType
        DoubleClickReason = 3  # StylerEventReasonMemberType
        OkReason = 4  # StylerEventReasonMemberType
        ApplyReason = 5  # StylerEventReasonMemberType
        BackReason = 6  # StylerEventReasonMemberType
        CancelReason = 7  # StylerEventReasonMemberType
        ConstructReason = 8  # StylerEventReasonMemberType
        DestructReason = 9  # StylerEventReasonMemberType
        FileopReason = 10  # StylerEventReasonMemberType
        SwitchReason = 11  # StylerEventReasonMemberType
        FileOperationReason = 12  # StylerEventReasonMemberType
        ExitFileOperationReason = 13  # StylerEventReasonMemberType
        
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
        
    
    
    class Indicator():
        """
        Describes indicator value 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoValue", "No value"
           "StringValue", "String value"
           "StringPointerValue", "String pointer value"
           "IntegerValue", "Integer value"
           "IntegerPointerValue", "Integer pointer value"
           "RealValue", "Real value"
           "RealPointerValue", "Real pointer value"
           "SelectionValue", "Selection value"
           "OptionToggleValue", "Option toggle value"
        """
        NoValue = -1  # StylerEventIndicatorMemberType
        StringValue = 0  # StylerEventIndicatorMemberType
        StringPointerValue = 1  # StylerEventIndicatorMemberType
        IntegerValue = 2  # StylerEventIndicatorMemberType
        IntegerPointerValue = 3  # StylerEventIndicatorMemberType
        RealValue = 4  # StylerEventIndicatorMemberType
        RealPointerValue = 5  # StylerEventIndicatorMemberType
        SelectionValue = 6  # StylerEventIndicatorMemberType
        OptionToggleValue = 7  # StylerEventIndicatorMemberType
        
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
        
    
    
    class Miscellaneous():
        """
        Describes event index 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoSubIndex", "No sub index"
           "OkIndex", "Ok index"
           "ApplyIndex", "Apply index"
           "BackIndex", "Back index"
           "CancelIndex", "Cancel index"
        """
        NoSubIndex = -1  # StylerEventMiscellaneousMemberType
        OkIndex = 0  # StylerEventMiscellaneousMemberType
        ApplyIndex = 1  # StylerEventMiscellaneousMemberType
        BackIndex = 2  # StylerEventMiscellaneousMemberType
        CancelIndex = 3  # StylerEventMiscellaneousMemberType
        
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
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET or Java, this 
        method is automatically called when the object is deleted by the 
        garbage collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStylerItem(self) -> StylerItem:
        """
        Gets the dialog item 
        
        Signature ``GetStylerItem()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.UIStyler.StylerItem` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReason(self) -> StylerEventReason:
        """
        Gets the reason for the event 
        
        Signature ``GetReason()`` 
        
        :returns:  Reason  
        :rtype: :py:class:`NXOpen.UIStyler.StylerEventReason` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class RadioBox(StylerItem):
    """
    Represents a RadioBox for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers value change callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Callback for value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Sets label 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text to be set for the descriptive label  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Sets the sensitivity 
        
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex: 
        :type subitemIndex: int 
        :param type:  TRUE if visible, FALSE if invisible  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Gets the sensitivity  
        
        Signature ``GetSensitivity()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultAction(self) -> None:
        """
        Set default action 
        
        Signature ``SetDefaultAction()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: int = ...
    """
    Returns or sets  the item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  Zero-based index indicating the choice to be selected.     It must be in the range of existing choices. 
    :type itemVal: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class SingleSelectList(StylerItem):
    """
    Represents a SingleSelectList for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent: 
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDoubleClickHandler(self, doubleclickevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers double click callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDoubleClickHandler(doubleclickevent, isDialogLaunchingEvent)`` 
        
        :param doubleclickevent: 
        :type doubleclickevent: CallableObject 
        :param isDialogLaunchingEvent: 
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSelected(self, subIndex: int) -> None:
        """
        Specifies particular list items to be selected 
        
        Signature ``SetSelected(subIndex)`` 
        
        :param subIndex:  Inndex of particular list items to be selected 
        :type subIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetListItems(self, itemVal: 'list[str]') -> None:
        """
        Specifies an array of character strings that are used as entries in the list 
        
        Signature ``SetListItems(itemVal)`` 
        
        :param itemVal:  An array of string items  
        :type itemVal: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetListItems(self) -> 'list[str]':
        """
        Gets an array of character strings that are used as entries in the list.  
        
        Signature ``GetListItems()`` 
        
        :returns:  An array of string items  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFocus(self) -> None:
        """
        Indicates that this dialog item is receiving keyboard focus.  
        
        Signature ``SetFocus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeselectSubItem(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deselected.  
        
        Signature ``DeselectSubItem(subItemIndex)`` 
        
        :param subItemIndex: 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertSubItem(self, subitemIndex: int, multiEntries: 'list[str]') -> None:
        """
        Requests one or more entries to be inserted into the list.  
        
        You can insert entries at the bottom of the list or at any position within the list. 
        
        Signature ``InsertSubItem(subitemIndex, multiEntries)`` 
        
        :param subitemIndex:  Position index where the insertion should be made. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then the new list entries are added to the bottom of the list. 
        :type subitemIndex: int 
        :param multiEntries: An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list. 
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Append(self, multiEntries: 'list[str]') -> None:
        """
        Appends one or more entries to be inserted into the list 
        
        Signature ``Append(multiEntries)`` 
        
        :param multiEntries: An array of entry names to be inserted into the list. This field is used only when more than one entry are to be inserted into the list. 
        :type multiEntries: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteSubItem(self, subItemIndex: int) -> None:
        """
        Requests a list entry to be deleted.  
        
        Signature ``DeleteSubItem(subItemIndex)`` 
        
        :param subItemIndex: Zero-based index of a list entry to be deleted. If subitem_index equals UF_STYLER_NO_SUB_INDEX, then all list entries are deleted.  
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSubItem(self, subItemIndex: int) -> None:
        """
        Requests that a list entry be scrolled up to the first line in the list 
        
        Signature ``ShowSubItem(subItemIndex)`` 
        
        :param subItemIndex:  Zero-based index of a list entry to be scrolled up to the first line of the list. 
        :type subItemIndex: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedIndexValue(self) -> int:
        """
        Gets selected index  
        
        Signature ``GetSelectedIndexValue()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedString(self) -> str:
        """
        Gets selected string  
        
        Signature ``GetSelectedString()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HasSelected(self) -> bool:
        """
        Returns whether or not an item has been selected  
        
        Signature ``HasSelected()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX7.5.1
        
        License requirements: None.
        """
        ...
    
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity of the single select list
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility of the single select list
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type: 
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class BitMap(StylerItem):
    """
    Represents a Bit Map for UI Styler.  
    
    .. versionadded:: NX5.0.0
    """
    
    def SetBitmap(self, bitmap: str) -> None:
        """
        Sets the bitmap filename.  
        
        The filename extension must be: .UBM, .XPM, or .BMP.
        The bitmap can be of any size.
        
        Signature ``SetBitmap(bitmap)`` 
        
        :param bitmap:  filename with .ubm, .xpm, or .bmp extension that contains bitmap definition  
        :type bitmap: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class OptionToggle(StylerItem):
    """
    Represents a OptionToggle for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddActivateHandler(self, activateevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers activate callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddActivateHandler(activateevent, isDialogLaunchingEvent)`` 
        
        :param activateevent:  Callback for activate event  
        :type activateevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers value change callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Callback for value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBitmaps(self, bitmaps: 'list[str]') -> None:
        """
        Set bitmaps 
        
        Signature ``SetBitmaps(bitmaps)`` 
        
        :param bitmaps:  An array of one or more bitmap filenames.         If all bitmaps for the option menu reside in the same file, specify an array of just one entry,         which contains the bitmap filename for this attribute. All existing choices for the option menu         remain intact when this attribute is set. Only the bitmaps are changed. Note that the number of         bitmaps must match the number of existing choices.  
        :type bitmaps: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabel(self, strLabel: str) -> None:
        """
        Sets label 
        
        Signature ``SetLabel(strLabel)`` 
        
        :param strLabel:  Text to be set for the tool tip.  
        :type strLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItems(self, strListArray: 'list[str]') -> None:
        """
        Sets items in the array 
        
        Signature ``SetItems(strListArray)`` 
        
        :param strListArray:  An array of new choices to be used for the dialog item.         Note that this removes all existing choices (both text and bitmaps).  
        :type strListArray: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItems(self) -> 'list[str]':
        """
        Returns the items  
        
        Signature ``GetItems()`` 
        
        :returns:  An array of items  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetItemValue(self, subitemIndex: int, setCheck: bool) -> None:
        """
        Sets item value 
        
        Signature ``SetItemValue(subitemIndex, setCheck)`` 
        
        :param subitemIndex:  Zero-based index indicating the choice to be selected.         It must be in the range of existing choices. 
        :type subitemIndex: int 
        :param setCheck:  TRUE if set, FALSE if unset.  
        :type setCheck: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetItemValue(self) -> tuple:
        """
        Returns item value  
        
        Signature ``GetItemValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (itemVal, setCheck). itemVal is a int.   Item value setCheck is a bool. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSensitivity(self, subitemIndex: int, type: bool) -> None:
        """
        Set the sesitivity 
        
        Signature ``SetSensitivity(subitemIndex, type)`` 
        
        :param subitemIndex:  If the entire dialog item should change to the new Sensitivity state,         set this field to UF_STYLER_NO_SUB_INDEX. If only one sub-item should change to the new sensitivity         state, set this field to its zero-based index.  
        :type subitemIndex: int 
        :param type:  TRUE if sensitive, FALSE if insensitive  
        :type type: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSensitivity(self) -> bool:
        """
        Returns the sesitivity  
        
        Signature ``GetSensitivity()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDefaultAction(self) -> None:
        """
        Sets default action 
        
        Signature ``SetDefaultAction()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class RealScale(StylerItem):
    """
    Represents a RealScale for UI Styler   
    
    .. versionadded:: NX5.0.0
    """
    
    def AddValueChangedHandler(self, valuechangedevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Called when a dialog user moves the slider up and down the scale.  
        
        For example, if a user moves the slider from 0.0 to 10.0, 
        the dialog calls the drag callback 100 times, one for each value that the slider moves across. 
        Do not terminate the dialog with a drag callback. The dialog should always return UF_UI_CB_CONTINUE_DIALOG.
        
        Signature ``AddValueChangedHandler(valuechangedevent, isDialogLaunchingEvent)`` 
        
        :param valuechangedevent:  Callback for value changed event  
        :type valuechangedevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDragHandler(self, dragevent: typing.Callable, isDialogLaunchingEvent: bool) -> None:
        """
        Registers dtag callback.  
        
        This method should be called before calling :py:meth:`UIStyler.Dialog.Show` or :py:meth:`UIStyler.Dialog.RegisterWithUiMenu` 
        
        Signature ``AddDragHandler(dragevent, isDialogLaunchingEvent)`` 
        
        :param dragevent:  Callback for add drag event  
        :type dragevent: CallableObject 
        :param isDialogLaunchingEvent:  TRUE if dialog is going to launch, FALSE if not  
        :type isDialogLaunchingEvent: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLimits(self, minimumValue: float, maximumValue: float) -> None:
        """
        Sets limits 
        
        Signature ``SetLimits(minimumValue, maximumValue)`` 
        
        :param minimumValue:  Real minimum value  
        :type minimumValue: float 
        :param maximumValue:  Real maximum value  
        :type maximumValue: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLabels(self, minimumLabel: str, maximumLabel: str) -> None:
        """
        Sets labels 
        
        Signature ``SetLabels(minimumLabel, maximumLabel)`` 
        
        :param minimumLabel:  String minimum label  
        :type minimumLabel: str 
        :param maximumLabel:  String maximum label  
        :type maximumLabel: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDecimalPrecision(self, digits: int) -> None:
        """
        Sets decimal precision 
        
        Signature ``SetDecimalPrecision(digits)`` 
        
        :param digits:  The number significant digits  
        :type digits: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ItemValue: float = ...
    """
    Returns or sets  the item value 
    
    <hr>
    
    Getter Method
    
    Signature ``ItemValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ItemValue`` 
    
    :param itemVal:  New real value for the slider. It must be within the min/max range  
    :type itemVal: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Sensitivity: bool = ...
    """
    Returns or sets  the sensitivity 
    
    <hr>
    
    Getter Method
    
    Signature ``Sensitivity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sensitivity`` 
    
    :param type:  TRUE if sensitive, FALSE if insensitive  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Visibility: bool = ...
    """
    Returns or sets  the visibility 
    
    <hr>
    
    Getter Method
    
    Signature ``Visibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Visibility`` 
    
    :param type:  TRUE if visible, FALSE if invisible  
    :type type: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


