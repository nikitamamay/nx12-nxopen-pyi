# module 'NXOpen.Positioning'
#
# Automatically generated 2025-06-09T14:38:47.234733
#
"""Default documentation for NXOpen.Positioning."""

import typing

import NXOpen
import NXOpen.Assemblies



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class NetworkObjectStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NetworkObjectStatus():
    """
    Specifies the solver status of a movable object. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "Not yet evaluated."
       "Fixed", "Attempt to put constraint between two fixed objects."
       "OverDefined", "Conflicts with other constraints."
       "NotConsistentDims", "Cannot solve with current dimension values. Model fully defined."
       "NotConsistentOther", "Cannot find a solution. Model underdefined."
       "NotConsistentUnknown", "One movable object fixed."
       "NotChanged", "Not evaluated because other parts of the model are over defined or inconsistent."
       "WellDefined", "The constraint is solved and satisfied"
       "UnderDefined", "The constraint is solved and satisfied"
    """
    Unknown = 0  # NetworkObjectStatusMemberType
    Fixed = 1  # NetworkObjectStatusMemberType
    OverDefined = 2  # NetworkObjectStatusMemberType
    NotConsistentDims = 3  # NetworkObjectStatusMemberType
    NotConsistentOther = 4  # NetworkObjectStatusMemberType
    NotConsistentUnknown = 5  # NetworkObjectStatusMemberType
    NotChanged = 6  # NetworkObjectStatusMemberType
    WellDefined = 7  # NetworkObjectStatusMemberType
    UnderDefined = 8  # NetworkObjectStatusMemberType
    
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
    


class Network(NXOpen.NXObject):
    """
    Network for use in positioning objects in NX.  
    
    A network consists of explicitly added constraints and movable objects
    together with others implicitly added because they are connected by 
    to those in the network.
    
    Use :py:meth:`Positioning.Positioner.EstablishNetwork` to create an instance of this class.
    
    .. versionadded:: NX4.0.0
    """
    
    class ObjectStatus():
        """
        Specifies the solver status of a movable object. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "Not yet evaluated."
           "Fixed", "Attempt to put constraint between two fixed objects."
           "OverDefined", "Conflicts with other constraints."
           "NotConsistentDims", "Cannot solve with current dimension values. Model fully defined."
           "NotConsistentOther", "Cannot find a solution. Model underdefined."
           "NotConsistentUnknown", "One movable object fixed."
           "NotChanged", "Not evaluated because other parts of the model are over defined or inconsistent."
           "WellDefined", "The constraint is solved and satisfied"
           "UnderDefined", "The constraint is solved and satisfied"
        """
        Unknown = 0  # NetworkObjectStatusMemberType
        Fixed = 1  # NetworkObjectStatusMemberType
        OverDefined = 2  # NetworkObjectStatusMemberType
        NotConsistentDims = 3  # NetworkObjectStatusMemberType
        NotConsistentOther = 4  # NetworkObjectStatusMemberType
        NotConsistentUnknown = 5  # NetworkObjectStatusMemberType
        NotChanged = 6  # NetworkObjectStatusMemberType
        WellDefined = 7  # NetworkObjectStatusMemberType
        UnderDefined = 8  # NetworkObjectStatusMemberType
        
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
        
    
    
    def AddConstraint(self, constraint: Constraint) -> None:
        """
        Add a :py:class:`Constraint` to the network.
        
        Signature ``AddConstraint(constraint)`` 
        
        :param constraint:  The :py:class:`Constraint` to be added  
        :type constraint: :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveConstraint(self, constraint: Constraint) -> None:
        """
        Remove a :py:class:`Constraint` from the network. A constraint
        explicitly removed by this method may still included in a network solve
        if connected to another constraint or movable object which has been
        explicitly added.
        
        Signature ``RemoveConstraint(constraint)`` 
        
        :param constraint:  The :py:class:`Constraint` to be removed  
        :type constraint: :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveAllConstraints(self) -> None:
        """
        Remove all :py:class:`Constraint`s which have been explcitly added
        to the network.  Those constraints connected to explcicitly added movable
        objects will still be include in a network solve.
        
        Signature ``RemoveAllConstraints()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def AddMovableObject(self, movableObject: NXOpen.NXObject) -> None:
        """
        Add a movable object to the network.  
        
        An object explicitly added
        by this method will be directly moved by calls 
        to :py:meth:`Positioning.Network.DragByRay`,
        :py:meth:`Positioning.Network.DragByTransform` and
        :py:meth:`Positioning.Network.DragByTranslation`.        
        
        Signature ``AddMovableObject(movableObject)`` 
        
        :param movableObject:  An :py:class:`NXObject` to be moved  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def RemoveMovableObject(self, movableObject: NXOpen.NXObject) -> None:
        """
        Remove a movable object from the network.  
        
        An object explicitly
        removed by this method will not be directly moved by calls 
        to :py:meth:`Positioning.Network.DragByRay`,
        :py:meth:`Positioning.Network.DragByTransform` and
        :py:meth:`Positioning.Network.DragByTranslation`, though it
        may still be moved indirectly if constrained to other movable objects.
        
        Signature ``RemoveMovableObject(movableObject)`` 
        
        :param movableObject:  An :py:class:`NXObject` to be removed from the network  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ApplyToModel(self) -> None:
        """
        Applies the current network state to the model.  
        
        This may change the position
        of movable objects and the status of constraints in the model.  Does not do 
        a solve or an update.
        
        Signature ``ApplyToModel()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Solve(self) -> None:
        """
        Solves the constraint network.  
        
        Does apply the results to the model but does not 
        do an update.
        
        Signature ``Solve()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ResetDisplay(self) -> None:
        """
        Returns the display objects to their model positions.  
        
        Signature ``ResetDisplay()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetMovableObjectStatus(self, movableObject: NXOpen.NXObject) -> NetworkObjectStatus:
        """
        Returns the solver status of a movable object.  
        
        Signature ``GetMovableObjectStatus(movableObject)`` 
        
        :param movableObject:  An :py:class:`NXObject` positioned by the network  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        :returns:  The solver status of the movable object  
        :rtype: :py:class:`NXOpen.Positioning.NetworkObjectStatus` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def BeginDrag(self) -> None:
        """
        Notify the network that a sequence of drag operations is about to
        begin.  
        
        This must be called before a series of calls to
        :py:meth:`Positioning.Network.DragByRay`,
        :py:meth:`Positioning.Network.DragByTransform` or
        :py:meth:`Positioning.Network.DragByTranslation`.
        Following a drag, and before any other changes to a network
        are made, :py:meth:`Positioning.Network.EndDrag`
        should be called.
        
        Signature ``BeginDrag()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DragByRay(self, point: NXOpen.Point3d, direction: NXOpen.Vector3d) -> None:
        """
        Move objects which have been added to the network using 
        :py:meth:`Positioning.Network.AddMovableObject`.  
        
        Constraints are honored during the drag so that other
        objects may also move as a result of this call.
        On the first call to this method, a notional point is added to each of
        the objects to be dragged.  On subsequent calls, this notional point,
        and hence the dragged object, is kept as close as possible to the ray
        determined by point and direction. If there are no constraints then the
        point will stay on the ray.
        
        A series of calls to this method can be made between calls to
        :py:meth:`Positioning.Network.BeginDrag` and
        :py:meth:`Positioning.Network.EndDrag`.
        
        Signature ``DragByRay(point, direction)`` 
        
        :param point:  A point on the ray  
        :type point: :py:class:`NXOpen.Point3d` 
        :param direction:  The direction of the ray  
        :type direction: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DragByTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
        Move objects which have been added to the network using 
        :py:meth:`Positioning.Network.AddMovableObject`.  
        
        Constraints are honored during the drag so that other
        objects may also move as a result of this call.
        The rotation is applied first, then the translation.
        
        A series of calls to this method can be made between calls to
        :py:meth:`Positioning.Network.BeginDrag` and
        :py:meth:`Positioning.Network.EndDrag`.
        
        Signature ``DragByTransform(translation, rotation)`` 
        
        :param translation:  The translation to be applied  
        :type translation: :py:class:`NXOpen.Vector3d` 
        :param rotation:  The rotation to be applied  
        :type rotation: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DragByTranslation(self, translation: NXOpen.Vector3d) -> None:
        """
        Move objects which have been added to the network using 
        :py:meth:`Positioning.Network.AddMovableObject`.  
        
        Constraints are honored during the drag so that other
        objects may also move as a result of this call.
        
        Unlike :py:meth:`Positioning.Network.DragByTransform`
        there is no rotational element passed in. This can improve the
        behavior of the constraint solver.
        
        A series of calls to this method can be made between calls to
        :py:meth:`Positioning.Network.BeginDrag` and
        :py:meth:`Positioning.Network.EndDrag`.
        
        Signature ``DragByTranslation(translation)`` 
        
        :param translation:  The translation to be applied  
        :type translation: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX6.0.4
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EndDrag(self) -> None:
        """
        Notify the network that a sequence of drag operations has
        ended.  
        
        This must be called after a series of calls to
        :py:meth:`Positioning.Network.DragByRay`,
        :py:meth:`Positioning.Network.DragByTransform` or
        :py:meth:`Positioning.Network.DragByTranslation`.
        
        Signature ``EndDrag()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetMovingGroup(self, movableObjects: 'list[NXOpen.NXObject]') -> None:
        """
        Set the elements of the moving_group.  
        
        The elements of the moving_group will move as a rigid body
        during a solve or drag operation.  Objects outside the moving
        group can all be prevented from moving by setting 
        :py:meth:`Positioning.Network.NonMovingGroupGrounded``
        
        Signature ``SetMovingGroup(movableObjects)`` 
        
        :param movableObjects:  The :py:class:`NXObject`s to be moved  
        :type movableObjects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EmptyMovingGroup(self) -> None:
        """
        Remove all elements from the moving_group.  
        
        See :py:meth:`Positioning.Network.SetMovingGroup`.
        
        Signature ``EmptyMovingGroup()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def IsReferencedGeometryLoaded(self) -> bool:
        """
        Are the necessary objects loaded so that all connected constraints can be
        included during a drag or solve ?
        
        Signature ``IsReferencedGeometryLoaded()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def LoadReferencedGeometry(self) -> None:
        """
        Load the necessary objects so that all connected constraints can be
        included during a drag or solve.  
        
        If an object is not loaded then the part containing it will be 
        fully loaded by this call.
        
        Signature ``LoadReferencedGeometry()`` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    DisplayComponent: NXOpen.Assemblies.Component = ...
    """
    Returns or sets  
    the :py:class:`Assemblies.Component` in which the display is changed
    by solving the network.  
    
    The display component can be None if display
    changes are made in the part of the network.
    The prototype of the display component should be the part containing the
    network.
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayComponent`` 
    
    :returns:  The component in which the constraints are displayed. Can be NULL.  
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayComponent`` 
    
    :param displayComponent:  The component in which the constraints are displayed. Can be NULL.  
    :type displayComponent: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    MoveObjectsState: bool = ...
    """
    Returns or sets  
    the move objects state for the network.  
    
    When set the display positions of objects are immediately updated
    upon constraint creation or edit.
    
    <hr>
    
    Getter Method
    
    Signature ``MoveObjectsState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``MoveObjectsState`` 
    
    :param moveObjectsState: 
    :type moveObjectsState: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NonMovingGroupGrounded: bool = ...
    """
    Returns or sets  
    the grounded state of non-moving_group objects.  
    
    When set all objects outside the moving_group are fixed and will
    not move during a solve or drag.
    
    <hr>
    
    Getter Method
    
    Signature ``NonMovingGroupGrounded`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``NonMovingGroupGrounded`` 
    
    :param ground: 
    :type ground: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: Network = ...  # unknown typename


class ComponentNetworkArrangementsModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentNetworkArrangementsMode():
    """
    Specifies how changes in the network are applied to arrangements. 
    This setting will be ignored when positioning geometry in a piece part.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Existing", "Apply transforms in arrangements according to existing component properties. Constraints are created non-arrangement specific."
       "InUsed", "Apply transforms in the used arrangement only. Constraints are created arrangement specific in the used arrangement and suppressed in all other arrangements"
    """
    Existing = 0  # ComponentNetworkArrangementsModeMemberType
    InUsed = 1  # ComponentNetworkArrangementsModeMemberType
    
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
    


class ComponentNetwork(Network):
    """
    Network for use in positioning components in NX.  
    
    A component network extends the :py:class:`NXOpen.Positioning.Network` by
    adding support for :py:class:`NXOpen.Assemblies.Arrangement`s.
    
    Use :py:meth:`NXOpen.Positioning.Positioner.EstablishNetwork` to create an instance of this class.
    
    .. versionadded:: NX6.0.0
    """
    
    class ArrangementsMode():
        """
        Specifies how changes in the network are applied to arrangements. 
        This setting will be ignored when positioning geometry in a piece part.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Existing", "Apply transforms in arrangements according to existing component properties. Constraints are created non-arrangement specific."
           "InUsed", "Apply transforms in the used arrangement only. Constraints are created arrangement specific in the used arrangement and suppressed in all other arrangements"
        """
        Existing = 0  # ComponentNetworkArrangementsModeMemberType
        InUsed = 1  # ComponentNetworkArrangementsModeMemberType
        
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
        
    
    NetworkArrangementsMode: ComponentNetworkArrangementsMode = ...
    """
    Returns or sets 
    the arrangements mode for this network.  
    
    <hr>
    
    Getter Method
    
    Signature ``NetworkArrangementsMode`` 
    
    :returns:  The :py:class:`Positioning.ComponentNetworkArrangementsMode`.  
    :rtype: :py:class:`NXOpen.Positioning.ComponentNetworkArrangementsMode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``NetworkArrangementsMode`` 
    
    :param mode:  The :py:class:`Positioning.ComponentNetworkArrangementsMode`. 
    :type mode: :py:class:`NXOpen.Positioning.ComponentNetworkArrangementsMode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NetworkSolveInWorksetMode: bool = ...
    """
    Returns or sets 
    the mode that moves components in the workset instead of the model.  
    
    <hr>
    
    Getter Method
    
    Signature ``NetworkSolveInWorksetMode`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``NetworkSolveInWorksetMode`` 
    
    :param solveInWorkset: 
    :type solveInWorkset: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ComponentNetwork = ...  # unknown typename


class Positioner(NXOpen.NXObject):
    """
    An instance of this class can be used to create :py:class:`NXOpen.Positioning.Constraint`s and
    associated objects.  
    
    To obtain an instance of this class, use :py:meth:`NXOpen.Assemblies.ComponentAssembly.Positioner`
    
    .. versionadded:: NX4.0.0
    """
    
    def CreateConstraint(self, persistent: bool) -> Constraint:
        """
        Creates a new :py:class:`NXOpen.Positioning.Constraint` in the positioner.  
        
        Signature ``CreateConstraint(persistent)`` 
        
        :param persistent:  Persistent state of constraint  
        :type persistent: bool 
        :returns:  The new :py:class:`NXOpen.Positioning.Constraint`  
        :rtype: :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        
        Creates a new :py:class:`NXOpen.Positioning.Constraint` in the positioner.
        
        Signature ``CreateConstraint()`` 
        
        :returns:  The new :py:class:`NXOpen.Positioning.Constraint`  
        :rtype: :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EstablishNetwork(self) -> Network:
        """
        Establishes a :py:class:`NXOpen.Positioning.Network` in the positioner.  
        
        Signature ``EstablishNetwork()`` 
        
        :returns:  The new :py:class:`NXOpen.Positioning.Network`  
        :rtype: :py:class:`NXOpen.Positioning.Network` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ClearNetwork(self) -> None:
        """
        Removes the :py:class:`NXOpen.Positioning.Network` of the positioner.  
        
        The network is added to the delete list by this call.
        
        Signature ``ClearNetwork()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteNonPersistentConstraints(self) -> None:
        """
        Deletes all the non-persistent :py:class:`NXOpen.Positioning.Constraint`s of the positioner.  
        
        Signature ``DeleteNonPersistentConstraints()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Constraints: ConstraintCollection = ...
    """
    The collection of :py:class:`NXOpen.Positioning.Constraint`s defined in the positioner 
    
    Signature ``Constraints`` 
    
    .. versionadded:: NX3.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.Positioning.ConstraintCollection`
    """
    Null: Positioner = ...  # unknown typename


class ComponentPositioner(Positioner):
    """
    An instance of this class can be used to create :py:class:`NXOpen.Positioning.Constraint`s and
    associated objects.  
    
    To obtain an instance of this class, use :py:meth:`NXOpen.Assemblies.ComponentAssembly.Positioner`
    
    .. versionadded:: NX4.0.0
    """
    
    def BeginMoveComponent(self) -> None:
        """
        Begins a mode of operation where (1) each new :py:class:`NXOpen.Positioning.Constraint`
        is created as transient and (2) a component transform is applied at the level where 
        position is controlled for the component, typically in the component's immediate parent.  
        
        Signature ``BeginMoveComponent()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EndMoveComponent(self) -> None:
        """
        Ends the mode of operation started by 
        :py:meth:`NXOpen.Positioning.ComponentPositioner.BeginMoveComponent`
        All constraints created while in that mode will be deleted.  
        
        Signature ``EndMoveComponent()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def BeginAssemblyConstraints(self) -> None:
        """
        Begins a mode of operation where (1) each new :py:class:`NXOpen.Positioning.Constraint`
        created by this :py:class:`NXOpen.Positioning.ComponentPositioner` applies to
        components in the part of the positioner (or to components with variable component positioning
        defined in the part of the positioner) and (2) and component transforms derived from
        a :py:class:`NXOpen.Positioning.Network` will apply to components in the part of the positioner.  
        
        Signature ``BeginAssemblyConstraints()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EndAssemblyConstraints(self) -> None:
        """
        Ends the mode of operation started by 
        :py:meth:`NXOpen.Positioning.ComponentPositioner.BeginAssemblyConstraints`
        All non-persistent constraints in this :py:class:`NXOpen.Positioning.ComponentPositioner`
        will be deleted.  
        
        Signature ``EndAssemblyConstraints()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def BeginMoveComponentInWorkset(self) -> None:
        """
        Begins a mode of operation where (1) each new :py:class:`NXOpen.Positioning.Constraint`
        is created as transient and (2) a component transform is applied at the workset level.  
        
        Signature ``BeginMoveComponentInWorkset()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EndMoveComponentInWorkset(self) -> None:
        """
        Ends the mode of operation started by
        :py:meth:`NXOpen.Positioning.ComponentPositioner.BeginMoveComponentInWorkset`
        All constraints created while in that mode will be deleted.  
        
        Signature ``EndMoveComponentInWorkset()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def LoadConstraintGeometry(self, constraints: 'list[ComponentConstraint]') -> None:
        """
        Attempts to load all the parts that contain unloaded geometry that is referenced by the constraints
        or by any related constraints.  
        
        The constraints must be within the positioner otherwise an error will be
        raised. Any constraints that are suppressed will be ignored.
        
        If the number of constraints is zero then the function attempts to load the parts for every unsuppressed
        constraint in the positioner.
        
        Calling this function can cause objects to be logged for update and therefore the caller of this function
        must call update.
        
        Signature ``LoadConstraintGeometry(constraints)`` 
        
        :param constraints:  Constraints  
        :type constraints: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SolvePostponedConstraints(self) -> None:
        """
        Solves constraints in all arrangements that are currently postponing 
        their solve.  
        
        This could lead to updating the model if required.  This call
        will have no effect if assembly constraint update has been delayed. 
        
        Signature ``SolvePostponedConstraints()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    DisplayConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether constraints in the part of this positioner
    are to be displayed on the graphics window or not.  
    
    (This is a separate
    system from hiding and showing individual constraints.)  This flag controls the
    visibility of both suppressed and unsuppressed constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplayConstraints`` 
    
    :param display: 
    :type display: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    DisplaySuppressedConstraints: bool = ...
    """
    Returns or sets 
    the flag indicating whether suppressed constraints in the part of this positioner
    are to be displayed on the graphics window or not.  
    
    (This is a separate
    system from hiding and showing individual constraints.)
    
    <hr>
    
    Getter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``DisplaySuppressedConstraints`` 
    
    :param display: 
    :type display: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    MoveDumbGeometry: bool = ...
    """
    Returns or sets  the flag that enables the positioner to reposition dumb geometry.  
    
    Dumb geometry
    is any geometry that is not controlled by another object such as a 
    :py:class:`NXOpen.Features.Feature` object.  This flag has no effect
    on Routing geometry (segments and control points) as they are always considered
    movable by the positioner.
    
    <hr>
    
    Getter Method
    
    Signature ``MoveDumbGeometry`` 
    
    :returns:  Whether the positioner will reposition dumb geometry  
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``MoveDumbGeometry`` 
    
    :param moveDumbGeometry:  Whether the positioner will reposition dumb geometry  
    :type moveDumbGeometry: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    PrimaryArrangement: NXOpen.Assemblies.Arrangement = ...
    """
    Returns or sets  
    the :py:class:`NXOpen.Assemblies.Arrangement` in which the 
    primary :py:class:`NXOpen.Positioning.Network` will solve.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryArrangement`` 
    
    :returns:  The primary :py:class:`NXOpen.Assemblies.Arrangement`.  
    :rtype: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``PrimaryArrangement`` 
    
    :param arrangement:  The primary :py:class:`NXOpen.Assemblies.Arrangement`.  
    :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ComponentPositioner = ...  # unknown typename


class DisplayedConstraintCollection(NXOpen.TaggedObjectCollection):
    """
    a collection of displayed constraints    
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX7.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    


class ConstraintTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintType():
    """
    Specifies the type of a constraint. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", "No type"
       "Touch", "Two geometries touch"
       "Concentric", "Two geometries share a center and plane"
       "Fix", "One movable object fixed"
       "Distance", "Two geometries have a specified distance between them"
       "Parallel", "Two geometries are parallel"
       "Perpendicular", "Two geometries are perpendicular"
       "Center12", "One geometry is positioned mid-way between two others"
       "Center22", "An implicit plane between two geometries of one movable object is positioned mid-way between two others"
       "Angle", "Two geometries have a specified angle between them"
       "Fit", "Two geometries are coincident"
       "Bond", "A number of movable objects form a rigid group"
       "OrientAngle", "Two geometries have a specified angle between them about an axis"
       "SplineData", "A spline and its defining points"
       "SplineLength", "Constrains the curve length of a spline"
       "LinearPattern", "For internal use only"
       "CircularPattern", "For internal use only"
       "Linear2dPattern", "For internal use only"
       "RadiantPattern", "For internal use only"
       "AlignLock", "Two geometries are constrained to have a common axis and no rotation about it"
       "CommonOffsetTransform", "For internal use only"
       "Hinge", "For internal use only"
       "Slider", "For internal use only"
       "Cylindrical", "For internal use only"
       "Ball", "For internal use only"
       "Screw", "For internal use only"
       "Gear", "For internal use only"
       "RackPinion", "For internal use only"
       "Cable", "For internal use only"
    """
    Undefined = 0  # ConstraintTypeMemberType
    Touch = 1  # ConstraintTypeMemberType
    Concentric = 2  # ConstraintTypeMemberType
    Fix = 3  # ConstraintTypeMemberType
    Distance = 4  # ConstraintTypeMemberType
    Parallel = 5  # ConstraintTypeMemberType
    Perpendicular = 6  # ConstraintTypeMemberType
    Center12 = 7  # ConstraintTypeMemberType
    Center22 = 8  # ConstraintTypeMemberType
    Angle = 9  # ConstraintTypeMemberType
    Fit = 10  # ConstraintTypeMemberType
    Bond = 11  # ConstraintTypeMemberType
    OrientAngle = 12  # ConstraintTypeMemberType
    SplineData = 13  # ConstraintTypeMemberType
    SplineLength = 14  # ConstraintTypeMemberType
    LinearPattern = 15  # ConstraintTypeMemberType
    CircularPattern = 16  # ConstraintTypeMemberType
    Linear2dPattern = 17  # ConstraintTypeMemberType
    RadiantPattern = 18  # ConstraintTypeMemberType
    AlignLock = 19  # ConstraintTypeMemberType
    CommonOffsetTransform = 20  # ConstraintTypeMemberType
    Hinge = 21  # ConstraintTypeMemberType
    Slider = 22  # ConstraintTypeMemberType
    Cylindrical = 23  # ConstraintTypeMemberType
    Ball = 24  # ConstraintTypeMemberType
    Screw = 25  # ConstraintTypeMemberType
    Gear = 26  # ConstraintTypeMemberType
    RackPinion = 27  # ConstraintTypeMemberType
    Cable = 28  # ConstraintTypeMemberType
    
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
    


class ConstraintAlignmentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintAlignment():
    """
    Specifies alignment of directed geometries used in a constraint. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InferAlign", "Allow the solver to decide the alignment"
       "CoAlign", "Directions are the same"
       "ContraAlign", "Directions are opposite"
    """
    InferAlign = 0  # ConstraintAlignmentMemberType
    CoAlign = 1  # ConstraintAlignmentMemberType
    ContraAlign = 2  # ConstraintAlignmentMemberType
    
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
    


class ConstraintSolverStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintSolverStatus():
    """
    Specifies the status of a constraint. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NewlyCreated", "Not evaluated or suppressed since creation"
       "Suppressed", "Constraint is suppressed"
       "OutOfDate", "Needs evaluation"
       "OverConstrained", "Conflicts with other constraints"
       "NotConsistentDims", "Cannot solve with current dimension values. Model fully defined"
       "NotConsistentOther", "Cannot find a solution. Model underdefined"
       "NotConsistentUnknown", "Cannot find a solution"
       "BetweenFixed", "Attempt to put constraint between two fixed objects"
       "NotSolved", "Not evaluated because other parts of the model are over defined or inconsistent"
       "Solved", "The constraint is solved and satisfied"
       "CannotSolve", "The constraint has invalid geometry and could not be passed to the solver"
       "Delayed", "The constraint is delayed and will not solve"
       "IgnoredInArrangement", "The current arrangement ignores all constraints and they will not solve"
       "InternallyInconsistent", "The constraint references invalid geometry for this constraint type"
       "UnloadedGeometry", "The constraint could not solve as some geometry is unloaded"
       "PendingConvertedMc", "The constraint has been converted from a mating condition and has not solved since conversion"
       "ConflictingWithWave", "The constraint has been suppressed because it's conflicting with WAVE"
       "InconsistentLimits", "The constraint has limits that are inconsistent and it could not be passed to the solver"
       "BeyondLimits", "The value of the expression of the constraint is beyond its limits and it could not be passed to the solver"
    """
    NewlyCreated = 0  # ConstraintSolverStatusMemberType
    Suppressed = 1  # ConstraintSolverStatusMemberType
    OutOfDate = 2  # ConstraintSolverStatusMemberType
    OverConstrained = 3  # ConstraintSolverStatusMemberType
    NotConsistentDims = 4  # ConstraintSolverStatusMemberType
    NotConsistentOther = 5  # ConstraintSolverStatusMemberType
    NotConsistentUnknown = 6  # ConstraintSolverStatusMemberType
    BetweenFixed = 7  # ConstraintSolverStatusMemberType
    NotSolved = 8  # ConstraintSolverStatusMemberType
    Solved = 9  # ConstraintSolverStatusMemberType
    CannotSolve = 10  # ConstraintSolverStatusMemberType
    Delayed = 11  # ConstraintSolverStatusMemberType
    IgnoredInArrangement = 12  # ConstraintSolverStatusMemberType
    InternallyInconsistent = 13  # ConstraintSolverStatusMemberType
    UnloadedGeometry = 14  # ConstraintSolverStatusMemberType
    PendingConvertedMc = 15  # ConstraintSolverStatusMemberType
    ConflictingWithWave = 16  # ConstraintSolverStatusMemberType
    InconsistentLimits = 17  # ConstraintSolverStatusMemberType
    BeyondLimits = 18  # ConstraintSolverStatusMemberType
    
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
    


class ConstraintSplineTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintSplineType():
    """
    Specifies how the spline points define the shape of the spline. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ByPoles", "Spline points define control points."
       "ByPoints", "Spline points define interpolation/through points."
       "Invalid", "Not a valid spline constraint."
    """
    ByPoles = 0  # ConstraintSplineTypeMemberType
    ByPoints = 1  # ConstraintSplineTypeMemberType
    Invalid = 2  # ConstraintSplineTypeMemberType
    
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
    


class Constraint(NXOpen.NXObject):
    """
    Constraints for use in positioning objects in NX.  
    
    For constraints between components, the subclass :py:class:`NXOpen.Positioning.ComponentConstraint` should be used by preference.
    
    Some constraint types have an :py:class:`NXOpen.Expression` associated with them, which the user can change to determine the value 
    of that constraint. This expression applies to distance and angle constraints. The user can choose for this expression value to be driven 
    by the system, so it will not have a fixed value set by the user.  
    
    The constraint types with values can be given limits. If the constraint is driven, the solver will always try to solve it to remain within 
    those limits, and the constraint will fail if this is not possible. If the constraint is driving, it will have a failure status if its value 
    is set to violate those limits (though it will still solve the model). 
    
    To create a new instance of this class, use :py:meth:`NXOpen.Positioning.Positioner.CreateConstraint`
    
    .. versionadded:: NX4.0.0
    """
    
    class Type():
        """
        Specifies the type of a constraint. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Undefined", "No type"
           "Touch", "Two geometries touch"
           "Concentric", "Two geometries share a center and plane"
           "Fix", "One movable object fixed"
           "Distance", "Two geometries have a specified distance between them"
           "Parallel", "Two geometries are parallel"
           "Perpendicular", "Two geometries are perpendicular"
           "Center12", "One geometry is positioned mid-way between two others"
           "Center22", "An implicit plane between two geometries of one movable object is positioned mid-way between two others"
           "Angle", "Two geometries have a specified angle between them"
           "Fit", "Two geometries are coincident"
           "Bond", "A number of movable objects form a rigid group"
           "OrientAngle", "Two geometries have a specified angle between them about an axis"
           "SplineData", "A spline and its defining points"
           "SplineLength", "Constrains the curve length of a spline"
           "LinearPattern", "For internal use only"
           "CircularPattern", "For internal use only"
           "Linear2dPattern", "For internal use only"
           "RadiantPattern", "For internal use only"
           "AlignLock", "Two geometries are constrained to have a common axis and no rotation about it"
           "CommonOffsetTransform", "For internal use only"
           "Hinge", "For internal use only"
           "Slider", "For internal use only"
           "Cylindrical", "For internal use only"
           "Ball", "For internal use only"
           "Screw", "For internal use only"
           "Gear", "For internal use only"
           "RackPinion", "For internal use only"
           "Cable", "For internal use only"
        """
        Undefined = 0  # ConstraintTypeMemberType
        Touch = 1  # ConstraintTypeMemberType
        Concentric = 2  # ConstraintTypeMemberType
        Fix = 3  # ConstraintTypeMemberType
        Distance = 4  # ConstraintTypeMemberType
        Parallel = 5  # ConstraintTypeMemberType
        Perpendicular = 6  # ConstraintTypeMemberType
        Center12 = 7  # ConstraintTypeMemberType
        Center22 = 8  # ConstraintTypeMemberType
        Angle = 9  # ConstraintTypeMemberType
        Fit = 10  # ConstraintTypeMemberType
        Bond = 11  # ConstraintTypeMemberType
        OrientAngle = 12  # ConstraintTypeMemberType
        SplineData = 13  # ConstraintTypeMemberType
        SplineLength = 14  # ConstraintTypeMemberType
        LinearPattern = 15  # ConstraintTypeMemberType
        CircularPattern = 16  # ConstraintTypeMemberType
        Linear2dPattern = 17  # ConstraintTypeMemberType
        RadiantPattern = 18  # ConstraintTypeMemberType
        AlignLock = 19  # ConstraintTypeMemberType
        CommonOffsetTransform = 20  # ConstraintTypeMemberType
        Hinge = 21  # ConstraintTypeMemberType
        Slider = 22  # ConstraintTypeMemberType
        Cylindrical = 23  # ConstraintTypeMemberType
        Ball = 24  # ConstraintTypeMemberType
        Screw = 25  # ConstraintTypeMemberType
        Gear = 26  # ConstraintTypeMemberType
        RackPinion = 27  # ConstraintTypeMemberType
        Cable = 28  # ConstraintTypeMemberType
        
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
        
    
    
    class Alignment():
        """
        Specifies alignment of directed geometries used in a constraint. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InferAlign", "Allow the solver to decide the alignment"
           "CoAlign", "Directions are the same"
           "ContraAlign", "Directions are opposite"
        """
        InferAlign = 0  # ConstraintAlignmentMemberType
        CoAlign = 1  # ConstraintAlignmentMemberType
        ContraAlign = 2  # ConstraintAlignmentMemberType
        
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
        
    
    
    class SolverStatus():
        """
        Specifies the status of a constraint. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NewlyCreated", "Not evaluated or suppressed since creation"
           "Suppressed", "Constraint is suppressed"
           "OutOfDate", "Needs evaluation"
           "OverConstrained", "Conflicts with other constraints"
           "NotConsistentDims", "Cannot solve with current dimension values. Model fully defined"
           "NotConsistentOther", "Cannot find a solution. Model underdefined"
           "NotConsistentUnknown", "Cannot find a solution"
           "BetweenFixed", "Attempt to put constraint between two fixed objects"
           "NotSolved", "Not evaluated because other parts of the model are over defined or inconsistent"
           "Solved", "The constraint is solved and satisfied"
           "CannotSolve", "The constraint has invalid geometry and could not be passed to the solver"
           "Delayed", "The constraint is delayed and will not solve"
           "IgnoredInArrangement", "The current arrangement ignores all constraints and they will not solve"
           "InternallyInconsistent", "The constraint references invalid geometry for this constraint type"
           "UnloadedGeometry", "The constraint could not solve as some geometry is unloaded"
           "PendingConvertedMc", "The constraint has been converted from a mating condition and has not solved since conversion"
           "ConflictingWithWave", "The constraint has been suppressed because it's conflicting with WAVE"
           "InconsistentLimits", "The constraint has limits that are inconsistent and it could not be passed to the solver"
           "BeyondLimits", "The value of the expression of the constraint is beyond its limits and it could not be passed to the solver"
        """
        NewlyCreated = 0  # ConstraintSolverStatusMemberType
        Suppressed = 1  # ConstraintSolverStatusMemberType
        OutOfDate = 2  # ConstraintSolverStatusMemberType
        OverConstrained = 3  # ConstraintSolverStatusMemberType
        NotConsistentDims = 4  # ConstraintSolverStatusMemberType
        NotConsistentOther = 5  # ConstraintSolverStatusMemberType
        NotConsistentUnknown = 6  # ConstraintSolverStatusMemberType
        BetweenFixed = 7  # ConstraintSolverStatusMemberType
        NotSolved = 8  # ConstraintSolverStatusMemberType
        Solved = 9  # ConstraintSolverStatusMemberType
        CannotSolve = 10  # ConstraintSolverStatusMemberType
        Delayed = 11  # ConstraintSolverStatusMemberType
        IgnoredInArrangement = 12  # ConstraintSolverStatusMemberType
        InternallyInconsistent = 13  # ConstraintSolverStatusMemberType
        UnloadedGeometry = 14  # ConstraintSolverStatusMemberType
        PendingConvertedMc = 15  # ConstraintSolverStatusMemberType
        ConflictingWithWave = 16  # ConstraintSolverStatusMemberType
        InconsistentLimits = 17  # ConstraintSolverStatusMemberType
        BeyondLimits = 18  # ConstraintSolverStatusMemberType
        
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
        
    
    
    class SplineType():
        """
        Specifies how the spline points define the shape of the spline. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ByPoles", "Spline points define control points."
           "ByPoints", "Spline points define interpolation/through points."
           "Invalid", "Not a valid spline constraint."
        """
        ByPoles = 0  # ConstraintSplineTypeMemberType
        ByPoints = 1  # ConstraintSplineTypeMemberType
        Invalid = 2  # ConstraintSplineTypeMemberType
        
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
        
    
    
    def GetReferences(self) -> 'list[ConstraintReference]':
        """
        Gets all the :py:class:`NXOpen.Positioning.ConstraintReference`s for the 
        constraint.  
        
        Signature ``GetReferences()`` 
        
        :returns:  ConstraintReferences used by this constraint  
        :rtype: list of :py:class:`NXOpen.Positioning.ConstraintReference` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteConstraintReference(self, constraintReference: ConstraintReference) -> None:
        """
        Removes a :py:class:`NXOpen.Positioning.ConstraintReference` from the constraint.  
        
        Signature ``DeleteConstraintReference(constraintReference)`` 
        
        :param constraintReference:  The constraint reference to remove. A list                                                                                   of references can be obtained via                                                                                  :py:meth:`NXOpen.Positioning.Constraint.GetReferences`.  
        :type constraintReference: :py:class:`NXOpen.Positioning.ConstraintReference` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @typing.overload
    def CreateConstraintReference(self, movableObject: NXOpen.NXObject, geometry: NXOpen.NXObject, usesAxis: bool, isIndirect: bool) -> ConstraintReference:
        """
        Adds geometry to a constraint and sets the movable object
        to be constrained.
        
        Signature ``CreateConstraintReference(movableObject, geometry, usesAxis, isIndirect)`` 
        
        :param movableObject:  Object to be positioned by constraint  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        :param geometry:  Geometry used to define constraint  
        :type geometry: :py:class:`NXOpen.NXObject` 
        :param usesAxis:  Use axis of geometry  
        :type usesAxis: bool 
        :param isIndirect:  Geometry is to be used indirectly to identify geometry in another part  
        :type isIndirect: bool 
        :returns:  The new :py:class:`NXOpen.Positioning.ConstraintReference`  
        :rtype: :py:class:`NXOpen.Positioning.ConstraintReference` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    @typing.overload
    def CreateConstraintReference(self, movableObject: NXOpen.NXObject, geometry: NXOpen.NXObject, usesAxis: bool, isIndirect: bool, usePortRotate: bool) -> ConstraintReference:
        """
        Adds geometry to a constraint and sets the movable object
        to be constrained.  
        
        Signature ``CreateConstraintReference(movableObject, geometry, usesAxis, isIndirect, usePortRotate)`` 
        
        :param movableObject:  Object to be positioned by constraint  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        :param geometry:  Geometry used to define constraint  
        :type geometry: :py:class:`NXOpen.NXObject` 
        :param usesAxis:  Use axis of geometry  
        :type usesAxis: bool 
        :param isIndirect:  Geometry is to be used indirectly to identify geometry in another part  
        :type isIndirect: bool 
        :param usePortRotate:  Use rotate vector of :py:class:`NXOpen.Routing.Port`.  
        :type usePortRotate: bool 
        :returns:  The new :py:class:`NXOpen.Positioning.ConstraintReference`  
        :rtype: :py:class:`NXOpen.Positioning.ConstraintReference` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def EditConstraintReference(self, constraintReference: ConstraintReference, movableObject: NXOpen.NXObject, geometry: NXOpen.NXObject, usesAxis: bool, isIndirect: bool, usePortRotate: bool) -> None:
        """
        Adds geometry to a constraint and sets the movable object
        to be constrained, replacing the properties of an existing
        reference of the constraint.  
        
        Signature ``EditConstraintReference(constraintReference, movableObject, geometry, usesAxis, isIndirect, usePortRotate)`` 
        
        :param constraintReference:  The :py:class:`NXOpen.Positioning.ConstraintReference` whose properties are to be changed  
        :type constraintReference: :py:class:`NXOpen.Positioning.ConstraintReference` 
        :param movableObject:  Object to be positioned by constraint  
        :type movableObject: :py:class:`NXOpen.NXObject` 
        :param geometry:  Geometry used to define constraint  
        :type geometry: :py:class:`NXOpen.NXObject` 
        :param usesAxis:  Use axis of geometry  
        :type usesAxis: bool 
        :param isIndirect:  Geometry is to be used indirectly to identify geometry in another part  
        :type isIndirect: bool 
        :param usePortRotate:  Use rotate vector of :py:class:`NXOpen.Routing.Port`.  
        :type usePortRotate: bool 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def FlipAlignment(self) -> None:
        """
        Reverses the constraint alignment if this is possible.  
        
        Signature ``FlipAlignment()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetExpression(self, expression: str) -> None:
        """
        The :py:class:`NXOpen.Expression` of a constraint - only for distance or angle constraints.  
        
        Signature ``SetExpression(expression)`` 
        
        :param expression:  Name of expression used in the constraint  
        :type expression: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetConstraintStatus(self) -> ConstraintSolverStatus:
        """
        Returns the solver status of a constraint.  
        
        Signature ``GetConstraintStatus()`` 
        
        :returns:  The solver status of the constraint  
        :rtype: :py:class:`NXOpen.Positioning.ConstraintSolverStatus` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetAlignmentHint(self, alignment: ConstraintAlignment) -> None:
        """
        Set a hint as to which alignment should be used by the
        solver for this constraint.  
        
        If the constraint does not solve using this alignment
        then the hint will be ignored.                
        
        The hint can only have an effect when the alignment of
        [version_created("4")] 
        the constraint, as returned by :py:meth:`NXOpen.Positioning.Constraint.ConstraintAlignment`,
        is :py:class:`NXOpen.Positioning.ConstraintAlignment.InferAlign <NXOpen.Positioning.ConstraintAlignment>`.
        
        The hint can only have an effect when the constraint has been
        explicitly added to a :py:class:`NXOpen.Positioning.Network`.
        
        Passing in :py:class:`NXOpen.Positioning.ConstraintAlignment.InferAlign <NXOpen.Positioning.ConstraintAlignment>` as the alignment
        argument will have no effect.
        
        The hint is forgotten after an update.
        
        Signature ``SetAlignmentHint(alignment)`` 
        
        :param alignment:  The alignment hint  
        :type alignment: :py:class:`NXOpen.Positioning.ConstraintAlignment` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GenerateConversionReport(self) -> 'list[str]':
        """
        Returns a textual conversion report this constraint from when it was converted from a
        Mating Constraint to an Assembly Constraint.  
        
        If this isn't a converted constraint
        or there were no problems converting this constraint, then an empty string is returned.
        
        Signature ``GenerateConversionReport()`` 
        
        :returns:  The text lines of the conversion report  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ReverseDirection(self) -> None:
        """
        Reverses the constraint direction.  
        
        This operation reverses the :py:meth:`NXOpen.Positioning.ConstraintReference.Order`
        on each :py:class:`NXOpen.Positioning.ConstraintReference`.
        So "Inside" becomes "Outside", "Outside" becomes "Inside" and "Unknown" remains as it is.
        
        Signature ``ReverseDirection()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDisplayedConstraint(self) -> DisplayedConstraint:
        """
        Gets the :py:class:`NXOpen.Positioning.DisplayedConstraint` that is in the same part as that of the constraint.  
        
        Note that this will be None if the part has not been the displayed part since the constraint was created.
        
        Signature ``GetDisplayedConstraint()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Positioning.DisplayedConstraint` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Renew(self) -> None:
        """
        Changes the constraint to solve with the latest version of the constraint code.  
        
        Signature ``Renew()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Automatic: bool = ...
    """
    Returns or sets  the flag marking the constraint as an "automatic" constraint.  
    
    Automatic constraints are
    constraints created by the system, but are visible and editable by the user.  Automatic
    constraints are automatically deleted when one of the referenced objects are deleted
    by update. 
    
    <hr>
    
    Getter Method
    
    Signature ``Automatic`` 
    
    :returns:  The automatic state   
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``Automatic`` 
    
    :param isauto:  The automatic state  
    :type isauto: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ConstraintAlignment: ConstraintAlignment = ...
    """
    Returns or sets  
    the alignment behavior for the constraint.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintAlignment`` 
    
    :returns:  Alignment behavior for constraint  
    :rtype: :py:class:`NXOpen.Positioning.ConstraintAlignment` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintAlignment`` 
    
    :param alignment:  Alignment behavior for constraint  
    :type alignment: :py:class:`NXOpen.Positioning.ConstraintAlignment` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ConstraintType: ConstraintType = ...
    """
    Returns or sets  
    the constraint type.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Positioning.ConstraintType` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintType`` 
    
    :param constraintType: 
    :type constraintType: :py:class:`NXOpen.Positioning.ConstraintType` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Expression: NXOpen.Expression = ...
    """
    Returns  
    the :py:class:`NXOpen.Expression` of a constraint.  
    
    The expression will be unused unless this constraint type supports an expression, 
    such as a distance or angle constraint.
    
    <hr>
    
    Getter Method
    
    Signature ``Expression`` 
    
    :returns:  Expression used in the constraint  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ExpressionDriven: bool = ...
    """
    Returns or sets  
    the driven state of the expression of a constraint.  
    
    The value of a driven expression can change. Driven expression values are controlled 
    by the solver and cannot be edited by the user. Only distance and angle constraints can
    have their expression made driven.
    
    <hr>
    
    Getter Method
    
    Signature ``ExpressionDriven`` 
    
    :returns:  Whether or not the expression is driven.  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ExpressionDriven`` 
    
    :param expressionDriven:  Whether or not the expression is driven.  
    :type expressionDriven: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LowerLimitEnabled: bool = ...
    """
    Returns or sets  
    the lower limit of the expression of a constraint.  
    
    The limit expression will only be used for constraint types that can have their expression made driven. 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerLimitEnabled`` 
    
    :returns:  Return if the constraint has a lower limit of the expression enabled  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``LowerLimitEnabled`` 
    
    :param hasLimit:  Whether or not the lower limit of the expression is enabled.  
    :type hasLimit: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LowerLimitExpression: NXOpen.Expression = ...
    """
    Returns  
    the lower limit of the expression of a constraint.  
    
    The limit expression will only be used for certain constraint types, and they must have an expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerLimitExpression`` 
    
    :returns:  Return the lower limit of the expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LowerLimitRightHandSide: str = ...
    """
    Returns or sets  
    the lower limit of the expression right hand side of a constraint.  
    
    The limit expression will only be used for certain constraint types, and they must have an expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerLimitRightHandSide`` 
    
    :returns:  Return the lower limit right hand side of the expression.  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``LowerLimitRightHandSide`` 
    
    :param limitRightHandSide:  The expression to be applied to the lower limit of the expression.  
    :type limitRightHandSide: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    OffsetExpression: NXOpen.Expression = ...
    """
    Returns  
    the offset of a constraint.  
    
    The offset will only be used for coupler constraint types. 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetExpression`` 
    
    :returns:  Return the offset expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    OffsetRightHandSide: str = ...
    """
    Returns or sets  
    the offset right hand side of a constraint.  
    
    The offset right hand side will only be used for coupler constraint types. 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetRightHandSide`` 
    
    :returns:  Return the offset expression.  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``OffsetRightHandSide`` 
    
    :param offset:  The offset to be applied to the constraint.  
    :type offset: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Persistent: bool = ...
    """
    Returns or sets  
    the persistent state of the constraint.  
    
    <hr>
    
    Getter Method
    
    Signature ``Persistent`` 
    
    :returns:   The persistent state  
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``Persistent`` 
    
    :param persistent:   The persistent state  
    :type persistent: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondExpression: NXOpen.Expression = ...
    """
    Returns  
    the second :py:class:`NXOpen.Expression` of a constraint.  
    
    The second expression will be unused unless this constraint type supports a second expression. 
    This only applies to cylindrical joints.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondExpression`` 
    
    :returns:  Return the second expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondExpressionDriven: bool = ...
    """
    Returns or sets  
    the driven state of the second expression of a constraint.  
    
    The value of the driven second expression can change. Driven second expression values are controlled 
    by the solver and cannot be edited by the user. This only applies to cylindrical joints.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondExpressionDriven`` 
    
    :returns:  Whether or not the second expression is driven.  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondExpressionDriven`` 
    
    :param secondExpressionDriven:  Whether or not the second expression is driven.  
    :type secondExpressionDriven: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondExpressionRightHandSide: str = ...
    """
    Returns or sets  
    the second expression right hand side of a constraint.  
    
    The second expression right hand side will be unused unless this constraint type supports a second expression. 
    This only applies to cylindrical joints.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondExpressionRightHandSide`` 
    
    :returns:  Return the second expression.  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondExpressionRightHandSide`` 
    
    :param secondExpressionRightHandSide:  The second expression to be applied to the constraint.  
    :type secondExpressionRightHandSide: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondLowerLimitEnabled: bool = ...
    """
    Returns or sets  
    the lower limit of the second expression of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondLowerLimitEnabled`` 
    
    :returns:  Return if the constraint has a lower limit of the second expression enabled  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondLowerLimitEnabled`` 
    
    :param hasLimit:  Whether or not the lower limit of the second expression is enabled.  
    :type hasLimit: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondLowerLimitExpression: NXOpen.Expression = ...
    """
    Returns  
    the lower limit of the second expression of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondLowerLimitExpression`` 
    
    :returns:  Return the lower limit of the second expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondLowerLimitRightHandSide: str = ...
    """
    Returns or sets  
    the lower limit of the second expression right hand side of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondLowerLimitRightHandSide`` 
    
    :returns:  Return the lower limit right hand side of the second expression.  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondLowerLimitRightHandSide`` 
    
    :param limitRightHandSide:  The expression to be applied to the lower limit of the second expression.  
    :type limitRightHandSide: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondUpperLimitEnabled: bool = ...
    """
    Returns or sets  
    the upper limit of the second expression of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondUpperLimitEnabled`` 
    
    :returns:  Return if the constraint has an upper limit of the second expression enabled  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondUpperLimitEnabled`` 
    
    :param hasLimit:  Whether or not the upper limit of the second expression is enabled.  
    :type hasLimit: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondUpperLimitExpression: NXOpen.Expression = ...
    """
    Returns  
    the upper limit of the second expression of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondUpperLimitExpression`` 
    
    :returns:  Return the upper limit of the second expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SecondUpperLimitRightHandSide: str = ...
    """
    Returns or sets  
    the upper limit of the second expression right hand side of a constraint.  
    
    The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondUpperLimitRightHandSide`` 
    
    :returns:  Return the upper limit right hand side of the second expression.  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SecondUpperLimitRightHandSide`` 
    
    :param limitRightHandSide:  The expression to be applied to the upper limit of the second expression.  
    :type limitRightHandSide: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SplinePointsType: ConstraintSplineType = ...
    """
    Returns or sets  the type of the spline.  
    
    Only valid if the type of the constraint is
    set to :py:class:`NXOpen.Positioning.ConstraintType.SplineData <NXOpen.Positioning.ConstraintType>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``SplinePointsType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Positioning.ConstraintSplineType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``SplinePointsType`` 
    
    :param splineType: 
    :type splineType: :py:class:`NXOpen.Positioning.ConstraintSplineType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Suppressed: bool = ...
    """
    Returns or sets  
    the suppression state for the constraint.  
    
    In a :py:class:`NXOpen.Positioning.ComponentConstraint` this is the state in the :py:meth:`NXOpen.Positioning.ComponentPositioner.PrimaryArrangement``."
    
    <hr>
    
    Getter Method
    
    Signature ``Suppressed`` 
    
    :returns:   The suppression state  
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``Suppressed`` 
    
    :param suppressed:   The suppression state  
    :type suppressed: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UpperLimitEnabled: bool = ...
    """
    Returns or sets  
    the upper limit of the expression of a constraint.  
    
    The limit expression will only be used for constraint types that can have their expression made driven. 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperLimitEnabled`` 
    
    :returns:  Return if the constraint has an upper limit of the expression enabled  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``UpperLimitEnabled`` 
    
    :param hasLimit:  Whether or not the upper limit of the expression is enabled.  
    :type hasLimit: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UpperLimitExpression: NXOpen.Expression = ...
    """
    Returns  
    the upper limit of the expression of a constraint.  
    
    The limit expression will only be used for certain constraint types, and they must have an expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperLimitExpression`` 
    
    :returns:  Return the upper limit of the expression.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UpperLimitRightHandSide: str = ...
    """
    Returns or sets  
    the upper limit of the expression right hand side of a constraint.  
    
    The limit expression will only be used for certain constraint types, and they must have an expression. 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperLimitRightHandSide`` 
    
    :returns:  Return the upper limit right hand side of the expression.  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``UpperLimitRightHandSide`` 
    
    :param limitRightHandSide:  The expression to be applied to the upper limit of the expression.  
    :type limitRightHandSide: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: Constraint = ...  # unknown typename


class ComponentConstraintDirectionToFixedMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentConstraintDirectionToFixed():
    """
    Specifies how a constraint affects the positioning of a component.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "No information available"
       "Toward", "Toward fixed geometry"
       "AwayFrom", "Away from fixed geometry"
       "NothingFixed", "The network does not contain any fixed geometry"
       "Fix", "The constraint is a :py:class:`NXOpen.Positioning.ConstraintType.Fix <NXOpen.Positioning.ConstraintType>`"
       "Suppressed", "The constraint is suppressed"
       "IgnoredInArrangement", "The current arrangement ignores all constraints"
    """
    Unknown = -1  # ComponentConstraintDirectionToFixedMemberType
    Toward = 0  # ComponentConstraintDirectionToFixedMemberType
    AwayFrom = 1  # ComponentConstraintDirectionToFixedMemberType
    NothingFixed = 2  # ComponentConstraintDirectionToFixedMemberType
    Fix = 3  # ComponentConstraintDirectionToFixedMemberType
    Suppressed = 4  # ComponentConstraintDirectionToFixedMemberType
    IgnoredInArrangement = 5  # ComponentConstraintDirectionToFixedMemberType
    
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
    


class ComponentConstraint(Constraint):
    """
    Constraint for use in positioning assembly objects in NX.  
    
    .. versionadded:: NX5.0.1
    """
    
    class DirectionToFixed():
        """
        Specifies how a constraint affects the positioning of a component.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "No information available"
           "Toward", "Toward fixed geometry"
           "AwayFrom", "Away from fixed geometry"
           "NothingFixed", "The network does not contain any fixed geometry"
           "Fix", "The constraint is a :py:class:`NXOpen.Positioning.ConstraintType.Fix <NXOpen.Positioning.ConstraintType>`"
           "Suppressed", "The constraint is suppressed"
           "IgnoredInArrangement", "The current arrangement ignores all constraints"
        """
        Unknown = -1  # ComponentConstraintDirectionToFixedMemberType
        Toward = 0  # ComponentConstraintDirectionToFixedMemberType
        AwayFrom = 1  # ComponentConstraintDirectionToFixedMemberType
        NothingFixed = 2  # ComponentConstraintDirectionToFixedMemberType
        Fix = 3  # ComponentConstraintDirectionToFixedMemberType
        Suppressed = 4  # ComponentConstraintDirectionToFixedMemberType
        IgnoredInArrangement = 5  # ComponentConstraintDirectionToFixedMemberType
        
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
        
    
    
    def RememberOnComponent(self, component: NXOpen.Assemblies.Component) -> None:
        """
        Remembers the constraint in the prototype part of a referenced component
        for reuse in other occurrences of the part.  
        
        Fix and Bond constraints are
        never remembered.  If the constraint does not reference geometry in the
        component, it is not remembered.
        
        Signature ``RememberOnComponent(component)`` 
        
        :param component:  The :py:class:`NXOpen.Assemblies.Component` on which the constraint is remembered  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
        Get the arrangement specific state of this :py:class:`NXOpen.Positioning.ComponentConstraint` in the 
        specified :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        Signature ``GetSpecificInArrangement(arrangement)`` 
        
        :param arrangement:   The :py:class:`NXOpen.Assemblies.Arrangement` in which the arrangement specific state is being enquired.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:   The arrangement specific state.  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, arrangementSpecific: bool) -> None:
        """
        Set the arrangement specific state of this :py:class:`NXOpen.Positioning.ComponentConstraint` in the 
        specified :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        Signature ``SetSpecificInArrangement(arrangement, arrangementSpecific)`` 
        
        :param arrangement:   The :py:class:`NXOpen.Assemblies.Arrangement` in which the arrangement specific state is being set.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :param arrangementSpecific:   The arrangement specific state.  
        :type arrangementSpecific: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
        Get the suppression state of this :py:class:`NXOpen.Positioning.ComponentConstraint` in the 
        specified :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        If the constraint is not arrangement
        specific in this arrangement then the shared suppression state, used across all 
        arrangements where the constraint is not arrangement specific, is used.
        
        Signature ``GetSuppressedInArrangement(arrangement)`` 
        
        :param arrangement:   The :py:class:`NXOpen.Assemblies.Arrangement` in which the suppression state is being enquired.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:   The suppression state.  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, suppressed: bool) -> None:
        """
        Set the suppression state of this :py:class:`NXOpen.Positioning.ComponentConstraint` in the 
        specified :py:class:`NXOpen.Assemblies.Arrangement`.  
        
        If the constraint is not arrangement
        specific in this arrangement then the shared suppression state, used across all 
        arrangements where the constraint is not arrangement specific, is set.
        
        Signature ``SetSuppressedInArrangement(arrangement, suppressed)`` 
        
        :param arrangement:   The :py:class:`NXOpen.Assemblies.Arrangement` in which the suppression state is being set.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :param suppressed:   The suppression state.  
        :type suppressed: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetSharedSuppressed(self) -> bool:
        """
        Get the shared suppression state of this :py:class:`NXOpen.Positioning.ComponentConstraint` used across all 
        arrangements where the constraint is not arrangement specific.  
        
        Signature ``GetSharedSuppressed()`` 
        
        :returns:   The suppression state.  
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetSharedSuppressed(self, suppressed: bool) -> None:
        """
        Set the shared suppression state of this :py:class:`NXOpen.Positioning.ComponentConstraint` used across all 
        arrangements where the constraint is not arrangement specific.  
        
        Signature ``SetSharedSuppressed(suppressed)`` 
        
        :param suppressed:   The suppression state.  
        :type suppressed: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetInherited(self) -> bool:
        """
        Get whether this :py:class:`NXOpen.Positioning.ComponentConstraint` is 
        an inherited constraint.  
        
        An inherited constraint is created by the system 
        to support Positioning Overrides. 
        
        Signature ``GetInherited()`` 
        
        :returns:  The inherited state of this :py:class:`NXOpen.Positioning.ComponentConstraint`  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDirectionToFixed(self, component: NXOpen.Assemblies.Component, arrangement: NXOpen.Assemblies.Arrangement) -> ComponentConstraintDirectionToFixed:
        """
        Get the :py:class:`NXOpen.Positioning.ComponentConstraintDirectionToFixed` value of the :py:class:`NXOpen.Positioning.ComponentConstraint`
        given a component and an arrangement.  
        
        This value specifies how a constraint affects the positioning of a component.
        If the arrangement is null, the "direction to fixed" value will be evaluated based on the default arrangement.
        
        Signature ``GetDirectionToFixed(component, arrangement)`` 
        
        :param component:  The component constrained to the specified constraint.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        :param arrangement:  The :py:class:`NXOpen.Assemblies.Arrangement` in which the constraint state is being evaluated.  
        :type arrangement: :py:class:`NXOpen.Assemblies.Arrangement` 
        :returns:  The :py:class:`NXOpen.Positioning.ComponentConstraintDirectionToFixed` value.  
        :rtype: :py:class:`NXOpen.Positioning.ComponentConstraintDirectionToFixed` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def CopyToOverride(self) -> None:
        """
        Given an inherited :py:class:`NXOpen.Positioning.ComponentConstraint` created because of Positioning Overrides, create a new constraint copied
        from it in the same part.  
        
        Unlike the inherited :py:class:`NXOpen.Positioning.ComponentConstraint`, the new constraint can be modified by the
        user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
        
        If the constraint is not an inherited constraint, an error is raised.
        
        Signature ``CopyToOverride()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetSeparateSuppression(self) -> bool:
        """
        An inherited :py:class:`NXOpen.Positioning.ComponentConstraint` can be suppressed independently of the constraint it is
        derived from.  
        
        When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
        of the constraint it is derived from.  This method returns true for an inherited constraint in this state.  It does not indicate
        if the constraint is inherited or not: use :py:meth:`NXOpen.Positioning.Constraint.Suppressed` for this.
        
        Given a non-inherited constraint, this will return false.
        
        Signature ``GetSeparateSuppression()`` 
        
        :returns:  The separate suppression state of this :py:class:`NXOpen.Positioning.ComponentConstraint`  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetSeparateSuppression(self, separateSuppression: bool) -> None:
        """
        An inherited :py:class:`NXOpen.Positioning.ComponentConstraint` can be suppressed independently of the constraint it is
        derived from.  
        
        When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
        of the constraint it is derived from.  This method sets this state on an inherited constraint.  Setting this flag will not in
        itself suppress or unsuppress the inherited constraint: use :py:meth:`NXOpen.Positioning.Constraint.Suppressed` for this.
        
        If the constraint is not an inherited constraint, an error is raised.
        
        Signature ``SetSeparateSuppression(separateSuppression)`` 
        
        :param separateSuppression: 
        :type separateSuppression: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    ArrangementSpecific: bool = ...
    """
    Returns or sets 
    the arrangement specific state of this :py:class:`NXOpen.Positioning.ComponentConstraint` in the 
    :py:meth:`NXOpen.Positioning.ComponentPositioner.PrimaryArrangement``.  
    
    Constraints can
    never be arrangement specific in piece parts.
    
    <hr>
    
    Getter Method
    
    Signature ``ArrangementSpecific`` 
    
    :returns:   The arrangement specific state  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ArrangementSpecific`` 
    
    :param arrangementSpecific:   The arrangement specific state  
    :type arrangementSpecific: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ComponentConstraint = ...  # unknown typename


class ConstraintCollection(NXOpen.TaggedObjectCollection):
    """
    a collection of constraints    
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Positioning.Positioner`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    


class ComponentConstraintGroupBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Positioning.ComponentConstraintGroupBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ComponentAssembly.CreateConstraintGroupBuilder`
    
    Default values.
    
    =========================  ==========================
    Property                   Value
    =========================  ==========================
    ConstraintCollectionType   BetweenSelectedComponents 
    -------------------------  --------------------------
    RememberComponentState     true 
    =========================  ==========================
    
    .. versionadded:: NX8.0.1
    """
    
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
        Gets the context component which is used to decide the displayed constraints that can be in the
        selected constraints list.  
        
        The context component is only set by the creator and can be None.
        If the context component is None the displayed constraints will be in same part as the
        constraint group.
        
        Signature ``GetContextComponent()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    ConstraintCollectionType: ComponentConstraintGroupConstraintsCollectionType = ...
    """
    Returns or sets  the constraint collection types 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintCollectionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Positioning.ComponentConstraintGroupConstraintsCollectionType` 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintCollectionType`` 
    
    :param constraintCollectionType: 
    :type constraintCollectionType: :py:class:`NXOpen.Positioning.ComponentConstraintGroupConstraintsCollectionType` 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    ConstraintGroupName: str = ...
    """
    Returns or sets  the name of constraint group 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintGroupName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintGroupName`` 
    
    :param nameOfConstraintGroup: 
    :type nameOfConstraintGroup: str 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    RememberComponentState: bool = ...
    """
    Returns or sets  the toggle to remember selected component 
    
    <hr>
    
    Getter Method
    
    Signature ``RememberComponentState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``RememberComponentState`` 
    
    :param rememberComponentState: 
    :type rememberComponentState: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectedComponentList: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected components list 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedComponentList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SelectedConstraintsList: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the selected constraint list 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedConstraintsList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX8.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ComponentConstraintGroupBuilder = ...  # unknown typename


class ConstraintReferenceGeometryTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintReferenceGeometryType():
    """
    Specifies the type of the geometry used in a :py:class:`NXOpen.Positioning.ConstraintReference`.
    The type reflects that used in a :py:class:`NXOpen.Positioning.Constraint` while it is being
    solved and may be different from that inferred directly from 
    :py:meth:`NXOpen.Positioning.ConstraintReference.GetGeometry`. For example we may use
    :py:class:`NXOpen.Positioning.ConstraintReferenceGeometryType.Line <NXOpen.Positioning.ConstraintReferenceGeometryType>` as an axis when given a cylindrical face as the geometry.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "No geometry suitable for solving"
       "Point", "Point"
       "Line", "Straight line"
       "Circle", "Circle"
       "Plane", "Plane"
       "Cylinder", "Cylinder"
       "Sphere", "Sphere"
       "SweepSurface", "Swept surface"
       "ParametricSurface", "Parametric surface"
       "ParametricCurve", "Parametric curve"
       "SplineCurve", "Spline curve"
       "Torus", "Torus"
       "Cone", "Cone"
       "Ellipse", "Ellipse"
       "SplineSurface", "Spline surface"
       "CoordinateSystem", "Coordinate system"
    """
    Unknown = -1  # ConstraintReferenceGeometryTypeMemberType
    Point = 0  # ConstraintReferenceGeometryTypeMemberType
    Line = 1  # ConstraintReferenceGeometryTypeMemberType
    Circle = 2  # ConstraintReferenceGeometryTypeMemberType
    Plane = 3  # ConstraintReferenceGeometryTypeMemberType
    Cylinder = 4  # ConstraintReferenceGeometryTypeMemberType
    Sphere = 5  # ConstraintReferenceGeometryTypeMemberType
    SweepSurface = 6  # ConstraintReferenceGeometryTypeMemberType
    ParametricSurface = 7  # ConstraintReferenceGeometryTypeMemberType
    ParametricCurve = 8  # ConstraintReferenceGeometryTypeMemberType
    SplineCurve = 9  # ConstraintReferenceGeometryTypeMemberType
    Torus = 10  # ConstraintReferenceGeometryTypeMemberType
    Cone = 11  # ConstraintReferenceGeometryTypeMemberType
    Ellipse = 12  # ConstraintReferenceGeometryTypeMemberType
    SplineSurface = 13  # ConstraintReferenceGeometryTypeMemberType
    CoordinateSystem = 1001  # ConstraintReferenceGeometryTypeMemberType
    
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
    


class ConstraintReferenceConstraintOrderMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintReferenceConstraintOrder():
    """
    Specifies the order of the constraint reference used in a :py:class:`NXOpen.Positioning.Constraint`.
    Typically the order is set during creation, where the first constraint reference added is "outside"
    and the second "outside".
    For Bond constraints, the order is set to be "unknown" at creation.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "No order specified"
       "Inside", "Inside"
       "Outside", "Outside"
    """
    Unknown = 0  # ConstraintReferenceConstraintOrderMemberType
    Inside = 1  # ConstraintReferenceConstraintOrderMemberType
    Outside = 2  # ConstraintReferenceConstraintOrderMemberType
    
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
    


class ConstraintReferenceHalfSpaceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConstraintReferenceHalfSpace():
    """
    Specifies the half space value of one geometry used in a distance constraint.
    This is only used for surface geometries, and it determines which side of the
    surface the distance constraint is measured from.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Infer", "Allow the solver to decide the half space value, or the geometry is not a surface"
       "Positive", "Measure to the positive side of the surface"
       "Negative", "Measure to the negative side of the surface"
    """
    Infer = 0  # ConstraintReferenceHalfSpaceMemberType
    Positive = 1  # ConstraintReferenceHalfSpaceMemberType
    Negative = 2  # ConstraintReferenceHalfSpaceMemberType
    
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
    


class ConstraintReference(NXOpen.NXObject):
    """
    ConstraintReference for use in positioning objects in NX.  
    
    A ConstraintReference is used by a Constraint to determine 
    the movable object to be positioned by the constraint and
    the geometry used to define the constraint.
    
    To create an instance of this class, use :py:meth:`NXOpen.Positioning.Constraint.CreateConstraintReference`.
    
    .. versionadded:: NX4.0.0
    """
    
    class GeometryType():
        """
        Specifies the type of the geometry used in a :py:class:`NXOpen.Positioning.ConstraintReference`.
        The type reflects that used in a :py:class:`NXOpen.Positioning.Constraint` while it is being
        solved and may be different from that inferred directly from 
        :py:meth:`NXOpen.Positioning.ConstraintReference.GetGeometry`. For example we may use
        :py:class:`NXOpen.Positioning.ConstraintReferenceGeometryType.Line <NXOpen.Positioning.ConstraintReferenceGeometryType>` as an axis when given a cylindrical face as the geometry.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "No geometry suitable for solving"
           "Point", "Point"
           "Line", "Straight line"
           "Circle", "Circle"
           "Plane", "Plane"
           "Cylinder", "Cylinder"
           "Sphere", "Sphere"
           "SweepSurface", "Swept surface"
           "ParametricSurface", "Parametric surface"
           "ParametricCurve", "Parametric curve"
           "SplineCurve", "Spline curve"
           "Torus", "Torus"
           "Cone", "Cone"
           "Ellipse", "Ellipse"
           "SplineSurface", "Spline surface"
           "CoordinateSystem", "Coordinate system"
        """
        Unknown = -1  # ConstraintReferenceGeometryTypeMemberType
        Point = 0  # ConstraintReferenceGeometryTypeMemberType
        Line = 1  # ConstraintReferenceGeometryTypeMemberType
        Circle = 2  # ConstraintReferenceGeometryTypeMemberType
        Plane = 3  # ConstraintReferenceGeometryTypeMemberType
        Cylinder = 4  # ConstraintReferenceGeometryTypeMemberType
        Sphere = 5  # ConstraintReferenceGeometryTypeMemberType
        SweepSurface = 6  # ConstraintReferenceGeometryTypeMemberType
        ParametricSurface = 7  # ConstraintReferenceGeometryTypeMemberType
        ParametricCurve = 8  # ConstraintReferenceGeometryTypeMemberType
        SplineCurve = 9  # ConstraintReferenceGeometryTypeMemberType
        Torus = 10  # ConstraintReferenceGeometryTypeMemberType
        Cone = 11  # ConstraintReferenceGeometryTypeMemberType
        Ellipse = 12  # ConstraintReferenceGeometryTypeMemberType
        SplineSurface = 13  # ConstraintReferenceGeometryTypeMemberType
        CoordinateSystem = 1001  # ConstraintReferenceGeometryTypeMemberType
        
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
        
    
    
    class ConstraintOrder():
        """
        Specifies the order of the constraint reference used in a :py:class:`NXOpen.Positioning.Constraint`.
        Typically the order is set during creation, where the first constraint reference added is "outside"
        and the second "outside".
        For Bond constraints, the order is set to be "unknown" at creation.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "No order specified"
           "Inside", "Inside"
           "Outside", "Outside"
        """
        Unknown = 0  # ConstraintReferenceConstraintOrderMemberType
        Inside = 1  # ConstraintReferenceConstraintOrderMemberType
        Outside = 2  # ConstraintReferenceConstraintOrderMemberType
        
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
        
    
    
    class HalfSpace():
        """
        Specifies the half space value of one geometry used in a distance constraint.
        This is only used for surface geometries, and it determines which side of the
        surface the distance constraint is measured from.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Infer", "Allow the solver to decide the half space value, or the geometry is not a surface"
           "Positive", "Measure to the positive side of the surface"
           "Negative", "Measure to the negative side of the surface"
        """
        Infer = 0  # ConstraintReferenceHalfSpaceMemberType
        Positive = 1  # ConstraintReferenceHalfSpaceMemberType
        Negative = 2  # ConstraintReferenceHalfSpaceMemberType
        
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
        
    
    
    def GetGeometry(self) -> NXOpen.NXObject:
        """
        Returns the geometry of the constraint reference.  
        
        This is the 
        geometry used in any :py:class:`NXOpen.Positioning.Constraint` using
        this constraint reference.
        
        Signature ``GetGeometry()`` 
        
        :returns:  The geometry referenced by the constraint  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPrototypeGeometry(self) -> NXOpen.NXObject:
        """
        Returns the prototype geometry of the constraint reference.  
        
        This is never an occurrence.
        
        Signature ``GetPrototypeGeometry()`` 
        
        :returns:  The prototype geometry referenced by the constraint  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetMovableObject(self) -> NXOpen.NXObject:
        """
        Returns the movable object of the constraint reference.  
        
        The movable object determines the object to be 
        positioned by any :py:class:`NXOpen.Positioning.Constraint` using
        this constraint reference.
        
        Signature ``GetMovableObject()`` 
        
        :returns:  The object positioned by the constraint  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetUsesGeometryAxis(self) -> bool:
        """
        Returns if the constraint reference should use the axis of the
        geometry (for example a cylindrical face) rather than the surface
        
        Signature ``GetUsesGeometryAxis()`` 
        
        :returns:  If this reference is using the axis of the geometry  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetFixHint(self, set: bool) -> None:
        """
        Set a hint to the solver to fix the movable object associated
        with this constraint reference.  
        
        The hint is unset when "set" is false.
        
        The hint can only have an effect when the constraint owning this
        constraint reference has been explicitly added to 
        a :py:class:`NXOpen.Positioning.Network`.
        
        The hint is forgotten after an update.
        
        Signature ``SetFixHint(set)`` 
        
        :param set:  Set or unset the hint  
        :type set: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetFixHintForUpdate(self, set: bool) -> None:
        """
        Set a hint to the solver to fix the movable object associated
        with this constraint reference.  
        
        The hint is unset when "set" is false.
        
        The hint is forgotten after an update.
        
        Ensures that the constraint that owns this reference will
        solve during the next call to :py:meth:`NXOpen.Update.DoUpdate`.
        
        Signature ``SetFixHintForUpdate(set)`` 
        
        :param set:  Set or unset the hint  
        :type set: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetUsePortRotate(self) -> bool:
        """
        Get the flag forcing the use of the rotation vector of the 
        referenced :py:class:`NXOpen.Routing.Port` object instead of the alignment vector 
        when solving the constraint system.  
        
        Only effective when the referenced geometry is a :py:class:`NXOpen.Routing.Port`
        object.
        
        Signature ``GetUsePortRotate()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetHasPerpendicularVector(self) -> bool:
        """
        Get the flag indicating whether the constraint reference is one that maintains a direction
        perpendicular to the primary geometry.  
        
        This is only applicable to :py:class:`NXOpen.Positioning.ConstraintType` 
        :py:class:`NXOpen.Positioning.ConstraintType.AlignLock <NXOpen.Positioning.ConstraintType>`.
        
        Signature ``GetHasPerpendicularVector()`` 
        
        :returns:  Whether the constraint has a perpendicular vector  
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetPrototypePerpendicularVector(self) -> NXOpen.Vector3d:
        """
        Get the value of the perpendicular vector, which will be (0,0,0)
        for most constraints apart from :py:class:`NXOpen.Positioning.ConstraintType.AlignLock <NXOpen.Positioning.ConstraintType>`.  
        
        Signature ``GetPrototypePerpendicularVector()`` 
        
        :returns:  The value of the perpendicular vector  
        :rtype: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetPrototypePerpendicularVector(self, perpendicularVector: NXOpen.Vector3d) -> None:
        """
        Set the value of the perpendicular vector.  
        
        The value must be a unit vector given in the coordinates
        of the part containing the referenced geometry.
        
        The perpendicular vector must be set to (0,0,0) for most constraints apart 
        from :py:class:`NXOpen.Positioning.ConstraintType.AlignLock <NXOpen.Positioning.ConstraintType>` which 
        must have a value. An error is raised if this is not the case.
        
        Whenever the constraint is solved, the value of the perpendicular vector may be modified,
        to ensure that the vector is perpendicular to the referenced geometry. 
        
        Signature ``SetPrototypePerpendicularVector(perpendicularVector)`` 
        
        :param perpendicularVector:  The value of the perpendicular vector  
        :type perpendicularVector: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    ConstraintReferenceHalfSpace: ConstraintReferenceHalfSpace = ...
    """
    Returns or sets  
    the half_space value for the constraint reference.  
    
    This is only used for distance constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintReferenceHalfSpace`` 
    
    :returns:  Half space for constraint reference  
    :rtype: :py:class:`NXOpen.Positioning.ConstraintReferenceHalfSpace` 
    
    .. versionadded:: NX5.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintReferenceHalfSpace`` 
    
    :param halfSpace:  Half space for constraint reference  
    :type halfSpace: :py:class:`NXOpen.Positioning.ConstraintReferenceHalfSpace` 
    
    .. versionadded:: NX5.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    GeometryDirectionReversed: bool = ...
    """
    Returns or sets 
    whether the direction is reversed with respect to the direction of the geometry.  
    
    This property is only used if the underlying geometry can have an associated direction.
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryDirectionReversed`` 
    
    :returns:  Whether the direction is reversed with respect to the geometry  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryDirectionReversed`` 
    
    :param geometryDirectionReversed:  Whether the direction is reversed with respect to the geometry  
    :type geometryDirectionReversed: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    HelpPoint: NXOpen.Point3d = ...
    """
    Returns or sets  
    the help point of the constraint reference.  
    
    <hr>
    
    Getter Method
    
    Signature ``HelpPoint`` 
    
    :returns:  Coordinates of point in part of constraint  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``HelpPoint`` 
    
    :param helpPoint:  Coordinates of point in part of constraint  
    :type helpPoint: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Order: ConstraintReferenceConstraintOrder = ...
    """
    Returns  
    the order of the constraint reference within its constraint.  
    
    Note that
    this order is not associated with the geometry or with the alignment 
    of the constraint.  It is based on the idea that the constraint has a direction
    from "outside" to "inside".  It does not affect the result of a solve.
    
    <hr>
    
    Getter Method
    
    Signature ``Order`` 
    
    :returns:  The order  
    :rtype: :py:class:`NXOpen.Positioning.ConstraintReferenceConstraintOrder` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    SolverGeometryType: ConstraintReferenceGeometryType = ...
    """
    Returns  
    the geometry type of the constraint reference used during a solve.  
    
    <hr>
    
    Getter Method
    
    Signature ``SolverGeometryType`` 
    
    :returns:  The geometry type  
    :rtype: :py:class:`NXOpen.Positioning.ConstraintReferenceGeometryType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    UsePortRotateFlag: bool = ...
    """
    Returns or sets 
    the flag forcing the use of the rotation vector of the 
    referenced :py:class:`NXOpen.Routing.Port` object instead of the alignment vector 
    when solving the constraint system.  
    
    Only effective when the referenced geometry is a :py:class:`NXOpen.Routing.Port`
    object.
    
    <hr>
    
    Getter Method
    
    Signature ``UsePortRotateFlag`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``UsePortRotateFlag`` 
    
    :param useRotate: 
    :type useRotate: bool 
    
    .. versionadded:: NX5.0.1
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: ConstraintReference = ...  # unknown typename


class ComponentConstraintGroupConstraintsCollectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComponentConstraintGroupConstraintsCollectionType():
    """
    the enum to define constraint collection type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BetweenSelectedComponents", " - "
       "ConnectedToSelectedComponents", " - "
    """
    BetweenSelectedComponents = 0  # ComponentConstraintGroupConstraintsCollectionTypeMemberType
    ConnectedToSelectedComponents = 1  # ComponentConstraintGroupConstraintsCollectionTypeMemberType
    
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
    


class ComponentConstraintGroup(NXOpen.NXObject):
    """
    Constraint group which represents a group of component constraints in NX.  
    
    .. versionadded:: NX8.0.1
    """
    
    class ConstraintsCollectionType():
        """
        the enum to define constraint collection type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BetweenSelectedComponents", " - "
           "ConnectedToSelectedComponents", " - "
        """
        BetweenSelectedComponents = 0  # ComponentConstraintGroupConstraintsCollectionTypeMemberType
        ConnectedToSelectedComponents = 1  # ComponentConstraintGroupConstraintsCollectionTypeMemberType
        
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
        
    
    
    def GetMemberConstraints(self) -> 'list[ComponentConstraint]':
        """
        Returns the member constraints present in the group.  
        
        The member constraints are generated from the defining
        constraints and components. This attribute cannot be set directly.
        
        Signature ``GetMemberConstraints()`` 
        
        :returns:  Member constraints  
        :rtype: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDefiningConstraints(self) -> 'list[ComponentConstraint]':
        """
        Returns the defining constraints within the group.  
        
        Signature ``GetDefiningConstraints()`` 
        
        :returns:  Defining constraints  
        :rtype: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetDefiningConstraints(self, constraints: 'list[ComponentConstraint]') -> None:
        """
        Sets the defining constraints within the group.  
        
        Signature ``SetDefiningConstraints(constraints)`` 
        
        :param constraints:  Defining constraints  
        :type constraints: list of :py:class:`NXOpen.Positioning.ComponentConstraint` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetDefiningComponents(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Returns the defining components within the group.  
        
        Signature ``GetDefiningComponents()`` 
        
        :returns:  Defining components  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetDefiningComponents(self, constraints: 'list[NXOpen.Assemblies.Component]') -> None:
        """
        Sets the defining constraints within the group.  
        
        Signature ``SetDefiningComponents(constraints)`` 
        
        :param constraints:  Defining components  
        :type constraints: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetConstraintCollectionType(self) -> ComponentConstraintGroupConstraintsCollectionType:
        """
        Gets the type of constraint collection that is performed using the defining components.  
        
        Signature ``GetConstraintCollectionType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Positioning.ComponentConstraintGroupConstraintsCollectionType` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetConstraintCollectionType(self, constraintCollectionType: ComponentConstraintGroupConstraintsCollectionType) -> None:
        """
        Sets the type of constraint collection that is performed using the defining components.  
        
        Signature ``SetConstraintCollectionType(constraintCollectionType)`` 
        
        :param constraintCollectionType: 
        :type constraintCollectionType: :py:class:`NXOpen.Positioning.ComponentConstraintGroupConstraintsCollectionType` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetRememberComponentState(self) -> bool:
        """
        Gets the state which indicates if defining components are remembered when updating the member constraints.  
        
        Signature ``GetRememberComponentState()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def SetRememberComponentState(self, rememberComponentState: bool) -> None:
        """
        Sets the state which indicates if defining components are remembered when updating the member constraints.  
        
        Signature ``SetRememberComponentState(rememberComponentState)`` 
        
        :param rememberComponentState: 
        :type rememberComponentState: bool 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def UpdateMemberConstraints(self) -> bool:
        """
        Updates the member constraints so that they match the definition implied by the defining constraints,
        defining components and associated constraint collection type.  
        
        Signature ``UpdateMemberConstraints()`` 
        
        :returns:  True if the member constraints have been changed by update  
        :rtype: bool 
        
        .. versionadded:: NX8.0.1
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: ComponentConstraintGroup = ...  # unknown typename


class MatingConverterPartContextMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MatingConverterPartContext():
    """
    Defines in which parts mating conditions will be converted.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InOwningPart", "Convert mating conditions in the owning part"
       "InLoadedChildren", "Convert mating conditions in the owning part and all loaded children. Partially-loaded children will be fully-loaded."
       "InAllChildren", "Convert mating conditions in the owning part and all children. Partially-loaded and unloaded children will be fully-loaded."
    """
    InOwningPart = 0  # MatingConverterPartContextMemberType
    InLoadedChildren = 1  # MatingConverterPartContextMemberType
    InAllChildren = 2  # MatingConverterPartContextMemberType
    
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
    


class MatingConverter(NXOpen.TaggedObject):
    """
    An instance of this class can be used to convert Mating Conditions
    to Assembly Constraints in its owning assembly or in child parts
    of its owning assembly.  
    
    The owning assembly is the
    :py:class:`NXOpen.Assemblies.ComponentAssembly` from which this
    object was obtained using
    :py:meth:`NXOpen.Assemblies.ComponentAssembly.CreateMatingConverter`.
    
    Not directly created by user.
    
    .. versionadded:: NX5.0.0
    """
    
    class PartContext():
        """
        Defines in which parts mating conditions will be converted.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InOwningPart", "Convert mating conditions in the owning part"
           "InLoadedChildren", "Convert mating conditions in the owning part and all loaded children. Partially-loaded children will be fully-loaded."
           "InAllChildren", "Convert mating conditions in the owning part and all children. Partially-loaded and unloaded children will be fully-loaded."
        """
        InOwningPart = 0  # MatingConverterPartContextMemberType
        InLoadedChildren = 1  # MatingConverterPartContextMemberType
        InAllChildren = 2  # MatingConverterPartContextMemberType
        
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
        
    
    
    def ConvertMatingConditions(self) -> None:
        """
        Converts Mating Conditions to Assembly Constraints according to the
        properties defined on this :py:class:`NXOpen.Positioning.MatingConverter`
        object.  
        
        Signature ``ConvertMatingConditions()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetConvertedConstraints(self) -> 'list[Constraint]':
        """
        Returns all constraints converted by this conversion operation.  
        
        Use :py:meth:`NXOpen.Positioning.Constraint.GenerateConversionReport`
        to obtain the conversion status of these constraints.
        
        Signature ``GetConvertedConstraints()`` 
        
        :returns:  The converted constraints  
        :rtype: list of :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetConvertedParts(self) -> 'list[Constraint]':
        """
        Returns all parts converted by this conversion operation.  
        
        Signature ``GetConvertedParts()`` 
        
        :returns:  The converted constraints  
        :rtype: list of :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetLatestResults(self, showAllResults: bool) -> 'list[str]':
        """
        Returns textual descriptions of the results of the last conversion operation
        
        Signature ``GetLatestResults(showAllResults)`` 
        
        :param showAllResults:  Whether to show results for all converted constraints even if no issues arose during their conversion  
        :type showAllResults: bool 
        :returns:  The generated results  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetResults(self, showAllResults: bool) -> 'list[str]':
        """
        Returns textual descriptions of the results of all prior conversion
        operations for all the parts described by the current context set using
        :py:meth:`NXOpen.Positioning.MatingConverter.Context`.  
        
        Signature ``GetResults(showAllResults)`` 
        
        :param showAllResults:  Whether to show results for all converted constraints even if no issues arose during their conversion  
        :type showAllResults: bool 
        :returns:  The generated results  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def DeleteResults(self) -> None:
        """
        Removes details from the mating conversion results of the individual constraints that were converted.  
        
        This will be applied to the mating conversion results in the parts described by the current context
        (determined by :py:meth:`NXOpen.Positioning.MatingConverter.Context`). Note that the
        summary information for each part in the conversion results is not modified by this function.
        
        Signature ``DeleteResults()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Destroy(self) -> None:
        """
        Deletes this :py:class:`NXOpen.Positioning.MatingConverter` immediately.  
        
        Signature ``Destroy()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Context: MatingConverterPartContext = ...
    """
    Returns or sets 
    the current conversion context in which mating conditions will be converted.  
    
    <hr>
    
    Getter Method
    
    Signature ``Context`` 
    
    :returns:  The current context  
    :rtype: :py:class:`NXOpen.Positioning.MatingConverterPartContext` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``Context`` 
    
    :param context:  The new context  
    :type context: :py:class:`NXOpen.Positioning.MatingConverterPartContext` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LoadReferencedGeometry: bool = ...
    """
    Returns or sets 
    whether to load unloaded referenced geometry before performing a conversion.  
    
    When all referenced geometry is loaded the conversion operation is more
    effective. If it isn't loaded, then the conversion operation will often
    need to be completed next time the assembly and geometry are loaded
    together.
    
    <hr>
    
    Getter Method
    
    Signature ``LoadReferencedGeometry`` 
    
    :returns:  Whether referenced-geometry will be loaded  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    
    <hr>
    
    Setter Method
    
    Signature ``LoadReferencedGeometry`` 
    
    :param loadGeometry:  Whether to load referenced-geometry  
    :type loadGeometry: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    LoadStatus: NXOpen.PartLoadStatus = ...
    """
    Returns 
    the load status resulting from a conversion operation.  
    
    This indicates
    any problems which arose when loading parts during conversion.
    
    <hr>
    
    Getter Method
    
    Signature ``LoadStatus`` 
    
    :returns:  Parts that could not be loaded
    and their associated errors.  
    :rtype: :py:class:`NXOpen.PartLoadStatus` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    NumberOfConvertedParts: int = ...
    """
    Returns 
    the number of parts parts converted by this conversion operation.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfConvertedParts`` 
    
    :returns:  The number of converted parts  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: assemblies ("ASSEMBLIES MODULE")
    """
    Null: MatingConverter = ...  # unknown typename


class DisplayedConstraint(NXOpen.DisplayableObject):
    """
    The displayed representation of a constraint, used for graphical
    display and to represent it in the Assembly Navigator.  
    
    Instances of :py:class:`NXOpen.Positioning.DisplayedConstraint` are created whenever a
    :py:class:`NXOpen.Positioning.Constraint` is created.
    
    A :py:class:`NXOpen.Positioning.Constraint` has an instance of :py:class:`NXOpen.Positioning.DisplayedConstraint`
    in the same part as itself, but an instance of :py:class:`NXOpen.Positioning.DisplayedConstraint` doesn't
    necessarily exist in the same part as the underlying :py:class:`NXOpen.Positioning.Constraint`.
    
    An instance of this class can be obtained from :py:meth:`NXOpen.Positioning.Constraint.GetDisplayedConstraint`.
    
    .. versionadded:: NX7.5.0
    """
    
    def GetConstraint(self) -> Constraint:
        """
        Get the underlying :py:class:`NXOpen.Positioning.Constraint`.  
        
        Note that this will be None if the underlying :py:class:`NXOpen.Positioning.Constraint` is unloaded.
        
        Signature ``GetConstraint()`` 
        
        :returns:  The underlying constraint  
        :rtype: :py:class:`NXOpen.Positioning.Constraint` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetConstraintPart(self) -> NXOpen.Part:
        """
        Get the part containing the underlying :py:class:`NXOpen.Positioning.Constraint`.  
        
        Note that this will be None if the underlying :py:class:`NXOpen.Positioning.Constraint` is unloaded.
        
        Signature ``GetConstraintPart()`` 
        
        :returns:  The part containing the underlying constraint  
        :rtype: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
        Get the component containing the underlying :py:class:`NXOpen.Positioning.Constraint`.  
        
        Note that this will be None if the underlying :py:class:`NXOpen.Positioning.Constraint` is in the
        same part as the displayed constraint.
        
        Signature ``GetContextComponent()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: DisplayedConstraint = ...  # unknown typename


