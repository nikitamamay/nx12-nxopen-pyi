# module 'NXOpen.Layer'
#
# Automatically generated 2025-06-09T14:38:46.883700
#
"""Default documentation for NXOpen.Layer."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class Category(NXOpen.NXObject):
    """
    Represents a layer category.  
    
    A layer category is a set of layers.  A layer
    can belong to more than one category. 
    To create a new instance of this class, use :py:meth:`NXOpen.Layer.CategoryCollection.CreateCategory`
    
    .. versionadded:: NX3.0.0
    """
    
    def SetMemberLayers(self, layers: 'list[int]') -> None:
        """
        Sets which layers belong to the category 
        
        Signature ``SetMemberLayers(layers)`` 
        
        :param layers: 
        :type layers: list of int 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetMemberLayers(self) -> 'list[int]':
        """
        Returns all the layers that belong to the category  
        
        Signature ``GetMemberLayers()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetState(self, state: State) -> None:
        """
        Changes the state of every layer in the category to the
        specified state, except the work layer 
        
        Signature ``SetState(state)`` 
        
        :param state:  new state for the category.  Must not be                                :py:class:`LayerState.WorkLayer <LayerState>`  
        :type state: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    Description: str = ...
    """
    Returns or sets  the category's description, if one exists 
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: Category = ...  # unknown typename


class StateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class State():
    """
    Represents the state of the layer 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WorkLayer", "Work layer. All newly created objects are placed on the work layer."
       "Selectable", "Objects on the layer are selectable"
       "Visible", "Objects on the layer are visible but not selectable"
       "Hidden", "Objects on the layer are not visible and not selectable"
    """
    WorkLayer = 0  # StateMemberType
    Selectable = 1  # StateMemberType
    Visible = 2  # StateMemberType
    Hidden = 3  # StateMemberType
    
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
    


class CategoryCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of layer categories   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX3.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateCategory(self, name: str, description: str, memberLayers: 'list[int]') -> Category:
        """
        Creates a new layer category  
        
        Signature ``CreateCategory(name, description, memberLayers)`` 
        
        :param name:  The name must not None and                             must not already be used by another layer category.  
        :type name: str 
        :param description:  Optional  
        :type description: str 
        :param memberLayers:  Layers to be placed into the category  
        :type memberLayers: list of int 
        :returns:  The new category  
        :rtype: :py:class:`NXOpen.Layer.Category` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, name: str) -> Category:
        """
        Finds the :py:class:`NXOpen.Layer.Category` with the given name.  
        
        An exception will be thrown if no object can be found with the given name.
        
        Signature ``FindObject(name)`` 
        
        :param name:  The name of the :py:class:`NXOpen.Layer.Category`  
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Layer.Category` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    


class StateCollection(NXOpen.TransientObject):
    """
    Represents a copy of the layer states.  
    
    You can manipulate the 
    StateCollection without affecting the actual layer states in the part.
    Your changes to the StateCollection will not be applied to the part until you
    apply them through the method :py:meth:`Layer.LayerManager.SetStates`. 
    
    .. versionadded:: NX3.0.0
    """
    
    def GetState(self, layer: int) -> State:
        """
        Returns the state of the specified layer  
        
        Signature ``GetState(layer)`` 
        
        :param layer: 
        :type layer: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetState(self, layer: int, state: State) -> None:
        """
        Sets the state of the specified layer 
        
        Signature ``SetState(layer, state)`` 
        
        :param layer: 
        :type layer: int 
        :param state: 
        :type state: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStateOfCategory(self, category: Category, state: State) -> None:
        """
        Sets the state of every layer in the category to the
        specified state, except the work layer  
        
        Signature ``SetStateOfCategory(category, state)`` 
        
        :param category: 
        :type category: :py:class:`NXOpen.Layer.Category` 
        :param state:  new state for the category.  Must not be                                :py:class:`LayerState.WorkLayer <LayerState>`  
        :type state: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
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
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    


class StateInfo():
    """
    Used in several methods that get or set the state of a layer .  
    
    Constructor: 
    NXOpen.Layer.StateInfo()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Layer: int = ...
    """
    Layer number 
    <hr>
    
    Field Value
    Type:int
    """
    State: State = ...
    """
    The state of the layer 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Layer.State`
    """


class ConstantsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Constants():
    """
    Constants for layers 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FirstLayer", "The number of the first layer. Valid layers are numbered from :py:class:`LayerConstants.FirstLayer <LayerConstants>` to :py:class:`LayerConstants.LastLayer <LayerConstants>`"
       "LastLayer", "The number of the last layer. Valid layers are numbered from :py:class:`LayerConstants.FirstLayer <LayerConstants>` to :py:class:`LayerConstants.LastLayer <LayerConstants>`"
    """
    FirstLayer = 1  # ConstantsMemberType
    LastLayer = 256  # ConstantsMemberType
    
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
    


class LayerManager():
    """
    Represents an object that manages layers   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX3.0.0
    """
    
    @typing.overload
    def ChangeStates(self, stateArray: 'list[StateInfo]', fitAll: bool) -> None:
        """
        Changes the states of the specified layers in the part. 
        Note: there must be exactly one work layer.  If you change the work layer,
        you must specify a new work layer.  If you set the work layer, the
        old work layer will be changed to Selectable, unless you specify otherwise.
        The part must be the displayed part.
        
        Signature ``ChangeStates(stateArray, fitAll)`` 
        
        :param stateArray:                  Indicates the new states for the layers.  
        :type stateArray: list of :py:class:`NXOpen.Layer.StateInfo` 
        :param fitAll:  Whether to refit the view to what is visible after the layer states have been changed  
        :type fitAll: bool 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ChangeStates(self, stateArray: 'list[StateInfo]') -> None:
        """
        Changes the states of the specified layers in the part. 
        Note: there must be exactly one work layer.  If you change the work layer,
        you must specify a new work layer.  If you set the work layer, the
        old work layer will be changed to Selectable, unless you specify otherwise.
        The part must be the displayed part.
        
        Signature ``ChangeStates(stateArray)`` 
        
        :param stateArray:                  Indicates the new states for the layers.  
        :type stateArray: list of :py:class:`NXOpen.Layer.StateInfo` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetStates(self) -> StateCollection:
        """
        Gets the states for all layers in the part.  
        
        The part must be the displayed part.  
        
        Signature ``GetStates()`` 
        
        :returns:  Indicates the states for all layers in the part.  
        :rtype: :py:class:`NXOpen.Layer.StateCollection` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetStates(self, stateCollection: StateCollection, fitAll: bool) -> None:
        """
        Sets the states for all layers in the part.  The part must be the displayed part.
        Note: there must be exactly one work layer. 
        
        Signature ``SetStates(stateCollection, fitAll)`` 
        
        :param stateCollection:  The states for all layers in the part.   
        :type stateCollection: :py:class:`NXOpen.Layer.StateCollection` 
        :param fitAll:  Whether to refit the view to what is visible after the layer states have been changed  
        :type fitAll: bool 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetStates(self, stateCollection: StateCollection) -> None:
        """
        Sets the states for all layers in the part.  The part must be the displayed part.
        Note: there must be exactly one work layer. 
        
        Signature ``SetStates(stateCollection)`` 
        
        :param stateCollection:  The states for all layers in the part.   
        :type stateCollection: :py:class:`NXOpen.Layer.StateCollection` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetState(self, layer: int, state: State) -> None:
        """
        Sets the state of the specified layer.
        The specified layer must not be the work layer.
        If you are changing the state of the layer to Work,
        the old work layer will be changed to Selectable.
        The part must be the displayed part.
        
        Signature ``SetState(layer, state)`` 
        
        :param layer: 
        :type layer: int 
        :param state: 
        :type state: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetState(self, layer: int, state: State, fitAll: bool) -> None:
        """
        Sets the state of the specified layer.
        The specified layer must not be the work layer.
        If you are changing the state of the layer to Work,
        the old work layer will be changed to Selectable.
        The part must be the displayed part.
        
        Signature ``SetState(layer, state, fitAll)`` 
        
        :param layer: 
        :type layer: int 
        :param state: 
        :type state: :py:class:`NXOpen.Layer.State` 
        :param fitAll:  Whether to refit the view to what is visible after the layer state has been changed  
        :type fitAll: bool 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetState(self, layer: int) -> State:
        """
        Gets the state of the specified layer.  
        
        The part must be the displayed part.  
        
        Signature ``GetState(layer)`` 
        
        :param layer: 
        :type layer: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Layer.State` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveDisplayableObjects(self, newLayer: int, objectArray: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Moves displayable objects to the specified layer.  
        
        The specified part may be the displayed part or the work part.  If it is
        the work part but not the displayed part, then none of the objects to be
        moved may be currently displayed.
        
        This method is the preferred way to change the layer of one or more objects,
        because :py:meth:`NXOpen.DisplayableObject.Layer` does not correct
        the display of the objects and does not work as expected for sketches and
        components, because it does not move the members of the sketch or component.
        
        Objects of class :py:class:`NXOpen.CAE.CAEEdge`,
        :py:class:`NXOpen.CAE.CAEFace`, :py:class:`NXOpen.CAE.CAEVertex`,
        :py:class:`NXOpen.Edge`, :py:class:`NXOpen.Face` or
        :py:class:`NXOpen.View` may not be moved.
        
        Signature ``MoveDisplayableObjects(newLayer, objectArray)`` 
        
        :param newLayer:  The layer to move the objects to  
        :type newLayer: int 
        :param objectArray:  The objects to be moved  
        :type objectArray: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING")
        """
        ...
    
    
    def ApplyMoveToLayerToOwningParts(self, newLayer: int, objectArray: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Move the selected objects to the specified layer in their Owning Parts.  
        
        This only works when a single layer has been selected on the Layer Settings dialog.
        
        The owning parts will be fully loaded if they are not already.
        
        Objects of class :py:class:`NXOpen.CAE.CAEEdge`,
        :py:class:`NXOpen.CAE.CAEFace`, :py:class:`NXOpen.CAE.CAEVertex`,
        :py:class:`NXOpen.Edge`, :py:class:`NXOpen.Face` or
        :py:class:`NXOpen.View` may not be moved.
        
        Signature ``ApplyMoveToLayerToOwningParts(newLayer, objectArray)`` 
        
        :param newLayer:  The layer in the owning parts to move the objects to  
        :type newLayer: int 
        :param objectArray:  The objects to be moved  
        :type objectArray: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING")
        """
        ...
    
    
    def GetAllObjectsOnLayer(self, layer: int) -> 'list[NXOpen.NXObject]':
        """
        Returns all objects on the specified layer.  
        
        This includes objects which are not counted as objects on the layer by the "Layer Settings" dialog.
        
        The part must be the displayed part.
        
        Signature ``GetAllObjectsOnLayer(layer)`` 
        
        :param layer: 
        :type layer: int 
        :returns:  All the objects on the specified layer  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyObjects(self, newLayer: int, objectArray: 'list[NXOpen.NXObject]') -> None:
        """
        Copies objects to the specified layer
        
        Objects of class :py:class:`NXOpen.Assemblies.Component`,
        :py:class:`NXOpen.DatumAxis`, :py:class:`NXOpen.DatumPlane`
        :py:class:`NXOpen.Edge`, :py:class:`NXOpen.Face`,
        :py:class:`NXOpen.Features.Feature` or :py:class:`NXOpen.View`,
        may not be copied.
        
        Objects of type UF_cs2_vertex_type may not be copied.
        
        The part must be the work part.
        
        Signature ``CopyObjects(newLayer, objectArray)`` 
        
        :param newLayer:  The layer to move the objects to  
        :type newLayer: int 
        :param objectArray:  The objects to be copied  
        :type objectArray: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING")
        """
        ...
    
    
    def GetVisibilitiesInView(self, view: NXOpen.View) -> 'list[StateInfo]':
        """
        Gets the visibility of all layers in a specified view.  
        
        The part must be the displayed part. 
        
        Signature ``GetVisibilitiesInView(view)`` 
        
        :param view:  The view object being queried  
        :type view: :py:class:`NXOpen.View` 
        :returns:  The current states for the layers.
        The returned states can only be
        :py:class:`LayerState.Visible <LayerState>` and
        :py:class:`LayerState.Hidden <LayerState>`.
        state_array[i] is for layer i+1  
        :rtype: list of :py:class:`NXOpen.Layer.StateInfo` 
        
        .. versionadded:: NX4.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetObjectsVisibilityOnLayer(self, view: NXOpen.View, stateArray: 'list[StateInfo]', doUpdate: bool) -> None:
        """
        Sets specified layer(s) visibility in a specified view.  
        
        The part must be the displayed part. 
        
        Signature ``SetObjectsVisibilityOnLayer(view, stateArray, doUpdate)`` 
        
        :param view:  The view object being modified  
        :type view: :py:class:`NXOpen.View` 
        :param stateArray:  The new states for the layers.                                             The given states may only be                                             :py:class:`LayerState.Visible <LayerState>` and                                             :py:class:`LayerState.Hidden <LayerState>`.  
        :type stateArray: list of :py:class:`NXOpen.Layer.StateInfo` 
        :param doUpdate:  Whether to update the view(s) after the layer states have been changed  
        :type doUpdate: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetViewVisibilityToGlobal(self, view: NXOpen.View) -> None:
        """
        Resets a view's layer visibility to the global states.  
        
        The part must be the displayed part. 
        
        Signature ``ResetViewVisibilityToGlobal(view)`` 
        
        :param view:  The view object  
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    WorkLayer: int = ...
    """
    Returns or sets  the work layer.  
    
    If you change the work layer, the old work layer is changed to Selectable.
    The part must be the displayed part. 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkLayer`` 
    
    :returns:  Layer number of the work layer  
    :rtype: int 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WorkLayer`` 
    
    :param newWorkLayer:  Layer number for the new work layer  
    :type newWorkLayer: int 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """


