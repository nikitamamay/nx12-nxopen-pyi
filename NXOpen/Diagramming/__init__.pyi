# module 'NXOpen.Diagramming'
#
# Automatically generated 2025-06-09T14:38:45.449197
#
"""Default documentation for NXOpen.Diagramming."""

import typing

import NXOpen
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class BaseObjectBuilder(NXOpen.Builder):
    """
    Represents a BaseObjectBuilder.  
    
    This is an abstract class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    Null: BaseObjectBuilder = ...  # unknown typename


class SheetElementBuilderResizeOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetElementBuilderResizeOptionType():
    """
    Represents the resize option 
    for a :py:class:`NXOpen.Diagramming.SheetElementBuilder`.
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AnyDirection", " - "
       "OnAnchor", " - "
       "SameRatio", " - "
       "SameRationOnCorner", " - "
       "SameRatioOnEdge", " - "
    """
    AnyDirection = 0  # SheetElementBuilderResizeOptionTypeMemberType
    OnAnchor = 1  # SheetElementBuilderResizeOptionTypeMemberType
    SameRatio = 2  # SheetElementBuilderResizeOptionTypeMemberType
    SameRationOnCorner = 3  # SheetElementBuilderResizeOptionTypeMemberType
    SameRatioOnEdge = 4  # SheetElementBuilderResizeOptionTypeMemberType
    
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
    


class SheetElementBuilder(BaseObjectBuilder):
    """
    Represents a SheetElementBuilder.  
    
    This is an abstract class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    class ResizeOptionType():
        """
        Represents the resize option 
        for a :py:class:`NXOpen.Diagramming.SheetElementBuilder`.
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AnyDirection", " - "
           "OnAnchor", " - "
           "SameRatio", " - "
           "SameRationOnCorner", " - "
           "SameRatioOnEdge", " - "
        """
        AnyDirection = 0  # SheetElementBuilderResizeOptionTypeMemberType
        OnAnchor = 1  # SheetElementBuilderResizeOptionTypeMemberType
        SameRatio = 2  # SheetElementBuilderResizeOptionTypeMemberType
        SameRationOnCorner = 3  # SheetElementBuilderResizeOptionTypeMemberType
        SameRatioOnEdge = 4  # SheetElementBuilderResizeOptionTypeMemberType
        
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
        
    
    
    def GetMinNodeSize(self) -> 'list[float]':
        """
        Gets the minimum node size values 
        
        Signature ``GetMinNodeSize()`` 
        
        :returns:  Minimum node size values as output 
        :rtype: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMinNodeSize(self, sizeValues: 'list[float]') -> None:
        """
        Sets the minimum node size values 
        
        Signature ``SetMinNodeSize(sizeValues)`` 
        
        :param sizeValues:  Minimum node size values as input 
        :type sizeValues: list of float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllowedTransformations(self) -> tuple:
        """
        Get the allowed transformations of the sheet element.  
        
        Signature ``GetAllowedTransformations()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isAllowedTranslation, isAllowedRotation, isAllowedScale, isAllowedShear). isAllowedTranslation is a bool. isAllowedRotation is a bool. isAllowedScale is a bool. isAllowedShear is a bool. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
        Set the owning sheet when the sheet element is created.  
        
        It is not allowed to change the owning sheet when editing the sheet element. 
        
        Signature ``SetOwningSheet(owningSheet)`` 
        
        :param owningSheet: 
        :type owningSheet: :py:class:`NXOpen.Diagramming.Sheet` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Height: float = ...
    """
    Returns or sets  the height.  
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    HeightPolicy: DiagrammingSizingpolicy = ...
    """
    Returns or sets  the height policy.  
    
    <hr>
    
    Getter Method
    
    Signature ``HeightPolicy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingSizingpolicy` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeightPolicy`` 
    
    :param heightPolicy: 
    :type heightPolicy: :py:class:`NXOpen.Diagramming.DiagrammingSizingpolicy` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Internal: bool = ...
    """
    Returns  the flag that indicates if the sheet element is internal.  
    
    If false it is not part of the user's data model; for example, an Annotation is not part of the user's model of Nodes and Connections. 
    
    <hr>
    
    Getter Method
    
    Signature ``Internal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Label: Annotation = ...
    """
    Returns  the label of this sheet element.  
    
    <hr>
    
    Getter Method
    
    Signature ``Label`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Annotation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LabelName: str = ...
    """
    Returns or sets  the label name of this sheet element.  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelName`` 
    
    :param labelname: 
    :type labelname: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Location: LocationBuilder = ...
    """
    Returns  the location of the sheet element relative to another sheet element.  
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LocationBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LocationStyle: DiagrammingLocationstyle = ...
    """
    Returns or sets  the location style.  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingLocationstyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LocationStyle`` 
    
    :param locationStyle: 
    :type locationStyle: :py:class:`NXOpen.Diagramming.DiagrammingLocationstyle` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MirrorX: bool = ...
    """
    Returns or sets  the sheet element to Mirror along the X axis.  
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorX`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorX`` 
    
    :param mirrorX: 
    :type mirrorX: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MirrorY: bool = ...
    """
    Returns or sets  the sheet element to Mirror along the Y axis.  
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorY`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorY`` 
    
    :param mirrorY: 
    :type mirrorY: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Owner: SheetElement = ...
    """
    Returns or sets  the owning sheet element.  
    
    <hr>
    
    Getter Method
    
    Signature ``Owner`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetElement` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Owner`` 
    
    :param owner: 
    :type owner: :py:class:`NXOpen.Diagramming.SheetElement` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OwningSheet: Sheet = ...
    """
    Returns  the owning sheet.  
    
    <hr>
    
    Getter Method
    
    Signature ``OwningSheet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Sheet` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ResizeOption: SheetElementBuilderResizeOptionType = ...
    """
    Returns or sets  the resize option of the sheet element 
    
    <hr>
    
    Getter Method
    
    Signature ``ResizeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetElementBuilderResizeOptionType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResizeOption`` 
    
    :param resizeOption: 
    :type resizeOption: :py:class:`NXOpen.Diagramming.SheetElementBuilderResizeOptionType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Rotation: float = ...
    """
    Returns or sets  the rotation angle that is counter clockwise and relative to the owner.  
    
    <hr>
    
    Getter Method
    
    Signature ``Rotation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotation`` 
    
    :param angle: 
    :type angle: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SourceElement: SheetElement = ...
    """
    Returns  the source element that records which sheet element it is a copy of.  
    
    <hr>
    
    Getter Method
    
    Signature ``SourceElement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetElement` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    UpToDate: bool = ...
    """
    Returns  the flag that indicates if the sheet element is up to date.  
    
    <hr>
    
    Getter Method
    
    Signature ``UpToDate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Visible: bool = ...
    """
    Returns  the flag that indicates if the sheet element is visible.  
    
    If true it is visible. 
    
    <hr>
    
    Getter Method
    
    Signature ``Visible`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Width: float = ...
    """
    Returns or sets  the width.  
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    WidthPolicy: DiagrammingSizingpolicy = ...
    """
    Returns or sets  the width policy.  
    
    <hr>
    
    Getter Method
    
    Signature ``WidthPolicy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingSizingpolicy` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthPolicy`` 
    
    :param widthPolicy: 
    :type widthPolicy: :py:class:`NXOpen.Diagramming.DiagrammingSizingpolicy` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    X: float = ...
    """
    Returns or sets  the absolute x coordinate.  
    
    <hr>
    
    Getter Method
    
    Signature ``X`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``X`` 
    
    :param x: 
    :type x: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Y: float = ...
    """
    Returns or sets  the absolute y coordinate.  
    
    <hr>
    
    Getter Method
    
    Signature ``Y`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Y`` 
    
    :param y: 
    :type y: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ZDepth: int = ...
    """
    Returns or sets  the Z depth.  
    
    Higher values of the Z depth indicates that the object is rendered on top of objects with a lower value. 
    
    <hr>
    
    Getter Method
    
    Signature ``ZDepth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZDepth`` 
    
    :param zDepth: 
    :type zDepth: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SheetElementBuilder = ...  # unknown typename


class ConnectableElementBuilder(SheetElementBuilder):
    """
    Represents a ConnectableElementBuilder.  
    
    This is an abstract class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def GetAllPorts(self) -> 'list[Port]':
        """
        Gets all ports of this connectable element.  
        
        Signature ``GetAllPorts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Port` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPorts(self, direction: Direction) -> 'list[Port]':
        """
        Gets ports of this connectable element by the direction.  
        
        Signature ``GetPorts(direction)`` 
        
        :param direction: 
        :type direction: :py:class:`NXOpen.Diagramming.Direction` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Port` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ConnectableElementBuilder = ...  # unknown typename


class AnnotationBuilderTextTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AnnotationBuilderTextTypeOption():
    """
    Represents the option :py:meth:`NXOpen.Diagramming.AnnotationBuilder.TextType`
    for a :py:class:`NXOpen.Diagramming.AnnotationBuilder`.
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fixed", "Setting the text type fixed"
       "Parametric", "Setting the text type parametric"
    """
    Fixed = 0  # AnnotationBuilderTextTypeOptionMemberType
    Parametric = 1  # AnnotationBuilderTextTypeOptionMemberType
    
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
    


class AnnotationBuilder(ConnectableElementBuilder):
    """
    Represents a AnnotationBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.AnnotationCollection.CreateAnnotationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class TextTypeOption():
        """
        Represents the option :py:meth:`NXOpen.Diagramming.AnnotationBuilder.TextType`
        for a :py:class:`NXOpen.Diagramming.AnnotationBuilder`.
        
        .. versionadded:: NX10.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fixed", "Setting the text type fixed"
           "Parametric", "Setting the text type parametric"
        """
        Fixed = 0  # AnnotationBuilderTextTypeOptionMemberType
        Parametric = 1  # AnnotationBuilderTextTypeOptionMemberType
        
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
        
    
    BoundaryDisplay: bool = ...
    """
    Returns or sets  the visibility of boundary.  
    
    If return true, the annotation will show its boundary if it has one. 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundaryDisplay`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoundaryDisplay`` 
    
    :param boundaryDisplay: 
    :type boundaryDisplay: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    BoundaryType: DiagrammingAnnotationboundarytype = ...
    """
    Returns or sets  the boundary type of the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundaryType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingAnnotationboundarytype` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoundaryType`` 
    
    :param boundaryType: 
    :type boundaryType: :py:class:`NXOpen.Diagramming.DiagrammingAnnotationboundarytype` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FormattedStringBuilder: FormattedStringBuilder = ...
    """
    Returns  the formatted string of the text.  
    
    <hr>
    
    Getter Method
    
    Signature ``FormattedStringBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.FormattedStringBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Text: str = ...
    """
    Returns or sets  the text should be used only when textType is Diagramming.  
    
    AnnotationBuilder.TextTypeOption.Fixed 
    
    <hr>
    
    Getter Method
    
    Signature ``Text`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Text`` 
    
    :param strValue: 
    :type strValue: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TextStyleBuilder: TextStyleBuilder = ...
    """
    Returns  the text style of the annotation.  
    
    <hr>
    
    Getter Method
    
    Signature ``TextStyleBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.TextStyleBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextType: AnnotationBuilderTextTypeOption = ...
    """
    Returns or sets  the text type.  
    
    If :py:class:`NXOpen.Diagramming.AnnotationBuilderTextTypeOption.Fixed <NXOpen.Diagramming.AnnotationBuilderTextTypeOption>`, the text
    of annotation is stored in :py:meth:`NXOpen.Diagramming.AnnotationBuilder`. 
    If :py:class:`NXOpen.Diagramming.AnnotationBuilderTextTypeOption.Parametric <NXOpen.Diagramming.AnnotationBuilderTextTypeOption>`, the text
    of annotation is stored in :py:meth:`NXOpen.Diagramming.AnnotationBuilder.FormattedStringBuilder`.
    
    <hr>
    
    Getter Method
    
    Signature ``TextType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.AnnotationBuilderTextTypeOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextType`` 
    
    :param textType: 
    :type textType: :py:class:`NXOpen.Diagramming.AnnotationBuilderTextTypeOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: AnnotationBuilder = ...  # unknown typename


class AnnotationCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Annotation.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateAnnotationBuilder(self, annotation: Annotation) -> AnnotationBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.AnnotationBuilder`.  
        
        Signature ``CreateAnnotationBuilder(annotation)`` 
        
        :param annotation:  :py:class:`NXOpen.Diagramming.Annotation` to be edited, if None then create a new one  
        :type annotation: :py:class:`NXOpen.Diagramming.Annotation` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.AnnotationBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Annotation:
        """
        Finds the :py:class:`NXOpen.Diagramming.Annotation` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Annotation` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Annotation` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class DirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Direction():
    """
    Represents the direction type.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "In", "In direction"
       "Out", "Out direction"
       "Both", "Both direction"
    """
    In = 1  # DirectionMemberType
    Out = 2  # DirectionMemberType
    Both = 3  # DirectionMemberType
    
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
    


class DefineTitleBlockBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Diagramming.DefineTitleBlockBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.TitleBlockCollection.CreateDefineTitleBlockBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    def GetTables(self) -> 'list[NXOpen.Diagramming.Tables.Table]':
        """
        Get tables.  
        
        Signature ``GetTables()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Tables.Table` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetTables(self, tables: 'list[NXOpen.Diagramming.Tables.Table]') -> None:
        """
        Set tables.  
        
        Signature ``SetTables(tables)`` 
        
        :param tables: 
        :type tables: list of :py:class:`NXOpen.Diagramming.Tables.Table` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
        Get the cell builder.  
        
        Signature ``GetCell(table, rowIndex, columnIndex)`` 
        
        :param table: 
        :type table: :py:class:`NXOpen.Diagramming.Tables.Table` 
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.TitleBlockCellBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    Null: DefineTitleBlockBuilder = ...  # unknown typename


class BaseObject(NXOpen.DisplayableObject):
    """
    Represents the BaseObject class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.BaseObjectBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: BaseObject = ...  # unknown typename


class SheetElement(BaseObject):
    """
    Represents the SheetElement class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.SheetElementBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: SheetElement = ...  # unknown typename


class Connection(SheetElement):
    """
    Represents the Connection class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.ConnectionBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: Connection = ...  # unknown typename


class LeaderLine(Connection):
    """
    Represents the LeaderLine class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.LeaderLineBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: LeaderLine = ...  # unknown typename


class DiagrammingAlignmentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingAlignment():
    """
    Represents the alignment.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Setting the left alignment"
       "Center", "Setting the center alignment"
       "Right", "Setting the right alignment"
       "Justify", "Setting the justify alignment"
    """
    Left = 0  # DiagrammingAlignmentMemberType
    Center = 1  # DiagrammingAlignmentMemberType
    Right = 2  # DiagrammingAlignmentMemberType
    Justify = 3  # DiagrammingAlignmentMemberType
    
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
    


class ArrowDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ArrowDirectionType():
    """
    the arrow direction type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OutofSheet", "Out of Sheet"
       "IntoSheet", " - "
    """
    OutofSheet = 0  # ArrowDirectionTypeMemberType
    IntoSheet = 1  # ArrowDirectionTypeMemberType
    
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
    


class LeaderLineBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[LeaderLineBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: LeaderLineBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearIndex(self, deleteIdx: int) -> None:
        """
        Deletes the item at the index specified.  
        
        The size of the list does
        *   not change, but the item at this index is set to NULL.
        
        Signature ``ClearIndex(deleteIdx)`` 
        
        :param deleteIdx:  index of item to be deleted  
        :type deleteIdx: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindIndex(self, obj: LeaderLineBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> LeaderLineBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Erase(self, index: int) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, index: int, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object at the given position from the list.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index, deleteOption)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: LeaderLineBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: LeaderLineBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Clear(self) -> None:
        """
        Clears the entire list without deleting the objects.  The caller is responsible for 
        accounting for these objects.  If they are not used or deleted by the time the part is 
        closed (in other words, leaked) an error will occur 
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Clear(self, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Clears the entire list 
        
        Signature ``Clear(deleteOption)`` 
        
        :param deleteOption:  whether to delete the objects when removing them  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContents(self) -> 'list[LeaderLineBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[LeaderLineBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Swap(self, index1: int, index2: int) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(index1, index2)`` 
        
        :param index1:  location of the first item  
        :type index1: int 
        :param index2:  location of the second item  
        :type index2: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Swap(self, object1: LeaderLineBuilder, object2: LeaderLineBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: LeaderLineBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToTop(self, index: int) -> None:
        """
        Move object at the specified location to the top of the list.  
        
        Signature ``MoveToTop(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToBottom(self, index: int) -> None:
        """
        Move object at the specified location to the bottom of the list.  
        
        Signature ``MoveToBottom(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Length: int = ...
    """
    Returns  the length of the list 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: LeaderLineBuilderList = ...  # unknown typename


class DiagrammingJumpertypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingJumpertype():
    """
    Represents the jumper type.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "U", "U shape"
       "Break", "Break"
    """
    U = 1  # DiagrammingJumpertypeMemberType
    Break = 2  # DiagrammingJumpertypeMemberType
    
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
    


class PortBuilder(SheetElementBuilder):
    """
    Represents a PortBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.PortCollection.CreatePortBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetAllowedParentSides(self) -> tuple:
        """
        Get allowed parent sides.  
        
        Signature ``GetAllowedParentSides()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (isAllowedLeftSide, isAllowedRightSide, isAllowedUpSide, isAllowedDownSide). isAllowedLeftSide is a bool. isAllowedRightSide is a bool. isAllowedUpSide is a bool. isAllowedDownSide is a bool. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanAnotherConnectionBeAdded(self) -> bool:
        """
        Get whether another connection can be added or not.  
        
        Signature ``CanAnotherConnectionBeAdded()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsNumberOfConnectionInfinite(self) -> bool:
        """
        Get if the number of connections to reference is infinite.  
        
        If true it is infinite.  
        
        Signature ``IsNumberOfConnectionInfinite()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOwningConnectableElement(self) -> ConnectableElement:
        """
        Get the owner connectable element.  
        
        Signature ``GetOwningConnectableElement()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.ConnectableElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetConnections(self) -> 'list[Connection]':
        """
        Get associated connections.  
        
        Signature ``GetConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Connection` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Direction: Direction = ...
    """
    Returns or sets  the direction of the port.  
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Diagramming.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    NumberAllowedConnections: int = ...
    """
    Returns or sets  the maximum number of allowed connections the port may reference.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberAllowedConnections`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberAllowedConnections`` 
    
    :param numberAllowedConnections: 
    :type numberAllowedConnections: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Pinned: bool = ...
    """
    Returns or sets  the flag that indicates the port is pinned.  
    
    If true the port is pinned and cannot be moved. 
    
    <hr>
    
    Getter Method
    
    Signature ``Pinned`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Pinned`` 
    
    :param isPinned: 
    :type isPinned: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Proxy: Port = ...
    """
    Returns or sets  the proxy port for the port inside the super node.  
    
    <hr>
    
    Getter Method
    
    Signature ``Proxy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Proxy`` 
    
    :param proxy: 
    :type proxy: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: PortBuilder = ...  # unknown typename


class ConnectionBuilder(SheetElementBuilder):
    """
    Represents a ConnectionBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.ConnectionCollection.CreateConnectionBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetBendPoints(self) -> 'list[NXOpen.Point2d]':
        """
        Get bending points for polyline to render the connection.  
        
        Signature ``GetBendPoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBendPoints(self, points: 'list[NXOpen.Point2d]') -> None:
        """
        Set bending points for polyline to render the connection.  
        
        Signature ``SetBendPoints(points)`` 
        
        :param points: 
        :type points: list of :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Discipline: str = ...
    """
    Returns or sets  the discipline of this connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``Discipline`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Discipline`` 
    
    :param discipline: 
    :type discipline: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    End: Port = ...
    """
    Returns or sets  the end port of this connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``End`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``End`` 
    
    :param endPort: 
    :type endPort: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    EndLocation: LocationBuilder = ...
    """
    Returns  the end location of this connection.  
    
    This end location is applicable only when the :py:meth:`Diagramming.ConnectionBuilder.End` port is None. 
    
    <hr>
    
    Getter Method
    
    Signature ``EndLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LocationBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ReverseEnd: bool = ...
    """
    Returns  the reversed flag of this connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseEnd`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Start: Port = ...
    """
    Returns or sets  the start port of this connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``Start`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Start`` 
    
    :param startPort: 
    :type startPort: :py:class:`NXOpen.Diagramming.Port` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    StartLocation: LocationBuilder = ...
    """
    Returns  the start location of this connection.  
    
    This start location is applicable only when the :py:meth:`Diagramming.ConnectionBuilder.Start` is None.
    
    <hr>
    
    Getter Method
    
    Signature ``StartLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LocationBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: ConnectionBuilder = ...  # unknown typename


class TitleBlockCellBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a builder to edit :py:class:`NXOpen.Diagramming.TitleBlock`'s cell 
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX11.0.1
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
    
    Label: str = ...
    """
    Returns or sets  the cell label 
    
    <hr>
    
    Getter Method
    
    Signature ``Label`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Label`` 
    
    :param label: 
    :type label: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Lock: bool = ...
    """
    Returns or sets  the lock status 
    
    <hr>
    
    Getter Method
    
    Signature ``Lock`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Lock`` 
    
    :param lockStatus: 
    :type lockStatus: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Value: str = ...
    """
    Returns or sets  the editable text of the cell 
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param text: 
    :type text: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: drafting ("DRAFTING")
    """
    Null: TitleBlockCellBuilder = ...  # unknown typename


class ConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of connection.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.ConnectionBuilder`.  
        
        Signature ``CreateConnectionBuilder(connection)`` 
        
        :param connection:  :py:class:`NXOpen.Diagramming.Connection` to be edited, if None then create a new one  
        :type connection: :py:class:`NXOpen.Diagramming.Connection` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.ConnectionBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Connection:
        """
        Finds the :py:class:`NXOpen.Diagramming.Connection` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Connection` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Connection` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class TitleBlock(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.Diagramming.TitleBlock`   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.DefineTitleBlockBuilder`
    
    .. versionadded:: NX11.0.1
    """
    Null: TitleBlock = ...  # unknown typename


class GroupCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of group.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateGroupBuilder(self, group: Group) -> GroupBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.GroupBuilder`.  
        
        Signature ``CreateGroupBuilder(group)`` 
        
        :param group:  :py:class:`NXOpen.Diagramming.Group` to be edited, if None then create a new one  
        :type group: :py:class:`NXOpen.Diagramming.Group` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.GroupBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Group:
        """
        Finds the :py:class:`NXOpen.Diagramming.Group` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Group` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Group` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class AxisMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Axis():
    """
    Represents the axis type.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "X axis"
       "Y", "Y axis"
    """
    X = 1  # AxisMemberType
    Y = 2  # AxisMemberType
    
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
    


class SheetCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Sheet.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSheetBuilder(self, sheet: Sheet) -> SheetBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.SheetBuilder`.  
        
        Signature ``CreateSheetBuilder(sheet)`` 
        
        :param sheet:  :py:class:`NXOpen.Diagramming.Sheet` to be edited, if None then create a new one  
        :type sheet: :py:class:`NXOpen.Diagramming.Sheet` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.SheetBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Sheet:
        """
        Finds the :py:class:`NXOpen.Diagramming.Sheet` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Sheet` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Sheet` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class DiagrammingSizingpolicyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingSizingpolicy():
    """
    Represents the sizing policy type.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Length", "Length policy"
       "Auto", "Auto policy"
       "Percent", "Percent policy"
       "Inherit", "Inherit policy"
    """
    Length = 0  # DiagrammingSizingpolicyMemberType
    Auto = 1  # DiagrammingSizingpolicyMemberType
    Percent = 2  # DiagrammingSizingpolicyMemberType
    Inherit = 4  # DiagrammingSizingpolicyMemberType
    
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
    


class BaseTaggedObjectBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a BaseTaggedObjectBuilder.  
    
    This is an abstract and sub-builder class and cannot be directly instantiated
    
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
    
    Null: BaseTaggedObjectBuilder = ...  # unknown typename


class DiagrammingConnectionlabelpositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingConnectionlabelposition():
    """
    Represents the connection label position.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Start", "Start"
       "End", "End"
       "Center", "Centered"
       "Spaced", "Spaced"
    """
    Start = 1  # DiagrammingConnectionlabelpositionMemberType
    End = 2  # DiagrammingConnectionlabelpositionMemberType
    Center = 4  # DiagrammingConnectionlabelpositionMemberType
    Spaced = 8  # DiagrammingConnectionlabelpositionMemberType
    
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
    


class ShapeCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Shape.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateShapeBuilder(self, shape: Shape) -> ShapeBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.ShapeBuilder`.  
        
        Signature ``CreateShapeBuilder(shape)`` 
        
        :param shape:  :py:class:`NXOpen.Diagramming.Shape` to be edited, if None then create a new one  
        :type shape: :py:class:`NXOpen.Diagramming.Shape` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.ShapeBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Shape:
        """
        Finds the :py:class:`NXOpen.Diagramming.Shape` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Shape` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Shape` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class HorizontalCenteringMarkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HorizontalCenteringMarkType():
    """
    the horizontal centering mark type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "LeftArrow", "Left Arrow"
       "RightArrow", "Right Arrow"
       "LeftandRightArrow", "Left and Right Arrow"
       "LeftandRightLine", " - "
    """
    NotSet = 0  # HorizontalCenteringMarkTypeMemberType
    LeftArrow = 1  # HorizontalCenteringMarkTypeMemberType
    RightArrow = 2  # HorizontalCenteringMarkTypeMemberType
    LeftandRightArrow = 3  # HorizontalCenteringMarkTypeMemberType
    LeftandRightLine = 4  # HorizontalCenteringMarkTypeMemberType
    
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
    


class DiagrammingStubsidesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingStubsides():
    """
    Represents the stub side type.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Auto", "Auto side"
       "Left", "Left side"
       "Right", "Right side"
    """
    Auto = 0  # DiagrammingStubsidesMemberType
    Left = 1  # DiagrammingStubsidesMemberType
    Right = 2  # DiagrammingStubsidesMemberType
    
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
    


class PortBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[PortBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: PortBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearIndex(self, deleteIdx: int) -> None:
        """
        Deletes the item at the index specified.  
        
        The size of the list does
        *   not change, but the item at this index is set to NULL.
        
        Signature ``ClearIndex(deleteIdx)`` 
        
        :param deleteIdx:  index of item to be deleted  
        :type deleteIdx: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindIndex(self, obj: PortBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Diagramming.PortBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> PortBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Erase(self, index: int) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, index: int, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object at the given position from the list.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index, deleteOption)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PortBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PortBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.PortBuilder` 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Clear(self) -> None:
        """
        Clears the entire list without deleting the objects.  The caller is responsible for 
        accounting for these objects.  If they are not used or deleted by the time the part is 
        closed (in other words, leaked) an error will occur 
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Clear(self, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Clears the entire list 
        
        Signature ``Clear(deleteOption)`` 
        
        :param deleteOption:  whether to delete the objects when removing them  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContents(self) -> 'list[PortBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[PortBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Swap(self, index1: int, index2: int) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(index1, index2)`` 
        
        :param index1:  location of the first item  
        :type index1: int 
        :param index2:  location of the second item  
        :type index2: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Swap(self, object1: PortBuilder, object2: PortBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Diagramming.PortBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: PortBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToTop(self, index: int) -> None:
        """
        Move object at the specified location to the top of the list.  
        
        Signature ``MoveToTop(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToBottom(self, index: int) -> None:
        """
        Move object at the specified location to the bottom of the list.  
        
        Signature ``MoveToBottom(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Length: int = ...
    """
    Returns  the length of the list 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: PortBuilderList = ...  # unknown typename


class DiagrammingFlowdirectionarrowstyleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingFlowdirectionarrowstyle():
    """
    Represents the flow direction arrow style.   
    
    .. versionadded:: NX11.0.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BottomFilledArrow", " - "
       "BottomOpenArrow", " - "
       "ClosedArrow", " - "
       "ClosedDoubleArrow", " - "
       "ClosedDoubleSolidArrow", " - "
       "ClosedSolidArrow", " - "
       "FilledArrow", " - "
       "FilledDoubleArrow", " - "
       "OpenArrow", " - "
       "OpenDoubleArrow", " - "
       "TopFilledArrow", " - "
       "TopOpenArrow", " - "
    """
    BottomFilledArrow = 0  # DiagrammingFlowdirectionarrowstyleMemberType
    BottomOpenArrow = 1  # DiagrammingFlowdirectionarrowstyleMemberType
    ClosedArrow = 2  # DiagrammingFlowdirectionarrowstyleMemberType
    ClosedDoubleArrow = 3  # DiagrammingFlowdirectionarrowstyleMemberType
    ClosedDoubleSolidArrow = 4  # DiagrammingFlowdirectionarrowstyleMemberType
    ClosedSolidArrow = 5  # DiagrammingFlowdirectionarrowstyleMemberType
    FilledArrow = 6  # DiagrammingFlowdirectionarrowstyleMemberType
    FilledDoubleArrow = 7  # DiagrammingFlowdirectionarrowstyleMemberType
    OpenArrow = 8  # DiagrammingFlowdirectionarrowstyleMemberType
    OpenDoubleArrow = 9  # DiagrammingFlowdirectionarrowstyleMemberType
    TopFilledArrow = 10  # DiagrammingFlowdirectionarrowstyleMemberType
    TopOpenArrow = 11  # DiagrammingFlowdirectionarrowstyleMemberType
    
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
    


class DiagrammingJumperprioritytypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingJumperprioritytype():
    """
    Represents the jumper priority.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Horizontal", "Horizontal"
       "Vertical", "Vertical"
    """
    Horizontal = 0  # DiagrammingJumperprioritytypeMemberType
    Vertical = 1  # DiagrammingJumperprioritytypeMemberType
    
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
    


class BulkEditBuilder(NXOpen.Builder):
    """
    Represents a BulkEditBuilder to edit bulk of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.DiagrammingManager.CreateBulkEditBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def SetSheetElements(self, sheetElements: 'list[SheetElement]') -> None:
        """
        Sets the sheet elements for bulk editing.  
        
        Signature ``SetSheetElements(sheetElements)`` 
        
        :param sheetElements: 
        :type sheetElements: list of :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDeltaXCoordinate(self, deltaXCoordinate: float) -> None:
        """
        Sets the delta value of X coordinate for bulk moving.  
        
        Signature ``SetDeltaXCoordinate(deltaXCoordinate)`` 
        
        :param deltaXCoordinate: 
        :type deltaXCoordinate: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDeltaYCoordinate(self, deltaYCoordinate: float) -> None:
        """
        Sets the delta value of Y coordinate for bulk moving.  
        
        Signature ``SetDeltaYCoordinate(deltaYCoordinate)`` 
        
        :param deltaYCoordinate: 
        :type deltaYCoordinate: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHide(self, hide: bool) -> None:
        """
        Sets the visibility of sheet elements.  
        
        Signature ``SetHide(hide)`` 
        
        :param hide: 
        :type hide: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetHideLabel(self, hideLabel: bool) -> None:
        """
        Sets the visibility of labels.  
        
        Signature ``SetHideLabel(hideLabel)`` 
        
        :param hideLabel: 
        :type hideLabel: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    RenderingProperties: RenderingPropertiesBuilder = ...
    """
    Returns  the line rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``RenderingProperties`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: BulkEditBuilder = ...  # unknown typename


class FontEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FontEnum():
    """
    the font 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Blockfont", " - "
    """
    Blockfont = 0  # FontEnumMemberType
    
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
    


class ConnectableElement(SheetElement):
    """
    Represents the ConnectableElement class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.ConnectableElementBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: ConnectableElement = ...  # unknown typename


class Shape(ConnectableElement):
    """
    Represents the Shape class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.ShapeBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: Shape = ...  # unknown typename


class ConnectionLocationBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[ConnectionLocationBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: ConnectionLocationBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearIndex(self, deleteIdx: int) -> None:
        """
        Deletes the item at the index specified.  
        
        The size of the list does
        *   not change, but the item at this index is set to NULL.
        
        Signature ``ClearIndex(deleteIdx)`` 
        
        :param deleteIdx:  index of item to be deleted  
        :type deleteIdx: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindIndex(self, obj: ConnectionLocationBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> ConnectionLocationBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Erase(self, index: int) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, index: int, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object at the given position from the list.
        The list is shifted so that there isn't a null where the object used to be. 
        
        Signature ``Erase(index, deleteOption)`` 
        
        :param index:  index of item to be removed from the list  
        :type index: int 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: ConnectionLocationBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: ConnectionLocationBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        :param deleteOption:  whether to delete the object  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Clear(self) -> None:
        """
        Clears the entire list without deleting the objects.  The caller is responsible for 
        accounting for these objects.  If they are not used or deleted by the time the part is 
        closed (in other words, leaked) an error will occur 
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Clear(self, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Clears the entire list 
        
        Signature ``Clear(deleteOption)`` 
        
        :param deleteOption:  whether to delete the objects when removing them  
        :type deleteOption: :py:class:`NXOpen.ObjectListDeleteOption` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContents(self) -> 'list[ConnectionLocationBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[ConnectionLocationBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Swap(self, index1: int, index2: int) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(index1, index2)`` 
        
        :param index1:  location of the first item  
        :type index1: int 
        :param index2:  location of the second item  
        :type index2: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Swap(self, object1: ConnectionLocationBuilder, object2: ConnectionLocationBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: ConnectionLocationBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Diagramming.ConnectionLocationBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToTop(self, index: int) -> None:
        """
        Move object at the specified location to the top of the list.  
        
        Signature ``MoveToTop(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToBottom(self, index: int) -> None:
        """
        Move object at the specified location to the bottom of the list.  
        
        Signature ``MoveToBottom(index)`` 
        
        :param index:  location of the item  
        :type index: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Length: int = ...
    """
    Returns  the length of the list 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: ConnectionLocationBuilderList = ...  # unknown typename


class LeaderLineBuilderVerticalAlignmentOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LeaderLineBuilderVerticalAlignmentOption():
    """
    Represents the option :py:meth:`NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignment`
    for a :py:class:`NXOpen.Diagramming.LeaderLineBuilder`.
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", "Setting the vertical alignment top"
       "Middle", "Setting the vertical alignment middle"
       "Bottom", "Setting the vertical alignment bottom"
    """
    Top = 0  # LeaderLineBuilderVerticalAlignmentOptionMemberType
    Middle = 1  # LeaderLineBuilderVerticalAlignmentOptionMemberType
    Bottom = 2  # LeaderLineBuilderVerticalAlignmentOptionMemberType
    
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
    


class LeaderLineBuilder(SheetElementBuilder):
    """
    Represents a LeaderLineBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.LeaderLineCollection.CreateLeaderLineBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class VerticalAlignmentOption():
        """
        Represents the option :py:meth:`NXOpen.Diagramming.LeaderLineBuilder.VerticalAlignment`
        for a :py:class:`NXOpen.Diagramming.LeaderLineBuilder`.
        
        .. versionadded:: NX10.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Top", "Setting the vertical alignment top"
           "Middle", "Setting the vertical alignment middle"
           "Bottom", "Setting the vertical alignment bottom"
        """
        Top = 0  # LeaderLineBuilderVerticalAlignmentOptionMemberType
        Middle = 1  # LeaderLineBuilderVerticalAlignmentOptionMemberType
        Bottom = 2  # LeaderLineBuilderVerticalAlignmentOptionMemberType
        
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
        
    
    
    def GetBendPoints(self) -> 'list[NXOpen.Point2d]':
        """
        Get bending points for polyline to render the leader line.  
        
        Signature ``GetBendPoints()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBendPoints(self, points: 'list[NXOpen.Point2d]') -> None:
        """
        Set bending points for polyline to render the leader line.  
        
        Signature ``SetBendPoints(points)`` 
        
        :param points: 
        :type points: list of :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTerminator(self, terminator: SheetElement, segmentId: int, percentX: float, inputX: float, percentY: float, inputY: float) -> None:
        """
        Sets the terminator of the leader.  
        
        Signature ``SetTerminator(terminator, segmentId, percentX, inputX, percentY, inputY)`` 
        
        :param terminator: 
        :type terminator: :py:class:`NXOpen.Diagramming.SheetElement` 
        :param segmentId: 
        :type segmentId: int 
        :param percentX: 
        :type percentX: float 
        :param inputX: 
        :type inputX: float 
        :param percentY: 
        :type percentY: float 
        :param inputY: 
        :type inputY: float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetTerminator(self) -> tuple:
        """
        Gets the terminator of the leader.  
        
        Signature ``GetTerminator()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (terminator, segmentId, percentX, inputX, percentY, inputY). terminator is a :py:class:`NXOpen.Diagramming.SheetElement`. segmentId is a int. percentX is a float. inputX is a float. percentY is a float. inputY is a float. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    ArrowType: DiagrammingArrowtype = ...
    """
    Returns or sets  the arrow type of the end arrow 
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingArrowtype` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowType`` 
    
    :param arrowTypeOption: 
    :type arrowTypeOption: :py:class:`NXOpen.Diagramming.DiagrammingArrowtype` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    StubLength: float = ...
    """
    Returns or sets  the stub length of this leader line.  
    
    The negative value is not expected.
    
    <hr>
    
    Getter Method
    
    Signature ``StubLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StubLength`` 
    
    :param stubLength: 
    :type stubLength: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    StubSides: DiagrammingStubsides = ...
    """
    Returns or sets  the stub sides of this leader line.  
    
    <hr>
    
    Getter Method
    
    Signature ``StubSides`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingStubsides` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StubSides`` 
    
    :param stubSides: 
    :type stubSides: :py:class:`NXOpen.Diagramming.DiagrammingStubsides` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    VerticalAlignment: LeaderLineBuilderVerticalAlignmentOption = ...
    """
    Returns or sets  the vertical alignment option.  
    
    <hr>
    
    Getter Method
    
    Signature ``VerticalAlignment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LeaderLineBuilderVerticalAlignmentOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VerticalAlignment`` 
    
    :param alignmentOption: 
    :type alignmentOption: :py:class:`NXOpen.Diagramming.LeaderLineBuilderVerticalAlignmentOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: LeaderLineBuilder = ...  # unknown typename


class Group(SheetElement):
    """
    Represents the Group class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.GroupBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: Group = ...  # unknown typename


class SheetBuilder(BaseObjectBuilder):
    """
    Represents a SheetBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.SheetCollection.CreateSheetBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetFeatures(self) -> 'list[SheetElement]':
        """
        Gets all features.  
        
        Signature ``GetFeatures()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSheetElements(self) -> 'list[SheetElement]':
        """
        Gets all sheet elements.  
        
        Signature ``GetSheetElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSize(self) -> tuple:
        """
        Gets the height and width of this sheet.  
        
        Signature ``GetSize()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (height, width). height is a float. width is a float. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSize(self, height: float, width: float) -> None:
        """
        Sets the height and width of this sheet.  
        
        Signature ``SetSize(height, width)`` 
        
        :param height: 
        :type height: float 
        :param width: 
        :type width: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    AllowJumpers: bool = ...
    """
    Returns or sets  the flag if jumpers are allowed to use where connections cross.  
    
    <hr>
    
    Getter Method
    
    Signature ``AllowJumpers`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowJumpers`` 
    
    :param allowJumper: 
    :type allowJumper: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Description: str = ...
    """
    Returns or sets  the description that will be visible when a template is selected in the Item Rev dialog.  
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    JumperType: DiagrammingJumpertype = ...
    """
    Returns or sets  the jumper type of the sheet.  
    
    <hr>
    
    Getter Method
    
    Signature ``JumperType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.DiagrammingJumpertype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``JumperType`` 
    
    :param jumperType: 
    :type jumperType: :py:class:`NXOpen.Diagramming.DiagrammingJumpertype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Opacity: float = ...
    """
    Returns or sets  the opacity of sheet.  
    
    0.0 is completely transparent and 1.0 is completely opaque
    
    <hr>
    
    Getter Method
    
    Signature ``Opacity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Opacity`` 
    
    :param opacity: 
    :type opacity: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    PaxFileName: str = ...
    """
    Returns or sets  the path name of the PAX file to which the template will be written to.  
    
    <hr>
    
    Getter Method
    
    Signature ``PaxFileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PaxFileName`` 
    
    :param paxFileName: 
    :type paxFileName: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    PresentationName: str = ...
    """
    Returns or sets  the presentation name that will be visible in the "Presentation" column of the Item Rev dialog.  
    
    <hr>
    
    Getter Method
    
    Signature ``PresentationName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PresentationName`` 
    
    :param presentationName: 
    :type presentationName: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ToolTip: str = ...
    """
    Returns or sets  the tooltip that will be visible when a template is selected in the Item Rev dialog.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToolTip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolTip`` 
    
    :param toolTip: 
    :type toolTip: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Units: NXOpen.Unit = ...
    """
    Returns or sets  the units of the sheet.  
    
    It could be either "meters" or "inches". 
    
    <hr>
    
    Getter Method
    
    Signature ``Units`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Units`` 
    
    :param unit: 
    :type unit: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    UpdatePAXFile: bool = ...
    """
    Returns or sets  the flag to update pax file or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``UpdatePAXFile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpdatePAXFile`` 
    
    :param updatePAXFile: 
    :type updatePAXFile: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SheetBuilder = ...  # unknown typename


class BaseSubObjectBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a BaseSubObjectBuilder.  
    
    This is an abstract and sub-builder class and cannot be directly instantiated
    
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
    
    Null: BaseSubObjectBuilder = ...  # unknown typename


class LocationBuilder(BaseSubObjectBuilder):
    """
    Represents a LocationBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def SetValueX(self, inputPercent: float, inputValue: float) -> None:
        """
        Set the x value of the location.  
        
        The inputPercent means of the x coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
        The inputValue means the offset value of the x coordinate from the calculated location by the inputPercent value. 
        
        Signature ``SetValueX(inputPercent, inputValue)`` 
        
        :param inputPercent: 
        :type inputPercent: float 
        :param inputValue: 
        :type inputValue: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueY(self, inputPercent: float, inputValue: float) -> None:
        """
        Set the y value of the location.  
        
        The inputPercent means of the y coordinate value as a percentage of the size of its reference object. The valid value is from 0.0 to 1.0, and 1.0 means 100%.
        The inputValue means the offset value of the y coordinate from the calculated location by the inputPercent value. 
        
        Signature ``SetValueY(inputPercent, inputValue)`` 
        
        :param inputPercent: 
        :type inputPercent: float 
        :param inputValue: 
        :type inputValue: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    EvaluatedValueX: float = ...
    """
    Returns  the evaluated X coordinate value that is the result calculated by the input percentage and offset.  
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluatedValueX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    EvaluatedValueY: float = ...
    """
    Returns  the evaluated Y coordinate value that is the result calculated by input percentage and offset.  
    
    <hr>
    
    Getter Method
    
    Signature ``EvaluatedValueY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InputPercentX: float = ...
    """
    Returns or sets  the user input percentage (0.  
    
    0 to 1.0) of the width of the referenced object. 
    
    <hr>
    
    Getter Method
    
    Signature ``InputPercentX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputPercentX`` 
    
    :param inputPercentX: 
    :type inputPercentX: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InputPercentY: float = ...
    """
    Returns or sets  the user input percentage (0.  
    
    0 to 1.0) of the height of the referenced object. 
    
    <hr>
    
    Getter Method
    
    Signature ``InputPercentY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputPercentY`` 
    
    :param inputPercentY: 
    :type inputPercentY: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InputValueX: float = ...
    """
    Returns or sets  the user input X coordinate.  
    
    If the location refers to an object, the input X is the offset to the X coordinate of the object; Otherwise, it's the X coordinate value. 
    
    <hr>
    
    Getter Method
    
    Signature ``InputValueX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputValueX`` 
    
    :param inputValueX: 
    :type inputValueX: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InputValueY: float = ...
    """
    Returns or sets  the user input Y coordinate.  
    
    If the location refers to an object, the input Y is the offset to the Y coordinate of the object; Otherwise, it's the Y coordinate value. 
    
    <hr>
    
    Getter Method
    
    Signature ``InputValueY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputValueY`` 
    
    :param inputValueY: 
    :type inputValueY: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Reference: SheetElement = ...
    """
    Returns or sets  the sheet element whose coordinate system the coordinate is specified in.  
    
    If this is None, the coordinate is in the Sheet's coordinate system. 
    
    <hr>
    
    Getter Method
    
    Signature ``Reference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetElement` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Reference`` 
    
    :param reference: 
    :type reference: :py:class:`NXOpen.Diagramming.SheetElement` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    UpToDate: bool = ...
    """
    Returns  the up to date flag.  
    
    If true, :py:meth:`NXOpen.Diagramming.LocationBuilder.EvaluatedValueX` and :py:meth:`NXOpen.Diagramming.LocationBuilder.EvaluatedValueY`
    of :py:class:`NXOpen.Diagramming.LocationBuilder` may be used; Otherwise it must be evaluated.
    
    <hr>
    
    Getter Method
    
    Signature ``UpToDate`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: LocationBuilder = ...  # unknown typename


class ConnectionLocationBuilder(LocationBuilder):
    """
    Represents a ConnectionLocationBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    SegmentIdentifier: int = ...
    """
    Returns or sets  the segment identifier.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentIdentifier`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SegmentIdentifier`` 
    
    :param segmentId: 
    :type segmentId: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: ConnectionLocationBuilder = ...  # unknown typename


class Port(SheetElement):
    """
    Represents the Port class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.PortBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: Port = ...  # unknown typename


class ZoneOriginMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ZoneOrigin():
    """
    the zone origin 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BottomRight", "Bottom Right"
       "TopLeft", "Top Left"
       "TopRight", "Top Right"
       "BottomLeft", " - "
    """
    BottomRight = 0  # ZoneOriginMemberType
    TopLeft = 1  # ZoneOriginMemberType
    TopRight = 2  # ZoneOriginMemberType
    BottomLeft = 3  # ZoneOriginMemberType
    
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
    


class DiagrammingLocationstyleMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingLocationstyle():
    """
    Represents the location style.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Absolute", "Absolute"
       "Relative", "Relative"
    """
    Absolute = 0  # DiagrammingLocationstyleMemberType
    Relative = 1  # DiagrammingLocationstyleMemberType
    
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
    


class DiagrammingManager():
    """
    A manager to deal with all objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX10.0.0
    """
    
    def CreateBulkEditBuilder(self) -> BulkEditBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.BulkEditBuilder`  
        
        Signature ``CreateBulkEditBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.BulkEditBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateCannedAnnotationBuilder(self, annotation: Annotation) -> CannedAnnotationBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.CannedAnnotationBuilder`.  
        
        Signature ``CreateCannedAnnotationBuilder(annotation)`` 
        
        :param annotation:  :py:class:`NXOpen.Diagramming.Annotation` to be edited, if None then create a new one  
        :type annotation: :py:class:`NXOpen.Diagramming.Annotation` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.CannedAnnotationBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def OpenSheet(self, sheet: Sheet) -> None:
        """
        Opens a :py:class:`NXOpen.Diagramming.Sheet`.  
        
        Signature ``OpenSheet(sheet)`` 
        
        :param sheet: 
        :type sheet: :py:class:`NXOpen.Diagramming.Sheet` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX12.0.0
           Moved to SheetManager
        
        License requirements: None.
        """
        ...
    
    ActiveSheet: Sheet = ...
    """
    Returns or sets  the active sheet 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveSheet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Sheet` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Moved to SheetManager
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveSheet`` 
    
    :param sheet: 
    :type sheet: :py:class:`NXOpen.Diagramming.Sheet` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Moved to SheetManager
    
    License requirements: None.
    """
    Nodes: NodeCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.NodeCollection` belonging to this part 
    
    Signature ``Nodes`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.NodeCollection`
    """
    Sheets: SheetCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.SheetCollection` belonging to this part 
    
    Signature ``Sheets`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetCollection`
    """
    Connections: ConnectionCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.ConnectionCollection` belonging to this part 
    
    Signature ``Connections`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.ConnectionCollection`
    """
    Groups: GroupCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.GroupCollection` belonging to this part 
    
    Signature ``Groups`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.GroupCollection`
    """
    Shapes: ShapeCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.ShapeCollection` belonging to this part 
    
    Signature ``Shapes`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.ShapeCollection`
    """
    Ports: PortCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.PortCollection` belonging to this part 
    
    Signature ``Ports`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.PortCollection`
    """
    Annotations: AnnotationCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.AnnotationCollection` belonging to this part 
    
    Signature ``Annotations`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.AnnotationCollection`
    """
    LeaderLines: LeaderLineCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.LeaderLineCollection` belonging to this part 
    
    Signature ``LeaderLines`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LeaderLineCollection`
    """
    SheetBordersAndZones: SheetBordersAndZonesCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.SheetBordersAndZonesCollection` belonging to this part 
    
    Signature ``SheetBordersAndZones`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesCollection`
    """
    Tables: NXOpen.Diagramming.Tables.TableCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.Tables.TableCollection` belonging to this part 
    
    Signature ``Tables`` 
    
    .. versionadded:: NX10.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.TableCollection`
    """
    TitleBlocks: TitleBlockCollection = ...
    """
    Returns the :py:class:`NXOpen.Diagramming.TitleBlockCollection` belonging to this part 
    
    Signature ``TitleBlocks`` 
    
    .. versionadded:: NX11.0.1
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.TitleBlockCollection`
    """


class SheetMarginSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The SheetMarginSettings builder   
    
    .. versionadded:: NX11.0.1
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
    
    BottomTrimmedMargin: float = ...
    """
    Returns or sets  the value of the margin in bottom border.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomTrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BottomTrimmedMargin`` 
    
    :param bottomTrimmedMargin: 
    :type bottomTrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    BottomUntrimmedMargin: float = ...
    """
    Returns or sets  the distance between bottom of the sheet and bottom trimmed margin.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomUntrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BottomUntrimmedMargin`` 
    
    :param bottomUntrimmedMargin: 
    :type bottomUntrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateUntrimmedMargins: bool = ...
    """
    Returns or sets  the flag indicates to create untrimmed margins or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateUntrimmedMargins`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateUntrimmedMargins`` 
    
    :param createUntrimmedMargins: 
    :type createUntrimmedMargins: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LeftTrimmedMargin: float = ...
    """
    Returns or sets  the value of the margin in left border.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeftTrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LeftTrimmedMargin`` 
    
    :param leftTrimmedMargin: 
    :type leftTrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LeftUntrimmedMargin: float = ...
    """
    Returns or sets  the distance between left of the sheet and left trimmed margin.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeftUntrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LeftUntrimmedMargin`` 
    
    :param leftUntrimmedMargin: 
    :type leftUntrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    MarginLineColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font and width of margin line.  
    
    <hr>
    
    Getter Method
    
    Signature ``MarginLineColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    RightTrimmedMargin: float = ...
    """
    Returns or sets  the value of the margin in right border.  
    
    <hr>
    
    Getter Method
    
    Signature ``RightTrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RightTrimmedMargin`` 
    
    :param rightTrimmedMargin: 
    :type rightTrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    RightUntrimmedMargin: float = ...
    """
    Returns or sets  the distance between right of the sheet and right trimmed margin.  
    
    <hr>
    
    Getter Method
    
    Signature ``RightUntrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RightUntrimmedMargin`` 
    
    :param rightUntrimmedMargin: 
    :type rightUntrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TopTrimmedMargin: float = ...
    """
    Returns or sets  the value of the margin in top border.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopTrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TopTrimmedMargin`` 
    
    :param topMargin: 
    :type topMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TopUntrimmedMargin: float = ...
    """
    Returns or sets  the distance between top of the sheet and top trimmed margin.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopUntrimmedMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TopUntrimmedMargin`` 
    
    :param topUntrimmedMargin: 
    :type topUntrimmedMargin: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SheetMarginSettingsBuilder = ...  # unknown typename


class DiagrammingConnectionlabelverticaloffsetpositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingConnectionlabelverticaloffsetposition():
    """
    Represents the vertical connection label offset position.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Left"
       "Right", "Right"
    """
    Left = 0  # DiagrammingConnectionlabelverticaloffsetpositionMemberType
    Right = 1  # DiagrammingConnectionlabelverticaloffsetpositionMemberType
    
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
    


class SheetZoneSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The SheetZoneSettings builder   
    
    .. versionadded:: NX11.0.1
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
    
    ContinueZoneIndexingAcrossSheets: bool = ...
    """
    Returns or sets  the flag indicates whether the index for horizontal numeric zone labels will continue onto the next sheet or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContinueZoneIndexingAcrossSheets`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContinueZoneIndexingAcrossSheets`` 
    
    :param continueZoneIndexingAcrossSheets: 
    :type continueZoneIndexingAcrossSheets: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CornerZoneModification: float = ...
    """
    Returns or sets  the corner zone modification used as determine the size of the corner zone.  
    
    <hr>
    
    Getter Method
    
    Signature ``CornerZoneModification`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CornerZoneModification`` 
    
    :param cornerZoneModification: 
    :type cornerZoneModification: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateZoneLabels: bool = ...
    """
    Returns or sets  the flag indicates to create zone labels or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateZoneLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateZoneLabels`` 
    
    :param createZoneLabels: 
    :type createZoneLabels: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateZoneMarkings: bool = ...
    """
    Returns or sets  the flag indicates to create zone markings or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateZoneMarkings`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateZoneMarkings`` 
    
    :param createZoneMarkings: 
    :type createZoneMarkings: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateZones: bool = ...
    """
    Returns or sets  the flag indicates to create zones or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateZones`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateZones`` 
    
    :param createZones: 
    :type createZones: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    HorizontalSize: float = ...
    """
    Returns or sets  the size of the horizontal zone.  
    
    It must be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``HorizontalSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HorizontalSize`` 
    
    :param horizontalSize: 
    :type horizontalSize: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelColor: int = ...
    """
    Returns or sets  the color of the label(text).  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelColor`` 
    
    :param labelColor: 
    :type labelColor: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelFont: int = ...
    """
    Returns or sets  the font of the label(text).  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelFont`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelFont`` 
    
    :param labelFont: 
    :type labelFont: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelHeight: float = ...
    """
    Returns or sets  the height of the label(text).  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelHeight`` 
    
    :param labelHeight: 
    :type labelHeight: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelItalicized: bool = ...
    """
    Returns or sets  the flag indicates the label(text) is italic or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelItalicized`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelItalicized`` 
    
    :param italic: 
    :type italic: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelWidth: int = ...
    """
    Returns or sets  the width of the label(text) like Regular, Bold.  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelWidth`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelWidth`` 
    
    :param labelWidth: 
    :type labelWidth: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LabelsToSkip: str = ...
    """
    Returns or sets  the characters to skip in label(text).  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelsToSkip`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelsToSkip`` 
    
    :param labelsToSkip: 
    :type labelsToSkip: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    MarkingHeight: float = ...
    """
    Returns or sets  the height of the marking.  
    
    <hr>
    
    Getter Method
    
    Signature ``MarkingHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MarkingHeight`` 
    
    :param markingHeight: 
    :type markingHeight: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    MarkingLineColorWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color and width of marking line.  
    
    <hr>
    
    Getter Method
    
    Signature ``MarkingLineColorWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Origin: ZoneOrigin = ...
    """
    Returns or sets  the type of zone origin like TopLeft/BottomRight.  
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.ZoneOrigin` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Diagramming.ZoneOrigin` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    VerticalSize: float = ...
    """
    Returns or sets  the size of the vertical zone.  
    
    It must be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``VerticalSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VerticalSize`` 
    
    :param verticalSize: 
    :type verticalSize: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SheetZoneSettingsBuilder = ...  # unknown typename


class PopulateTitleBlockBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Diagramming.PopulateTitleBlockBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.TitleBlockCollection.CreatePopulateTitleBlockBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    def GetCellValueForLabel(self, label: str) -> str:
        """
        Return the value of the cell for given label.  
        
        If multiple title blocks are input, 
        then the value of the cell from the first title block, which has the cell with given label, is returned.  
        
        Signature ``GetCellValueForLabel(label)`` 
        
        :param label:  Label whose value is queried  
        :type label: str 
        :returns:  Value of the label  
        :rtype: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetCellValueForLabel(self, label: str, value: str) -> None:
        """
        Sets the value of the cell for given label.  
        
        If multiple title blocks are selected, 
        then values of cells with the given label in all the title blocks are set. 
        
        Signature ``SetCellValueForLabel(label, value)`` 
        
        :param label:  Label whose value is to be set  
        :type label: str 
        :param value:  Value of the label  
        :type value: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetCell(self, table: NXOpen.Diagramming.Tables.Table, rowIndex: int, columnIndex: int) -> TitleBlockCellBuilder:
        """
        Get the cell builder.  
        
        Signature ``GetCell(table, rowIndex, columnIndex)`` 
        
        :param table: 
        :type table: :py:class:`NXOpen.Diagramming.Tables.Table` 
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.TitleBlockCellBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    Null: PopulateTitleBlockBuilder = ...  # unknown typename


class SheetBorderSettingsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The SheetBorderSettings builder   
    
    .. versionadded:: NX11.0.1
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
    
    ArrowAngle: float = ...
    """
    Returns or sets  the angle of arrow in the borders.  
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowAngle`` 
    
    :param arrowAngle: 
    :type arrowAngle: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ArrowDirection: ArrowDirectionType = ...
    """
    Returns or sets  the direction of arrow like Into Sheet or Out of Sheet.  
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.ArrowDirectionType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowDirection`` 
    
    :param arrowDirection: 
    :type arrowDirection: :py:class:`NXOpen.Diagramming.ArrowDirectionType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ArrowHeadTail: float = ...
    """
    Returns or sets  the length of arrow tail.  
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowHeadTail`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowHeadTail`` 
    
    :param arrowHeadTail: 
    :type arrowHeadTail: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ArrowLength: float = ...
    """
    Returns or sets  the length of arrow in the borders.  
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowLength`` 
    
    :param arrowLength: 
    :type arrowLength: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ArrowStyle: ArrowStyleType = ...
    """
    Returns or sets  the type of arrow style like Open, Closed.  
    
    .. 
    
    <hr>
    
    Getter Method
    
    Signature ``ArrowStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.ArrowStyleType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ArrowStyle`` 
    
    :param arrowStyle: 
    :type arrowStyle: :py:class:`NXOpen.Diagramming.ArrowStyleType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    BorderLineWidth: float = ...
    """
    Returns or sets  the width of border.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``BorderLineWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BorderLineWidth`` 
    
    :param borderLineWidth: 
    :type borderLineWidth: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CenteringMarkLength: float = ...
    """
    Returns or sets  the length of centering mark.  
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarkLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CenteringMarkLength`` 
    
    :param centeringMarkLength: 
    :type centeringMarkLength: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CenteringMarksColorWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color and width of centering marks.  
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarksColorWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CenteringMarksExtension: float = ...
    """
    Returns or sets  the length of centering marks extension from inner border.  
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarksExtension`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CenteringMarksExtension`` 
    
    :param centeringMarksExtension: 
    :type centeringMarksExtension: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CenteringMarksHorizontal: HorizontalCenteringMarkType = ...
    """
    Returns or sets  the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarksHorizontal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.HorizontalCenteringMarkType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CenteringMarksHorizontal`` 
    
    :param centeringMarksHorizontal: 
    :type centeringMarksHorizontal: :py:class:`NXOpen.Diagramming.HorizontalCenteringMarkType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CenteringMarksVertical: VerticalCenteringMarkType = ...
    """
    Returns or sets  the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarksVertical`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.VerticalCenteringMarkType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CenteringMarksVertical`` 
    
    :param centeringMarksVertical: 
    :type centeringMarksVertical: :py:class:`NXOpen.Diagramming.VerticalCenteringMarkType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateBorders: bool = ...
    """
    Returns or sets  the flag that indicates if borders are created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateBorders`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateBorders`` 
    
    :param createBorders: 
    :type createBorders: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    CreateTrimmingMarks: bool = ...
    """
    Returns or sets  the flag indicates to create trimming marks or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateTrimmingMarks`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateTrimmingMarks`` 
    
    :param createTrimmingMarks: 
    :type createTrimmingMarks: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DisplaySheetSizeInBorder: bool = ...
    """
    Returns or sets  the flag indicates to display sheet size in border or not 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySheetSizeInBorder`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySheetSizeInBorder`` 
    
    :param displaySheetSizeInBorder: 
    :type displaySheetSizeInBorder: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DistanceFromInnerBorder: float = ...
    """
    Returns or sets  the distance between inner border and arrow head.  
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromInnerBorder`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceFromInnerBorder`` 
    
    :param distanceInFromInnerBorder: 
    :type distanceInFromInnerBorder: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    InnerLineCFW: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font and width of inner border line.  
    
    <hr>
    
    Getter Method
    
    Signature ``InnerLineCFW`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Method: Method = ...
    """
    Returns or sets  the type of method to display like Standard/Custom 
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Method` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Diagramming.Method` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    OuterLineCFW: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font and width of outer border line.  
    
    <hr>
    
    Getter Method
    
    Signature ``OuterLineCFW`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TrimmingMarkColor: NXOpen.NXColor = ...
    """
    Returns or sets  the color of trimming mark.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkColor`` 
    
    :param trimmingMarkColor: 
    :type trimmingMarkColor: Id 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TrimmingMarkLength: float = ...
    """
    Returns or sets  the length of trimming mark.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkLength`` 
    
    :param trimmingMarkLength: 
    :type trimmingMarkLength: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TrimmingMarkStyle: TrimmingMarkStyleType = ...
    """
    Returns or sets  the type of trimming mark style like Corner or Triangle.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.TrimmingMarkStyleType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkStyle`` 
    
    :param trimmingMarkStyle: 
    :type trimmingMarkStyle: :py:class:`NXOpen.Diagramming.TrimmingMarkStyleType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TrimmingMarkWidth: float = ...
    """
    Returns or sets  the width of trimming mark.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkWidth`` 
    
    :param trimmingMarkWidth: 
    :type trimmingMarkWidth: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: SheetBorderSettingsBuilder = ...  # unknown typename


class NodeBuilder(ConnectableElementBuilder):
    """
    Represents a NodeBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.NodeCollection.CreateNodeBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def AddGroupMember(self, member: SheetElement) -> None:
        """
        Adds a node to this node group.  
        
        Signature ``AddGroupMember(member)`` 
        
        :param member: 
        :type member: :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveGroupMember(self, member: SheetElement) -> None:
        """
        Removes a node from this node group.  
        
        Signature ``RemoveGroupMember(member)`` 
        
        :param member: 
        :type member: :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllGroupMembers(self) -> None:
        """
        Remove all members.  
        
        Signature ``RemoveAllGroupMembers()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Expanded: bool = ...
    """
    Returns or sets  the node state of expanded or collapsed.  
    
    If true the node is expanded. 
    
    <hr>
    
    Getter Method
    
    Signature ``Expanded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Expanded`` 
    
    :param expanded: 
    :type expanded: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Fullfillment: bool = ...
    """
    Returns  the flag that indicates if the node is a fulfillment object.  
    
    If true the node represents a physical object such as a piece of equipment from a library. 
    
    <hr>
    
    Getter Method
    
    Signature ``Fullfillment`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    GroupingAllowed: bool = ...
    """
    Returns or sets  the flag that indicates if the node is allowed to be a nested node and contain other child sheet elements.  
    
    <hr>
    
    Getter Method
    
    Signature ``GroupingAllowed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GroupingAllowed`` 
    
    :param isGroupingAllowed: 
    :type isGroupingAllowed: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OffsheetReference: Node = ...
    """
    Returns or sets  the referenced offsheet node.  
    
    It could be elsewhere on the same sheet or on a different sheet and it can be None. 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsheetReference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Node` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OffsheetReference`` 
    
    :param offsheetReference: 
    :type offsheetReference: :py:class:`NXOpen.Diagramming.Node` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: NodeBuilder = ...  # unknown typename


class FormattedStringBuilder(BaseSubObjectBuilder):
    """
    Represents a FormattedStringBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    @typing.overload
    def SetFormatValue(self, objTags: 'list[NXOpen.NXObject]', attrTitles: 'list[str]', format: str) -> None:
        """
        Sets the format and related referenced attributes to this builder.
        
        Signature ``SetFormatValue(objTags, attrTitles, format)`` 
        
        :param objTags:  The owners of the referenced attributes  
        :type objTags: list of :py:class:`NXOpen.NXObject` 
        :param attrTitles:  The titles of the referenced attributes  
        :type attrTitles: list of str 
        :param format: 
        :type format: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetFormatValue(self, objTags: 'list[NXOpen.NXObject]', parentTags: 'list[NXOpen.NXObject]', attrTitles: 'list[str]', format: str) -> None:
        """
        Sets the format and related referenced attributes to this builder in managed mode.
        
        Signature ``SetFormatValue(objTags, parentTags, attrTitles, format)`` 
        
        :param objTags:  The owners of the referenced attributes  
        :type objTags: list of :py:class:`NXOpen.NXObject` 
        :param parentTags:  The owner parents of the referenced attributes  
        :type parentTags: list of :py:class:`NXOpen.NXObject` 
        :param attrTitles:  The titles of the referenced attributes  
        :type attrTitles: list of str 
        :param format: 
        :type format: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def AppendFormat(self, objTags: 'list[NXOpen.NXObject]', attrTitles: 'list[str]', appendFormat: str) -> None:
        """
        Appends the format and related referenced attributes to this builder.  
        
        Signature ``AppendFormat(objTags, attrTitles, appendFormat)`` 
        
        :param objTags:  The owners of the referenced attributes  
        :type objTags: list of :py:class:`NXOpen.NXObject` 
        :param attrTitles:  The titles of the referenced attributes  
        :type attrTitles: list of str 
        :param appendFormat: 
        :type appendFormat: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearFormat(self) -> None:
        """
        Clears the format and related referenced attributes of this builder.  
        
        Signature ``ClearFormat()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetReferencedAttributes(self) -> tuple:
        """
        Gets the referenced attributes.  
        
        Signature ``GetReferencedAttributes()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (attrTitles, objTags). attrTitles is a list of str.   The titles of the referenced attributes objTags is a list of :py:class:`NXOpen.NXObject`.   The owners of the referenced attributes 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Format: str = ...
    """
    Returns  the format.  
    
    <hr>
    
    Getter Method
    
    Signature ``Format`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    String: str = ...
    """
    Returns  the string.  
    
    <hr>
    
    Getter Method
    
    Signature ``String`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: FormattedStringBuilder = ...  # unknown typename


class NodeCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Node.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateNodeBuilder(self, node: Node) -> NodeBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.NodeBuilder`.  
        
        Signature ``CreateNodeBuilder(node)`` 
        
        :param node:  :py:class:`NXOpen.Diagramming.Node` to be edited, if None then create a new one  
        :type node: :py:class:`NXOpen.Diagramming.Node` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.NodeBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Node:
        """
        Finds the :py:class:`NXOpen.Diagramming.Node` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Node` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Node` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class DiagrammingAnnotationboundarytypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingAnnotationboundarytype():
    """
    Represents the boundary type of annotation.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Boundary Type"
       "Circle", "Circle Type"
       "Ellipse", "Ellipse Type"
       "Rectangle", "Rectangle Type"
       "RoundedRectangle", "Rounded Rectangle Type"
    """
    NotSet = 0  # DiagrammingAnnotationboundarytypeMemberType
    Circle = 1  # DiagrammingAnnotationboundarytypeMemberType
    Ellipse = 2  # DiagrammingAnnotationboundarytypeMemberType
    Rectangle = 3  # DiagrammingAnnotationboundarytypeMemberType
    RoundedRectangle = 4  # DiagrammingAnnotationboundarytypeMemberType
    
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
    


class LeaderLineCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of leader line.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateLeaderLineBuilder(self, leaderLine: LeaderLine) -> LeaderLineBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.LeaderLineBuilder`.  
        
        Signature ``CreateLeaderLineBuilder(leaderLine)`` 
        
        :param leaderLine:  :py:class:`NXOpen.Diagramming.LeaderLine` to be edited, if None then create a new one  
        :type leaderLine: :py:class:`NXOpen.Diagramming.LeaderLine` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> LeaderLine:
        """
        Finds the :py:class:`NXOpen.Diagramming.LeaderLine` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.LeaderLine` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.LeaderLine` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class DiagrammingRepeatstartpositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingRepeatstartposition():
    """
    Represents the repeat start position.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Center", "Center"
       "Start", "Start"
       "End", "End"
    """
    Center = 0  # DiagrammingRepeatstartpositionMemberType
    Start = 1  # DiagrammingRepeatstartpositionMemberType
    End = 2  # DiagrammingRepeatstartpositionMemberType
    
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
    


class MethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Method():
    """
    the zone method
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "To support legacy parts"
       "Standard", "Standard"
       "Custom", " - "
    """
    NotSet = 0  # MethodMemberType
    Standard = 1  # MethodMemberType
    Custom = 2  # MethodMemberType
    
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
    


class ArrowStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ArrowStyleType():
    """
    the arrow style type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Filled", "Filled"
       "Closed", "Closed"
       "ClosedSolid", "Close Solid"
       "Open", " - "
    """
    Filled = 0  # ArrowStyleTypeMemberType
    Closed = 1  # ArrowStyleTypeMemberType
    ClosedSolid = 2  # ArrowStyleTypeMemberType
    Open = 3  # ArrowStyleTypeMemberType
    
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
    


class GroupBuilder(SheetElementBuilder):
    """
    Represents a GroupBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.GroupCollection.CreateGroupBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetMember(self, memberSid: str) -> SheetElement:
        """
        Get the member by given member identifier SID.  
        
        Signature ``GetMember(memberSid)`` 
        
        :param memberSid: 
        :type memberSid: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMembers(self) -> 'list[SheetElement]':
        """
        Get all members.  
        
        Signature ``GetMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddMember(self, sheetElement: SheetElement) -> None:
        """
        Add a member.  
        
        Signature ``AddMember(sheetElement)`` 
        
        :param sheetElement: 
        :type sheetElement: :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveMember(self, member: SheetElement) -> None:
        """
        Remove a member.  
        
        Signature ``RemoveMember(member)`` 
        
        :param member: 
        :type member: :py:class:`NXOpen.Diagramming.SheetElement` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllMembers(self) -> None:
        """
        Remove all members.  
        
        Signature ``RemoveAllMembers()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: GroupBuilder = ...  # unknown typename


class RenderingPropertiesBuilder(BaseSubObjectBuilder):
    """
    Represents a RenderingPropertiesBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    FillColor: NXOpen.NXColor = ...
    """
    Returns or sets  the fill color.  
    
    <hr>
    
    Getter Method
    
    Signature ``FillColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillColor`` 
    
    :param colorId: 
    :type colorId: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FillOpacity: float = ...
    """
    Returns or sets  the fill opacity.  
    
    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
    
    <hr>
    
    Getter Method
    
    Signature ``FillOpacity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillOpacity`` 
    
    :param opacity: 
    :type opacity: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LineFont: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the line font.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineFont`` 
    
    :param font: 
    :type font: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LineWidth: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the line width.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineWidth`` 
    
    :param width: 
    :type width: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    StrokeColor: NXOpen.NXColor = ...
    """
    Returns or sets  the stroke color.  
    
    <hr>
    
    Getter Method
    
    Signature ``StrokeColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StrokeColor`` 
    
    :param colorId: 
    :type colorId: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    StrokeOpacity: float = ...
    """
    Returns or sets  the stroke opacity.  
    
    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
    
    <hr>
    
    Getter Method
    
    Signature ``StrokeOpacity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StrokeOpacity`` 
    
    :param opacity: 
    :type opacity: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: RenderingPropertiesBuilder = ...  # unknown typename


class SheetBordersAndZonesCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Diagramming.SheetBordersAndZones` objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> SheetBordersAndZones:
        """
        Finds the :py:class:`NXOpen.Diagramming.SheetBordersAndZones` with the given name.  
        
        An exception will be thrown if no object can be found with the given name.  
        
        Signature ``FindObject(name)`` 
        
        :param name:  Drawing sheet name  
        :type name: str 
        :returns:   Borders and zones object  
        :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZones` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSheetBordersAndZonesBuilder(self, bordersAndZones: SheetBordersAndZones) -> SheetBordersAndZonesBuilder:
        """
        Creates a borders and zones builder  
        
        Signature ``CreateSheetBordersAndZonesBuilder(bordersAndZones)`` 
        
        :param bordersAndZones:  :py:class:`NXOpen.Diagramming.SheetBordersAndZones` to be redefined, if None then creates a new one  
        :type bordersAndZones: :py:class:`NXOpen.Diagramming.SheetBordersAndZones` 
        :returns:  SheetBordersAndZonesBuilder object  
        :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: drafting ("DRAFTING")
        """
        ...
    


class VerticalCenteringMarkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class VerticalCenteringMarkType():
    """
    the vertical centering mark type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "BottomArrow", "Bottom Arrow"
       "TopArrow", "Top Arrow"
       "BottomandTopArrow", "Bottom and Top Arrow"
       "BottomandTopLine", " - "
    """
    NotSet = 0  # VerticalCenteringMarkTypeMemberType
    BottomArrow = 1  # VerticalCenteringMarkTypeMemberType
    TopArrow = 2  # VerticalCenteringMarkTypeMemberType
    BottomandTopArrow = 3  # VerticalCenteringMarkTypeMemberType
    BottomandTopLine = 4  # VerticalCenteringMarkTypeMemberType
    
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
    


class DiagrammingConnectionlabelhorizontaloffsetpositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingConnectionlabelhorizontaloffsetposition():
    """
    Represents the horizontal connection label offset position.   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Above", "Above"
       "Below", "Below"
    """
    Above = 0  # DiagrammingConnectionlabelhorizontaloffsetpositionMemberType
    Below = 1  # DiagrammingConnectionlabelhorizontaloffsetpositionMemberType
    
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
    


class TitleBlockCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Title Block.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX11.0.1
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateDefineTitleBlockBuilder(self, titleBlock: TitleBlock) -> DefineTitleBlockBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.DefineTitleBlockBuilder`.  
        
        Signature ``CreateDefineTitleBlockBuilder(titleBlock)`` 
        
        :param titleBlock:  :py:class:`NXOpen.Diagramming.TitleBlock` to be edited, if None then create a new one  
        :type titleBlock: :py:class:`NXOpen.Diagramming.TitleBlock` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.DefineTitleBlockBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreatePopulateTitleBlockBuilder(self, titleBlocks: 'list[TitleBlock]') -> PopulateTitleBlockBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.PopulateTitleBlockBuilder`.  
        
        Signature ``CreatePopulateTitleBlockBuilder(titleBlocks)`` 
        
        :param titleBlocks: 
        :type titleBlocks: list of :py:class:`NXOpen.Diagramming.TitleBlock` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.PopulateTitleBlockBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> TitleBlock:
        """
        Finds the :py:class:`NXOpen.Diagramming.TitleBlock` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.TitleBlock` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.TitleBlock` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class CannedAnnotationBuilderInheritOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CannedAnnotationBuilderInheritOption():
    """
    Represents the inherit option.
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Preferences", "Setting the inherit from preferences option"
       "CustomerDefaults", "Setting the inherit from customer defaults option"
       "Selection", "Setting the inherit from selection option"
    """
    Preferences = 0  # CannedAnnotationBuilderInheritOptionMemberType
    CustomerDefaults = 1  # CannedAnnotationBuilderInheritOptionMemberType
    Selection = 2  # CannedAnnotationBuilderInheritOptionMemberType
    
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
    


class CannedAnnotationBuilder(NXOpen.Builder):
    """
    Represents a CannedAnnotationBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.DiagrammingManager.CreateCannedAnnotationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class InheritOption():
        """
        Represents the inherit option.
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Preferences", "Setting the inherit from preferences option"
           "CustomerDefaults", "Setting the inherit from customer defaults option"
           "Selection", "Setting the inherit from selection option"
        """
        Preferences = 0  # CannedAnnotationBuilderInheritOptionMemberType
        CustomerDefaults = 1  # CannedAnnotationBuilderInheritOptionMemberType
        Selection = 2  # CannedAnnotationBuilderInheritOptionMemberType
        
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
        
    
    
    def CreateLeaderLine(self) -> LeaderLineBuilder:
        """
        Create a new :py:class:`NXOpen.Diagramming.LeaderLineBuilder` builder.  
        
        Signature ``CreateLeaderLine()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.LeaderLineBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Inherit(self, inheritOption: CannedAnnotationBuilderInheritOption, annotation: Annotation) -> None:
        """
        Inherit.  
        
        Signature ``Inherit(inheritOption, annotation)`` 
        
        :param inheritOption: 
        :type inheritOption: :py:class:`NXOpen.Diagramming.CannedAnnotationBuilderInheritOption` 
        :param annotation: 
        :type annotation: :py:class:`NXOpen.Diagramming.Annotation` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    AnnotationBuilder: AnnotationBuilder = ...
    """
    Returns  the annotation of this canned annotation.  
    
    <hr>
    
    Getter Method
    
    Signature ``AnnotationBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.AnnotationBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LeaderLines: LeaderLineBuilderList = ...
    """
    Returns  the list of the leader lines.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeaderLines`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.LeaderLineBuilderList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TextBoxIndent: int = ...
    """
    Returns or sets  the indent value of the text box in the canned annotation.  
    
    <hr>
    
    Getter Method
    
    Signature ``TextBoxIndent`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextBoxIndent`` 
    
    :param indent: 
    :type indent: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TextBoxModifiable: bool = ...
    """
    Returns or sets  the flag that indicates if the text box in the canned annotation is modifiable.  
    
    <hr>
    
    Getter Method
    
    Signature ``TextBoxModifiable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextBoxModifiable`` 
    
    :param isModifiable: 
    :type isModifiable: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TextBoxShadowBox: bool = ...
    """
    Returns or sets  the flag that indicates if the text box in the canned annotation has shadow box.  
    
    <hr>
    
    Getter Method
    
    Signature ``TextBoxShadowBox`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextBoxShadowBox`` 
    
    :param isShadowBox: 
    :type isShadowBox: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CannedAnnotationBuilder = ...  # unknown typename


class SheetBordersAndZones(NXOpen.NXObject):
    """
    Represents Sheet Borders and Zones  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: SheetBordersAndZones = ...  # unknown typename


class Node(ConnectableElement):
    """
    Represents the Node class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.NodeBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPorts(self) -> 'list[Port]':
        """
        Get the ports on the node.  
        
        Signature ``GetPorts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Port` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    Null: Node = ...  # unknown typename


class TextStyleBuilderTextAlignmentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextStyleBuilderTextAlignmentType():
    """
    Represents the option :py:meth:`NXOpen.Diagramming.TextStyleBuilder.TextAlignment`
    for a :py:class:`NXOpen.Diagramming.TextStyleBuilder`.
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", " - "
       "Center", " - "
       "Right", " - "
    """
    Left = 0  # TextStyleBuilderTextAlignmentTypeMemberType
    Center = 1  # TextStyleBuilderTextAlignmentTypeMemberType
    Right = 2  # TextStyleBuilderTextAlignmentTypeMemberType
    
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
    


class TextStyleBuilderTextAutoFitTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TextStyleBuilderTextAutoFitType():
    """
    Represents the option 
    for a :py:class:`NXOpen.Diagramming.TextStyleBuilder`.
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "ResizeOutline", " - "
       "ShrinkText", " - "
    """
    NotSet = 0  # TextStyleBuilderTextAutoFitTypeMemberType
    ResizeOutline = 1  # TextStyleBuilderTextAutoFitTypeMemberType
    ShrinkText = 2  # TextStyleBuilderTextAutoFitTypeMemberType
    
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
    


class TextStyleBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a TextStyleBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX11.0.0
    """
    
    class TextAlignmentType():
        """
        Represents the option :py:meth:`NXOpen.Diagramming.TextStyleBuilder.TextAlignment`
        for a :py:class:`NXOpen.Diagramming.TextStyleBuilder`.
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", " - "
           "Center", " - "
           "Right", " - "
        """
        Left = 0  # TextStyleBuilderTextAlignmentTypeMemberType
        Center = 1  # TextStyleBuilderTextAlignmentTypeMemberType
        Right = 2  # TextStyleBuilderTextAlignmentTypeMemberType
        
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
        
    
    
    class TextAutoFitType():
        """
        Represents the option 
        for a :py:class:`NXOpen.Diagramming.TextStyleBuilder`.
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "ResizeOutline", " - "
           "ShrinkText", " - "
        """
        NotSet = 0  # TextStyleBuilderTextAutoFitTypeMemberType
        ResizeOutline = 1  # TextStyleBuilderTextAutoFitTypeMemberType
        ShrinkText = 2  # TextStyleBuilderTextAutoFitTypeMemberType
        
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
    
    TextAlignment: TextStyleBuilderTextAlignmentType = ...
    """
    Returns or sets  the text alignment of the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``TextAlignment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.TextStyleBuilderTextAlignmentType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextAlignment`` 
    
    :param alignment: 
    :type alignment: :py:class:`NXOpen.Diagramming.TextStyleBuilderTextAlignmentType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextAllowWrapping: bool = ...
    """
    Returns or sets  the text allow wrapping 
    
    <hr>
    
    Getter Method
    
    Signature ``TextAllowWrapping`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextAllowWrapping`` 
    
    :param allowWrapping: 
    :type allowWrapping: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextAutoFit: TextStyleBuilderTextAutoFitType = ...
    """
    Returns or sets  the text auto fit 
    
    <hr>
    
    Getter Method
    
    Signature ``TextAutoFit`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.TextStyleBuilderTextAutoFitType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextAutoFit`` 
    
    :param autoFit: 
    :type autoFit: :py:class:`NXOpen.Diagramming.TextStyleBuilderTextAutoFitType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextColorFontWidth: NXOpen.TextColorFontWidthBuilder = ...
    """
    Returns  the text color font width 
    
    <hr>
    
    Getter Method
    
    Signature ``TextColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TextColorFontWidthBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextHeight: float = ...
    """
    Returns or sets  the height of the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``TextHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextHeight`` 
    
    :param height: 
    :type height: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextOverlined: bool = ...
    """
    Returns or sets  whether the text is overlined 
    
    <hr>
    
    Getter Method
    
    Signature ``TextOverlined`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextOverlined`` 
    
    :param overlined: 
    :type overlined: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    TextUnderlined: bool = ...
    """
    Returns or sets  whether the text is underlined 
    
    <hr>
    
    Getter Method
    
    Signature ``TextUnderlined`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TextUnderlined`` 
    
    :param underlined: 
    :type underlined: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: TextStyleBuilder = ...  # unknown typename


class TrimmingMarkStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TrimmingMarkStyleType():
    """
    the trimming mark style type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Triangle", "Triangle"
       "Corner", " - "
    """
    Triangle = 0  # TrimmingMarkStyleTypeMemberType
    Corner = 1  # TrimmingMarkStyleTypeMemberType
    
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
    


class PortCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Port.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreatePortBuilder(self, port: Port) -> PortBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.PortBuilder`.  
        
        Signature ``CreatePortBuilder(port)`` 
        
        :param port:  :py:class:`NXOpen.Diagramming.Port` to be edited, if None then create a new one  
        :type port: :py:class:`NXOpen.Diagramming.Port` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.PortBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Port:
        """
        Finds the :py:class:`NXOpen.Diagramming.Port` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Port` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Port` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderHorizontalCenteringMarkType():
    """
    Represents the horizontal centering mark type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "LeftArrow", "Left Arrow"
       "RightArrow", "Right Arrow"
       "LeftandRightArrow", "Left and Right Arrow"
       "LeftandRightLine", " - "
    """
    NotSet = 0  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
    LeftArrow = 1  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
    RightArrow = 2  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
    LeftandRightArrow = 3  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
    LeftandRightLine = 4  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
    
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
    


class SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderVerticalCenteringMarkType():
    """
    Represents the vertical centering mark type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "BottomArrow", "Bottom Arrow"
       "TopArrow", "Top Arrow"
       "BottomandTopArrow", "Bottom and Top Arrow"
       "BottomandTopLine", " - "
    """
    NotSet = 0  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
    BottomArrow = 1  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
    TopArrow = 2  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
    BottomandTopArrow = 3  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
    BottomandTopLine = 4  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
    
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
    


class SheetBordersAndZonesBuilderZoneMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderZoneMethod():
    """
    Represents the zone method. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Standard", "Standard"
       "Custom", " - "
    """
    NotSet = 0  # SheetBordersAndZonesBuilderZoneMethodMemberType
    Standard = 1  # SheetBordersAndZonesBuilderZoneMethodMemberType
    Custom = 2  # SheetBordersAndZonesBuilderZoneMethodMemberType
    
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
    


class SheetBordersAndZonesBuilderZoneOriginMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderZoneOrigin():
    """
    Represents the zone origin. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BottomRight", "Bottom Right"
       "TopLeft", "Top Left"
       "TopRight", "Top Right"
       "BottomLeft", " - "
    """
    BottomRight = 0  # SheetBordersAndZonesBuilderZoneOriginMemberType
    TopLeft = 1  # SheetBordersAndZonesBuilderZoneOriginMemberType
    TopRight = 2  # SheetBordersAndZonesBuilderZoneOriginMemberType
    BottomLeft = 3  # SheetBordersAndZonesBuilderZoneOriginMemberType
    
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
    


class SheetBordersAndZonesBuilderArrowStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderArrowStyleType():
    """
    Represents the arrow style type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Filled", "Filled"
       "Closed", "Closed"
       "ClosedSolid", "Close Solid"
       "Open", " - "
    """
    Filled = 0  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
    Closed = 1  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
    ClosedSolid = 2  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
    Open = 3  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
    
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
    


class SheetBordersAndZonesBuilderArrowDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderArrowDirectionType():
    """
    Represents the arrow direction type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OutofSheet", "Out of Sheet"
       "IntoSheet", " - "
    """
    OutofSheet = 0  # SheetBordersAndZonesBuilderArrowDirectionTypeMemberType
    IntoSheet = 1  # SheetBordersAndZonesBuilderArrowDirectionTypeMemberType
    
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
    


class SheetBordersAndZonesBuilderTrimmingMarkStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetBordersAndZonesBuilderTrimmingMarkStyleType():
    """
    Represents the trimming mark style type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Triangle", "Triangle"
       "Corner", " - "
    """
    Triangle = 0  # SheetBordersAndZonesBuilderTrimmingMarkStyleTypeMemberType
    Corner = 1  # SheetBordersAndZonesBuilderTrimmingMarkStyleTypeMemberType
    
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
    


class SheetBordersAndZonesBuilder(NXOpen.Builder):
    """
    The SheetBordersAndZones builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.SheetBordersAndZonesCollection.CreateSheetBordersAndZonesBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class HorizontalCenteringMarkType():
        """
        Represents the horizontal centering mark type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "LeftArrow", "Left Arrow"
           "RightArrow", "Right Arrow"
           "LeftandRightArrow", "Left and Right Arrow"
           "LeftandRightLine", " - "
        """
        NotSet = 0  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
        LeftArrow = 1  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
        RightArrow = 2  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
        LeftandRightArrow = 3  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
        LeftandRightLine = 4  # SheetBordersAndZonesBuilderHorizontalCenteringMarkTypeMemberType
        
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
        
    
    
    class VerticalCenteringMarkType():
        """
        Represents the vertical centering mark type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "BottomArrow", "Bottom Arrow"
           "TopArrow", "Top Arrow"
           "BottomandTopArrow", "Bottom and Top Arrow"
           "BottomandTopLine", " - "
        """
        NotSet = 0  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
        BottomArrow = 1  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
        TopArrow = 2  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
        BottomandTopArrow = 3  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
        BottomandTopLine = 4  # SheetBordersAndZonesBuilderVerticalCenteringMarkTypeMemberType
        
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
        
    
    
    class ZoneMethod():
        """
        Represents the zone method. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "Standard", "Standard"
           "Custom", " - "
        """
        NotSet = 0  # SheetBordersAndZonesBuilderZoneMethodMemberType
        Standard = 1  # SheetBordersAndZonesBuilderZoneMethodMemberType
        Custom = 2  # SheetBordersAndZonesBuilderZoneMethodMemberType
        
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
        
    
    
    class ZoneOrigin():
        """
        Represents the zone origin. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BottomRight", "Bottom Right"
           "TopLeft", "Top Left"
           "TopRight", "Top Right"
           "BottomLeft", " - "
        """
        BottomRight = 0  # SheetBordersAndZonesBuilderZoneOriginMemberType
        TopLeft = 1  # SheetBordersAndZonesBuilderZoneOriginMemberType
        TopRight = 2  # SheetBordersAndZonesBuilderZoneOriginMemberType
        BottomLeft = 3  # SheetBordersAndZonesBuilderZoneOriginMemberType
        
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
        
    
    
    class ArrowStyleType():
        """
        Represents the arrow style type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Filled", "Filled"
           "Closed", "Closed"
           "ClosedSolid", "Close Solid"
           "Open", " - "
        """
        Filled = 0  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
        Closed = 1  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
        ClosedSolid = 2  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
        Open = 3  # SheetBordersAndZonesBuilderArrowStyleTypeMemberType
        
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
        
    
    
    class ArrowDirectionType():
        """
        Represents the arrow direction type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OutofSheet", "Out of Sheet"
           "IntoSheet", " - "
        """
        OutofSheet = 0  # SheetBordersAndZonesBuilderArrowDirectionTypeMemberType
        IntoSheet = 1  # SheetBordersAndZonesBuilderArrowDirectionTypeMemberType
        
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
        
    
    
    class TrimmingMarkStyleType():
        """
        Represents the trimming mark style type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Triangle", "Triangle"
           "Corner", " - "
        """
        Triangle = 0  # SheetBordersAndZonesBuilderTrimmingMarkStyleTypeMemberType
        Corner = 1  # SheetBordersAndZonesBuilderTrimmingMarkStyleTypeMemberType
        
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
        
    
    
    def SetOwningSheet(self, owningSheet: Sheet) -> None:
        """
        Set the owning sheet when the sheet element is created.  
        
        It is not allowed to change the owning sheet when editing the borders and zones. 
        
        Signature ``SetOwningSheet(owningSheet)`` 
        
        :param owningSheet: 
        :type owningSheet: :py:class:`NXOpen.Diagramming.Sheet` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    BottomMargin: float = ...
    """
    Returns or sets  the value of the margin in bottom border.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BottomMargin`` 
    
    :param bottomMargin: 
    :type bottomMargin: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CenteringMarkExtension: float = ...
    """
    Returns or sets  the length of centering marks extension from inner border 
    
    <hr>
    
    Getter Method
    
    Signature ``CenteringMarkExtension`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CenteringMarkExtension`` 
    
    :param centeringMarkExtension: 
    :type centeringMarkExtension: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CreateBorders: bool = ...
    """
    Returns or sets  the flag that indicates if borders are created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateBorders`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateBorders`` 
    
    :param createBorders: 
    :type createBorders: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CreateTrimmingMarks: bool = ...
    """
    Returns or sets  the flag that indicate if trimming marks are created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateTrimmingMarks`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateTrimmingMarks`` 
    
    :param createTrimmingMarks: 
    :type createTrimmingMarks: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CreateZoneLabels: bool = ...
    """
    Returns or sets  the flag that indicates if zone labels are created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateZoneLabels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateZoneLabels`` 
    
    :param createZoneLabels: 
    :type createZoneLabels: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CreateZoneMarking: bool = ...
    """
    Returns or sets  the flag that indicates if zone marking is create.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateZoneMarking`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateZoneMarking`` 
    
    :param createZoneMarking: 
    :type createZoneMarking: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    HorizontalCenteringMark: SheetBordersAndZonesBuilderHorizontalCenteringMarkType = ...
    """
    Returns or sets  the horizontal centering mark used to show the type of centering mark like LeftArrow/RightArrow.  
    
    <hr>
    
    Getter Method
    
    Signature ``HorizontalCenteringMark`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderHorizontalCenteringMarkType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HorizontalCenteringMark`` 
    
    :param horizontalCenteringMarkType: 
    :type horizontalCenteringMarkType: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderHorizontalCenteringMarkType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    HorizontalSize: float = ...
    """
    Returns or sets  the size of horizontal zones.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``HorizontalSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HorizontalSize`` 
    
    :param horizontalSize: 
    :type horizontalSize: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LabelFont: int = ...
    """
    Returns or sets  the font of the label(text).  
    
    <hr>
    
    Getter Method
    
    Signature ``LabelFont`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelFont`` 
    
    :param labelFont: 
    :type labelFont: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LabelHeight: float = ...
    """
    Returns or sets  the height of the label(text).  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``LabelHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LabelHeight`` 
    
    :param labelHeight: 
    :type labelHeight: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LeftMargin: float = ...
    """
    Returns or sets  the value of the margin in left border.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeftMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LeftMargin`` 
    
    :param leftMargin: 
    :type leftMargin: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MarkingHeight: float = ...
    """
    Returns or sets  the height of marking.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``MarkingHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MarkingHeight`` 
    
    :param markingHeight: 
    :type markingHeight: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Method: SheetBordersAndZonesBuilderZoneMethod = ...
    """
    Returns or sets  the type of methods to create the zones.  
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Origin: SheetBordersAndZonesBuilderZoneOrigin = ...
    """
    Returns or sets  the type of zone origin like TopLeft/BottomRight.  
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneOrigin` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderZoneOrigin` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    RightMargin: float = ...
    """
    Returns or sets  the value of the margin in right border.  
    
    <hr>
    
    Getter Method
    
    Signature ``RightMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RightMargin`` 
    
    :param rightMargin: 
    :type rightMargin: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SheetBorderSettings: SheetBorderSettingsBuilder = ...
    """
    Returns  the sheet border settings builder used to get the values related to borders
    
    <hr>
    
    Getter Method
    
    Signature ``SheetBorderSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBorderSettingsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    SheetMarginSettings: SheetMarginSettingsBuilder = ...
    """
    Returns  the sheet margin settings builder used to get the values related to margins
    
    <hr>
    
    Getter Method
    
    Signature ``SheetMarginSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetMarginSettingsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    SheetZoneSettings: SheetZoneSettingsBuilder = ...
    """
    Returns  the sheet zone settings builder used to get the values related to zones
    
    <hr>
    
    Getter Method
    
    Signature ``SheetZoneSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetZoneSettingsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TopMargin: float = ...
    """
    Returns or sets  the value of the margin in top border.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopMargin`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TopMargin`` 
    
    :param topMargin: 
    :type topMargin: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TrimmingMarkLength: float = ...
    """
    Returns or sets  the length of trimming mark.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkLength`` 
    
    :param trimmingMarkLength: 
    :type trimmingMarkLength: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TrimmingMarkThickness: float = ...
    """
    Returns or sets  the width of trimming mark.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``TrimmingMarkThickness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimmingMarkThickness`` 
    
    :param trimmingMarkThickness: 
    :type trimmingMarkThickness: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    VerticalCenteringMark: SheetBordersAndZonesBuilderVerticalCenteringMarkType = ...
    """
    Returns or sets  the vertical centering mark  used to show the type of centering mark like TopArrow/BottomArrow.  
    
    <hr>
    
    Getter Method
    
    Signature ``VerticalCenteringMark`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderVerticalCenteringMarkType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VerticalCenteringMark`` 
    
    :param verticalCenteringMark: 
    :type verticalCenteringMark: :py:class:`NXOpen.Diagramming.SheetBordersAndZonesBuilderVerticalCenteringMarkType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    VerticalSize: float = ...
    """
    Returns or sets  the size of vertical zones.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``VerticalSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VerticalSize`` 
    
    :param verticalSize: 
    :type verticalSize: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Width: float = ...
    """
    Returns or sets  the width of border.  
    
    It should be greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SheetBordersAndZonesBuilder = ...  # unknown typename


class DiagrammingArrowtypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiagrammingArrowtype():
    """
    Represents the arrow type.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Setting the arrow type none arrow"
       "Open", "Setting the arrow type open arrow"
       "Filled", "Setting the arrow type filled arrow"
       "ClosedSolid", "Setting the arrow type closed solid arrow"
    """
    NotSet = 0  # DiagrammingArrowtypeMemberType
    Open = 1  # DiagrammingArrowtypeMemberType
    Filled = 2  # DiagrammingArrowtypeMemberType
    ClosedSolid = 3  # DiagrammingArrowtypeMemberType
    
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
    


class ShapeBuilder(SheetElementBuilder):
    """
    Represents a ShapeBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.ShapeCollection.CreateShapeBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: ShapeBuilder = ...  # unknown typename


class SheetManager():
    """
    A manager to deal with all objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX12.0.0
    """
    
    def OpenSheet(self, sheet: Sheet) -> None:
        """
        Opens a :py:class:`NXOpen.Diagramming.Sheet`.  
        
        Signature ``OpenSheet(sheet)`` 
        
        :param sheet: 
        :type sheet: :py:class:`NXOpen.Diagramming.Sheet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ActiveSheet: Sheet = ...
    """
    Returns or sets  the active sheet 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveSheet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Sheet` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveSheet`` 
    
    :param sheet: 
    :type sheet: :py:class:`NXOpen.Diagramming.Sheet` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """


class Sheet(BaseObject):
    """
    Represents the Sheet class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.SheetBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def LogGroupToDelete(self, group: Group) -> None:
        """
        Logs a group and all its members to delete.  
        
        Signature ``LogGroupToDelete(group)`` 
        
        :param group: 
        :type group: :py:class:`NXOpen.Diagramming.Group` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Sheet = ...  # unknown typename


class Annotation(ConnectableElement):
    """
    Represents the Annotation class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.AnnotationBuilder`
    
    .. versionadded:: NX10.0.0
    """
    Null: Annotation = ...  # unknown typename


