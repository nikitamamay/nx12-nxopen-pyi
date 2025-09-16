# module 'NXOpen.SheetMetal'
#
# Automatically generated 2025-06-09T14:38:47.469622
#
"""Default documentation for NXOpen.SheetMetal."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct():
    """
    The members of the following structure are the display data for an
    object in a flat pattern drawing member view.  
    
    .
    Constructor: 
    NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Type: FlatPatternSettingsFlatPatternObjectType = ...
    """
    Object type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectType`
    """
    IsEnabled: int = ...
    """
    Enabled status for the object type 
    <hr>
    
    Field Value
    Type:int
    """
    Color: NXOpen.NXColor = ...
    """
    Object color 
    <hr>
    
    Field Value
    Type:Id
    """
    Font: NXOpen.ViewDependentDisplayManagerFont = ...
    """
    Object font 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.ViewDependentDisplayManagerFont`
    """
    Width: NXOpen.ViewDependentDisplayManagerWidth = ...
    """
    Object width 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.ViewDependentDisplayManagerWidth`
    """


class FlatPatternSettingsFlatPatternObjectTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlatPatternSettingsFlatPatternObjectType():
    """
    The members of the following enumerated type are used to identify
    object types to the FlatPatternView API. These are not the usual
    NX object types; they are ordinary NX objects that are known to
    the flat pattern feature for the type of outline they provide to
    a bend region, joggle region, or lightening hole. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BendCenterLine", "Deprecated"
       "BendUpCenterLine", " - "
       "BendDownCenterLine", " - "
       "BendTangentLine", " - "
       "OuterMoldLine", " - "
       "InnerMoldLine", " - "
       "ExteriorCurves", " - "
       "InteriorCurves", "Deprecated"
       "InteriorCutoutCurves", " - "
       "InteriorFeatureCurves", " - "
       "LighteningHoleCenter", " - "
       "JoggleLine", " - "
       "AddedTopGeometry", " - "
       "AddedBottomGeometry", " - "
       "ToolMarker", " - "
    """
    BendCenterLine = 0  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    BendUpCenterLine = 1  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    BendDownCenterLine = 2  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    BendTangentLine = 3  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    OuterMoldLine = 4  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    InnerMoldLine = 5  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    ExteriorCurves = 6  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    InteriorCurves = 7  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    InteriorCutoutCurves = 8  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    InteriorFeatureCurves = 9  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    LighteningHoleCenter = 10  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    JoggleLine = 11  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    AddedTopGeometry = 12  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    AddedBottomGeometry = 13  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    ToolMarker = 14  # FlatPatternSettingsFlatPatternObjectTypeMemberType
    
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
    


class FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct():
    """
    The members of the following structure are the display data for a
    callout in a flat pattern drawing member view.  
    
    .
    Constructor: 
    NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Type: str = ...
    """
    The name of the callout type.  
    
    The string is one returned by the 
    get_callout_data method, or can
    be hand-coded as the application name 'dot' the callout
    name, like this:
    "FlatPatternView.BendRadius". Neither name is
    case sensitive and blanks are not significant. This type
    of hand-coded callout type is usable as long as the
    callout type name is unique within the application name. 
    Beware of changing the defaults and loading old parts. 
    <hr>
    
    Field Value
    Type:str
    """
    IsEnabled: int = ...
    """
    Enabled status for the callout type.  
    
    <hr>
    
    Field Value
    Type:int
    """
    Name: str = ...
    """
    dialog name for the callout type.  
    
    <hr>
    
    Field Value
    Type:str
    """


class FlatPatternSettings(NXOpen.TaggedObject):
    """
    Provides access to object and callout properties for sheet-metal data in
    flat pattern views on drawings.  
    
    The class is created upon a query to
    obtain the FlatPatternView object from either a view (style) or a 
    part (preferences). 
    This class is not created directly by the user.
    
    .. versionadded:: NX5.0.0
    """
    
    class FlatPatternObjectType():
        """
        The members of the following enumerated type are used to identify
        object types to the FlatPatternView API. These are not the usual
        NX object types; they are ordinary NX objects that are known to
        the flat pattern feature for the type of outline they provide to
        a bend region, joggle region, or lightening hole. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BendCenterLine", "Deprecated"
           "BendUpCenterLine", " - "
           "BendDownCenterLine", " - "
           "BendTangentLine", " - "
           "OuterMoldLine", " - "
           "InnerMoldLine", " - "
           "ExteriorCurves", " - "
           "InteriorCurves", "Deprecated"
           "InteriorCutoutCurves", " - "
           "InteriorFeatureCurves", " - "
           "LighteningHoleCenter", " - "
           "JoggleLine", " - "
           "AddedTopGeometry", " - "
           "AddedBottomGeometry", " - "
           "ToolMarker", " - "
        """
        BendCenterLine = 0  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        BendUpCenterLine = 1  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        BendDownCenterLine = 2  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        BendTangentLine = 3  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        OuterMoldLine = 4  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        InnerMoldLine = 5  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        ExteriorCurves = 6  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        InteriorCurves = 7  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        InteriorCutoutCurves = 8  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        InteriorFeatureCurves = 9  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        LighteningHoleCenter = 10  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        JoggleLine = 11  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        AddedTopGeometry = 12  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        AddedBottomGeometry = 13  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        ToolMarker = 14  # FlatPatternSettingsFlatPatternObjectTypeMemberType
        
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
        
    
    
    class FlatPatternObjectTypeDisplay():
        """
        The members of the following structure are the display data for an
        object in a flat pattern drawing member view.  
        
        .
        Constructor: 
        NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectTypeDisplay()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Type: FlatPatternSettingsFlatPatternObjectType = ...
        """
        Object type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectType`
        """
        IsEnabled: int = ...
        """
        Enabled status for the object type 
        <hr>
        
        Field Value
        Type:int
        """
        Color: NXOpen.NXColor = ...
        """
        Object color 
        <hr>
        
        Field Value
        Type:Id
        """
        Font: NXOpen.ViewDependentDisplayManagerFont = ...
        """
        Object font 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.ViewDependentDisplayManagerFont`
        """
        Width: NXOpen.ViewDependentDisplayManagerWidth = ...
        """
        Object width 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.ViewDependentDisplayManagerWidth`
        """
    
    
    class FlatPatternCalloutTypeDisplay():
        """
        The members of the following structure are the display data for a
        callout in a flat pattern drawing member view.  
        
        .
        Constructor: 
        NXOpen.SheetMetal.FlatPatternSettings.FlatPatternCalloutTypeDisplay()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Type: str = ...
        """
        The name of the callout type.  
        
        The string is one returned by the 
        get_callout_data method, or can
        be hand-coded as the application name 'dot' the callout
        name, like this:
        "FlatPatternView.BendRadius". Neither name is
        case sensitive and blanks are not significant. This type
        of hand-coded callout type is usable as long as the
        callout type name is unique within the application name. 
        Beware of changing the defaults and loading old parts. 
        <hr>
        
        Field Value
        Type:str
        """
        IsEnabled: int = ...
        """
        Enabled status for the callout type.  
        
        <hr>
        
        Field Value
        Type:int
        """
        Name: str = ...
        """
        dialog name for the callout type.  
        
        <hr>
        
        Field Value
        Type:str
        """
    
    
    def GetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettingsFlatPatternObjectType) -> FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct:
        """
        Returns the display data for a flat pattern object type.  
        
        Signature ``GetFlatPatternObjectTypeDisplay(objectType)`` 
        
        :param objectType:  The object type for which to return the display data.  
        :type objectType: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectType` 
        :returns:  The display data for the flat pattern object type.  
        :rtype: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetFlatPatternObjectTypeDisplay(self, objectType: FlatPatternSettingsFlatPatternObjectType, displayData: FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct) -> None:
        """
        Sets the display data for a flat pattern object type.  
        
        Signature ``SetFlatPatternObjectTypeDisplay(objectType, displayData)`` 
        
        :param objectType:  The object type for which to get the display data.  
        :type objectType: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectType` 
        :param displayData:  The display data for the flat pattern object type.  
        :type displayData: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct:
        """
        Returns the display data for a callout type.  
        
        The name member of the
        :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct`
        is separately allocated from the callout_type argument string. 
        In some cases the new string will contain an
        extended form of the callout_type passed in, and that form should
        be used for subsequent calls, without modification.  
        
        Signature ``GetFlatPatternCalloutTypeDisplay(calloutType)`` 
        
        :param calloutType:  The name of the callout type for which to get the display data.  
        :type calloutType: str 
        :returns:  The display data for the callout type.  
        :rtype: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct) -> None:
        """
        Sets the display data for a callout type.  
        
        Signature ``SetFlatPatternCalloutTypeDisplay(calloutType, displayData)`` 
        
        :param calloutType:  The name of the callout type for which to set the display data.  
        :type calloutType: str 
        :param displayData:  The display data for the callout type.  
        :type displayData: :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFlatPatternAllObjectTypeDisplay(self) -> 'list[FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct]':
        """
        Returns the types, colors, fonts, widths, and enabled status for all
        the available object types.  
        
        Signature ``GetFlatPatternAllObjectTypeDisplay()`` 
        
        :returns:  Array of structures with the object type display data.  
        :rtype: list of :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternObjectTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFlatPatternAllCalloutTypeDisplay(self) -> 'list[FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct]':
        """
        Returns the dialog names, identifiers, and enabled status for all the
        available callout types.  
        
        Signature ``GetFlatPatternAllCalloutTypeDisplay()`` 
        
        :returns:  Array of structures with the callout type display data.  
        :rtype: list of :py:class:`NXOpen.SheetMetal.FlatPatternSettingsFlatPatternCalloutTypeDisplay_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    Null: FlatPatternSettings = ...  # unknown typename


