# module 'NXOpen.CAE.QualityAudit'
#
# Automatically generated 2025-06-09T14:38:44.605509
#

import typing

import NXOpen
import NXOpen.CAE
import NXOpen.CAE.Connections



class ActionIdMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ActionId():
    """
    Action ids. Each action can be identified through an unique id. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ListAllConnections", "the action that lists all connections. Available in the global actions"
       "ListNonModeledConnections", "the action that list all non modeled connections. Available in the global actions"
       "CheckComponentConnectivity", "the action analyzing component connectivity. Available in the global actions"
       "CheckComponentSynthesis", "the action listing components and their direct connections. Available in the global actions"
       "CheckDiameterRange", "the action checking diameter bounds. Available in the connection related actions"
       "ObjectLevelCheckProjection", "the action listing projection errors at object level. Available in the connection related actions"
       "MeshLevelCheckProjection", "the action listing projection errors at mesh level. Available in the connection related actions"
       "CheckDistanceBetweenConnectionPoints", "the action verifying distance between the points of the same connection. Available in the connection related actions"
       "CheckDistanceBetweenConnections", "the action checking the distance between connections. Available in the connection related actions"
       "CheckFreeEdgeDistance", "the action checking for near edge connections. Available in the connection related actions"
       "CheckTargetSequence", "the action verifying the support order. Available in the connection related actions"
    """
    ListAllConnections = 0  # ActionIdMemberType
    ListNonModeledConnections = 1  # ActionIdMemberType
    CheckComponentConnectivity = 2  # ActionIdMemberType
    CheckComponentSynthesis = 3  # ActionIdMemberType
    CheckDiameterRange = 4  # ActionIdMemberType
    ObjectLevelCheckProjection = 5  # ActionIdMemberType
    MeshLevelCheckProjection = 6  # ActionIdMemberType
    CheckDistanceBetweenConnectionPoints = 7  # ActionIdMemberType
    CheckDistanceBetweenConnections = 8  # ActionIdMemberType
    CheckFreeEdgeDistance = 9  # ActionIdMemberType
    CheckTargetSequence = 10  # ActionIdMemberType
    
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
    


class Action(NXOpen.NXObject):
    """
    The Quality Audit Action is a base class that performs actions on a list of objects. Results of the action are also stored here. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    
    class Id():
        """
        Action ids. Each action can be identified through an unique id. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ListAllConnections", "the action that lists all connections. Available in the global actions"
           "ListNonModeledConnections", "the action that list all non modeled connections. Available in the global actions"
           "CheckComponentConnectivity", "the action analyzing component connectivity. Available in the global actions"
           "CheckComponentSynthesis", "the action listing components and their direct connections. Available in the global actions"
           "CheckDiameterRange", "the action checking diameter bounds. Available in the connection related actions"
           "ObjectLevelCheckProjection", "the action listing projection errors at object level. Available in the connection related actions"
           "MeshLevelCheckProjection", "the action listing projection errors at mesh level. Available in the connection related actions"
           "CheckDistanceBetweenConnectionPoints", "the action verifying distance between the points of the same connection. Available in the connection related actions"
           "CheckDistanceBetweenConnections", "the action checking the distance between connections. Available in the connection related actions"
           "CheckFreeEdgeDistance", "the action checking for near edge connections. Available in the connection related actions"
           "CheckTargetSequence", "the action verifying the support order. Available in the connection related actions"
        """
        ListAllConnections = 0  # ActionIdMemberType
        ListNonModeledConnections = 1  # ActionIdMemberType
        CheckComponentConnectivity = 2  # ActionIdMemberType
        CheckComponentSynthesis = 3  # ActionIdMemberType
        CheckDiameterRange = 4  # ActionIdMemberType
        ObjectLevelCheckProjection = 5  # ActionIdMemberType
        MeshLevelCheckProjection = 6  # ActionIdMemberType
        CheckDistanceBetweenConnectionPoints = 7  # ActionIdMemberType
        CheckDistanceBetweenConnections = 8  # ActionIdMemberType
        CheckFreeEdgeDistance = 9  # ActionIdMemberType
        CheckTargetSequence = 10  # ActionIdMemberType
        
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
        
    
    
    def Perform(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Performs the action on the given object list.  
        
        Signature ``Perform(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetResults(self) -> 'list[Result]':
        """
        Get the :py:class:`CAE.QualityAudit.Result` list obtained from the latest check
        
        Signature ``GetResults()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.QualityAudit.Result` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Description: str = ...
    """
    Returns  the action description
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns:  The description of the action  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Settings: ActionSettings = ...
    """
    Returns  the action settings
    
    <hr>
    
    Getter Method
    
    Signature ``Settings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.ActionSettings` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Action = ...  # unknown typename


class ComponentSynthesis(Action):
    """
    This action has as result a list of components and the connections using them. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ComponentSynthesis = ...  # unknown typename


class Result(NXOpen.NXObject):
    """
    The Quality Audit Result class offers means to access information about specific problems found while performing specific quality audit checks. 
    
    Results can be obtained from :py:class:`CAE.QualityAudit.Action` after checks have been performed via :py:meth:`NXOpen.CAE.QualityAudit.Action.GetResults`.
    
    .. versionadded:: NX12.0.0
    """
    Description: str = ...
    """
    Returns  the text description of this result  
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns:  The description of the action  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    OwningAction: Action = ...
    """
    Returns  the owning action that provides this result 
    
    <hr>
    
    Getter Method
    
    Signature ``OwningAction`` 
    
    :returns:  Action that created this result  
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.Action` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Result = ...  # unknown typename


class ConnectionDistanceResult(Result):
    """
    The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection distance checks on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ConnectionDistanceCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ConnectionDistanceResult = ...  # unknown typename


class ConnectionPointsDistanceCheck(Action):
    """
    This action checks the distance between connection's definition points. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ConnectionPointsDistanceCheck = ...  # unknown typename


class MeshLevelFailedElementCreationResult(Result):
    """
    The Quality Audit MeshLevelFailedElementCreationResult is a class containing information about failed element creations on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.MeshLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the failed element creation 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with failed mesh element creation  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the failing element creation in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the failing element creation.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the failing element creation.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the failing element creation.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: MeshLevelFailedElementCreationResult = ...  # unknown typename


class ListNonModeledConnections(Action):
    """
    This action's output is a list of connections that are not realized. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ListNonModeledConnections = ...  # unknown typename


class FreeEdgeDistanceResult(Result):
    """
    The Quality Audit FreeEdgeDistanceResult contains information about problematic places where distance between connection points and free edges is less than a given value. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.FreeEdgeDistanceCheck`.
    
    .. versionadded:: NX12.0.0
    """
    CaeEdge: NXOpen.CAE.CAEEdge = ...
    """
    Returns  the CAE edge (if present).  
    
    <hr>
    
    Getter Method
    
    Signature ``CaeEdge`` 
    
    :returns:  The CAE Edge if it has one  
    :rtype: :py:class:`NXOpen.CAE.CAEEdge` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with points close to the edge 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with points close to the edge  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the close to the edge point in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the point close to edge.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    EdgePoint: NXOpen.Point3d = ...
    """
    Returns  the edge point.  
    
    <hr>
    
    Getter Method
    
    Signature ``EdgePoint`` 
    
    :returns:  Closest point on edge in ABS coordinates  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FeElementEdge: NXOpen.CAE.FEElemEdge = ...
    """
    Returns  the FE edge (if present).  
    
    <hr>
    
    Getter Method
    
    Signature ``FeElementEdge`` 
    
    :returns:  The FE Edge if it has one  
    :rtype: :py:class:`NXOpen.CAE.FEElemEdge` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the close to the edge point.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the point close to edge.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: FreeEdgeDistanceResult = ...  # unknown typename


class ConnectionPointsDistanceResult(Result):
    """
    The Quality Audit ConnectionPointsDistanceResult is a class containing information about failed distance between connection points checks on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ConnectionPointsDistanceCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with points that are too close to each other  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex1: int = ...
    """
    Returns  the coordinate index of the first point in the first location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex1`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex2: int = ...
    """
    Returns  the coordinate index of the second point in the second location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex2`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex1: int = ...
    """
    Returns  the definition index of the first point.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex1`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex2: int = ...
    """
    Returns  the definition index of the second point.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex2`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex1: int = ...
    """
    Returns  the location index of the first point.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex1`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex2: int = ...
    """
    Returns  the location index of the second point.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex2`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ConnectionPointsDistanceResult = ...  # unknown typename


class SupportSequenceCheck(Action):
    """
    This action's output is the list of connections having more than 2 supports with wrong order (e.g. first support between the second and third). 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: SupportSequenceCheck = ...  # unknown typename


class ObjectLevelFailedProjectionToleranceResult(Result):
    """
    The Quality Audit ObjectLevelFailedProjectionToleranceResult is a class containing information about projections 
    that failed the tolerance criteria although the projection itself was successful. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ObjectLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the failed tolerance projection 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with failed tolerance projection  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the tolerance failing projection in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the tolerance failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the tolerance failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the tolerance failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ObjectLevelFailedProjectionToleranceResult = ...  # unknown typename


class ActionSettings(NXOpen.NXObject):
    """
    The Quality Audit ActionSettings is the base class for :py:class:`NXOpen.CAE.QualityAudit.Action` settings. It provides basic functionality. 
    
    Settings instances can be obtained via :py:meth:`NXOpen.CAE.QualityAudit.Action.Settings``.
    
    .. versionadded:: NX12.0.0
    """
    
    def ResetToDefaults(self) -> None:
        """
        Reset the action settings to default values 
        
        Signature ``ResetToDefaults()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    Action: Action = ...
    """
    Returns  the action using these settings 
    
    <hr>
    
    Getter Method
    
    Signature ``Action`` 
    
    :returns:  Action using these settings  
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.Action` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ActionSettings = ...  # unknown typename


class ProjectionCheckSettings(ActionSettings):
    """
    This class contains settings used by the projection checks. 
    
    To obtain an instance of this class see :py:class:`CAE.QualityAudit.MeshLevelProjectionCheck` or :py:class:`CAE.QualityAudit.ObjectLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Threshold: NXOpen.Expression = ...
    """
    Returns  the threshold distance from definition point to projection point.  
    
    Once this is surpassed an error is reported 
    
    <hr>
    
    Getter Method
    
    Signature ``Threshold`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ProjectionCheckSettings = ...  # unknown typename


class ObjectLevelProjectionCheck(Action):
    """
    This action has as output the list of failed projections of the universal connections at object level. 
    
    To obtain this action see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ObjectLevelProjectionCheck = ...  # unknown typename


class ManagerActionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ManagerActionType():
    """
    Action type to be used in the quality audit process. Based on this action type the input and action list changes. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Global", "Global action types"
       "Connection", "Connection related actions"
    """
    Global = 0  # ManagerActionTypeMemberType
    Connection = 1  # ManagerActionTypeMemberType
    
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
    


class Manager():
    """
    The Quality Audit Manager class offers means to check for errors at assembly level  
    
    To obtain an instance of this class use :py:meth:`NXOpen.CAE.CaeSession.QualityAuditManager`.
    
    .. versionadded:: NX12.0.0
    """
    
    class ActionType():
        """
        Action type to be used in the quality audit process. Based on this action type the input and action list changes. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Global", "Global action types"
           "Connection", "Connection related actions"
        """
        Global = 0  # ManagerActionTypeMemberType
        Connection = 1  # ManagerActionTypeMemberType
        
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
        
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
        Finds the :py:class:`NXOpen.INXObject` with the given identifier as recorded in a journal.  
        
        An object may not return the same value as its JournalIdentifier in different versions of 
        the software. However newer versions of the software should find the same object when 
        FindObject is passed older versions of its journal identifier. In general, this method 
        should not be used in handwritten code and exists to support record and playback of journals.
        
        An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns:  An object matching the journal identifier  
        :rtype: :py:class:`NXOpen.INXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PerformActions(self, inputActions: 'list[Action]', pObjects: 'list[NXOpen.NXObject]') -> None:
        """
        This method performs checks on the selected objects.  
        
        Signature ``PerformActions(inputActions, pObjects)`` 
        
        :param inputActions:  The :py:class:`CAE.QualityAudit.Action` array of actions to be performed.  
        :type inputActions: list of :py:class:`NXOpen.CAE.QualityAudit.Action` 
        :param pObjects:  The objects to be used by the actions.  
        :type pObjects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    ActionList: ActionList = ...
    """
    Returns  the quality audit action list.  
    
    <hr>
    
    Getter Method
    
    Signature ``ActionList`` 
    
    :returns:  Action list of the quality audit manager  
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.ActionList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CurrentActionType: ManagerActionType = ...
    """
    Returns or sets  the current quality audit action type.  
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentActionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.ManagerActionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurrentActionType`` 
    
    :param actionType: 
    :type actionType: :py:class:`NXOpen.CAE.QualityAudit.ManagerActionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    InputList: InputList = ...
    """
    Returns  the quality audit input list.  
    
    <hr>
    
    Getter Method
    
    Signature ``InputList`` 
    
    :returns:  Input list of the quality audit manager  
    :rtype: :py:class:`NXOpen.CAE.QualityAudit.InputList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """


class MeshLevelFailedProjectionToleranceResult(Result):
    """
    The Quality Audit MeshLevelFailedProjectionToleranceResult is a class containing information about mesh projections 
    that failed the tolerance criteria. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.MeshLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the failed mesh tolerance projection
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with failed mesh tolerance projection  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the tolerance failing mesh projection in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the tolerance failing mesh projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the tolerance failing mesh projection.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the tolerance failing mesh projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    OffendingDistance: float = ...
    """
    Returns  the offending distance of the failing mesh projection.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffendingDistance`` 
    
    :returns:  The offending distance  
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: MeshLevelFailedProjectionToleranceResult = ...  # unknown typename


class MergedNodesResult(Result):
    """
    The Quality Audit MergedNodesResult is a class containing information about nodes connecting components. They are obtained by the :py:class:`NXOpen.CAE.QualityAudit.ListConnections` action. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ListConnections`.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Returns the merged nodes.  
        
        Signature ``GetNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: MergedNodesResult = ...  # unknown typename


class InputList(NXOpen.NXObject):
    """
    The Quality Audit InputList class offers means to select, deselect, obtain the objects to be used by :py:class:`CAE.QualityAudit.Action` instances. 
    
    To obtain the instance of this class use :py:meth:`CAE.QualityAudit.Manager.InputList`.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetAllObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Return all the objects available as input for the quality audit actions.  
        
        Signature ``GetAllObjects()`` 
        
        :returns:  Array of selected objects  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SelectAll(self) -> None:
        """
        Select all input from the :py:class:`CAE.QualityAudit.InputList`.  
        
        Signature ``SelectAll()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DeselectAll(self) -> None:
        """
        Deselect all input from the :py:class:`CAE.QualityAudit.InputList`.  
        
        Signature ``DeselectAll()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def Select(self, obj: NXOpen.NXObject) -> None:
        """
        Mark the specified object to be included in the quality audit actions.  
        
        Signature ``Select(obj)`` 
        
        :param obj: 
        :type obj: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def Deselect(self, obj: NXOpen.NXObject) -> None:
        """
        Mark the specified object to be excluded from the quality audit actions.  
        
        Signature ``Deselect(obj)`` 
        
        :param obj: 
        :type obj: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def IsSelected(self, obj: NXOpen.NXObject) -> bool:
        """
        Tells if the specified object is included in the quality audit actions.  
        
        Signature ``IsSelected(obj)`` 
        
        :param obj: 
        :type obj: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Return all the selected objects available as input to the quality audit actions.  
        
        Signature ``GetSelectedObjects()`` 
        
        :returns:  Array of selected objects  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    Null: InputList = ...  # unknown typename


class MeshLevelProjectionCheck(Action):
    """
    This action has as output the list of failed projections of the universal connections at mesh level. 
    
    To obtain this action see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: MeshLevelProjectionCheck = ...  # unknown typename


class ListConnections(Action):
    """
    This action has as result the list of all connections from the specified model. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ListConnections = ...  # unknown typename


class DiameterCheck(Action):
    """
    This action performs checks on connections supporting diameter and displays errors when diameter is different from the expected one. 
    
    To obtain this action see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: DiameterCheck = ...  # unknown typename


class ObjectLevelCorrectedProjectionResult(Result):
    """
    The Quality Audit ObjectLevelCorrectedProjectionResult is a class containing information about corrected projections on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ObjectLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the corrected projection 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with corrected projection  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the corrected projection in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the corrected projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the corrected projection.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the corrected projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ObjectLevelCorrectedProjectionResult = ...  # unknown typename


class ObjectLevelFailedProjectionResult(Result):
    """
    The Quality Audit ObjectLevelFailedProjectionResult is a class containing information about failed projections on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ObjectLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the failed projection 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with failed projection  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the failing projection in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ObjectLevelFailedProjectionResult = ...  # unknown typename


class ListConnectionsResult(Result):
    """
    The Quality Audit ListConnectionsResult is a class containing information about connections found when performing the :py:class:`NXOpen.CAE.QualityAudit.ListConnections` action. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ListConnections`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.TaggedObject = ...
    """
    Returns  the connection.  
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  the connection  
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ListConnectionsResult = ...  # unknown typename


class DiameterResult(Result):
    """
    The Quality Audit DiameterResult is a class containing information about failed diameter checks of universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.DiameterCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Null: DiameterResult = ...  # unknown typename


class ManualElementsResult(Result):
    """
    The Quality Audit ManualElementsResult is a class containing information about nodes connecting components. They are obtained by the :py:class:`NXOpen.CAE.QualityAudit.ListConnections` action. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ListConnections`.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetElements(self) -> 'list[NXOpen.CAE.FEElement]':
        """
        Returns the manual elements.  
        
        Signature ``GetElements()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.FEElement` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ManualElementsResult = ...  # unknown typename


class ConnectivityCheck(Action):
    """
    This action's output is a list of connected groups together with the involved connections. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ConnectivityCheck = ...  # unknown typename


class MinimumDistanceSettings(ActionSettings):
    """
    This class contains the minimum distance settings available for the following actions: 
    :py:class:`NXOpen.CAE.QualityAudit.FreeEdgeDistanceCheck`
    :py:class:`NXOpen.CAE.QualityAudit.ConnectionDistanceCheck`
    :py:class:`NXOpen.CAE.QualityAudit.ConnectionPointsDistanceCheck`
    . 
    
    To obtain an instance of this class get the :py:meth:`NXOpen.CAE.QualityAudit.Action.Settings`` of classed using it.
    
    .. versionadded:: NX12.0.0
    """
    MinimumDistance: NXOpen.Expression = ...
    """
    Returns  the minimum distance required.  
    
    For a smaller distance an error is reported 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: MinimumDistanceSettings = ...  # unknown typename


class MeshLevelFailedProjectionResult(Result):
    """
    The Quality Audit MeshLevelFailedProjectionResult is a class containing information about failed projections on universal connections. 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.MeshLevelProjectionCheck`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection with the failed mesh projection 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection with failed projection  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CoordinateIndex: int = ...
    """
    Returns  the coordinate index of the failing projection in the location.  
    
    See :py:class:`NXOpen.CAE.Connections.Location` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateIndex`` 
    
    :returns:  The coordinate index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DefinitionIndex: int = ...
    """
    Returns  the definition index of the failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details 
    
    <hr>
    
    Getter Method
    
    Signature ``DefinitionIndex`` 
    
    :returns:  The definition index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    FlangeIndex: int = ...
    """
    Returns  the flange index of the failing mesh projection.  
    
    See :py:class:`NXOpen.CAE.Connections.IFlangesContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeIndex`` 
    
    :returns:  The flange index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LocationIndex: int = ...
    """
    Returns  the location index of the failing projection.  
    
    See :py:class:`NXOpen.CAE.Connections.ILocationsContainer` for details  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationIndex`` 
    
    :returns:  The location index  
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: MeshLevelFailedProjectionResult = ...  # unknown typename


class ListNonModeledConnectionsResult(Result):
    """
    This is a class containing information about the non modeled universal connections. It is in the results of :py:class:`NXOpen.CAE.QualityAudit.ListNonModeledConnections` 
    
    To obtain this type of results see :py:class:`CAE.QualityAudit.ListNonModeledConnections`.
    
    .. versionadded:: NX12.0.0
    """
    Connection: NXOpen.CAE.Connections.IConnection = ...
    """
    Returns  the connection not being modeled 
    
    <hr>
    
    Getter Method
    
    Signature ``Connection`` 
    
    :returns:  Connection not being modeled  
    :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: ListNonModeledConnectionsResult = ...  # unknown typename


class FreeEdgeDistanceCheck(Action):
    """
    This action checks if there are connections that are too close to the edge based on a configurable tolerance. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: FreeEdgeDistanceCheck = ...  # unknown typename


class ActionList(NXOpen.NXObject):
    """
    The Quality Audit ActionList class offers means to select, deselect, obtain :py:class:`NXOpen.CAE.QualityAudit.Action` instances. 
    
    To obtain the instance of this class access :py:meth:`CAE.QualityAudit.Manager.ActionList` of  :py:class:`CAE.QualityAudit.Manager`.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetAction(self, id: ActionId) -> Action:
        """
        Get the action by id.  
        
        See :py:class:`NXOpen.CAE.QualityAudit.ActionId` for full the list of actions.
        
        Signature ``GetAction(id)`` 
        
        :param id:  Action id. See :py:class:`NXOpen.CAE.QualityAudit.ActionId`  
        :type id: :py:class:`NXOpen.CAE.QualityAudit.ActionId` 
        :returns:  Corresponding action  
        :rtype: :py:class:`NXOpen.CAE.QualityAudit.Action` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SelectAll(self) -> None:
        """
        Select all the actions available.  
        
        Signature ``SelectAll()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeselectAll(self) -> None:
        """
        Deselect all available actions.  
        
        Signature ``DeselectAll()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsSelected(self, pAction: Action) -> bool:
        """
        Tells if the action is to be used in the quality audit.  
        
        Signature ``IsSelected(pAction)`` 
        
        :param pAction:  The action to be checked if selected or not  
        :type pAction: :py:class:`NXOpen.CAE.QualityAudit.Action` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Select(self, pAction: Action) -> None:
        """
        Select the specified action to be used in the quality audit.  
        
        Signature ``Select(pAction)`` 
        
        :param pAction:  The action to be selected  
        :type pAction: :py:class:`NXOpen.CAE.QualityAudit.Action` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Deselect(self, pAction: Action) -> None:
        """
        Deselect the specified action to avoid using it in the quality audit.  
        
        Signature ``Deselect(pAction)`` 
        
        :param pAction:  The action to be deselected  
        :type pAction: :py:class:`NXOpen.CAE.QualityAudit.Action` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSelectedActions(self) -> 'list[Action]':
        """
        Returns an array of all selected actions.  
        
        Signature ``GetSelectedActions()`` 
        
        :returns:  The selected actions  
        :rtype: list of :py:class:`NXOpen.CAE.QualityAudit.Action` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LoadActionSettings(self, actionConfigFile: str) -> None:
        """
        Import action settings from file
        
        Signature ``LoadActionSettings(actionConfigFile)`` 
        
        :param actionConfigFile: 
        :type actionConfigFile: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SaveActionSettings(self, actionConfigFile: str) -> None:
        """
        Export action settings to file
        
        Signature ``SaveActionSettings(actionConfigFile)`` 
        
        :param actionConfigFile: 
        :type actionConfigFile: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ActionList = ...  # unknown typename


class ConnectionDistanceCheck(Action):
    """
    This action checks the distance between connections. 
    
    To obtain all the actions see :py:class:`CAE.QualityAudit.ActionList`.
    
    .. versionadded:: NX12.0.0
    """
    Null: ConnectionDistanceCheck = ...  # unknown typename


