# module 'NXOpen.Layout2d'
#
# Automatically generated 2025-06-09T14:38:46.886079
#
"""Default documentation for NXOpen.Layout2d."""

import typing

import NXOpen
import NXOpen.Display
import NXOpen.Drafting
import NXOpen.Drawings
import NXOpen.Gateway
import NXOpen.GeometricUtilities
import NXOpen.PDM



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class Layout2dDefinitionLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Layout2dDefinitionLocation():
    """
    Definition location 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unspecified", " - "
       "Local", " - "
       "Native", " - "
       "TcEng", " - "
    """
    Unspecified = 0  # Layout2dDefinitionLocationMemberType
    Local = 1  # Layout2dDefinitionLocationMemberType
    Native = 2  # Layout2dDefinitionLocationMemberType
    TcEng = 3  # Layout2dDefinitionLocationMemberType
    
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
    


class ConvertLayoutToSheetBuilderSheetProjectionAngleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConvertLayoutToSheetBuilderSheetProjectionAngleType():
    """
    the drawing sheet projection angle 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "First", "first angle projection"
       "Third", "third angle projection"
    """
    First = 0  # ConvertLayoutToSheetBuilderSheetProjectionAngleTypeMemberType
    Third = 1  # ConvertLayoutToSheetBuilderSheetProjectionAngleTypeMemberType
    
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
    


class ConvertLayoutToSheetBuilder(NXOpen.Builder):
    """
    Represents a Builder for converting Layout to drawing sheet   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.LayoutDrawingSheetCollection.CreateConvertLayoutToSheetBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    class SheetProjectionAngleType():
        """
        the drawing sheet projection angle 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "First", "first angle projection"
           "Third", "third angle projection"
        """
        First = 0  # ConvertLayoutToSheetBuilderSheetProjectionAngleTypeMemberType
        Third = 1  # ConvertLayoutToSheetBuilderSheetProjectionAngleTypeMemberType
        
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
        
    
    
    def GetScale(self) -> tuple:
        """
        Gets the sheet scale 
        
        Signature ``GetScale()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (numerator, denominator). numerator is a float.   the scale numerator denominator is a float.   the scale denominator 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetScale(self, numerator: float, denominator: float) -> None:
        """
        Sets the sheet scale 
        
        Signature ``SetScale(numerator, denominator)`` 
        
        :param numerator:  the scale numerator  
        :type numerator: float 
        :param denominator:  the scale denominator  
        :type denominator: float 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    Name: str = ...
    """
    Returns or sets  the name of the drawing sheet to be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  the drawing sheet name  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  drawing sheet name  
    :type name: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Number: str = ...
    """
    Returns or sets  the number of the drawing sheet to be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns:  the drawing sheet number  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number:  the drawing sheet number  
    :type number: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ProjectionAngleType: ConvertLayoutToSheetBuilderSheetProjectionAngleType = ...
    """
    Returns or sets  the sheet projection angle option 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionAngleType`` 
    
    :returns:  the projection angle type  
    :rtype: :py:class:`NXOpen.Layout2d.ConvertLayoutToSheetBuilderSheetProjectionAngleType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionAngleType`` 
    
    :param type:  the projection angle type  
    :type type: :py:class:`NXOpen.Layout2d.ConvertLayoutToSheetBuilderSheetProjectionAngleType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Revision: str = ...
    """
    Returns or sets  the revision of the drawing sheet to be created 
    
    <hr>
    
    Getter Method
    
    Signature ``Revision`` 
    
    :returns:  the drawing sheet revision  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Revision`` 
    
    :param revision:  the drawing sheet revision  
    :type revision: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    SecondaryNumber: str = ...
    """
    Returns or sets  the secondary number of the drawing sheet to be created 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryNumber`` 
    
    :returns:  the drawing sheet secondary number  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryNumber`` 
    
    :param secondaryNumber:  the drawing sheet secondary number  
    :type secondaryNumber: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    SelectLayoutSheetView: NXOpen.SelectView = ...
    """
    Returns  the select layout sheet view to convert
    
    <hr>
    
    Getter Method
    
    Signature ``SelectLayoutSheetView`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectView` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ConvertLayoutToSheetBuilder = ...  # unknown typename


class Layout2dDefinitionStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Layout2dDefinitionStatus():
    """
    Definition Status 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", " - "
       "Synced", " - "
       "Newer", " - "
       "Older", " - "
       "Missing", " - "
    """
    Unknown = 0  # Layout2dDefinitionStatusMemberType
    Synced = 1  # Layout2dDefinitionStatusMemberType
    Newer = 2  # Layout2dDefinitionStatusMemberType
    Older = 3  # Layout2dDefinitionStatusMemberType
    Missing = 4  # Layout2dDefinitionStatusMemberType
    
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
    


class DefineComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Define 2D component functionality which will define
    *  a 2D Component and stores its definition in the Reuse Library               
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateDefineComponentBuilder`
    
    Default values.
    
    ===========================  =============
    Property                     Value
    ===========================  =============
    ImageCapture.CaptureMethod   GraphicsArea 
    ---------------------------  -------------
    ImageCapture.Format          Bmp 
    ---------------------------  -------------
    ImageCapture.Size            Pixels64 
    ===========================  =============
    
    .. versionadded:: NX10.0.0
    """
    
    def SetPath(self, path: str) -> None:
        """
        Sets the path to store the 2D Component 
        
        Signature ``SetPath(path)`` 
        
        :param path:  location of component  
        :type path: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
        Sets the location type of the component indicating local, native or team center
        
        Signature ``SetLocation(locationType)`` 
        
        :param locationType: 
        :type locationType: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    AnchorPoint: NXOpen.Point = ...
    """
    Returns or sets  the anchor point to define the 2D Component
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorPoint`` 
    
    :param anchorPoint: 
    :type anchorPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ComponentName: ComponentNameBuilder = ...
    """
    Returns  the 2D Component Name defines the name for the new created definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentNameBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Contents: NXOpen.SelectNXObjectList = ...
    """
    Returns  the select objects to create a 2D Component definition
    
    <hr>
    
    Getter Method
    
    Signature ``Contents`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ImageCapture: NXOpen.Gateway.ImageCaptureBuilder = ...
    """
    Returns  the image capture builder used to create an image for the definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageCapture`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ImageName: str = ...
    """
    Returns or sets  the 2D Component image name for the new created definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageName`` 
    
    :param imageName: 
    :type imageName: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: DefineComponentBuilder = ...  # unknown typename


class ComponentNameBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    This class is used to construct the component name and part file name block, if it is in
    manage mode, we also have item number, item revision and item name .  
    
    .. versionadded:: NX10.0.0
    """
    
    def SetPartOperationBuilder(self, partOperationBuilder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
        Sets :py:class:`NXOpen.PDM.PartOperationCreateBuilder` 
        
        Signature ``SetPartOperationBuilder(partOperationBuilder)`` 
        
        :param partOperationBuilder: 
        :type partOperationBuilder: :py:class:`NXOpen.PDM.PartOperationCreateBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    Location: Layout2dDefinitionLocation = ...
    """
    Returns or sets  the location type of the component indicating local, native or team center  
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param location: 
    :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Name: str = ...
    """
    Returns or sets  the JA method support for accessing and setting Component Name value,
    NOTE: Client must free the returned TEXT_p_t* with TEXT_free
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    PartName: str = ...
    """
    Returns or sets  the JA method support for accessing and setting Component part file mame value,
    NOTE: Client must free the returned TEXT_p_t* with TEXT_free 
    
    <hr>
    
    Getter Method
    
    Signature ``PartName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PartName`` 
    
    :param partName: 
    :type partName: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Null: ComponentNameBuilder = ...  # unknown typename


class EditComponentSettingsBuilder(NXOpen.Drafting.BaseEditSettingsBuilder):
    """
    Represents a :py:class:`NXOpen.Layout2d.EditComponentSettingsBuilder` builder.  
    
    It provides an interface for editing layout2d component settings. 
    The committed object is the component with the new settings 
    To create a new instance of this class, use :py:meth:`NXOpen.Drafting.SettingsManager.CreateLayout2dEditComponentSettingsBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
        Inherit Settings From Selected Objects 
        
        Signature ``InheritSettingsFromSelectedObject(selectedObject)`` 
        
        :param selectedObject:  The selected 2D Component object.                                                                         None is not allowed.  
        :type selectedObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
        Inherit Settings From Customer Default 
        
        Signature ``InheritSettingsFromCustomerDefault()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def InheritSettingsFromPreferences(self) -> None:
        """
        Inherit Settings From Preference 
        
        Signature ``InheritSettingsFromPreferences()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    ComponentSettings: ComponentSettingsBlockBuilder = ...
    """
    Returns  the 2D Component settings block builder which holds the component settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentSettingsBlockBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: EditComponentSettingsBuilder = ...  # unknown typename


class NewComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for New 2D Component functionality which will create an empty 2D Component 
    instance and stores its definition in the local 2D Component folder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateNewComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Owner: NXOpen.NXObject = ...
    """
    Returns or sets  the owner to create the 2D Component, can be either a drawing sheet, a drawing view
    a sketch or a 2D Component 
    
    <hr>
    
    Getter Method
    
    Signature ``Owner`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Owner`` 
    
    :param owner: 
    :type owner: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: NewComponentBuilder = ...  # unknown typename


class ComponentSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Layout2d.ComponentSettingsBuilder`
    This builder stores the information of the 2D Component settings
    
    .. versionadded:: NX10.0.0
    """
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    AutomaticUpdate: bool = ...
    """
    Returns or sets  the flag to do automatic update or not 
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticUpdate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticUpdate`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    KeepEditedPartsOpen: bool = ...
    """
    Returns or sets  the flag indicating whether to keep edited parts open or not 
    
    <hr>
    
    Getter Method
    
    Signature ``KeepEditedPartsOpen`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``KeepEditedPartsOpen`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ShowAnnotations: bool = ...
    """
    Returns or sets  the flag to show annotations or not 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowAnnotations`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowAnnotations`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ShowDimensions: bool = ...
    """
    Returns or sets  the flag to show dimensions or not 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowDimensions`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowDimensions`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ShowReferenceGeometry: bool = ...
    """
    Returns or sets  the flag to show reference geometry or not 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowReferenceGeometry`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowReferenceGeometry`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: ComponentSettingsBuilder = ...  # unknown typename


class LayoutDrawingSheet(NXOpen.Drawings.DrawingSheet):
    """
    Represents a Layout drawing sheet.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Layout2d.LayoutDrawingSheetBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: LayoutDrawingSheet = ...  # unknown typename


class LocalDefinitionFolder(NXOpen.NXObject):
    """
    Represents a local definition folder.  
    
    This folder contains 2D Component definitions stored in 
    the current part 
    To create or edit an instance of this class, use :py:class:`NXOpen.Layout2d.LocalDefinitionFolderBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: LocalDefinitionFolder = ...  # unknown typename


class CreateComponentFrom3DSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
        Inherit Settings From Customer Default 
        
        Signature ``InheritSettingsFromCustomerDefault()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def InheritSettingsFromPreferences(self) -> None:
        """
        Inherit Settings From Preference 
        
        Signature ``InheritSettingsFromPreferences()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    AutomaticallyStartInsert2DComponentCommand: bool = ...
    """
    Returns or sets  the settings to determines whether or not automatically start insert 2D component command
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticallyStartInsert2DComponentCommand`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticallyStartInsert2DComponentCommand`` 
    
    :param automaticallyStartInsert2DComponentCommand: 
    :type automaticallyStartInsert2DComponentCommand: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Color: int = ...
    """
    Returns or sets   the settings to specifies the 2D component curves color.  
    
    <hr>
    
    Getter Method
    
    Signature ``Color`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Color`` 
    
    :param color: 
    :type color: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    ColorOption: NXOpen.Display.DynamicSectionTypesCurveColorOption = ...
    """
    Returns or sets   the settings to specifies how the color of the 2D component curves is defined.  
    
    <hr>
    
    Getter Method
    
    Signature ``ColorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Display.DynamicSectionTypesCurveColorOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ColorOption`` 
    
    :param colorOption: 
    :type colorOption: :py:class:`NXOpen.Display.DynamicSectionTypesCurveColorOption` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    CreateSingle2DComponentDefinition: bool = ...
    """
    Returns or sets  the settings to determines whether or not create single 2D component definition
    
    <hr>
    
    Getter Method
    
    Signature ``CreateSingle2DComponentDefinition`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateSingle2DComponentDefinition`` 
    
    :param createSingle2DComponentDefinition: 
    :type createSingle2DComponentDefinition: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Null: CreateComponentFrom3DSettingsBuilder = ...  # unknown typename


class MakeComponentUniqueBuilder(NXOpen.Builder):
    """
    Represents a Builder for Make 2D Component unique functionality which will create a
    *  new definition of the selected 2D Component instance   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateMakeComponentUniqueBuilder`
    
    Default values.
    
    ===========================  =============
    Property                     Value
    ===========================  =============
    ImageCapture.CaptureMethod   GraphicsArea 
    ---------------------------  -------------
    ImageCapture.Format          Bmp 
    ---------------------------  -------------
    ImageCapture.Size            Pixels64 
    ===========================  =============
    
    .. versionadded:: NX10.0.0
    """
    
    def SetPath(self, path: str) -> None:
        """
        Sets the path to store the 2D Component
        
        Signature ``SetPath(path)`` 
        
        :param path:  location of component  
        :type path: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
        Sets the location type of the 2D Component indicating local, native or team center
        
        Signature ``SetLocation(locationType)`` 
        
        :param locationType: 
        :type locationType: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    Component: SelectComponent = ...
    """
    Returns  the select 2D Comoponent instance to create definition 
    
    <hr>
    
    Getter Method
    
    Signature ``Component`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.SelectComponent` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ComponentName: ComponentNameBuilder = ...
    """
    Returns  the 2D Component Name defines the name for the new created definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentNameBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ImageCapture: NXOpen.Gateway.ImageCaptureBuilder = ...
    """
    Returns  the image capture builder used to create an image for the new definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageCapture`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ImageName: str = ...
    """
    Returns or sets  the 2D Component image name for the new created definition 
    
    <hr>
    
    Getter Method
    
    Signature ``ImageName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImageName`` 
    
    :param imageName: 
    :type imageName: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: MakeComponentUniqueBuilder = ...  # unknown typename


class ReparentComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Reparent 2D Component functionality which will reparents
    *   the selected 2D Component contents from another 2D Component definition.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateReparentComponentBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def AddComponents(self, components: 'list[Component]') -> None:
        """
        Add a list of 2D Components
        
        Signature ``AddComponents(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Components: SelectComponentList = ...
    """
    Returns  the select 2D Components to reparent the definitions 
    
    <hr>
    
    Getter Method
    
    Signature ``Components`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.SelectComponentList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    CreateCopy: bool = ...
    """
    Returns or sets  the flag to distinguish copy and cut operations 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateCopy`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateCopy`` 
    
    :param createCopy: 
    :type createCopy: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Target: NXOpen.DisplayableObject = ...
    """
    Returns or sets  the target of 2D Components reparent operation 
    
    <hr>
    
    Getter Method
    
    Signature ``Target`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Target`` 
    
    :param target: 
    :type target: :py:class:`NXOpen.DisplayableObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: ReparentComponentBuilder = ...  # unknown typename


class PublishComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Publish 2D Component functionality which will allow
    local definitions to be exported into external storage locations   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreatePublishComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    DestinationPath: str = ...
    """
    Returns or sets  the path of folder to publish into 
    
    <hr>
    
    Getter Method
    
    Signature ``DestinationPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DestinationPath`` 
    
    :param destinationPath: 
    :type destinationPath: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    IsFolder: bool = ...
    """
    Returns or sets  the type of object to pblish.  
    
    Can be definition or folder 
    
    <hr>
    
    Getter Method
    
    Signature ``IsFolder`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    
    <hr>
    
    Setter Method
    
    Signature ``IsFolder`` 
    
    :param isFolder: 
    :type isFolder: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Location: Layout2dDefinitionLocation = ...
    """
    Returns or sets  the location type of folder to publish into 
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param locationType: 
    :type locationType: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    OriginPath: str = ...
    """
    Returns or sets  the path of folder or definition to publish 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginPath`` 
    
    :param originPath: 
    :type originPath: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: PublishComponentBuilder = ...  # unknown typename


class AssemblyCreationSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Layout2d.AssemblyCreationSettingsBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
        Inherit Settings From Customer Default 
        
        Signature ``InheritSettingsFromCustomerDefault()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def InheritSettingsFromPreferences(self) -> None:
        """
        Inherit Settings From Preference 
        
        Signature ``InheritSettingsFromPreferences()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    AutomaticallyStartModelingApplication: bool = ...
    """
    Returns or sets   the settings todetermines whether or not automatically start modeling application
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticallyStartModelingApplication`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticallyStartModelingApplication`` 
    
    :param automaticallyStartModelingApplication: 
    :type automaticallyStartModelingApplication: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Transfer2dComponentAnnotation: bool = ...
    """
    Returns or sets  the settings to determines whether or not transfer 2d component annotation
    
    <hr>
    
    Getter Method
    
    Signature ``Transfer2dComponentAnnotation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Transfer2dComponentAnnotation`` 
    
    :param transfer2dComponentAnnotation: 
    :type transfer2dComponentAnnotation: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    TransferTopLevelSketchAnnotation: bool = ...
    """
    Returns or sets  the settings to determines whether or not transfer top level sketch annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``TransferTopLevelSketchAnnotation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransferTopLevelSketchAnnotation`` 
    
    :param transferTopLevelSketchAnnotation: 
    :type transferTopLevelSketchAnnotation: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Null: AssemblyCreationSettingsBuilder = ...  # unknown typename


class LocalDefinitionFolderBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Layout2d.LocalDefinitionFolderBuilder`.  
    
    A local definition folder contains 2D Component definitions stored in 
    the current part.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.LocalDefinitionFolderCollection.CreateLocalDefinitionFolderBuilder`
    
    .. versionadded:: NX10.0.0
    """
    FolderName: str = ...
    """
    Returns or sets  the current folder name
    
    <hr>
    
    Getter Method
    
    Signature ``FolderName`` 
    
    :returns:  folder name 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    
    <hr>
    
    Setter Method
    
    Signature ``FolderName`` 
    
    :param folderName:  folder name 
    :type folderName: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Parent: LocalDefinitionFolder = ...
    """
    Returns or sets  the current folder's parent 
    
    <hr>
    
    Getter Method
    
    Signature ``Parent`` 
    
    :returns:  parent local definition folder 
    :rtype: :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    
    <hr>
    
    Setter Method
    
    Signature ``Parent`` 
    
    :param parentfolder:  parent local definition folder 
    :type parentfolder: :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: LocalDefinitionFolderBuilder = ...  # unknown typename


class SmashComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Smash 2D Component functionality which will break instances
    *  of 2D Components into its constituent pieces, we can have multiple committed objects   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateSmashComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Components: SelectComponentList = ...
    """
    Returns  the select 2D Component instances to smash 
    
    <hr>
    
    Getter Method
    
    Signature ``Components`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.SelectComponentList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SmashComponentBuilder = ...  # unknown typename


class GeneralPreferencesBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Layout2d.GeneralPreferencesBuilder`
    This builder stores the general layout preferences
    
    .. versionadded:: NX12.0.0
    """
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    ShowLayoutOrigin: bool = ...
    """
    Returns or sets  the flag controling the visibility of layout origin symbols in the session
    
    <hr>
    
    Getter Method
    
    Signature ``ShowLayoutOrigin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowLayoutOrigin`` 
    
    :param toggle: 
    :type toggle: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: GeneralPreferencesBuilder = ...  # unknown typename


class DefineComponentAnchorPointBuilder(NXOpen.Builder):
    """
    Represents a Builder for Define Component Anchor Point functionality which will define the anchor
    *  point location of a 2D Component instance   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateDefineComponentAnchorPointBuilder`
    
    .. versionadded:: NX10.0.0
    """
    AnchorPoint: NXOpen.Point = ...
    """
    Returns or sets  the anchor point of a 2D Component 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorPoint`` 
    
    :param anchorPoint: 
    :type anchorPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: DefineComponentAnchorPointBuilder = ...  # unknown typename


class LayoutDrawingSheetBuilder(NXOpen.Drawings.DrawingSheetBuilder):
    """
    Represents a Builder for creating :py:class:`Layout2d.LayoutDrawingSheet`s   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.LayoutDrawingSheetCollection.CreateLayoutDrawingSheetBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: LayoutDrawingSheetBuilder = ...  # unknown typename


class LocalDefinitionFolderCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` objects.  
    
    A local definition folder contains 2D Component definitions stored in 
    the current part 
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateLocalDefinitionFolderBuilder(self, currentFolder: LocalDefinitionFolder) -> LocalDefinitionFolderBuilder:
        """
        Creates local definition folder builder instance.  
        
        The builder allows operations such as Creation, Edit and Deletion
        of local definition folders. These operations are Undo/Redo supported.
        
        Signature ``CreateLocalDefinitionFolderBuilder(currentFolder)`` 
        
        :param currentFolder:  :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` to be set as current folder.                                                                                      If None, create a new folder  
        :type currentFolder: :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` 
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.LocalDefinitionFolderBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def FindObject(self, name: str) -> LocalDefinitionFolder:
        """
        Finds the :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` with the given name.  
        
        An exception will be thrown if no object can be found with the given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.LocalDefinitionFolder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    


class ExportComponentHierarchyBuilder(NXOpen.Builder):
    """
    Represents a Builder for export component 2D hierarchy   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateExportComponentHierarchyBuilder`
    
    .. versionadded:: NX11.0.0
    """
    ChildComponentsForComponents: bool = ...
    """
    Returns or sets  the flag indicating whether to export child components for components 
    
    <hr>
    
    Getter Method
    
    Signature ``ChildComponentsForComponents`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChildComponentsForComponents`` 
    
    :param childComponentsForComponents: 
    :type childComponentsForComponents: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ChildComponentsForDefinitions: bool = ...
    """
    Returns or sets  the flag indicating whether to export child components for definitions 
    
    <hr>
    
    Getter Method
    
    Signature ``ChildComponentsForDefinitions`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChildComponentsForDefinitions`` 
    
    :param childComponentsForDefinitions: 
    :type childComponentsForDefinitions: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Contents: bool = ...
    """
    Returns or sets  the flag indicating whether to export contents for components 
    
    <hr>
    
    Getter Method
    
    Signature ``Contents`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Contents`` 
    
    :param contents: 
    :type contents: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    DefinitionReferenceProperties: bool = ...
    """
    Returns or sets  the flag indicating whether to export definition reference properties for components 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionReferenceProperties`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefinitionReferenceProperties`` 
    
    :param definitionReferenceProperties: 
    :type definitionReferenceProperties: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Definitions: bool = ...
    """
    Returns or sets  the flag indicating whether to export definitions for components 
    
    <hr>
    
    Getter Method
    
    Signature ``Definitions`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Definitions`` 
    
    :param definitions: 
    :type definitions: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    OutputFileName: str = ...
    """
    Returns or sets  the selected output file 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputFileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputFileName`` 
    
    :param outputFileName: 
    :type outputFileName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Selection: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected objects which may be of :py:class:`NXOpen.Layout2d.Component` or :py:class:`NXOpen.Sketch` type 
    
    <hr>
    
    Getter Method
    
    Signature ``Selection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SoftwareProperties: bool = ...
    """
    Returns or sets  the flag indicating whether to export software properties for components 
    
    <hr>
    
    Getter Method
    
    Signature ``SoftwareProperties`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SoftwareProperties`` 
    
    :param softwareProperties: 
    :type softwareProperties: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: ExportComponentHierarchyBuilder = ...  # unknown typename


class SelectComponentList(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a list of objects on a selection list.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def Add(self, object: Component) -> bool:
        """
        Adds an object to the list
        
        Signature ``Add(object)`` 
        
        :param object:  object to add  
        :type object: :py:class:`NXOpen.Layout2d.Component` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, objects: 'list[Component]') -> bool:
        """
        Adds a set of objects to the list
        
        Signature ``Add(objects)`` 
        
        :param objects:  objects to add  
        :type objects: list of :py:class:`NXOpen.Layout2d.Component` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Adds the objects from a SelectionMethod to the list
        
        Signature ``Add(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
        Adds the object with the objects view and objects point
        
        Signature ``Add(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``Add(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Layout2d.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Layout2d.Component` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: Component, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> bool:
        """
        The object being selected with CAE set object information.
        
        Signature ``Add(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObjectList.Add`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Remove(self, object: Component) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Layout2d.Component` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, object: Component, view: NXOpen.View) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object, view)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Layout2d.Component` 
        :param view:  with this view 
        :type view: :py:class:`NXOpen.View` 
        :returns:  True if succesully removed from list;
        False if the object / view was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Layout2d.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Layout2d.Component` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Removes the objects from a SelectionMethod from the list
        
        Signature ``Remove(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully removed all objects from the list;
        False if there was at least one object that was not a
        member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveArray(self, objects: 'list[Component]') -> bool:
        """
        Remove specified objects from list.  
        
        Signature ``RemoveArray(objects)`` 
        
        :param objects:  Objects to remove  
        :type objects: list of :py:class:`NXOpen.Layout2d.Component` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Clear(self) -> None:
        """
        Removes all items from the list.  
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Contains(self, object: Component) -> bool:
        """
        Returns whether the specified object is already in the list or not.  
        
        Signature ``Contains(object)`` 
        
        :param object:  object to check  
        :type object: :py:class:`NXOpen.Layout2d.Component` 
        :returns:  true if object is in the list, false otherwise  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetArray(self, objects: 'list[Component]') -> None:
        """
        Overloaded method SetArray
        
        * ``SetArray(objects)`` 
        * ``SetArray(vars)`` 
        
        <hr>
        
        Sets the list of objects in the selection list. This will clear any existing
        items in the list.
        
        Signature ``SetArray(objects)`` 
        
        :param objects:  items to put in the list 
        :type objects: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetArray(self) -> 'list[Component]':
        """
        Overloaded method GetArray
        
        * ``GetArray()`` 
        * ``GetArray()`` 
        
        <hr>
        
        Returns the list of objects in the selection list.
        
        Signature ``GetArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetSelectObjectArray(self) -> 'list[NXOpen.SelectObject]':
        """
        Returns the list of SelectObjects in the selection list.  
        
        Signature ``GetSelectObjectArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.SelectObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    DuplicatesAllowed: bool = ...
    """
    Returns  whether duplicate objects are allowed in the selection list.  
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicatesAllowed`` 
    
    :returns:  Whether duplicate objects are allowed  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Size: int = ...
    """
    Returns  the number of objects in the list.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns:  number of objects in the list  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectComponentList = ...  # unknown typename


class ReplaceComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Replace 2D Component functionality which will replaces
    *   the selected 2D Component contents from another 2D Component definition.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateReplaceComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Components: SelectComponentList = ...
    """
    Returns  the select 2D Components to replace the definitions 
    
    <hr>
    
    Getter Method
    
    Signature ``Components`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.SelectComponentList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Location: Layout2dDefinitionLocation = ...
    """
    Returns or sets  the location type of the 2D Component definition to replace 
    *   indicating local, native or team center
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param locationType: 
    :type locationType: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Path: str = ...
    """
    Returns or sets  the path of the 2D Component definition to replace 
    
    <hr>
    
    Getter Method
    
    Signature ``Path`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Path`` 
    
    :param path: 
    :type path: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    ReplaceAll: bool = ...
    """
    Returns or sets  the flag indicating whether to replace all instances of selected components 
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceAll`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceAll`` 
    
    :param replaceAll: 
    :type replaceAll: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: ReplaceComponentBuilder = ...  # unknown typename


class ComponentCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Layout2d.Component`s.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Component:
        """
        Finds the :py:class:`NXOpen.Layout2d.Component` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of
        the software. However newer versions of the software should find the same object when
        FindObject is passed older versions of its journal identifier. In general, this method
        should not be used in handwritten code and exists to support record and playback of journals.
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the 2D Component to be found  
        :type journalIdentifier: str 
        :returns:  2D Component with this identifier  
        :rtype: :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDefineComponentBuilder(self, component: Component) -> DefineComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.DefineComponentBuilder` that can create a fully defined 2D 
        Component with specified content, anchor point, name and reuse library destination folder.  
        
        Signature ``CreateDefineComponentBuilder(component)`` 
        
        :param component:  the component to be edited,                                                                     None in case of new component view. 
        :type component: :py:class:`NXOpen.Layout2d.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.DefineComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateInsertComponentBuilder(self) -> InsertComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.InsertComponentBuilder` that inserts a 2D Component instance in the active
        *  sketch.  
        
        Signature ``CreateInsertComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.InsertComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateReplaceComponentBuilder(self) -> ReplaceComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.ReplaceComponentBuilder` that can replace the selected 2D Component
        *   instance with another 2D Component definition
        
        Signature ``CreateReplaceComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.ReplaceComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateSmashComponentBuilder(self) -> SmashComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.SmashComponentBuilder` that can smash the selected 
        *  2D Component instance
        
        Signature ``CreateSmashComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.SmashComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateMakeComponentUniqueBuilder(self) -> MakeComponentUniqueBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.MakeComponentUniqueBuilder` that can create definition
        *  for the selected 2D Component instance
        
        Signature ``CreateMakeComponentUniqueBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.MakeComponentUniqueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateDefineComponentAnchorPointBuilder(self) -> DefineComponentAnchorPointBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.DefineComponentAnchorPointBuilder` that can define the Anchor Point location of a
        *  2D Component
        
        Signature ``CreateDefineComponentAnchorPointBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.DefineComponentAnchorPointBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreatePublishComponentBuilder(self) -> PublishComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.PublishComponentBuilder` that can export local definitions into external storage locations
        
        Signature ``CreatePublishComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.PublishComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateNewComponentBuilder(self) -> NewComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.NewComponentBuilder` that creates an empty 2D Component instance and stores its
        *  definition in local 2D Component folder
        
        Signature ``CreateNewComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.NewComponentBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def DeleteComponents(self, components: 'list[Component]') -> None:
        """
        Deletes a list of 2D Components
        
        Signature ``DeleteComponents(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def IsComponentMember(self, disObject: NXOpen.DisplayableObject) -> bool:
        """
        Verify if the object belong to this component  
        
        Signature ``IsComponentMember(disObject)`` 
        
        :param disObject: 
        :type disObject: :py:class:`NXOpen.DisplayableObject` 
        :returns:  true if the object is component member  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateAssemblyFromLayout2dBuilder(self) -> AssemblyFromLayout2dBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.AssemblyFromLayout2dBuilder` that can create assembly from  
        *  the selected layout
        
        Signature ``CreateAssemblyFromLayout2dBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.AssemblyFromLayout2dBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateReparentComponentBuilder(self) -> ReparentComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.ReplaceComponentBuilder` that can reparent the selected 2D Component
        *  instance with another 2D Component or sketch  
        
        Signature ``CreateReparentComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.ReparentComponentBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def UpdateComponents(self, components: 'list[Component]') -> None:
        """
        Updates 2D Components without propagating the changes to the hierarchy in given layout 
        
        Signature ``UpdateComponents(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def UpdateComponentHierarchy(self, components: 'list[Component]') -> None:
        """
        Updates 2D Components and propagates the changes to the hierarchy in given layout 
        
        Signature ``UpdateComponentHierarchy(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateComponentFrom3dBuilder(self, myView: NXOpen.View) -> CreateComponentFrom3DBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.CreateComponentFrom3DBuilder` that can create assembly from
        *  the selected layout
        
        Signature ``CreateComponentFrom3dBuilder(myView)`` 
        
        :param myView: 
        :type myView: :py:class:`NXOpen.View` 
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateExportComponentHierarchyBuilder(self) -> ExportComponentHierarchyBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.ExportComponentHierarchyBuilder`  
        
        Signature ``CreateExportComponentHierarchyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.ExportComponentHierarchyBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    OrderManagers: NXOpen.Drawings.OrderManager = ...
    """
    Returns the OrderManager for part 
    
    Signature ``OrderManagers`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.OrderManager`
    """


class LayoutDrawingSheetCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Layout2d.LayoutDrawingSheet`s.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> LayoutDrawingSheet:
        """
        Finds the :py:class:`NXOpen.Layout2d.LayoutDrawingSheet` with the given identifier 
        as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in 
        different versions of  the software. However newer versions of the software should find the same 
        object when  FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the Layout drawing sheet you want  
        :type journalIdentifier: str 
        :returns:  Layout drawing sheet with this identifier  
        :rtype: :py:class:`NXOpen.Layout2d.LayoutDrawingSheet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateLayoutDrawingSheetBuilder(self, layoutDrawingSheet: LayoutDrawingSheet) -> LayoutDrawingSheetBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.LayoutDrawingSheetBuilder`  
        
        Signature ``CreateLayoutDrawingSheetBuilder(layoutDrawingSheet)`` 
        
        :param layoutDrawingSheet:  reserved for future use, set to 0  
        :type layoutDrawingSheet: :py:class:`NXOpen.Layout2d.LayoutDrawingSheet` 
        :returns:  the layout drawing sheet builder  
        :rtype: :py:class:`NXOpen.Layout2d.LayoutDrawingSheetBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def InsertSheet(self, name: str, units: NXOpen.Drawings.DrawingSheetUnit, numerator: float, denominator: float, projectionAngle: NXOpen.Drawings.DrawingSheetProjectionAngleType) -> LayoutDrawingSheet:
        """
        Inserts a layout drawing sheet into a part.  
        
        Signature ``InsertSheet(name, units, numerator, denominator, projectionAngle)`` 
        
        :param name:  Layout drawing sheet name  
        :type name: str 
        :param units:  Unit of sheet size  
        :type units: :py:class:`NXOpen.Drawings.DrawingSheetUnit` 
        :param numerator:  Numerator of the scale of layout  
        :type numerator: float 
        :param denominator:  Denominator of the scale of layout  
        :type denominator: float 
        :param projectionAngle:  Projection angle  
        :type projectionAngle: :py:class:`NXOpen.Drawings.DrawingSheetProjectionAngleType` 
        :returns:  the inserted layout drawing sheet  
        :rtype: :py:class:`NXOpen.Layout2d.LayoutDrawingSheet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateConvertSheetToLayoutBuilder(self) -> ConvertSheetToLayoutBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.ConvertSheetToLayoutBuilder`  
        
        Signature ``CreateConvertSheetToLayoutBuilder()`` 
        
        :returns:  the convert sheet to layout builder  
        :rtype: :py:class:`NXOpen.Layout2d.ConvertSheetToLayoutBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def CreateConvertLayoutToSheetBuilder(self) -> ConvertLayoutToSheetBuilder:
        """
        Creates a :py:class:`NXOpen.Layout2d.ConvertLayoutToSheetBuilder`  
        
        Signature ``CreateConvertLayoutToSheetBuilder()`` 
        
        :returns:  the convert layout to sheet builder  
        :rtype: :py:class:`NXOpen.Layout2d.ConvertLayoutToSheetBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    


class InsertComponentBuilder(NXOpen.Builder):
    """
    Represents a Builder for Insert Component functionality which will insert a 2D
    *  Component instance in the active sketch    
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateInsertComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def SetPath(self, path: str) -> None:
        """
        Sets the path of the reuse library for the 2D Component 
        
        Signature ``SetPath(path)`` 
        
        :param path:  the path of the 2D Component  
        :type path: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetLocation(self, locationType: Layout2dDefinitionLocation) -> None:
        """
        Sets the location type of the 2D Component indicating local, native or team center
        
        Signature ``SetLocation(locationType)`` 
        
        :param locationType: 
        :type locationType: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    Angle: float = ...
    """
    Returns or sets  the component rotation angle, measured counterclockwise, around the anchor point, from the sketch +X direction to component's X axis 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Angle`` 
    
    :param angle: 
    :type angle: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Settings: ComponentSettingsBlockBuilder = ...
    """
    Returns  the Component settings block builder which holds the component settings builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Settings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentSettingsBlockBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Sketch: NXOpen.Sketch = ...
    """
    Returns or sets  the sketch to insert the 2D Component 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Sketch` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Sketch` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    SpecifyPoint: NXOpen.Point3d = ...
    """
    Returns or sets  the point specified to put the 2D Component instance
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifyPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecifyPoint`` 
    
    :param specifyPoint: 
    :type specifyPoint: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: InsertComponentBuilder = ...  # unknown typename


class ConvertSheetToLayoutBuilder(LayoutDrawingSheetBuilder):
    """
    Represents a Builder for converting a drawing sheet to Layout   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.LayoutDrawingSheetCollection.CreateConvertSheetToLayoutBuilder`
    
    .. versionadded:: NX12.0.0
    """
    SelectSheetView: NXOpen.SelectView = ...
    """
    Returns  the select drawing sheet to convert
    
    <hr>
    
    Getter Method
    
    Signature ``SelectSheetView`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectView` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ConvertSheetToLayoutBuilder = ...  # unknown typename


class ComponentDefinitionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Layout2d.ComponentDefinition` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, sid: str) -> ComponentDefinition:
        """
        Finds the :py:class:`NXOpen.Layout2d.ComponentDefinition` with the given sid.  
        
        An exception will be thrown if no object can be found with the given sid. 
        This method can only be used to find Local definitions  
        
        Signature ``FindObject(sid)`` 
        
        :param sid:  The sid of the definition to find  
        :type sid: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.ComponentDefinition` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Rename(self, location: Layout2dDefinitionLocation, definitionPath: str, newName: str) -> None:
        """
        Renames definition
        
        Signature ``Rename(location, definitionPath, newName)`` 
        
        :param location:  Location of the definition to rename  
        :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        :param definitionPath:  Path of the definition to rename  
        :type definitionPath: str 
        :param newName:  New definition name  
        :type newName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Delete(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
        Deletes definition
        
        Signature ``Delete(location, definitionPath)`` 
        
        :param location:  Location of the definition to delete  
        :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        :param definitionPath:  Path of the definition to delete  
        :type definitionPath: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def UpdateImage(self, location: Layout2dDefinitionLocation, definitionPath: str, imagePath: str) -> None:
        """
        Updates definition preview 
        
        Signature ``UpdateImage(location, definitionPath, imagePath)`` 
        
        :param location:  Location of the definition to update image  
        :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        :param definitionPath:  Path of the definition to update image  
        :type definitionPath: str 
        :param imagePath:  Path of the image file used to update definition preview  
        :type imagePath: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetAutomaticPreview(self, location: Layout2dDefinitionLocation, definitionPath: str, isAutomatic: bool) -> None:
        """
        Sets the automatic preview mode of definition with the given path 
        
        Signature ``SetAutomaticPreview(location, definitionPath, isAutomatic)`` 
        
        :param location:  Location of the definition to set the preview mode  
        :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        :param definitionPath:  Path of the definition to set the preview mode  
        :type definitionPath: str 
        :param isAutomatic: 
        :type isAutomatic: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Update(self, location: Layout2dDefinitionLocation, definitionPath: str) -> None:
        """
        Updates definition with the given path 
        
        Signature ``Update(location, definitionPath)`` 
        
        :param location:  Location of the definition to update  
        :type location: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        :param definitionPath:  Path of the definition to update  
        :type definitionPath: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def RefreshAllReferences(self) -> None:
        """
        Refreshes all definition references in part to obtain the actual out-of-date status of components 
        
        Signature ``RefreshAllReferences()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    


class CreateComponentFrom3DBuilderCreateMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateComponentFrom3DBuilderCreateMethod():
    """
    the method to use 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Section", "use section"
       "Plane", "use plane"
    """
    Section = 0  # CreateComponentFrom3DBuilderCreateMethodMemberType
    Plane = 1  # CreateComponentFrom3DBuilderCreateMethodMemberType
    
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
    


class CreateComponentFrom3DBuilder(NXOpen.Display.DynamicSectionBuilder):
    """
    Represents a Builder that creates :py:class:`NXOpen.Layout2d.Component` from Assembly  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateComponentFrom3dBuilder`
    
    Default values.
    
    ========================  =========
    Property                  Value
    ========================  =========
    BoxExtentDelayUpdate      false 
    ------------------------  ---------
    CapColorOption            Any 
    ------------------------  ---------
    ClipType                  Section 
    ------------------------  ---------
    CurveColorOption          Any 
    ------------------------  ---------
    LockPlanes                true 
    ------------------------  ---------
    ShowCap                   true 
    ------------------------  ---------
    ShowClip                  true 
    ------------------------  ---------
    ShowCurves (deprecated)   false 
    ------------------------  ---------
    ShowGrid                  false 
    ------------------------  ---------
    ShowInterference          false 
    ------------------------  ---------
    ShowViewer                false 
    ------------------------  ---------
    Type                      OnePlane 
    ========================  =========
    
    .. versionadded:: NX11.0.0
    """
    
    class CreateMethod():
        """
        the method to use 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Section", "use section"
           "Plane", "use plane"
        """
        Section = 0  # CreateComponentFrom3DBuilderCreateMethodMemberType
        Plane = 1  # CreateComponentFrom3DBuilderCreateMethodMemberType
        
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
        
    
    
    def SetSourcePart(self, part: NXOpen.Part) -> None:
        """
        Sets the source part to create 2D component from.  
        
        The part may be the current work part or other part loaded in session. 
        
        Signature ``SetSourcePart(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetSourcePart(self) -> NXOpen.Part:
        """
        Returns the current source part  
        
        Signature ``GetSourcePart()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetProjectionPlane(self, origin: NXOpen.Point3d, yAxis: NXOpen.Vector3d, zAxis: NXOpen.Vector3d) -> None:
        """
        Sets the projection plane specified by origin, y and z vectors, where z is the plane normal and
        the x vector is computed.  
        
        Signature ``SetProjectionPlane(origin, yAxis, zAxis)`` 
        
        :param origin: 
        :type origin: :py:class:`NXOpen.Point3d` 
        :param yAxis: 
        :type yAxis: :py:class:`NXOpen.Vector3d` 
        :param zAxis: 
        :type zAxis: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetProjectionPlane(self) -> tuple:
        """
        Gets the projection plane origin and orientation matrix 
        
        Signature ``GetProjectionPlane()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (origin, orientation). origin is a :py:class:`NXOpen.Point3d`. orientation is a :py:class:`NXOpen.Matrix3x3`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    ComponentName: str = ...
    """
    Returns or sets  the component name 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentName`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Method: CreateComponentFrom3DBuilderCreateMethod = ...
    """
    Returns or sets  the method to utilize in create Component from 3D
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DBuilderCreateMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DBuilderCreateMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    SelectedObjects: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects of Solid body or Component type 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Settings: CreateComponentFrom3DSettingsBuilder = ...
    """
    Returns or sets  the settings of create component from 3D 
    
    <hr>
    
    Getter Method
    
    Signature ``Settings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Settings`` 
    
    :param settings: 
    :type settings: :py:class:`NXOpen.Layout2d.CreateComponentFrom3DSettingsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: CreateComponentFrom3DBuilder = ...  # unknown typename


class ComponentSettingsBlockBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the Component Settings Button (Layout2d.  
    
    ComponentSettingsBlockBuilder)
    
    .. versionadded:: NX10.0.0
    """
    
    def InheritSettingsFromSelectedObject(self, selectedObject: NXOpen.NXObject) -> None:
        """
        Inherit Settings From Selected Objects 
        
        Signature ``InheritSettingsFromSelectedObject(selectedObject)`` 
        
        :param selectedObject:  The selected 2C Component object.                                                                         None is not allowed.  
        :type selectedObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
        Inherit Settings From Customer Default 
        
        Signature ``InheritSettingsFromCustomerDefault()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def InheritSettingsFromPreferences(self) -> None:
        """
        Inherit Settings From Preference 
        
        Signature ``InheritSettingsFromPreferences()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    ComponentSettings: ComponentSettingsBuilder = ...
    """
    Returns  the Component settings builder which stores the component settings 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.ComponentSettingsBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: ComponentSettingsBlockBuilder = ...  # unknown typename


class AssemblyFromLayout2dBuilder(NXOpen.Builder):
    """
    Represents a Builder for create assembly from Layout functionality which will create a
    *  new assembly from the selected Layout   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Layout2d.ComponentCollection.CreateAssemblyFromLayout2dBuilder`
    
    .. versionadded:: NX10.0.0
    """
    AssemblyPart: NXOpen.Part = ...
    """
    Returns or sets  the destination part for the Layout assembly 
    
    <hr>
    
    Getter Method
    
    Signature ``AssemblyPart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssemblyPart`` 
    
    :param assemblyPart: 
    :type assemblyPart: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Layout2dObject: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the select Layout object to create assembly 
    
    <hr>
    
    Getter Method
    
    Signature ``Layout2dObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Settings: AssemblyCreationSettingsBuilder = ...
    """
    Returns  the settings of the assembly creation 
    
    <hr>
    
    Getter Method
    
    Signature ``Settings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Layout2d.AssemblyCreationSettingsBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: AssemblyFromLayout2dBuilder = ...  # unknown typename


class ComponentDefinition(NXOpen.NXObject):
    """
    Represents a component definition.  
    
    The definition contains sketch curves, sketch dimensions
    and drafting annotations representing a two dimensional reusable sketch component.
    
    .. versionadded:: NX10.0.0
    """
    
    def Rename(self, definitionPath: str, newName: str) -> None:
        """
        Renames definition
        
        Signature ``Rename(definitionPath, newName)`` 
        
        :param definitionPath:  Path of the definition to rename  
        :type definitionPath: str 
        :param newName:  New definition name  
        :type newName: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Delete(self, definitionPath: str) -> None:
        """
        Deletes definition
        
        Signature ``Delete(definitionPath)`` 
        
        :param definitionPath:  Path of the definition to delete  
        :type definitionPath: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def UpdateImage(self, definitionPath: str, imagePath: str) -> None:
        """
        Updates definition preview 
        
        Signature ``UpdateImage(definitionPath, imagePath)`` 
        
        :param definitionPath:  Path of the definition to rename  
        :type definitionPath: str 
        :param imagePath:  Path of the image file used to update definition preview  
        :type imagePath: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> 'list[NXOpen.DisplayableObject]':
        """
        Returns an array of specified members in this component definition
        
        Signature ``GetMembers(memberType)`` 
        
        :param memberType: 
        :type memberType: :py:class:`NXOpen.Layout2d.Layout2dComponentMemberType` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    Null: ComponentDefinition = ...  # unknown typename


class Component(NXOpen.DisplayableObject):
    """
    Represents the Component object.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Layout2d.DefineComponentBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def Activate(self) -> None:
        """
        Activates the component.  
        
        Signature ``Activate()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Deactivate(self) -> None:
        """
        Deactivates the component.  
        
        Signature ``Deactivate()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Update(self) -> None:
        """
        Updates the component and all of its sub components.  
        
        Signature ``Update()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def ExitActivate(self) -> None:
        """
        Exits the component active status without committing the changes.  
        
        Signature ``ExitActivate()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetMembers(self, memberType: Layout2dComponentMemberType) -> 'list[NXOpen.DisplayableObject]':
        """
        Returns an array of specified members in this component 
        
        Signature ``GetMembers(memberType)`` 
        
        :param memberType: 
        :type memberType: :py:class:`NXOpen.Layout2d.Layout2dComponentMemberType` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def Transform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
        Transforms the component given a rotation matrix and a translation vector
        
        Signature ``Transform(rotation, translation)`` 
        
        :param rotation: 
        :type rotation: :py:class:`NXOpen.Matrix3x3` 
        :param translation: 
        :type translation: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def SetTransform(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Vector3d) -> None:
        """
        Sets the absolute transform on a component, given a rotation matrix and a translation vector
        
        Signature ``SetTransform(rotation, translation)`` 
        
        :param rotation: 
        :type rotation: :py:class:`NXOpen.Matrix3x3` 
        :param translation: 
        :type translation: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetTransform(self) -> tuple:
        """
        Gets the absolute transform of a component, as a rotation matrix and a translation vector
        
        Signature ``GetTransform()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (rotation, translation). rotation is a :py:class:`NXOpen.Matrix3x3`. translation is a :py:class:`NXOpen.Vector3d`. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def AddExistingCurves(self, curves: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Add an array of specified curves from top level sketch to this component 
        
        Signature ``AddExistingCurves(curves)`` 
        
        :param curves: 
        :type curves: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetDefinition(self) -> ComponentDefinition:
        """
        Gets the component definition of a component  
        
        Signature ``GetDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.ComponentDefinition` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetAnchorPoint(self) -> tuple:
        """
        Gets the anchor point of a component if it exist  
        
        Signature ``GetAnchorPoint()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isAnchorPointExist, anchorPoint). isAnchorPointExist is a bool. anchorPoint is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetDefinitionName(self) -> str:
        """
        Gets the component definition name of a component  
        
        Signature ``GetDefinitionName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetDefinitionPath(self) -> str:
        """
        Gets the path of the component definition  
        
        Signature ``GetDefinitionPath()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def GetDefinitionLocation(self) -> Layout2dDefinitionLocation:
        """
        Gets the location of the component definition  
        
        Signature ``GetDefinitionLocation()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Layout2d.Layout2dDefinitionLocation` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    
    def ActivateInIsolation(self) -> NXOpen.Sketch:
        """
        Activates the component while in edit in isolation task environment and
        returns component internal sketch  
        
        Signature ``ActivateInIsolation()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Sketch` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_layout ("NX Layout")
        """
        ...
    
    IsActive: bool = ...
    """
    Returns  the active state of 2D Component.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsActive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    LockUpdateStatus: bool = ...
    """
    Returns or sets  the lock update status of 2D Component.  
    
    <hr>
    
    Getter Method
    
    Signature ``LockUpdateStatus`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: drafting ("DRAFTING")
    
    <hr>
    
    Setter Method
    
    Signature ``LockUpdateStatus`` 
    
    :param lock: 
    :type lock: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_layout ("NX Layout")
    """
    Null: Component = ...  # unknown typename


class Layout2dComponentMemberTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Layout2dComponentMemberType():
    """
    Component member type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "SketchGeometryNonReference", " - "
       "SketchGeometryReference", " - "
       "SketchGeometry", " - "
       "SketchDimension", " - "
       "SketchConstraint", " - "
       "Sketch", " - "
       "Component", " - "
       "DraftingDimension", " - "
       "Dimension", " - "
       "DraftingAnnotationNonDimension", " - "
       "DraftingAnnotation", " - "
       "Annotation", " - "
       "MiscOthers", " - "
       "Misc", " - "
       "All", " - "
    """
    NotSet = 0  # Layout2dComponentMemberTypeMemberType
    SketchGeometryNonReference = 1  # Layout2dComponentMemberTypeMemberType
    SketchGeometryReference = 2  # Layout2dComponentMemberTypeMemberType
    SketchGeometry = 3  # Layout2dComponentMemberTypeMemberType
    SketchDimension = 4  # Layout2dComponentMemberTypeMemberType
    SketchConstraint = 8  # Layout2dComponentMemberTypeMemberType
    Sketch = 16  # Layout2dComponentMemberTypeMemberType
    Component = 32  # Layout2dComponentMemberTypeMemberType
    DraftingDimension = 64  # Layout2dComponentMemberTypeMemberType
    Dimension = 68  # Layout2dComponentMemberTypeMemberType
    DraftingAnnotationNonDimension = 128  # Layout2dComponentMemberTypeMemberType
    DraftingAnnotation = 192  # Layout2dComponentMemberTypeMemberType
    Annotation = 196  # Layout2dComponentMemberTypeMemberType
    MiscOthers = 256  # Layout2dComponentMemberTypeMemberType
    Misc = 448  # Layout2dComponentMemberTypeMemberType
    All = 511  # Layout2dComponentMemberTypeMemberType
    
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
    


class SelectComponent(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a single object selection.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def SetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def SetValue(self, selection: Component) -> None:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: Component) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: Component, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
        The object being selected with the object's view and object's point
        
        Signature ``SetValue(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: Component, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Component, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``SetValue(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Layout2d.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1:  first selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Layout2d.Component` 
        :param view2:  second selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: Component, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> None:
        """
        The object being selected with CAE set object information.
        
        Signature ``SetValue(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.SetValue`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def GetValue(self) -> Component:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :returns:  selected object  
        :rtype: :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self, selection: Component) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Layout2d.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the object's view and point.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, view, point). selection is a :py:class:`NXOpen.Layout2d.Component`.   selected object view is a :py:class:`NXOpen.View`.   selected object viewpoint is a :py:class:`NXOpen.Point3d`.   selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the objects view and point and snap information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (snapType, selection1, view1, point1, selection2, view2, point2). snapType is a :py:class:`NXOpen.InferSnapTypeSnapType`.    snap point typeselection1 is a :py:class:`NXOpen.Layout2d.Component`.   first selected object view1 is a :py:class:`NXOpen.View`.   first selected object viewpoint1 is a :py:class:`NXOpen.Point3d`.   first selected object pointselection2 is a :py:class:`NXOpen.Layout2d.Component`.   second selected object view2 is a :py:class:`NXOpen.View`.   second selected object viewpoint2 is a :py:class:`NXOpen.Point3d`.   second selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with CAE set object information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, caeSubType, caeSubId). selection is a :py:class:`NXOpen.Layout2d.Component`.   selected object caeSubType is a :py:class:`NXOpen.CaeObjectTypeCaeSubType`.   CAE set object sub typecaeSubId is a int.   CAE set object sub id
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.GetValue`.
        
        License requirements: None.
        """
        ...
    
    
    def Validate(self) -> bool:
        """
        Validate whether the inputs to the component are sufficient for 
        commit to be called.  
        
        If the component is not in a state to commit
        then an exception is thrown.  For example, if the component requires
        you to set some property, this method will throw an exception if
        you haven't set it.  This method throws a not-yet-implemented
        NXException for some components.
        
        Signature ``Validate()`` 
        
        :returns:  Was self validation successful  
        :rtype: bool 
        
        .. versionadded:: NX3.0.1
        
        License requirements: None.
        """
        ...
    
    Value: Component = ...
    """
    Returns or sets  the object being selected
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns:  selected object  
    :rtype: :py:class:`NXOpen.Layout2d.Component` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param selection:  selected object  
    :type selection: :py:class:`NXOpen.Layout2d.Component` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectComponent = ...  # unknown typename


