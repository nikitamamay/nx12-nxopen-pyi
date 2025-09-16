# module 'NXOpen.Assemblies'
#
# Automatically generated 2025-06-09T14:38:43.589875
#
"""Default documentation for NXOpen.Assemblies."""

import typing

import NXOpen
import NXOpen.Assemblies.ProductInterface
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.PDM
import NXOpen.PartFamily
import NXOpen.Positioning
import NXOpen.Routing



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ComponentRepresentationModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentRepresentationMode():
    """
    Representation status of a component
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Lightweight", "The component's solid bodies are all displayed using the lightweight representation"
       "Partial", "The component's solid bodies are displayed with some being exact and some being shown lightweight"
       "Exact", "The component's solid bodies are displayed with the exact data"
       "NotSet", "There are no bodies to display for the current component"
    """
    Lightweight = 0  # ComponentRepresentationModeMemberType
    Partial = 1  # ComponentRepresentationModeMemberType
    Exact = 2  # ComponentRepresentationModeMemberType
    NotSet = 3  # ComponentRepresentationModeMemberType
    
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
    


class Component(NXOpen.DisplayableObject, NXOpen.Routing.ICharacteristic):
    """
    Represents a component in a :py:class:`NXOpen.Assemblies.ComponentAssembly`.  
    
    Note that a
    Component is an occurrence whose prototype is a :py:class:`NXOpen.Part`. See
    :py:meth:`NXOpen.NXObject.Prototype`.
    
    Components are arranged in a tree, with each component having a single parent, and one
    or more children. The top of the tree is the Root Component (see
    :py:meth:`NXOpen.Assemblies.ComponentAssembly.RootComponent` which has a None
    parent. The components below the root are referred to as "Top Level" components, which
    represent the component parts that have been added directly to the
    ComponentAssembly. (Calling :py:meth:`NXOpen.Assemblies.ComponentAssembly.AddComponent` will
    create a new Top Level component.) Components beneath the top level represent
    components defined in sub-assemblies of the main assembly.
    
    .. versionadded:: NX3.0.0
    """
    
    class RepresentationMode():
        """
        Representation status of a component
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Lightweight", "The component's solid bodies are all displayed using the lightweight representation"
           "Partial", "The component's solid bodies are displayed with some being exact and some being shown lightweight"
           "Exact", "The component's solid bodies are displayed with the exact data"
           "NotSet", "There are no bodies to display for the current component"
        """
        Lightweight = 0  # ComponentRepresentationModeMemberType
        Partial = 1  # ComponentRepresentationModeMemberType
        Exact = 2  # ComponentRepresentationModeMemberType
        NotSet = 3  # ComponentRepresentationModeMemberType
        
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
        
    
    
    def GetChildren(self) -> 'list[Component]':
        """
        Returns the child components of this component 
        However, it does not return non-geometric components (NGCs)
        To enable this method to also return NGCs, set the following environment variable:
        UGII_ALLOW_NGC_IN_UGOPEN=YES  
        
        Signature ``GetChildren()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindOccurrence(self, proto: NXOpen.NXObject) -> NXOpen.NXObject:
        """
        Given a prototype object, returns the corresponding occurrence
        in this component  
        
        Signature ``FindOccurrence(proto)`` 
        
        :param proto:  the prototype  
        :type proto: :py:class:`NXOpen.NXObject` 
        :returns:  the occurrence of the prototype in this component  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLayerOption(self) -> int:
        """
        Gets the layer option.  
        
        This controls which layer the component's geometry will appear on in its parent part.
        
        Signature ``GetLayerOption()`` 
        
        :returns:  The layer option of the component in its parent part
        -1 Means that the component's geometry has the layer settings defined in its orginal part
        1-255 Means the components geometry is on the specified layer
        
        :rtype: int 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetLayerOption(self, layer: int) -> None:
        """
        Sets the layer option.  
        
        This controls which layer the component's geometry will appear on in its parent part.
        
        Signature ``SetLayerOption(layer)`` 
        
        :param layer:  The new layer for this component in its parent part                                      -1 Means use the original layer settings defined in the component's part.                                      0 Means use the current work layer                                      1-255 Means use the specified layer.                          
        :type layer: int 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPosition(self) -> tuple:
        """
        Gets the position of a component
        
        Signature ``GetPosition()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (position, orientation). position is a :py:class:`NXOpen.Point3d`.   The origin of this component orientation is a :py:class:`NXOpen.Matrix3x3`.   The orientation of this component 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EstablishPositionOverride(self, parent: Component) -> None:
        """
        Ensures there is a positioning override on component in the given part of
        the given parent.  
        
        This method does nothing if the component already has a
        positioning override in the parent, or if any necessary data is unloaded.
        
        If parent is None, the positioning override will be created in the same part 
        as the :py:class:`NXOpen.Assemblies.Component`.
        
        Signature ``EstablishPositionOverride(parent)`` 
        
        :param parent:  The parent of the component in which the override is to be created  
        :type parent: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EstablishIsolatedPositionOverride(self, parent: Component, arrangement: Arrangement) -> None:
        """
        Ensures there is an isolated positioning override for the :py:class:`NXOpen.Assemblies.Component` in the given part of
        the given parent.  
        
        This method does nothing if the :py:class:`NXOpen.Assemblies.Component` already has an isolated
        positioning override in the parent, or if any necessary data is unloaded.
        
        If parent is None, the isolated positioning override will be created in the same part as the :py:class:`NXOpen.Assemblies.Component`.
        
        Signature ``EstablishIsolatedPositionOverride(parent, arrangement)`` 
        
        :param parent:  The parent of the :py:class:`NXOpen.Assemblies.Component` in which the override is to be created  
        :type parent: :py:class:`NXOpen.Assemblies.Component` 
        :param arrangement:  The :py:class:`NXOpen.Assemblies.Arrangement` in which to create the                                                        isolated position override. This :py:class:`NXOpen.Assemblies.Arrangement` must be                                                         an isolated :py:class:`NXOpen.Assemblies.Arrangement`.                                                     
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetPositioningIsolated(self, arrangement: Arrangement) -> None:
        """
        Set positioning for the selected :py:class:`NXOpen.Assemblies.Component` as isolated in the specified 
        :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        The arrangement must be an isolated arrangement defined in the same part as the component.
        
        Signature ``SetPositioningIsolated(arrangement)`` 
        
        :param arrangement:  The :py:class:`NXOpen.Assemblies.Arrangement` in which to set                                                        positioning as isolated. This :py:class:`NXOpen.Assemblies.Arrangement` must                                                         be an isolated :py:class:`NXOpen.Assemblies.Arrangement`.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def IsPositioningIsolated(self, arrangement: Arrangement) -> bool:
        """
        Get whether positioning for the selected :py:class:`NXOpen.Assemblies.Component` is isolated in the specified 
        :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        Signature ``IsPositioningIsolated(arrangement)`` 
        
        :param arrangement:  The specified :py:class:`NXOpen.Assemblies.Arrangement`.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  Whether positioning for the selected :py:class:`NXOpen.Assemblies.Component` is isolated 
        in the specified :py:class:`NXOpen.Assemblies.Arrangement`. 
        :rtype: bool 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemovePositionOverride(self, parent: Component) -> None:
        """
        Removes the highest level positioning override on component in or below
        the given parent.  
        
        parent may be None, in which case the highest level
        positioning override on component is removed.  This method does nothing
        if there is no positioning override on the component, or if any necessary
        data is unloaded.
        
        Signature ``RemovePositionOverride(parent)`` 
        
        :param parent:  The parent of the component in or below which the override is to be removed  
        :type parent: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPositionOverrideParent(self) -> Component:
        """
        Find the highest level parent in which the position of component is
        overridden.  
        
        This will be None if the component is not overridden.
        It will be the root component if the component is overridden in
        the same part as itself.  It will be None if the position of the
        component is overridden in a parent assembly which is currently
        unloaded.
        
        Signature ``GetPositionOverrideParent()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPositionOverrideType(self) -> PositionOverrideType:
        """
        Gets the type of the highest level positioning override on the component.  
        
        Signature ``GetPositionOverrideType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PositionOverrideType` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetArrangements(self) -> 'list[Arrangement]':
        """
        Outputs the :py:class:`NXOpen.Assemblies.Arrangement` objects within the :py:class:`NXOpen.Assemblies.Component`.  
        
        They are output in alphabetic order.
        
        Signature ``GetArrangements()`` 
        
        :returns:  Alphabetically sorted arrangements  
        :rtype: list of :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetUsedArrangement(self, newArrangement: Arrangement) -> None:
        """
        Changes the Arrangement used for this component.  
        
        If this is the root component
        (i.e. it has no parent) then this is equivalent to setting the active arrangement
        in the owner. (See :py:meth:`NXOpen.Assemblies.Component.DirectOwner` and
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.ActiveArrangement`.) For
        non-root components, this sets the arrangement used for this component in the
        context of its parent component. Note that this method should only be used for
        components which have children.
        
        Signature ``SetUsedArrangement(newArrangement)`` 
        
        :param newArrangement:  The new :py:class:`NXOpen.Assemblies.Arrangement`. This Arrangement                                                               must be defined in a the ComponentAssembly of this Component's                                                               prototype part.                                                             
        :type newArrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetPositioningVaried(self, components: 'list[Component]', setAsVaried: bool) -> None:
        """
        Set positioning for the selected :py:class:`NXOpen.Assemblies.Component`s across all possible 
        :py:class:`NXOpen.Assemblies.Arrangement`s.  
        
        Positioning can be set to either the same in all
        :py:class:`NXOpen.Assemblies.Arrangement`s, set_as_varied = FALSE, or individually positioned in each,
        set_as_varied = TRUE. 
        
        Signature ``SetPositioningVaried(components, setAsVaried)`` 
        
        :param components:  The components whose positioning will be altered.  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param setAsVaried:  If FALSE components will have same position in all :py:class:`NXOpen.Assemblies.Arrangement`s, TRUE allows the position to be varied.  
        :type setAsVaried: bool 
        
        .. versionadded:: NX7.5.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def Suppress(self) -> None:
        """
        Suppresses the component in the ComponentAssembly that contains its controlling Arrangement. 
        The component will be suppressed in all Arrangements in the ComponentAssembly, not just
        in the controlling arrangement.
        
        This is equivalent to calling:
        
        :py:meth:`NXOpen.Assemblies.Component.SuppressingArrangement`
        
        :py:meth:`NXOpen.Assemblies.Arrangement.Owner`
        
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.SuppressComponents`
        
        Signature ``Suppress()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def Suppress(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Suppresses an array of components in the ComponentAssembly that contains their
        controlling Arrangement.  The component will be suppressed in all Arrangements in
        the ComponentAssembly.  
        
        This is equivalent to calling:
        
        :py:meth:`NXOpen.Assemblies.Component.SuppressingArrangement`
        
        :py:meth:`NXOpen.Assemblies.Arrangement.Owner`
        
        And then calling
        
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.SuppressComponents`
        
        on the component array. Note that all components should have
        the same suppressing Arrangement.
        
        Signature ``Suppress(components)`` 
        
        :param components:  Components to be suppressed. Each component will be                                                                                    suppressed in its controlling arrangement. Note that                                                                                    the components must all be underneath the same assembly                                                                                 
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the suppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def Unsuppress(self) -> None:
        """
        Unsuppresses the component in the ComponentAssembly that contains its controlling Arrangement. 
        The component will be unsuppressed in all Arrangements in the ComponentAssembly.
        
        This is equivalent to calling:
        
        :py:meth:`NXOpen.Assemblies.Component.SuppressingArrangement`
        
        :py:meth:`NXOpen.Assemblies.Arrangement.Owner`
        
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.UnsuppressComponents`
        
        Signature ``Unsuppress()`` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def Unsuppress(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Unsuppresses an array of components in the ComponentAssembly that contains their
        controlling Arrangement.  The component will be unsuppressed in all Arrangements in
        the ComponentAssembly.  This is equivalent to calling:
        
        :py:meth:`NXOpen.Assemblies.Component.SuppressingArrangement`
        
        :py:meth:`NXOpen.Assemblies.Arrangement.Owner`
        
        :py:meth:`NXOpen.Assemblies.ComponentAssembly.UnsuppressComponents`
        
        on the component array. Note that all components should have
        the same suppressing Arrangement.
        
        Signature ``Unsuppress(components)`` 
        
        :param components:  Components to be unsuppressed. Each component will be                                                                                    unsuppressed in its controlling arrangement. Note that                                                                                    the components must all be underneath the same assembly                                                                                 
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the unsuppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def UpdateStructure(self, components: 'list[Component]', nLevels: int) -> None:
        """
        Update the assembly structure for this assembly in the 
        context of the displayed part to the specified number of
        levels, ignoring components already processed by previous
        calls.
        
        Signature ``UpdateStructure(components, nLevels)`` 
        
        :param components:  Component tags to start update structure from  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param nLevels:  The number of levels to update. If -1 then all levels are updated. 
        :type nLevels: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    @typing.overload
    def UpdateStructure(self, components: 'list[Component]', nLevels: int, checkComponentsVisited: bool) -> None:
        """
        Update the assembly structure for this assembly in the 
        context of the displayed part to the specified number of
        levels.
        
        Signature ``UpdateStructure(components, nLevels, checkComponentsVisited)`` 
        
        :param components:  Component tags to start update structure from  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param nLevels:  The number of levels to update. If -1 then all levels are updated. 
        :type nLevels: int 
        :param checkComponentsVisited:  If true, only perform update structure on each component once this session. 
        :type checkComponentsVisited: bool 
        
        .. versionadded:: NX4.0.1
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def GetConstraints(self) -> 'list[NXOpen.Positioning.ComponentConstraint]':
        """
        Returns the :py:class:`NXOpen.Positioning.ComponentConstraint`s directly connected to this component.  
        
        If
        the part containing those constraints is not loaded then no constraints will be 
        returned.
        
        Signature ``GetConstraints()`` 
        
        :returns:  Constraints directly connected to this component  
        :rtype: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def GetDegreesOfFreedom(self) -> DegreesOfFreedom:
        """
        Returns the :py:class:`NXOpen.Assemblies.DegreesOfFreedom` for this component. 
        Any constraints that reference unloaded data are ignored in the degrees of freedom calculation. An example
        would be if a constraint was referencing geometry in an unloaded component. When this occurs there may be
        a greater number of degrees of freedom than if all the data were loaded.
        
        Signature ``GetDegreesOfFreedom()`` 
        
        :returns:  The degrees of freedom of this component.  
        :rtype: :py:class:`NXOpen.Assemblies.DegreesOfFreedom` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def GetDegreesOfFreedom(self, components: 'list[Component]') -> DegreesOfFreedom:
        """
        Returns the :py:class:`NXOpen.Assemblies.DegreesOfFreedom` for this component. 
        The degrees of freedom are found relative to the components passed in.
        Those components are regarded as fixed and only constraints directly 
        connecting this component with those in the array are considered.
        
        Note that any directly connected constraints that reference unloaded data
        are ignored in the degrees of freedom calculation. An example would be if
        a constraint was referencing geometry in an unloaded component. When this
        occurs there may be a greater number of degrees of freedom than if all
        the data were loaded.         
        
        Signature ``GetDegreesOfFreedom(components)`` 
        
        :param components:  Components relative to which the degrees                                                                                                of freedom will be found.                                                                                            
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The degrees of freedom of this component.  
        :rtype: :py:class:`NXOpen.Assemblies.DegreesOfFreedom` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RecallConstraints(self) -> None:
        """
        Recalls the :py:class:`NXOpen.Positioning.ComponentConstraint`s previously remembered on the part
        of this component, creating new constraints from them.  
        
        The new constraints are
        incomplete and refer to the component.
        
        Signature ``RecallConstraints()`` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RecallAndListConstraints(self) -> 'list[NXOpen.Positioning.ComponentConstraint]':
        """
        Recalls the :py:class:`NXOpen.Positioning.ComponentConstraint`s previously remembered on the part
        of this component, creating new constraints from them.  
        
        The new constraints are
        incomplete and refer to the component.
        
        Signature ``RecallAndListConstraints()`` 
        
        :returns:  The constraints created by the recall operation  
        :rtype: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveRememberedConstraints(self) -> None:
        """
        Remove all the remembered constraints stored on the part of this component.  
        
        Signature ``RemoveRememberedConstraints()`` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetNonGeometricState(self) -> bool:
        """
        Gets the component state as Geometric or Non-Geometric.  
        
        Signature ``GetNonGeometricState()`` 
        
        :returns:  True if the component is non-geometric, false otherwise  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetComponentQuantityType(self) -> ComponentQuantity:
        """
        Gets the quantity type of the components.  
        
        Returns :py:class:`NXOpen.Assemblies.ComponentQuantity`.
        
        Signature ``GetComponentQuantityType()`` 
        
        :returns:  Quantity type an enumeration value  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentQuantity` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetIntegerQuantity(self) -> int:
        """
        Gets the value of the integer quantity of component.  
        
        Signature ``GetIntegerQuantity()`` 
        
        :returns:  Integer quantity value  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetRealQuantity(self) -> tuple:
        """
        Gets the value of real quantity and corresponding units on this component.  
        
        Signature ``GetRealQuantity()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (realQuantity, quantityUnits). realQuantity is a float.   Real quantity value quantityUnits is a str.   Units 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetAsRequiredQuantity(self) -> str:
        """
        Gets the as-required quantity on this component.  
        
        Signature ``GetAsRequiredQuantity()`` 
        
        :returns:  As-Required string "A/R" 
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DisplayComponentsLightweight(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Sets an array of components to display using the lightweight representation.  
        
        Signature ``DisplayComponentsLightweight(components)`` 
        
        :param components:  Array of components to be set to lightweight  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the display as lightweight  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def DisplayComponentsExact(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Sets an array of components to display using the exact representation.  
        
        Signature ``DisplayComponentsExact(components)`` 
        
        :param components:  Array of componets to be set to exact  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the display as exact  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def GetComponentRepresentationMode(self) -> ComponentRepresentationMode:
        """
        Returns the representation mode for the component's bodies.  
        
        This mode is dependent on the currently used reference set for the component.
        
        Signature ``GetComponentRepresentationMode()`` 
        
        :returns:  The mode for the components display. An enumeration value.  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentRepresentationMode` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetInstanceUserAttribute(self, info: NXOpen.NXObjectAttributeInformation_Struct, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies an attribute with the option to update or not. 
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`.
        Instead, set the type to :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>` and specify a ReferenceValue.
        
        The following data members of the Info structure are ignored by this method:
        Alias
        Inherited
        Required
        Unset
        Locked
        
        The following data members of an attribute cannot be edited once the attribute is set:
        Type 
        Title
        TitleAlias
        Array
        ArrayElementIndex
        The dimensionality of the Unit specification (cannot change from mm to microA, but from mm to cm is fine) 
        
        The following data members can be set and modified only if the attribute is not associated with a template:
        Category
        
        The following data of an attribute can be set if and only if the attribute is not associated with a template. It cannot be modified once set.
        Array 
        
        Signature ``SetInstanceUserAttribute(info, option)`` 
        
        :param info: 
        :type info: :py:class:`NXOpen.NXObjectAttributeInformation_Struct` 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: int, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies an integer attribute with the option to update or not. 
        
        Signature ``SetInstanceUserAttribute(title, index, value, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param value: 
        :type value: int 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: float, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a real attribute with the option to update or not. 
        
        Signature ``SetInstanceUserAttribute(title, index, value, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param value: 
        :type value: float 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetInstanceUserAttribute(self, title: str, index: int, value: str, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a string attribute with the option to update or not. 
        
        Signature ``SetInstanceUserAttribute(title, index, value, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param value: 
        :type value: str 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetInstanceUserAttribute(self, title: str, index: int, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a null attribute with the option to update or not. 
        
        Signature ``SetInstanceUserAttribute(title, index, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInstanceTimeUserAttribute(self, title: str, index: int, value: str, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a time attribute with the option to update or not.  
        
        The time value is assumed to be in the current time zone of the machine running the program. 
        NX will store the value in UTC. 
        
        Signature ``SetInstanceTimeUserAttribute(title, index, value, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param value:  The current date and time is used if                                    the value is None.  See                                    :py:class:`NXOpen.NXObjectDateAndTimeFormat`                                    for valid formats.  
        :type value: str 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInstanceBooleanUserAttribute(self, title: str, index: int, value: bool, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a boolean attribute with the option to update or not.  
        
        Signature ``SetInstanceBooleanUserAttribute(title, index, value, option)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :param value: 
        :type value: bool 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def HasInstanceUserAttribute(self, title: str, type: NXOpen.NXObjectAttributeType, index: int) -> bool:
        """
        Determines if and attribute with the given Title, Type and array Index is present on the object
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).  
        
        The first element of an array has Index 0 (zero).
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`.
        Instead, use :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>`.  
        
        Signature ``HasInstanceUserAttribute(title, type, index)`` 
        
        :param title: 
        :type title: str 
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceUserAttribute(self, title: str, type: NXOpen.NXObjectAttributeType, index: int) -> NXOpen.NXObjectAttributeInformation_Struct:
        """
        Gets the first attribute encountered on the object, if any, with a given Title, Type and array Index.  
        
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`.
        The date format set by the Customer Defaults is used for attributes of type time.
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`.
        Instead, use :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>`.
        For reference type string attributes, both the ReferenceValue and the calculated StringValue are returned.  
        
        Signature ``GetInstanceUserAttribute(title, type, index)`` 
        
        :param title: 
        :type title: str 
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObjectAttributeInformation_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceBooleanUserAttribute(self, title: str, index: int) -> bool:
        """
        Gets a boolean attribute by Title and array Index.  
        
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`.  
        
        Signature ``GetInstanceBooleanUserAttribute(title, index)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceIntegerUserAttribute(self, title: str, index: int) -> int:
        """
        Gets an integer attribute by Title and array Index.  
        
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`.  
        
        Signature ``GetInstanceIntegerUserAttribute(title, index)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceRealUserAttribute(self, title: str, index: int) -> float:
        """
        Gets a real attribute by Title and array Index.  
        
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`.  
        
        Signature ``GetInstanceRealUserAttribute(title, index)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceStringUserAttribute(self, title: str, index: int) -> str:
        """
        Gets a string attribute by Title and array Index.  
        
        For reference type string attributes, the calculated StringValue is returned.
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`.
        Gets a string attribute value by title.  
        
        Signature ``GetInstanceStringUserAttribute(title, index)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceTimeUserAttribute(self, title: str, index: int) -> str:
        """
        Gets a time attribute by Title and array Index.  
        
        The date format set by the Customer Defaults is used.
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributes`. 
        Gets a time attribute by title.  
        
        Signature ``GetInstanceTimeUserAttribute(title, index)`` 
        
        :param title: 
        :type title: str 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetInstanceUserAttributes(self) -> 'list[NXOpen.NXObjectAttributeInformation_Struct]':
        """
        Gets all the attributes that have been set on the given object.
        The elements of array attributes are returned individually in order of increasing indices. 
        The returned Title of an array element is the array title (without index). The Index data member holds the index.
        The date format set by the Customer Defaults is used.
        Reference type attributes are returned as being of type :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>`,
        and both the ReferenceValue and the calculated StringValue are returned.  
        
        Signature ``GetInstanceUserAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObjectAttributeInformation_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetInstanceUserAttributes(self, includeUnset: bool) -> 'list[NXOpen.NXObjectAttributeInformation_Struct]':
        """
        Gets all the attributes that have been set on the given object, 
        as well as information from attribute templates that have not been set (if 'IncludeUnset' is 'true').
        The elements of array attributes are returned individually in order of increasing indices. 
        The returned Title of an array element is the array title (without index). The Index data member holds the index.
        The date format set by the Customer Defaults is used.
        Reference type attributes are returnes as being of type :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>`,
        and both the ReferenceValue and the calculated StringValue are returned.  
        
        Signature ``GetInstanceUserAttributes(includeUnset)`` 
        
        :param includeUnset: 
        :type includeUnset: bool 
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObjectAttributeInformation_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceUserAttributeAsString(self, title: str, type: NXOpen.NXObjectAttributeType, index: int) -> str:
        """
        Gets the first attribute encountered on the object, if any, with a given title, type and array index.  
        
        The value of the attribute is converted to and returned as a string.
        If the attribute is not an array, the Index is ignored (if this is known beforehand, we recommend setting the Index to -1 to save time).
        The first element of an array has Index 0 (zero).
        To get all the array elements of an array, please use :py:meth:`NXOpen.NXObject.GetUserAttributesAsStrings`.
        The date format set by the Customer Defaults is used for attributes of type time.
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`.
        Instead, use :py:class:`NXOpen.NXObjectAttributeType.String <NXOpen.NXObjectAttributeType>`.
        For reference type string attributes, the calculated StringValue is returned.  
        
        Signature ``GetInstanceUserAttributeAsString(title, type, index)`` 
        
        :param title: 
        :type title: str 
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param index: 
        :type index: int 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceUserAttributesAsStrings(self) -> 'list[str]':
        """
        Gets all the attributes that have been set on the given object.  
        
        The values are returned as strings.
        The elements of array attributes are returned individually in order of increasing indices. 
        The returned Title of an array element is the array title (without index). The Index data member holds the index.
        This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`.
        Reference type attributes return the calculated StringValue.
        The date format set by the Customer Defaults is used.  
        
        Signature ``GetInstanceUserAttributesAsStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteInstanceUserAttribute(self, type: NXOpen.NXObjectAttributeType, title: str, deleteEntireArray: bool, option: NXOpen.UpdateOption) -> None:
        """
        Deletes the first attribute encountered with the given Type, Title and Index.  
        
        If a candidate attribute is not an array attribute, the DeleteEntireArray input is ignored,
        otherwise the last element of the array is deleted.
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`. 
        
        Signature ``DeleteInstanceUserAttribute(type, title, deleteEntireArray, option)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param title: 
        :type title: str 
        :param deleteEntireArray: 
        :type deleteEntireArray: bool 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteInstanceUserAttributes(self, type: NXOpen.NXObjectAttributeType, option: NXOpen.UpdateOption) -> None:
        """
        Deletes the attributes encountered with the given Type with option to update or not.  
        
        NOTE: This method does not support the use of :py:class:`NXOpen.NXObjectAttributeType.Reference <NXOpen.NXObjectAttributeType>`. 
        
        Signature ``DeleteInstanceUserAttributes(type, option)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInstanceUserAttributeLock(self, title: str, type: NXOpen.NXObjectAttributeType, lock: bool) -> None:
        """
        Lock or unlock the given attribute.  
        
        For array attributes, the Title should be set to the array title, without the appended index.
        Individual array elements cannot be separately locked 
        
        Signature ``SetInstanceUserAttributeLock(title, type, lock)`` 
        
        :param title: 
        :type title: str 
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :param lock: 
        :type lock: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInstanceUserAttributeLock(self, title: str, type: NXOpen.NXObjectAttributeType) -> bool:
        """
        Determine the lock of the given attribute.  
        
        For array attributes, the Title should be set to the array title, without the appended index.
        Individual array elements cannot be separately locked  
        
        Signature ``GetInstanceUserAttributeLock(title, type)`` 
        
        :param title: 
        :type title: str 
        :param type: 
        :type type: :py:class:`NXOpen.NXObjectAttributeType` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateEmptyPartFamilyInstanceSelectionCriteria(self, family: NXOpen.PartFamily.Template) -> NXOpen.PartFamily.InstanceSelectionCriteria:
        """
        Creates an empty :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria`  
        
        Signature ``CreateEmptyPartFamilyInstanceSelectionCriteria(family)`` 
        
        :param family: 
        :type family: :py:class:`NXOpen.PartFamily.Template` 
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def GetPartFamilyInstanceSelectionCriteria(self) -> NXOpen.PartFamily.InstanceSelectionCriteria:
        """
        Obtains the:py:class:`NXOpen.PartFamily.InstanceSelectionCriteria`, if it exists.  
        
        Signature ``GetPartFamilyInstanceSelectionCriteria()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def SetPartFamilyInstanceSelectionCriteria(self, selectionCriteria: NXOpen.PartFamily.InstanceSelectionCriteria) -> None:
        """
        Hooks :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria` to this component 
        
        Signature ``SetPartFamilyInstanceSelectionCriteria(selectionCriteria)`` 
        
        :param selectionCriteria: 
        :type selectionCriteria: :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def DeletePartFamilyInstanceSelectionCriteria(self) -> None:
        """
        Deletes :py:class:`NXOpen.PartFamily.InstanceSelectionCriteria` associated with this component 
        
        Signature ``DeletePartFamilyInstanceSelectionCriteria()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: solid_modeling ("SOLIDS MODELING")
        """
        ...
    
    
    def FindComponentPatterns(self) -> tuple:
        """
        Finds :py:class:`NXOpen.Assemblies.ComponentPattern` associated with this component.  
        
        De-allocation of memory used for list of pattern definitions is responsibility of user. 
        
        Signature ``FindComponentPatterns()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (patternDefinition, patternDefinitions). patternDefinition is a :py:class:`NXOpen.Assemblies.ComponentPattern`.   A Pattern which refers 'component' as one of its output instances patternDefinitions is a list of :py:class:`NXOpen.Assemblies.ComponentPattern`.   List of patterns which refer 'component' as its master component 
        
        .. versionadded:: NX10.0.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetCharacteristics(self) -> NXOpen.Routing.CharacteristicList:
        """
        Get all of the characteristics values on the this object.  
        
        Signature ``GetCharacteristics()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetCharacteristics(self, values: NXOpen.Routing.CharacteristicList) -> None:
        """
        Set all of the characteristics values on this object.  
        
        Signature ``SetCharacteristics(values)`` 
        
        :param values: 
        :type values: :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Routing.ICharacteristic.SetCharacteristics2` instead.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetIntegerCharacteristic(self, name: str) -> int:
        """
        Get the value of an integer characteristic associated with the input name.  
        
        Signature ``GetIntegerCharacteristic(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    @typing.overload
    def SetCharacteristic(self, name: str, value: int) -> None:
        """
        Set the value of an integer characteristic associated with the input name,
        adds a new characteristic to the list if one doesn't exist already. Converts
        the type of an existing characteristic with the same name to integer if it's 
        type is not integer. 
        
        Signature ``SetCharacteristic(name, value)`` 
        
        :param name: 
        :type name: str 
        :param value: 
        :type value: int 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Routing.ICharacteristic.SetCharacteristic2` instead.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def SetCharacteristic(self, name: str, value: float) -> None:
        """
        Set the value of an real characteristic associated with the input name,
        adds a new characteristic to the list if one doesn't exist already. Converts
        the type of an existing characteristic with the same name to real if it's 
        type is not real. 
        
        Signature ``SetCharacteristic(name, value)`` 
        
        :param name: 
        :type name: str 
        :param value: 
        :type value: float 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Routing.ICharacteristic.SetCharacteristic2` instead.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def SetCharacteristic(self, name: str, value: str) -> None:
        """
        Set the value of an string characteristic associated with the input name,
        adds a new characteristic to the list if one doesn't exist already. Converts
        the type of an existing characteristic with the same name to string if it's 
        type is not string. 
        
        Signature ``SetCharacteristic(name, value)`` 
        
        :param name: 
        :type name: str 
        :param value: 
        :type value: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`NXOpen.Routing.ICharacteristic.SetCharacteristic2` instead.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetRealCharacteristic(self, name: str) -> float:
        """
        Get the value of a real characteristic associated with the input name.  
        
        Signature ``GetRealCharacteristic(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetStringCharacteristic(self, name: str) -> str:
        """
        Get the value of a string characteristic associated with the input name.  
        
        Signature ``GetStringCharacteristic(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def DeleteCharacterstics(self, values: NXOpen.Routing.CharacteristicList) -> None:
        """
        Removes the input list of characteristics from this object.  
        
        Signature ``DeleteCharacterstics(values)`` 
        
        :param values: 
        :type values: :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetDestinationCharacteristics(self) -> NXOpen.Routing.CharacteristicList:
        """
        Returns the destination characteristics from the input object.  
        
        Retrieves the description of which destination characteristics to read
        from the application view and then reads those destination 
        characteristics from the object
        
          * Ports: Reads characteristics from the port.
          * RCPs: Attempts to find a port at the RCP, reads characteristics from
        the port if it exists, otherwise reads from the
        stock associated with the rcp.
          * Segments: Reads characteristics from the stock associated with the segment.
          * Components: Reads characteristics directly from the component.
          * Stock: Reads characteristics from the stock or from the stock's data.
        
        Signature ``GetDestinationCharacteristics()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    @typing.overload
    def SetCharacteristic2(self, title: str, value: int) -> None:
        """
        Sets or creates an integer type attribute associated with the input title. 
        creating a new attribute if one doesn't exist already. 
        
        If the method is called on a stock :py:class:`Assemblies.Component`, the 
        method will create or edit a part attribute on the stock part. For legacy parts 
        where the attribute is on the stock component, the attribute will be moved 
        to the stock part. 
        
        If the method is called on a non-stock :py:class:`Assemblies.Component`, 
        the method will create or edit an attribute on the corresponding instance. For 
        legacy parts where the attribute is on the component, the attribute will be moved 
        to the corresponding instance. 
        
        If the method is called on any non-component object, the method will 
        access or create an attribute on the object itself. 
        
        Signature ``SetCharacteristic2(title, value)`` 
        
        :param title:  Unique title for the Attribute or Characteristic  
        :type title: str 
        :param value:  New Value to be set on the Attribute  
        :type value: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def SetCharacteristic2(self, title: str, value: float) -> None:
        """
        Sets or creates a double type attribute associated with the input title. 
        creating a new attribute if one doesn't exist already. 
        
        If the method is called on a stock :py:class:`Assemblies.Component`, the 
        method will create or edit a part attribute on the stock part. For legacy parts 
        where the attribute is on the stock component, the attribute will be moved 
        to the stock part. 
        
        If the method is called on a non-stock :py:class:`Assemblies.Component`, 
        the method will create or edit an attribute on the corresponding instance. For 
        legacy parts where the attribute is on the component, the attribute will be moved 
        to the corresponding instance. 
        
        If the method is called on any non-component object, the method will 
        access or create an attribute on the object itself. 
        
        Signature ``SetCharacteristic2(title, value)`` 
        
        :param title:  Unique title for the Attribute or Characteristic  
        :type title: str 
        :param value:  New Value to be set on the Attribute  
        :type value: float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def SetCharacteristic2(self, title: str, value: str) -> None:
        """
        Sets or creates a string type type attribute associated with the input title. 
        creating a new attribute if one doesn't exist already. 
        
        If the method is called on a stock :py:class:`Assemblies.Component`, the 
        method will create or edit a part attribute on the stock part. For legacy parts 
        where the attribute is on the stock component, the attribute will be moved 
        to the stock part. 
        
        If the method is called on a non-stock :py:class:`Assemblies.Component`, 
        the method will create or edit an attribute on the corresponding instance. For 
        legacy parts where the attribute is on the component, the attribute will be moved 
        to the corresponding instance. 
        
        If the method is called on any non-component object, the method will 
        access or create an attribute on the object itself. 
        
        Signature ``SetCharacteristic2(title, value)`` 
        
        :param title:  Unique title for the Attribute or Characteristic  
        :type title: str 
        :param value:  New Value to be set on the Attribute  
        :type value: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetCharacteristics2(self, values: NXOpen.Routing.CharacteristicList) -> None:
        """
        Sets all attributes associated with the titles from the input list, 
        creating new attributes for the ones that don't exist already.  
        
        If the method is called on a stock :py:class:`Assemblies.Component`, the 
        method will create or edit part attributes on the stock part. For legacy parts 
        where the attributes are on the stock component, the attributes will be moved 
        to the stock part. 
        
        If the method is called on a non-stock :py:class:`Assemblies.Component`, 
        the method will create or edit attributes on the corresponding instance. For 
        legacy parts where the attribute is on the component, the attributes will be moved 
        to the corresponding instance. 
        
        If the method is called on any non-component object, the method will 
        access or create attributes on the object itself. 
        
        Signature ``SetCharacteristics2(values)`` 
        
        :param values:  :py:class:`NXOpen.Routing.CharacteristicList` having the titles, types and values of Attributes to be set  
        :type values: :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    CollaborativeContentType: CollaborativeContentType = ...
    """
    Returns  the collaborative content type of this component.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollaborativeContentType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.CollaborativeContentType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DesignElementRevision: NXOpen.PDM.DesignElementRevision = ...
    """
    Returns  the :py:class:`NXOpen.PDM.DesignElementRevision` that corresponds to this component.  
    
    This can be None if the component is not a design element.
    This will return parent reuse design element revision if this component represent a :py:class:`NXOpen.PDM.DesignSubordinateRevision` .
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.DesignElementRevision` 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:meth:`NXOpen.Assemblies.Component.ModelElementRevision` instead.
    
    License requirements: None.
    """
    DesignSubordinateRevision: NXOpen.PDM.DesignSubordinateRevision = ...
    """
    Returns  the :py:class:`NXOpen.PDM.DesignSubordinateRevision` that corresponds to this component.  
    
    This can be None if the component is not a subordinate design element.
    
    <hr>
    
    Getter Method
    
    Signature ``DesignSubordinateRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.DesignSubordinateRevision` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DirectOwner: ComponentAssembly = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.ComponentAssembly` which owns this component as a "Top Level" component.  
    
    For components in a multi-level assembly, this is NOT the same the part that owns this component object. 
    I.e. it is not the same as calling:
    
    NXOpen.NXObject.OwningPart:py:meth:`NXOpen.NXObject.OwningPart`()
    
    NXOpen.BasePart.ComponentAssembly:py:meth:`NXOpen.BasePart.ComponentAssembly`()
    
    <hr>
    
    Getter Method
    
    Signature ``DirectOwner`` 
    
    :returns:  The owning ComponentAssembly  
    :rtype: :py:class:`NXOpen.Assemblies.ComponentAssembly` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    DisplayName: str = ...
    """
    Returns  the displayable name of the prototype part.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayName`` 
    
    :returns:  The displayable name of the prototype part  
    :rtype: str 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    EmptyPartRefsetName: str = ...
    """
    Returns  the name of the reference set which represents the empty set.  
    
    This
    can be used as a parameter to :py:meth:`NXOpen.Assemblies.ComponentAssembly.ReplaceReferenceSet`.
    
    <hr>
    
    Getter Method
    
    Signature ``EmptyPartRefsetName`` 
    
    :returns:  The name of the "Empty" reference set  
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    EntirePartRefsetName: str = ...
    """
    Returns  the name of the reference set which represents the entire part.  
    
    This
    can be used as a parameter to :py:meth:`NXOpen.Assemblies.ComponentAssembly.ReplaceReferenceSet`.
    
    <hr>
    
    Getter Method
    
    Signature ``EntirePartRefsetName`` 
    
    :returns:  The name of the "Entire Part" reference set  
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    FixConstraint: NXOpen.Positioning.ComponentConstraint = ...
    """
    Returns  a fix :py:class:`NXOpen.Positioning.ComponentConstraint` of this component.  
    
    The constraint may be suppressed or None.  If the part 
    controlling the position of this component is not loaded then None
    will be returned.
    
    <hr>
    
    Getter Method
    
    Signature ``FixConstraint`` 
    
    :returns:  A fix constraint  
    :rtype: :py:class:`NXOpen.Positioning.ComponentConstraint` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsFixed: bool = ...
    """
    Returns  the fixed state of this component.  
    
    True if there is an unsuppressed
    :py:class:`NXOpen.Positioning.ComponentConstraint` fix constraint on this component
    and false otherwise.  If the part controlling the position of this
    component is not loaded then false will be returned.
    
    <hr>
    
    Getter Method
    
    Signature ``IsFixed`` 
    
    :returns:  True if the component is fixed, false otherwise  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsSuppressed: bool = ...
    """
    Returns 
    the suppressed state of the component in its controlling arrangement.  
    
    (See :py:meth:`NXOpen.Assemblies.Component.SuppressingArrangement`.)
    
    <hr>
    
    Getter Method
    
    Signature ``IsSuppressed`` 
    
    :returns:  True if the component is suppressed, false otherwise  
    :rtype: bool 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ModelElementRevision: NXOpen.PDM.ModelElementRevision = ...
    """
    Returns  the :py:class:`NXOpen.PDM.ModelElementRevision` that corresponds to this component.  
    
    This can be None if the component is not a model element.
    This will return parent reuse design element revision if this component represent a :py:class:`NXOpen.PDM.DesignSubordinateRevision` .
    If component is independent design feature then this will return :py:class:`NXOpen.PDM.DesignFeatureRevision`.
    
    <hr>
    
    Getter Method
    
    Signature ``ModelElementRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ModelElementRevision` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    Parent: Component = ...
    """
    Returns  the parent of the component.  
    
    For the root component of an assembly, this
    will be None. See :py:meth:`NXOpen.Assemblies.ComponentAssembly.RootComponent`.
    
    <hr>
    
    Getter Method
    
    Signature ``Parent`` 
    
    :returns:  The parent component  
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    ReferenceSet: str = ...
    """
    Returns  
    the name of the reference set used for this component
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSet`` 
    
    :returns:  The name of the component's reference set  
    :rtype: str 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Subset: Subset = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.Subset` that corresponds to this component.  
    
    This can be None if the component is not a subset. 
    
    <hr>
    
    Getter Method
    
    Signature ``Subset`` 
    
    :returns:  The subset  
    :rtype: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SuppressingArrangement: Arrangement = ...
    """
    Returns 
    the :py:class:`NXOpen.Assemblies.Arrangement` that controls this component's
    suppression state.  
    
    The controlling Arrangement will be defined in a
    :py:class:`NXOpen.Assemblies.ComponentAssembly` in the tree above this Component.
    
    Note: In the current release, Arrangements are only used for controlling a
    component's suppression state. In future releases, further attributes will be
    controlled via Arrangements.
    
    <hr>
    
    Getter Method
    
    Signature ``SuppressingArrangement`` 
    
    :returns:  The :py:class:`NXOpen.Assemblies.Arrangement` controlling this component's
    suppression state. This will be None if the assembly containing the
    arrangement is not loaded. 
    :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UsedArrangement: Arrangement = ...
    """
    Returns 
    the Arrangement used for this component.  
    
    See :py:meth:`NXOpen.Assemblies.Component.SetUsedArrangement`
    
    <hr>
    
    Getter Method
    
    Signature ``UsedArrangement`` 
    
    :returns:  The Arrangement used for this component. This will be None
    if the component does not have any children.
    
    :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: Component = ...  # unknown typename


class DegreesOfFreedom():
    """
    Structure used to report the Degrees of Freedom of a component.  
    
    If there is one rational degrees of freedom then axis is determined by base_point1
    and rotation_direction1. 
    If there are 2 rotational degrees of freedom then one axis is determined by base_point1
    and rotation_direction1 and the other by base_point2 and rotation_direction2.
    If there are 3 rotational degrees of freedom then the fixed point for the rotations
    is in base_point1 and there is no axis direction given.
    The translational degrees of freedom are given in translation_direction1 and
    translation_direction2, with the possibility that one of these may be a "normal" 
    to 2 degrees of freedom, as specified in the associated status. .
    Constructor: 
    NXOpen.Assemblies.DegreesOfFreedom()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Result: DegreesOfFreedomResult = ...
    """
    The success or otherwise of the degrees of freedom calculation 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomResult`
    """
    NumRotational: int = ...
    """
    Number of static and free rotational degrees of freedom.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumTranslational: int = ...
    """
    Number of static and free translational degrees of freedom.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumInstantaneousRotational: int = ...
    """
    Number of instantaneous rotational degrees of freedom.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumInstantaneousTranslational: int = ...
    """
    Number of instantaneous translational degrees of freedom.  
    
    <hr>
    
    Field Value
    Type:int
    """
    BasePoint1Status: DegreesOfFreedomStatus = ...
    """
    First rotation base point status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    BasePoint1: NXOpen.Point3d = ...
    """
    First rotation base point.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    RotationDirection1Status: DegreesOfFreedomStatus = ...
    """
    First rotation direction status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    RotationDirection1: NXOpen.Vector3d = ...
    """
    First rotation direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    BasePoint2Status: DegreesOfFreedomStatus = ...
    """
    Second rotation base point status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    BasePoint2: NXOpen.Point3d = ...
    """
    Second rotation base point.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    RotationDirection2Status: DegreesOfFreedomStatus = ...
    """
    Second rotation direction status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    RotationDirection2: NXOpen.Vector3d = ...
    """
    Second rotation direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    TranslationDirection1Status: DegreesOfFreedomStatus = ...
    """
    First translation direction status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    TranslationDirection1: NXOpen.Vector3d = ...
    """
    First translation direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    TranslationDirection2Status: DegreesOfFreedomStatus = ...
    """
    Second translation direction status.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.DegreesOfFreedomStatus`
    """
    TranslationDirection2: NXOpen.Vector3d = ...
    """
    Second translation direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """


class ClearanceSetSummary_Struct():
    """
    Summary of the most recent Clearance Analysis results .  
    
    Constructor: 
    NXOpen.Assemblies.ClearanceSet.Summary()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    StartTime: int = ...
    """
    The starting time of the last
    analysis run (in seconds since
    00:00:00 1/1/1970.  
    
    <hr>
    
    Field Value
    Type:int
    """
    EndTime: int = ...
    """
    The ending time of the last
    analysis run (in seconds since
    00:00:00 1/1/1970.  
    
    <hr>
    
    Field Value
    Type:int
    """
    RunTime: int = ...
    """
    the total analysis time (in secs.  
    
    ) 
    <hr>
    
    Field Value
    Type:int
    """
    Version: int = ...
    """
    The version of this analysis run.  
    
    This is a positive number.
    
    <hr>
    
    Field Value
    Type:int
    """
    AnalysisMode: ClearanceAnalysisBuilderCalculationMethodType = ...
    """
    The analysis mode.  
    
    One of
    :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.Lightweight <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`,
    :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.ExactifLoaded <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`,
    :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.Exact <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`.
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType`
    """
    NumCollections: int = ...
    """
    Number of collections analyzed.  
    
    Can be either 1 or 2.
    
    <hr>
    
    Field Value
    Type:int
    """
    NumCollection1: int = ...
    """
    The number of objects in collection 1.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumCollection2: int = ...
    """
    The number of objects in collection 2.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumPairs: int = ...
    """
    The number of pairs built from
    the object collections.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumExcludedPairs: int = ...
    """
    The number of pairs that were
    excluded from analysis, either
    due to exclusion rules or
    explicit pair exclusion.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumChangedPairs: int = ...
    """
    The number of pairs that had
    changed since the previous
    clearance analysis.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumChangedObjs: int = ...
    """
    The number of objects that had
    changed since the previous
    clearance analysis.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumCheckedPairs: int = ...
    """
    The total number of pairs that
    underwent analysis.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumNewHard: int = ...
    """
    The total number of new hard
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumNewSoft: int = ...
    """
    The total number of new soft
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumNewTouching: int = ...
    """
    The total number of new touching
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumNewContainment: int = ...
    """
    The total number of new containment
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumNewAllInterf: int = ...
    """
    The total number of new
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumHard: int = ...
    """
    The total number of hard
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumSoft: int = ...
    """
    The total number of soft
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumTouching: int = ...
    """
    The total number of touching
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumContainment: int = ...
    """
    The total number of containment
    interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    NumAllInterf: int = ...
    """
    The total number of interferences.  
    
    <hr>
    
    Field Value
    Type:int
    """
    JobStatus: ClearanceSetJobStatus = ...
    """
    Indicates if the analysis was
    aborted.  
    
    Valid values are
    :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.NotAborted <NXOpen.Assemblies.ClearanceSetJobStatus>`,
    :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.AbortedByUser <NXOpen.Assemblies.ClearanceSetJobStatus>` and
    :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.AbortedOnError <NXOpen.Assemblies.ClearanceSetJobStatus>`.
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Assemblies.ClearanceSetJobStatus`
    """
    NumZones: int = ...
    """
    The number of assembly zones used
    by the analysis (batch only).  
    
    <hr>
    
    Field Value
    Type:int
    """


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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
        
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
        
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection1: :py:class:`NXOpen.Assemblies.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1:  first selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
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
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
        
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
        :rtype: A tuple consisting of (selection, view, point). selection is a :py:class:`NXOpen.Assemblies.Component`.   selected object view is a :py:class:`NXOpen.View`.   selected object viewpoint is a :py:class:`NXOpen.Point3d`.   selected object point
        
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
        :rtype: A tuple consisting of (snapType, selection1, view1, point1, selection2, view2, point2). snapType is a :py:class:`NXOpen.InferSnapTypeSnapType`.    snap point typeselection1 is a :py:class:`NXOpen.Assemblies.Component`.   first selected object view1 is a :py:class:`NXOpen.View`.   first selected object viewpoint1 is a :py:class:`NXOpen.Point3d`.   first selected object pointselection2 is a :py:class:`NXOpen.Assemblies.Component`.   second selected object view2 is a :py:class:`NXOpen.View`.   second selected object viewpoint2 is a :py:class:`NXOpen.Point3d`.   second selected object point
        
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
        :rtype: A tuple consisting of (selection, caeSubType, caeSubId). selection is a :py:class:`NXOpen.Assemblies.Component`.   selected object caeSubType is a :py:class:`NXOpen.CaeObjectTypeCaeSubType`.   CAE set object sub typecaeSubId is a int.   CAE set object sub id
        
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
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param selection:  selected object  
    :type selection: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectComponent = ...  # unknown typename


class CreateNewComponentBuilderComponentReferenceSetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateNewComponentBuilderComponentReferenceSetType():
    """
    Set the reference set 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Model", "Set the reference set to model"
       "EntirePartOnly", "Set the reference set to entire part only"
       "Other", "Set the reference to other"
    """
    Model = 0  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
    EntirePartOnly = 1  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
    Other = 2  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
    
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
    


class CreateNewComponentBuilderComponentLayerOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateNewComponentBuilderComponentLayerOptionType():
    """
    Set the layer option type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Original", "Set the layer option type to original"
       "Work", "Set the layer option type to work"
       "AsSpecified", "Set the layer option type to as specified"
    """
    Original = 0  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
    Work = 1  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
    AsSpecified = 2  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
    
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
    


class CreateNewComponentBuilderComponentOriginTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateNewComponentBuilderComponentOriginType():
    """
    Set the cam component type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Wcs", "Set the origin type to wcs"
       "Absolute", "Set the origin type to absolute"
    """
    Wcs = 0  # CreateNewComponentBuilderComponentOriginTypeMemberType
    Absolute = 1  # CreateNewComponentBuilderComponentOriginTypeMemberType
    
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
    


class CreateNewComponentBuilderComponentCamTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CreateNewComponentBuilderComponentCamType():
    """
    Set the origin type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Target", "Set the origin type to target"
       "Resource", "Set the component type to resource"
       "Workpiece", "Set the component type to workpiece"
    """
    Target = 0  # CreateNewComponentBuilderComponentCamTypeMemberType
    Resource = 1  # CreateNewComponentBuilderComponentCamTypeMemberType
    Workpiece = 2  # CreateNewComponentBuilderComponentCamTypeMemberType
    
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
    


class CreateNewComponentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.CreateNewComponentBuilder` builder class.  
    
    Input to this class can be PSM facet objects.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateNewComponentBuilder`
    
    Default values.
    
    =======================  =========
    Property                 Value
    =======================  =========
    ComponentCam             Target 
    -----------------------  ---------
    ComponentOrigin          Wcs 
    -----------------------  ---------
    DefiningObjectsAdded     1 
    -----------------------  ---------
    LayerNumber              1 
    -----------------------  ---------
    LayerOption              Original 
    -----------------------  ---------
    OriginalObjectsDeleted   1 
    -----------------------  ---------
    ReferenceSet             Model 
    =======================  =========
    
    .. versionadded:: NX6.0.0
    """
    
    class ComponentReferenceSetType():
        """
        Set the reference set 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Model", "Set the reference set to model"
           "EntirePartOnly", "Set the reference set to entire part only"
           "Other", "Set the reference to other"
        """
        Model = 0  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
        EntirePartOnly = 1  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
        Other = 2  # CreateNewComponentBuilderComponentReferenceSetTypeMemberType
        
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
        
    
    
    class ComponentLayerOptionType():
        """
        Set the layer option type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Original", "Set the layer option type to original"
           "Work", "Set the layer option type to work"
           "AsSpecified", "Set the layer option type to as specified"
        """
        Original = 0  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
        Work = 1  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
        AsSpecified = 2  # CreateNewComponentBuilderComponentLayerOptionTypeMemberType
        
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
        
    
    
    class ComponentOriginType():
        """
        Set the cam component type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Wcs", "Set the origin type to wcs"
           "Absolute", "Set the origin type to absolute"
        """
        Wcs = 0  # CreateNewComponentBuilderComponentOriginTypeMemberType
        Absolute = 1  # CreateNewComponentBuilderComponentOriginTypeMemberType
        
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
        
    
    
    class ComponentCamType():
        """
        Set the origin type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Target", "Set the origin type to target"
           "Resource", "Set the component type to resource"
           "Workpiece", "Set the component type to workpiece"
        """
        Target = 0  # CreateNewComponentBuilderComponentCamTypeMemberType
        Resource = 1  # CreateNewComponentBuilderComponentCamTypeMemberType
        Workpiece = 2  # CreateNewComponentBuilderComponentCamTypeMemberType
        
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
        
    
    ComponentCam: CreateNewComponentBuilderComponentCamType = ...
    """
    Returns or sets  the cam component cam type 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentCam`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentCamType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentCam`` 
    
    :param componentCam: 
    :type componentCam: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentCamType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ComponentOrigin: CreateNewComponentBuilderComponentOriginType = ...
    """
    Returns or sets  the component origin 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentOriginType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentOrigin`` 
    
    :param componentOrigin: 
    :type componentOrigin: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentOriginType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DefiningObjectsAdded: bool = ...
    """
    Returns or sets  the defining objects added toggle
    
    <hr>
    
    Getter Method
    
    Signature ``DefiningObjectsAdded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DefiningObjectsAdded`` 
    
    :param definingObjectsAdded: 
    :type definingObjectsAdded: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LayerNumber: int = ...
    """
    Returns or sets  the layer number 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerNumber`` 
    
    :param layerNumber: 
    :type layerNumber: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LayerOption: CreateNewComponentBuilderComponentLayerOptionType = ...
    """
    Returns or sets  the layer option 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentLayerOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerOption`` 
    
    :param layerOption: 
    :type layerOption: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentLayerOptionType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NewComponentName: str = ...
    """
    Returns or sets  the new component name 
    
    <hr>
    
    Getter Method
    
    Signature ``NewComponentName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NewComponentName`` 
    
    :param newComponentName: 
    :type newComponentName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NewFile: NXOpen.FileNew = ...
    """
    Returns or sets  the file new object is get and set 
    
    <hr>
    
    Getter Method
    
    Signature ``NewFile`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FileNew` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NewFile`` 
    
    :param fileNew: 
    :type fileNew: :py:class:`NXOpen.FileNew` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ObjectForNewComponent: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the objects for select block 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectForNewComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    OriginalObjectsDeleted: bool = ...
    """
    Returns or sets  the original objects deleted 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginalObjectsDeleted`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginalObjectsDeleted`` 
    
    :param originalObjectsDeleted: 
    :type originalObjectsDeleted: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReferenceSet: CreateNewComponentBuilderComponentReferenceSetType = ...
    """
    Returns or sets  the reference set 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSet`` 
    
    :returns:  Get the reference set  
    :rtype: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentReferenceSetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSet`` 
    
    :param referenceSet:  Get the reference set  
    :type referenceSet: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilderComponentReferenceSetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReferenceSetName: str = ...
    """
    Returns or sets  the reference set name.  
    
    This should be used when reference set type is set to other
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSetName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSetName`` 
    
    :param referenceSetName: 
    :type referenceSetName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: CreateNewComponentBuilder = ...  # unknown typename


class SearchResultElement(NXOpen.NXObject):
    """
    A search result element can be produced as the result of a search performed in the context of a :py:class:`NXOpen.Assemblies.SubsetBuilder`.  
    
    They can be found through :py:meth:`NXOpen.Assemblies.SubsetBuilder.SearchResults`.
    
    Instances of this object can be accessed through :py:meth:`NXOpen.Assemblies.SubsetBuilder.SearchResults`.
    
    .. versionadded:: NX8.5.0
    """
    ModelElementRevision: NXOpen.PDM.ModelElementRevision = ...
    """
    Returns 
    the underlying design model revision associated with this search element.  
    
    <hr>
    
    Getter Method
    
    Signature ``ModelElementRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ModelElementRevision` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SearchResultElement = ...  # unknown typename


class SearchTermSearchTermLogicTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SearchTermSearchTermLogicType():
    """
    Logic used to determine how a search term is used within a recipe.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Include", "Include results found by this search term"
       "Exclude", "Exclude results found by this search term"
       "Filter", "Filter using results found by this search term"
    """
    Include = 0  # SearchTermSearchTermLogicTypeMemberType
    Exclude = 1  # SearchTermSearchTermLogicTypeMemberType
    Filter = 2  # SearchTermSearchTermLogicTypeMemberType
    
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
    


class SearchTerm(NXOpen.NXObject):
    """
    A search term is used to specify a search for the contents of a :py:class:`NXOpen.Assemblies.Subset`.  
    
    It is an element of a :py:class:`NXOpen.Assemblies.SubsetRecipe`.
    
    Subclasses of this class can be created by :py:class:`NXOpen.Assemblies.SubsetRecipe`
    
    .. versionadded:: NX8.5.0
    """
    
    class SearchTermLogicType():
        """
        Logic used to determine how a search term is used within a recipe.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Include", "Include results found by this search term"
           "Exclude", "Exclude results found by this search term"
           "Filter", "Filter using results found by this search term"
        """
        Include = 0  # SearchTermSearchTermLogicTypeMemberType
        Exclude = 1  # SearchTermSearchTermLogicTypeMemberType
        Filter = 2  # SearchTermSearchTermLogicTypeMemberType
        
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
        
    
    Null: SearchTerm = ...  # unknown typename


class ArrangementCollection(NXOpen.TaggedObjectCollection):
    """
    a collection of arrangements   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX3.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def Create(self, templateArrangement: Arrangement, name: str) -> Arrangement:
        """
        Creates a standard :py:class:`NXOpen.Assemblies.Arrangement`, based on an existing standard :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        Note that any :py:class:`NXOpen.Assemblies.ComponentAssembly` that contains components will have at least one standard :py:class:`NXOpen.Assemblies.Arrangement`. 
        
        See :py:meth:`Assemblies.ComponentAssembly.ActiveArrangement`.
        
        Note that the existing :py:class:`NXOpen.Assemblies.Arrangement` must not be isolated.
        
        Signature ``Create(templateArrangement, name)`` 
        
        :param templateArrangement:  The original :py:class:`NXOpen.Assemblies.Arrangement`. The new :py:class:`NXOpen.Assemblies.Arrangement` will be copied from this.  This :py:class:`NXOpen.Assemblies.Arrangement` must not be isolated.  
        :type templateArrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :param name:  The name of the new arrangement 
        :type name: str 
        :returns:  The new arrangement  
        :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateIsolated(self, templateArrangement: Arrangement, name: str) -> Arrangement:
        """
        Creates an isolated :py:class:`NXOpen.Assemblies.Arrangement`, based on an existing :py:class:`NXOpen.Assemblies.Arrangement` :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        Note that any :py:class:`NXOpen.Assemblies.ComponentAssembly` that contains components will have at least one standard :py:class:`NXOpen.Assemblies.Arrangement`. 
        
        See :py:meth:`Assemblies.ComponentAssembly.ActiveArrangement`.
        
        Note that the existing :py:class:`NXOpen.Assemblies.Arrangement` must not be isolated.
        
        Signature ``CreateIsolated(templateArrangement, name)`` 
        
        :param templateArrangement:  The original :py:class:`NXOpen.Assemblies.Arrangement`. This :py:class:`NXOpen.Assemblies.Arrangement` must not be isolated.  
        :type templateArrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :param name:  The name of the new :py:class:`NXOpen.Assemblies.Arrangement`. 
        :type name: str 
        :returns:  The new :py:class:`NXOpen.Assemblies.Arrangement`. 
        :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Arrangement:
        """
        Finds the :py:class:`NXOpen.Assemblies.Arrangement` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Name of the arrangement to be found  
        :type journalIdentifier: str 
        :returns:  Arrangement found, or null if no such arrangement exists. 
        :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    


class ExplicitSearchTerm(SearchTerm):
    """
    A :py:class:`NXOpen.Assemblies.SubsetRecipe` search term that refers explicitly to
    a design element.  
    
    To create an instance of this object use :py:meth:`NXOpen.Assemblies.SubsetRecipe.CreateExplicitSearchTerm`
    
    .. versionadded:: NX8.5.0
    """
    SearchResultElement: SearchResultElement = ...
    """
    Returns  the search result element of this search term.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchResultElement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchResultElement` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: ExplicitSearchTerm = ...  # unknown typename


class AssembliesEventTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesEventTypes():
    """
    NX Event types
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BrowserUpdate", "update all relations in the browser event"
       "DeselectAll", "deselect all that is currently selected event"
       "PartSelectAll", "select all parts event"
       "PartDeselectAll", "deselect all parts event"
       "PartSelect", "select specified parts event"
       "PartDeselect", "deselect specified parts event"
       "PartFullyLoad", "part fully load event"
       "PartMakeDisplayed", "part make displayed part event"
       "PartMakeWork", "part make work part event"
       "LinkedObjectSelectAll", "select all linked objects event"
       "LinkedObjectDeselectAll", "deselect all linked objects event"
       "LinkedObjectSelect", "select specified linked objects event"
       "LinkedObjectDeselect", "deselect specified linked objects event"
       "LinkedFeatureEdit", "linked feature edit event"
       "LinkedFeatureBreak", "linked feature break event"
       "LinkedFeatureAcceptBroken", "linked feature accept broken event"
       "Launch", "browser successfully launched event"
       "Exit", "browser exit event"
    """
    BrowserUpdate = 0  # AssembliesEventTypesMemberType
    DeselectAll = 1  # AssembliesEventTypesMemberType
    PartSelectAll = 2  # AssembliesEventTypesMemberType
    PartDeselectAll = 3  # AssembliesEventTypesMemberType
    PartSelect = 4  # AssembliesEventTypesMemberType
    PartDeselect = 5  # AssembliesEventTypesMemberType
    PartFullyLoad = 6  # AssembliesEventTypesMemberType
    PartMakeDisplayed = 7  # AssembliesEventTypesMemberType
    PartMakeWork = 8  # AssembliesEventTypesMemberType
    LinkedObjectSelectAll = 9  # AssembliesEventTypesMemberType
    LinkedObjectDeselectAll = 10  # AssembliesEventTypesMemberType
    LinkedObjectSelect = 11  # AssembliesEventTypesMemberType
    LinkedObjectDeselect = 12  # AssembliesEventTypesMemberType
    LinkedFeatureEdit = 13  # AssembliesEventTypesMemberType
    LinkedFeatureBreak = 14  # AssembliesEventTypesMemberType
    LinkedFeatureAcceptBroken = 15  # AssembliesEventTypesMemberType
    Launch = 16  # AssembliesEventTypesMemberType
    Exit = 17  # AssembliesEventTypesMemberType
    
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
    


class DrawingExplosion(NXOpen.NXObject):
    """
    Represents an explosion used in a drawing view of an arrangement.  
    
    Cannot be user created.
    
    .. versionadded:: NX12.0.0
    """
    RootComponent: ExplodedComponent = ...
    """
    Returns  the root component of the drawing explosion.  
    
    The root component is the exploded component at the top of the exploded component
    tree. The exploded component tree has the same structure as that of the component tree in :py:class:`NXOpen.Assemblies.ComponentAssembly`.
    
    <hr>
    
    Getter Method
    
    Signature ``RootComponent`` 
    
    :returns:  The :py:class:`NXOpen.Assemblies.ExplodedComponent` at the root of this Drawing Explosion  
    :rtype: :py:class:`NXOpen.Assemblies.ExplodedComponent` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: DrawingExplosion = ...  # unknown typename


class ComponentQuantityMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentQuantity():
    """
    Represents the component quantity type of the component 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No quantity"
       "Integer", "Integer quantity"
       "Real", "Real quantity"
       "AsRequired", "Quantity As required."
    """
    NotSet = 0  # ComponentQuantityMemberType
    Integer = 1  # ComponentQuantityMemberType
    Real = 2  # ComponentQuantityMemberType
    AsRequired = 3  # ComponentQuantityMemberType
    
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
    


class MakeUniquePartBuilderOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MakeUniquePartBuilderOption():
    """
    Represents possible copy assembly options for unique part   
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CopyAssemblyOnly", " - "
    """
    CopyAssemblyOnly = 0  # MakeUniquePartBuilderOptionMemberType
    
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
    


class MakeUniquePartBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.MakeUniquePartBuilder` builder.  
    
    Input to this class can be PSM facet objects.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateMakeUniquePartBuilder`
    
    Default values.
    
    ============  =================
    Property      Value
    ============  =================
    CopyChoices   CopyAssemblyOnly 
    ============  =================
    
    .. versionadded:: NX8.0.0
    """
    
    class Option():
        """
        Represents possible copy assembly options for unique part   
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CopyAssemblyOnly", " - "
        """
        CopyAssemblyOnly = 0  # MakeUniquePartBuilderOptionMemberType
        
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
        
    
    CopyChoices: MakeUniquePartBuilderOption = ...
    """
    Returns or sets  the copy choices returned.  
    
    <hr>
    
    Getter Method
    
    Signature ``CopyChoices`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.MakeUniquePartBuilderOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``CopyChoices`` 
    
    :param copyChoices: 
    :type copyChoices: :py:class:`NXOpen.Assemblies.MakeUniquePartBuilderOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectedComponents: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected components to be made unique are returned.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedComponents`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: MakeUniquePartBuilder = ...  # unknown typename


class AssembliesParameterPropertiesBuilderArrangementOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesParameterPropertiesBuilderArrangementOptions():
    """
    The positioning mixture status options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "IndividuallyPositioned", "All components are varied"
       "SamePositionInAll", "All components are unvaried"
       "Mixed", "All components are neither varied nor unvaried"
    """
    IndividuallyPositioned = 0  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
    SamePositionInAll = 1  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
    Mixed = 2  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
    
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
    


class AssembliesParameterPropertiesBuilder(NXOpen.Builder):
    """
    Represents an :py:class:`NXOpen.Assemblies.AssembliesParameterPropertiesBuilder` to be used for changing the
    name or modifying the positioning mixture status of a component.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PropertiesManager.CreateAssembliesParameterPropertiesBuilder`
    
    Default values.
    
    =============  =======================
    Property       Value
    =============  =======================
    Arrangements   IndividuallyPositioned 
    =============  =======================
    
    .. versionadded:: NX8.0.0
    """
    
    class ArrangementOptions():
        """
        The positioning mixture status options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "IndividuallyPositioned", "All components are varied"
           "SamePositionInAll", "All components are unvaried"
           "Mixed", "All components are neither varied nor unvaried"
        """
        IndividuallyPositioned = 0  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
        SamePositionInAll = 1  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
        Mixed = 2  # AssembliesParameterPropertiesBuilderArrangementOptionsMemberType
        
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
        
    
    Arrangements: AssembliesParameterPropertiesBuilderArrangementOptions = ...
    """
    Returns or sets  the arrangements.  
    
    The positioning mixture status for the selected components.
    No action will take place if Mixed is set as the arrangement option. 
    
    <hr>
    
    Getter Method
    
    Signature ``Arrangements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.AssembliesParameterPropertiesBuilderArrangementOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``Arrangements`` 
    
    :param arrangements: 
    :type arrangements: :py:class:`NXOpen.Assemblies.AssembliesParameterPropertiesBuilderArrangementOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectedObjects: SelectComponentList = ...
    """
    Returns  the selected object(s) list.  
    
    This is the active list of components that will be
    modified by any parameter changes. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: AssembliesParameterPropertiesBuilder = ...  # unknown typename


class PartitionScheme(NXOpen.NXObject):
    """
    A partition scheme is a Teamcenter object in a Collaborative Design.  
    
    A partition scheme 
    contains partitions.
    
    Instances of this object can be accessed through :py:class:`CollaborativeDesign`.
    
    .. versionadded:: NX8.5.0
    """
    
    def GetRootPartitions(self) -> 'list[Partition]':
        """
        Get the root partitions of partition scheme.  
        
        Signature ``GetRootPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    CollaborativeDesign: NXOpen.CollaborativeDesign = ...
    """
    Returns 
    the owning collaborative design.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollaborativeDesign`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: PartitionScheme = ...  # unknown typename


class ComponentPatternBuilder(NXOpen.Builder):
    """
    Represents a builder class that performs various :py:class:`NXOpen.Assemblies.ComponentPattern` operations.  
    
    Input to this class can be PSM facet objects.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ComponentAssembly.CreateComponentPatternBuilder`
    
    Default values.
    
    =====================================================================  ==========================================
    Property                                                               Value
    =====================================================================  ==========================================
    PatternService.AlongPathDefinition.XOnPathSpacing.NCopies.Value        2 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.XOnPathSpacing.SpaceType            Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.XPathOption                         Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YDirectionOption                    Section 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YOnPathSpacing.NCopies.Value        1 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YPathOption                         Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YSpacing.NCopies.Value              1 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YSpacing.PitchDistance.Value        10 (millimeters part), 1 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YSpacing.SpaceType                  Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.AlongPathDefinition.YSpacing.SpanDistance.Value         100 (millimeters part), 10 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.NCopies.Value         12 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.PitchAngle.Value      30 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.PitchDistance.Value   10 (millimeters part), 1 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.SpaceType             Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.SpanAngle.Value       360 (millimeters part), 360 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.AngularSpacing.UsePitchOption        Angle 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.CreateLastStaggered                  true 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.HorizontalRef.RotationAngle.Value    0 (millimeters part), 0 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.IncludeSeedToggle                    true 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.RadialSpacing.NCopies.Value          1 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.CircularDefinition.StaggerType                          None 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.AnglePitch.Value                        30 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.CountOfInstances.Value                  6 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.DirectionType                           Righthand 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.DistancePitch.Value                     10 (millimeters part), 0.4 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.HelixPitch.Value                        50 (millimeters part), 2 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.HelixSpan.Value                         100 (millimeters part), 4 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.NumberOfTurns.Value                     2 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.HelixDefinition.SizeOption                              CountAngleDistance 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternFill.FillMargin.Value                            0 (millimeters part), 0 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternFill.FillOptions                                 None 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternFill.SimplifiedBoundaryToggle                    False 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.AlongOrientationOption               NormalToPath 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.CircularOrientationOption            FollowPattern 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.FollowFaceProjDirOption              PatternPlaneNormal 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.GeneralOrientationOption             Fixed 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.HelixOrientationOption               FollowPattern 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.LinearOrientationOption              Fixed 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.MirrorOrientationOption              FollowPattern 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.OrientationOption                    Fixed 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.PolygonOrientationOption             FollowPattern 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternOrientation.SpiralOrientationOption              FollowPattern 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PatternType                                             Linear 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.NumberOfSides.Value                   6 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.PolygonSizeOption                     Inscribed 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.PolygonSpacing.NCopies.Value          4 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.PolygonSpacing.PitchDistance.Value    25 (millimeters part), 1 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.PolygonSpacing.SpaceType              Offset 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.PolygonSpacing.SpanAngle.Value        360 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.RadialSpacing.NCopies.Value           1 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.RadialSpacing.PitchDistance.Value     25 (millimeters part), 1 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.PolygonDefinition.RadialSpacing.SpanDistance.Value      100 (millimeters part), 4 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.RectangularDefinition.CreateLastStaggered               true 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.RectangularDefinition.SimplifiedLayoutType              Square 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.RectangularDefinition.StaggerType                       None 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.RectangularDefinition.XSpacing.NCopies.Value            2 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.RectangularDefinition.YSpacing.NCopies.Value            1 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.SpiralDefinition.DirectionType                          Lefthand 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.SpiralDefinition.NumberOfTurns.Value                    1 (millimeters part), 1 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.SpiralDefinition.RadialPitch.Value                      50 (millimeters part), 2 (inches part) 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.SpiralDefinition.SizeSpiralType                         NumberOfTurns 
    ---------------------------------------------------------------------  ------------------------------------------
    PatternService.SpiralDefinition.TotalAngle.Value                       360 (millimeters part), 360 (inches part) 
    =====================================================================  ==========================================
    
    .. versionadded:: NX9.0.0
    """
    
    def GetDynamicPositioning(self) -> bool:
        """
        Returns the dynamic positioning flag.  
        
        Signature ``GetDynamicPositioning()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDynamicPositioning(self, isDynamicPositioning: bool) -> None:
        """
        Sets the dynamic positioning flag.  
        
        It will enable or disable the dynamic preview of the components. 
        
        Signature ``SetDynamicPositioning(isDynamicPositioning)`` 
        
        :param isDynamicPositioning: 
        :type isDynamicPositioning: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetObject(self, compPattern: ComponentPattern) -> None:
        """
        Sets the object selected for pattern definition 
        
        Signature ``SetObject(compPattern)`` 
        
        :param compPattern:  The pattern definition object  
        :type compPattern: :py:class:`NXOpen.Assemblies.ComponentPattern` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Associative: bool = ...
    """
    Returns or sets  the option to specify whether the :py:class:`NXOpen.Assemblies.ComponentPattern` is 
    associative or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param isAssociative: 
    :type isAssociative: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentPatternSet: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.Component` for pattern.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentPatternSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CopyConstraintPattern: bool = ...
    """
    Returns or sets  the copy constraint option.  
    
    The copy constraint type of pattern is created 
    when this option is enabled otherwise Pure Reference pattern is created.
    
    <hr>
    
    Getter Method
    
    Signature ``CopyConstraintPattern`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CopyConstraintPattern`` 
    
    :param isCopyConstraintReferencePattern: 
    :type isCopyConstraintReferencePattern: bool 
    
    .. versionadded:: NX9.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    PatternService: NXOpen.GeometricUtilities.PatternDefinition = ...
    """
    Returns  the :py:class:`NXOpen.GeometricUtilities.PatternDefinition`.  
    
    <hr>
    
    Getter Method
    
    Signature ``PatternService`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.PatternDefinition` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ComponentPatternBuilder = ...  # unknown typename


class ShowComponentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.ShowComponentBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateShowComponentBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Components: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the components to show 
    
    <hr>
    
    Getter Method
    
    Signature ``Components`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Views: NXOpen.Drawings.SelectDraftingViewList = ...
    """
    Returns  the drafting views 
    
    <hr>
    
    Getter Method
    
    Signature ``Views`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingViewList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: ShowComponentBuilder = ...  # unknown typename


class UpdateStructureBuilder(NXOpen.Builder):
    """
    Represents a builder :py:class:`NXOpen.Assemblies.UpdateStructureBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateUpdateStructureBuilder`
    
    Default values.
    
    ==================  =====
    Property            Value
    ==================  =====
    IsUpdateAllLevels   1 
    ------------------  -----
    NumberOfLevels      1 
    ==================  =====
    
    .. versionadded:: NX6.0.0
    """
    IsUpdateAllLevels: bool = ...
    """
    Returns or sets  the all level toggled on for updating the assembly structure.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsUpdateAllLevels`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUpdateAllLevels`` 
    
    :param isUpdateAllLevels: 
    :type isUpdateAllLevels: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NumberOfLevels: int = ...
    """
    Returns or sets  the particular selected level for updating the structure.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfLevels`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfLevels`` 
    
    :param numberOfLevels: 
    :type numberOfLevels: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    StructureToUpdate: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the component selection of the Assembly structure to Update.  
    
    <hr>
    
    Getter Method
    
    Signature ``StructureToUpdate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: UpdateStructureBuilder = ...  # unknown typename


class ProductOutlineBuilderLineFontMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ProductOutlineBuilderLineFont():
    """
    Represents the line font types
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Solid", "Solid Line"
       "Dashed", "Dashed Line"
       "Phantom", "Phantom Line"
       "Centerline", "Center Line"
       "Dotted", "Dotted Line"
       "Longdash", "Longdash Line"
       "Dotdash", "Dotdash Line"
    """
    Solid = 0  # ProductOutlineBuilderLineFontMemberType
    Dashed = 1  # ProductOutlineBuilderLineFontMemberType
    Phantom = 2  # ProductOutlineBuilderLineFontMemberType
    Centerline = 3  # ProductOutlineBuilderLineFontMemberType
    Dotted = 4  # ProductOutlineBuilderLineFontMemberType
    Longdash = 5  # ProductOutlineBuilderLineFontMemberType
    Dotdash = 6  # ProductOutlineBuilderLineFontMemberType
    
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
    


class ProductOutlineBuilder(NXOpen.Builder):
    """
    Represents a builder :py:class:`NXOpen.Assemblies.ProductOutlineBuilder`.  
    
    Input to this class can be PSM facet objects.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ProductOutlineManager.CreateProductOutlineBuilder`
    
    Default values.
    
    ==============  ======
    Property        Value
    ==============  ======
    LineFontType    Solid 
    --------------  ------
    OverrideColor   false 
    --------------  ------
    Translucency    50 
    ==============  ======
    
    .. versionadded:: NX6.0.0
    """
    
    class LineFont():
        """
        Represents the line font types
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Solid", "Solid Line"
           "Dashed", "Dashed Line"
           "Phantom", "Phantom Line"
           "Centerline", "Center Line"
           "Dotted", "Dotted Line"
           "Longdash", "Longdash Line"
           "Dotdash", "Dotdash Line"
        """
        Solid = 0  # ProductOutlineBuilderLineFontMemberType
        Dashed = 1  # ProductOutlineBuilderLineFontMemberType
        Phantom = 2  # ProductOutlineBuilderLineFontMemberType
        Centerline = 3  # ProductOutlineBuilderLineFontMemberType
        Dotted = 4  # ProductOutlineBuilderLineFontMemberType
        Longdash = 5  # ProductOutlineBuilderLineFontMemberType
        Dotdash = 6  # ProductOutlineBuilderLineFontMemberType
        
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
        
    
    LineFontType: ProductOutlineBuilderLineFont = ...
    """
    Returns or sets  the line font type for the objects defined in Product Outline.  
    
    The font types are mentioned in 
    :py:class:`NXOpen.Assemblies.ProductOutlineBuilderLineFont`.
    
    <hr>
    
    Getter Method
    
    Signature ``LineFontType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ProductOutlineBuilderLineFont` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineFontType`` 
    
    :param lineFontType: 
    :type lineFontType: :py:class:`NXOpen.Assemblies.ProductOutlineBuilderLineFont` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    OutlineColor: NXOpen.NXColor = ...
    """
    Returns or sets  the color for all the objects defined in Product Outline.  
    
    The range is 1-216
    
    <hr>
    
    Getter Method
    
    Signature ``OutlineColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutlineColor`` 
    
    :param outlineColor: 
    :type outlineColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    OverrideColor: bool = ...
    """
    Returns or sets  the flag to override-color switch.  
    
    If "true" the facet representation is in original color of selected object, 
    else representation is in the color defined by :py:meth:`NXOpen.Assemblies.ProductOutlineBuilder.OutlineColor`.
    
    <hr>
    
    Getter Method
    
    Signature ``OverrideColor`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverrideColor`` 
    
    :param overrideColor: 
    :type overrideColor: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectObject: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the objects defined in Product Outline.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Translucency: int = ...
    """
    Returns or sets  the translucency of faceted bodies/objects defined in Product Outline.  
    
    The range is 0-100.
    
    <hr>
    
    Getter Method
    
    Signature ``Translucency`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Translucency`` 
    
    :param translucency: 
    :type translucency: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ProductOutlineBuilder = ...  # unknown typename


class ArrangementsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents an arrangements builder that selects an arrangement
    
    .. versionadded:: NX6.0.0
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
    
    InheritArrangementFromParent: bool = ...
    """
    Returns or sets  the inherit arrangement from parent flag 
    
    <hr>
    
    Getter Method
    
    Signature ``InheritArrangementFromParent`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InheritArrangementFromParent`` 
    
    :param inheritArrangementFromParent: 
    :type inheritArrangementFromParent: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectedArrangement: Arrangement = ...
    """
    Returns or sets  the selected arrangement 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedArrangement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectedArrangement`` 
    
    :param arrangement: 
    :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ArrangementsBuilder = ...  # unknown typename


class AttributeSearchTerm(SearchTerm):
    """
    An attribute search term within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.AttributeSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: AttributeSearchTerm = ...  # unknown typename


class FindInCollaborativeDesignObjectTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FindInCollaborativeDesignObjectType():
    """
    The type of object for which the search is performed.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Partition", "Search for partitions"
       "DesignElement", "Search for Design Elements"
       "RunElement", "Search for Run Elements"
    """
    Partition = 0  # FindInCollaborativeDesignObjectTypeMemberType
    DesignElement = 1  # FindInCollaborativeDesignObjectTypeMemberType
    RunElement = 2  # FindInCollaborativeDesignObjectTypeMemberType
    
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
    


class FindInCollaborativeDesignSearchTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FindInCollaborativeDesignSearchType():
    """
    The attribute against which the search text is matched.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ItemQuery", "Match text with item name or id"
    """
    ItemQuery = 0  # FindInCollaborativeDesignSearchTypeMemberType
    
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
    


class FindInCollaborativeDesign(NXOpen.NXObject):
    """
    FindInCollaborativeDesign is a searcher for performing simple searches in the context of a subset.  
    
    To get an instance of this object use :py:class:`NXOpen.Assemblies.SubsetBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class ObjectType():
        """
        The type of object for which the search is performed.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Partition", "Search for partitions"
           "DesignElement", "Search for Design Elements"
           "RunElement", "Search for Run Elements"
        """
        Partition = 0  # FindInCollaborativeDesignObjectTypeMemberType
        DesignElement = 1  # FindInCollaborativeDesignObjectTypeMemberType
        RunElement = 2  # FindInCollaborativeDesignObjectTypeMemberType
        
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
        
    
    
    class SearchType():
        """
        The attribute against which the search text is matched.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ItemQuery", "Match text with item name or id"
        """
        ItemQuery = 0  # FindInCollaborativeDesignSearchTypeMemberType
        
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
        
    
    
    @typing.overload
    def PerformFind(self, objectType: FindInCollaborativeDesignObjectType, searchType: FindInCollaborativeDesignSearchType, searchText: str) -> None:
        """
        Generate the search results according to the search text.
        
        Signature ``PerformFind(objectType, searchType, searchText)`` 
        
        :param objectType: 
        :type objectType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignObjectType` 
        :param searchType: 
        :type searchType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignSearchType` 
        :param searchText: 
        :type searchText: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    @typing.overload
    def PerformFind(self, partition: Partition, objectType: FindInCollaborativeDesignObjectType, searchType: FindInCollaborativeDesignSearchType, searchText: str) -> None:
        """
        Generate the search results according to the search text, searching only
        within the partition.
        
        Signature ``PerformFind(partition, objectType, searchType, searchText)`` 
        
        :param partition: 
        :type partition: :py:class:`NXOpen.Assemblies.Partition` 
        :param objectType: 
        :type objectType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignObjectType` 
        :param searchType: 
        :type searchType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignSearchType` 
        :param searchText: 
        :type searchText: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    @typing.overload
    def PerformFind(self, objectType: FindInCollaborativeDesignObjectType, searchType: FindInCollaborativeDesignSearchType, criteriaTitles: 'list[str]', criteriaValues: 'list[str]') -> None:
        """
        Generate the search results according to the search criteria of advance search.
        Advanced search takes in detailed inputs to perform the search. The parameters "criteriaTitles" 
        and "criteriaValues" are the internal property names and their values to be searched. 
        The attribute/value pairs are combined logically using AND so that only objects matching 
        ALL of the specified criteria are returned. The method can only be used to search for matches 
        on Teamcenter properties that are string valued. It does not work for properties which are Object/LOV valued.
        To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
        use Edit-> Options...-> General-> UI-> Sys Admin-> Real Property Name in the Rich Client.
        
        Signature ``PerformFind(objectType, searchType, criteriaTitles, criteriaValues)`` 
        
        :param objectType: 
        :type objectType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignObjectType` 
        :param searchType: 
        :type searchType: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesignSearchType` 
        :param criteriaTitles:  The query criteria titles  
        :type criteriaTitles: list of str 
        :param criteriaValues:  The query criteria values  
        :type criteriaValues: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetPartitions(self) -> 'list[Partition]':
        """
        Retrieve the :py:class:`NXOpen.Assemblies.Partition`s found in the last search.  
        
        Signature ``GetPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetSearchResultElements(self) -> 'list[SearchResultElement]':
        """
        Retrieve the :py:class:`NXOpen.Assemblies.SearchResultElement`s found in the last search.  
        
        Signature ``GetSearchResultElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.SearchResultElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Null: FindInCollaborativeDesign = ...  # unknown typename


class AddComponentBuilderLocationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AddComponentBuilderLocationType():
    """
    Represents initial location type that can be present during add component 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Snap", "Snap as initial location type"
       "WorkPartAbsolute", "Absolute of work part as initial location type"
       "DisplayedPartAbsolute", "Absolute of displayed part as initial location type"
       "DisplayedPartWCS", "WCS as initial location type"
    """
    Snap = 0  # AddComponentBuilderLocationTypeMemberType
    WorkPartAbsolute = 1  # AddComponentBuilderLocationTypeMemberType
    DisplayedPartAbsolute = 2  # AddComponentBuilderLocationTypeMemberType
    DisplayedPartWCS = 3  # AddComponentBuilderLocationTypeMemberType
    
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
    


class AddComponentBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that performs add existing component operation in current context.  
    
    Context can be Assembly or 4GD.   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateAddComponentBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    class LocationType():
        """
        Represents initial location type that can be present during add component 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Snap", "Snap as initial location type"
           "WorkPartAbsolute", "Absolute of work part as initial location type"
           "DisplayedPartAbsolute", "Absolute of displayed part as initial location type"
           "DisplayedPartWCS", "WCS as initial location type"
        """
        Snap = 0  # AddComponentBuilderLocationTypeMemberType
        WorkPartAbsolute = 1  # AddComponentBuilderLocationTypeMemberType
        DisplayedPartAbsolute = 2  # AddComponentBuilderLocationTypeMemberType
        DisplayedPartWCS = 3  # AddComponentBuilderLocationTypeMemberType
        
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
        
    
    
    def GetPartsToAdd(self) -> 'list[NXOpen.BasePart]':
        """
        Returns the parts to be used for adding components
        
        Signature ``GetPartsToAdd()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPartsToAdd(self, partsToUse: 'list[NXOpen.BasePart]') -> None:
        """
        Sets the parts to be used for adding components
        
        Signature ``SetPartsToAdd(partsToUse)`` 
        
        :param partsToUse: 
        :type partsToUse: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveAddedComponents(self) -> None:
        """
        Removes the components added through add component
        
        Signature ``RemoveAddedComponents()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetCount(self) -> int:
        """
        Gets the number of components to be added.  
        
        Signature ``GetCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCount(self, count: int) -> None:
        """
        Sets the number of components to be added.  
        
        Signature ``SetCount(count)`` 
        
        :param count: 
        :type count: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetInitialLocationType(self) -> AddComponentBuilderLocationType:
        """
        Get the initial location type during add component.  
        
        Signature ``GetInitialLocationType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.AddComponentBuilderLocationType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInitialLocationType(self, locationType: AddComponentBuilderLocationType) -> None:
        """
        Set the initial location type during add component.  
        
        Signature ``SetInitialLocationType(locationType)`` 
        
        :param locationType: 
        :type locationType: :py:class:`NXOpen.Assemblies.AddComponentBuilderLocationType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetInitialLocationAndOrientation(self) -> tuple:
        """
        Returns the location and orientation used for adding component
        
        Signature ``GetInitialLocationAndOrientation()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (initialLocation, initialOrientation). initialLocation is a :py:class:`NXOpen.Point`. initialOrientation is a :py:class:`NXOpen.CoordinateSystem`. 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetInitialLocationAndOrientation(self, initialLocation: NXOpen.Point, initialOrientation: NXOpen.CoordinateSystem) -> None:
        """
        Sets the location and orientation to be used for adding component. Orientation is optional and user can pass None.
        
        Signature ``SetInitialLocationAndOrientation(initialLocation, initialOrientation)`` 
        
        :param initialLocation: 
        :type initialLocation: :py:class:`NXOpen.Point` 
        :param initialOrientation: 
        :type initialOrientation: :py:class:`NXOpen.CoordinateSystem` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def SetInitialLocationAndOrientation(self, point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3) -> None:
        """
        Sets the location and orientation to be used for add component. Orientation is optional and user can pass None.
        
        Signature ``SetInitialLocationAndOrientation(point, orientation)`` 
        
        :param point: 
        :type point: :py:class:`NXOpen.Point3d` 
        :param orientation: 
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetScatterOption(self) -> bool:
        """
        Gets the scatter option for added components.  
        
        Signature ``GetScatterOption()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetScatterOption(self, scatterOption: bool) -> None:
        """
        Sets the scatter option for added components.  
        
        Signature ``SetScatterOption(scatterOption)`` 
        
        :param scatterOption: 
        :type scatterOption: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetKeepConstraintsOption(self) -> bool:
        """
        Gets the keep constraints option for added components.  
        
        Signature ``GetKeepConstraintsOption()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetKeepConstraintsOption(self, keepConstraintsOption: bool) -> None:
        """
        Sets the keep constraints option for added components.  
        
        Signature ``SetKeepConstraintsOption(keepConstraintsOption)`` 
        
        :param keepConstraintsOption: 
        :type keepConstraintsOption: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetComponentAnchor(self) -> NXOpen.Assemblies.ProductInterface.InterfaceObject:
        """
        Returns the component anchor used for adding component 
        
        Signature ``GetComponentAnchor()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComponentAnchor(self, componentAnchor: NXOpen.Assemblies.ProductInterface.InterfaceObject) -> None:
        """
        Sets the component anchor to be used for adding component
        
        Signature ``SetComponentAnchor(componentAnchor)`` 
        
        :param componentAnchor: 
        :type componentAnchor: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetAllProductInterfaceObjects(self) -> 'list[NXOpen.Assemblies.ProductInterface.InterfaceObject]':
        """
        Returns all product interface objects available, one of these can be used as component anchor
        
        Signature ``GetAllProductInterfaceObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the pre-creation objects 
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the pre-creation objects which have unassign required attributes
        
        Signature ``GetLogicalObjectsHavingUnassignedRequiredAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns add component operation failures  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetToSnapped(self) -> None:
        """
        Resets the component to snapped position and orientation 
        
        Signature ``ResetToSnapped()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def OrientToWCS(self) -> None:
        """
        Orient added components to the WCS 
        
        Signature ``OrientToWCS()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ReverseZDirection(self) -> None:
        """
        Reverse the Z direction of added components 
        
        Signature ``ReverseZDirection()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RotateAlongZDirection(self) -> None:
        """
        Rotate added components along Z direction by 90 degrees 
        
        Signature ``RotateAlongZDirection()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetSynchDisplayProperties(self, synchDisplayProperties: bool) -> None:
        """
        Sets the option to synchronize display properties with the component to be added 
        
        Signature ``SetSynchDisplayProperties(synchDisplayProperties)`` 
        
        :param synchDisplayProperties: 
        :type synchDisplayProperties: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    ComponentName: str = ...
    """
    Returns or sets  the component name for added components.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentName`` 
    
    :param componentName: 
    :type componentName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DesignElementType: str = ...
    """
    Returns or sets  the type of a add component
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementType`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DesignElementType`` 
    
    :param deType: 
    :type deType: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    FileNewDescriptor: NXOpen.FileNew = ...
    """
    Returns  the file new descriptor to identify an added component in 4GD 
    
    <hr>
    
    Getter Method
    
    Signature ``FileNewDescriptor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FileNew` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Layer: int = ...
    """
    Returns or sets  the layer for added components.  
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReferenceSet: str = ...
    """
    Returns or sets  the reference set for added components.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSet`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSet`` 
    
    :param referenceSet: 
    :type referenceSet: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: AddComponentBuilder = ...  # unknown typename


class ClearanceAnalysisBuilderClearanceBetweenEntityMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderClearanceBetweenEntity():
    """
    Specify the type of clearance analysis. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Components", " - "
       "Bodies", " - "
    """
    Components = 0  # ClearanceAnalysisBuilderClearanceBetweenEntityMemberType
    Bodies = 1  # ClearanceAnalysisBuilderClearanceBetweenEntityMemberType
    
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
    


class ClearanceAnalysisBuilderNumberOfCollectionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderNumberOfCollections():
    """
    Specify the number of collections used for clearance analysis. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "One", " - "
       "Two", " - "
    """
    One = 0  # ClearanceAnalysisBuilderNumberOfCollectionsMemberType
    Two = 1  # ClearanceAnalysisBuilderNumberOfCollectionsMemberType
    
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
    


class ClearanceAnalysisBuilderCollectionRangeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderCollectionRange():
    """
    Specify how to compare objects inside a collection. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AllObjects", " - "
       "AllVisibleObjects", " - "
       "SelectedObjects", " - "
       "AllButSelectedObjects", " - "
    """
    AllObjects = 0  # ClearanceAnalysisBuilderCollectionRangeMemberType
    AllVisibleObjects = 1  # ClearanceAnalysisBuilderCollectionRangeMemberType
    SelectedObjects = 2  # ClearanceAnalysisBuilderCollectionRangeMemberType
    AllButSelectedObjects = 3  # ClearanceAnalysisBuilderCollectionRangeMemberType
    
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
    


class ClearanceAnalysisBuilderZoneTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderZoneType():
    """
    Specify the clearance zone type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Object", " - "
       "Pair", " - "
    """
    Object = 0  # ClearanceAnalysisBuilderZoneTypeMemberType
    Pair = 1  # ClearanceAnalysisBuilderZoneTypeMemberType
    
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
    


class ClearanceAnalysisBuilderCalculationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderCalculationMethodType():
    """
    Specify the analysis method. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Lightweight", " - "
       "ExactifLoaded", " - "
       "Exact", " - "
    """
    Lightweight = 0  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
    ExactifLoaded = 1  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
    Exact = 2  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
    
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
    


class ClearanceAnalysisBuilderClearanceZoneSourceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderClearanceZoneSource():
    """
    Specify the source of the clearance zone 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pair", " - "
       "Object1", " - "
       "Object2", " - "
       "Default", " - "
       "Defined", " - "
    """
    Pair = 0  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
    Object1 = 1  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
    Object2 = 2  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
    Default = 3  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
    Defined = 4  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
    
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
    


class ClearanceAnalysisBuilderPairExcludedReasonMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceAnalysisBuilderPairExcludedReason():
    """
    Specify the reason for excluding the pair 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoReason", "default behavior"
       "UserDefined", "user has explicitly included or excluded this pair"
       "SameCompRule", "global exclusion rule for same component applies"
       "SameGroupRule", "global exclusion rule for same group applies"
       "MatedCompRule", "global exclusion rule for mated component applies"
       "SamePartRule", "global exclusion rule for same part applies"
       "CompSuppressed", "suppressed component"
       "NonGeom", "no geometry"
       "UnitSubassy", "in unit subassembly"
    """
    NoReason = 0  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    UserDefined = 1  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    SameCompRule = 2  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    SameGroupRule = 3  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    MatedCompRule = 4  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    SamePartRule = 5  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    CompSuppressed = 6  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    NonGeom = 7  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    UnitSubassy = 8  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
    
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
    


class ClearanceAnalysisBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilder`.  
    
    The builder builds the clearance set
    which contains properties for the analysis.  The properties are:
    
    Clearance Set Name: the name of the clearance set.
    
    Clearance Type: either components or bodies or PSM facet objects.
    
    Number of collections: either one or two.  Where one collection is chosen, the analysis is performed 
    between all objects in the collection.  Where two collections are chosen, the analysis compares objects 
    from one collection with objects from the other.
    
    Exceptions:
    Select Subassemblies: Specific subassemblies selected within the displayed part can be treated as a single entity.
    
    Explicitly Ignore: A number of options to reduce the amount of results reported.
    
    Additional exceptions: Addtional pairs of objects to be excluded or included regardless of exception rules previously defined.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateClearanceAnalysisBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class ClearanceBetweenEntity():
        """
        Specify the type of clearance analysis. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Components", " - "
           "Bodies", " - "
        """
        Components = 0  # ClearanceAnalysisBuilderClearanceBetweenEntityMemberType
        Bodies = 1  # ClearanceAnalysisBuilderClearanceBetweenEntityMemberType
        
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
        
    
    
    class NumberOfCollections():
        """
        Specify the number of collections used for clearance analysis. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "One", " - "
           "Two", " - "
        """
        One = 0  # ClearanceAnalysisBuilderNumberOfCollectionsMemberType
        Two = 1  # ClearanceAnalysisBuilderNumberOfCollectionsMemberType
        
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
        
    
    
    class CollectionRange():
        """
        Specify how to compare objects inside a collection. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AllObjects", " - "
           "AllVisibleObjects", " - "
           "SelectedObjects", " - "
           "AllButSelectedObjects", " - "
        """
        AllObjects = 0  # ClearanceAnalysisBuilderCollectionRangeMemberType
        AllVisibleObjects = 1  # ClearanceAnalysisBuilderCollectionRangeMemberType
        SelectedObjects = 2  # ClearanceAnalysisBuilderCollectionRangeMemberType
        AllButSelectedObjects = 3  # ClearanceAnalysisBuilderCollectionRangeMemberType
        
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
        
    
    
    class ZoneType():
        """
        Specify the clearance zone type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Object", " - "
           "Pair", " - "
        """
        Object = 0  # ClearanceAnalysisBuilderZoneTypeMemberType
        Pair = 1  # ClearanceAnalysisBuilderZoneTypeMemberType
        
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
        
    
    
    class CalculationMethodType():
        """
        Specify the analysis method. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Lightweight", " - "
           "ExactifLoaded", " - "
           "Exact", " - "
        """
        Lightweight = 0  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
        ExactifLoaded = 1  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
        Exact = 2  # ClearanceAnalysisBuilderCalculationMethodTypeMemberType
        
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
        
    
    
    class ClearanceZoneSource():
        """
        Specify the source of the clearance zone 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pair", " - "
           "Object1", " - "
           "Object2", " - "
           "Default", " - "
           "Defined", " - "
        """
        Pair = 0  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
        Object1 = 1  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
        Object2 = 2  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
        Default = 3  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
        Defined = 4  # ClearanceAnalysisBuilderClearanceZoneSourceMemberType
        
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
        
    
    
    class PairExcludedReason():
        """
        Specify the reason for excluding the pair 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoReason", "default behavior"
           "UserDefined", "user has explicitly included or excluded this pair"
           "SameCompRule", "global exclusion rule for same component applies"
           "SameGroupRule", "global exclusion rule for same group applies"
           "MatedCompRule", "global exclusion rule for mated component applies"
           "SamePartRule", "global exclusion rule for same part applies"
           "CompSuppressed", "suppressed component"
           "NonGeom", "no geometry"
           "UnitSubassy", "in unit subassembly"
        """
        NoReason = 0  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        UserDefined = 1  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        SameCompRule = 2  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        SameGroupRule = 3  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        MatedCompRule = 4  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        SamePartRule = 5  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        CompSuppressed = 6  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        NonGeom = 7  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        UnitSubassy = 8  # ClearanceAnalysisBuilderPairExcludedReasonMemberType
        
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
        
    
    
    def AddException(self, isExclude: bool, comp1: NXOpen.DisplayableObject, comp2: NXOpen.DisplayableObject, text: str) -> None:
        """
        Add an exception.  
        
        Signature ``AddException(isExclude, comp1, comp2, text)`` 
        
        :param isExclude:  exclude or include type of the exception  
        :type isExclude: bool 
        :param comp1:  the first object of the pair  
        :type comp1: :py:class:`NXOpen.DisplayableObject` 
        :param comp2:  the second object of the pair  
        :type comp2: :py:class:`NXOpen.DisplayableObject` 
        :param text:  note for the exception  
        :type text: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteException(self, comp1: NXOpen.DisplayableObject, comp2: NXOpen.DisplayableObject) -> None:
        """
        Delete an exception.  
        
        Signature ``DeleteException(comp1, comp2)`` 
        
        :param comp1:  the first object of the pair  
        :type comp1: :py:class:`NXOpen.DisplayableObject` 
        :param comp2:  the second object of the pair  
        :type comp2: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateClearanceZoneExpression(self, rhsExpression: str) -> NXOpen.Expression:
        """
        Create an expression using the Clearance Zone naming convention.  
        
        The expression is intended for use in the following methods:
        :py:meth:`NXOpen.Assemblies.ClearanceAnalysisBuilder.SetDefaultClearanceZone` 
        :py:meth:`NXOpen.Assemblies.ClearanceAnalysisBuilder.AddPairClearanceZone` 
        :py:meth:`NXOpen.Assemblies.ClearanceAnalysisBuilder.AddObjectClearanceZone`  
        
        Signature ``CreateClearanceZoneExpression(rhsExpression)`` 
        
        :param rhsExpression:  the text for the expression  
        :type rhsExpression: str 
        :returns:  the new expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetDefaultClearanceZone(self, expression: NXOpen.Expression) -> None:
        """
        Set the expression as the default Clearance Zone.  
        
        Create the expression using :py:meth:`CreateClearanceZoneExpression` 
        if the Clearance Zone expression naming convention is desired. 
        
        Signature ``SetDefaultClearanceZone(expression)`` 
        
        :param expression:  the expression  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDefaultClearanceZone(self) -> NXOpen.Expression:
        """
        Get the default Clearance Zone expression.  
        
        If there is no expression set previously, a None will be returned.  
        
        Signature ``GetDefaultClearanceZone()`` 
        
        :returns:  the expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddPairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, expression: NXOpen.Expression) -> None:
        """
        Add a Clearance Zone between a pair of objects.  
        
        Create the expression using :py:meth:`CreateClearanceZoneExpression` 
        if the Clearance Zone expression naming convention is desired. 
        
        Signature ``AddPairClearanceZone(object1, object2, expression)`` 
        
        :param object1:  the first object  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :param expression:  the expression  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> tuple:
        """
        Inquire the Clearance Zone for a specific pair of objects.  
        
        Both objects
        must be members of the Clearance Set.  The source parameter tells where the 
        clearance zone comes from.  The clearance zone could be the greater of the zones 
        from object 1 or 2 (:py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Object1 <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>`
        or :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Object2 <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>`.
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Pair <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>`
        means this pair has its own explicit clearance zone. 
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Default <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>` means the default clearance zone is used..  
        
        Signature ``GetPairClearanceZone(object1, object2)`` 
        
        :param object1:  the first object  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (source, expression). source is a :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource`.   the source of the clearance zone expression is a :py:class:`NXOpen.Expression`.   the corresponding expression 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeletePairClearanceZone(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> None:
        """
        Delete an existing Clearance Zone between the given pair of objects.  
        
        Signature ``DeletePairClearanceZone(object1, object2)`` 
        
        :param object1:  the first object  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetIsPairIncluded(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> tuple:
        """
        Inquires if an object pair is to be included in the analysis.  
        
        Both objects
        must be solid bodies or facet models that are members of the
        clearance analysis data set. If the pair is to be analyzed, the includeIt
        is returned as TRUE. The reason parameter signifies why the pair is
        included or excluded.
        The text parameter is only returned for the :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderPairExcludedReason.UserDefined <NXOpen.Assemblies.ClearanceAnalysisBuilderPairExcludedReason>` reason.
        
        Signature ``GetIsPairIncluded(object1, object2)`` 
        
        :param object1:  the first object  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (includeIt, reason, text). includeIt is a bool.   the flag reason is a :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderPairExcludedReason`.   the reason text is a str.   the text 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddObjectClearanceZone(self, object: NXOpen.DisplayableObject, expression: NXOpen.Expression) -> None:
        """
        Add a Clearance Zone around an object.  
        
        Create the expression using :py:meth:`CreateClearanceZoneExpression` 
        if the Clearance Zone expression naming convention is desired. 
        
        Signature ``AddObjectClearanceZone(object, expression)`` 
        
        :param object:  the object  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        :param expression:  the expression  
        :type expression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetObjectClearanceZone(self, object: NXOpen.DisplayableObject) -> tuple:
        """
        Inquire the Clearance Zone assigned to a given object.  
        
        The object must be
        a member of the dataset.  The expression, the distance, and the source 
        are the outputs.  If no expression has ever been set, the part of the given object is 
        checked for a Clearance Zone expression, if none is found, None will be returned
        for the expression. Interpret its value as 0.0 (this is the default value). The
        source parameter tells where the clearance zone comes from.
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Defined <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>` specifies 
        that the object has its own Clearance Zone.  
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource.Default <NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource>` means the 
        default clearance zone is used.
        
        Signature ``GetObjectClearanceZone(object)`` 
        
        :param object:  the object  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (source, expression). source is a :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceZoneSource`.   the source of the clearance zone expression is a :py:class:`NXOpen.Expression`.   the expression 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteObjectClearanceZone(self, object: NXOpen.DisplayableObject) -> None:
        """
        Delete an existing Clearance Zone from around an object.  
        
        Signature ``DeleteObjectClearanceZone(object)`` 
        
        :param object:  the object  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    CalculationMethod: ClearanceAnalysisBuilderCalculationMethodType = ...
    """
    Returns or sets  the setting for the clearance calculation method.  
    
    <hr>
    
    Getter Method
    
    Signature ``CalculationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CalculationMethod`` 
    
    :param calculateMethod: 
    :type calculateMethod: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ClearanceBetween: ClearanceAnalysisBuilderClearanceBetweenEntity = ...
    """
    Returns or sets  the setting to determine whether components or bodies should be used.  
    
    Please note that changing the collection type will clear the collections, 
    exceptions and clearance zones from the clearance set
    
    <hr>
    
    Getter Method
    
    Signature ``ClearanceBetween`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceBetweenEntity` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClearanceBetween`` 
    
    :param clearanceBetweenEntity: 
    :type clearanceBetweenEntity: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderClearanceBetweenEntity` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ClearanceSetName: str = ...
    """
    Returns or sets  the clearance set name.  
    
    <hr>
    
    Getter Method
    
    Signature ``ClearanceSetName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClearanceSetName`` 
    
    :param clearanceSetName: 
    :type clearanceSetName: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    CollectionOneObjects: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected objects for collection one.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollectionOneObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    CollectionOneRange: ClearanceAnalysisBuilderCollectionRange = ...
    """
    Returns or sets  the range setting for collection one.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollectionOneRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCollectionRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CollectionOneRange`` 
    
    :param collectionRange: 
    :type collectionRange: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCollectionRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    CollectionTwoObjects: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected objects for collection two.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollectionTwoObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CollectionTwoRange: ClearanceAnalysisBuilderCollectionRange = ...
    """
    Returns or sets  the range setting for collection two.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollectionTwoRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCollectionRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CollectionTwoRange`` 
    
    :param collectionRange: 
    :type collectionRange: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCollectionRange` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    InterferenceColor: NXOpen.NXColor = ...
    """
    Returns or sets  the color of the interference geometry.  
    
    <hr>
    
    Getter Method
    
    Signature ``InterferenceColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterferenceColor`` 
    
    :param color: 
    :type color: Id 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsCalculatePenetrationDepth: bool = ...
    """
    Returns or sets  the setting to determine whether penetration depth should be calculated.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsCalculatePenetrationDepth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsCalculatePenetrationDepth`` 
    
    :param isCalculatePenetrationDepth: 
    :type isCalculatePenetrationDepth: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsIgnorePairsWithinSameGroup: bool = ...
    """
    Returns or sets  the setting to determine whether to ignore pairs within same group.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsIgnorePairsWithinSameGroup`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsIgnorePairsWithinSameGroup`` 
    
    :param isIgnorePairsWithinSameGroup: 
    :type isIgnorePairsWithinSameGroup: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsIgnorePairsWithinSamePart: bool = ...
    """
    Returns or sets  the setting to determine whether to ignore pairs within same part.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsIgnorePairsWithinSamePart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsIgnorePairsWithinSamePart`` 
    
    :param isIgnorePairsWithinSamePart: 
    :type isIgnorePairsWithinSamePart: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsIgnorePairsWithinSameSubassembly: bool = ...
    """
    Returns or sets  the setting to determine whether to ignore pairs within same subassembly.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsIgnorePairsWithinSameSubassembly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsIgnorePairsWithinSameSubassembly`` 
    
    :param isIgnorePairsWithinSameSubassembly: 
    :type isIgnorePairsWithinSameSubassembly: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    IsIgnorePairsWithinSelectedSubassemblies: bool = ...
    """
    Returns or sets  the setting to determine whether to ignore pairs within the selected subassemblies.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsIgnorePairsWithinSelectedSubassemblies`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsIgnorePairsWithinSelectedSubassemblies`` 
    
    :param isIgnorePairsWithinSelectedSubassemblies: 
    :type isIgnorePairsWithinSelectedSubassemblies: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Layer: int = ...
    """
    Returns or sets  the layer for interference geometry.  
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SaveInterferenceGeometry: bool = ...
    """
    Returns or sets  the setting to determine if interference geometry should be saved.  
    
    <hr>
    
    Getter Method
    
    Signature ``SaveInterferenceGeometry`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveInterferenceGeometry`` 
    
    :param saveInterferenceGeometry: 
    :type saveInterferenceGeometry: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    TotalCollectionCount: ClearanceAnalysisBuilderNumberOfCollections = ...
    """
    Returns or sets  the setting to determine whether one collection or two collections should be used.  
    
    <hr>
    
    Getter Method
    
    Signature ``TotalCollectionCount`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderNumberOfCollections` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TotalCollectionCount`` 
    
    :param totalCollectionCount: 
    :type totalCollectionCount: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderNumberOfCollections` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UnitSubassemblies: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected unit subassemblies.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnitSubassemblies`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ClearanceAnalysisBuilder = ...  # unknown typename


class SearchTermBuilder(NXOpen.Builder):
    """
    A SearchTermBuilder is used to create or edit an :py:class:`NXOpen.Assemblies.SearchTerm`.  
    
    This is the abstract base class for builders used to create search terms.
    
    No creator is available because this is an abstract class.
    
    .. versionadded:: NX8.5.0
    """
    Null: SearchTermBuilder = ...  # unknown typename


class BoxSearchTermBuilder(SearchTermBuilder):
    """
    A BoxSearchTermBuilder is used to create or edit an :py:class:`NXOpen.Assemblies.BoxSearchTerm`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateBoxSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    BottomCorner: NXOpen.Point3d = ...
    """
    Returns or sets  
    the bottom corner of the box.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomCorner`` 
    
    :returns:  Vertex of box in workset part coordinates  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``BottomCorner`` 
    
    :param bottomCorner:  Vertex of box in workset part coordinates  
    :type bottomCorner: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    BoxOverlapLogic: BoxSearchTermBoxOverlapLogicType = ...
    """
    Returns or sets  
    the box overlap logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``BoxOverlapLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.BoxSearchTermBoxOverlapLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``BoxOverlapLogic`` 
    
    :param boxOverlapLogic: 
    :type boxOverlapLogic: :py:class:`NXOpen.Assemblies.BoxSearchTermBoxOverlapLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchTermLogic: SearchTermSearchTermLogicType = ...
    """
    Returns or sets  
    the search term logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTermLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTermLogic`` 
    
    :param searchTermLogic: 
    :type searchTermLogic: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TopCorner: NXOpen.Point3d = ...
    """
    Returns or sets  
    the top corner of the box.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopCorner`` 
    
    :returns:  Vertex of box in workset part coordinates  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``TopCorner`` 
    
    :param topCorner:  Vertex of box in workset part coordinates  
    :type topCorner: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TrueShapeRefinement: bool = ...
    """
    Returns or sets  
    the true-shape refinement.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :param trueShapeRefinement: 
    :type trueShapeRefinement: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: BoxSearchTermBuilder = ...  # unknown typename


class SubsetConfigurationBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    A SubsetConfigurationBuilder is used to edit the revision rule and effectivity used
    to configure the contents of the subset.  
    
    .. versionadded:: NX8.5.0
    """
    
    def Commit(self) -> None:
        """
        Commit the subset configuration changes to the :py:class:`Assemblies.SubsetBuilder` 
        
        Signature ``Commit()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
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
    
    Effectivity: NXOpen.BasicEffectivityBuilder = ...
    """
    Returns  the effectivity for use in searches for the contents of the :py:class:`Assemblies.Subset`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Effectivity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BasicEffectivityBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    RevisionRule: str = ...
    """
    Returns or sets  the revision rule for use in searches for the contents of the :py:class:`Assemblies.Subset`.  
    
    <hr>
    
    Getter Method
    
    Signature ``RevisionRule`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``RevisionRule`` 
    
    :param revisionRule: 
    :type revisionRule: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: SubsetConfigurationBuilder = ...  # unknown typename


class CreateOverridePartBuilder(NXOpen.Builder):
    """
    Represents a builder class that creates empty override part in the specified design elements.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreateOverridePartBuilder`
    
    Default values.
    
    =============  =====
    Property       Value
    =============  =====
    MakeWorkPart   0 
    =============  =====
    
    .. versionadded:: NX10.0.0
    """
    ComponentSelectionList: SelectComponentList = ...
    """
    Returns  the list that contains components of reuse design element or subordinates
    in which to create an empty override part.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentSelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MakeWorkPart: bool = ...
    """
    Returns or sets  the state to determine whether to make the new override part as work part.  
    
    <hr>
    
    Getter Method
    
    Signature ``MakeWorkPart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MakeWorkPart`` 
    
    :param makeWorkPart: 
    :type makeWorkPart: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CreateOverridePartBuilder = ...  # unknown typename


class OrderCollection(NXOpen.TaggedObjectCollection):
    """
    a collection of  :py:class:`NXOpen.Assemblies.Order`s   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Order:
        """
        Finds the :py:class:`NXOpen.Assemblies.Order` with the given identifier as recorded in a journal.  
        
        This method should not be used in handwritten code and exists to support record and playback of journals.
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Name of the Order to be found  
        :type journalIdentifier: str 
        :returns:  Order found, or null if no such Order exists. 
        :rtype: :py:class:`NXOpen.Assemblies.Order` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class PlaneSearchTermPlaneOverlapLogicTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlaneSearchTermPlaneOverlapLogicType():
    """
    Logic used to determine the type of inclusion used in a plane search term within a recipe.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Above", "Include objects residing above the plane defined by this search term"
       "Below", "Include objects residing below the plane defined by this search term"
       "Intersects", "Include objects intersecting the plane defined by this search term"
       "AboveOrIntersects", "Include objects residing above or intersecting the plane defined by this search term"
       "BelowOrIntersects", "Include objects residing below or intersecting the plane defined by this search term"
    """
    Above = 0  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
    Below = 1  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
    Intersects = 2  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
    AboveOrIntersects = 3  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
    BelowOrIntersects = 4  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
    
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
    


class PlaneSearchTerm(SearchTerm):
    """
    A plane search term within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.PlaneSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class PlaneOverlapLogicType():
        """
        Logic used to determine the type of inclusion used in a plane search term within a recipe.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Above", "Include objects residing above the plane defined by this search term"
           "Below", "Include objects residing below the plane defined by this search term"
           "Intersects", "Include objects intersecting the plane defined by this search term"
           "AboveOrIntersects", "Include objects residing above or intersecting the plane defined by this search term"
           "BelowOrIntersects", "Include objects residing below or intersecting the plane defined by this search term"
        """
        Above = 0  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
        Below = 1  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
        Intersects = 2  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
        AboveOrIntersects = 3  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
        BelowOrIntersects = 4  # PlaneSearchTermPlaneOverlapLogicTypeMemberType
        
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
        
    
    Null: PlaneSearchTerm = ...  # unknown typename


class Explosion(NXOpen.NXObject):
    """
    Represents an explosion.  
    
    An explosion is a view containing parts or subassemblies
    that have been displaced from their real model positions.
    
    Use the :py:class:`NXOpen.Assemblies.ExplosionCollection` to create an explosion.
    
    .. versionadded:: NX4.0.0
    """
    
    def Copy(self, destinationExplosion: Explosion) -> None:
        """
        Copies the component transformations in the source explosion onto the destination explosion.  
        
        Signature ``Copy(destinationExplosion)`` 
        
        :param destinationExplosion: 
        :type destinationExplosion: :py:class:`NXOpen.Assemblies.Explosion` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Show(self, view: NXOpen.View) -> None:
        """
        Changes the view so that it shows the explosion.  
        
        Signature ``Show(view)`` 
        
        :param view: 
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Hide(self, view: NXOpen.View) -> None:
        """
        Changes the view so that it no longer shows an exploded view.  
        
        Signature ``Hide(view)`` 
        
        :param view: 
        :type view: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Deletes the given :py:class:`NXOpen.Assemblies.Explosion`.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    RootComponent: ExplodedComponent = ...
    """
    Returns  the root component of the explosion.  
    
    The root component is the exploded component at the top of the exploded component
    tree. The exploded component tree has the same structure as that of the component tree in :py:class:`NXOpen.Assemblies.ComponentAssembly`.
    
    <hr>
    
    Getter Method
    
    Signature ``RootComponent`` 
    
    :returns:  The :py:class:`NXOpen.Assemblies.ExplodedComponent` at the root of this Explosion  
    :rtype: :py:class:`NXOpen.Assemblies.ExplodedComponent` 
    
    .. versionadded:: NX9.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: Explosion = ...  # unknown typename


class ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetReanalyzeOutOfDateExcludedPairs():
    """
    Specify whether to reanalyze out-of-date excluded pairs. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CustomerDefault", " - "
       "True", " - "
       "False", " - "
    """
    CustomerDefault = 0  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
    TrueValue = 1  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
    FalseValue = 2  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
    
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
    


class ClearanceSetJobStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetJobStatus():
    """
    Specify the job aborted status 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotAborted", " - "
       "AbortedByUser", " - "
       "AbortedOnError", " - "
    """
    NotAborted = 0  # ClearanceSetJobStatusMemberType
    AbortedByUser = 1  # ClearanceSetJobStatusMemberType
    AbortedOnError = 2  # ClearanceSetJobStatusMemberType
    
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
    


class ClearanceSetCopyModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetCopyMode():
    """
    Specify the dataset copy mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoResults", " - "
       "Results", " - "
       "InterfBodies", " - "
    """
    NoResults = 0  # ClearanceSetCopyModeMemberType
    Results = 1  # ClearanceSetCopyModeMemberType
    InterfBodies = 2  # ClearanceSetCopyModeMemberType
    
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
    


class ClearanceSetReanalyzePairCalculationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetReanalyzePairCalculationMethod():
    """
    The analysis method to use when reanalyzing a pair. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UseStoredMethod", "Use the clearance set's defined analysis method."
       "Lightweight", " - "
       "ExactIfLoaded", " - "
       "Exact", " - "
    """
    UseStoredMethod = 0  # ClearanceSetReanalyzePairCalculationMethodMemberType
    Lightweight = 1  # ClearanceSetReanalyzePairCalculationMethodMemberType
    ExactIfLoaded = 2  # ClearanceSetReanalyzePairCalculationMethodMemberType
    Exact = 3  # ClearanceSetReanalyzePairCalculationMethodMemberType
    
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
    


class ClearanceSetInterferenceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetInterferenceType():
    """
    Specify the type of interference 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Soft", " - "
       "Touch", " - "
       "Hard", " - "
       "Cont1In2", " - "
       "Cont2In1", " - "
       "NoInterference", " - "
    """
    Soft = 0  # ClearanceSetInterferenceTypeMemberType
    Touch = 1  # ClearanceSetInterferenceTypeMemberType
    Hard = 2  # ClearanceSetInterferenceTypeMemberType
    Cont1In2 = 3  # ClearanceSetInterferenceTypeMemberType
    Cont2In1 = 4  # ClearanceSetInterferenceTypeMemberType
    NoInterference = 5  # ClearanceSetInterferenceTypeMemberType
    
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
    


class ClearanceSetPenetrationDepthResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClearanceSetPenetrationDepthResult():
    """
    The result of penetration depth calculation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotAttempted", " - "
       "Success", " - "
       "NoClash", " - "
       "Touching", " - "
       "BothSheets", " - "
       "UnspecifiedError", " - "
    """
    NotAttempted = 0  # ClearanceSetPenetrationDepthResultMemberType
    Success = 1  # ClearanceSetPenetrationDepthResultMemberType
    NoClash = 2  # ClearanceSetPenetrationDepthResultMemberType
    Touching = 3  # ClearanceSetPenetrationDepthResultMemberType
    BothSheets = 4  # ClearanceSetPenetrationDepthResultMemberType
    UnspecifiedError = 5  # ClearanceSetPenetrationDepthResultMemberType
    
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
    


class ClearanceSet(NXOpen.NXObject):
    """
    Represents :py:class:`NXOpen.Assemblies.ClearanceSet`.  
    
    Input to this class can be PSM facet objects.
    
    Currently we don't support KF at this time.
    
    .. versionadded:: NX9.0.0
    """
    
    class ReanalyzeOutOfDateExcludedPairs():
        """
        Specify whether to reanalyze out-of-date excluded pairs. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CustomerDefault", " - "
           "True", " - "
           "False", " - "
        """
        CustomerDefault = 0  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
        TrueValue = 1  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
        FalseValue = 2  # ClearanceSetReanalyzeOutOfDateExcludedPairsMemberType
        
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
        
    
    
    class JobStatus():
        """
        Specify the job aborted status 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotAborted", " - "
           "AbortedByUser", " - "
           "AbortedOnError", " - "
        """
        NotAborted = 0  # ClearanceSetJobStatusMemberType
        AbortedByUser = 1  # ClearanceSetJobStatusMemberType
        AbortedOnError = 2  # ClearanceSetJobStatusMemberType
        
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
        
    
    
    class CopyMode():
        """
        Specify the dataset copy mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoResults", " - "
           "Results", " - "
           "InterfBodies", " - "
        """
        NoResults = 0  # ClearanceSetCopyModeMemberType
        Results = 1  # ClearanceSetCopyModeMemberType
        InterfBodies = 2  # ClearanceSetCopyModeMemberType
        
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
        
    
    
    class ReanalyzePairCalculationMethod():
        """
        The analysis method to use when reanalyzing a pair. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UseStoredMethod", "Use the clearance set's defined analysis method."
           "Lightweight", " - "
           "ExactIfLoaded", " - "
           "Exact", " - "
        """
        UseStoredMethod = 0  # ClearanceSetReanalyzePairCalculationMethodMemberType
        Lightweight = 1  # ClearanceSetReanalyzePairCalculationMethodMemberType
        ExactIfLoaded = 2  # ClearanceSetReanalyzePairCalculationMethodMemberType
        Exact = 3  # ClearanceSetReanalyzePairCalculationMethodMemberType
        
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
        
    
    
    class InterferenceType():
        """
        Specify the type of interference 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Soft", " - "
           "Touch", " - "
           "Hard", " - "
           "Cont1In2", " - "
           "Cont2In1", " - "
           "NoInterference", " - "
        """
        Soft = 0  # ClearanceSetInterferenceTypeMemberType
        Touch = 1  # ClearanceSetInterferenceTypeMemberType
        Hard = 2  # ClearanceSetInterferenceTypeMemberType
        Cont1In2 = 3  # ClearanceSetInterferenceTypeMemberType
        Cont2In1 = 4  # ClearanceSetInterferenceTypeMemberType
        NoInterference = 5  # ClearanceSetInterferenceTypeMemberType
        
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
        
    
    
    class PenetrationDepthResult():
        """
        The result of penetration depth calculation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotAttempted", " - "
           "Success", " - "
           "NoClash", " - "
           "Touching", " - "
           "BothSheets", " - "
           "UnspecifiedError", " - "
        """
        NotAttempted = 0  # ClearanceSetPenetrationDepthResultMemberType
        Success = 1  # ClearanceSetPenetrationDepthResultMemberType
        NoClash = 2  # ClearanceSetPenetrationDepthResultMemberType
        Touching = 3  # ClearanceSetPenetrationDepthResultMemberType
        BothSheets = 4  # ClearanceSetPenetrationDepthResultMemberType
        UnspecifiedError = 5  # ClearanceSetPenetrationDepthResultMemberType
        
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
        
    
    
    class Summary():
        """
        Summary of the most recent Clearance Analysis results .  
        
        Constructor: 
        NXOpen.Assemblies.ClearanceSet.Summary()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        StartTime: int = ...
        """
        The starting time of the last
        analysis run (in seconds since
        00:00:00 1/1/1970.  
        
        <hr>
        
        Field Value
        Type:int
        """
        EndTime: int = ...
        """
        The ending time of the last
        analysis run (in seconds since
        00:00:00 1/1/1970.  
        
        <hr>
        
        Field Value
        Type:int
        """
        RunTime: int = ...
        """
        the total analysis time (in secs.  
        
        ) 
        <hr>
        
        Field Value
        Type:int
        """
        Version: int = ...
        """
        The version of this analysis run.  
        
        This is a positive number.
        
        <hr>
        
        Field Value
        Type:int
        """
        AnalysisMode: ClearanceAnalysisBuilderCalculationMethodType = ...
        """
        The analysis mode.  
        
        One of
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.Lightweight <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`,
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.ExactifLoaded <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`,
        :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType.Exact <NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType>`.
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilderCalculationMethodType`
        """
        NumCollections: int = ...
        """
        Number of collections analyzed.  
        
        Can be either 1 or 2.
        
        <hr>
        
        Field Value
        Type:int
        """
        NumCollection1: int = ...
        """
        The number of objects in collection 1.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumCollection2: int = ...
        """
        The number of objects in collection 2.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumPairs: int = ...
        """
        The number of pairs built from
        the object collections.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumExcludedPairs: int = ...
        """
        The number of pairs that were
        excluded from analysis, either
        due to exclusion rules or
        explicit pair exclusion.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumChangedPairs: int = ...
        """
        The number of pairs that had
        changed since the previous
        clearance analysis.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumChangedObjs: int = ...
        """
        The number of objects that had
        changed since the previous
        clearance analysis.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumCheckedPairs: int = ...
        """
        The total number of pairs that
        underwent analysis.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumNewHard: int = ...
        """
        The total number of new hard
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumNewSoft: int = ...
        """
        The total number of new soft
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumNewTouching: int = ...
        """
        The total number of new touching
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumNewContainment: int = ...
        """
        The total number of new containment
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumNewAllInterf: int = ...
        """
        The total number of new
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumHard: int = ...
        """
        The total number of hard
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumSoft: int = ...
        """
        The total number of soft
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumTouching: int = ...
        """
        The total number of touching
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumContainment: int = ...
        """
        The total number of containment
        interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        NumAllInterf: int = ...
        """
        The total number of interferences.  
        
        <hr>
        
        Field Value
        Type:int
        """
        JobStatus: ClearanceSetJobStatus = ...
        """
        Indicates if the analysis was
        aborted.  
        
        Valid values are
        :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.NotAborted <NXOpen.Assemblies.ClearanceSetJobStatus>`,
        :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.AbortedByUser <NXOpen.Assemblies.ClearanceSetJobStatus>` and
        :py:class:`NXOpen.Assemblies.ClearanceSetJobStatus.AbortedOnError <NXOpen.Assemblies.ClearanceSetJobStatus>`.
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Assemblies.ClearanceSetJobStatus`
        """
        NumZones: int = ...
        """
        The number of assembly zones used
        by the analysis (batch only).  
        
        <hr>
        
        Field Value
        Type:int
        """
    
    
    def PerformAnalysis(self, reanalyzeOption: ClearanceSetReanalyzeOutOfDateExcludedPairs) -> None:
        """
        Perform an analysis on this clearance set with option to specify whether
        out-of-date excluded pairs will be reanalyzed.  
        
        You can specify to use the
        Customer Default setting, or you can specify a true or false option to override
        the Customer Default. 
        
        Signature ``PerformAnalysis(reanalyzeOption)`` 
        
        :param reanalyzeOption: 
        :type reanalyzeOption: :py:class:`NXOpen.Assemblies.ClearanceSetReanalyzeOutOfDateExcludedPairs` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ReanalyzePairs(self, firstObjects: 'list[NXOpen.DisplayableObject]', secondObjects: 'list[NXOpen.DisplayableObject]', calculationMethod: ClearanceSetReanalyzePairCalculationMethod) -> None:
        """
        Reanalyze a set of interferences using the specified analysis method.  
        
        The interferences
        must be specified using two parallel arrays: the objects in the first interference should
        be given in the first elements of the arrays, the objects in the second interference should
        be given in the second elements of the arrays, etc. 
        
        Signature ``ReanalyzePairs(firstObjects, secondObjects, calculationMethod)`` 
        
        :param firstObjects:  The first object of each interference.  Must be the same size as secondObjects.  
        :type firstObjects: list of :py:class:`NXOpen.DisplayableObject` 
        :param secondObjects:  The second object of each interference.  Must be the same size as firstObjects.  
        :type secondObjects: list of :py:class:`NXOpen.DisplayableObject` 
        :param calculationMethod: 
        :type calculationMethod: :py:class:`NXOpen.Assemblies.ClearanceSetReanalyzePairCalculationMethod` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateInterferenceGeometry(self, firstObjects: 'list[NXOpen.DisplayableObject]', secondObjects: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Construct interference geometry for a set of hard interferences.  
        
        The interferences
        must be specified using two parallel arrays: the objects in the first interference should
        be given in the first elements of the arrays, the objects in the second interference should
        be given in the second elements of the arrays, etc. 
        
        Signature ``CreateInterferenceGeometry(firstObjects, secondObjects)`` 
        
        :param firstObjects:  The first object of each interference.  Must be the same size as secondObjects.  
        :type firstObjects: list of :py:class:`NXOpen.DisplayableObject` 
        :param secondObjects:  The second object of each interference.  Must be the same size as firstObjects.  
        :type secondObjects: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CalculatePenetrationDepth(self, firstObjects: 'list[NXOpen.DisplayableObject]', secondObjects: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Calculate penetration depth for a set of hard interferences.  
        
        The interferences
        must be specified using two parallel arrays: the objects in the first interference should
        be given in the first elements of the arrays, the objects in the second interference should
        be given in the second elements of the arrays, etc. 
        
        Signature ``CalculatePenetrationDepth(firstObjects, secondObjects)`` 
        
        :param firstObjects:  The first object of each interference.  Must be the same size as secondObjects.  
        :type firstObjects: list of :py:class:`NXOpen.DisplayableObject` 
        :param secondObjects:  The second object of each interference.  Must be the same size as firstObjects.  
        :type secondObjects: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Delete this clearance set 
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetVersion(self) -> int:
        """
        Gets the version of a clearance analysis dataset.  
        
        The version indicates
        how many times clearance analysis has been run on a data set. If the
        version is zero, then the analysis has never been run.  
        
        Signature ``GetVersion()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetInterferenceData(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> tuple:
        """
        Inquires the data associated with a given pair of interfering objects.  
        
        Signature ``GetInterferenceData(object1, object2)`` 
        
        :param object1:  the first object in the pair  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object in the pair  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (type, newInterference, interfBodies, point1, point2, text, interfNum, config, depthResult, depth, direction, minPoint, maxPoint). type is a :py:class:`NXOpen.Assemblies.ClearanceSetInterferenceType`.   the interference type newInterference is a bool.   the flag for new interference interfBodies is a list of :py:class:`NXOpen.DisplayableObject`.   the list of interference bodies point1 is a :py:class:`NXOpen.Point3d`.   a point on the first object point2 is a :py:class:`NXOpen.Point3d`.   a point on the second object text is a str.   text associated with the interference interfNum is a int.   a unique number for the interference config is a int.   the configuration index depthResult is a int.   result status of penetration depth calculation depth is a float.   depth of penetration direction is a :py:class:`NXOpen.Vector3d`.   a unit vector indicating the direction of penetration minPoint is a :py:class:`NXOpen.Point3d`.   the points on the interference region at the extremes of depth maxPoint is a :py:class:`NXOpen.Point3d`.   the points on the interference region at the extremes of depth 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetResults(self) -> ClearanceSetSummary_Struct:
        """
        Inquires a summary of the results of the most recent clearance analysis run.  
        
        The :py:class:`NXOpen.Assemblies.ClearanceSetSummary_Struct` structure is 
        filled with analysis statistics, including numbers of objects, number of pairs,
        number of checked pairs, and number of interferences of each type. If
        clearance analysis has never been run on the data set, an error is
        returned.  
        
        Signature ``GetResults()`` 
        
        :returns:  the summary structure  
        :rtype: :py:class:`NXOpen.Assemblies.ClearanceSetSummary_Struct` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetNumberOfInterferences(self) -> int:
        """
        Inquires the number of interferences stored in a clearance analysis
        data set.  
        
        If clearance analysis has never been run on the data set, an
        error is returned.  
        
        Signature ``GetNumberOfInterferences()`` 
        
        :returns:  the number of interferences associated with the dataset  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteInterference(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> None:
        """
        Deletes the interference for a given object pair.  
        
        Both objects must be
        members of the given data set. If the object pair does not refer to an
        existing interference, an error is returned. All data associated with the
        interference is deleted. 
        
        Signature ``DeleteInterference(object1, object2)`` 
        
        :param object1:  the first object in the pair  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object in the pair  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetIsPairChanged(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> bool:
        """
        Inquires if an object pair has changed since the last analysis run.  
        
        Both
        objects must be solid bodies or facet models that are members of the
        clearance analysis data set. If either object has changed since the last
        analysis run, then isChanged is returned as TRUE. If no analysis has
        been run on either of the objects, TRUE is returned.  
        
        Signature ``GetIsPairChanged(object1, object2)`` 
        
        :param object1:  the first object in the pair  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object in the pair  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :returns:  Has this pair changed since the last analysis run?  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetNextInterference(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject) -> tuple:
        """
        Cycles the interference in a clearance analysis data set.  
        
        Interferences
        are stored as object pairs. Start the cycling using None as the
        input values for both object1 and object2. This routine passes back the
        tags of the objects that define the next interference. None
        returned for either object indicates the end of the cycling. 
        
        Signature ``GetNextInterference(object1, object2)`` 
        
        :param object1:  the first object in the pair of the current interference  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object in the pair of the current interference  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (nextObject1, nextObject2). nextObject1 is a :py:class:`NXOpen.DisplayableObject`.   the first object in the pair of the next interference nextObject2 is a :py:class:`NXOpen.DisplayableObject`.   the second object in the pair of the next interference 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Copy(self, name: str, mode: ClearanceSetCopyMode) -> ClearanceSet:
        """
        Makes a copy of a dataset.  
        
        You must supply a unique name.  There are three
        modes in which to copy the dataset: :py:class:`NXOpen.Assemblies.ClearanceSetCopyMode.NoResults <NXOpen.Assemblies.ClearanceSetCopyMode>` 
        only copies the setup data.  The version of the new dataset is set to zero (meaning clearance analysis 
        has not been run);  :py:class:`NXOpen.Assemblies.ClearanceSetCopyMode.Results <NXOpen.Assemblies.ClearanceSetCopyMode>` makes a copy of the current 
        analysis results, but not the interference bodies; :py:class:`NXOpen.Assemblies.ClearanceSetCopyMode.InterfBodies <NXOpen.Assemblies.ClearanceSetCopyMode>` 
        makes a complete copy of the results. The name must  be less than MAX_LINE_SIZE characters long  
        
        Signature ``Copy(name, mode)`` 
        
        :param name:  the name of the new dataset  
        :type name: str 
        :param mode:  copy mode  
        :type mode: :py:class:`NXOpen.Assemblies.ClearanceSetCopyMode` 
        :returns:  the dataset that is copied  
        :rtype: :py:class:`NXOpen.Assemblies.ClearanceSet` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetInterferenceText(self, object1: NXOpen.DisplayableObject, object2: NXOpen.DisplayableObject, text: str) -> None:
        """
        Associates a text string to an interfering object pair.  
        
        Both objects must
        be members of the given dataset. If the object pair does not refer to
        an existing interference, an error is returned. 
        
        Signature ``SetInterferenceText(object1, object2, text)`` 
        
        :param object1:  the first object in the pair  
        :type object1: :py:class:`NXOpen.DisplayableObject` 
        :param object2:  the second object in the pair  
        :type object2: :py:class:`NXOpen.DisplayableObject` 
        :param text:  the name of the new dataset  
        :type text: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DetectObsoleteSettings(self, doCleanupNow: bool) -> bool:
        """
        Detects whether a clearance set was defined with settings which are obsolete/no longer supported.  
        
        For example,
        prior to NX 9.0, an optional setting "ignore mated pairs" was available.  Existing results may still be read
        from a clearance set with obsolete settings, but the next time analysis is performed, the obsolete settings
        will be removed and all existing results cleared.
        Optionally, this method can perform any required cleanup now, instead of waiting until the next analysis.  
        
        Signature ``DetectObsoleteSettings(doCleanupNow)`` 
        
        :param doCleanupNow:  whether cleanup should be performed now  
        :type doCleanupNow: bool 
        :returns:  whether the clearance set contains obsolete settings  
        :rtype: bool 
        
        .. versionadded:: NX10.0.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: ClearanceSet = ...  # unknown typename


class DegreesOfFreedomStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DegreesOfFreedomStatus():
    """
    The status of a rotation point, rotation axis or translation direction reported
    in :py:class:`NXOpen.Assemblies.DegreesOfFreedom`. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotUsed", "The field is not used."
       "Static", "The point or direction is well defined."
       "Free", "The point or direction is under defined."
       "Instantaneous", "The point or direction is instantaneous."
       "StaticNormal", "The direction represents a normal to two translational degrees of freedom. The direction is well defined."
       "FreeNormal", "The direction represents a normal to two translational degrees of freedom. The direction is under defined."
       "InstantaneousNormal", "The direction represents a normal to two translational degrees of freedom. The direction is instantaneous."
    """
    NotUsed = 0  # DegreesOfFreedomStatusMemberType
    Static = 1  # DegreesOfFreedomStatusMemberType
    Free = 2  # DegreesOfFreedomStatusMemberType
    Instantaneous = 3  # DegreesOfFreedomStatusMemberType
    StaticNormal = 4  # DegreesOfFreedomStatusMemberType
    FreeNormal = 5  # DegreesOfFreedomStatusMemberType
    InstantaneousNormal = 6  # DegreesOfFreedomStatusMemberType
    
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
    


class PatternMember(NXOpen.NXObject):
    """
    Represents the pattern member object.  
    
    Instances of this class can be accessed through component pattern object
    
    .. versionadded:: NX9.0.0
    """
    
    def GetAllComponents(self) -> 'list[Component]':
        """
        Returns all the :py:class:`NXOpen.Assemblies.Component` of pattern member.  
        
        Signature ``GetAllComponents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsPatternMaster(self) -> bool:
        """
        Indicates whether this member is the :py:class:`NXOpen.Assemblies.PatternMaster` or not.  
        
        Signature ``IsPatternMaster()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PatternMember = ...  # unknown typename


class PatternMaster(PatternMember):
    """
    Represents the pattern master object.  
    
    Instances of this class can be accessed through component pattern object
    
    .. versionadded:: NX9.0.0
    """
    Null: PatternMaster = ...  # unknown typename


class WaveQuery(NXOpen.TransientObject):
    """
    Provides information about the inter-part relations (e.g. WAVE, inter-part
    expressions) in a NX model. 
    
    The returned XML string contains information from
    parts loaded in the NX session and from published TeamCenter data. The XML
    must be unmarshaled using the Browser_model_schema.xsd.The XML identifiers
    are valid for the life of the session and are used in sequent queries.
    
    For the selected parts, the queries return the first level parent (source) and
    child (target) parts. The object-object relations that comprise a part-part
    relation are included if the information is available. Each query provides a
    context for the meaning of a selected part. For example, the work part is the
    only selected part for GetWorkPartWithPartRelationsXml. However, the method
    GetPartsInContextAssemblyXml considers all the unique parts in the context
    assembly to be selected.
    
    Since the queries also return the first level parent and child parents, these
    non-selected parts could exist only in TeamCenter.
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX6.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector.
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPartPreview(self, partSpec: str, partIdentifier: int) -> tuple:
        """
        Gets the part's preview image.  
        
        Signature ``GetPartPreview(partSpec, partIdentifier)`` 
        
        :param partSpec:  the part's specification  
        :type partSpec: str 
        :param partIdentifier:  part's in-session identifier  
        :type partIdentifier: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (height, width, pixels). height is a int.   height of preview image width is a int.   width of preview image pixels is a list of int.   the pixels 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetInSessionPartsXml(self, includeOnlyWithLinks: bool) -> str:
        """
        Gets the parts that are in-session.  
        
        The parts are not necessarily fully loaded.
        
        Signature ``GetInSessionPartsXml(includeOnlyWithLinks)`` 
        
        :param includeOnlyWithLinks:  true if only parts that own inter-part links are returned  
        :type includeOnlyWithLinks: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetPartsInContextAssemblyXml(self, includeOnlyWithLinks: bool) -> str:
        """
        Gets the parts that are in the context assembly.  
        
        The parts are not necessarily fully loaded.
        
        Signature ``GetPartsInContextAssemblyXml(includeOnlyWithLinks)`` 
        
        :param includeOnlyWithLinks:  true if only parts that own inter-part links are returned  
        :type includeOnlyWithLinks: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetAllSelectedPartsXml(self, includeOnlyWithLinks: bool) -> str:
        """
        Gets all the parts in the current selection list in the NX session.  
        
        Signature ``GetAllSelectedPartsXml(includeOnlyWithLinks)`` 
        
        :param includeOnlyWithLinks:  true if only parts that own inter-part links are returned  
        :type includeOnlyWithLinks: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetWorkPartWithPartRelationsXml(self) -> str:
        """
        Gets the current work part.  
        
        Signature ``GetWorkPartWithPartRelationsXml()`` 
        
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetChildPartRelationsXml(self, parentPartSpec: str, parentPartIdentifier: int, walkAll: bool) -> str:
        """
        Gets the child parts for a given part.  
        
        The parts are not necessarily fully loaded.
        The specified part and its children are considered to be "selected" parts.
        
        Signature ``GetChildPartRelationsXml(parentPartSpec, parentPartIdentifier, walkAll)`` 
        
        :param parentPartSpec:  the part's specification  
        :type parentPartSpec: str 
        :param parentPartIdentifier:  part's in-session identifier  
        :type parentPartIdentifier: int 
        :param walkAll:  true if children of all descendants are obtained  
        :type walkAll: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetParentPartRelationsXml(self, childPartSpec: str, childPartIdentifier: int, walkAll: bool) -> str:
        """
        Gets the parent parts for a given part.  
        
        The parts are not necessarily fully loaded.
        The specified part and its parents are considered to be "selected" parts.
        
        Signature ``GetParentPartRelationsXml(childPartSpec, childPartIdentifier, walkAll)`` 
        
        :param childPartSpec:  the part's specification  
        :type childPartSpec: str 
        :param childPartIdentifier:  part's in-session identifier  
        :type childPartIdentifier: int 
        :param walkAll:  true if parents of all ancestors are obtained  
        :type walkAll: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetProductInterfacesXml(self, partSpec: str, partIdentifier: int) -> str:
        """
        Gets the product interfaces and their references for a given part.  
        
        The owning part is the
        "selected" part.
        
        Signature ``GetProductInterfacesXml(partSpec, partIdentifier)`` 
        
        :param partSpec:  the part's specification  
        :type partSpec: str 
        :param partIdentifier:  part's in-session identifier  
        :type partIdentifier: int 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetInterPartLinksXml(self, partSpec: str, partIdentifier: int) -> str:
        """
        Gets the inter-part links and their sources for a given part.  
        
        The owning part is the
        "selected" part.
        
        Signature ``GetInterPartLinksXml(partSpec, partIdentifier)`` 
        
        :param partSpec:  the part's specification  
        :type partSpec: str 
        :param partIdentifier:  part's in-session identifier  
        :type partIdentifier: int 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetReferencesToProductInterfaceXml(self, owningPartSpec: str, owningPartIdentifier: int, prodintHandle: str, prodintIdentifier: int) -> str:
        """
        Gets a product interface's referencing objects.  
        
        The owning part is the "selected" part.
        
        Signature ``GetReferencesToProductInterfaceXml(owningPartSpec, owningPartIdentifier, prodintHandle, prodintIdentifier)`` 
        
        :param owningPartSpec:  the owning part's specification  
        :type owningPartSpec: str 
        :param owningPartIdentifier:  owning part's in-session identifier  
        :type owningPartIdentifier: int 
        :param prodintHandle:  the product interface's handle  
        :type prodintHandle: str 
        :param prodintIdentifier:  product interface's in-session identifier  
        :type prodintIdentifier: int 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def HandleApplicationEvents(self, eventType: AssembliesEventTypes, eventDescription: str, entitySpecs: 'list[str]', entityIdentifiers: 'list[int]') -> int:
        """
        Provides application (e.  
        
        g. the graphical browser) event processing by NX.
        Some events refer to part level actions while others refer to part object level actions.
        
        Signature ``HandleApplicationEvents(eventType, eventDescription, entitySpecs, entityIdentifiers)`` 
        
        :param eventType:  type of event for processing  
        :type eventType: :py:class:`NXOpen.Assemblies.AssembliesEventTypes` 
        :param eventDescription:  textual description of the event for reporting  
        :type eventDescription: str 
        :param entitySpecs:  the NX part specifications or the handles of the objects  
        :type entitySpecs: list of str 
        :param entityIdentifiers:  the NX part or object identifiers  
        :type entityIdentifiers: list of int 
        :returns:  the return status of this method  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetPartFeatureDependenciesXml(self, partSpec: str, partIdentifier: int) -> str:
        """
        Gets the feature dependency lists for a fully loaded part.  
        
        Signature ``GetPartFeatureDependenciesXml(partSpec, partIdentifier)`` 
        
        :param partSpec:  the part's specification  
        :type partSpec: str 
        :param partIdentifier:  part's in-session identifier  
        :type partIdentifier: int 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def AreAssemblyConstraintsDelayed(self) -> bool:
        """
        Returns true if update of assembly constraints is delayed
        
        Signature ``AreAssemblyConstraintsDelayed()`` 
        
        :returns:  whether constraints are delayed  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetSpecifiedPartRelationsXml(self, partSpecs: 'list[str]', partIdentifiers: 'list[int]', includeOnlyWithLinks: bool) -> str:
        """
        Gets information about the specified parts.  
        
        The parts are not necessarily fully loaded.
        
        Signature ``GetSpecifiedPartRelationsXml(partSpecs, partIdentifiers, includeOnlyWithLinks)`` 
        
        :param partSpecs:  the NX part specifications  
        :type partSpecs: list of str 
        :param partIdentifiers:  the NX part identifiers  
        :type partIdentifiers: list of int 
        :param includeOnlyWithLinks:  true if only parts that own inter-part links are returned  
        :type includeOnlyWithLinks: bool 
        :returns:  the XML  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def SetChildRevisionOption(self, optionType: AssembliesChildRevisionOptions) -> None:
        """
        Specifies what child revisions to fetch from Teamcenter
        
        Signature ``SetChildRevisionOption(optionType)`` 
        
        :param optionType:  what child revisions to fetch from Teamcenter  
        :type optionType: :py:class:`NXOpen.Assemblies.AssembliesChildRevisionOptions` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetChildRevisionOption(self) -> AssembliesChildRevisionOptions:
        """
        Returns the child revision option
        
        Signature ``GetChildRevisionOption()`` 
        
        :returns:  the child revision option that is currently set  
        :rtype: :py:class:`NXOpen.Assemblies.AssembliesChildRevisionOptions` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    


class ProximitySearchTerm(SearchTerm):
    """
    A proximity search term within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.ProximitySearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: ProximitySearchTerm = ...  # unknown typename


class DrawingExplosionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of drawing explosions   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> DrawingExplosion:
        """
        Finds the :py:class:`NXOpen.Assemblies.DrawingExplosion` with the given identifier as recorded in a journal.  
        
        This method should not be used in handwritten code and exists to support record and playback of journals.
        An exception will be thrown if no object can be found with the given journal identifier.
        
        Signature ``FindObject(name)`` 
        
        :param name:  Name of the DrawingExplosion to be found  
        :type name: str 
        :returns:  DrawingExplosion found, or null if no such DrawingExplosion exists. 
        :rtype: :py:class:`NXOpen.Assemblies.DrawingExplosion` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    


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
        :type object: :py:class:`NXOpen.Assemblies.Component` 
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
        :type objects: list of :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection1: :py:class:`NXOpen.Assemblies.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection: :py:class:`NXOpen.Assemblies.Component` 
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
        :type object: :py:class:`NXOpen.Assemblies.Component` 
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
        :type object: :py:class:`NXOpen.Assemblies.Component` 
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
        :type selection1: :py:class:`NXOpen.Assemblies.Component` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Assemblies.Component` 
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
        :type objects: list of :py:class:`NXOpen.Assemblies.Component` 
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
        :type object: :py:class:`NXOpen.Assemblies.Component` 
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
        :type objects: list of :py:class:`NXOpen.Assemblies.Component` 
        
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
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
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


class ComponentPattern(NXOpen.NXObject):
    """
    Represents the component pattern class.  
    
    Input to this class can be PSM facet objects. 
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.ComponentPatternBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    def Delete(self, deleteComponents: bool) -> None:
        """
        Deletes the component pattern object.  
        
        Signature ``Delete(deleteComponents)`` 
        
        :param deleteComponents: 
        :type deleteComponents: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Suppress(self) -> None:
        """
        Suppresses the component pattern object.  
        
        Signature ``Suppress()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Unsuppress(self) -> None:
        """
        Unsuppresses the component pattern object.  
        
        Signature ``Unsuppress()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DisplayInformation(self) -> None:
        """
        Displays the information of the component pattern.  
        
        Signature ``DisplayInformation()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadRelatedGeometry(self) -> NXOpen.PartLoadStatus:
        """
        Loads the parts containing data referenced by this pattern, 
        including the parts that are patterned and parts containing 
        the objects that define the pattern parameters.  
        
        Signature ``LoadRelatedGeometry()`` 
        
        :returns:  Error information for any part that could not be loaded.  
        :rtype: :py:class:`NXOpen.PartLoadStatus` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPatternName(self) -> str:
        """
        Gets the component pattern name.  
        
        Signature ``GetPatternName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPatternSuppressedStatus(self) -> bool:
        """
        Gets the suppressed status of the component pattern.  
        
        Signature ``GetPatternSuppressedStatus()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPatternDeferredStatus(self) -> bool:
        """
        Gets the deferred status of the component pattern.  
        
        Signature ``GetPatternDeferredStatus()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllPatternMembers(self) -> 'list[PatternMember]':
        """
        Returns all the pattern members.  
        
        Signature ``GetAllPatternMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.PatternMember` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetComponentsToPattern(self) -> 'list[Component]':
        """
        Gets all the :py:class:`Assemblies.Component` that are selected for component pattern.  
        
        Signature ``GetComponentsToPattern()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ChangeReferencePatternTemplate(self, firstBaseInstanceIndex: int, secondBaseInstanceIndex: int) -> None:
        """
        Changes the template component of a reference pattern to a pattern member at indices (firstBaseInstanceIndex, secondBaseInstanceIndex).  
        
        Signature ``ChangeReferencePatternTemplate(firstBaseInstanceIndex, secondBaseInstanceIndex)`` 
        
        :param firstBaseInstanceIndex: 
        :type firstBaseInstanceIndex: int 
        :param secondBaseInstanceIndex: 
        :type secondBaseInstanceIndex: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ComponentPattern = ...  # unknown typename


class AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesGeneralPropertiesBuilderHiddenOptions():
    """
    Options for managing the hidden property on the components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "No", "Do not hide the objects"
       "Yes", "Hide the objects"
       "Mixed", "Objects hidden properties differ and will not change"
    """
    No = 0  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
    Yes = 1  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
    Mixed = 2  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
    
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
    


class AssembliesGeneralPropertiesBuilderLayerOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesGeneralPropertiesBuilderLayerOptions():
    """
    Layer options for the components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OriginalLayer", "Objects will be placed on original layer"
       "SpecifiedLayer", "Objects will be placed on a user specified layer"
       "Mixed", "Objects are on different layers and will not be changed"
    """
    OriginalLayer = 0  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
    SpecifiedLayer = 1  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
    Mixed = 2  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
    
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
    


class AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesGeneralPropertiesBuilderReferenceComponentOptions():
    """
    Options for setting the reference-only property on the components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "No", "Objects will be non reference-only components"
       "Yes", "Objects will be reference-only components"
       "Mixed", "Objects are a mixture of reference-only and non reference-only components, and will not be changed"
    """
    No = 0  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
    Yes = 1  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
    Mixed = 2  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
    
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
    


class AssembliesGeneralPropertiesBuilderQuantityOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesGeneralPropertiesBuilderQuantityOptions():
    """
    Options for assigning the quantity on the components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Number", "Use either the integer or real value to set the quantity"
       "AsRequired", "Sets the as-required quantity on this component."
    """
    Number = 0  # AssembliesGeneralPropertiesBuilderQuantityOptionsMemberType
    AsRequired = 1  # AssembliesGeneralPropertiesBuilderQuantityOptionsMemberType
    
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
    


class AssembliesGeneralPropertiesBuilder(NXOpen.Builder):
    """
    Represents an :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilder` to be used for changing the
    general properties of a component.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PropertiesManager.CreateAssembliesGeneralPropertiesBuilder`
    
    Default values.
    
    =====================  ==============
    Property               Value
    =====================  ==============
    Hidden                 No 
    ---------------------  --------------
    IntegerQuantity        0 
    ---------------------  --------------
    Layer                  0 
    ---------------------  --------------
    LayerOption            OriginalLayer 
    ---------------------  --------------
    NonGeometric           0 
    ---------------------  --------------
    QuantityType           Number 
    ---------------------  --------------
    RealQuantity           0 
    ---------------------  --------------
    ReferenceComponent     No 
    ---------------------  --------------
    SpecificColor          0 
    ---------------------  --------------
    SpecificPartialShade   0 
    ---------------------  --------------
    SpecificTranslucency   0 
    =====================  ==============
    
    .. versionadded:: NX8.0.0
    """
    
    class HiddenOptions():
        """
        Options for managing the hidden property on the components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "No", "Do not hide the objects"
           "Yes", "Hide the objects"
           "Mixed", "Objects hidden properties differ and will not change"
        """
        No = 0  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
        Yes = 1  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
        Mixed = 2  # AssembliesGeneralPropertiesBuilderHiddenOptionsMemberType
        
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
        
    
    
    class LayerOptions():
        """
        Layer options for the components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OriginalLayer", "Objects will be placed on original layer"
           "SpecifiedLayer", "Objects will be placed on a user specified layer"
           "Mixed", "Objects are on different layers and will not be changed"
        """
        OriginalLayer = 0  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
        SpecifiedLayer = 1  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
        Mixed = 2  # AssembliesGeneralPropertiesBuilderLayerOptionsMemberType
        
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
        
    
    
    class ReferenceComponentOptions():
        """
        Options for setting the reference-only property on the components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "No", "Objects will be non reference-only components"
           "Yes", "Objects will be reference-only components"
           "Mixed", "Objects are a mixture of reference-only and non reference-only components, and will not be changed"
        """
        No = 0  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
        Yes = 1  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
        Mixed = 2  # AssembliesGeneralPropertiesBuilderReferenceComponentOptionsMemberType
        
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
        
    
    
    class QuantityOptions():
        """
        Options for assigning the quantity on the components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Number", "Use either the integer or real value to set the quantity"
           "AsRequired", "Sets the as-required quantity on this component."
        """
        Number = 0  # AssembliesGeneralPropertiesBuilderQuantityOptionsMemberType
        AsRequired = 1  # AssembliesGeneralPropertiesBuilderQuantityOptionsMemberType
        
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
        
    
    
    def SynchronizeLayers(self) -> None:
        """
        Synchronize the layers on the components 
        
        Signature ``SynchronizeLayers()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SynchronizeDisplay(self) -> None:
        """
        Synchronize the display on the components 
        
        Signature ``SynchronizeDisplay()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SynchronizeAttributes(self) -> None:
        """
        Synchronize the attributes on the components 
        
        Signature ``SynchronizeAttributes()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    Hidden: AssembliesGeneralPropertiesBuilderHiddenOptions = ...
    """
    Returns or sets  the hidden option.  
    
    The hidden option will be "Yes" if all the objects are hidden, 
    "No" if all the objects are not hidden, and "Mixed" if there is a combination. 
    
    <hr>
    
    Getter Method
    
    Signature ``Hidden`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderHiddenOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Hidden`` 
    
    :param hidden: 
    :type hidden: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderHiddenOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    IntegerQuantity: int = ...
    """
    Returns or sets  the integer quantity.  
    
    This value will be used if the Quantity Type is set to Number
    and the DB_UNITS attribute is not set. 
    
    <hr>
    
    Getter Method
    
    Signature ``IntegerQuantity`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IntegerQuantity`` 
    
    :param integerQuantity: 
    :type integerQuantity: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Layer: int = ...
    """
    Returns or sets  the layer.  
    
    Used if the layer option is set to specified. 
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    LayerOption: AssembliesGeneralPropertiesBuilderLayerOptions = ...
    """
    Returns or sets  the layer option.  
    
    If specified layer is set, then the layer will be used. 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderLayerOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerOption`` 
    
    :param layerOption: 
    :type layerOption: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderLayerOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    NonGeometric: bool = ...
    """
    Returns or sets  the non geometric flag.  
    
    Sets the components to either geometric or non-geometric. 
    
    <hr>
    
    Getter Method
    
    Signature ``NonGeometric`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NonGeometric`` 
    
    :param nonGeometric: 
    :type nonGeometric: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    QuantityType: AssembliesGeneralPropertiesBuilderQuantityOptions = ...
    """
    Returns or sets  the quantity type.  
    
    If the quantity type is set to number than either the integer 
    quantity or the real quantity values will be used.  Otherwise the quantity will
    be set to as-required. 
    
    <hr>
    
    Getter Method
    
    Signature ``QuantityType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderQuantityOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``QuantityType`` 
    
    :param quantityType: 
    :type quantityType: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderQuantityOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    RealQuantity: float = ...
    """
    Returns or sets  the real quantity.  
    
    This value will be used if the Quantity Type is set to Number
    and the DB_UNITS attribute has been set. 
    
    <hr>
    
    Getter Method
    
    Signature ``RealQuantity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RealQuantity`` 
    
    :param realQuantity: 
    :type realQuantity: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReferenceComponent: AssembliesGeneralPropertiesBuilderReferenceComponentOptions = ...
    """
    Returns or sets  the reference-only component flag.  
    
    This option determines whether the components will
    be reference-only or not. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderReferenceComponentOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceComponent`` 
    
    :param referenceComponent: 
    :type referenceComponent: :py:class:`NXOpen.Assemblies.AssembliesGeneralPropertiesBuilderReferenceComponentOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SelectedObjects: SelectComponentList = ...
    """
    Returns  the selected object(s) list.  
    
    This is the active list of components that will be
    modified by any changes. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SpecificColor: bool = ...
    """
    Returns or sets  the specific color flag.  
    
    The explicit color display property will be discarded from all
    components. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecificColor`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecificColor`` 
    
    :param specificColor: 
    :type specificColor: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SpecificPartialShade: bool = ...
    """
    Returns or sets  the specific partial shade flag.  
    
    The explicit partial shade display property will be 
    discarded from all components. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecificPartialShade`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecificPartialShade`` 
    
    :param specificPartialShade: 
    :type specificPartialShade: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SpecificTranslucency: bool = ...
    """
    Returns or sets  the specific translucency flag.  
    
    The explicit translucency display property will be 
    discarded from all components. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecificTranslucency`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpecificTranslucency`` 
    
    :param specificTranslucency: 
    :type specificTranslucency: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: AssembliesGeneralPropertiesBuilder = ...  # unknown typename


class ClearanceSetCollection(NXOpen.TaggedObjectCollection):
    """
    Represents :py:class:`NXOpen.Assemblies.ClearanceSetCollection`.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> ClearanceSet:
        """
        Finds the :py:class:`NXOpen.Assemblies.ClearanceSet` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of the software. 
        However newer versions of the software should find the same object when FindObject is passed older versions of its journal identifier. 
        In general, this method should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier. 
        
        Signature ``FindObject(name)`` 
        
        :param name:  Name of the clearance set to be found  
        :type name: str 
        :returns:  the clearance set found, or null if no such clearance set exists. 
        :rtype: :py:class:`NXOpen.Assemblies.ClearanceSet` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CountClearanceSets(self) -> int:
        """
        Determines the number of clearance analysis datasets in the specified part.  
        
        Signature ``CountClearanceSets()`` 
        
        :returns:  the number of clearance sets  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteAllAnalysisData(self) -> None:
        """
        Deletes all clearance analysis data from the given part, including all
        clearance analysis data sets, analysis results, and interference bodies.  
        
        Signature ``DeleteAllAnalysisData()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    


class HideComponentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.HideComponentBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateHideComponentBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Components: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the components to hide 
    
    <hr>
    
    Getter Method
    
    Signature ``Components`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Views: NXOpen.Drawings.SelectDraftingViewList = ...
    """
    Returns  the drafting views from which components to hide 
    
    <hr>
    
    Getter Method
    
    Signature ``Views`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingViewList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: HideComponentBuilder = ...  # unknown typename


class ComponentPatternCollection(NXOpen.TaggedObjectCollection):
    """
    Represents the collection object for all component patterns.  
    
    An instance of this class can be obtained from the :py:class:`NXOpen.Assemblies.ComponentAssembly`.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> ComponentPattern:
        """
        Finds the :py:class:`NXOpen.Assemblies.ComponentPattern` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        An exception will be thrown if no object can be found with the given journal identifier. 
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Name of the component pattern to be found  
        :type journalIdentifier: str 
        :returns:  Component pattern with this identifier, or None if no such pattern exists  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentPattern` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllComponentPatterns(self) -> 'list[ComponentPattern]':
        """
        Returns all the component patterns in an assembly.  
        
        Signature ``GetAllComponentPatterns()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.ComponentPattern` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class ReplaceComponentBuilderComponentReferenceSetMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReplaceComponentBuilderComponentReferenceSet():
    """
    Represents possible reference set for replacement part 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Maintain", "Maintain the reference set of the component being replaced out"
       "EntirePart", "Set the reference set to Entire Part"
       "Empty", "Set the reference to Empty"
       "Others", "Set the specified reference set"
    """
    Maintain = 0  # ReplaceComponentBuilderComponentReferenceSetMemberType
    EntirePart = 1  # ReplaceComponentBuilderComponentReferenceSetMemberType
    Empty = 2  # ReplaceComponentBuilderComponentReferenceSetMemberType
    Others = 3  # ReplaceComponentBuilderComponentReferenceSetMemberType
    
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
    


class ReplaceComponentBuilderComponentLayerOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReplaceComponentBuilderComponentLayerOption():
    """
    Represents possible layer option for replacement part 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Maintain", "Maintain the layer of the component being replaced out"
       "Original", "Set the layer to replacement part's original layer"
       "Work", "Set the layer to current work layer"
       "AsSpecified", "Set the specified layer"
    """
    Maintain = 0  # ReplaceComponentBuilderComponentLayerOptionMemberType
    Original = 1  # ReplaceComponentBuilderComponentLayerOptionMemberType
    Work = 2  # ReplaceComponentBuilderComponentLayerOptionMemberType
    AsSpecified = 3  # ReplaceComponentBuilderComponentLayerOptionMemberType
    
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
    


class ReplaceComponentBuilderComponentNameOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ReplaceComponentBuilderComponentNameOption():
    """
    Represents possible component name option for replace operation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Maintain", "Maintain the component name of the component being replaced out"
       "Original", "Use the replacement part name as the component name"
       "AsSpecified", "Set the specified component name"
    """
    Maintain = 0  # ReplaceComponentBuilderComponentNameOptionMemberType
    Original = 1  # ReplaceComponentBuilderComponentNameOptionMemberType
    AsSpecified = 2  # ReplaceComponentBuilderComponentNameOptionMemberType
    
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
    


class ReplaceComponentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.ReplaceComponentBuilder` builder.  
    
    Input to this class can be PSM facet objects.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateReplaceComponentBuilder`
    
    Default values.
    
    =========================  ============
    Property                   Value
    =========================  ============
    ComponentLayer             1 
    -------------------------  ------------
    ComponentLayerOptionType   Maintain 
    -------------------------  ------------
    ComponentName              
    -------------------------  ------------
    ComponentNameType          AsSpecified 
    -------------------------  ------------
    MaintainRelationships      1 
    -------------------------  ------------
    ReplaceAllOccurrences      0 
    =========================  ============
    
    .. versionadded:: NX6.0.0
    """
    
    class ComponentReferenceSet():
        """
        Represents possible reference set for replacement part 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Maintain", "Maintain the reference set of the component being replaced out"
           "EntirePart", "Set the reference set to Entire Part"
           "Empty", "Set the reference to Empty"
           "Others", "Set the specified reference set"
        """
        Maintain = 0  # ReplaceComponentBuilderComponentReferenceSetMemberType
        EntirePart = 1  # ReplaceComponentBuilderComponentReferenceSetMemberType
        Empty = 2  # ReplaceComponentBuilderComponentReferenceSetMemberType
        Others = 3  # ReplaceComponentBuilderComponentReferenceSetMemberType
        
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
        
    
    
    class ComponentLayerOption():
        """
        Represents possible layer option for replacement part 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Maintain", "Maintain the layer of the component being replaced out"
           "Original", "Set the layer to replacement part's original layer"
           "Work", "Set the layer to current work layer"
           "AsSpecified", "Set the specified layer"
        """
        Maintain = 0  # ReplaceComponentBuilderComponentLayerOptionMemberType
        Original = 1  # ReplaceComponentBuilderComponentLayerOptionMemberType
        Work = 2  # ReplaceComponentBuilderComponentLayerOptionMemberType
        AsSpecified = 3  # ReplaceComponentBuilderComponentLayerOptionMemberType
        
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
        
    
    
    class ComponentNameOption():
        """
        Represents possible component name option for replace operation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Maintain", "Maintain the component name of the component being replaced out"
           "Original", "Use the replacement part name as the component name"
           "AsSpecified", "Set the specified component name"
        """
        Maintain = 0  # ReplaceComponentBuilderComponentNameOptionMemberType
        Original = 1  # ReplaceComponentBuilderComponentNameOptionMemberType
        AsSpecified = 2  # ReplaceComponentBuilderComponentNameOptionMemberType
        
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
        
    
    
    def GetComponentReferenceSetType(self) -> tuple:
        """
        Get the  reference set  
        
        Signature ``GetComponentReferenceSetType()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (componentReferenceSet, referenceSetName). componentReferenceSet is a :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentReferenceSet`. referenceSetName is a str.   Name of the reference set
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComponentReferenceSetType(self, componentReferenceSet: ReplaceComponentBuilderComponentReferenceSet, referenceSetName: str) -> None:
        """
        Set the reference set 
        
        Signature ``SetComponentReferenceSetType(componentReferenceSet, referenceSetName)`` 
        
        :param componentReferenceSet:  Reference set  
        :type componentReferenceSet: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentReferenceSet` 
        :param referenceSetName:  Name of the reference set. Used only when componentReferenceSet is :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentReferenceSet.Others <NXOpen.Assemblies.ReplaceComponentBuilderComponentReferenceSet>`  
        :type referenceSetName: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RegisterReplacePartLoadStatus(self) -> NXOpen.PartLoadStatus:
        """
        Register the part load status with the replace operation.  
        
        If during the operation
        a part could not be loaded, then this object will be used to store error information.
        
        Signature ``RegisterReplacePartLoadStatus()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PartLoadStatus` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetErrorList(self) -> NXOpen.ErrorList:
        """
        Get the list of components that failed to replace with their corresponding error codes.  
        
        Caller need to dispose the error list after processing it.  
        
        Signature ``GetErrorList()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.0.2
        
        License requirements: None.
        """
        ...
    
    AllowTemporaryPartsToReplace: bool = ...
    """
    Returns or sets  the flag to determine whether unsaved parts are allowed to replace.  
    
    If set to true, then this may result in loss of unsaved data.
    
    <hr>
    
    Getter Method
    
    Signature ``AllowTemporaryPartsToReplace`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowTemporaryPartsToReplace`` 
    
    :param allowTemporaryPartsToReplace: 
    :type allowTemporaryPartsToReplace: bool 
    
    .. versionadded:: NX7.5.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentLayer: int = ...
    """
    Returns or sets  the layer for the new replacement part.  
    
      #. -1 means use the original layers defined in the component.
      #. 0 means use the work layer.
      #. 1-256 means use the specified layer.
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentLayer`` 
    
    :param componentLayer: 
    :type componentLayer: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentLayerOptionType: ReplaceComponentBuilderComponentLayerOption = ...
    """
    Returns or sets  the layer options 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentLayerOptionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentLayerOption` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentLayerOptionType`` 
    
    :param componentLayerOption: 
    :type componentLayerOption: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentLayerOption` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentName: str = ...
    """
    Returns or sets  the component name 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentName`` 
    
    :param componentName: 
    :type componentName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentNameType: ReplaceComponentBuilderComponentNameOption = ...
    """
    Returns or sets  the component name options 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentNameType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentNameOption` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentNameType`` 
    
    :param componentNameOption: 
    :type componentNameOption: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilderComponentNameOption` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ComponentsToReplace: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the objects to be replaced.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsToReplace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MaintainRelationships: bool = ...
    """
    Returns or sets  the maintain relationships 
    
    <hr>
    
    Getter Method
    
    Signature ``MaintainRelationships`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaintainRelationships`` 
    
    :param maintainRelationships: 
    :type maintainRelationships: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReplaceAllOccurrences: bool = ...
    """
    Returns or sets  the replace all occurrences 
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceAllOccurrences`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceAllOccurrences`` 
    
    :param replaceAllOccurrences: 
    :type replaceAllOccurrences: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ReplacementPart: str = ...
    """
    Returns or sets  the replacement part.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReplacementPart`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplacementPart`` 
    
    :param replacementPart: 
    :type replacementPart: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ReplaceComponentBuilder = ...  # unknown typename


class Assembly(NXOpen.NXObject):
    """
    Assembly class   
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX6.0.0
    """
    Null: Assembly = ...  # unknown typename


class SubsetCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of subset.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSubsetBuilder(self, subset: Subset) -> SubsetBuilder:
        """
        Creates an :py:class:`NXOpen.Assemblies.SubsetBuilder`  
        
        Signature ``CreateSubsetBuilder(subset)`` 
        
        :param subset:  :py:class:`NXOpen.Assemblies.Subset` to be edited, if None then create a new one  
        :type subset: :py:class:`NXOpen.Assemblies.Subset` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateBoxSearchTermBuilder(self, boxSearchTerm: BoxSearchTerm) -> BoxSearchTermBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.BoxSearchTermBuilder`.  
        
        Signature ``CreateBoxSearchTermBuilder(boxSearchTerm)`` 
        
        :param boxSearchTerm:  :py:class:`NXOpen.Assemblies.BoxSearchTerm` to be edited, if None then create a new one  
        :type boxSearchTerm: :py:class:`NXOpen.Assemblies.BoxSearchTerm` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.BoxSearchTermBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreatePlaneSearchTermBuilder(self, planeSearchTerm: PlaneSearchTerm) -> PlaneSearchTermBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.PlaneSearchTermBuilder`.  
        
        Signature ``CreatePlaneSearchTermBuilder(planeSearchTerm)`` 
        
        :param planeSearchTerm:  :py:class:`NXOpen.Assemblies.PlaneSearchTerm` to be edited, if None then create a new one  
        :type planeSearchTerm: :py:class:`NXOpen.Assemblies.PlaneSearchTerm` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PlaneSearchTermBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateAttributeSearchTermBuilder(self, attributeSearchTerm: AttributeSearchTerm) -> AttributeSearchTermBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.AttributeSearchTermBuilder`.  
        
        Signature ``CreateAttributeSearchTermBuilder(attributeSearchTerm)`` 
        
        :param attributeSearchTerm:  :py:class:`NXOpen.Assemblies.AttributeSearchTerm` to be edited, if None then create a new one  
        :type attributeSearchTerm: :py:class:`NXOpen.Assemblies.AttributeSearchTerm` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.AttributeSearchTermBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateProximitySearchTermBuilder(self, proximitySearchTerm: ProximitySearchTerm) -> ProximitySearchTermBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ProximitySearchTermBuilder`.  
        
        Signature ``CreateProximitySearchTermBuilder(proximitySearchTerm)`` 
        
        :param proximitySearchTerm:  :py:class:`NXOpen.Assemblies.ProximitySearchTerm` to be edited, if None then create a new one  
        :type proximitySearchTerm: :py:class:`NXOpen.Assemblies.ProximitySearchTerm` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProximitySearchTermBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateRunContentProximitySearchTermBuilder(self, runContentProximitySearchTerm: RunContentProximitySearchTerm) -> RunContentProximitySearchTermBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.RunContentProximitySearchTermBuilder`.  
        
        Signature ``CreateRunContentProximitySearchTermBuilder(runContentProximitySearchTerm)`` 
        
        :param runContentProximitySearchTerm:  :py:class:`NXOpen.Assemblies.RunContentProximitySearchTerm` to be edited, if None then create a new one  
        :type runContentProximitySearchTerm: :py:class:`NXOpen.Assemblies.RunContentProximitySearchTerm` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.RunContentProximitySearchTermBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreatePositioningTaskBuilder(self, positioningTask: PositioningTask) -> PositioningTaskBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.PositioningTaskBuilder` 
        
        Signature ``CreatePositioningTaskBuilder(positioningTask)`` 
        
        :param positioningTask: 
        :type positioningTask: :py:class:`NXOpen.Assemblies.PositioningTask` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PositioningTaskBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateMechanicalRoutingSubsetBuilder(self, subsetBuilderTag: SubsetBuilder) -> MechanicalRoutingSubsetBuilder:
        """
        Creates an :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder`.  
        
        The SubsetBuilder parameter is for editing of the existing routing subset. 
        
        Signature ``CreateMechanicalRoutingSubsetBuilder(subsetBuilderTag)`` 
        
        :param subsetBuilderTag: 
        :type subsetBuilderTag: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateMechanicalRoutingSubsetBuilderForSurroundingEdit(self, subsetBuilderTag: SubsetBuilder) -> MechanicalRoutingSubsetBuilder:
        """
        Creates an :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder`.  
        
        The SubsetBuilder parameter is for editing of the existing surrounding subset's recipe. 
        
        Signature ``CreateMechanicalRoutingSubsetBuilderForSurroundingEdit(subsetBuilderTag)`` 
        
        :param subsetBuilderTag: 
        :type subsetBuilderTag: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    


class ComponentGroup(NXOpen.NXObject):
    """
    Represents a Component Group that is defined within an Assembly.  
    
    .. versionadded:: NX5.0.0
    """
    
    def Open(self) -> NXOpen.PartLoadStatus:
        """
        Loads a selected component group by name during Assembly part file open.  
        
        This operation is used in conjunction with the :py:class:`NXOpen.LoadOptions`
        enumerator :py:class:`NXOpen.LoadOptionsLoadComponents` and using the
        specify filter option.
        This method is not intented to be used after an Assembly has been
        loaded but during the loading operations.
        
        Signature ``Open()`` 
        
        :returns:  Parts
        that could not be loaded and their associated errors.  
        :rtype: :py:class:`NXOpen.PartLoadStatus` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def GetComponents(self) -> 'list[Component]':
        """
        Returns the Components within this Component Group  
        
        Signature ``GetComponents()`` 
        
        :returns:  the components  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddComponent(self, component: Component, andChildren: bool) -> None:
        """
        Adds a component to a component group.  
        
        If add chilren is true, the children of the added component
        are also added.
        
        Signature ``AddComponent(component, andChildren)`` 
        
        :param component:  the component to add  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param andChildren:  if true add chilren of component also  
        :type andChildren: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def RemoveComponent(self, component: Component) -> None:
        """
        Removes a component from a component group 
        
        Signature ``RemoveComponent(component)`` 
        
        :param component:  the component to remove  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    NumberOfComponents: int = ...
    """
    Returns  the number of Components within this Component Group 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfComponents`` 
    
    :returns:  the number of Components contained in the group  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: ComponentGroup = ...  # unknown typename


class OrderStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OrderState():
    """
    Represents whether an order is saved or not
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UnSaved", "Order is unsaved"
       "Saved", "Order is saved"
    """
    UnSaved = 0  # OrderStateMemberType
    Saved = 1  # OrderStateMemberType
    
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
    


class OrderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OrderType():
    """
    Represents the type of an order
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefinedComponent", "User defined component order"
       "SequentialComponent", "System defined sequential component order"
       "ChronologicalComponent", "System defined chronological component order"
       "AlphanumericComponent", "System defined alphanumeric component order"
       "AlphabeticComponent", "System defined alphabetic component order"
    """
    UserDefinedComponent = 0  # OrderTypeMemberType
    SequentialComponent = 1  # OrderTypeMemberType
    ChronologicalComponent = 2  # OrderTypeMemberType
    AlphanumericComponent = 3  # OrderTypeMemberType
    AlphabeticComponent = 4  # OrderTypeMemberType
    
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
    


class Order(NXOpen.NXObject):
    """
    Represents base class for all Order classes.  
    
    It is an abstract class and
    cannot be instantiated on its own. All Order classes should inherit from this class.
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    
    class State():
        """
        Represents whether an order is saved or not
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UnSaved", "Order is unsaved"
           "Saved", "Order is saved"
        """
        UnSaved = 0  # OrderStateMemberType
        Saved = 1  # OrderStateMemberType
        
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
        
    
    
    class Type():
        """
        Represents the type of an order
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UserDefinedComponent", "User defined component order"
           "SequentialComponent", "System defined sequential component order"
           "ChronologicalComponent", "System defined chronological component order"
           "AlphanumericComponent", "System defined alphanumeric component order"
           "AlphabeticComponent", "System defined alphabetic component order"
        """
        UserDefinedComponent = 0  # OrderTypeMemberType
        SequentialComponent = 1  # OrderTypeMemberType
        ChronologicalComponent = 2  # OrderTypeMemberType
        AlphanumericComponent = 3  # OrderTypeMemberType
        AlphabeticComponent = 4  # OrderTypeMemberType
        
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
        
    
    
    def GetReversed(self) -> bool:
        """
        Gets the reverse state of the :py:class:`NXOpen.Assemblies.Order` 
        
        Signature ``GetReversed()`` 
        
        :returns:  True if order is reversed else False  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetReversed(self, isReversed: bool) -> None:
        """
        Sets the reverse state of the :py:class:`NXOpen.Assemblies.Order`
        
        Signature ``SetReversed(isReversed)`` 
        
        :param isReversed: 
        :type isReversed: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Activate(self) -> None:
        """
        Applies this order
        
        Signature ``Activate()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Deletes an order 
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves an order
        
        Signature ``Save()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SaveAs(self, newName: str) -> Order:
        """
        Creates a copy of the order, and gives the copy a new name.  
        
        Each :py:class:`NXOpen.Assemblies.ComponentAssembly` contains a set of system defined orders,
        which could be queried using :py:meth:`NXOpen.Assemblies.ComponentAssembly.GetComponentOrders` method.
        A new :py:class:`NXOpen.Assemblies.OrderType.UserDefinedComponent <NXOpen.Assemblies.OrderType>` order can only be created using this method.
        
        Signature ``SaveAs(newName)`` 
        
        :param newName: 
        :type newName: str 
        :returns:  The new Order  
        :rtype: :py:class:`NXOpen.Assemblies.Order` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetChildrenOrder(self, parent: Component) -> 'list[Component]':
        """
        Returns immediate children of input :py:class:`NXOpen.Assemblies.Component`
        as they are ordered in this :py:class:`NXOpen.Assemblies.ComponentOrder` 
        
        Signature ``GetChildrenOrder(parent)`` 
        
        :param parent: 
        :type parent: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  Returns children in order  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Assemblies.ComponentOrder.AskChildrenOrder` instead to get children order in this :py:class:`NXOpen.Assemblies.ComponentOrder`.
        
        License requirements: None.
        """
        ...
    
    
    def IsActive(self) -> bool:
        """
        Returns true if this order is the active order in owning :py:class:`NXOpen.Assemblies.ComponentAssembly`> 
        
        Signature ``IsActive()`` 
        
        :returns:  True if the current order is active 
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    OrderState: OrderState = ...
    """
    Returns  the state of :py:class:`NXOpen.Assemblies.Order`.  
    
    An order can be in one of the 
    :py:class:`NXOpen.Assemblies.OrderState`.
    
    <hr>
    
    Getter Method
    
    Signature ``OrderState`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.OrderState` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    OrderType: OrderType = ...
    """
    Returns  the type of :py:class:`NXOpen.Assemblies.Order`.  
    
    An order can be of
    :py:class:`NXOpen.Assemblies.OrderType` 
    
    <hr>
    
    Getter Method
    
    Signature ``OrderType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.OrderType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: Order = ...  # unknown typename


class PositioningGroupStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PositioningGroupStatus():
    """
    Represents the position status of positioning group 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OutOfDate", " - "
       "UpToDate", " - "
       "Unknown", " - "
    """
    OutOfDate = 0  # PositioningGroupStatusMemberType
    UpToDate = 1  # PositioningGroupStatusMemberType
    Unknown = 2  # PositioningGroupStatusMemberType
    
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
    


class PositioningGroup(NXOpen.NXObject):
    """
    Represents the class for positioning group.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.PositioningGroupBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class Status():
        """
        Represents the position status of positioning group 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OutOfDate", " - "
           "UpToDate", " - "
           "Unknown", " - "
        """
        OutOfDate = 0  # PositioningGroupStatusMemberType
        UpToDate = 1  # PositioningGroupStatusMemberType
        Unknown = 2  # PositioningGroupStatusMemberType
        
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
        
    
    
    def GetStatus(self) -> PositioningGroupStatus:
        """
        Returns status of positioning group.  
        
        The status can be one of 
        :py:class:`NXOpen.Assemblies.PositioningGroupStatus`.
        
        Signature ``GetStatus()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PositioningGroupStatus` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether constraints of member design elements 
    of this positioning group are to be displayed on the graphics window or not.  
    
    (This is a separate system from hiding and showing individual constraints.)
    This flag controls the visibility of both suppressed and unsuppressed constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayConstraints`` 
    
    :param displayConstraints: 
    :type displayConstraints: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DisplaySuppressedConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether suppressed constraints of member design elements 
    of this positioning group are to be displayed on the graphics window or not.  
    
    (This is a separate system from hiding and showing individual constraints.)
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :param displaySuppressedConstraints: 
    :type displaySuppressedConstraints: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: PositioningGroup = ...  # unknown typename


class PartitionList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[Partition]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: Partition) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Assemblies.Partition` 
        
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
    
    
    def FindIndex(self, obj: Partition) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Assemblies.Partition` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> Partition:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Assemblies.Partition` 
        
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
    def Erase(self, obj: Partition) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: Partition, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Assemblies.Partition` 
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
    
    
    def GetContents(self) -> 'list[Partition]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[Partition]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Assemblies.Partition` 
        
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
    def Swap(self, object1: Partition, object2: Partition) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Assemblies.Partition` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: Partition) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Assemblies.Partition` 
        
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
    Null: PartitionList = ...  # unknown typename


class ComponentOrder(Order):
    """
    Represents an order object that stores the order of child :py:class:`NXOpen.Assemblies.Component`s in context
    of parent :py:class:`NXOpen.Assemblies.ComponentAssembly`.  
    
    Typically, an :py:class:`NXOpen.Assemblies.ComponentAssembly` 
    can have multiple :py:class:`NXOpen.Assemblies.ComponentOrder`s and user can switch between 
    :py:class:`NXOpen.Assemblies.ComponentOrder`s to display different order of the assembly in the tree. 
    
    .. versionadded:: NX9.0.0
    """
    
    def AskChildrenOrder(self, parent: Component) -> 'list[Component]':
        """
        Given a parent :py:class:`NXOpen.Assemblies.Component` this method
        returns immediate child :py:class:`NXOpen.Assemblies.Component`s in the same order in
        which they are ordered in this :py:class:`NXOpen.Assemblies.ComponentOrder` 
        
        Signature ``AskChildrenOrder(parent)`` 
        
        :param parent:  :py:class:`NXOpen.Assemblies.Component` whose children are required  
        :type parent: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  Children of :py:class:`NXOpen.Assemblies.Component`   
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ComponentOrder = ...  # unknown typename


class Arrangement(NXOpen.NXObject):
    """
    Manages the suppression of :py:class:`NXOpen.Assemblies.Component`s within a
    :py:class:`NXOpen.Assemblies.ComponentAssembly`.  
    
    Currently, an Arrangement simply acts as a
    context within which a Component can be suppressed, unsuppressed, or positioned. 
    
    To create an :py:class:`NXOpen.Assemblies.Arrangement`, use the :py:class:`NXOpen.Assemblies.ArrangementCollection` class.
    
    An isolated :py:class:`NXOpen.Assemblies.Arrangement` is an :py:class:`NXOpen.Assemblies.Arrangement` that is capable of supporting 
    isolated positions and isolated position overrides. 
    
    A standard :py:class:`NXOpen.Assemblies.Arrangement` is an :py:class:`NXOpen.Assemblies.Arrangement` that does not support isolated 
    position or isolated position overrides. All :py:class:`NXOpen.Assemblies.Arrangement`s created in NX 8.5 or earlier are standard :py:class:`NXOpen.Assemblies.Arrangement`s.
    
    .. versionadded:: NX3.0.0
    """
    
    def Delete(self, forgetPositioning: bool) -> None:
        """
        Delete the given :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        If the forget_positioning flag is set to
        TRUE then components will not maintain their positions, otherwise variable component positioning
        will be created to maintain the components current positions.  If the part containing the 
        :py:class:`NXOpen.Assemblies.Arrangement` is not already fully loaded this method will cause it to be. 
        
        Signature ``Delete(forgetPositioning)`` 
        
        :param forgetPositioning:  If TRUE then components will not maintain their position. 
        :type forgetPositioning: bool 
        
        .. versionadded:: NX7.5.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetMaintainsConstraints(self) -> bool:
        """
        Get whether this :py:class:`NXOpen.Assemblies.Arrangement` is currently used in the session.  
        
        If it is, it will be kept up to date.
        
        Signature ``GetMaintainsConstraints()`` 
        
        :returns:  Whether this :py:class:`NXOpen.Assemblies.Arrangement` is currently used in the session. 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetHasPostponedConstraints(self) -> bool:
        """
        Get whether this :py:class:`NXOpen.Assemblies.Arrangement` has postponed its solve.  
        
        The solving of constraints is postponed in an :py:class:`NXOpen.Assemblies.Arrangement` that is not currently used in the session.
        The constraints will solve when the component positions in the :py:class:`NXOpen.Assemblies.Arrangement` are needed.
        
        Signature ``GetHasPostponedConstraints()`` 
        
        :returns:  Whether this :py:class:`NXOpen.Assemblies.Arrangement` has postponed solving its constraints. 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SolvePostponedConstraints(self) -> None:
        """
        Forces a postponed :py:class:`NXOpen.Assemblies.Arrangement`, that is not currently used in the session,
        to solve its constraints.  
        
        This could lead to updating the model if required. 
        
        Signature ``SolvePostponedConstraints()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def IsIsolated(self) -> bool:
        """
        Get whether this :py:class:`NXOpen.Assemblies.Arrangement` is isolated.  
        
        An isolated :py:class:`NXOpen.Assemblies.Arrangement` is an :py:class:`NXOpen.Assemblies.Arrangement` that is capable of supporting 
        isolated positions and isolated position overrides. 
        
        Signature ``IsIsolated()`` 
        
        :returns:  Whether this :py:class:`NXOpen.Assemblies.Arrangement` is isolated. 
        :rtype: bool 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    IgnoringConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether this :py:class:`NXOpen.Assemblies.Arrangement` is ignoring constraints.  
    
    <hr>
    
    Getter Method
    
    Signature ``IgnoringConstraints`` 
    
    :returns:  Whether this :py:class:`NXOpen.Assemblies.Arrangement` is ignoring all constraints. 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``IgnoringConstraints`` 
    
    :param isIgnoreConstraints:  Whether this :py:class:`NXOpen.Assemblies.Arrangement` is ignoring all constraints. 
    :type isIgnoreConstraints: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Owner: ComponentAssembly = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.ComponentAssembly` which owns this arrangement 
    
    <hr>
    
    Getter Method
    
    Signature ``Owner`` 
    
    :returns:  The :py:class:`NXOpen.Assemblies.ComponentAssembly` which owns this Arrangement  
    :rtype: :py:class:`NXOpen.Assemblies.ComponentAssembly` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Null: Arrangement = ...  # unknown typename


class ComponentGroupCollection(NXOpen.TaggedObjectCollection):
    """
    Contains a collection of Component Groups a :py:class:`NXOpen.Assemblies.ComponentGroup`
    that are defined within an Assembly part.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> ComponentGroup:
        """
        Finds the :py:class:`NXOpen.Assemblies.ComponentGroup` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the ComponentGroup you want  
        :type journalIdentifier: str 
        :returns:  ComponentGroup with this identifier  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentGroup` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateComponentGroup(self, name: str) -> ComponentGroup:
        """
        Creates a :py:class:`NXOpen.Assemblies.ComponentGroup` with the given name  
        
        Signature ``CreateComponentGroup(name)`` 
        
        :param name:  Name for the ComponentGroup  
        :type name: str 
        :returns:  the ComponentGroup created  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentGroup` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    


class PositioningGroupBuilder(NXOpen.Builder):
    """
    Represents builder class for positioning group which is used to store constraints for design element.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreatePositioningGroupBuilder`
    
    Default values.
    
    ===========  =====
    Property     Value
    ===========  =====
    MakeActive   1 
    ===========  =====
    
    .. versionadded:: NX10.0.0
    """
    MakeActive: bool = ...
    """
    Returns or sets  the option to specify whether a newly created positioning group 
    should be made active after creation or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``MakeActive`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MakeActive`` 
    
    :param makeActive: 
    :type makeActive: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    OwningPositioningTask: PositioningTask = ...
    """
    Returns or sets  the owning positioning task.  
    
    During creation set method should be called with the positioning task
    in which new :py:class:`NXOpen.Assemblies.PositioningGroup` has to be created. During edit operation set 
    method should not be called. An error would be raised if during edit operation set method is called with a positioning task
    which is different from the owning positioning task of :py:class:`NXOpen.Assemblies.PositioningGroup`.
    
    <hr>
    
    Getter Method
    
    Signature ``OwningPositioningTask`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.PositioningTask` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OwningPositioningTask`` 
    
    :param positioningTask:  This parameter may not be None. 
    :type positioningTask: :py:class:`NXOpen.Assemblies.PositioningTask` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PositioningGroupDataMembers: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the members for positioning group 
    
    <hr>
    
    Getter Method
    
    Signature ``PositioningGroupDataMembers`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    PositioningGroupName: str = ...
    """
    Returns or sets  the name of positioning group.  
    
    The user of this API is responcible to free the text pointer 
    
    <hr>
    
    Getter Method
    
    Signature ``PositioningGroupName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PositioningGroupName`` 
    
    :param nameOfPositioningGroup: 
    :type nameOfPositioningGroup: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: PositioningGroupBuilder = ...  # unknown typename


class CopyDesignElementBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that performs copying design element operation in 4GD.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreateCopyDesignElementBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the pre-creation objects 
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the pre-creation objects which have unassign required attributes
        
        Signature ``GetLogicalObjectsHavingUnassignedRequiredAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns the design element copy operation failures  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PartiallyCommit(self) -> None:
        """
        Copy design elements with minimal required information.  
        
        Call to builder Commit is required after this to Commit creation.
        
        Signature ``PartiallyCommit()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateDesignElementLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Creates the pre-creation objects for the design elements to be copied 
        
        Signature ``CreateDesignElementLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def DeleteCopiedComponents(self) -> None:
        """
        Removes the copied components created during the copy operation 
        
        Signature ``DeleteCopiedComponents()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DesignElementsToCopy: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the design elements to copy 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementsToCopy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: CopyDesignElementBuilder = ...  # unknown typename


class AssembliesChildRevisionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssembliesChildRevisionOptions():
    """
    Child revision options
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AllRevisions", "show all revisions of the child parts"
       "UseRevRule", "show revision of the child parts based on the revision rule"
       "LatestRevisionWithRelation", "show the latest revision of the child part that has an interpart relation"
    """
    AllRevisions = 0  # AssembliesChildRevisionOptionsMemberType
    UseRevRule = 1  # AssembliesChildRevisionOptionsMemberType
    LatestRevisionWithRelation = 2  # AssembliesChildRevisionOptionsMemberType
    
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
    


class ProximitySearchTermBuilder(SearchTermBuilder):
    """
    A ProximitySearchTermBuilder is used to create or edit an :py:class:`Assemblies.BoxSearchTerm`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateProximitySearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def GetSeeds(self) -> 'list[SearchResultElement]':
        """
        Get the proximity search term seed elements.  
        
        Signature ``GetSeeds()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.SearchResultElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetSeeds(self, seeds: 'list[SearchResultElement]') -> None:
        """
        Set the proximity search term seed elements.  
        
        Signature ``SetSeeds(seeds)`` 
        
        :param seeds: 
        :type seeds: list of :py:class:`NXOpen.Assemblies.SearchResultElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Distance: float = ...
    """
    Returns or sets  
    the distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Distance`` 
    
    :param distance: 
    :type distance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchTermLogic: SearchTermSearchTermLogicType = ...
    """
    Returns or sets  
    the search term logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTermLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTermLogic`` 
    
    :param searchTermLogic: 
    :type searchTermLogic: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TrueShapeRefinement: bool = ...
    """
    Returns or sets  
    the true-shape refinement.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :param trueShapeRefinement: 
    :type trueShapeRefinement: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: ProximitySearchTermBuilder = ...  # unknown typename


class LoadInterpartDataBuilderSelectionScopeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LoadInterpartDataBuilderSelectionScopeType():
    """
    Represents the load interpart selection scope types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AllPartsInDisplayedAssembly", "Load interpart data for all parts in displayed assembly"
       "AllPartsInSession", "Load interpart data for all parts in session"
    """
    AllPartsInDisplayedAssembly = 0  # LoadInterpartDataBuilderSelectionScopeTypeMemberType
    AllPartsInSession = 1  # LoadInterpartDataBuilderSelectionScopeTypeMemberType
    
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
    


class LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LoadInterpartDataBuilderOpenUnloadedParentsType():
    """
    Represents the load interpart parent level types
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Load all partially loaded parts that contain links and all immediate level parents parts if they are partially loaded"
       "ImmediateLevel", "Load all partially loaded parts that contain links and all immediate level parents parts regardless of load status"
       "AllLevels", "Load all partially loaded parts that contain links and all level parent parts regardless of load status"
    """
    NotSet = 0  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
    ImmediateLevel = 1  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
    AllLevels = 2  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
    
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
    


class LoadInterpartDataBuilder(NXOpen.Builder):
    """
    Represents a builder:py:class:`NXOpen.Assemblies.LoadInterpartDataBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateLoadInterpartDataBuilder`
    
    Default values.
    
    ====================  ============================
    Property              Value
    ====================  ============================
    OpenUnloadedParents   None 
    --------------------  ----------------------------
    SelectionScope        AllPartsInDisplayedAssembly 
    ====================  ============================
    
    .. versionadded:: NX6.0.0
    """
    
    class SelectionScopeType():
        """
        Represents the load interpart selection scope types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AllPartsInDisplayedAssembly", "Load interpart data for all parts in displayed assembly"
           "AllPartsInSession", "Load interpart data for all parts in session"
        """
        AllPartsInDisplayedAssembly = 0  # LoadInterpartDataBuilderSelectionScopeTypeMemberType
        AllPartsInSession = 1  # LoadInterpartDataBuilderSelectionScopeTypeMemberType
        
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
        
    
    
    class OpenUnloadedParentsType():
        """
        Represents the load interpart parent level types
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Load all partially loaded parts that contain links and all immediate level parents parts if they are partially loaded"
           "ImmediateLevel", "Load all partially loaded parts that contain links and all immediate level parents parts regardless of load status"
           "AllLevels", "Load all partially loaded parts that contain links and all level parent parts regardless of load status"
        """
        NotSet = 0  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
        ImmediateLevel = 1  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
        AllLevels = 2  # LoadInterpartDataBuilderOpenUnloadedParentsTypeMemberType
        
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
        
    
    
    def GetFailedParts(self) -> 'list[NXOpen.BasePart]':
        """
        Returns an array of the parts that failed to load and update  
        
        Signature ``GetFailedParts()`` 
        
        :returns:  Array of the part tags failed to 
        load and update 
        :rtype: list of :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLoadInterpartDataStatus(self, part: NXOpen.BasePart) -> tuple:
        """
        Returns part load status and delayed update status for the part which failed to load and update
        
        Signature ``GetLoadInterpartDataStatus(part)`` 
        
        :param part:  Failed part tag 
        :type part: :py:class:`NXOpen.BasePart` 
        :returns: a tuple 
        :rtype: A tuple consisting of (loadStatus, delayedUpdateStatus). loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Part load status for the failed partdelayedUpdateStatus is a :py:class:`NXOpen.PartDelayedUpdateStatus`.   Delayed update status data status for the failed part
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    OpenUnloadedParents: LoadInterpartDataBuilderOpenUnloadedParentsType = ...
    """
    Returns or sets  the open unloaded parents level type 
    
    <hr>
    
    Getter Method
    
    Signature ``OpenUnloadedParents`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilderOpenUnloadedParentsType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OpenUnloadedParents`` 
    
    :param openUnloadedParents: 
    :type openUnloadedParents: :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilderOpenUnloadedParentsType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SelectionScope: LoadInterpartDataBuilderSelectionScopeType = ...
    """
    Returns or sets  the selection scope type
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilderSelectionScopeType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionScope`` 
    
    :param selectionScope: 
    :type selectionScope: :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilderSelectionScopeType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    Null: LoadInterpartDataBuilder = ...  # unknown typename


class SearchResultCollection(NXOpen.TaggedObjectCollection):
    """
    A collection of :py:class:`NXOpen.Assemblies.SearchResultElement`s.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.SubsetBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> SearchResultElement:
        """
        Finds the :py:class:`NXOpen.Assemblies.SearchResultElement` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Name of the search result to be found  
        :type journalIdentifier: str 
        :returns:  Element found, or null if no such search result element exists. 
        :rtype: :py:class:`NXOpen.Assemblies.SearchResultElement` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    


class AttributeSearchTermBuilder(SearchTermBuilder):
    """
    An AttributeSearchTermBuilder is used to create or edit an :py:class:`NXOpen.Assemblies.AttributeSearchTerm`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateAttributeSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def GetCriteria(self) -> tuple:
        """
        Get the entry titles and values that are used to populate the saved query.  
        
        Signature ``GetCriteria()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (titles, values). titles is a list of str.   search criteria titles values is a list of str.   search criteria values 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetCriteria(self, titles: 'list[str]', values: 'list[str]') -> None:
        """
        Set the entry titles and values that are used to populate the saved query.  
        
        Signature ``SetCriteria(titles, values)`` 
        
        :param titles:  search criteria titles  
        :type titles: list of str 
        :param values:  search criteria values  
        :type values: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    QueryName: str = ...
    """
    Returns or sets  the name of the saved query upon which this search term is based.  
    
    <hr>
    
    Getter Method
    
    Signature ``QueryName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``QueryName`` 
    
    :param queryName: 
    :type queryName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchTermLogic: SearchTermSearchTermLogicType = ...
    """
    Returns or sets  the search term logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTermLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTermLogic`` 
    
    :param searchTermLogic: 
    :type searchTermLogic: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: AttributeSearchTermBuilder = ...  # unknown typename


class UpdateDesignElementPositionBuilder(NXOpen.Builder):
    """
    Represents the builder class that updates positions of the DE's(Shape/Reuse) or Subordinates with override that are out of date.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreateUpdateDesignElementPositionBuilder`
    
    .. versionadded:: NX10.0.0
    """
    DesignElementsToUpdatePosition: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the objects for update position 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementsToUpdatePosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: UpdateDesignElementPositionBuilder = ...  # unknown typename


class DesignElementBuilderOperationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderOperationType():
    """
    Represents an operation type that can be performed on a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Create", "Creates a design element"
       "Edit", "Edits a design element"
       "SaveAs", "Save as a design element"
       "Save", "Saves a design element"
       "SaveAndClose", "Saves a design element and if it is a reuse closes the reused part"
       "Undefined", " - "
    """
    Create = 0  # DesignElementBuilderOperationTypeMemberType
    Edit = 1  # DesignElementBuilderOperationTypeMemberType
    SaveAs = 2  # DesignElementBuilderOperationTypeMemberType
    Save = 3  # DesignElementBuilderOperationTypeMemberType
    SaveAndClose = 4  # DesignElementBuilderOperationTypeMemberType
    Undefined = 5  # DesignElementBuilderOperationTypeMemberType
    
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
    


class DesignElementBuilderEditActionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderEditActionType():
    """
    Represents the edit action on a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Category", " - "
       "Partitions", " - "
       "Effectivity", " - "
    """
    Category = 0  # DesignElementBuilderEditActionTypeMemberType
    Partitions = 1  # DesignElementBuilderEditActionTypeMemberType
    Effectivity = 2  # DesignElementBuilderEditActionTypeMemberType
    
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
    


class DesignElementBuilderSaveAsActionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderSaveAsActionType():
    """
    Represents the save as action on a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NewRevision", " - "
       "NewDesignElement", " - "
    """
    NewRevision = 0  # DesignElementBuilderSaveAsActionTypeMemberType
    NewDesignElement = 1  # DesignElementBuilderSaveAsActionTypeMemberType
    
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
    


class DesignElementBuilderStateTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderStateType():
    """
    Represents the state of a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Shape", "Shape design element"
       "Reuse", "Reuse design element"
       "Promissory", "Promissory design element"
    """
    Shape = 0  # DesignElementBuilderStateTypeMemberType
    Reuse = 1  # DesignElementBuilderStateTypeMemberType
    Promissory = 2  # DesignElementBuilderStateTypeMemberType
    
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
    


class DesignElementBuilderReferenceSetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderReferenceSetType():
    """
    Represents the reference set of a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Model", "Model"
       "EntirePart", "Entire part"
       "AsSpecified", "As specified reference set"
    """
    Model = 0  # DesignElementBuilderReferenceSetTypeMemberType
    EntirePart = 1  # DesignElementBuilderReferenceSetTypeMemberType
    AsSpecified = 2  # DesignElementBuilderReferenceSetTypeMemberType
    
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
    


class DesignElementBuilderLayerOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderLayerOptionType():
    """
    Represents the layer option of a design element 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Original", "Original layer"
       "Work", "Work layer"
       "AsSpecified", "As specified layer"
    """
    Original = 0  # DesignElementBuilderLayerOptionTypeMemberType
    Work = 1  # DesignElementBuilderLayerOptionTypeMemberType
    AsSpecified = 2  # DesignElementBuilderLayerOptionTypeMemberType
    
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
    


class DesignElementBuilderPositioningOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignElementBuilderPositioningOption():
    """
    Represents the positioning option of a design element.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AbsoluteOrigin", "Applies absolute origin position on the design elements"
       "Maintain", "Maintains the existing positions of the design elements. Applicable only if the edit action type is set to :py:class:`DesignElementBuilderEditActionType.Category <DesignElementBuilderEditActionType>`"
       "AsSpecified", "Applies the specified position on the design elements"
    """
    AbsoluteOrigin = 0  # DesignElementBuilderPositioningOptionMemberType
    Maintain = 1  # DesignElementBuilderPositioningOptionMemberType
    AsSpecified = 2  # DesignElementBuilderPositioningOptionMemberType
    
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
    


class DesignElementBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a builder class that performs various design element operations.  
    
    The operation can be one of :py:class:`NXOpen.Assemblies.DesignElementBuilderOperationType` 
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreateDesignElementBuilder`
    
    Default values.
    
    ==========================  ============
    Property                    Value
    ==========================  ============
    EditAction                  Partitions 
    --------------------------  ------------
    KeepOriginalDesignElement   0 
    --------------------------  ------------
    LayerOption                 Original 
    --------------------------  ------------
    PositioningOptionValue      Maintain 
    --------------------------  ------------
    ReferenceSet                EntirePart 
    --------------------------  ------------
    SaveAsAction                NewRevision 
    ==========================  ============
    
    .. versionadded:: NX8.5.0
    """
    
    class OperationType():
        """
        Represents an operation type that can be performed on a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Create", "Creates a design element"
           "Edit", "Edits a design element"
           "SaveAs", "Save as a design element"
           "Save", "Saves a design element"
           "SaveAndClose", "Saves a design element and if it is a reuse closes the reused part"
           "Undefined", " - "
        """
        Create = 0  # DesignElementBuilderOperationTypeMemberType
        Edit = 1  # DesignElementBuilderOperationTypeMemberType
        SaveAs = 2  # DesignElementBuilderOperationTypeMemberType
        Save = 3  # DesignElementBuilderOperationTypeMemberType
        SaveAndClose = 4  # DesignElementBuilderOperationTypeMemberType
        Undefined = 5  # DesignElementBuilderOperationTypeMemberType
        
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
        
    
    
    class EditActionType():
        """
        Represents the edit action on a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Category", " - "
           "Partitions", " - "
           "Effectivity", " - "
        """
        Category = 0  # DesignElementBuilderEditActionTypeMemberType
        Partitions = 1  # DesignElementBuilderEditActionTypeMemberType
        Effectivity = 2  # DesignElementBuilderEditActionTypeMemberType
        
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
        
    
    
    class SaveAsActionType():
        """
        Represents the save as action on a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NewRevision", " - "
           "NewDesignElement", " - "
        """
        NewRevision = 0  # DesignElementBuilderSaveAsActionTypeMemberType
        NewDesignElement = 1  # DesignElementBuilderSaveAsActionTypeMemberType
        
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
        
    
    
    class StateType():
        """
        Represents the state of a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Shape", "Shape design element"
           "Reuse", "Reuse design element"
           "Promissory", "Promissory design element"
        """
        Shape = 0  # DesignElementBuilderStateTypeMemberType
        Reuse = 1  # DesignElementBuilderStateTypeMemberType
        Promissory = 2  # DesignElementBuilderStateTypeMemberType
        
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
        
    
    
    class ReferenceSetType():
        """
        Represents the reference set of a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Model", "Model"
           "EntirePart", "Entire part"
           "AsSpecified", "As specified reference set"
        """
        Model = 0  # DesignElementBuilderReferenceSetTypeMemberType
        EntirePart = 1  # DesignElementBuilderReferenceSetTypeMemberType
        AsSpecified = 2  # DesignElementBuilderReferenceSetTypeMemberType
        
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
        
    
    
    class LayerOptionType():
        """
        Represents the layer option of a design element 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Original", "Original layer"
           "Work", "Work layer"
           "AsSpecified", "As specified layer"
        """
        Original = 0  # DesignElementBuilderLayerOptionTypeMemberType
        Work = 1  # DesignElementBuilderLayerOptionTypeMemberType
        AsSpecified = 2  # DesignElementBuilderLayerOptionTypeMemberType
        
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
        
    
    
    class PositioningOption():
        """
        Represents the positioning option of a design element.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AbsoluteOrigin", "Applies absolute origin position on the design elements"
           "Maintain", "Maintains the existing positions of the design elements. Applicable only if the edit action type is set to :py:class:`DesignElementBuilderEditActionType.Category <DesignElementBuilderEditActionType>`"
           "AsSpecified", "Applies the specified position on the design elements"
        """
        AbsoluteOrigin = 0  # DesignElementBuilderPositioningOptionMemberType
        Maintain = 1  # DesignElementBuilderPositioningOptionMemberType
        AsSpecified = 2  # DesignElementBuilderPositioningOptionMemberType
        
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
        
    
    
    def GetPosition(self) -> tuple:
        """
        Gets the position of design element 
        
        Signature ``GetPosition()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (position, orientation). position is a :py:class:`NXOpen.Point3d`. orientation is a :py:class:`NXOpen.Matrix3x3`. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPosition(self, position: NXOpen.Point3d, orientation: NXOpen.Matrix3x3) -> None:
        """
        Sets the position of design element.  
        
        This value is used only when positioning option is 
        :py:class:`DesignElementBuilderPositioningOption.AsSpecified <DesignElementBuilderPositioningOption>`
        
        Signature ``SetPosition(position, orientation)`` 
        
        :param position: 
        :type position: :py:class:`NXOpen.Point3d` 
        :param orientation: 
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetAddPartitions(self) -> 'list[Partition]':
        """
        Get the partitions to which the design elements will be added.  
        
        Signature ``GetAddPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddToPartitions(self, partitions: 'list[Partition]') -> None:
        """
        Specify partitions to which the design elements will be added.  
        
        The design elements
        will remain a member of any partitions to which they already belongs. The partitions
        to which the design elements will be added accumulate if this method is called more
        than once.  If both :py:meth:`Assemblies.DesignElementBuilder.AddToPartitions`
        and :py:meth:`Assemblies.DesignElementBuilder.RemoveFromPartitions` are called
        with the same partition then the design elements will be added or removed from that partition
        depending upon which was the last method called.
        
        Signature ``AddToPartitions(partitions)`` 
        
        :param partitions: 
        :type partitions: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetRemovePartitions(self) -> 'list[Partition]':
        """
        Get the partitions from which the design elements will be removed.  
        
        Signature ``GetRemovePartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveFromPartitions(self, partitions: 'list[Partition]') -> None:
        """
        Specify partitions from which the design elements will be removed.  
        
        The partitions
        from which the design elements will be removed accumulate if this method is called more
        than once.  If both :py:meth:`Assemblies.DesignElementBuilder.AddToPartitions`
        and :py:meth:`Assemblies.DesignElementBuilder.RemoveFromPartitions` are called
        with the same partition then the design elements will be added or removed from that partition
        depending upon which was the last method called.
        
        Signature ``RemoveFromPartitions(partitions)`` 
        
        :param partitions: 
        :type partitions: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Creates the pre-creation objects for the design elements 
        
        Signature ``CreateLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def PartiallyCommit(self, logicalObjects: 'list[NXOpen.PDM.LogicalObject]') -> None:
        """
        Equivalent to builder Commit call but this one would create design elements with minimal required 
        information.  
        
        Can be used only when this :py:class:`NXOpen.Assemblies.DesignElementBuilder` has 
        been created with :py:class:`NXOpen.Assemblies.DesignElementBuilderOperationType.Create <NXOpen.Assemblies.DesignElementBuilderOperationType>`. 
        Call to builder Commit is required after this to Commit creation.
        
        Signature ``PartiallyCommit(logicalObjects)`` 
        
        :param logicalObjects: 
        :type logicalObjects: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
        Returns design element operation failures  
        
        Signature ``GetOperationFailures()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Count: int = ...
    """
    Returns or sets  the number of design elements to be created.  
    
    Applicable only if the operation type is set to 
    :py:class:`DesignElementBuilderOperationType.Create <DesignElementBuilderOperationType>`
    
    <hr>
    
    Getter Method
    
    Signature ``Count`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Count`` 
    
    :param count: 
    :type count: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DesignElementType: str = ...
    """
    Returns or sets  the type of a design element
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementType`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DesignElementType`` 
    
    :param deType: 
    :type deType: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DesignElementsToOperate: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the design elements to operate upon 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElementsToOperate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    EditAction: DesignElementBuilderEditActionType = ...
    """
    Returns or sets  the edit action type on a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``EditAction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderEditActionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EditAction`` 
    
    :param actionType: 
    :type actionType: :py:class:`NXOpen.Assemblies.DesignElementBuilderEditActionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Effectivity: NXOpen.BasicEffectivityBuilder = ...
    """
    Returns  the effectivity interface of a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``Effectivity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BasicEffectivityBuilder` 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Assemblies.DesignElementBuilder.EffectivityTable` instead.
    
    License requirements: None.
    """
    EffectivityTable: NXOpen.PDM.EffectivityTableBuilder = ...
    """
    Returns  the effectivity interface of a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``EffectivityTable`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FileNewDescriptor: NXOpen.FileNew = ...
    """
    Returns  the file new descriptor to identify a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``FileNewDescriptor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.FileNew` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    KeepOriginalDesignElement: bool = ...
    """
    Returns or sets  the option determines whether to keep the original design element in the subset during save as
    
    <hr>
    
    Getter Method
    
    Signature ``KeepOriginalDesignElement`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``KeepOriginalDesignElement`` 
    
    :param valueType: 
    :type valueType: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Layer: int = ...
    """
    Returns or sets  the layer value of a design element.  
    
    Applicable only if the layer option is set to 
    :py:class:`DesignElementBuilderLayerOptionType.AsSpecified <DesignElementBuilderLayerOptionType>`
    
    <hr>
    
    Getter Method
    
    Signature ``Layer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Layer`` 
    
    :param layer: 
    :type layer: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    LayerOption: DesignElementBuilderLayerOptionType = ...
    """
    Returns or sets  the layer option of a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``LayerOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderLayerOptionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LayerOption`` 
    
    :param layerOption: 
    :type layerOption: :py:class:`NXOpen.Assemblies.DesignElementBuilderLayerOptionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    OwningSubsetInstance: Subset = ...
    """
    Returns or sets  the owning subset instance
    
    <hr>
    
    Getter Method
    
    Signature ``OwningSubsetInstance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OwningSubsetInstance`` 
    
    :param subsetInstance: 
    :type subsetInstance: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PartToUse: NXOpen.BasePart = ...
    """
    Returns or sets  the part to use of a reuse design element.  
    
    Applicable only if the state is set to 
    :py:class:`DesignElementBuilderStateType.Reuse <DesignElementBuilderStateType>`
    
    <hr>
    
    Getter Method
    
    Signature ``PartToUse`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PartToUse`` 
    
    :param partToUse: 
    :type partToUse: :py:class:`NXOpen.BasePart` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PositioningOptionValue: DesignElementBuilderPositioningOption = ...
    """
    Returns or sets  the positioning option of a design element
    
    <hr>
    
    Getter Method
    
    Signature ``PositioningOptionValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderPositioningOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PositioningOptionValue`` 
    
    :param positioningOption: 
    :type positioningOption: :py:class:`NXOpen.Assemblies.DesignElementBuilderPositioningOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ReferenceSet: DesignElementBuilderReferenceSetType = ...
    """
    Returns or sets  the reference set of a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderReferenceSetType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSet`` 
    
    :param referenceSet: 
    :type referenceSet: :py:class:`NXOpen.Assemblies.DesignElementBuilderReferenceSetType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ReferenceSetName: str = ...
    """
    Returns or sets  the reference set name of a design element.  
    
    Applicable only if the reference set is
    set to :py:class:`DesignElementBuilderReferenceSetType.AsSpecified <DesignElementBuilderReferenceSetType>`
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSetName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSetName`` 
    
    :param referenceSetName: 
    :type referenceSetName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SaveAsAction: DesignElementBuilderSaveAsActionType = ...
    """
    Returns or sets  the save as action type of a design element 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveAsAction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderSaveAsActionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveAsAction`` 
    
    :param actionType: 
    :type actionType: :py:class:`NXOpen.Assemblies.DesignElementBuilderSaveAsActionType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Scatter: bool = ...
    """
    Returns or sets  the option to determine whether to scatter design elements during creation
    
    <hr>
    
    Getter Method
    
    Signature ``Scatter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Scatter`` 
    
    :param scatterValue: 
    :type scatterValue: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    State: DesignElementBuilderStateType = ...
    """
    Returns or sets  the state of a design element
    
    <hr>
    
    Getter Method
    
    Signature ``State`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DesignElementBuilderStateType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``State`` 
    
    :param state: 
    :type state: :py:class:`NXOpen.Assemblies.DesignElementBuilderStateType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: DesignElementBuilder = ...  # unknown typename


class SubsetPartitionViewStyleTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubsetPartitionViewStyleType():
    """
    Represents the type of partition view style to show for a subset.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Show no partition view style for subset"
       "Flat", "Show flat partition view style for subset"
       "Hierarchical", "Show hierachical view style for subset"
    """
    NotSet = 0  # SubsetPartitionViewStyleTypeMemberType
    Flat = 1  # SubsetPartitionViewStyleTypeMemberType
    Hierarchical = 2  # SubsetPartitionViewStyleTypeMemberType
    
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
    


class SubsetContentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubsetContentType():
    """
    Represents the content type for a subset.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Public", "Represents a public content subset"
       "Baseline", "Represents a baseline content subset"
       "ChangeNotice", "Represents a change notice content subset"
    """
    Public = 0  # SubsetContentTypeMemberType
    Baseline = 1  # SubsetContentTypeMemberType
    ChangeNotice = 2  # SubsetContentTypeMemberType
    
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
    


class Subset(NXOpen.NXObject):
    """
    A subset is a set of design elements within a collaborative design.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.SubsetBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class PartitionViewStyleType():
        """
        Represents the type of partition view style to show for a subset.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Show no partition view style for subset"
           "Flat", "Show flat partition view style for subset"
           "Hierarchical", "Show hierachical view style for subset"
        """
        NotSet = 0  # SubsetPartitionViewStyleTypeMemberType
        Flat = 1  # SubsetPartitionViewStyleTypeMemberType
        Hierarchical = 2  # SubsetPartitionViewStyleTypeMemberType
        
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
        
    
    
    class ContentType():
        """
        Represents the content type for a subset.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Public", "Represents a public content subset"
           "Baseline", "Represents a baseline content subset"
           "ChangeNotice", "Represents a change notice content subset"
        """
        Public = 0  # SubsetContentTypeMemberType
        Baseline = 1  # SubsetContentTypeMemberType
        ChangeNotice = 2  # SubsetContentTypeMemberType
        
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
        
    
    
    def ReplayRecipe(self) -> None:
        """
        Replay this subset.  
        
        This will perform a search using the current subset recipe 
        and configuration.  The contents of the subset will be changed accordingly.
        
        Signature ``ReplayRecipe()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveDesignElements(self, designElements: 'list[NXOpen.NXObject]') -> None:
        """
        Removes the design elements from this subset.  
        
        This will not delete the design element from the
        owning :py:class:`NXOpen.CollaborativeDesign`.
        
        Signature ``RemoveDesignElements(designElements)`` 
        
        :param designElements: 
        :type designElements: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def DeleteFromCollaborativeDesign(self, designElement: 'list[NXOpen.NXObject]') -> None:
        """
        Deletes the design elements from the owning :py:class:`NXOpen.CollaborativeDesign`.  
        
        Signature ``DeleteFromCollaborativeDesign(designElement)`` 
        
        :param designElement: 
        :type designElement: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddInterpartParents(self) -> None:
        """
        Add sources of interpart relationships (wave links in the subset and Connected To relationships for design features)
        that are not in the specified subset to the subset recipe.  
        
        The recipe will be modified and explicit include terms will be added for each parent.
        The modified recipe will be replayed at the end of the operation. 
        
        Signature ``AddInterpartParents()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddConnectedByElements(self) -> None:
        """
        Add Elements to a subset that reference the existing Design Elements in it by a Connection relation.  
        
        A typical example will be to add Weld Design Features that reference any of the Design Elements in this subset.
        The recipe will be modified and explicit include terms will be added for each Element.
        The modified recipe will be replayed at the end of the operation. 
        See :py:meth:`NXOpen.Assemblies.Subset.AddInterpartParents`" 
        
        Signature ``AddConnectedByElements()`` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddAllChildrenToSubset(self, reuseDesignElements: 'list[Component]') -> None:
        """
        Adds all the child components of the selected Reuse Design Element to the owning subset.  
        
        Signature ``AddAllChildrenToSubset(reuseDesignElements)`` 
        
        :param reuseDesignElements: 
        :type reuseDesignElements: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddNewChildrenToSubset(self) -> None:
        """
        If the Reuse Design Elements in the subset contain any new components which were not added
        to the subset because its owning workset was not the displayed part at the time of creation,
        then add those new components to the subset now.  
        
        Signature ``AddNewChildrenToSubset()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetDesignElementRevisionMembers(self) -> 'list[NXOpen.PDM.DesignElementRevision]':
        """
        The :py:class:`NXOpen.PDM.DesignElementRevision`s that are members of this subset.  
        
        Note that this does not include elements that have been loaded only because they contain
        a :py:class:`NXOpen.PDM.DesignSubordinateRevision` that belongs to this subset.
        See :py:meth:`GetDesignElementRevisionParents`
        
        Signature ``GetDesignElementRevisionMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.DesignElementRevision` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetDesignElementRevisionParents(self) -> 'list[NXOpen.PDM.DesignElementRevision]':
        """
        The :py:class:`NXOpen.PDM.DesignElementRevision`s that have been loaded because they contain
        a :py:class:`NXOpen.PDM.DesignSubordinateRevision` that belongs to this subset.  
        
        Signature ``GetDesignElementRevisionParents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.DesignElementRevision` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetDesignSubordinateRevisionMembers(self) -> 'list[NXOpen.PDM.DesignSubordinateRevision]':
        """
        The :py:class:`NXOpen.PDM.DesignSubordinateRevision`s that are members of this subset.  
        
        Note that this does not include elements that have been loaded only because they contain
        a :py:class:`NXOpen.PDM.DesignSubordinateRevision` that belongs to this subset.
        See :py:meth:`GetDesignSubordinateRevisionParents`
        
        Signature ``GetDesignSubordinateRevisionMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.DesignSubordinateRevision` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetDesignSubordinateRevisionParents(self) -> 'list[NXOpen.PDM.DesignSubordinateRevision]':
        """
        The :py:class:`NXOpen.PDM.DesignSubordinateRevision`s that have been loaded because they contain
        a :py:class:`NXOpen.PDM.DesignSubordinateRevision` that belongs to this subset.  
        
        Signature ``GetDesignSubordinateRevisionParents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.DesignSubordinateRevision` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def ShowCollaborativeDesignPreview(self) -> bool:
        """
        Displays the preview for the Collaborative Design in the graphics window.  
        
        The preview is stored as a JT dataset on the Collaborative Design. 
        Any transformation specific to this subset will also be applied to the preview. 
        isPreviewAvailable will be false if no JT dataset could be found. 
        See :py:meth:`HideCollaborativeDesignPreview`. 
        
        Signature ``ShowCollaborativeDesignPreview()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.1
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def HideCollaborativeDesignPreview(self) -> None:
        """
        Hides the preview for the Collaborative Design in the graphics window if it was 
        already displayed.  
        
        See :py:meth:`ShowCollaborativeDesignPreview`. 
        
        Signature ``HideCollaborativeDesignPreview()`` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def IsCollaborativeDesignPreviewDisplayed(self) -> bool:
        """
        Is the preview for the Collaborative Design being displayed in the Graphics window.  
        
        Signature ``IsCollaborativeDesignPreviewDisplayed()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.5.1
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetTargetPartitionSet(self) -> 'list[Partition]':
        """
        Gets the list of array of target partitions that are set on the subsetInstance
        
        Signature ``GetTargetPartitionSet()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetTargetPartitionSet(self, partitions: 'list[Partition]') -> None:
        """
        Sets the list of array of target partitions on the subsetInstance
        
        Signature ``SetTargetPartitionSet(partitions)`` 
        
        :param partitions: 
        :type partitions: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetAllPositioningTasks(self) -> 'list[PositioningTask]':
        """
        Gets all :py:class:`NXOpen.Assemblies.PositioningTask` 
        that belong to this subset.  
        
        Signature ``GetAllPositioningTasks()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.PositioningTask` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeletePositioningTask(self, positioningTask: PositioningTask) -> None:
        """
        Deletes the :py:class:`NXOpen.Assemblies.PositioningTask` from this subset.  
        
        Signature ``DeletePositioningTask(positioningTask)`` 
        
        :param positioningTask: 
        :type positioningTask: :py:class:`NXOpen.Assemblies.PositioningTask` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> None:
        """
        Set a new :py:class:`NXOpen.ContentDefinition` object on the Subset.  
        
        Signature ``SetContentDefinition(contentDefinition)`` 
        
        :param contentDefinition: 
        :type contentDefinition: :py:class:`NXOpen.ContentDefinition` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def ReplaceContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> None:
        """
        Replace the :py:class:`NXOpen.ContentDefinition` object on the Subset.  
        
        Signature ``ReplaceContentDefinition(contentDefinition)`` 
        
        :param contentDefinition: 
        :type contentDefinition: :py:class:`NXOpen.ContentDefinition` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CanReplaceContentDefinition(self, contentDefinition: NXOpen.ContentDefinition) -> bool:
        """
        Checks if the :py:class:`NXOpen.ContentDefinition` object on the Subset can be replaced with the specified :py:class:`NXOpen.ContentDefinition` object.  
        
        Signature ``CanReplaceContentDefinition(contentDefinition)`` 
        
        :param contentDefinition: 
        :type contentDefinition: :py:class:`NXOpen.ContentDefinition` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddDesignElementsToSubset(self, designElements: 'list[NXOpen.PDM.ModelElementRevision]') -> NXOpen.PartLoadStatus:
        """
        Adds the specified :py:class:`NXOpen.PDM.ModelElementRevision`s as members of the subset.  
        
        The subset recipe will be edited to include these elements with explicit include terms. 
        A replay of the entire recipe will not be performed. The specified elements will be appended to the 
        subset. 
        See :py:meth:`NXOpen.Assemblies.Subset.ReplayRecipe`
        
        Signature ``AddDesignElementsToSubset(designElements)`` 
        
        :param designElements: 
        :type designElements: list of :py:class:`NXOpen.PDM.ModelElementRevision` 
        :returns: 
        :rtype: :py:class:`NXOpen.PartLoadStatus` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    AllowMultipleTargetPartitions: bool = ...
    """
    Returns or sets  
    the allow multiple target partitions property, if set to false (default) only first target partition will be considered
    
    <hr>
    
    Getter Method
    
    Signature ``AllowMultipleTargetPartitions`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``AllowMultipleTargetPartitions`` 
    
    :param allowMultiplePartitions: 
    :type allowMultiplePartitions: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ComponentInWorkset: Component = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.Component` that corresponds to this subset in 
    the workset :py:class:`NXOpen.Assemblies.ComponentAssembly`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentInWorkset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Description: str = ...
    """
    Returns  the description of this subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DisplayExcludedDesignElements: bool = ...
    """
    Returns or sets  the design elements excluded from spatial search to be displayed or not
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayExcludedDesignElements`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayExcludedDesignElements`` 
    
    :param displayExcluded: 
    :type displayExcluded: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PartitionViewStyle: SubsetPartitionViewStyleType = ...
    """
    Returns or sets  
    the partition view style to show.  
    
    <hr>
    
    Getter Method
    
    Signature ``PartitionViewStyle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetPartitionViewStyleType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``PartitionViewStyle`` 
    
    :param partitionViewStyle: 
    :type partitionViewStyle: :py:class:`NXOpen.Assemblies.SubsetPartitionViewStyleType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ShowSubsetStructure: bool = ...
    """
    Returns or sets  
    the subset structure to be shown or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSubsetStructure`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSubsetStructure`` 
    
    :param showSubsetStructure: 
    :type showSubsetStructure: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SubsetType: SubsetContentType = ...
    """
    Returns  the type of plm object used to create subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetContentType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: Subset = ...  # unknown typename


class PositioningTaskBuilder(NXOpen.Builder):
    """
    Represents the class for positioning task builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreatePositioningTaskBuilder`
    
    .. versionadded:: NX10.0.0
    """
    ContextCollection: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the context collection 
    
    <hr>
    
    Getter Method
    
    Signature ``ContextCollection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OwningSubset: Subset = ...
    """
    Returns or sets  the owning subset.  
    
    During creation set method should be called with the subset instance
    in which new :py:class:`NXOpen.Assemblies.PositioningTask` has to be created. During edit operation set 
    method should not be called. An error would be raised if during edit operation set method is called with a subset instance 
    which is different from the owning subset instance of :py:class:`NXOpen.Assemblies.PositioningTask`.
    
    <hr>
    
    Getter Method
    
    Signature ``OwningSubset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OwningSubset`` 
    
    :param subsetInstance:  This parameter may not be None. 
    :type subsetInstance: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    WorkCollection: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the work collection 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkCollection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: PositioningTaskBuilder = ...  # unknown typename


class AbsolutePositionBuilder(NXOpen.Builder):
    """
    Represents a builder class that absolutely positions the specified objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.CreateAbsolutePositionBuilder`
    
    .. versionadded:: NX10.0.0
    """
    AbsolutelyPosition: bool = ...
    """
    Returns or sets  the option to know whether the object is absolutely positioned or not
    
    <hr>
    
    Getter Method
    
    Signature ``AbsolutelyPosition`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AbsolutelyPosition`` 
    
    :param absolutePositioned: 
    :type absolutePositioned: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ObjectsToAbsolutePosition: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the object list selected for absolute position 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectsToAbsolutePosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: AbsolutePositionBuilder = ...  # unknown typename


class ExplodedComponent(Component):
    """
    Represents a :py:class:`NXOpen.Assemblies.Component` within an explosion.  
    
    Use the :py:class:`NXOpen.Assemblies.Explosion` and :py:class:`NXOpen.Assemblies.Component` to create an exploded component.
    
    .. versionadded:: NX9.0.1
    """
    
    def GetExplosion(self) -> Explosion:
        """
        Gets the :py:class:`NXOpen.Assemblies.Explosion` associated with the exploded component.  
        
        Signature ``GetExplosion()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Explosion` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetComponent(self) -> Component:
        """
        Gets the :py:class:`NXOpen.Assemblies.Component` associated with the exploded component.  
        
        Signature ``GetComponent()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: ExplodedComponent = ...  # unknown typename


class RunContentProximitySearchTerm(SearchTerm):
    """
    A proximity search term within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.RunContentProximitySearchTermBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Null: RunContentProximitySearchTerm = ...  # unknown typename


class DeleteOverridePartBuilder(NXOpen.Builder):
    """
    Represents a builder class that deletes override part in the specified design elements.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CollaborativeContentManager.DeleteOverridePartBuilder`
    
    .. versionadded:: NX10.0.0
    """
    ComponentSelectionList: SelectComponentList = ...
    """
    Returns  the list that contains components of reuse design element or subordinates
    of which override part is to be deleted.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentSelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: DeleteOverridePartBuilder = ...  # unknown typename


class CollaborativeContentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CollaborativeContentType():
    """
    Represents the collaborative content type corresponding to this component
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Workset", "Workset"
       "Subset", "Subset"
       "ShapeDesignElement", "Shape Design Element in a Workset"
       "ReuseDesignElement", "Reuse Design Element in a Workset"
       "PromissoryDesignElement", "Promissory Design Element in a Workset"
       "Subordinate", "Subordinate Design Element in a Workset"
       "DesignFeature", "Design Feature"
       "DesignControlElement", "Design Control Element"
       "NotAssigned", "Non-collaborative content such as items"
    """
    Workset = 0  # CollaborativeContentTypeMemberType
    Subset = 1  # CollaborativeContentTypeMemberType
    ShapeDesignElement = 2  # CollaborativeContentTypeMemberType
    ReuseDesignElement = 3  # CollaborativeContentTypeMemberType
    PromissoryDesignElement = 4  # CollaborativeContentTypeMemberType
    Subordinate = 5  # CollaborativeContentTypeMemberType
    DesignFeature = 6  # CollaborativeContentTypeMemberType
    DesignControlElement = 7  # CollaborativeContentTypeMemberType
    NotAssigned = 8  # CollaborativeContentTypeMemberType
    
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
    


class ComponentAssemblySubstitutionModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblySubstitutionMode():
    """
    Defines how a component substitution operation is performed.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NonAssociative", "The old component is deleted, and the new one is added"
       "SingleComponent", "An associative substitution is performed. As far as possible, this will attempt to preserve assembly constraints and interpart links."
       "All", "An associative substitution is performed on all components that represent the same prototype part. This effectively substitutes one child part for a new one."
    """
    NonAssociative = 0  # ComponentAssemblySubstitutionModeMemberType
    SingleComponent = 1  # ComponentAssemblySubstitutionModeMemberType
    All = 2  # ComponentAssemblySubstitutionModeMemberType
    
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
    


class ComponentAssemblyOpenOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblyOpenOption():
    """
    Open options for open_components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ComponentOnly", "Open the component but none of its children"
       "ImmediateChildren", "Open the immediate children of an already open component"
       "WholeAssembly", "Open the component and all of its children"
       "ReapplyRevRule", "Reconfigure and open components based on current revision rules. If this option is used in native mode, it will behave just like Open Component."
    """
    ComponentOnly = 0  # ComponentAssemblyOpenOptionMemberType
    ImmediateChildren = 1  # ComponentAssemblyOpenOptionMemberType
    WholeAssembly = 2  # ComponentAssemblyOpenOptionMemberType
    ReapplyRevRule = 3  # ComponentAssemblyOpenOptionMemberType
    
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
    


class ComponentAssemblyOpenComponentStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblyOpenComponentStatus():
    """
    Open Component Status 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SuccessfullyOpened", "The component was opened as expected"
       "DeletedByOpen", "The component was deleted on load as a result of the open"
       "CouldNotOpen", "The component could not be opened"
    """
    SuccessfullyOpened = 0  # ComponentAssemblyOpenComponentStatusMemberType
    DeletedByOpen = 1  # ComponentAssemblyOpenComponentStatusMemberType
    CouldNotOpen = 2  # ComponentAssemblyOpenComponentStatusMemberType
    
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
    


class ComponentAssemblyCheckinCheckoutOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblyCheckinCheckoutOption():
    """
    Check in and Check out options for components 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DesignElement", "Checks in or Checks out the design element"
       "SourceItem", "Checks in or Checks out the source item that is referenced by a reuse design element or subordinate design element"
       "Both", "Checks in or Checks out the design element and its referenced source item"
       "Default", "Check In or Check Out option is determined by the system using whatever option is appropriate for the selected object type. For Reuse design element, the system defaults to checking out both the design element and the underlying item."
    """
    DesignElement = 0  # ComponentAssemblyCheckinCheckoutOptionMemberType
    SourceItem = 1  # ComponentAssemblyCheckinCheckoutOptionMemberType
    Both = 2  # ComponentAssemblyCheckinCheckoutOptionMemberType
    Default = 3  # ComponentAssemblyCheckinCheckoutOptionMemberType
    
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
    


class ComponentAssemblyCloseModifiedMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblyCloseModified():
    """
    Indicates how close component should handle component parts when they are modified 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "False", "Close only unmodified parts, not modified parts"
       "True", "Close all parts, modified and unmodified"
    """
    FalseValue = 0  # ComponentAssemblyCloseModifiedMemberType
    TrueValue = 1  # ComponentAssemblyCloseModifiedMemberType
    
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
    


class ComponentAssemblySuppressedStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblySuppressedState():
    """
    Defines the component supression states.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inherit", "Inherit"
       "Suppressed", "Suppressed"
       "Unsuppressed", "Unsuppressed"
       "SuppressedByExp", "Suppressed by expression"
       "UnsuppressedByExp", "Unsuppressed by expression"
    """
    Inherit = 0  # ComponentAssemblySuppressedStateMemberType
    Suppressed = 1  # ComponentAssemblySuppressedStateMemberType
    Unsuppressed = 2  # ComponentAssemblySuppressedStateMemberType
    SuppressedByExp = 3  # ComponentAssemblySuppressedStateMemberType
    UnsuppressedByExp = 4  # ComponentAssemblySuppressedStateMemberType
    
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
    


class ComponentAssemblyOrderTargetLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentAssemblyOrderTargetLocation():
    """
    Option controls whether reordered :py:class:`NXOpen.Assemblies.Component`s are placed 
    before or after the target :py:class:`NXOpen.Assemblies.Component`
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PlaceBefore", "Move reordered :py:class:`NXOpen.Assemblies.Component`s before the target :py:class:`NXOpen.Assemblies.Component`"
       "PlaceAfter", "Move reordered :py:class:`NXOpen.Assemblies.Component`s after the target :py:class:`NXOpen.Assemblies.Component`"
    """
    PlaceBefore = 0  # ComponentAssemblyOrderTargetLocationMemberType
    PlaceAfter = 1  # ComponentAssemblyOrderTargetLocationMemberType
    
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
    


class ComponentAssembly(NXOpen.NXObject):
    """
    Represents the set of :py:class:`NXOpen.Assemblies.Component`s that make up an
    assembly.  
    
    Components are arranged in a tree structure, with a single component at the
    root. (See :py:meth:`NXOpen.Assemblies.ComponentAssembly.RootComponent`.) The
    components directly below the root are added to this assembly by calling
    :py:meth:`NXOpen.Assemblies.ComponentAssembly.AddComponent`. These "Top Level" components are
    said to be owned directly by this assembly. Top Level components may themselves have
    subcomponents.
    
    Certain methods in this class will only operate on Top Level components. For example,
    :py:meth:`NXOpen.Assemblies.ComponentAssembly.MoveComponent` will throw an exception if the
    input component is not owned directly by this assembly.  
    
    Note, however, that input components will be mapped onto the correct component in the
    assembly. See :py:meth:`NXOpen.Assemblies.ComponentAssembly.MapComponentFromParent`.
    
    For any methods that specify a component's position, the orientation matrix is in column order. 
    The first column of the matrix specifies the X axis, the second the Y axis, and the third the Z
    axis.
    
    To obtain an instance of this class, use :py:meth:`NXOpen.BasePart.ComponentAssembly`
    
    .. versionadded:: NX3.0.0
    """
    
    class SubstitutionMode():
        """
        Defines how a component substitution operation is performed.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NonAssociative", "The old component is deleted, and the new one is added"
           "SingleComponent", "An associative substitution is performed. As far as possible, this will attempt to preserve assembly constraints and interpart links."
           "All", "An associative substitution is performed on all components that represent the same prototype part. This effectively substitutes one child part for a new one."
        """
        NonAssociative = 0  # ComponentAssemblySubstitutionModeMemberType
        SingleComponent = 1  # ComponentAssemblySubstitutionModeMemberType
        All = 2  # ComponentAssemblySubstitutionModeMemberType
        
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
        
    
    
    class OpenOption():
        """
        Open options for open_components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ComponentOnly", "Open the component but none of its children"
           "ImmediateChildren", "Open the immediate children of an already open component"
           "WholeAssembly", "Open the component and all of its children"
           "ReapplyRevRule", "Reconfigure and open components based on current revision rules. If this option is used in native mode, it will behave just like Open Component."
        """
        ComponentOnly = 0  # ComponentAssemblyOpenOptionMemberType
        ImmediateChildren = 1  # ComponentAssemblyOpenOptionMemberType
        WholeAssembly = 2  # ComponentAssemblyOpenOptionMemberType
        ReapplyRevRule = 3  # ComponentAssemblyOpenOptionMemberType
        
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
        
    
    
    class OpenComponentStatus():
        """
        Open Component Status 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SuccessfullyOpened", "The component was opened as expected"
           "DeletedByOpen", "The component was deleted on load as a result of the open"
           "CouldNotOpen", "The component could not be opened"
        """
        SuccessfullyOpened = 0  # ComponentAssemblyOpenComponentStatusMemberType
        DeletedByOpen = 1  # ComponentAssemblyOpenComponentStatusMemberType
        CouldNotOpen = 2  # ComponentAssemblyOpenComponentStatusMemberType
        
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
        
    
    
    class CheckinCheckoutOption():
        """
        Check in and Check out options for components 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DesignElement", "Checks in or Checks out the design element"
           "SourceItem", "Checks in or Checks out the source item that is referenced by a reuse design element or subordinate design element"
           "Both", "Checks in or Checks out the design element and its referenced source item"
           "Default", "Check In or Check Out option is determined by the system using whatever option is appropriate for the selected object type. For Reuse design element, the system defaults to checking out both the design element and the underlying item."
        """
        DesignElement = 0  # ComponentAssemblyCheckinCheckoutOptionMemberType
        SourceItem = 1  # ComponentAssemblyCheckinCheckoutOptionMemberType
        Both = 2  # ComponentAssemblyCheckinCheckoutOptionMemberType
        Default = 3  # ComponentAssemblyCheckinCheckoutOptionMemberType
        
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
        
    
    
    class CloseModified():
        """
        Indicates how close component should handle component parts when they are modified 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "False", "Close only unmodified parts, not modified parts"
           "True", "Close all parts, modified and unmodified"
        """
        FalseValue = 0  # ComponentAssemblyCloseModifiedMemberType
        TrueValue = 1  # ComponentAssemblyCloseModifiedMemberType
        
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
        
    
    
    class SuppressedState():
        """
        Defines the component supression states.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inherit", "Inherit"
           "Suppressed", "Suppressed"
           "Unsuppressed", "Unsuppressed"
           "SuppressedByExp", "Suppressed by expression"
           "UnsuppressedByExp", "Unsuppressed by expression"
        """
        Inherit = 0  # ComponentAssemblySuppressedStateMemberType
        Suppressed = 1  # ComponentAssemblySuppressedStateMemberType
        Unsuppressed = 2  # ComponentAssemblySuppressedStateMemberType
        SuppressedByExp = 3  # ComponentAssemblySuppressedStateMemberType
        UnsuppressedByExp = 4  # ComponentAssemblySuppressedStateMemberType
        
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
        
    
    
    class OrderTargetLocation():
        """
        Option controls whether reordered :py:class:`NXOpen.Assemblies.Component`s are placed 
        before or after the target :py:class:`NXOpen.Assemblies.Component`
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PlaceBefore", "Move reordered :py:class:`NXOpen.Assemblies.Component`s before the target :py:class:`NXOpen.Assemblies.Component`"
           "PlaceAfter", "Move reordered :py:class:`NXOpen.Assemblies.Component`s after the target :py:class:`NXOpen.Assemblies.Component`"
        """
        PlaceBefore = 0  # ComponentAssemblyOrderTargetLocationMemberType
        PlaceAfter = 1  # ComponentAssemblyOrderTargetLocationMemberType
        
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
        
    
    
    @typing.overload
    def AddComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> tuple:
        """
        Creates a new :py:class:`NXOpen.Assemblies.Component` in this assembly, based on an existing part file.
        
        Signature ``AddComponent(partToAdd, referenceSetName, componentName, basePoint, orientation, layer)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: str 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.  
        :type layer: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the                                                                                    part_to_add 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def AddComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, uomAsNgc: bool) -> tuple:
        """
        Creates a new :py:class:`NXOpen.Assemblies.Component` in this assembly, based on an existing part file.
        
        Signature ``AddComponent(partToAdd, referenceSetName, componentName, basePoint, orientation, layer, uomAsNgc)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: str 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.  
        :type layer: int 
        :param uomAsNgc:  Whether to set to non-geometric if with unit-of-measure  
        :type uomAsNgc: bool 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the                                                                                    part_to_add 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def AddComponent(self, partToAdd: NXOpen.BasePart, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> tuple:
        """
        Creates a new :py:class:`NXOpen.Assemblies.Component` in this assembly, based on an existing part file.
        
        Signature ``AddComponent(partToAdd, referenceSetName, componentName, basePoint, orientation, layer)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: :py:class:`NXOpen.BasePart` 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.  
        :type layer: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the                                                                                    part_to_add 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddComponents(self, partsToAdd: 'list[NXOpen.Part]', point: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, referenceSetName: str, count: int, scatter: bool) -> 'list[Component]':
        """
        Creates new :py:class:`NXOpen.Assemblies.Component` in this assembly, based on existing part files.  
        
        Signature ``AddComponents(partsToAdd, point, orientation, layer, referenceSetName, count, scatter)`` 
        
        :param partsToAdd:  The parts that define new components  
        :type partsToAdd: list of :py:class:`NXOpen.Part` 
        :param point:  Location of the new component  
        :type point: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.  
        :type layer: int 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param count:   number of times each part to be added as component in parent part   
        :type count: int 
        :param scatter:  Scatter the multiple components around the specified location  
        :type scatter: bool 
        :returns:  The array of components added to the parent part  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def AddMasterPartComponent(self, partToAdd: str, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> tuple:
        """
        Creates a new :py:class:`NXOpen.Assemblies.Component` in this assembly as master part.
        
        Signature ``AddMasterPartComponent(partToAdd, referenceSetName, componentName, basePoint, orientation, layer)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: str 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.                                          
        :type layer: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the part_to_add 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def AddMasterPartComponent(self, partToAdd: NXOpen.Part, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int) -> tuple:
        """
        Creates a new :py:class:`NXOpen.Assemblies.Component` in this assembly as master part.
        
        Signature ``AddMasterPartComponent(partToAdd, referenceSetName, componentName, basePoint, orientation, layer)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: :py:class:`NXOpen.Part` 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.                                          
        :type layer: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the part_to_add 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def InsertProduct(self, productPart: NXOpen.Part, layer: int) -> tuple:
        """
        Adds a product into workset part at identity location.  
        
        Signature ``InsertProduct(productPart, layer)`` 
        
        :param productPart:  The product being added to the workset  
        :type productPart: :py:class:`NXOpen.Part` 
        :param layer:   The layer to place the new component on                                                      -1 means use the original layers defined in the component.                                                     0 means use the work layer.                                                     1-256 means use the specified layer.                                                   
        :type layer: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (component, loadStatus). component is a :py:class:`NXOpen.Assemblies.Component`.   The new Component loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   Result of loading the                                                                                    part_to_add 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SubstituteComponent(self, component: Component, part: NXOpen.BasePart, newName: str, referenceSet: str, layer: int, mode: ComponentAssemblySubstitutionMode) -> Component:
        """
        Substitutes an old component with a new component.  
        
        The new component represents a new part, but 
        will be placed in the same location as the original.
        
        Signature ``SubstituteComponent(component, part, newName, referenceSet, layer, mode)`` 
        
        :param component:  The old component to be substituted.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param part:  The new part  
        :type part: :py:class:`NXOpen.BasePart` 
        :param newName:  The name for the new component  
        :type newName: str 
        :param referenceSet:  The name of the reference set for the new component  
        :type referenceSet: str 
        :param layer:  The layer for the new component                                                     -1 means use the original layers defined in the component.                                                    0 means use the work layer                                                    1-256 means use the specified layer.                                               
        :type layer: int 
        :param mode:  Defines the substitution mode  
        :type mode: :py:class:`NXOpen.Assemblies.ComponentAssemblySubstitutionMode` 
        :returns:  The new Component that replaces the old one.  
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveComponent(self, component: Component) -> None:
        """
        Removes a component from this assemebly.  
        
        Signature ``RemoveComponent(component)`` 
        
        :param component:  The component to remove. Must be directly owned by this assembly.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def MapComponentFromParent(self, component: Component) -> Component:
        """
        Maps a component in a parent assembly onto a corresponding component in this
        assembly.  
        
        For example, given an Axle assembly: 
        
        Axle
        /      \          
        /        \         
        Left        Right     
        Wheel       Wheel     
        
        and a Car assembly containing two Axle components:
        
        Car
        _______ |_______                   
        /                \                  
        /                  \                 
        Front                     Rear            
        Axle                      Axle            
        /      \                  /      \          
        /        \                /        \         
        Front Left  Front Right    Rear Left   Rear Right 
        Wheel       Wheel         Wheel       Wheel     
        
        then calling Axle.MapComponentFromParent with the Front Left Wheel component will
        return the Left Wheel component. Note that calling Car.MapComponentFromParent on
        Left Wheel will not work. See :py:meth:`NXOpen.Assemblies.ComponentAssembly.MapComponentsFromSubassembly`.
        
        Calling Axle.MapComponent with the Left Wheel component will simply return Left
        Wheel, i.e. it is a null operation.
        
        Note that calling this method may load additional assembly data from the Axle part. 
        
        Signature ``MapComponentFromParent(component)`` 
        
        :param component:  The component to map. This should be defined in the                                                                    tree of a parent assembly which contains this assembly.                                                                 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The mapped component. This will be defined in the
        component tree of this assembly parameter.
        
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MapComponentsFromSubassembly(self, component: Component) -> 'list[Component]':
        """
        Maps a component in a subassembly onto the corresponding components in this
        parent assembly.  
        
        For example, given an Axle assembly: 
        
        Axle
        /      \          
        /        \         
        Left        Right     
        Wheel       Wheel     
        
        and a Car assembly containing two Axle components:
        
        Car
        _______ |_______                   
        /                \                  
        /                  \                 
        Front                     Rear            
        Axle                      Axle            
        /      \                  /      \          
        /        \                /        \         
        Front Left  Front Right    Rear Left   Rear Right 
        Wheel       Wheel         Wheel       Wheel     
        
        then calling Car.MapComponentsFromSubassembly on Left Wheel will return
        Front Left Wheel and Rear Left Wheel.
        See also :py:meth:`NXOpen.Assemblies.ComponentAssembly.MapComponentFromParent`.
        
        Signature ``MapComponentsFromSubassembly(component)`` 
        
        :param component:  The component to map. This must be defined in a subassembly                                                                            of this assembly.                                                                          
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The mapped components. 
        
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ChangeByName(self, name: str, partOccs: 'list[Component]') -> None:
        """
        Changes the current :py:class:`NXOpen.Assemblies.Arrangement` of the given :py:class:`NXOpen.Assemblies.Component`s to the
        :py:class:`NXOpen.Assemblies.Arrangement` with the given name.  
        
        Signature ``ChangeByName(name, partOccs)`` 
        
        :param name:  The name of arrangement to change to  
        :type name: str 
        :param partOccs:  The :py:class:`NXOpen.Assemblies.Component`s to be modified  
        :type partOccs: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetDefault(self, arrangement: Arrangement) -> None:
        """
        Set the default :py:class:`NXOpen.Assemblies.Arrangement` for the given :py:class:`NXOpen.Assemblies.ComponentAssembly`.  
        
        Signature ``SetDefault(arrangement)`` 
        
        :param arrangement:  The new default :py:class:`NXOpen.Assemblies.Arrangement`.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        
        .. versionadded:: NX7.5.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def SuppressComponents(self, components: 'list[Component]', arrangements: 'list[Arrangement]') -> NXOpen.ErrorList:
        """
        Suppresses an array of components
        
        Signature ``SuppressComponents(components, arrangements)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be suppressed  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param arrangements:  Arrangements in which components should be suppressed.                                                                                          These arrangements must be defined in this ComponentAssembly                                                                                        
        :type arrangements: list of :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  list of errors encountered during the suppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def SuppressComponents(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Suppresses an array of components in all :py:class:`NXOpen.Assemblies.Arrangement` s in this ComponentAssembly
        
        Signature ``SuppressComponents(components)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be suppressed  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the suppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def SuppressComponents(self, components: 'list[Component]', arrangements: 'list[Arrangement]', expression: str) -> NXOpen.ErrorList:
        """
        Suppresses an array of components in all :py:class:`NXOpen.Assemblies.Arrangement` s in this ComponentAssembly
        
        Signature ``SuppressComponents(components, arrangements, expression)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be suppressed  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param arrangements:  Arrangements in which components should be unsuppressed  
        :type arrangements: list of :py:class:`NXOpen.Assemblies.Arrangement` 
        :param expression:  Suppress components if expression evalutes zero else unsuppress components  
        :type expression: str 
        :returns:  list of errors encountered during the suppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def UnsuppressComponents(self, components: 'list[Component]', arrangements: 'list[Arrangement]') -> NXOpen.ErrorList:
        """
        Unsuppresses an array of components in this ComponentAssembly
        
        Signature ``UnsuppressComponents(components, arrangements)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be unsuppressed  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param arrangements:  Arrangements in which components should be unsuppressed.                                                                                          These arrangements must be defined in this ComponentAssembly                                                                                        
        :type arrangements: list of :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  list of errors encountered during the unsuppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def UnsuppressComponents(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Unsuppresses an array of components in all :py:class:`NXOpen.Assemblies.Arrangement` s in this ComponentAssembly
        
        Signature ``UnsuppressComponents(components)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be unsuppressed  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the unsuppress  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def ReleaseSuppression(self, components: 'list[Component]', arrangements: 'list[Arrangement]') -> NXOpen.ErrorList:
        """
        Release control of the suppression state of an array of components. The components
        will no longer have their suppression state controlled by the given arrangements. (Note
        that it is not an error if the given arrangements do not control the components.)
        
        Signature ``ReleaseSuppression(components, arrangements)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be released  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param arrangements:  Arrangements in which components should be released.                                                                                          These arrangements must be defined in this ComponentAssembly                                                                                        
        :type arrangements: list of :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  list of errors encountered during the release  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def ReleaseSuppression(self, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Release control of the suppression state of an array of components. The components
        will no longer have their suppression state controlled by any of the arrangements
        in the ComponentAssembly.
        
        Signature ``ReleaseSuppression(components)`` 
        
        :param components:  :py:class:`NXOpen.Assemblies.Component`s to be released  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the release  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetEntirePartRefset(self, component: Component) -> None:
        """
        Convenience method for setting the reference set used to represent a component
        to be the entire part.  
        
        Signature ``SetEntirePartRefset(component)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEmptyRefset(self, component: Component) -> None:
        """
        Convenience method for setting the reference set used to represent a component
        to be empty
        
        Signature ``SetEmptyRefset(component)`` 
        
        :param component:  The component to edit.  Must be directly owned by this assembly.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReplaceReferenceSetInOwners(self, newReferenceSet: str, components: 'list[Component]') -> NXOpen.ErrorList:
        """
        Sets the reference set used to represent each component in an array.  
        
        This is the equivalent of calling:
        
        NXOpen.Assemblies.Component.DirectOwner:py:meth:`NXOpen.Assemblies.Component.DirectOwner`
        
        NXOpen.Assemblies.ComponentAssembly.ReplaceReferenceSet:py:meth:`NXOpen.Assemblies.ComponentAssembly.ReplaceReferenceSet`
        
        on each component in the array. However, this method will ensure that the reference set operations
        are carried out in the correct order, so that any effects caused by a parent's reference set change will
        be correctly reflected in the children. If changing reference set on components at various levels in the
        assembly, use this method.
        
        Note that the names of the default reference sets Empty and Entire Part can be
        obtained from :py:meth:`NXOpen.Assemblies.Component.EmptyPartRefsetName` or
        :py:meth:`NXOpen.Assemblies.Component.EntirePartRefsetName`.
        
        Signature ``ReplaceReferenceSetInOwners(newReferenceSet, components)`` 
        
        :param newReferenceSet:  The name of the new reference set  
        :type newReferenceSet: str 
        :param components:  Components to be edited. Each component                                                                                     will have its reference set updated in its                                                                                    owning assembly.  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  list of errors encountered during the edit 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReplaceReferenceSet(self, component: Component, newReferenceSet: str) -> None:
        """
        Replaces the reference set used by a component.  
        
        Note that the names of the default reference sets Empty and Entire Part can be
        obtained from :py:meth:`NXOpen.Assemblies.Component.EmptyPartRefsetName` or
        :py:meth:`NXOpen.Assemblies.Component.EntirePartRefsetName`. 
        
        Signature ``ReplaceReferenceSet(component, newReferenceSet)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param newReferenceSet:  The name of the new reference set  
        :type newReferenceSet: str 
        
        .. versionadded:: NX3.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveComponent(self, component: Component, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
        Moves a component by specifying a translation and rotation.  
        
        Note that these are
        specified in the coordinates of this assembly, which are not necessarily the
        coordinates of the displayed part. Note that the rotation matrix is expected to 
        be stored in a column order fashion.
        
        Signature ``MoveComponent(component, translation, rotation)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly   
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param translation:  The translation delta  
        :type translation: :py:class:`NXOpen.Vector3d` 
        :param rotation:  The rotation delta, in column order.   
        :type rotation: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX3.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateMatingConverter(self) -> NXOpen.Positioning.MatingConverter:
        """
        Creates a :py:class:`NXOpen.Positioning.MatingConverter` object for this assembly.  
        
        This can be used to convert Mating Conditions in this part and in its child components
        to Assembly Constraints. Note that this part need not be the work part for this. 
        
        Signature ``CreateMatingConverter()`` 
        
        :returns:  The new Mating Converter  
        :rtype: :py:class:`NXOpen.Positioning.MatingConverter` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteMatingConditions(self) -> None:
        """
        Delete all the mating conditions in this assembly.  
        
        This can be used before creating
        assembly constraints in the assembly, if the mating conditions are not being converted.
        Component-component mating conditions and inherited mating conditions are not deleted.
        Update should be called afterwards.
        
        Signature ``DeleteMatingConditions()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ConvertRememberedMcs(self) -> None:
        """
        Converts all remembered mating constraints in the part of this assembly to remembered
        assembly constraints
        
        Signature ``ConvertRememberedMcs()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetNonGeometricState(self, component: Component, nonGeometricState: bool) -> None:
        """
        Sets the component state to Geometric or Non-Geometric.  
        
        Component which are made non-geometric are undrawn from graphics area.
        
        Signature ``SetNonGeometricState(component, nonGeometricState)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param nonGeometricState:  True to make component non-geometric, false otherwise  
        :type nonGeometricState: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetNonGeometricState(self, component: Component) -> bool:
        """
        Gets the component state as Geometric or Non-Geometric.  
        
        Signature ``GetNonGeometricState(component)`` 
        
        :param component:  The component to query. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  True if the component is non-geometric, false otherwise  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetComponentQuantityType(self, component: Component) -> ComponentQuantity:
        """
        Gets the quantity type of the components.  
        
        Returns :py:class:`NXOpen.Assemblies.ComponentQuantity`.
        
        Signature ``GetComponentQuantityType(component)`` 
        
        :param component:  The component to query. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  Quantity type an enumeration value  
        :rtype: :py:class:`NXOpen.Assemblies.ComponentQuantity` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetIntegerQuantity(self, component: Component, integerQuantity: int) -> None:
        """
        Sets the integer quantity on this component.  
        
        Signature ``SetIntegerQuantity(component, integerQuantity)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param integerQuantity:  Integer quantity value  
        :type integerQuantity: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetIntegerQuantity(self, component: Component) -> int:
        """
        Gets the value of the integer quantity of component.  
        
        Signature ``GetIntegerQuantity(component)`` 
        
        :param component:  The component to query. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  Integer quantity value  
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetRealQuantity(self, component: Component, realQuantity: float, quantityUnits: str) -> None:
        """
        Sets the real quantity and corresponding units on this component.  
        
        Signature ``SetRealQuantity(component, realQuantity, quantityUnits)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param realQuantity:  Real quantity value  
        :type realQuantity: float 
        :param quantityUnits:  Units  
        :type quantityUnits: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetRealQuantity(self, component: Component) -> tuple:
        """
        Gets the value of real quantity and corresponding units on this component.  
        
        Signature ``GetRealQuantity(component)`` 
        
        :param component:  The component to query. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (realQuantity, units). realQuantity is a float.   Real quantity value units is a str.   Units 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetAsRequiredQuantity(self, component: Component) -> None:
        """
        Sets the as-required quantity on this component.  
        
        Signature ``SetAsRequiredQuantity(component)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetAsRequiredQuantity(self, component: Component) -> str:
        """
        Gets the as-required quantity on this component.  
        
        Signature ``GetAsRequiredQuantity(component)`` 
        
        :param component:  The component to edit. Must be directly owned by this assembly. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  As-Required string "A/R" 
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CopyComponents(self, components: 'list[Component]') -> 'list[Component]':
        """
        Given an array of components, creates copies of the components such that each copy is created
        under the parent assembly of the original component.  
        
        The original components do not need to be
        under the same parent assembly as each other.
        
        The number of new components may be different from the original number of components if problems
        occurred during the copy.
        
        Signature ``CopyComponents(components)`` 
        
        :param components:  Components to be copied.  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The newly created copies.  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RestructureComponents(self, origComponents: 'list[Component]', newParentComponent: Component, deleteFlag: bool) -> tuple:
        """
        Given an array of components and a specified parent this function will transfer the given components to the parent.  
        
        The original components do not need to be under the same parent assembly as each other.
        
        The number of new components may be different from the original number of components if problems occurred during the transfer
        
        Signature ``RestructureComponents(origComponents, newParentComponent, deleteFlag)`` 
        
        :param origComponents:  Array of components to be restructured   
        :type origComponents: list of :py:class:`NXOpen.Assemblies.Component` 
        :param newParentComponent:  Destination for restructure   
        :type newParentComponent: :py:class:`NXOpen.Assemblies.Component` 
        :param deleteFlag:  Flag to delete original components  
        :type deleteFlag: bool 
        :returns: a tuple 
        :rtype: A tuple consisting of (newComponents, errorList). newComponents is a list of :py:class:`NXOpen.Assemblies.Component`.   Restructured components errorList is a :py:class:`NXOpen.ErrorList`.   Any errors that occurred during the restructure  
        
        .. versionadded:: NX6.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def OpenComponents(self, openOption: ComponentAssemblyOpenOption, componentsToOpen: 'list[Component]') -> tuple:
        """
        Given an array of components, open the components using the open_option.  
        
        Signature ``OpenComponents(openOption, componentsToOpen)`` 
        
        :param openOption:  The option that controls the open operation  
        :type openOption: :py:class:`NXOpen.Assemblies.ComponentAssemblyOpenOption` 
        :param componentsToOpen:  Array of components to open   
        :type componentsToOpen: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (loadStatus, openStatus). loadStatus is a :py:class:`NXOpen.PartLoadStatus`.   If any components could not be loaded, this object contains the error information. openStatus is a list of :py:class:`NXOpen.Assemblies.ComponentAssemblyOpenComponentStatus`.   Shows the status of the objects in an indexed array according to if they could be opened 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CloseComponents(self, componentsToClose: 'list[Component]', wholeTree: NXOpen.BasePartCloseWholeTree, closeModified: ComponentAssemblyCloseModified) -> NXOpen.PartCloseStatus:
        """
        Given an array of components, close the components.  
        
        This close of the components will check for different reasons that the part cannot be closed. 
        The reasons will be returned in the PartCloseStatus object.    
        
        Signature ``CloseComponents(componentsToClose, wholeTree, closeModified)`` 
        
        :param componentsToClose:  Array of components to close   
        :type componentsToClose: list of :py:class:`NXOpen.Assemblies.Component` 
        :param wholeTree:  If true, unloads all components of the part. If false, unloads only the top-level part  
        :type wholeTree: :py:class:`NXOpen.BasePartCloseWholeTree` 
        :param closeModified:  Behavior of close if component parts are modified.  
        :type closeModified: :py:class:`NXOpen.Assemblies.ComponentAssemblyCloseModified` 
        :returns:  Close status for the parts   
        :rtype: :py:class:`NXOpen.PartCloseStatus` 
        
        .. versionadded:: NX6.0.1
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetSuppressionExpression(self, component: Component) -> NXOpen.Expression:
        """
        Gets the expression controlling the suppression of the component in its
        controlling arrangement
        
        Signature ``GetSuppressionExpression(component)`` 
        
        :param component:  The component to query. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The suppression expression.  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetSuppressionExpression(self, component: Component, arrangement: Arrangement) -> NXOpen.Expression:
        """
        Gets the expression controlling the suppression of the component in the given
        arrangment
        
        Signature ``GetSuppressionExpression(component, arrangement)`` 
        
        :param component:  The component to query. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param arrangement:  The arrangement in which to query the suppressed state  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  The suppression expression.  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetSuppressedState(self, component: Component) -> tuple:
        """
        Gets the suppression state of the component in its controlling arrangement
        
        Signature ``GetSuppressedState(component)`` 
        
        :param component:  The component to query. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (suppressedState, controlled). suppressedState is a :py:class:`NXOpen.Assemblies.ComponentAssemblySuppressedState`.   The suppressed state controlled is a bool.   Is the suppression state controlled at the level of arrangement? 
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetSuppressedState(self, component: Component, arrangement: Arrangement) -> tuple:
        """
        Gets the suppression state of the component in the given arrangement.
        
        Signature ``GetSuppressedState(component, arrangement)`` 
        
        :param component:  The component to query. 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param arrangement:  Arrangements in which components should                                                                              be suppressed.                                                                          
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns: a tuple 
        :rtype: A tuple consisting of (suppressedState, controlled). suppressedState is a :py:class:`NXOpen.Assemblies.ComponentAssemblySuppressedState`.   The suppressed state controlled is a bool.   Is the suppression state controlled at                                         the level of arrangement?                                    
        
        .. versionadded:: NX6.0.4
        
        License requirements: None.
        """
        ...
    
    
    def CreateComponentPatternBuilder(self, compPattern: ComponentPattern) -> ComponentPatternBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ComponentPatternBuilder` object 
        This can be used to create or edit a component pattern.  
        
        Signature ``CreateComponentPatternBuilder(compPattern)`` 
        
        :param compPattern:  The pattern definition object will be used in edit  
        :type compPattern: :py:class:`NXOpen.Assemblies.ComponentPattern` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ComponentPatternBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddPendingComponent(self, partToAdd: str, pendingComponent: NXOpen.NXObject, referenceSetName: str, componentName: str, basePoint: NXOpen.Point3d, orientation: NXOpen.Matrix3x3, layer: int, uomAsNgc: bool) -> NXOpen.PartLoadStatus:
        """
        Add a pending :py:class:`NXOpen.Assemblies.Component` in this assembly.  
        
        Signature ``AddPendingComponent(partToAdd, pendingComponent, referenceSetName, componentName, basePoint, orientation, layer, uomAsNgc)`` 
        
        :param partToAdd:  The part that defines the new component  
        :type partToAdd: str 
        :param pendingComponent:  component to add  
        :type pendingComponent: :py:class:`NXOpen.NXObject` 
        :param referenceSetName:  The name of the reference set used to represent the new component  
        :type referenceSetName: str 
        :param componentName:  The name of the new component  
        :type componentName: str 
        :param basePoint:  Location of the new component  
        :type basePoint: :py:class:`NXOpen.Point3d` 
        :param orientation:  Orientation matrix for the new component, in column order.   
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param layer:   The layer to place the new component on                                               -1 means use the original layers defined in the component.                                              0 means use the work layer.                                              1-256 means use the specified layer.  
        :type layer: int 
        :param uomAsNgc:  Whether to set to non-geometric if with unit-of-measure  
        :type uomAsNgc: bool 
        :returns:  Result of loading the
        part_to_add  
        :rtype: :py:class:`NXOpen.PartLoadStatus` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateConstraintGroupBuilder(self, group: NXOpen.Positioning.ComponentConstraintGroup, contextComponent: Component) -> NXOpen.Positioning.ComponentConstraintGroupBuilder:
        """
        Creates a :py:class:`NXOpen.Positioning.ComponentConstraintGroupBuilder` object.  
        
        This can be used to create a constraint group or edit an existing constraint group.
        The context component decides which displayed constraints are to be used from
        the member constraints of an existing constraint group. If the context component
        is None the displayed constraints used are in the same part as the member
        constraints.
        
        Signature ``CreateConstraintGroupBuilder(group, contextComponent)`` 
        
        :param group:  Group to be edited, if None then a new group is created  
        :type group: :py:class:`NXOpen.Positioning.ComponentConstraintGroup` 
        :param contextComponent:  Context component, can be None  
        :type contextComponent: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.Positioning.ComponentConstraintGroupBuilder` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CheckinComponents(self, partOccs: 'list[Component]', checkinInputOption: ComponentAssemblyCheckinCheckoutOption) -> NXOpen.ErrorList:
        """
        Checks in array of components as per the option :py:class:`NXOpen.Assemblies.ComponentAssemblyCheckinCheckoutOption`.  
        
        Signature ``CheckinComponents(partOccs, checkinInputOption)`` 
        
        :param partOccs:  Array of components to check in   
        :type partOccs: list of :py:class:`NXOpen.Assemblies.Component` 
        :param checkinInputOption:  Option that controls what to check in  
        :type checkinInputOption: :py:class:`NXOpen.Assemblies.ComponentAssemblyCheckinCheckoutOption` 
        :returns:  Any errors that occurred during the check in   
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CheckoutComponents(self, partOccs: 'list[Component]', checkoutInputOption: ComponentAssemblyCheckinCheckoutOption) -> NXOpen.ErrorList:
        """
        Checks out array of components as per the option :py:class:`NXOpen.Assemblies.ComponentAssemblyCheckinCheckoutOption`.  
        
        Signature ``CheckoutComponents(partOccs, checkoutInputOption)`` 
        
        :param partOccs:  Array of components to check out   
        :type partOccs: list of :py:class:`NXOpen.Assemblies.Component` 
        :param checkoutInputOption:  Option that controls what to check out 
        :type checkoutInputOption: :py:class:`NXOpen.Assemblies.ComponentAssemblyCheckinCheckoutOption` 
        :returns:  Any errors that occurred during the check out   
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CheckoutWorkset(self) -> NXOpen.ErrorList:
        """
        Checks out workset.  
        
        Signature ``CheckoutWorkset()`` 
        
        :returns:  Any errors that occurred during checking out of workset   
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CheckinWorkset(self) -> NXOpen.ErrorList:
        """
        Checks in workset.  
        
        Signature ``CheckinWorkset()`` 
        
        :returns:  Any errors that occurred during checking in of workset   
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CheckoutAllModifiedObjects(self) -> tuple:
        """
        Checks out all modified objects in the current session.  
        
        checkedOutObjects collection will be type of :py:class:`NXOpen.BasePart` or :py:class:`NXOpen.PDM.DesignElementRevision`
        
        Signature ``CheckoutAllModifiedObjects()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (errorList, checkedOutObjects). errorList is a :py:class:`NXOpen.ErrorList`.   Any errors that occurred during checking out of objects  checkedOutObjects is a list of :py:class:`NXOpen.NXObject`.   Array of NXObjects checked out  
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetCheckedoutStatusOfObjects(self) -> tuple:
        """
        Returns the checkedout status (checkedout/non checkedout) of all the objects open in NX.  
        
        Signature ``GetCheckedoutStatusOfObjects()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (checkedOutObjects, uncheckedOutObjects). checkedOutObjects is a list of :py:class:`NXOpen.NXObject`.   Array of NXObjects which are open in session and checked out uncheckedOutObjects is a list of :py:class:`NXOpen.NXObject`.   Array of NXObjects which are open in session but not checkout 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def ReorderComponents(self, order: ComponentOrder, componentsToReorder: 'list[Component]', targetComponent: Component, beforeOrAfter: ComponentAssemblyOrderTargetLocation) -> None:
        """
        Reorders the array of :py:class:`NXOpen.Assemblies.Component`s before or after the target :py:class:`NXOpen.Assemblies.Component`.  
        
        :py:class:`NXOpen.Assemblies.Component`s to reorder and the target :py:class:`NXOpen.Assemblies.Component` should be children of 
        the same immediate parent.
        
        Signature ``ReorderComponents(order, componentsToReorder, targetComponent, beforeOrAfter)`` 
        
        :param order:   :py:class:`NXOpen.Assemblies.ComponentOrder` in which components are reordered  
        :type order: :py:class:`NXOpen.Assemblies.ComponentOrder` 
        :param componentsToReorder:  Array of components to be reordered   
        :type componentsToReorder: list of :py:class:`NXOpen.Assemblies.Component` 
        :param targetComponent:  Components are moved before or after this component  
        :type targetComponent: :py:class:`NXOpen.Assemblies.Component` 
        :param beforeOrAfter:  Whether to move components before or after the target component  
        :type beforeOrAfter: :py:class:`NXOpen.Assemblies.ComponentAssemblyOrderTargetLocation` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ReorderChildrenOfParent(self, order: ComponentOrder, parentComponent: Component, componentsToReorder: 'list[Component]') -> None:
        """
        Assigns a new order to immediate children :py:class:`NXOpen.Assemblies.Component`s of parent :py:class:`NXOpen.Assemblies.Component`.  
        
        Signature ``ReorderChildrenOfParent(order, parentComponent, componentsToReorder)`` 
        
        :param order:   :py:class:`NXOpen.Assemblies.ComponentOrder` in which children are reordered  
        :type order: :py:class:`NXOpen.Assemblies.ComponentOrder` 
        :param parentComponent:  Parent component whose children are reordered  
        :type parentComponent: :py:class:`NXOpen.Assemblies.Component` 
        :param componentsToReorder:  Array of children components in new order   
        :type componentsToReorder: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetComponentOrders(self) -> 'list[ComponentOrder]':
        """
        Returns all :py:class:`NXOpen.Assemblies.ComponentOrder`s available in the part
        
        Signature ``GetComponentOrders()`` 
        
        :returns:  Returns array of :py:class:`NXOpen.Assemblies.ComponentOrder`s in part  
        :rtype: list of :py:class:`NXOpen.Assemblies.ComponentOrder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveToPendingComponent(self, component: NXOpen.NXObject) -> None:
        """
        Move a :py:class:`NXOpen.Assemblies.Component` in this assembly to a pending list.  
        
        The :py:class:`NXOpen.Assemblies.Component` should be previously in the pending list and
        just got added into the assembly.
        
        Signature ``MoveToPendingComponent(component)`` 
        
        :param component:  component to move to pending list 
        :type component: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetActiveOrder(self) -> Order:
        """
        Returns the active order in the part 
        
        Signature ``GetActiveOrder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Order` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateIsolateViewWithComponents(self, components: 'list[Component]') -> tuple:
        """
        Creates a temporary :py:class:`NXOpen.View` and shows array of components in it 
        and treats this as Isolate view till it gets undisplayed.  
        
        Only one Isolate view can be created
        for the assembly.
        Returns :py:class:`NXOpen.View` which is treated as Isolate View.
        
        Signature ``CreateIsolateViewWithComponents(components)`` 
        
        :param components:  Array of components to be shown in isolate view  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (errors, view). errors is a :py:class:`NXOpen.ErrorList`.   list of errors encountered during components shown in isolate view view is a :py:class:`NXOpen.View`.   Return the isolate view 
        
        .. versionadded:: NX11.0.1
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def ShowComponentsInIsolateView(self, components: 'list[Component]') -> tuple:
        """
        Shows array of components in Isolate view :py:class:`NXOpen.View`.  
        
        If Isolate view doesn't exist then this API doesn't do anything.
        Returns :py:class:`NXOpen.View` which is treated as Isolate View.
        
        Signature ``ShowComponentsInIsolateView(components)`` 
        
        :param components:  Array of components to be shown in isolate view  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (errors, view). errors is a :py:class:`NXOpen.ErrorList`.   list of errors encountered during components shown in isolate view view is a :py:class:`NXOpen.View`.   Return the isolate view 
        
        .. versionadded:: NX11.0.1
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    
    def HideComponentsInIsolateView(self, components: 'list[Component]') -> tuple:
        """
        Hides array of components in Isolate view :py:class:`NXOpen.View`.  
        
        If Isolate view doesn't exist then this API doesn't do anything.
        Returns :py:class:`NXOpen.View` which is treated as Isolate View.
        
        Signature ``HideComponentsInIsolateView(components)`` 
        
        :param components:  Array of components to be shown in isolate view  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (errors, view). errors is a :py:class:`NXOpen.ErrorList`.   list of errors encountered during components shown in isolate view view is a :py:class:`NXOpen.View`.   Return the isolate view 
        
        .. versionadded:: NX11.0.1
        
        License requirements: gateway ("UG GATEWAY")
        """
        ...
    
    ActiveArrangement: Arrangement = ...
    """
    Returns or sets 
    the currently active :py:class:`NXOpen.Assemblies.Arrangement` for this ComponentAssembly
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveArrangement`` 
    
    :returns:  The :py:class:`NXOpen.Assemblies.Arrangement` that is currently active  
    :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveArrangement`` 
    
    :param newArrangement:  The new active :py:class:`NXOpen.Assemblies.Arrangement`. This Arrangement                                                                must be defined in this ComponentAssembly.                                                             
    :type newArrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Positioner: NXOpen.Positioning.ComponentPositioner = ...
    """
    Returns  the component positioner for this assembly.  
    
    The positioner manages the component constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``Positioner`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Positioning.ComponentPositioner` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    RootComponent: Component = ...
    """
    Returns  the top-level component, i.e. the component at the root of the component
    tree.  
    
    This component corresponds to the part that owns this
    :py:class:`NXOpen.Assemblies.ComponentAssembly`. The components below this will correspond to
    parts added by calling :py:meth:`NXOpen.Assemblies.ComponentAssembly.AddComponent`.
    
    Note that this will be None if there are no components in the tree. (I.e. if the part
    that owns this ComponentAssembly is a piece part.)
    
    <hr>
    
    Getter Method
    
    Signature ``RootComponent`` 
    
    :returns:  The  :py:class:`NXOpen.Assemblies.Component` at the root of this ComponentAssembly's tree  
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX3.0.0
    
    License requirements: None.
    """
    Arrangements: ArrangementCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.Arrangement`s defined in the ComponentAssembly 
    
    Signature ``Arrangements`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ArrangementCollection`
    """
    Explosions: ExplosionCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.Explosion`s defined in the ComponentAssembly 
    
    Signature ``Explosions`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ExplosionCollection`
    """
    DrawingExplosions: DrawingExplosionCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.DrawingExplosion`s defined in the ComponentAssembly 
    
    Signature ``DrawingExplosions`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.DrawingExplosionCollection`
    """
    ComponentPatterns: ComponentPatternCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.ComponentPattern` defined in the ComponentAssembly 
    
    Signature ``ComponentPatterns`` 
    
    .. versionadded:: NX9.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ComponentPatternCollection`
    """
    Subsets: SubsetCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.Subset`s defined in the ComponentAssembly 
    
    Signature ``Subsets`` 
    
    .. versionadded:: NX8.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetCollection`
    """
    ClearanceSets: ClearanceSetCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.ClearanceSet`s defined in the ComponentAssembly 
    
    Signature ``ClearanceSets`` 
    
    .. versionadded:: NX9.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ClearanceSetCollection`
    """
    OrdersSet: OrderCollection = ...
    """
    The collection of :py:class:`NXOpen.Assemblies.Order`s defined in the ComponentAssembly 
    
    Signature ``OrdersSet`` 
    
    .. versionadded:: NX9.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.OrderCollection`
    """
    Null: ComponentAssembly = ...  # unknown typename


class RelinkerBuilderLinkScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RelinkerBuilderLinkScope():
    """
    Represents the relink scope type of Relinker. 
    Relink Scope defines the link destination part files and source files. 
    Relinker only searches part files defined in relink scope to get link/destination information and source parent for later reparenting
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PartsInSession", "Indicate relink scope is parts in session"
       "PartsInAssembly", "Indicate relink scope is parts in assembly"
       "WorkPart", "Indicate relink scope is work part"
       "SelectedParts", "Indicate relink scope is selected parts"
    """
    PartsInSession = 0  # RelinkerBuilderLinkScopeMemberType
    PartsInAssembly = 1  # RelinkerBuilderLinkScopeMemberType
    WorkPart = 2  # RelinkerBuilderLinkScopeMemberType
    SelectedParts = 3  # RelinkerBuilderLinkScopeMemberType
    
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
    


class RelinkerBuilderLinkCategoryMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RelinkerBuilderLinkCategory():
    """
    Represents the link category of Relinker, either geometry WAVE link or interpart expression. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WaveGeometry", "Indicate link category is wave geometry"
       "InterpartExpression", "Indicate link category is interpart expression"
    """
    WaveGeometry = 0  # RelinkerBuilderLinkCategoryMemberType
    InterpartExpression = 1  # RelinkerBuilderLinkCategoryMemberType
    
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
    


class RelinkerBuilderLinkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RelinkerBuilderLinkType():
    """
    Represents the link type option when browsing current available links.
    As a filter, it tells Link Browser what links should be listed. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "Indicate relink browser type is all"
       "NotBroken", "Indicate relink browser type is not broken only"
       "Broken", "Indicate relink browser type is broken only"
       "AutoLinked", "Indicate relink browser type is auto-linked only"
       "WithMultipleSource", "Indicate relink browser type is with multuple source"
    """
    All = 0  # RelinkerBuilderLinkTypeMemberType
    NotBroken = 1  # RelinkerBuilderLinkTypeMemberType
    Broken = 2  # RelinkerBuilderLinkTypeMemberType
    AutoLinked = 3  # RelinkerBuilderLinkTypeMemberType
    WithMultipleSource = 4  # RelinkerBuilderLinkTypeMemberType
    
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
    


class RelinkerBuilderLinkOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class RelinkerBuilderLinkOption():
    """
    Represents the relink option.
    Per this option, relinker will search the corresponding source and do relinking. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InterpartExpression", "Indicate relink option is interpart expression only"
       "WaveGeometry", "Indicate relink option is wave geometry only"
       "Both", "Indicate relink option is both interpart expression and wave link"
    """
    InterpartExpression = 0  # RelinkerBuilderLinkOptionMemberType
    WaveGeometry = 1  # RelinkerBuilderLinkOptionMemberType
    Both = 2  # RelinkerBuilderLinkOptionMemberType
    
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
    


class RelinkerBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.RelinkerBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.RelinkerCollection.CreateBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class LinkScope():
        """
        Represents the relink scope type of Relinker. 
        Relink Scope defines the link destination part files and source files. 
        Relinker only searches part files defined in relink scope to get link/destination information and source parent for later reparenting
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PartsInSession", "Indicate relink scope is parts in session"
           "PartsInAssembly", "Indicate relink scope is parts in assembly"
           "WorkPart", "Indicate relink scope is work part"
           "SelectedParts", "Indicate relink scope is selected parts"
        """
        PartsInSession = 0  # RelinkerBuilderLinkScopeMemberType
        PartsInAssembly = 1  # RelinkerBuilderLinkScopeMemberType
        WorkPart = 2  # RelinkerBuilderLinkScopeMemberType
        SelectedParts = 3  # RelinkerBuilderLinkScopeMemberType
        
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
        
    
    
    class LinkCategory():
        """
        Represents the link category of Relinker, either geometry WAVE link or interpart expression. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WaveGeometry", "Indicate link category is wave geometry"
           "InterpartExpression", "Indicate link category is interpart expression"
        """
        WaveGeometry = 0  # RelinkerBuilderLinkCategoryMemberType
        InterpartExpression = 1  # RelinkerBuilderLinkCategoryMemberType
        
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
        
    
    
    class LinkType():
        """
        Represents the link type option when browsing current available links.
        As a filter, it tells Link Browser what links should be listed. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "Indicate relink browser type is all"
           "NotBroken", "Indicate relink browser type is not broken only"
           "Broken", "Indicate relink browser type is broken only"
           "AutoLinked", "Indicate relink browser type is auto-linked only"
           "WithMultipleSource", "Indicate relink browser type is with multuple source"
        """
        All = 0  # RelinkerBuilderLinkTypeMemberType
        NotBroken = 1  # RelinkerBuilderLinkTypeMemberType
        Broken = 2  # RelinkerBuilderLinkTypeMemberType
        AutoLinked = 3  # RelinkerBuilderLinkTypeMemberType
        WithMultipleSource = 4  # RelinkerBuilderLinkTypeMemberType
        
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
        
    
    
    class LinkOption():
        """
        Represents the relink option.
        Per this option, relinker will search the corresponding source and do relinking. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InterpartExpression", "Indicate relink option is interpart expression only"
           "WaveGeometry", "Indicate relink option is wave geometry only"
           "Both", "Indicate relink option is both interpart expression and wave link"
        """
        InterpartExpression = 0  # RelinkerBuilderLinkOptionMemberType
        WaveGeometry = 1  # RelinkerBuilderLinkOptionMemberType
        Both = 2  # RelinkerBuilderLinkOptionMemberType
        
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
        
    
    
    def ExecuteRelink(self) -> None:
        """
        Relink with new source, for WAVE links, interpart explression or both.  
        
        Signature ``ExecuteRelink()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def SearchWavelinksInterpartExpressions(self) -> None:
        """
        Searches WAVE links and interpart expressions. 
        
        This method does not actually change the link data and interpart expressions.
        
        Signature ``SearchWavelinksInterpartExpressions()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def ExportToInformationWindow(self) -> None:
        """
        List all link information to the list window.  
        
        Signature ``ExportToInformationWindow()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def UpdateSession(self) -> None:
        """
        Updates the session.  
        
        Signature ``UpdateSession()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def UpdateSessionWithBreakDelayed(self) -> None:
        """
        Updates the session without immediately breaking wave links or inter part expressions.  
        
        Signature ``UpdateSessionWithBreakDelayed()`` 
        
        .. versionadded:: NX8.5.1
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def ViewFeatureFailure(self) -> None:
        """
        Views the feature failure information.  
        
        All failed features in assembly will be shown with detailed information. 
        
        Signature ``ViewFeatureFailure()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def GetExpressionSourceCount(self, partID: NXOpen.Part, expID: NXOpen.Expression, sourceID: NXOpen.Expression) -> int:
        """
        Gets the total count of multiple candidate sources to re-parent the inter part expression.  
        
        Signature ``GetExpressionSourceCount(partID, expID, sourceID)`` 
        
        :param partID: 
        :type partID: :py:class:`NXOpen.Part` 
        :param expID: 
        :type expID: :py:class:`NXOpen.Expression` 
        :param sourceID: 
        :type sourceID: :py:class:`NXOpen.Expression` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX7.5.5
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def RelinkInterpartExpression(self, partID: NXOpen.Part, expID: NXOpen.Expression, sourceID: NXOpen.Expression) -> None:
        """
        Relinks the inter part expression using the specific expression from the specific part in case of multiple expression sources.  
        
        Signature ``RelinkInterpartExpression(partID, expID, sourceID)`` 
        
        :param partID: 
        :type partID: :py:class:`NXOpen.Part` 
        :param expID: 
        :type expID: :py:class:`NXOpen.Expression` 
        :param sourceID: 
        :type sourceID: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def RelinkWaveFeature(self, partID: NXOpen.Part, featID: NXOpen.Features.Feature, sourceID: NXOpen.NXObject) -> None:
        """
        Relinks the wave feature using the specific geometry source from the specific part in case of multiple geometry sources.  
        
        Signature ``RelinkWaveFeature(partID, featID, sourceID)`` 
        
        :param partID: 
        :type partID: :py:class:`NXOpen.Part` 
        :param featID: 
        :type featID: :py:class:`NXOpen.Features.Feature` 
        :param sourceID: 
        :type sourceID: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    BreakInterpartExpression: bool = ...
    """
    Returns or sets  the option to break interpart expression.  
    
    If it's true, relinker will break interpart expression after relinking. If it's false, relinker will not break interpart expression.
    
    <hr>
    
    Getter Method
    
    Signature ``BreakInterpartExpression`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BreakInterpartExpression`` 
    
    :param breakInterPartExpression: 
    :type breakInterPartExpression: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    BreakWaveLink: bool = ...
    """
    Returns or sets  the option to break WAVE links.  
    
    If it's true, relinker will break WAVE links after relinking. If it's false, relinker will not break WAVE links.
    
    <hr>
    
    Getter Method
    
    Signature ``BreakWaveLink`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BreakWaveLink`` 
    
    :param breakWave: 
    :type breakWave: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    FaceCurveDirectionAdjustment: bool = ...
    """
    Returns or sets  the option to adjust face or curve direction.  
    
    If it's true, relinker will check the linked curve direction or face normal and 
    either keep or automatically flip the direction of new source while relinking.
    
    <hr>
    
    Getter Method
    
    Signature ``FaceCurveDirectionAdjustment`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceCurveDirectionAdjustment`` 
    
    :param adjustDir: 
    :type adjustDir: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    IncludeNonBrokenWaveLinks: bool = ...
    """
    Returns or sets  the option to include non-broken WAVE links or not.  
    
    If it's true, relinker will include non-broken WAVE links. If it's false, non-broken WAVE links will not be included while relinking.
    The default behavior in the relinker is not to include non-broken WAVE links. 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeNonBrokenWaveLinks`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeNonBrokenWaveLinks`` 
    
    :param includeNonBrokenWaveLinks: 
    :type includeNonBrokenWaveLinks: bool 
    
    .. versionadded:: NX5.0.2
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    IncludeSuppressedComponents: bool = ...
    """
    Returns or sets  the option to include suppressed components as source candidates or not.  
    
    If it's true, relinker will include suppressed components as source candidates. If it's false, suppressed components will not be included as source candidates while relinking.
    The default behavior in the relinker is not to include suppressed components. 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeSuppressedComponents`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeSuppressedComponents`` 
    
    :param includeSuppressedComponents: 
    :type includeSuppressedComponents: bool 
    
    .. versionadded:: NX5.0.2
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    RelinkCategory: RelinkerBuilderLinkCategory = ...
    """
    Returns or sets  the relink category either wave geometry or interpart expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``RelinkCategory`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkCategory` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelinkCategory`` 
    
    :param linkCategory: 
    :type linkCategory: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkCategory` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    RelinkOption: RelinkerBuilderLinkOption = ...
    """
    Returns or sets  the link option.  
    
    Relinker will check this option to relink WAVE, interpart expression or both 
    
    <hr>
    
    Getter Method
    
    Signature ``RelinkOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelinkOption`` 
    
    :param linkOption: 
    :type linkOption: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkOption` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    RelinkType: RelinkerBuilderLinkType = ...
    """
    Returns or sets  the current link type.  
    
    <hr>
    
    Getter Method
    
    Signature ``RelinkType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelinkType`` 
    
    :param linkType: 
    :type linkType: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SearchExistingInterPartExpressionOnly: bool = ...
    """
    Returns or sets  the option to search existing inter part expression only or all expressions including regular ones.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchExistingInterPartExpressionOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchExistingInterPartExpressionOnly`` 
    
    :param searchExistingIPEOnly: 
    :type searchExistingIPEOnly: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SearchingDestinationObject: str = ...
    """
    Returns or sets  the searching destination object string.  
    
    Used to specify the wildcard string to search the destination objects when cycling object by name.
    When cycling destination objects, relink scope will be used as the searching scope.
    
    <hr>
    
    Getter Method
    
    Signature ``SearchingDestinationObject`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchingDestinationObject`` 
    
    :param destinationObjectStr: 
    :type destinationObjectStr: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SearchingSourceObject: str = ...
    """
    Returns or sets  the searching source object string.  
    
    Used to specify the wildcard string to search the source objects when cycling object by name.
    When cycling source objects, source parts will define the searching scope.
    
    <hr>
    
    Getter Method
    
    Signature ``SearchingSourceObject`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchingSourceObject`` 
    
    :param sourceObjectStr: 
    :type sourceObjectStr: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SearchingSourcePart: str = ...
    """
    Returns or sets  the searching source part string.  
    
    Used to specify the wildcard string to search source parts by file names.
    Source parts define the scope of searching source objects.
    
    <hr>
    
    Getter Method
    
    Signature ``SearchingSourcePart`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchingSourcePart`` 
    
    :param sourcePartStr: 
    :type sourcePartStr: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SearchingSourcePartAttribute: str = ...
    """
    Returns or sets  the searching source part attribute string.  
    
    Used to specify the wildcard string to search source parts by part attribute predefined in source part.
    This criterial will furtherly narrow down the source part scope to avoid multiple source found.
    
    <hr>
    
    Getter Method
    
    Signature ``SearchingSourcePartAttribute`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchingSourcePartAttribute`` 
    
    :param sourcePartAttribute: 
    :type sourcePartAttribute: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    SelectComponent: SelectComponentList = ...
    """
    Returns  a list of the selected component as relink target scope.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    SelectComponentSource: SelectComponentList = ...
    """
    Returns  a list of the selected component as relink source scope.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectComponentSource`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    """
    SourceScope: RelinkerBuilderLinkScope = ...
    """
    Returns or sets  the current source scope.  
    
    <hr>
    
    Getter Method
    
    Signature ``SourceScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkScope` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SourceScope`` 
    
    :param sourceScope: 
    :type sourceScope: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkScope` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    TargetScope: RelinkerBuilderLinkScope = ...
    """
    Returns or sets  the current target scope.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetScope`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkScope` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetScope`` 
    
    :param targetScope: 
    :type targetScope: :py:class:`NXOpen.Assemblies.RelinkerBuilderLinkScope` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: wave ("WAVE FUNCTIONALITY")
    """
    Null: RelinkerBuilder = ...  # unknown typename


class ProductOutlineManager():
    """
    Represents a collection of assemblies.  
    
    Input to this class can be PSM facet objects.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def CreateProductOutlineBuilder(self) -> ProductOutlineBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ProductOutlineBuilder`.  
        
        Gives access to the attributes of the Product Outline  
        
        Signature ``CreateProductOutlineBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductOutlineBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def ShowProductOutline(self, isShow: bool) -> None:
        """
        Controls the visibility of already defined product outline.  
        
        Supply **true</b> to show the Product Outline, or **false</b>
        to hide the Product Outline.
        
        Signature ``ShowProductOutline(isShow)`` 
        
        :param isShow:  Flag to make the product Outline selectable or unselectable. If "true" the Product outline is made selectable.  
        :type isShow: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    
    def ShowSelectableProductOutline(self, isSelectable: bool) -> None:
        """
        Controls the visibility and selectability of already defined product outline.  
        
        Supply **true</b> to show the selectable Product Outline, or **false</b>
        to hide the Product Outline. 
        
        Signature ``ShowSelectableProductOutline(isSelectable)`` 
        
        :param isSelectable:  Flag to make the product Outline selectable or unselectable. If "true" the Product outline is made selectable.  
        :type isSelectable: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: adv_assemblies ("ADVANCED ASSEMBLIES")
        """
        ...
    
    IsProductOutlineDefined: bool = ...
    """
    Returns  the status of the product outline.  
    
    If the product outline is already defined, it returns "true", else returns "false".
    
    <hr>
    
    Getter Method
    
    Signature ``IsProductOutlineDefined`` 
    
    :returns:  Return value for the status of the product outline.  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """


class BoxSearchTermBoxOverlapLogicTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BoxSearchTermBoxOverlapLogicType():
    """
    Logic used to determine the type of inclusion used in a box search term within a recipe.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "Include objects residing inside the box defined by this search term"
       "Outside", "Include objects residing outside the box defined by this search term"
       "Intersects", "Include objects that intersect the box defined by this search term"
       "InsideOrIntersects", "Include objects residing inside or intersecting the box defined by this search term"
       "OutsideOrIntersects", "Include objects residing outside or intersecting the box defined by this search term"
    """
    Inside = 0  # BoxSearchTermBoxOverlapLogicTypeMemberType
    Outside = 1  # BoxSearchTermBoxOverlapLogicTypeMemberType
    Intersects = 2  # BoxSearchTermBoxOverlapLogicTypeMemberType
    InsideOrIntersects = 3  # BoxSearchTermBoxOverlapLogicTypeMemberType
    OutsideOrIntersects = 4  # BoxSearchTermBoxOverlapLogicTypeMemberType
    
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
    


class BoxSearchTerm(SearchTerm):
    """
    A volume search term within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    A volume search finds objects in a box with sides axis aligned in the space
    of the collaborative design.
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.BoxSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    class BoxOverlapLogicType():
        """
        Logic used to determine the type of inclusion used in a box search term within a recipe.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "Include objects residing inside the box defined by this search term"
           "Outside", "Include objects residing outside the box defined by this search term"
           "Intersects", "Include objects that intersect the box defined by this search term"
           "InsideOrIntersects", "Include objects residing inside or intersecting the box defined by this search term"
           "OutsideOrIntersects", "Include objects residing outside or intersecting the box defined by this search term"
        """
        Inside = 0  # BoxSearchTermBoxOverlapLogicTypeMemberType
        Outside = 1  # BoxSearchTermBoxOverlapLogicTypeMemberType
        Intersects = 2  # BoxSearchTermBoxOverlapLogicTypeMemberType
        InsideOrIntersects = 3  # BoxSearchTermBoxOverlapLogicTypeMemberType
        OutsideOrIntersects = 4  # BoxSearchTermBoxOverlapLogicTypeMemberType
        
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
        
    
    Null: BoxSearchTerm = ...  # unknown typename


class PlaneSearchTermBuilder(SearchTermBuilder):
    """
    A PlaneSearchTermBuilder is used to create or edit an :py:class:`NXOpen.Assemblies.PlaneSearchTerm`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreatePlaneSearchTermBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Displacement: float = ...
    """
    Returns or sets  
    the displacement of the plane from the origin.  
    
    <hr>
    
    Getter Method
    
    Signature ``Displacement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Displacement`` 
    
    :param displacement: 
    :type displacement: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Normal: NXOpen.Vector3d = ...
    """
    Returns or sets  
    the normal of the plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``Normal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Normal`` 
    
    :param normal: 
    :type normal: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PlaneOverlapLogic: PlaneSearchTermPlaneOverlapLogicType = ...
    """
    Returns or sets  
    the plane overlap logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneOverlapLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.PlaneSearchTermPlaneOverlapLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneOverlapLogic`` 
    
    :param planeOverlapLogic: 
    :type planeOverlapLogic: :py:class:`NXOpen.Assemblies.PlaneSearchTermPlaneOverlapLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    PointOnPlane: NXOpen.Point3d = ...
    """
    Returns or sets  
    the normal of the plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``PointOnPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``PointOnPlane`` 
    
    :param pointOnPlane: 
    :type pointOnPlane: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchTermLogic: SearchTermSearchTermLogicType = ...
    """
    Returns or sets  
    the search term logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTermLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTermLogic`` 
    
    :param searchTermLogic: 
    :type searchTermLogic: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TrueShapeRefinement: bool = ...
    """
    Returns or sets  
    the true-shape refinement.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :param trueShapeRefinement: 
    :type trueShapeRefinement: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: PlaneSearchTermBuilder = ...  # unknown typename


class CreateComponentBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.CreateComponentBuilder` builder class.  
    
    This builder class will perform various component creation operations under assembly, workset or subset. 
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateCreateComponentBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: CreateComponentBuilder = ...  # unknown typename


class PartitionSearchTermIncludeChildrenMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartitionSearchTermIncludeChildren():
    """
    Logic used to determine whether children are to be included for the search term which is used within a recipe.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "False", "Do not include Partition children while finding results by this search term"
       "True", "Include Partition children while finding results by this search term"
    """
    FalseValue = 0  # PartitionSearchTermIncludeChildrenMemberType
    TrueValue = 1  # PartitionSearchTermIncludeChildrenMemberType
    
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
    


class PartitionSearchTerm(SearchTerm):
    """
    A :py:class:`Assemblies.SubsetRecipe` search term that refers to a partition.  
    
    To create an instance of this object use :py:meth:`Assemblies.SubsetRecipe.CreatePartitionSearchTerm`
    
    .. versionadded:: NX8.5.0
    """
    
    class IncludeChildren():
        """
        Logic used to determine whether children are to be included for the search term which is used within a recipe.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "False", "Do not include Partition children while finding results by this search term"
           "True", "Include Partition children while finding results by this search term"
        """
        FalseValue = 0  # PartitionSearchTermIncludeChildrenMemberType
        TrueValue = 1  # PartitionSearchTermIncludeChildrenMemberType
        
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
        
    
    Partition: Partition = ...
    """
    Returns  the partition of this search term.  
    
    <hr>
    
    Getter Method
    
    Signature ``Partition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Partition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: PartitionSearchTerm = ...  # unknown typename


class Partition(NXOpen.NXObject):
    """
    A partition is a Teamcenter object in a Collaborative Design.  
    
    A partition can
    contain design elements and other partitions.
    
    Instances of this object can be accessed through :py:class:`NXOpen.Assemblies.PartitionScheme`.
    
    .. versionadded:: NX8.5.0
    """
    
    def LoadImmediateChildPartitions(self) -> None:
        """
        Load all immediate children for the given partition.  
        
        This may involve server calls in case data needs to be fetched from the database.
        Call this method at each level to load all partitions.
        
        Signature ``LoadImmediateChildPartitions()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetImmediateChildPartitions(self) -> 'list[Partition]':
        """
        Get all immediate children which are currently loaded.  
        
        This method needs to be called recursively to get full list of 
        loaded children. If immediate child partitions are not loaded then call :py:meth:`NXOpen.Assemblies.Partition.LoadImmediateChildPartitions`
        to load them.
        
        Signature ``GetImmediateChildPartitions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Partition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Partition = ...  # unknown typename


class PatternInstance(PatternMember):
    """
    Represents the pattern instance object.  
    
    Instances of this class can be accessed through component pattern object
    
    .. versionadded:: NX9.0.0
    """
    
    def GetIndices(self) -> tuple:
        """
        Gets the indices of pattern instance.  
        
        Signature ``GetIndices()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (index2, index1). index2 is a int. index1 is a int. 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSuppressedStatus(self) -> bool:
        """
        Gets the suppressed status of pattern instance.  
        
        Signature ``GetSuppressedStatus()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDeletedStatus(self) -> bool:
        """
        Gets the deleted status of pattern instance.  
        
        Signature ``GetDeletedStatus()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetClockedStatus(self) -> bool:
        """
        Gets the clocked status of pattern instance.  
        
        Signature ``GetClockedStatus()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PatternInstance = ...  # unknown typename


class MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethod():
    """
    Represents the method to use to determine the surrounding data corresponding to the routing design content that has been loaded.
    1. None : No surrounding data to be loaded.
    2. ProximityRoutingContent : This means surrounding data for the runs, this is related to the DE's that are in proximity to the DEs
    constituting the run.
    3. Manual: An empty Surrounding Object Subset will be created
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "ProximitytoRoutingContent", " - "
       "Manual", " - "
    """
    NotSet = 0  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
    ProximitytoRoutingContent = 1  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
    Manual = 2  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
    
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
    


class MechanicalRoutingSubsetBuilder(NXOpen.Builder):
    """
    A MechanicalRoutingSubsetBuilder is used to create/edit Subsets :py:class:`NXOpen.Assemblies.Subset` 
    that are used to define the context needed to perform a Mechanical Routing Design activity.  
    
    The builder may 
    generate multiple subsets. The content of these subsets can be classified into "Work" content - the elements
    of the Routing design that the user would like to focus on and "Surrounding Data" content - the 3D content that
    surrounds the Routing design. The subset definition process utilizes the concept of a Run ja class TBD by NX P and ID
    while defining the recipe terms needed for the subsets. 
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateMechanicalRoutingSubsetBuilderForSurroundingEdit`
    
    .. versionadded:: NX11.0.0
    """
    
    class SurroundingDataRecipeMethod():
        """
        Represents the method to use to determine the surrounding data corresponding to the routing design content that has been loaded.
        1. None : No surrounding data to be loaded.
        2. ProximityRoutingContent : This means surrounding data for the runs, this is related to the DE's that are in proximity to the DEs
        constituting the run.
        3. Manual: An empty Surrounding Object Subset will be created
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "ProximitytoRoutingContent", " - "
           "Manual", " - "
        """
        NotSet = 0  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
        ProximitytoRoutingContent = 1  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
        Manual = 2  # MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethodMemberType
        
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
        
    
    
    def GetSearchSubsetBuilder(self) -> SubsetBuilder:
        """
        The subset builder which is used for searching runs, the user will have to use
        :py:class:`NXOpen.Assemblies.FindInCollaborativeDesign` to search for runs 
        using object type RunElement.  
        
        Signature ``GetSearchSubsetBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetSearchSubsetBuilder(self, subsetBuilder: SubsetBuilder) -> None:
        """
        Sets the subset builder which needs to be set by user to search runs, the user will have to use
        :py:class:`NXOpen.Assemblies.FindInCollaborativeDesign` to search for runs 
        using object type RunElement.  
        
        Signature ``SetSearchSubsetBuilder(subsetBuilder)`` 
        
        :param subsetBuilder: 
        :type subsetBuilder: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetConfigurationContextBuilder(self) -> NXOpen.PDM.ConfigurationContextBuilder:
        """
        Returns the configuration context builder which will be used by user to set revision rule or effectivity and then user
        needs to use :py:class:`NXOpen.Assemblies.FindInCollaborativeDesign` to search for runs 
        using object type RunElement.  
        
        This is the builder which will be returned whenever you are creating new subsets.
        This will be NULL in edit mode scenario.  
        
        Signature ``GetConfigurationContextBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AppendSearchResultElementToSelectedList(self, runID: str) -> None:
        """
        Appends the Search Result Element corresponding to the given Run ID to the SelectedSearchResultElement list on :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder`.  
        
        Signature ``AppendSearchResultElementToSelectedList(runID)`` 
        
        :param runID: 
        :type runID: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveSearchResultElementFromSelectedList(self, runID: str) -> None:
        """
        Removes the Search Result Element corresponding to the given Run ID from the SelectedSearchResultElement list on :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder`.  
        
        Signature ``RemoveSearchResultElementFromSelectedList(runID)`` 
        
        :param runID: 
        :type runID: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveAllSearchResultElementsFromSelectedList(self) -> None:
        """
        Removes all the Search Result Element from the SelectedSearchResultElement list on :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilder`.  
        
        Signature ``RemoveAllSearchResultElementsFromSelectedList()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def UpdateSubsetUsingConfigurationContext(self, inputSubsetBuilder: SubsetBuilder) -> SubsetBuilder:
        """
        The routing subsets will be updated (e.  
        
        g. revision rule, effectivity) using the information available on the 
        ConfigurationContext if the input is NULL. In case of valid input the corresponding subset will be updated with
        the information available on the ConfigurationContext.  
        
        Signature ``UpdateSubsetUsingConfigurationContext(inputSubsetBuilder)`` 
        
        :param inputSubsetBuilder: 
        :type inputSubsetBuilder: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.SubsetBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetRoutingSubsetAsWorkPart(self) -> None:
        """
        The builder may generate multiple subsets.  
        
        This API will set the Routing Design Subset as the work part. 
        
        Signature ``SetRoutingSubsetAsWorkPart()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Fixtures: bool = ...
    """
    Returns or sets  an option for inclusion of fixtures DE's in the Routing Work.  
    
    <hr>
    
    Getter Method
    
    Signature ``Fixtures`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Fixtures`` 
    
    :param includeFixtures: 
    :type includeFixtures: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Insulation: bool = ...
    """
    Returns or sets  an option for inclusion of insulation DE's in the Routing Work Subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``Insulation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Insulation`` 
    
    :param includeInsulation: 
    :type includeInsulation: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SurroundingDataProximityDistance: float = ...
    """
    Returns or sets  a proximity to Routing Content method has been selected to determine the surrounding content then 
    this is the distance value used to perform the evaluation.  
    
    The units are in meters
    
    <hr>
    
    Getter Method
    
    Signature ``SurroundingDataProximityDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SurroundingDataProximityDistance`` 
    
    :param surroundingDataProximityDistance: 
    :type surroundingDataProximityDistance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SurroundingDataRecipeMethodType: MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethod = ...
    """
    Returns or sets  the routing recipes :py:class:`Assemblies.MechanicalRoutingSubsetBuilder`
    
    <hr>
    
    Getter Method
    
    Signature ``SurroundingDataRecipeMethodType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SurroundingDataRecipeMethodType`` 
    
    :param surroundingDataRecipeMethod: 
    :type surroundingDataRecipeMethod: :py:class:`NXOpen.Assemblies.MechanicalRoutingSubsetBuilderSurroundingDataRecipeMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: MechanicalRoutingSubsetBuilder = ...  # unknown typename


class GroupSearchTerm(SearchTerm):
    """
    A group of :py:class:`NXOpen.Assemblies.SearchTerm`s within a :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
    
    An instance of this object can be created via :py:class:`NXOpen.Assemblies.SubsetRecipe`
    
    .. versionadded:: NX8.5.0
    """
    Null: GroupSearchTerm = ...  # unknown typename


class RunContentProximitySearchTermBuilder(SearchTermBuilder):
    """
    A RunContentProximitySearchTermBuilder is used to create or edit an :py:class:`Assemblies.RunContentProximitySearchTerm`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateRunContentProximitySearchTermBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def GetSeedName(self) -> str:
        """
        Get the seed element name which is used in RunContentProximity search.  
        
        The seed in this case is the name of the Run object.
        The 3D contents of this Run object will be used as seeds for the proximity search.
        
        Signature ``GetSeedName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetSeedName(self, seedRunName: str) -> None:
        """
        Set the seed element name which is used in RunContentProximity search.  
        
        The seed in this case is the name of the Run object.
        The 3D contents of this Run object will be used as seeds for the proximity search.
        
        Signature ``SetSeedName(seedRunName)`` 
        
        :param seedRunName: 
        :type seedRunName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    Distance: float = ...
    """
    Returns or sets  
    the distance for the proximity.  
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Distance`` 
    
    :param distance: 
    :type distance: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchTermLogic: SearchTermSearchTermLogicType = ...
    """
    Returns or sets  
    the search term logic.  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchTermLogic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchTermLogic`` 
    
    :param searchTermLogic: 
    :type searchTermLogic: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TrueShapeRefinement: bool = ...
    """
    Returns or sets  
    the true-shape refinement.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``TrueShapeRefinement`` 
    
    :param trueShapeRefinement: 
    :type trueShapeRefinement: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: RunContentProximitySearchTermBuilder = ...  # unknown typename


class AssemblyManager():
    """
    Represents the Assembly Manager   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def CreateHideComponentBuilder(self) -> HideComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.HideComponentBuilder`  
        
        Signature ``CreateHideComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.HideComponentBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateShowComponentBuilder(self) -> ShowComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ShowComponentBuilder`  
        
        Signature ``CreateShowComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ShowComponentBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateUpdateStructureBuilder(self) -> UpdateStructureBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.UpdateStructureBuilder`  
        
        Signature ``CreateUpdateStructureBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.UpdateStructureBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateReplaceComponentBuilder(self) -> ReplaceComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ReplaceComponentBuilder`  
        
        Signature ``CreateReplaceComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ReplaceComponentBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateLoadInterpartDataBuilder(self) -> LoadInterpartDataBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilder`  
        
        Signature ``CreateLoadInterpartDataBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.LoadInterpartDataBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    
    
    def CreateNewComponentBuilder(self) -> CreateNewComponentBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.CreateNewComponentBuilder`  
        
        Signature ``CreateNewComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.CreateNewComponentBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateConstraintDisplayBuilder(self) -> ConstraintDisplayBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ConstraintDisplayBuilder` 
        
        Signature ``CreateConstraintDisplayBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ConstraintDisplayBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateMakeUniquePartBuilder(self) -> MakeUniquePartBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.MakeUniquePartBuilder` 
        
        Signature ``CreateMakeUniquePartBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.MakeUniquePartBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateClearanceAnalysisBuilder(self, clearanceSet: ClearanceSet) -> ClearanceAnalysisBuilder:
        """
        Creates a :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilder`.  
        
        The builder can be populated 
        with an existing clearance set specified in clearanceSet.
        
        Signature ``CreateClearanceAnalysisBuilder(clearanceSet)`` 
        
        :param clearanceSet:  :py:class:`NXOpen.Assemblies.ClearanceSet` to be edited - may be None if creating a new Clearance Set.  
        :type clearanceSet: :py:class:`NXOpen.Assemblies.ClearanceSet` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ClearanceAnalysisBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateAddComponentBuilder(self) -> AddComponentBuilder:
        """
        Creates a :py:class:`Assemblies.AddComponentBuilder`  
        
        Signature ``CreateAddComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.AddComponentBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CreateCreateComponentBuilder(self) -> CreateComponentBuilder:
        """
        Creates a :py:class:`Assemblies.CreateComponentBuilder`  
        
        Signature ``CreateCreateComponentBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.CreateComponentBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    


class SubsetBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    A SubsetBuilder is used to create or edit an :py:class:`NXOpen.Assemblies.Subset`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.SubsetCollection.CreateSubsetBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def GetSubsets(self) -> 'list[Subset]':
        """
        Returns subsets held / created by this builder.  
        
        Signature ``GetSubsets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Subset` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GenerateResults(self) -> None:
        """
        Generate the search results for the :py:class:`NXOpen.Assemblies.Subset` according to the current
        :py:class:`NXOpen.Assemblies.SubsetRecipe`.  
        
        Signature ``GenerateResults()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.NXObject:
        """
        Finds the :py:class:`NXOpen.NXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the :py:class:`NXOpen.NXObject` to be found  
        :type journalIdentifier: str 
        :returns:  Object found, or null if no such object exists  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetSubsetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns subset logical objects created by builder.  
        
        Signature ``GetSubsetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def UpdateConfigurationContext(self, logicalObject: NXOpen.PDM.LogicalObject) -> None:
        """
        Updates revision rule, effectivity and variant information on subset logical object of subset builder.  
        
        Input subset logical object must be member of this subset builder.
        
        Signature ``UpdateConfigurationContext(logicalObject)`` 
        
        :param logicalObject: 
        :type logicalObject: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def UpdateSubsetConfigurationOfDependentSubset(self) -> None:
        """
        Updates revision rule, effectivity information on the dependent subsets if any.  
        
        The dependent subset evaluated for the subset represented by the builder.
        
        Signature ``UpdateSubsetConfigurationOfDependentSubset()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def UpdateSubsetTargetPropertiesOfDependentSubset(self) -> None:
        """
        Updates target effectivity information on the dependent subsets if any.  
        
        The dependent subset evaluated for the subset represented by the builder.
        
        Signature ``UpdateSubsetTargetPropertiesOfDependentSubset()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AutoAssignAttributes(self, objects: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.  
        
        Signature ``AutoAssignAttributes(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AutoAssignAttributesWithNamingPattern(self, objects: 'list[NXOpen.NXObject]', properties: 'list[NXOpen.NXObject]') -> NXOpen.ErrorList:
        """
        Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.  
        
        properties needs to be created using :py:meth:`CreateAttributeTitleToNamingPatternMap`
        
        Signature ``AutoAssignAttributesWithNamingPattern(objects, properties)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param properties: 
        :type properties: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateAttributeTitleToNamingPatternMap(self, attributeTitles: 'list[str]', titlePatterns: 'list[str]') -> NXOpen.NXObject:
        """
        Creates a map object of attribute titles to their corresponding naming pattern  
        
        Signature ``CreateAttributeTitleToNamingPatternMap(attributeTitles, titlePatterns)`` 
        
        :param attributeTitles: 
        :type attributeTitles: list of str 
        :param titlePatterns: 
        :type titlePatterns: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    AddAllSubordinates: bool = ...
    """
    Returns or sets  the value which determines whether the subset will include all the subordinates of reuse design elements.  
    
    <hr>
    
    Getter Method
    
    Signature ``AddAllSubordinates`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``AddAllSubordinates`` 
    
    :param addAllSubordinates: 
    :type addAllSubordinates: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    CollaborativeDesign: NXOpen.CollaborativeDesign = ...
    """
    Returns or sets  the :py:class:`NXOpen.CollaborativeDesign` of the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``CollaborativeDesign`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``CollaborativeDesign`` 
    
    :param collaborativeDesign: 
    :type collaborativeDesign: :py:class:`NXOpen.CollaborativeDesign` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ConfigurationContext: NXOpen.PDM.ConfigurationContextBuilder = ...
    """
    Returns  the configuration context builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConfigurationContext`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.ConfigurationContextBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ContentDefinition: NXOpen.ContentDefinition = ...
    """
    Returns or sets  the :py:class:`NXOpen.ContentDefinition` used to define the context of the subset creation.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContentDefinition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ContentDefinition` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``ContentDefinition`` 
    
    :param contentDefinition: 
    :type contentDefinition: :py:class:`NXOpen.ContentDefinition` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Finder: FindInCollaborativeDesign = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.FindInCollaborativeDesign` for use in the context
    determined by this builder.  
    
    <hr>
    
    Getter Method
    
    Signature ``Finder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.FindInCollaborativeDesign` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Subset: Subset = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.Subset` that we are building.  
    
    <hr>
    
    Getter Method
    
    Signature ``Subset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Subset` 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Please use :py:meth:`NXOpen.Assemblies.SubsetBuilder.GetSubsets` instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SubsetConfiguration: SubsetConfigurationBuilder = ...
    """
    Returns  the subset configuration.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetConfiguration`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetConfigurationBuilder` 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Assemblies.SubsetBuilder.ConfigurationContext` instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SubsetDescription: str = ...
    """
    Returns or sets  the description of the :py:class:`NXOpen.Assemblies.Subset`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetDescription`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.PDM.LogicalObject` properties instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SubsetDescription`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.PDM.LogicalObject` properties instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SubsetName: str = ...
    """
    Returns or sets  the name of the :py:class:`NXOpen.Assemblies.Subset`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.PDM.LogicalObject` properties instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``SubsetName`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.PDM.LogicalObject` properties instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SubsetType: SubsetContentType = ...
    """
    Returns  the type of  PLM object used to create subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetContentType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TargetEffectivity: NXOpen.BasicEffectivityBuilder = ...
    """
    Returns  the :py:class:`NXOpen.BasicEffectivityBuilder` used to edit the target effectivity of the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetEffectivity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BasicEffectivityBuilder` 
    
    .. versionadded:: NX8.5.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`SubsetBuilder.TargetEffectivityTable` instead.
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TargetEffectivityTable: NXOpen.PDM.EffectivityTableBuilder = ...
    """
    Returns  the :py:class:`NXOpen.PDM.EffectivityTableBuilder` used to edit the target effectivity of the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetEffectivityTable`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PDM.EffectivityTableBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    TargetPartitionList: PartitionList = ...
    """
    Returns  the default target :py:class:`NXOpen.Assemblies.Partition`s for design elements created within the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetPartitionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.PartitionList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    ViewedPartitionScheme: PartitionScheme = ...
    """
    Returns or sets  the viewed :py:class:`NXOpen.Assemblies.PartitionScheme` of the subset.  
    
    <hr>
    
    Getter Method
    
    Signature ``ViewedPartitionScheme`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.PartitionScheme` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    
    <hr>
    
    Setter Method
    
    Signature ``ViewedPartitionScheme`` 
    
    :param partitionScheme: 
    :type partitionScheme: :py:class:`NXOpen.Assemblies.PartitionScheme` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Workset: ComponentAssembly = ...
    """
    Returns  the :py:class:`NXOpen.Assemblies.ComponentAssembly` within which we are 
    building an :py:class:`NXOpen.Assemblies.Subset`.  
    
    <hr>
    
    Getter Method
    
    Signature ``Workset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ComponentAssembly` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    SearchResults: SearchResultCollection = ...
    """
    Returns the :py:class:`NXOpen.Assemblies.SearchResultCollection` that contains current search results 
    associated with this subset builder.  
    
    SearchResults will be populated with the existing subset contents when the builder is created to
    edit a subset.  These are replaced with results found by the last call to :py:meth:`SubsetBuilder.GenerateResults`
    after that method is first called. 
    In addition, the last results from :py:meth:`SubsetBuilder.Finder` are included in this
    collection.
    
    Signature ``SearchResults`` 
    
    .. versionadded:: NX8.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SearchResultCollection`
    """
    Recipe: SubsetRecipe = ...
    """
    Returns the :py:class:`NXOpen.Assemblies.SubsetRecipe` that contains the :py:class:`NXOpen.Assemblies.SearchTerm`s 
    used to generate the contents of the subset 
    
    Signature ``Recipe`` 
    
    .. versionadded:: NX8.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SubsetRecipe`
    """
    Null: SubsetBuilder = ...  # unknown typename


class SubsetRecipe(NXOpen.TaggedObjectCollection):
    """
    A subset recipe is used by a :py:class:`NXOpen.Assemblies.SubsetBuilder` to collect :py:class:`NXOpen.Assemblies.SearchTerm`s.  
    
    The search terms specify the search that defines the contents of a :py:class:`NXOpen.Assemblies.Subset`.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.SubsetBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> SearchTerm:
        """
        Finds the :py:class:`NXOpen.Assemblies.SearchTerm` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Name of the search term to be found  
        :type journalIdentifier: str 
        :returns:  Search term found, or null if no such search term exists. 
        :rtype: :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateExplicitSearchTerm(self, logicType: SearchTermSearchTermLogicType, searchResultElement: SearchResultElement) -> ExplicitSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.ExplicitSearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateExplicitSearchTerm(logicType, searchResultElement)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param searchResultElement: 
        :type searchResultElement: :py:class:`NXOpen.Assemblies.SearchResultElement` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ExplicitSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateExplicitSearchTermGroup(self, logicType: SearchTermSearchTermLogicType, searchResultElements: 'list[SearchResultElement]') -> GroupSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.GroupSearchTerm` of :py:class:`NXOpen.Assemblies.ExplicitSearchTerm`s and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateExplicitSearchTermGroup(logicType, searchResultElements)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param searchResultElements: 
        :type searchResultElements: list of :py:class:`NXOpen.Assemblies.SearchResultElement` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.GroupSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def AddSearchTermBuilder(self, searchTermBuilder: SearchTermBuilder) -> None:
        """
        Add a :py:class:`NXOpen.Assemblies.SearchTermBuilder` to the recipe.  
        
        When this search term builder
        is committed the search term will be added to the recipe at the end of the list of search terms.
        
        Signature ``AddSearchTermBuilder(searchTermBuilder)`` 
        
        :param searchTermBuilder: 
        :type searchTermBuilder: :py:class:`NXOpen.Assemblies.SearchTermBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateBoxSearchTerm(self, logicType: SearchTermSearchTermLogicType, overlapType: BoxSearchTermBoxOverlapLogicType, bottomCorner: NXOpen.Point3d, topCorner: NXOpen.Point3d, trueShapeRefinement: bool) -> BoxSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.BoxSearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateBoxSearchTerm(logicType, overlapType, bottomCorner, topCorner, trueShapeRefinement)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param overlapType: 
        :type overlapType: :py:class:`NXOpen.Assemblies.BoxSearchTermBoxOverlapLogicType` 
        :param bottomCorner:  Vertex of zone in workset part coordinates  
        :type bottomCorner: :py:class:`NXOpen.Point3d` 
        :param topCorner:  Opposite vertex of zone in workset part coordinates  
        :type topCorner: :py:class:`NXOpen.Point3d` 
        :param trueShapeRefinement:  Apply TrueShape refinement to volume search  
        :type trueShapeRefinement: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.BoxSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateProximitySearchTerm(self, logicType: SearchTermSearchTermLogicType, seeds: 'list[SearchResultElement]', distance: float, trueShapeRefinement: bool) -> ProximitySearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.ProximitySearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateProximitySearchTerm(logicType, seeds, distance, trueShapeRefinement)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param seeds: 
        :type seeds: list of :py:class:`NXOpen.Assemblies.SearchResultElement` 
        :param distance:  Distance in workset part units  
        :type distance: float 
        :param trueShapeRefinement:  Apply TrueShape refinement to proximity search  
        :type trueShapeRefinement: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProximitySearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateRunContentProximitySearchTerm(self, logicType: SearchTermSearchTermLogicType, seedRunName: str, distance: float, trueShapeRefinement: bool) -> RunContentProximitySearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.RunContentProximitySearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateRunContentProximitySearchTerm(logicType, seedRunName, distance, trueShapeRefinement)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param seedRunName:  The contents of this Run will be seeds for the proximity  
        :type seedRunName: str 
        :param distance:  Distance in workset part units  
        :type distance: float 
        :param trueShapeRefinement:  Apply TrueShape refinement to proximity search  
        :type trueShapeRefinement: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.RunContentProximitySearchTerm` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreatePlaneSearchTerm(self, logicType: SearchTermSearchTermLogicType, overlapType: PlaneSearchTermPlaneOverlapLogicType, normal: NXOpen.Vector3d, displacement: float, pointOnPlane: NXOpen.Point3d, trueShapeRefinement: bool) -> PlaneSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.PlaneSearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreatePlaneSearchTerm(logicType, overlapType, normal, displacement, pointOnPlane, trueShapeRefinement)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param overlapType: 
        :type overlapType: :py:class:`NXOpen.Assemblies.PlaneSearchTermPlaneOverlapLogicType` 
        :param normal:  Unitized plane normal  
        :type normal: :py:class:`NXOpen.Vector3d` 
        :param displacement:  Displacement in workset part units  
        :type displacement: float 
        :param pointOnPlane:  Point On Plane in workset part coordinates  
        :type pointOnPlane: :py:class:`NXOpen.Point3d` 
        :param trueShapeRefinement:  Apply TrueShape refinement to plane search  
        :type trueShapeRefinement: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PlaneSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CreateAttributeSearchTerm(self, logicType: SearchTermSearchTermLogicType, queryName: str, entries: 'list[str]', values: 'list[str]') -> AttributeSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.AttributeSearchTerm` and
        adds it to the recipe at the end of the list of search terms.  
        
        Signature ``CreateAttributeSearchTerm(logicType, queryName, entries, values)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param queryName:  Name of the saved query upon which this search term is based  
        :type queryName: str 
        :param entries:  search criteria entries  
        :type entries: list of str 
        :param values:  search criteria values  
        :type values: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.AttributeSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    @typing.overload
    def CreatePartitionSearchTerm(self, logicType: SearchTermSearchTermLogicType, partition: Partition) -> PartitionSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.PartitionSearchTerm` and
        adds it to the recipe at the end of the list of search terms.
        Child partitions of the partition being passed as a parameter are not included in the recipe.
        
        Signature ``CreatePartitionSearchTerm(logicType, partition)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param partition:  The partition upon which this search term is based  
        :type partition: :py:class:`NXOpen.Assemblies.Partition` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PartitionSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        .. deprecated::  NX11.0.0
           Use the :py:meth:`NXOpen.Assemblies.SubsetRecipe.CreatePartitionSearchTerm` that gives specific control on whether or not to include children partition as well
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    @typing.overload
    def CreatePartitionSearchTerm(self, logicType: SearchTermSearchTermLogicType, includeChildrenLogic: PartitionSearchTermIncludeChildren, partition: Partition) -> PartitionSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.PartitionSearchTerm` and
        adds it to the recipe at the end of the list of search terms.
        
        Signature ``CreatePartitionSearchTerm(logicType, includeChildrenLogic, partition)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param includeChildrenLogic: 
        :type includeChildrenLogic: :py:class:`NXOpen.Assemblies.PartitionSearchTermIncludeChildren` 
        :param partition:  The partition upon which this search term is based  
        :type partition: :py:class:`NXOpen.Assemblies.Partition` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.PartitionSearchTerm` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    @typing.overload
    def CreatePartitionSearchTermGroup(self, logicType: SearchTermSearchTermLogicType, partitions: 'list[Partition]') -> GroupSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.GroupSearchTerm` of :py:class:`NXOpen.Assemblies.PartitionSearchTerm`s and
        adds it to the recipe at the end of the list of search terms.
        Child partitions of the partitions being passed as a parameter are not included in the recipe.  
        
        Signature ``CreatePartitionSearchTermGroup(logicType, partitions)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param partitions: 
        :type partitions: list of :py:class:`NXOpen.Assemblies.Partition` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.GroupSearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        .. deprecated::  NX11.0.0
           Use the :py:meth:`NXOpen.Assemblies.SubsetRecipe.CreatePartitionSearchTermGroup` that gives specific control on whether or not to include children partition as well
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    @typing.overload
    def CreatePartitionSearchTermGroup(self, logicType: SearchTermSearchTermLogicType, includeChildrenLogic: PartitionSearchTermIncludeChildren, partitions: 'list[Partition]') -> GroupSearchTerm:
        """
        Creates a :py:class:`NXOpen.Assemblies.GroupSearchTerm` of :py:class:`NXOpen.Assemblies.PartitionSearchTerm`s and
        adds it to the recipe at the end of the list of search terms.
        
        Signature ``CreatePartitionSearchTermGroup(logicType, includeChildrenLogic, partitions)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param includeChildrenLogic: 
        :type includeChildrenLogic: :py:class:`NXOpen.Assemblies.PartitionSearchTermIncludeChildren` 
        :param partitions: 
        :type partitions: list of :py:class:`NXOpen.Assemblies.Partition` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.GroupSearchTerm` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def MoveUp(self, searchTerm: SearchTerm) -> None:
        """
        Move a :py:class:`NXOpen.Assemblies.SearchTerm` up to another location in the recipe.  
        
        Signature ``MoveUp(searchTerm)`` 
        
        :param searchTerm: 
        :type searchTerm: :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def MoveDown(self, searchTerm: SearchTerm) -> None:
        """
        Move a :py:class:`NXOpen.Assemblies.SearchTerm` down to another location in the recipe.  
        
        Signature ``MoveDown(searchTerm)`` 
        
        :param searchTerm: 
        :type searchTerm: :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def Group(self, logicType: SearchTermSearchTermLogicType, searchTerms: 'list[SearchTerm]') -> None:
        """
        Put the :py:class:`NXOpen.Assemblies.SearchTerm`s in a new :py:class:`NXOpen.Assemblies.GroupSearchTerm`.  
        
        The group is placed in the recipe at the location of the first search term.
        
        Signature ``Group(logicType, searchTerms)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param searchTerms: 
        :type searchTerms: list of :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def Ungroup(self, searchTerms: 'list[SearchTerm]') -> None:
        """
        Any :py:class:`NXOpen.Assemblies.GroupSearchTerm`s in the input search terms will be removed
        from the recipe.  
        
        The members of the group will be re-parented as members of the
        group's parent.
        
        Signature ``Ungroup(searchTerms)`` 
        
        :param searchTerms: 
        :type searchTerms: list of :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def DeleteSearchTerms(self, searchTerms: 'list[SearchTerm]') -> None:
        """
        Removes the :py:class:`NXOpen.Assemblies.SearchTerm`s from the recipe and deletes them.  
        
        Signature ``DeleteSearchTerms(searchTerms)`` 
        
        :param searchTerms: 
        :type searchTerms: list of :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetSearchTermLogic(self, logicType: SearchTermSearchTermLogicType, searchTerms: 'list[SearchTerm]') -> None:
        """
        Changes the search term logic of each :py:class:`NXOpen.Assemblies.SearchTerm`s passed in.  
        
        Signature ``SetSearchTermLogic(logicType, searchTerms)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param searchTerms: 
        :type searchTerms: list of :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetPartitionSearchTermLogic(self, logicType: SearchTermSearchTermLogicType, includeChildrenLogic: PartitionSearchTermIncludeChildren, searchTerms: 'list[SearchTerm]') -> None:
        """
        Changes the search term include children logic of each :py:class:`NXOpen.Assemblies.PartitionSearchTerm`s passed in.  
        
        Signature ``SetPartitionSearchTermLogic(logicType, includeChildrenLogic, searchTerms)`` 
        
        :param logicType: 
        :type logicType: :py:class:`NXOpen.Assemblies.SearchTermSearchTermLogicType` 
        :param includeChildrenLogic: 
        :type includeChildrenLogic: :py:class:`NXOpen.Assemblies.PartitionSearchTermIncludeChildren` 
        :param searchTerms: 
        :type searchTerms: list of :py:class:`NXOpen.Assemblies.SearchTerm` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def SetSearchOptionValue(self, optionSet: str, searchOption: str, optionValue: bool) -> None:
        """
        Sets value of specified search option from given option set.  
        
        Both option set and search option should be internal name as
        defined in database.
        Use :py:meth:`NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets` to get all the option set internal names defined in database. 
        Use :py:meth:`NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptions` to get all the search option internal names defined in database. 
        
        Signature ``SetSearchOptionValue(optionSet, searchOption, optionValue)`` 
        
        :param optionSet: 
        :type optionSet: str 
        :param searchOption: 
        :type searchOption: str 
        :param optionValue: 
        :type optionValue: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetSearchOptionValue(self, optionSet: str, searchOption: str) -> bool:
        """
        Gets value of specified search option from given option set.  
        
        Both option set and search option should be internal name as
        defined in database.
        Use :py:meth:`NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets` to get all the option set internal names defined in database. 
        Use :py:meth:`NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptions` to get all the search option internal names defined in database. 
        
        Signature ``GetSearchOptionValue(optionSet, searchOption)`` 
        
        :param optionSet: 
        :type optionSet: str 
        :param searchOption: 
        :type searchOption: str 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllSearchOptions(self, optionSet: str) -> 'list[str]':
        """
        Gets the internal names of all search options from specified option set as defined in database.  
        
        The option set should be
        internal name as defined in database.
        Use :py:meth:`NXOpen.Assemblies.SubsetRecipe.GetAllSearchOptionSets` to get all the option sets internal name defined in database. 
        
        Signature ``GetAllSearchOptions(optionSet)`` 
        
        :param optionSet: 
        :type optionSet: str 
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllSearchOptionSets(self) -> 'list[str]':
        """
        Gets the internal names of all option sets defined in database.  
        
        Signature ``GetAllSearchOptionSets()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class ConstraintDisplayBuilderVisibleConstraintsRuleOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintDisplayBuilderVisibleConstraintsRuleOptions():
    """
    This enum is used to control which constraints are treated as connected to the selected
    components. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BetweenComponents", "Show only constraints that refer only to selected components"
       "ConnectedToComponents", "Show only constraints that refer at least once to a selected component"
    """
    BetweenComponents = 0  # ConstraintDisplayBuilderVisibleConstraintsRuleOptionsMemberType
    ConnectedToComponents = 1  # ConstraintDisplayBuilderVisibleConstraintsRuleOptionsMemberType
    
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
    


class ConstraintDisplayBuilder(NXOpen.Builder):
    """
    The :py:class:`NXOpen.Assemblies.ConstraintDisplayBuilder` can be used to control visibility
    of constraints and optionally components.  
    
    Any selected constraint is shown, and any
    constraint that refers to geometry in selected components is shown (subject to the
    setting of the VisibleConstraintsRule).  All other constraints are hidden.
    
    If ChangeComponentVisibility is on, then selected components and components positioned by
    selected constraints are shown, and all other components are hidden.  If
    ChangeComponentVisibility is off, then component visibility is not affected.
    
    This builder operates on displayed constraints.  A displayed constraint represents a single
    assembly constraint in a given assembly, and need not be in the same part as the assembly
    constraint it represents.  An assembly may contain more than one displayed constraint for a
    given assembly constraint.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.AssemblyManager.CreateConstraintDisplayBuilder`
    
    Default values.
    
    ==========================  ==================
    Property                    Value
    ==========================  ==================
    ChangeComponentVisibility   1 
    --------------------------  ------------------
    FilterNavigator             0 
    --------------------------  ------------------
    VisibleConstraintsRule      BetweenComponents 
    ==========================  ==================
    
    .. versionadded:: NX6.0.0
    """
    
    class VisibleConstraintsRuleOptions():
        """
        This enum is used to control which constraints are treated as connected to the selected
        components. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BetweenComponents", "Show only constraints that refer only to selected components"
           "ConnectedToComponents", "Show only constraints that refer at least once to a selected component"
        """
        BetweenComponents = 0  # ConstraintDisplayBuilderVisibleConstraintsRuleOptionsMemberType
        ConnectedToComponents = 1  # ConstraintDisplayBuilderVisibleConstraintsRuleOptionsMemberType
        
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
        
    
    ChangeComponentVisibility: bool = ...
    """
    Returns or sets  the flag indicating whether or not a Show Only operation should be done on the connecting
    components.  
    
    <hr>
    
    Getter Method
    
    Signature ``ChangeComponentVisibility`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChangeComponentVisibility`` 
    
    :param changeComponentVisibility: 
    :type changeComponentVisibility: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    FilterNavigator: bool = ...
    """
    Returns or sets  the flag indicating whether the assembly navigator should filter hidden constraints.  
    
    <hr>
    
    Getter Method
    
    Signature ``FilterNavigator`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilterNavigator`` 
    
    :param filterNavigator: 
    :type filterNavigator: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ObjectSelection: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected constraints and components.  
    
    All selected constraints and components are shown
    when the builder is committed, and so are constraints and components connected to them. 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    VisibleConstraintsRule: ConstraintDisplayBuilderVisibleConstraintsRuleOptions = ...
    """
    Returns or sets  the rule determining which constraints are treated as connected to the selected components.  
    
    <hr>
    
    Getter Method
    
    Signature ``VisibleConstraintsRule`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ConstraintDisplayBuilderVisibleConstraintsRuleOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VisibleConstraintsRule`` 
    
    :param visibleConstraintsRule: 
    :type visibleConstraintsRule: :py:class:`NXOpen.Assemblies.ConstraintDisplayBuilderVisibleConstraintsRuleOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ConstraintDisplayBuilder = ...  # unknown typename


class ExplosionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of explosions   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Assemblies.ComponentAssembly`
    
    .. versionadded:: NX4.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def Create(self, explosionName: str) -> Explosion:
        """
        Creates an explosion based upon the default arrangement in the given OCC part.  
        
        Signature ``Create(explosionName)`` 
        
        :param explosionName:  Name to be given to the new explosion  
        :type explosionName: str 
        :returns:  the new explosion  
        :rtype: :py:class:`NXOpen.Assemblies.Explosion` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def FindObject(self, name: str) -> Explosion:
        """
        Finds the :py:class:`NXOpen.Assemblies.Explosion` with the given identifier as recorded in a journal.  
        
        This method should not be used in handwritten code and exists to support record and playback of journals.
        An exception will be thrown if no object can be found with the given journal identifier.
        
        Signature ``FindObject(name)`` 
        
        :param name:  Name of the Explosion to be found  
        :type name: str 
        :returns:  Explosion found, or null if no such Explosion exists. 
        :rtype: :py:class:`NXOpen.Assemblies.Explosion` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RelinkerCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of relinker   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateBuilder(self) -> RelinkerBuilder:
        """
        Creates a Relinker builder  
        
        Signature ``CreateBuilder()`` 
        
        :returns: :py:class:`RelinkerBuilder` object object  
        :rtype: :py:class:`NXOpen.Assemblies.RelinkerBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: wave ("WAVE FUNCTIONALITY")
        """
        ...
    


class DegreesOfFreedomResultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DegreesOfFreedomResult():
    """
    The overall result of the degrees of freedom calculation reported
    in :py:class:`NXOpen.Assemblies.DegreesOfFreedom`. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "The calculation failed to produce a result, possibly because the component is inconsistently constrained."
       "Success", "The degrees of freedom calculation succeeded."
    """
    Unknown = 0  # DegreesOfFreedomResultMemberType
    Success = 1  # DegreesOfFreedomResultMemberType
    
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
    


class PositioningTask(NXOpen.NXObject):
    """
    Represents the class for positioning task.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Assemblies.PositioningTaskBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def IsInWorkCollection(self, component: Component) -> bool:
        """
        Checks whether the input :py:class:`NXOpen.Assemblies.Component` is 
        a part of :py:class:`NXOpen.Assemblies.PositioningTask` work collection or not.  
        
        Signature ``IsInWorkCollection(component)`` 
        
        :param component: 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllWorkCollectionMembers(self) -> 'list[Component]':
        """
        Gets all work collection members of :py:class:`NXOpen.Assemblies.PositioningTask`.  
        
        Signature ``GetAllWorkCollectionMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsInContextCollection(self, component: Component) -> bool:
        """
        Checks whether the input :py:class:`NXOpen.Assemblies.Component` 
        is a part of :py:class:`NXOpen.Assemblies.PositioningTask` context collection 
        or not.  
        
        Signature ``IsInContextCollection(component)`` 
        
        :param component: 
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllContextCollectionMembers(self) -> 'list[Component]':
        """
        Gets all context collection members of :py:class:`NXOpen.Assemblies.PositioningTask`.  
        
        Signature ``GetAllContextCollectionMembers()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ActivatePositioningGroup(self, positioningGroup: PositioningGroup) -> None:
        """
        Activates the :py:class:`NXOpen.Assemblies.PositioningGroup` in the positioning task.  
        
        Signature ``ActivatePositioningGroup(positioningGroup)`` 
        
        :param positioningGroup: 
        :type positioningGroup: :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def DeactivatePositioningGroup(self, positioningGroup: PositioningGroup) -> None:
        """
        Deactivates the :py:class:`NXOpen.Assemblies.PositioningGroup` in the positioning task.  
        
        Signature ``DeactivatePositioningGroup(positioningGroup)`` 
        
        :param positioningGroup: 
        :type positioningGroup: :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CheckOutPositioningGroups(self, positioningGroups: 'list[PositioningGroup]') -> NXOpen.ErrorList:
        """
        Checks out the specified :py:class:`NXOpen.Assemblies.PositioningGroup`s which must be 
        associated with this positioning task.  
        
        Signature ``CheckOutPositioningGroups(positioningGroups)`` 
        
        :param positioningGroups: 
        :type positioningGroups: list of :py:class:`NXOpen.Assemblies.PositioningGroup` 
        :returns:  Any errors that occurred during check out of the Positioning Groups  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def CheckInPositioningGroups(self, positioningGroups: 'list[PositioningGroup]') -> NXOpen.ErrorList:
        """
        Checks in the specified :py:class:`NXOpen.Assemblies.PositioningGroup`s which must be 
        associated with this positioning task.  
        
        Signature ``CheckInPositioningGroups(positioningGroups)`` 
        
        :param positioningGroups: 
        :type positioningGroups: list of :py:class:`NXOpen.Assemblies.PositioningGroup` 
        :returns:  Any errors that occurred during check in of the Positioning Groups  
        :rtype: :py:class:`NXOpen.ErrorList` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def Ungroup(self, positioningGroup: PositioningGroup) -> None:
        """
        Ungroups the positioning group.  
        
        It will delete positioning group and move all its members 
        to work collection of this :py:class:`NXOpen.Assemblies.PositioningTask`.                          
        
        Signature ``Ungroup(positioningGroup)`` 
        
        :param positioningGroup: 
        :type positioningGroup: :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def RemoveFromTask(self, positioningGroup: PositioningGroup) -> None:
        """
        Removes specified :py:class:`NXOpen.Assemblies.PositioningGroup` from 
        :py:class:`NXOpen.Assemblies.PositioningTask`.  
        
        Signature ``RemoveFromTask(positioningGroup)`` 
        
        :param positioningGroup: 
        :type positioningGroup: :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def GetAllPositioningGroups(self) -> 'list[PositioningGroup]':
        """
        Gets all :py:class:`NXOpen.Assemblies.PositioningGroup`s which are 
        associated with this positioning task.  
        
        Signature ``GetAllPositioningGroups()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.PositioningGroup` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Activate(self) -> None:
        """
        Activates the :py:class:`NXOpen.Assemblies.PositioningTask`.  
        
        Signature ``Activate()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    
    def Deactivate(self) -> None:
        """
        Deactivates the :py:class:`NXOpen.Assemblies.PositioningTask`.  
        
        Signature ``Deactivate()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_4gd_integration ("4th Generation Design")
        """
        ...
    
    DisplayConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether constraints of work collection design elements 
    of this positioning task are to be displayed on the graphics window or not.  
    
    (This is a separate system from hiding and showing individual constraints.) 
    This flag controls the visibility of both suppressed and unsuppressed constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayConstraints`` 
    
    :param displayConstraints: 
    :type displayConstraints: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    DisplaySuppressedConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether suppressed constraints of work collection design  
    elements of this positioning task are to be displayed on the graphics window   
    or not.  
    
    (This is a separate system from hiding and showing individual constraints.)
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :param displaySuppressedConstraints: 
    :type displaySuppressedConstraints: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_4gd_integration ("4th Generation Design")
    """
    Null: PositioningTask = ...  # unknown typename


class PositionOverrideTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PositionOverrideType():
    """
    Represents the type of the positioning override on the component 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No position override"
       "Unloaded", "Position overridden, but in an unloaded parent"
       "Explicit", "Position explicitly overridden by user"
       "MatingImplicit", "Position implicitly overridden because of mating conditions"
       "ConstraintImplicit", "Position implicitly overridden because of assembly constraints"
    """
    NotSet = 0  # PositionOverrideTypeMemberType
    Unloaded = 1  # PositionOverrideTypeMemberType
    Explicit = 2  # PositionOverrideTypeMemberType
    MatingImplicit = 3  # PositionOverrideTypeMemberType
    ConstraintImplicit = 4  # PositionOverrideTypeMemberType
    
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
    


