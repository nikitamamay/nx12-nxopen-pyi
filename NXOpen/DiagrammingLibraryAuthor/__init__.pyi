# module 'NXOpen.DiagrammingLibraryAuthor'
#
# Automatically generated 2025-06-09T14:38:45.464879
#
"""Default documentation for NXOpen.DiagrammingLibraryAuthor."""

import typing

import NXOpen
import NXOpen.Gateway
import NXOpen.GeometricUtilities
import NXOpen.Tooling



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PipeStockBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a PipeStockBuilder.  
    
    .. versionadded:: NX11.0.1
    """
    
    def SelectFolder(self, classId: str) -> None:
        """
        Selects the pipe stock folder by the class ID 
        
        Signature ``SelectFolder(classId)`` 
        
        :param classId: 
        :type classId: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SelectPipeStock(self, symbolId: str) -> None:
        """
        Selects one pipe stock by the symbol ID 
        
        Signature ``SelectPipeStock(symbolId)`` 
        
        :param symbolId: 
        :type symbolId: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetPipeStockObjects(self) -> 'list[AttributeHolder]':
        """
        Gets the pipe stock objects which have user attributes of the pipe stock.  
        
        Signature ``GetPipeStockObjects()`` 
        
        :returns:  the pipe stock objects  
        :rtype: list of :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreatePipeStock(self, instanceId: str, partId: str, partName: str, numberName: str) -> AttributeHolder:
        """
        Creates a new pipe stock  
        
        Signature ``CreatePipeStock(instanceId, partId, partName, numberName)`` 
        
        :param instanceId: 
        :type instanceId: str 
        :param partId: 
        :type partId: str 
        :param partName: 
        :type partName: str 
        :param numberName: 
        :type numberName: str 
        :returns:  the pipe stock object  
        :rtype: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def DeletePipeStock(self, pipeStockObject: AttributeHolder) -> None:
        """
        Deletes the pipe stock which is new created 
        
        Signature ``DeletePipeStock(pipeStockObject)`` 
        
        :param pipeStockObject:  the pipe stock object,                only accept the object which is got by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder.CreatePipeStock`  
        :type pipeStockObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
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
    
    Null: PipeStockBuilder = ...  # unknown typename


class PortDataBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a PortDataBuilder.  
    
    .. versionadded:: NX11.0.1
    """
    
    def GetPortObjects(self) -> 'list[AttributeHolder]':
        """
        Gets the port objects which have user attributes of the port.  
        
        Signature ``GetPortObjects()`` 
        
        :returns:  the port objects  
        :rtype: list of :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetPointLocation(self, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
        Gets the port location  
        
        Signature ``GetPointLocation(portObject)`` 
        
        :param portObject:  the port object,                only accept the object which is got by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.GetPortObjects` or :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.CreatePort`  
        :type portObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        :returns:  the port location  
        :rtype: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetPointLocation(self, portObject: AttributeHolder, portLocation: NXOpen.Point2d) -> None:
        """
        Sets the port location 
        
        Signature ``SetPointLocation(portObject, portLocation)`` 
        
        :param portObject:  the port object,                only accept the object which is by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.GetPortObjects` or :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.CreatePort`  
        :type portObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        :param portLocation:  the port location  
        :type portLocation: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetConnectionDirection(self, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
        Gets the connection direction  
        
        Signature ``GetConnectionDirection(portObject)`` 
        
        :param portObject:  the port object,                only accept the object which is got by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.GetPortObjects` or :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.CreatePort`  
        :type portObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        :returns:  the connection direction  
        :rtype: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetConnectionDirection(self, portObject: AttributeHolder, connectionDirection: NXOpen.Point2d) -> None:
        """
        Sets the connection direction  
        
        Signature ``SetConnectionDirection(portObject, connectionDirection)`` 
        
        :param portObject:  the port object,                only accept the object which is got by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.GetPortObjects` or :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.CreatePort`  
        :type portObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        :param connectionDirection:  the connection direction  
        :type connectionDirection: :py:class:`NXOpen.Point2d` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreatePort(self) -> AttributeHolder:
        """
        Creates a new port  
        
        Signature ``CreatePort()`` 
        
        :returns:  the port object  
        :rtype: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def DeletePort(self, portObject: AttributeHolder) -> None:
        """
        Deletes the port which is new created 
        
        Signature ``DeletePort(portObject)`` 
        
        :param portObject:  the port object,                only accept the object which is got by :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.CreatePort`  
        :type portObject: :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder` 
        
        .. versionadded:: NX11.0.1
        
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
    
    NozzleBottom: bool = ...
    """
    Returns or sets  the nozzle in the bottom edge.  
    
    <hr>
    
    Getter Method
    
    Signature ``NozzleBottom`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NozzleBottom`` 
    
    :param nozzleBottom: 
    :type nozzleBottom: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    NozzleLeft: bool = ...
    """
    Returns or sets  the nozzle in the left edge.  
    
    <hr>
    
    Getter Method
    
    Signature ``NozzleLeft`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NozzleLeft`` 
    
    :param nozzleLeft: 
    :type nozzleLeft: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    NozzleRight: bool = ...
    """
    Returns or sets  the nozzle in the right edge.  
    
    <hr>
    
    Getter Method
    
    Signature ``NozzleRight`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NozzleRight`` 
    
    :param nozzleRight: 
    :type nozzleRight: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    NozzleTop: bool = ...
    """
    Returns or sets  the nozzle in the top edge 
    
    <hr>
    
    Getter Method
    
    Signature ``NozzleTop`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NozzleTop`` 
    
    :param nozzleTop: 
    :type nozzleTop: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: PortDataBuilder = ...  # unknown typename


class AttributeHolder(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.DiagrammingLibraryAuthor.AttributeHolder`.  
    
    Use :py:meth:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder.GetPortObjects` or :py:meth:`NXOpen.DiagrammingLibraryAuthor.PipeStockBuilder.GetPipeStockObjects` to get the instance of this class.
    
    .. versionadded:: NX11.0.1
    """
    Null: AttributeHolder = ...  # unknown typename


class Symbol2DBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Symbol2DBuilder.  
    
    .. versionadded:: NX11.0.1
    """
    
    def CreateFromSymbol(self, symbolId: str) -> None:
        """
        Creates a new symbol from another symbol 
        
        Signature ``CreateFromSymbol(symbolId)`` 
        
        :param symbolId: 
        :type symbolId: str 
        
        .. versionadded:: NX11.0.1
        
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
    
    AnchorPoint: NXOpen.Point2d = ...
    """
    Returns or sets  the anchor point 
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point2d` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorPoint`` 
    
    :param anchorPoint: 
    :type anchorPoint: :py:class:`NXOpen.Point2d` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    DraftingSymbol: NXOpen.Tooling.SelectReuseLibraryItemBuilder = ...
    """
    Returns  the 2D symbol sub-builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``DraftingSymbol`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Tooling.SelectReuseLibraryItemBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    EnableScale: bool = ...
    """
    Returns or sets  the scaling 
    
    <hr>
    
    Getter Method
    
    Signature ``EnableScale`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnableScale`` 
    
    :param enableScale: 
    :type enableScale: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Image: NXOpen.Gateway.ImageCaptureBuilder = ...
    """
    Returns or sets  the image capture builder 
    
    <hr>
    
    Getter Method
    
    Signature ``Image`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Gateway.ImageCaptureBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Image`` 
    
    :param imageCaptureBuilder: 
    :type imageCaptureBuilder: :py:class:`NXOpen.Gateway.ImageCaptureBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    IsInline: bool = ...
    """
    Returns or sets  the inline 
    
    <hr>
    
    Getter Method
    
    Signature ``IsInline`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsInline`` 
    
    :param isInline: 
    :type isInline: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    PortData: PortDataBuilder = ...
    """
    Returns  the port data sub-builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``PortData`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DiagrammingLibraryAuthor.PortDataBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TagLocation: NXOpen.Point2d = ...
    """
    Returns or sets  the tag location 
    
    <hr>
    
    Getter Method
    
    Signature ``TagLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point2d` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TagLocation`` 
    
    :param tagLocation: 
    :type tagLocation: :py:class:`NXOpen.Point2d` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: Symbol2DBuilder = ...  # unknown typename


class LineTypeBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a LineTypeBuilder.  
    
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
    
    LineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the line color.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineColor`` 
    
    :param colorId: 
    :type colorId: Id 
    
    .. versionadded:: NX11.0.1
    
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
    LineTypeName: str = ...
    """
    Returns or sets  the name of the line type.  
    
    It should be unique. 
    
    <hr>
    
    Getter Method
    
    Signature ``LineTypeName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineTypeName`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LineTypePriority: int = ...
    """
    Returns or sets  the priority of the line type.  
    
    It should be greater than or equal to 0. 
    
    <hr>
    
    Getter Method
    
    Signature ``LineTypePriority`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineTypePriority`` 
    
    :param priority: 
    :type priority: int 
    
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
    ObjectId: str = ...
    """
    Returns  the object Id of the line type.  
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectId`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: LineTypeBuilder = ...  # unknown typename


class Symbol3DBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Symbol3DBuilder.  
    
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
    
    PortMappingData: NXOpen.ITableEditorDataProvider = ...
    """
    Returns  the data provider of the port mapping table.  
    
    <hr>
    
    Getter Method
    
    Signature ``PortMappingData`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ITableEditorDataProvider` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: Symbol3DBuilder = ...  # unknown typename


class LineTypeBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[LineTypeBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: LineTypeBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
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
    
    
    def FindIndex(self, obj: LineTypeBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> LineTypeBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
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
    def Erase(self, obj: LineTypeBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: LineTypeBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
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
    
    
    def GetContents(self) -> 'list[LineTypeBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[LineTypeBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
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
    def Swap(self, object1: LineTypeBuilder, object2: LineTypeBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: LineTypeBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.DiagrammingLibraryAuthor.LineTypeBuilder` 
        
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
    Null: LineTypeBuilderList = ...  # unknown typename


