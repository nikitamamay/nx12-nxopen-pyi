# module 'NXOpen.CAE.Connections'
#
# Automatically generated 2025-06-09T14:38:44.589792
#

import typing

import NXOpen
import NXOpen.CAE
import NXOpen.Fields



class LocationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LocationType():
    """
    Location type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Coordinates", "Coordinates"
       "Point", "Point"
       "Node", "Node"
       "SeriesOfNodes", "Series Of Nodes"
       "SeriesOfCoordinates", "Series Of Coordinates"
       "Curve", "Curve"
       "FeEdgeGroup", "Group Of Element Edges"
       "SeriesOfPoints", "Series Of Points"
       "LocationWithDirection", "Location with direction"
       "SelectionRecipe", "Selection Recipe"
    """
    Coordinates = 0  # LocationTypeMemberType
    Point = 1  # LocationTypeMemberType
    Node = 2  # LocationTypeMemberType
    SeriesOfNodes = 3  # LocationTypeMemberType
    SeriesOfCoordinates = 4  # LocationTypeMemberType
    Curve = 5  # LocationTypeMemberType
    FeEdgeGroup = 6  # LocationTypeMemberType
    SeriesOfPoints = 7  # LocationTypeMemberType
    LocationWithDirection = 8  # LocationTypeMemberType
    SelectionRecipe = 9  # LocationTypeMemberType
    
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
    


class Location(NXOpen.TaggedObject):
    """
    Location base class. This defines connection locations with common properties like coordinates.  
    
    This is an abstract class and cannot be instantiated
    
    .. versionadded:: NX11.0.0
    """
    
    def GetXyzCoordinates(self) -> 'list[NXOpen.Point3d]':
        """
        Gets the coordinates from the specified location.  
        
        The location can be any type: coordinates, node or point.
        Its coordinates will be returned.  
        
        Signature ``GetXyzCoordinates()`` 
        
        :returns:  Location coordinates  
        :rtype: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Location = ...  # unknown typename


class NodeLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX11.0.0
    """
    Node: NXOpen.CAE.FENode = ...
    """
    Returns or sets  the FEM node used for creating the location.  
    
    If the location type is not node, this method will raise an error. 
    
    <hr>
    
    Getter Method
    
    Signature ``Node`` 
    
    :returns:  Node used for location  
    :rtype: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Node`` 
    
    :param node:  Node used for location  
    :type node: :py:class:`NXOpen.CAE.FENode` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: NodeLocation = ...  # unknown typename


class INodalTargetsPairing(NXOpen.INXObject):
    """
    This class represents an Interface to the nodal connections pairing algorithm parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IConnection(NXOpen.DisplayableObject):
    """
    This class represents an interface to a connection object.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX12.0.0
    """
    UserDescription: str = ...
    """
    Returns or sets  the connection user description 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDescription`` 
    
    :returns:  User description of the connection  
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserDescription`` 
    
    :param description:  User description of the connection  
    :type description: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: IConnection = ...  # unknown typename


class IMaterial(NXOpen.INXObject):
    """
    This class represents an Interface to the Material entity.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ITolerance(NXOpen.INXObject):
    """
    This class represents an Interface to the Tolerance parameters.  
    
    .. versionadded:: NX11.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IHeight(NXOpen.INXObject):
    """
    This class represents an Interface to the Height parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IFlangesContainer(NXOpen.INXObject):
    """
    This interface offers access to the flanges of a connection (SpotWeld for example).
    The flanges are used for specifying the connecting surfaces of the connection. Each flange can have one or more entities like meshes, elements etc.
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ILocationsContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Locations parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ILineOffset(NXOpen.INXObject):
    """
    This class represents an Interface to the Diameter parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ILineDiscretization(NXOpen.INXObject):
    """
    This class represents an Interface to the Diameter parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IWidth(NXOpen.INXObject):
    """
    This class represents an Interface to the Width parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ILocationsWithDiscretizationContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Locations With Discretization container.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Adhesive(IConnection, IMaterial, ITolerance, IHeight, IFlangesContainer, ILocationsContainer, ILineOffset, ILineDiscretization, IWidth, ILocationsWithDiscretizationContainer):
    """
    Adhesive connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def IsInheritedMaterial(self) -> bool:
        """
        Use this function to check if the connection inherits material from flanges  
        
        Signature ``IsInheritedMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInheritedMaterial(self) -> None:
        """
        Use this function to set inherited material to connection 
        
        Signature ``SetInheritedMaterial()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CanInheritMaterial(self) -> bool:
        """
        Use this function to check if the connction supports inherited material  
        
        Signature ``CanInheritMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanHaveNoMaterial(self) -> bool:
        """
        Use this function to check if the connction supports having no material  
        
        Signature ``CanHaveNoMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedHeightTypes(self) -> 'list[HeightType]':
        """
        Gets supported height types of connection.  
        
        Signature ``GetSupportedHeightTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.HeightType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFlangeEntities(self, flangeIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from flange.  
        
        These can be meshes, elements, groups.  
        
        Signature ``GetFlangeEntities(flangeIndex)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :returns:  Flange entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMaxNumberOfFlanges(self) -> int:
        """
        Retrieve the max number of flanges supported by this connection  
        
        Signature ``GetMaxNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMinNumberOfFlanges(self) -> int:
        """
        Retrieve the minimmum number of flanges supported by this connection  
        
        Signature ``GetMinNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
        Get a node location to connection location list  
        
        Signature ``GetLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        :returns:  The location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
        Remove a location from connection location list 
        
        Signature ``RemoveLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
        Get a node location to connection location list  
        
        Signature ``GetNumberOfLocations(indexOfDefinition)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :returns:  The number of locations  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
        Convert a location to coordinates.  
        
        The location is given by its index  
        
        Signature ``ConvertLocationToCoordinatesType(indexOfDefinition, index)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param index:  The location index  
        :type index: int 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfDefinitions(self) -> int:
        """
        Gets the number of line offset definitions  
        
        Signature ``GetNumberOfDefinitions()`` 
        
        :returns:  The number of definitions  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
        Move the location by number of positions  
        
        Signature ``MoveLocation(indexOfDefinition, indexOfLocation, numberOfPositions)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The index of location  
        :type indexOfLocation: int 
        :param numberOfPositions:  The number of positions to move the location  
        :type numberOfPositions: int 
        :returns:  The operation result  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
        Gets the line offset vector  
        
        Signature ``GetOffsetVector(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
        Sets the line offset vector 
        
        Signature ``SetOffsetVector(lindeDefinitionIndex, offsetvector)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :param offsetvector: 
        :type offsetvector: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
        Gets the line offset distance  
        
        Signature ``GetOffsetDistance(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: 'list[NXOpen.CAE.FENode]') -> NodeSeriesLocation:
        """
        Adds a series of nodes location to connection location list  
        
        Signature ``AddLocationSeriesOfNodes(indexOfDefinition, nodes)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param nodes:  Nodes used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        :returns:  The node series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.NodeSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: 'list[NXOpen.Point]') -> PointSeriesLocation:
        """
        Adds a series of points location to connection location list  
        
        Signature ``AddLocationSeriesOfPoints(indexOfDefinition, points)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        :returns:  The point series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.PointSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: 'list[NXOpen.Point3d]') -> CoordinatesSeriesLocation:
        """
        Adds a series of coordinates location to connection location list  
        
        Signature ``AddLocationSeriesOfCoordinates(indexOfDefinition, coordinates)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param coordinates:  The location coordinates  
        :type coordinates: list of :py:class:`NXOpen.Point3d` 
        :returns:  The coord series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CoordinatesSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
        Adds a curve location to connection location list  
        
        Signature ``AddLocationCurve(indexOfDefinition, curve)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param curve:  Curve used for location creation  
        :type curve: :py:class:`NXOpen.IBaseCurve` 
        :returns:  The created curve type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CurveLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: 'list[NXOpen.CAE.FEElemEdge]') -> FeEdgesLocation:
        """
        Adds Fe Edges to connection location list  
        
        Signature ``AddLocationFeEdges(indexOfDefinition, edges)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param edges:  Edges used for location  
        :type edges: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        :returns:  The created edge group type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.FeEdgesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Material: NXOpen.PhysicalMaterial = ...
    """
    Returns or sets  the connection material 
    
    <hr>
    
    Getter Method
    
    Signature ``Material`` 
    
    :returns:  The connection material  
    :rtype: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Material`` 
    
    :param material:  The connection material  
    :type material: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaxDistCGToElemCG: NXOpen.Expression = ...
    """
    Returns  the maximum distance from definition point to center of support element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDistCGToElemCG`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxNormalDistCGToFlanges: NXOpen.Expression = ...
    """
    Returns  the maximum normal distance from definition point to center of element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxNormalDistCGToFlanges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxAngleBetweenNormals: NXOpen.Expression = ...
    """
    Returns  the maximum angle of normals with the projection surface 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxAngleBetweenNormals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProjectTolerance: NXOpen.Expression = ...
    """
    Returns  the projection tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    HeightType: HeightType = ...
    """
    Returns or sets  the height type 
    
    <hr>
    
    Getter Method
    
    Signature ``HeightType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeightType`` 
    
    :param heightType:  Diameter type  
    :type heightType: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height value 
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NumberOfFlanges: int = ...
    """
    Returns or sets  the number of flanges.  
    
    When changing the number of flanges this is not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFlanges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfFlanges`` 
    
    :param numberOfFlanges: 
    :type numberOfFlanges: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseOriginalNodesOfConnection: bool = ...
    """
    Returns or sets  the usage of original nodes of connection 
    
    <hr>
    
    Getter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseMaxLengthStep: bool = ...
    """
    Returns or sets  the usage of max length stepype 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DistanceFromStart: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance from start 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromStart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DistanceToEnd: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance to end 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceToEnd`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization length step 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaxLengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization max length step 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxLengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width value 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Adhesive = ...  # unknown typename


class DofCombinationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DofCombination():
    """
    Degrees Of Freedom Combination types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UserDefined", "User defined combination for all DOFs"
       "Clamp", "DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed"
       "Spheric", "DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free, DOF5 free, DOF6 free"
       "Point", "DOF1 fixed, DOF2 free, DOF3 free, DOF4 free, DOF5 free, DOF6 free"
       "Slider", "DOF1 free, DOF2 fixed, DOF3 fixed, DOF4 fixed, DOF5 fixed, DOF6 fixed"
       "Pivot", "DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free, DOF5 fixed, DOF6 fixed"
       "SliderPivot", "DOF1 free, DOF2 fixed, DOF3 fixed, DOF4 free, DOF5 fixed, DOF6 fixed"
       "Cardan", "DOF1 fixed, DOF2 fixed, DOF3 fixed, DOF4 free, DOF5 fixed, DOF6 free"
    """
    UserDefined = 0  # DofCombinationMemberType
    Clamp = 1  # DofCombinationMemberType
    Spheric = 2  # DofCombinationMemberType
    Point = 3  # DofCombinationMemberType
    Slider = 4  # DofCombinationMemberType
    Pivot = 5  # DofCombinationMemberType
    SliderPivot = 6  # DofCombinationMemberType
    Cardan = 7  # DofCombinationMemberType
    
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
    


class IDiameter(NXOpen.INXObject):
    """
    This class represents an Interface to the Diameter parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ComponentData(NXOpen.TaggedObject):
    """
    Composer connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    
    .. versionadded:: NX12.0.0
    """
    ComponentName: str = ...
    """
    Returns or sets  the component name  
    
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
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ConnectionPointsPath: str = ...
    """
    Returns or sets  the connection points path  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectionPointsPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectionPointsPath`` 
    
    :param connectionPointsPath: 
    :type connectionPointsPath: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    FilePath: str = ...
    """
    Returns or sets  the file path  
    
    <hr>
    
    Getter Method
    
    Signature ``FilePath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilePath`` 
    
    :param path: 
    :type path: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    IOSetPath: str = ...
    """
    Returns or sets  the IO set path  
    
    <hr>
    
    Getter Method
    
    Signature ``IOSetPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IOSetPath`` 
    
    :param ioSetPath: 
    :type ioSetPath: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MassPath: str = ...
    """
    Returns or sets  the mass path 
    
    <hr>
    
    Getter Method
    
    Signature ``MassPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MassPath`` 
    
    :param massPath: 
    :type massPath: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MeshPath: str = ...
    """
    Returns or sets  the mesh path  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshPath`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshPath`` 
    
    :param meshPath: 
    :type meshPath: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: ComponentData = ...  # unknown typename


class ILocationsWithDirContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Locations parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ConnectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectionType():
    """
    Connection type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SpotWeld", "SpotWeld"
       "Adhesive", "Adhesive"
       "Bolt", "Bolt"
       "Spring", "Spring"
       "Rigid", "Rigid"
       "Bushing", "Bushing"
       "Damper", "Damper"
       "Kinematic", "Kinematic"
       "SeamWeld", "Seam Weld"
       "Sealing", "Sealing"
    """
    SpotWeld = 0  # ConnectionTypeMemberType
    Adhesive = 1  # ConnectionTypeMemberType
    Bolt = 2  # ConnectionTypeMemberType
    Spring = 3  # ConnectionTypeMemberType
    Rigid = 4  # ConnectionTypeMemberType
    Bushing = 5  # ConnectionTypeMemberType
    Damper = 6  # ConnectionTypeMemberType
    Kinematic = 7  # ConnectionTypeMemberType
    SeamWeld = 8  # ConnectionTypeMemberType
    Sealing = 9  # ConnectionTypeMemberType
    
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
    


class ModelizationPPTRefTargetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ModelizationPPTRefTargetType():
    """
    Modelization PPTRefTargetType 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Ec", "Element collector"
       "Ecc", "Element collector container"
       "Ead", "Element Associated Data"
    """
    NotSet = 0  # ModelizationPPTRefTargetTypeMemberType
    Ec = 1  # ModelizationPPTRefTargetTypeMemberType
    Ecc = 2  # ModelizationPPTRefTargetTypeMemberType
    Ead = 3  # ModelizationPPTRefTargetTypeMemberType
    
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
    


class IStiffness(NXOpen.INXObject):
    """
    This class represents an Interface to the Stiffness constants.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class HeadDiameterTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HeadDiameterType():
    """
    Head diameter definition types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "User", "User defined diameter"
       "FactorOfDiameter", "User defined relationship with bolt diameter"
    """
    User = 0  # HeadDiameterTypeMemberType
    FactorOfDiameter = 1  # HeadDiameterTypeMemberType
    
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
    


class IDof(NXOpen.INXObject):
    """
    This class represents an interface to the connection's degrees of freedom.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IDofCombination(NXOpen.INXObject):
    """
    This class represents an interface to the connection's degrees of freedom combination.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ICsys(NXOpen.INXObject):
    """
    This class represents an Interface to the Connection Csys.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class INodalTargetsContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Connection Target Container.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Kinematic(IConnection, IDof, IDofCombination, ICsys, INodalTargetsContainer, INodalTargetsPairing):
    """
    Kinematic connection.  
    
    Use this interface to set/get properties and parameters of the Kinematic connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetDof(self, dof: Dof) -> DofType:
        """
        Get the specified degrees of freedom   
        
        Signature ``GetDof(dof)`` 
        
        :param dof: 
        :type dof: :py:class:`NXOpen.CAE.Connections.Dof` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.DofType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDof(self, dof: Dof, type: DofType) -> None:
        """
        Set the specified degrees of freedom  
        
        Signature ``SetDof(dof, type)`` 
        
        :param dof: 
        :type dof: :py:class:`NXOpen.CAE.Connections.Dof` 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.DofType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
        Set the target type 
        
        Signature ``SetTargetType(index, type)`` 
        
        :param index: 
        :type index: int 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetTarget(self, index: int) -> NodalTarget:
        """
        Get target  
        
        Signature ``GetTarget(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.NodalTarget` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    DofCombination: DofCombination = ...
    """
    Returns or sets  the degrees of freedom combination type 
    
    <hr>
    
    Getter Method
    
    Signature ``DofCombination`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.DofCombination` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DofCombination`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.CAE.Connections.DofCombination` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PairingMethod: NodalPairingMethod = ...
    """
    Returns or sets  the pairing method of targets 
    
    <hr>
    
    Getter Method
    
    Signature ``PairingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PairingMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchOrientation: NXOpen.Direction = ...
    """
    Returns or sets  the pairing search orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchConeAngle: NXOpen.Expression = ...
    """
    Returns  the search cone angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchConeAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SearchRange: NXOpen.Expression = ...
    """
    Returns  the search range 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Kinematic = ...  # unknown typename


class INodalTargetLegs(NXOpen.INXObject):
    """
    This class represents an Interface to the Connection Target.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class LocationWithDir(Location):
    """
    Location With Direction interface. This defines connection locations with direction.  
    
    To obtain an instance of this object use the AddLocationWithDirection creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    DirectionPoint: NXOpen.Point = ...
    """
    Returns or sets  the point of the direction definition end point.  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionPoint`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DirectionType: LocationDirectionType = ...
    """
    Returns  the direction type 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionType`` 
    
    :returns:  Direction type   
    :rtype: :py:class:`NXOpen.CAE.Connections.LocationDirectionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DirectionValue: NXOpen.Vector3d = ...
    """
    Returns  the direction value
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DirectionVector: NXOpen.Direction = ...
    """
    Returns or sets  the direction definition vector 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionVector`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the point of the direction definition start point.  
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: LocationWithDir = ...  # unknown typename


class IViscousDamping(NXOpen.INXObject):
    """
    This class represents an Interface to the ViscousDamping constants.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IViscousDampingDynamic(NXOpen.INXObject):
    """
    This class represents an Interface to the ViscousDamping dynamic.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class IStiffnessDynamic(NXOpen.INXObject):
    """
    This class represents an Interface to the Stiffness dynamic.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class NodalTarget(NXOpen.NXObject):
    """
    This class represents an Interface to the Connection Target.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX12.0.0
    """
    TargetType: NodalTargetType = ...
    """
    Returns  the target type 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetType`` 
    
    :returns:  Target type  
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: NodalTarget = ...  # unknown typename


class NodalTargetSetOfPoints(NodalTarget, INodalTargetLegs):
    """
    Set of Points Target. Use this interface to set/get parameters of the Set of Points Target type.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetLegsEntities(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from target's group of points.  
        
        These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
        objects able to return nodes.  
        
        Signature ``GetLegsEntities()`` 
        
        :returns:  Legs entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLegsEntities(self, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to target's group of points.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddLegsEntities(entities)`` 
        
        :param entities:  Legs entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveLegsEntities(self, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from target's group of points.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveLegsEntities(entities)`` 
        
        :param entities:  Legs entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: NodalTargetSetOfPoints = ...  # unknown typename


class PointLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX11.0.0
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the POINT used for creating the location.  
    
    If the location type is not point, this method will raise an error. 
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns:  Point used for location  
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point:  Point used for location  
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: PointLocation = ...  # unknown typename


class Sealing(IConnection, ITolerance, IFlangesContainer, ILocationsContainer, ILineOffset, ILineDiscretization, IStiffness, ICsys, ILocationsWithDiscretizationContainer):
    """
    Sealing connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    To obtain an instance of this object use the connection creators on the :py:class:`CAE.Connections.Folder`
    
    .. versionadded:: NX12.0.0
    """
    
    def GetFlangeEntities(self, flangeIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from flange.  
        
        These can be meshes, elements, groups.  
        
        Signature ``GetFlangeEntities(flangeIndex)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :returns:  Flange entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMaxNumberOfFlanges(self) -> int:
        """
        Retrieve the max number of flanges supported by this connection  
        
        Signature ``GetMaxNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMinNumberOfFlanges(self) -> int:
        """
        Retrieve the minimmum number of flanges supported by this connection  
        
        Signature ``GetMinNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
        Get a node location to connection location list  
        
        Signature ``GetLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        :returns:  The location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
        Remove a location from connection location list 
        
        Signature ``RemoveLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
        Get a node location to connection location list  
        
        Signature ``GetNumberOfLocations(indexOfDefinition)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :returns:  The number of locations  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
        Convert a location to coordinates.  
        
        The location is given by its index  
        
        Signature ``ConvertLocationToCoordinatesType(indexOfDefinition, index)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param index:  The location index  
        :type index: int 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfDefinitions(self) -> int:
        """
        Gets the number of line offset definitions  
        
        Signature ``GetNumberOfDefinitions()`` 
        
        :returns:  The number of definitions  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
        Move the location by number of positions  
        
        Signature ``MoveLocation(indexOfDefinition, indexOfLocation, numberOfPositions)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The index of location  
        :type indexOfLocation: int 
        :param numberOfPositions:  The number of positions to move the location  
        :type numberOfPositions: int 
        :returns:  The operation result  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
        Gets the line offset vector  
        
        Signature ``GetOffsetVector(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
        Sets the line offset vector 
        
        Signature ``SetOffsetVector(lindeDefinitionIndex, offsetvector)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :param offsetvector: 
        :type offsetvector: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
        Gets the line offset distance  
        
        Signature ``GetOffsetDistance(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: 'list[NXOpen.CAE.FENode]') -> NodeSeriesLocation:
        """
        Adds a series of nodes location to connection location list  
        
        Signature ``AddLocationSeriesOfNodes(indexOfDefinition, nodes)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param nodes:  Nodes used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        :returns:  The node series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.NodeSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: 'list[NXOpen.Point]') -> PointSeriesLocation:
        """
        Adds a series of points location to connection location list  
        
        Signature ``AddLocationSeriesOfPoints(indexOfDefinition, points)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        :returns:  The point series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.PointSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: 'list[NXOpen.Point3d]') -> CoordinatesSeriesLocation:
        """
        Adds a series of coordinates location to connection location list  
        
        Signature ``AddLocationSeriesOfCoordinates(indexOfDefinition, coordinates)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param coordinates:  The location coordinates  
        :type coordinates: list of :py:class:`NXOpen.Point3d` 
        :returns:  The coord series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CoordinatesSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
        Adds a curve location to connection location list  
        
        Signature ``AddLocationCurve(indexOfDefinition, curve)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param curve:  Curve used for location creation  
        :type curve: :py:class:`NXOpen.IBaseCurve` 
        :returns:  The created curve type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CurveLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: 'list[NXOpen.CAE.FEElemEdge]') -> FeEdgesLocation:
        """
        Adds Fe Edges to connection location list  
        
        Signature ``AddLocationFeEdges(indexOfDefinition, edges)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param edges:  Edges used for location  
        :type edges: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        :returns:  The created edge group type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.FeEdgesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    WithOrientation: bool = ...
    """
    Returns or sets  the target type 
    
    <hr>
    
    Getter Method
    
    Signature ``WithOrientation`` 
    
    :returns:  Orientation flag  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WithOrientation`` 
    
    :param orientation:  Orientation flag  
    :type orientation: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaxDistCGToElemCG: NXOpen.Expression = ...
    """
    Returns  the maximum distance from definition point to center of support element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDistCGToElemCG`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxNormalDistCGToFlanges: NXOpen.Expression = ...
    """
    Returns  the maximum normal distance from definition point to center of element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxNormalDistCGToFlanges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxAngleBetweenNormals: NXOpen.Expression = ...
    """
    Returns  the maximum angle of normals with the projection surface 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxAngleBetweenNormals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProjectTolerance: NXOpen.Expression = ...
    """
    Returns  the projection tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NumberOfFlanges: int = ...
    """
    Returns or sets  the number of flanges.  
    
    When changing the number of flanges this is not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFlanges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfFlanges`` 
    
    :param numberOfFlanges: 
    :type numberOfFlanges: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseOriginalNodesOfConnection: bool = ...
    """
    Returns or sets  the usage of original nodes of connection 
    
    <hr>
    
    Getter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseMaxLengthStep: bool = ...
    """
    Returns or sets  the usage of max length stepype 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DistanceFromStart: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance from start 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromStart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DistanceToEnd: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance to end 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceToEnd`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization length step 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaxLengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization max length step 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxLengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the X stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Y stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Z stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RX stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RY stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RZ stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: Sealing = ...  # unknown typename


class NodalPairingMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalPairingMethod():
    """
    Nodal pairing method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Proximity", "Proximity"
       "OrientatedSearch", "Oriented Search"
       "SelectionOrder", "Selection Order"
    """
    Proximity = 0  # NodalPairingMethodMemberType
    OrientatedSearch = 1  # NodalPairingMethodMemberType
    SelectionOrder = 2  # NodalPairingMethodMemberType
    
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
    


class LocationDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LocationDirectionType():
    """
    Location and Direction type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Point", "Two Points/Nodes"
       "Vector", "Points/Node and Vector"
    """
    Point = 0  # LocationDirectionTypeMemberType
    Vector = 1  # LocationDirectionTypeMemberType
    
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
    


class Composer(NXOpen.TaggedObject):
    """
    Composer.  
    
    Use this interface to set/get properties and parameters of the composer.  
    
    .. versionadded:: NX12.0.0
    """
    
    def ReadAssemblyDefinition(self, filePath: str) -> None:
        """
        ReadAssemblyFromExcel  
        
        Signature ``ReadAssemblyDefinition(filePath)`` 
        
        :param filePath: 
        :type filePath: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def WriteAssemblyDefinition(self, filePath: str) -> None:
        """
        WriteAssemblyFromExcel  
        
        Signature ``WriteAssemblyDefinition(filePath)`` 
        
        :param filePath: 
        :type filePath: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def ReadConnectionsDB(self, filePath: str) -> None:
        """
        ReadConnectionsDB  
        
        Signature ``ReadConnectionsDB(filePath)`` 
        
        :param filePath: 
        :type filePath: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMeshPartFromPID(self, pid: NXOpen.TaggedObject) -> 'list[NXOpen.TaggedObject]':
        """
        GetMeshPartFromPID  
        
        Signature ``GetMeshPartFromPID(pid)`` 
        
        :param pid: 
        :type pid: :py:class:`NXOpen.TaggedObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetAxisFromAlias(self, axisAlias: str) -> 'list[NXOpen.CoordinateSystem]':
        """
        GetAxisFromAlias  
        
        Signature ``GetAxisFromAlias(axisAlias)`` 
        
        :param axisAlias: 
        :type axisAlias: str 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CoordinateSystem` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetGroupFromAlias(self, axisAlias: str) -> 'list[NXOpen.CAE.SelectionRecipe]':
        """
        GetGroupFromAlias  
        
        Signature ``GetGroupFromAlias(axisAlias)`` 
        
        :param axisAlias: 
        :type axisAlias: str 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.SelectionRecipe` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CheckAssemblyConnections(self) -> 'list[str]':
        """
        CheckAssemblyConnections   
        
        Signature ``CheckAssemblyConnections()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CheckAssemblyDocumentConnections(self) -> 'list[str]':
        """
        CheckAssemblyDocumentConnections   
        
        Signature ``CheckAssemblyDocumentConnections()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    ComposerData: ComposerData = ...
    """
    Returns or sets  the composer data  
    
    <hr>
    
    Getter Method
    
    Signature ``ComposerData`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ComposerData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ComposerData`` 
    
    :param composerData: 
    :type composerData: :py:class:`NXOpen.CAE.Connections.ComposerData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ConnectionDBData: ConnectionDBData = ...
    """
    Returns or sets  the connection db data  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectionDBData`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ConnectionDBData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectionDBData`` 
    
    :param connectionDBData: 
    :type connectionDBData: :py:class:`NXOpen.CAE.Connections.ConnectionDBData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: Composer = ...  # unknown typename


class IStructuralDamping(NXOpen.INXObject):
    """
    This class represents an Interface to the StructuralDamping constants.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class MaterialTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MaterialType():
    """
    Material definition types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "User", "User defined material"
       "FromSupport", "Material defined from support"
    """
    User = 0  # MaterialTypeMemberType
    FromSupport = 1  # MaterialTypeMemberType
    
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
    


class ComposerData(NXOpen.TaggedObject):
    """
    Composer connection.  
    
    Use this interface to set/get properties and parameters of the composer.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetComponents(self) -> 'list[ComponentData]':
        """
        Gets components.  
        
        Signature ``GetComponents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Connections.ComponentData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetComponents(self, components: 'list[ComponentData]') -> None:
        """
        Sets components.  
        
        Signature ``SetComponents(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.CAE.Connections.ComponentData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetConnections(self) -> 'list[ConnectionData]':
        """
        Gets connections  
        
        Signature ``GetConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Connections.ConnectionData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetConnections(self, connections: 'list[ConnectionData]') -> None:
        """
        Sets connections 
        
        Signature ``SetConnections(connections)`` 
        
        :param connections: 
        :type connections: list of :py:class:`NXOpen.CAE.Connections.ConnectionData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    AssemblyName: str = ...
    """
    Returns or sets  the assembly name  
    
    <hr>
    
    Getter Method
    
    Signature ``AssemblyName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssemblyName`` 
    
    :param assemblyName: 
    :type assemblyName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    InputFileDir: str = ...
    """
    Returns or sets  the input file direction  
    
    <hr>
    
    Getter Method
    
    Signature ``InputFileDir`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputFileDir`` 
    
    :param inputFileDir: 
    :type inputFileDir: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaterialDBDir: str = ...
    """
    Returns or sets  the material file direction  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialDBDir`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialDBDir`` 
    
    :param materialDBDir: 
    :type materialDBDir: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    OutputFileDir: str = ...
    """
    Returns or sets  the output file direction  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputFileDir`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputFileDir`` 
    
    :param outputFileDir: 
    :type outputFileDir: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StartNumAxisSystems: int = ...
    """
    Returns or sets  the start axis number  
    
    <hr>
    
    Getter Method
    
    Signature ``StartNumAxisSystems`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartNumAxisSystems`` 
    
    :param startNumAxisSystems: 
    :type startNumAxisSystems: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StartNumNodeAndElement: int = ...
    """
    Returns or sets  the start node and element number  
    
    <hr>
    
    Getter Method
    
    Signature ``StartNumNodeAndElement`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartNumNodeAndElement`` 
    
    :param startNumNodeAndElement: 
    :type startNumNodeAndElement: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StartNumProperties: int = ...
    """
    Returns or sets  the start properties number  
    
    <hr>
    
    Getter Method
    
    Signature ``StartNumProperties`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartNumProperties`` 
    
    :param startNumProperties: 
    :type startNumProperties: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: ComposerData = ...  # unknown typename


class ConnectionDBItemData(NXOpen.TaggedObject):
    """
    Connection DB item data.  
    
    Use this interface to set/get properties and parameters of the Connection DB item data.  
    
    .. versionadded:: NX12.0.0
    """
    Mass: float = ...
    """
    Returns or sets  the mass  
    
    <hr>
    
    Getter Method
    
    Signature ``Mass`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Mass`` 
    
    :param mass: 
    :type mass: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaterialName: str = ...
    """
    Returns or sets  the material name  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialName`` 
    
    :param materialName: 
    :type materialName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Name: str = ...
    """
    Returns or sets  the name  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ScrewDiameter: float = ...
    """
    Returns or sets  the screw diameter  
    
    <hr>
    
    Getter Method
    
    Signature ``ScrewDiameter`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScrewDiameter`` 
    
    :param screwDiameter: 
    :type screwDiameter: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessR: float = ...
    """
    Returns or sets  the stiffness R  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessR`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessR`` 
    
    :param stiffnessR: 
    :type stiffnessR: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessRR: float = ...
    """
    Returns or sets  the stiffness RR  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessRR`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessRR`` 
    
    :param stiffnessRR: 
    :type stiffnessRR: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessRS: float = ...
    """
    Returns or sets  the stiffness RS  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessRS`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessRS`` 
    
    :param stiffnessRS: 
    :type stiffnessRS: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessRX: float = ...
    """
    Returns or sets  the stiffness RX  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessRX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessRX`` 
    
    :param stiffnessRX: 
    :type stiffnessRX: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessRY: float = ...
    """
    Returns or sets  the stiffness RY  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessRY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessRY`` 
    
    :param stiffnessRY: 
    :type stiffnessRY: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessRZ: float = ...
    """
    Returns or sets  the stiffness RZ  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessRZ`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessRZ`` 
    
    :param stiffnessRZ: 
    :type stiffnessRZ: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessS: float = ...
    """
    Returns or sets  the stiffness RS  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessS`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessS`` 
    
    :param stiffnessS: 
    :type stiffnessS: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessType: ConnectionDBItemStiffnessType = ...
    """
    Returns or sets  the mass  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ConnectionDBItemStiffnessType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessType`` 
    
    :param stiffnessType: 
    :type stiffnessType: :py:class:`NXOpen.CAE.Connections.ConnectionDBItemStiffnessType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessX: float = ...
    """
    Returns or sets  the stiffness X  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessX`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessX`` 
    
    :param stiffnessX: 
    :type stiffnessX: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessY: float = ...
    """
    Returns or sets  the stiffness Y  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessY`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessY`` 
    
    :param stiffnessY: 
    :type stiffnessY: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    StiffnessZ: float = ...
    """
    Returns or sets  the stiffness Z  
    
    <hr>
    
    Getter Method
    
    Signature ``StiffnessZ`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StiffnessZ`` 
    
    :param stiffnessZ: 
    :type stiffnessZ: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: ConnectionDBItemData = ...  # unknown typename


class ElementCollection(NXOpen.TaggedObjectCollection):
    """
    Element collection provides methods to manage :py:class:`CAE.Connections.Element` objects  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.BaseFEModel`
    
    .. versionadded:: NX11.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def Create(self, elementType: ElementType, name: str, connections: 'list[IConnection]') -> Element:
        """
        Creates a :py:class:`NXOpen.CAE.Connections.Element` 
        
        Signature ``Create(elementType, name, connections)`` 
        
        :param elementType: 
        :type elementType: :py:class:`NXOpen.CAE.Connections.ElementType` 
        :param name: 
        :type name: str 
        :param connections: 
        :type connections: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.Element` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    


class NodeSeriesLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    
    def GetNodes(self) -> 'list[NXOpen.CAE.FENode]':
        """
        Retrieve location nodes.  
        
        Signature ``GetNodes()`` 
        
        :returns:  Node used for location  
        :rtype: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddNodes(self, nodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Add location nodes.  
        
        Signature ``AddNodes(nodes)`` 
        
        :param nodes:  Node used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def SetNodes(self, nodes: 'list[NXOpen.CAE.FENode]') -> None:
        """
        Set location nodes.  
        
        Signature ``SetNodes(nodes)`` 
        
        :param nodes:  Node used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: NodeSeriesLocation = ...  # unknown typename


class Rigid(IConnection, IDof, ICsys, INodalTargetsContainer, INodalTargetsPairing):
    """
    Rigid connection.  
    
    Use this interface to set/get properties and parameters of the Rigid connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetDof(self, dof: Dof) -> DofType:
        """
        Get the specified degrees of freedom   
        
        Signature ``GetDof(dof)`` 
        
        :param dof: 
        :type dof: :py:class:`NXOpen.CAE.Connections.Dof` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.DofType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDof(self, dof: Dof, type: DofType) -> None:
        """
        Set the specified degrees of freedom  
        
        Signature ``SetDof(dof, type)`` 
        
        :param dof: 
        :type dof: :py:class:`NXOpen.CAE.Connections.Dof` 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.DofType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
        Set the target type 
        
        Signature ``SetTargetType(index, type)`` 
        
        :param index: 
        :type index: int 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetTarget(self, index: int) -> NodalTarget:
        """
        Get target  
        
        Signature ``GetTarget(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.NodalTarget` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PairingMethod: NodalPairingMethod = ...
    """
    Returns or sets  the pairing method of targets 
    
    <hr>
    
    Getter Method
    
    Signature ``PairingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PairingMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchOrientation: NXOpen.Direction = ...
    """
    Returns or sets  the pairing search orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchConeAngle: NXOpen.Expression = ...
    """
    Returns  the search cone angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchConeAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SearchRange: NXOpen.Expression = ...
    """
    Returns  the search range 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Rigid = ...  # unknown typename


class SeamWeld(IConnection, IMaterial, ITolerance, IHeight, IFlangesContainer, ILocationsContainer, ILineOffset, ILineDiscretization, IWidth, ILocationsWithDiscretizationContainer):
    """
    Seam Weld connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    To obtain an instance of this object use the connection creators on the :py:class:`CAE.Connections.Folder`
    
    .. versionadded:: NX12.0.0
    """
    
    def IsInheritedMaterial(self) -> bool:
        """
        Use this function to check if the connection inherits material from flanges  
        
        Signature ``IsInheritedMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInheritedMaterial(self) -> None:
        """
        Use this function to set inherited material to connection 
        
        Signature ``SetInheritedMaterial()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CanInheritMaterial(self) -> bool:
        """
        Use this function to check if the connction supports inherited material  
        
        Signature ``CanInheritMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanHaveNoMaterial(self) -> bool:
        """
        Use this function to check if the connction supports having no material  
        
        Signature ``CanHaveNoMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedHeightTypes(self) -> 'list[HeightType]':
        """
        Gets supported height types of connection.  
        
        Signature ``GetSupportedHeightTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.HeightType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFlangeEntities(self, flangeIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from flange.  
        
        These can be meshes, elements, groups.  
        
        Signature ``GetFlangeEntities(flangeIndex)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :returns:  Flange entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMaxNumberOfFlanges(self) -> int:
        """
        Retrieve the max number of flanges supported by this connection  
        
        Signature ``GetMaxNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMinNumberOfFlanges(self) -> int:
        """
        Retrieve the minimmum number of flanges supported by this connection  
        
        Signature ``GetMinNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
        Get a node location to connection location list  
        
        Signature ``GetLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        :returns:  The location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
        Remove a location from connection location list 
        
        Signature ``RemoveLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
        Get a node location to connection location list  
        
        Signature ``GetNumberOfLocations(indexOfDefinition)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :returns:  The number of locations  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
        Convert a location to coordinates.  
        
        The location is given by its index  
        
        Signature ``ConvertLocationToCoordinatesType(indexOfDefinition, index)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param index:  The location index  
        :type index: int 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfDefinitions(self) -> int:
        """
        Gets the number of line offset definitions  
        
        Signature ``GetNumberOfDefinitions()`` 
        
        :returns:  The number of definitions  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
        Move the location by number of positions  
        
        Signature ``MoveLocation(indexOfDefinition, indexOfLocation, numberOfPositions)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The index of location  
        :type indexOfLocation: int 
        :param numberOfPositions:  The number of positions to move the location  
        :type numberOfPositions: int 
        :returns:  The operation result  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
        Gets the line offset vector  
        
        Signature ``GetOffsetVector(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
        Sets the line offset vector 
        
        Signature ``SetOffsetVector(lindeDefinitionIndex, offsetvector)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :param offsetvector: 
        :type offsetvector: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
        Gets the line offset distance  
        
        Signature ``GetOffsetDistance(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: 'list[NXOpen.CAE.FENode]') -> NodeSeriesLocation:
        """
        Adds a series of nodes location to connection location list  
        
        Signature ``AddLocationSeriesOfNodes(indexOfDefinition, nodes)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param nodes:  Nodes used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        :returns:  The node series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.NodeSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: 'list[NXOpen.Point]') -> PointSeriesLocation:
        """
        Adds a series of points location to connection location list  
        
        Signature ``AddLocationSeriesOfPoints(indexOfDefinition, points)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        :returns:  The point series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.PointSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: 'list[NXOpen.Point3d]') -> CoordinatesSeriesLocation:
        """
        Adds a series of coordinates location to connection location list  
        
        Signature ``AddLocationSeriesOfCoordinates(indexOfDefinition, coordinates)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param coordinates:  The location coordinates  
        :type coordinates: list of :py:class:`NXOpen.Point3d` 
        :returns:  The coord series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CoordinatesSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
        Adds a curve location to connection location list  
        
        Signature ``AddLocationCurve(indexOfDefinition, curve)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param curve:  Curve used for location creation  
        :type curve: :py:class:`NXOpen.IBaseCurve` 
        :returns:  The created curve type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CurveLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: 'list[NXOpen.CAE.FEElemEdge]') -> FeEdgesLocation:
        """
        Adds Fe Edges to connection location list  
        
        Signature ``AddLocationFeEdges(indexOfDefinition, edges)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param edges:  Edges used for location  
        :type edges: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        :returns:  The created edge group type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.FeEdgesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    SeamWeldType: SeamWeldType = ...
    """
    Returns or sets  the seam weld type 
    
    <hr>
    
    Getter Method
    
    Signature ``SeamWeldType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.SeamWeldType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeamWeldType`` 
    
    :param seamWeldType: 
    :type seamWeldType: :py:class:`NXOpen.CAE.Connections.SeamWeldType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Material: NXOpen.PhysicalMaterial = ...
    """
    Returns or sets  the connection material 
    
    <hr>
    
    Getter Method
    
    Signature ``Material`` 
    
    :returns:  The connection material  
    :rtype: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Material`` 
    
    :param material:  The connection material  
    :type material: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaxDistCGToElemCG: NXOpen.Expression = ...
    """
    Returns  the maximum distance from definition point to center of support element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDistCGToElemCG`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxNormalDistCGToFlanges: NXOpen.Expression = ...
    """
    Returns  the maximum normal distance from definition point to center of element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxNormalDistCGToFlanges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxAngleBetweenNormals: NXOpen.Expression = ...
    """
    Returns  the maximum angle of normals with the projection surface 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxAngleBetweenNormals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProjectTolerance: NXOpen.Expression = ...
    """
    Returns  the projection tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    HeightType: HeightType = ...
    """
    Returns or sets  the height type 
    
    <hr>
    
    Getter Method
    
    Signature ``HeightType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeightType`` 
    
    :param heightType:  Diameter type  
    :type heightType: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height value 
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NumberOfFlanges: int = ...
    """
    Returns or sets  the number of flanges.  
    
    When changing the number of flanges this is not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFlanges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfFlanges`` 
    
    :param numberOfFlanges: 
    :type numberOfFlanges: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseOriginalNodesOfConnection: bool = ...
    """
    Returns or sets  the usage of original nodes of connection 
    
    <hr>
    
    Getter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseMaxLengthStep: bool = ...
    """
    Returns or sets  the usage of max length stepype 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DistanceFromStart: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance from start 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromStart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DistanceToEnd: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance to end 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceToEnd`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization length step 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaxLengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization max length step 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxLengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width value 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: SeamWeld = ...  # unknown typename


class Spring(IConnection, IStiffness, ICsys, INodalTargetsContainer, INodalTargetsPairing):
    """
    Spring connection.  
    
    Use this interface to set/get properties and parameters of the Spring connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
        Set the target type 
        
        Signature ``SetTargetType(index, type)`` 
        
        :param index: 
        :type index: int 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetTarget(self, index: int) -> NodalTarget:
        """
        Get target  
        
        Signature ``GetTarget(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.NodalTarget` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    XStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the X stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Y stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Z stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RX stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RY stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RZ stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PairingMethod: NodalPairingMethod = ...
    """
    Returns or sets  the pairing method of targets 
    
    <hr>
    
    Getter Method
    
    Signature ``PairingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PairingMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchOrientation: NXOpen.Direction = ...
    """
    Returns or sets  the pairing search orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchConeAngle: NXOpen.Expression = ...
    """
    Returns  the search cone angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchConeAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SearchRange: NXOpen.Expression = ...
    """
    Returns  the search range 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Spring = ...  # unknown typename


class TargetDependencyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TargetDependencyType():
    """
    Nodal target dependency type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No dependency"
       "Dependent", "Dependent target"
       "Independent", "Independent target"
    """
    NotSet = 0  # TargetDependencyTypeMemberType
    Dependent = 1  # TargetDependencyTypeMemberType
    Independent = 2  # TargetDependencyTypeMemberType
    
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
    


class CoordinatesSeriesLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    
    def GetCoordinates(self) -> 'list[NXOpen.Point3d]':
        """
        Gets the coordinates from the specified location.  
        
        The location can be any type: coordinates, node or point.
        Its coordinates will be returned.  
        
        Signature ``GetCoordinates()`` 
        
        :returns:  Location coordinates  
        :rtype: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCoordinates(self, coordinates: 'list[NXOpen.Point3d]') -> None:
        """
        Set the coordinates.  
        
        Only for coordinates type location 
        
        Signature ``SetCoordinates(coordinates)`` 
        
        :param coordinates:  The location coordinates  
        :type coordinates: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: CoordinatesSeriesLocation = ...  # unknown typename


class DofTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DofType():
    """
    Degrees Of Freedom types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Free", "The DOF is not constrained"
       "Fixed", "The DOF is fixed"
    """
    Free = 0  # DofTypeMemberType
    Fixed = 1  # DofTypeMemberType
    
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
    


class Bolt(IConnection, IMaterial, IFlangesContainer, ILocationsContainer, IDiameter, ILocationsWithDirContainer):
    """
    Bolt connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    To obtain an instance of this object use the connection creators on the :py:class:`CAE.Connections.Folder`
    
    .. versionadded:: NX12.0.0
    """
    
    def IsInheritedMaterial(self) -> bool:
        """
        Use this function to check if the connection inherits material from flanges  
        
        Signature ``IsInheritedMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInheritedMaterial(self) -> None:
        """
        Use this function to set inherited material to connection 
        
        Signature ``SetInheritedMaterial()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CanInheritMaterial(self) -> bool:
        """
        Use this function to check if the connction supports inherited material  
        
        Signature ``CanInheritMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanHaveNoMaterial(self) -> bool:
        """
        Use this function to check if the connction supports having no material  
        
        Signature ``CanHaveNoMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFlangeEntities(self, flangeIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from flange.  
        
        These can be meshes, elements, groups.  
        
        Signature ``GetFlangeEntities(flangeIndex)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :returns:  Flange entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMaxNumberOfFlanges(self) -> int:
        """
        Retrieve the max number of flanges supported by this connection  
        
        Signature ``GetMaxNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMinNumberOfFlanges(self) -> int:
        """
        Retrieve the minimmum number of flanges supported by this connection  
        
        Signature ``GetMinNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
        Get a node location to connection location list  
        
        Signature ``GetLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        :returns:  The location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
        Remove a location from connection location list 
        
        Signature ``RemoveLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
        Get a node location to connection location list  
        
        Signature ``GetNumberOfLocations(indexOfDefinition)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :returns:  The number of locations  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
        Convert a location to coordinates.  
        
        The location is given by its index  
        
        Signature ``ConvertLocationToCoordinatesType(indexOfDefinition, index)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param index:  The location index  
        :type index: int 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfDefinitions(self) -> int:
        """
        Gets the number of line offset definitions  
        
        Signature ``GetNumberOfDefinitions()`` 
        
        :returns:  The number of definitions  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
        Move the location by number of positions  
        
        Signature ``MoveLocation(indexOfDefinition, indexOfLocation, numberOfPositions)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The index of location  
        :type indexOfLocation: int 
        :param numberOfPositions:  The number of positions to move the location  
        :type numberOfPositions: int 
        :returns:  The operation result  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedDiameterTypes(self) -> 'list[DiameterType]':
        """
        Gets supported diameter types of connection.  
        
        Signature ``GetSupportedDiameterTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.DiameterType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLocationCoordinatesWithDirectionCoordinates(self, indexOfDefinition: int, point: NXOpen.Point, direction: NXOpen.Point) -> LocationWithDir:
        """
        Adds a coordinates location with direction definited by coordinates to connection location list  
        
        Signature ``AddLocationCoordinatesWithDirectionCoordinates(indexOfDefinition, point, direction)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param point:  Location Coordinates  
        :type point: :py:class:`NXOpen.Point` 
        :param direction:  Direction Point  
        :type direction: :py:class:`NXOpen.Point` 
        :returns:  The created coordinates with direction type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.LocationWithDir` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCoordinatesWithDirectionVector(self, indexOfDefinition: int, masterPoint: NXOpen.Point, direction: NXOpen.Direction) -> LocationWithDir:
        """
        Adds a coordinates location with direction definited by vector to connection location list  
        
        Signature ``AddLocationCoordinatesWithDirectionVector(indexOfDefinition, masterPoint, direction)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param masterPoint:  Location Coordinates  
        :type masterPoint: :py:class:`NXOpen.Point` 
        :param direction:  Direction direction  
        :type direction: :py:class:`NXOpen.Direction` 
        :returns:  The created point with direction type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.LocationWithDir` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    HeadDiameter: NXOpen.Expression = ...
    """
    Returns  the head diameter  
    
    <hr>
    
    Getter Method
    
    Signature ``HeadDiameter`` 
    
    :returns:  Head diameter 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    HeadDiameterCoefficient: NXOpen.Expression = ...
    """
    Returns  the head diameter coefficient 
    
    <hr>
    
    Getter Method
    
    Signature ``HeadDiameterCoefficient`` 
    
    :returns:  Head diameter 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    HeadDiameterType: HeadDiameterType = ...
    """
    Returns or sets  the head diameter type 
    
    <hr>
    
    Getter Method
    
    Signature ``HeadDiameterType`` 
    
    :returns:  Head diameter type 
    :rtype: :py:class:`NXOpen.CAE.Connections.HeadDiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeadDiameterType`` 
    
    :param param:  Head diameter type  
    :type param: :py:class:`NXOpen.CAE.Connections.HeadDiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaxBoltLength: NXOpen.Expression = ...
    """
    Returns  the maximum bolt length 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxBoltLength`` 
    
    :returns:  Maximmum bolt length 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Material: NXOpen.PhysicalMaterial = ...
    """
    Returns or sets  the connection material 
    
    <hr>
    
    Getter Method
    
    Signature ``Material`` 
    
    :returns:  The connection material  
    :rtype: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Material`` 
    
    :param material:  The connection material  
    :type material: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    NumberOfFlanges: int = ...
    """
    Returns or sets  the number of flanges.  
    
    When changing the number of flanges this is not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFlanges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfFlanges`` 
    
    :param numberOfFlanges: 
    :type numberOfFlanges: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DiameterType: DiameterType = ...
    """
    Returns or sets  the diameter type 
    
    <hr>
    
    Getter Method
    
    Signature ``DiameterType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.DiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DiameterType`` 
    
    :param diameterType: 
    :type diameterType: :py:class:`NXOpen.CAE.Connections.DiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the connection diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Coefficient: NXOpen.Expression = ...
    """
    Returns  the coefficient for formula defined diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``Coefficient`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    TableFile: str = ...
    """
    Returns or sets  the table file used to compute the diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``TableFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TableFile`` 
    
    :param tableFile:  Full path to the diameter table file.  
    :type tableFile: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: Bolt = ...  # unknown typename


class FeEdgesLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    
    def GetFeEdges(self) -> 'list[NXOpen.CAE.FEElemEdge]':
        """
        Retrieve location edges.  
        
        Signature ``GetFeEdges()`` 
        
        :returns:  Edges used for location  
        :rtype: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFeEdges(self, edges: 'list[NXOpen.CAE.FEElemEdge]') -> None:
        """
        Add location edges.  
        
        Signature ``SetFeEdges(edges)`` 
        
        :param edges:  Edges used for location  
        :type edges: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: FeEdgesLocation = ...  # unknown typename


class ConnectionDBItemStiffnessTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectionDBItemStiffnessType():
    """
    connection DB item stiffness type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Rectangular", "Rectangular"
       "Spherical", "Spherical"
       "Cylindrical", "Cylindrical"
    """
    NotSet = 0  # ConnectionDBItemStiffnessTypeMemberType
    Rectangular = 1  # ConnectionDBItemStiffnessTypeMemberType
    Spherical = 2  # ConnectionDBItemStiffnessTypeMemberType
    Cylindrical = 3  # ConnectionDBItemStiffnessTypeMemberType
    
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
    


class CurveLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    Curve: NXOpen.IBaseCurve = ...
    """
    Returns or sets  the CURVE used for creating the location.  
    
    If the location type is not curve, this method will raise an error. 
    
    <hr>
    
    Getter Method
    
    Signature ``Curve`` 
    
    :returns:  Curve used for location  
    :rtype: :py:class:`NXOpen.IBaseCurve` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Curve`` 
    
    :param curve:  Curve used for location  
    :type curve: :py:class:`NXOpen.IBaseCurve` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: CurveLocation = ...  # unknown typename


class ILocationsSinglePointContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Locations parameters.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class ILocationsMultiPointContainer(NXOpen.INXObject):
    """
    This class represents an Interface to the Multi Point Locations container.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class SpotWeld(IConnection, IMaterial, ITolerance, IDiameter, IHeight, IFlangesContainer, ILocationsContainer, ILocationsSinglePointContainer, ILocationsMultiPointContainer, ILocationsWithDiscretizationContainer, ILineOffset, ILineDiscretization):
    """
    Spot Weld connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def IsInheritedMaterial(self) -> bool:
        """
        Use this function to check if the connection inherits material from flanges  
        
        Signature ``IsInheritedMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInheritedMaterial(self) -> None:
        """
        Use this function to set inherited material to connection 
        
        Signature ``SetInheritedMaterial()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CanInheritMaterial(self) -> bool:
        """
        Use this function to check if the connction supports inherited material  
        
        Signature ``CanInheritMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CanHaveNoMaterial(self) -> bool:
        """
        Use this function to check if the connction supports having no material  
        
        Signature ``CanHaveNoMaterial()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedDiameterTypes(self) -> 'list[DiameterType]':
        """
        Gets supported diameter types of connection.  
        
        Signature ``GetSupportedDiameterTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.DiameterType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSupportedHeightTypes(self) -> 'list[HeightType]':
        """
        Gets supported height types of connection.  
        
        Signature ``GetSupportedHeightTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.HeightType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFlangeEntities(self, flangeIndex: int) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from flange.  
        
        These can be meshes, elements, groups.  
        
        Signature ``GetFlangeEntities(flangeIndex)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :returns:  Flange entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveFlangeEntities(self, flangeIndex: int, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from flange.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveFlangeEntities(flangeIndex, entities)`` 
        
        :param flangeIndex: 
        :type flangeIndex: int 
        :param entities:  Flange entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMaxNumberOfFlanges(self) -> int:
        """
        Retrieve the max number of flanges supported by this connection  
        
        Signature ``GetMaxNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetMinNumberOfFlanges(self) -> int:
        """
        Retrieve the minimmum number of flanges supported by this connection  
        
        Signature ``GetMinNumberOfFlanges()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLocation(self, indexOfDefinition: int, indexOfLocation: int) -> Location:
        """
        Get a node location to connection location list  
        
        Signature ``GetLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        :returns:  The location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveLocation(self, indexOfDefinition: int, indexOfLocation: int) -> None:
        """
        Remove a location from connection location list 
        
        Signature ``RemoveLocation(indexOfDefinition, indexOfLocation)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The location index  
        :type indexOfLocation: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfLocations(self, indexOfDefinition: int) -> int:
        """
        Get a node location to connection location list  
        
        Signature ``GetNumberOfLocations(indexOfDefinition)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :returns:  The number of locations  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertLocationToCoordinatesType(self, indexOfDefinition: int, index: int) -> Location:
        """
        Convert a location to coordinates.  
        
        The location is given by its index  
        
        Signature ``ConvertLocationToCoordinatesType(indexOfDefinition, index)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param index:  The location index  
        :type index: int 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.Location` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetNumberOfDefinitions(self) -> int:
        """
        Gets the number of line offset definitions  
        
        Signature ``GetNumberOfDefinitions()`` 
        
        :returns:  The number of definitions  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MoveLocation(self, indexOfDefinition: int, indexOfLocation: int, numberOfPositions: int) -> bool:
        """
        Move the location by number of positions  
        
        Signature ``MoveLocation(indexOfDefinition, indexOfLocation, numberOfPositions)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param indexOfLocation:  The index of location  
        :type indexOfLocation: int 
        :param numberOfPositions:  The number of positions to move the location  
        :type numberOfPositions: int 
        :returns:  The operation result  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLocationNode(self, indexOfDefinition: int, node: NXOpen.CAE.FENode) -> NodeLocation:
        """
        Adds a node location to connection location list  
        
        Signature ``AddLocationNode(indexOfDefinition, node)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param node:  Node used for location  
        :type node: :py:class:`NXOpen.CAE.FENode` 
        :returns:  The node type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.NodeLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCoordinates(self, indexOfDefinition: int, coordinates: NXOpen.Point3d) -> CoordinatesLocation:
        """
        Adds a coordinates location to connection location list  
        
        Signature ``AddLocationCoordinates(indexOfDefinition, coordinates)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param coordinates:  Coordinates  
        :type coordinates: :py:class:`NXOpen.Point3d` 
        :returns:  The created coordinates type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CoordinatesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationPoint(self, indexOfDefinition: int, point: NXOpen.Point) -> PointLocation:
        """
        Adds a point location to connection location list  
        
        Signature ``AddLocationPoint(indexOfDefinition, point)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param point:  Point used for location creation  
        :type point: :py:class:`NXOpen.Point` 
        :returns:  The created point type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.PointLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSelectionRecipe(self, indexOfDefinition: int, selectionRecipe: NXOpen.CAE.SelectionRecipe) -> SelectionRecipeLocation:
        """
        Adds a Selection Recipe to connection location list  
        
        Signature ``AddLocationSelectionRecipe(indexOfDefinition, selectionRecipe)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param selectionRecipe:  Selection Recipe used for location creation  
        :type selectionRecipe: :py:class:`NXOpen.CAE.SelectionRecipe` 
        :returns:  The created selection recipe type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.SelectionRecipeLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfNodes(self, indexOfDefinition: int, nodes: 'list[NXOpen.CAE.FENode]') -> NodeSeriesLocation:
        """
        Adds a series of nodes location to connection location list  
        
        Signature ``AddLocationSeriesOfNodes(indexOfDefinition, nodes)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param nodes:  Nodes used for location  
        :type nodes: list of :py:class:`NXOpen.CAE.FENode` 
        :returns:  The node series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.NodeSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfPoints(self, indexOfDefinition: int, points: 'list[NXOpen.Point]') -> PointSeriesLocation:
        """
        Adds a series of points location to connection location list  
        
        Signature ``AddLocationSeriesOfPoints(indexOfDefinition, points)`` 
        
        :param indexOfDefinition:  The index of definition   
        :type indexOfDefinition: int 
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        :returns:  The point series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.PointSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationSeriesOfCoordinates(self, indexOfDefinition: int, coordinates: 'list[NXOpen.Point3d]') -> CoordinatesSeriesLocation:
        """
        Adds a series of coordinates location to connection location list  
        
        Signature ``AddLocationSeriesOfCoordinates(indexOfDefinition, coordinates)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param coordinates:  The location coordinates  
        :type coordinates: list of :py:class:`NXOpen.Point3d` 
        :returns:  The coord series type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CoordinatesSeriesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationCurve(self, indexOfDefinition: int, curve: NXOpen.IBaseCurve) -> CurveLocation:
        """
        Adds a curve location to connection location list  
        
        Signature ``AddLocationCurve(indexOfDefinition, curve)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param curve:  Curve used for location creation  
        :type curve: :py:class:`NXOpen.IBaseCurve` 
        :returns:  The created curve type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.CurveLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddLocationFeEdges(self, indexOfDefinition: int, edges: 'list[NXOpen.CAE.FEElemEdge]') -> FeEdgesLocation:
        """
        Adds Fe Edges to connection location list  
        
        Signature ``AddLocationFeEdges(indexOfDefinition, edges)`` 
        
        :param indexOfDefinition: 
        :type indexOfDefinition: int 
        :param edges:  Edges used for location  
        :type edges: list of :py:class:`NXOpen.CAE.FEElemEdge` 
        :returns:  The created edge group type location  
        :rtype: :py:class:`NXOpen.CAE.Connections.FeEdgesLocation` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOffsetVector(self, lindeDefinitionIndex: int) -> NXOpen.Direction:
        """
        Gets the line offset vector  
        
        Signature ``GetOffsetVector(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOffsetVector(self, lindeDefinitionIndex: int, offsetvector: NXOpen.Direction) -> None:
        """
        Sets the line offset vector 
        
        Signature ``SetOffsetVector(lindeDefinitionIndex, offsetvector)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :param offsetvector: 
        :type offsetvector: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetOffsetDistance(self, lindeDefinitionIndex: int) -> NXOpen.Expression:
        """
        Gets the line offset distance  
        
        Signature ``GetOffsetDistance(lindeDefinitionIndex)`` 
        
        :param lindeDefinitionIndex: 
        :type lindeDefinitionIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Material: NXOpen.PhysicalMaterial = ...
    """
    Returns or sets  the connection material 
    
    <hr>
    
    Getter Method
    
    Signature ``Material`` 
    
    :returns:  The connection material  
    :rtype: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Material`` 
    
    :param material:  The connection material  
    :type material: :py:class:`NXOpen.PhysicalMaterial` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaxDistCGToElemCG: NXOpen.Expression = ...
    """
    Returns  the maximum distance from definition point to center of support element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDistCGToElemCG`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxNormalDistCGToFlanges: NXOpen.Expression = ...
    """
    Returns  the maximum normal distance from definition point to center of element 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxNormalDistCGToFlanges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    MaxAngleBetweenNormals: NXOpen.Expression = ...
    """
    Returns  the maximum angle of normals with the projection surface 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxAngleBetweenNormals`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ProjectTolerance: NXOpen.Expression = ...
    """
    Returns  the projection tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DiameterType: DiameterType = ...
    """
    Returns or sets  the diameter type 
    
    <hr>
    
    Getter Method
    
    Signature ``DiameterType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.DiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DiameterType`` 
    
    :param diameterType: 
    :type diameterType: :py:class:`NXOpen.CAE.Connections.DiameterType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the connection diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Coefficient: NXOpen.Expression = ...
    """
    Returns  the coefficient for formula defined diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``Coefficient`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    TableFile: str = ...
    """
    Returns or sets  the table file used to compute the diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``TableFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TableFile`` 
    
    :param tableFile:  Full path to the diameter table file.  
    :type tableFile: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    HeightType: HeightType = ...
    """
    Returns or sets  the height type 
    
    <hr>
    
    Getter Method
    
    Signature ``HeightType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeightType`` 
    
    :param heightType:  Diameter type  
    :type heightType: :py:class:`NXOpen.CAE.Connections.HeightType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height value 
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    NumberOfFlanges: int = ...
    """
    Returns or sets  the number of flanges.  
    
    When changing the number of flanges this is not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFlanges`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfFlanges`` 
    
    :param numberOfFlanges: 
    :type numberOfFlanges: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseOriginalNodesOfConnection: bool = ...
    """
    Returns or sets  the usage of original nodes of connection 
    
    <hr>
    
    Getter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseOriginalNodesOfConnection`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    UseMaxLengthStep: bool = ...
    """
    Returns or sets  the usage of max length stepype 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaxLengthStep`` 
    
    :param use: 
    :type use: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DistanceFromStart: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance from start 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromStart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    DistanceToEnd: NXOpen.Expression = ...
    """
    Returns  the line Discretization distance to end 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceToEnd`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization length step 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MaxLengthStep: NXOpen.Expression = ...
    """
    Returns  the line Discretization max length step 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxLengthStep`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: SpotWeld = ...  # unknown typename


class ElementTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementType():
    """
    Element type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "EHex8", "Hex8"
       "EHex8Spider", "Hex8 + Spider"
       "E1d", "1D"
       "E1DSpider", "1D + Spider"
       "ESpider", "Spider"
       "EBushing", "Bushing Elm"
       "ESpring", "Spring Elm"
       "EDamper", "Damper Elm"
       "ERigid", "Rigid Elm"
       "EKinematic", "Kinematic Elm"
       "ERigidConnector", "Rigid Connector"
       "ERigidRigidConnector", "Rigid Connector - Rigid Connector"
       "EInterpolationSpider", "Interpolation + Spider"
    """
    NotSet = 0  # ElementTypeMemberType
    EHex8 = 1  # ElementTypeMemberType
    EHex8Spider = 2  # ElementTypeMemberType
    E1d = 3  # ElementTypeMemberType
    E1DSpider = 4  # ElementTypeMemberType
    ESpider = 5  # ElementTypeMemberType
    EBushing = 6  # ElementTypeMemberType
    ESpring = 7  # ElementTypeMemberType
    EDamper = 8  # ElementTypeMemberType
    ERigid = 9  # ElementTypeMemberType
    EKinematic = 10  # ElementTypeMemberType
    ERigidConnector = 11  # ElementTypeMemberType
    ERigidRigidConnector = 12  # ElementTypeMemberType
    EInterpolationSpider = 13  # ElementTypeMemberType
    
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
    


class DofMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Dof():
    """
    Degrees of freedom definition 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "X Translation degree of freedom"
       "Y", "Y Translation degree of freedom"
       "Z", "Z Translation degree of freedom"
       "Rx", "X Rotation degree of freedom"
       "Ry", "Y Rotation degree of freedom"
       "Rz", "Z Rotation degree of freedom"
    """
    X = 0  # DofMemberType
    Y = 1  # DofMemberType
    Z = 2  # DofMemberType
    Rx = 3  # DofMemberType
    Ry = 4  # DofMemberType
    Rz = 5  # DofMemberType
    
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
    


class SelectionRecipeLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    SelectionRecipe: NXOpen.CAE.SelectionRecipe = ...
    """
    Returns or sets  the Selection Recipe used for creating the location.  
    
    If the location type is not a Selection Recipe, this method will raise an error. 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionRecipe`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SelectionRecipe` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionRecipe`` 
    
    :param selectionRecipe: 
    :type selectionRecipe: :py:class:`NXOpen.CAE.SelectionRecipe` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: SelectionRecipeLocation = ...  # unknown typename


class ComposerConnectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ComposerConnectionType():
    """
    composer Connection type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Bolt", "Bolt"
       "Spring", "Spring"
       "Latch", "Latch"
       "Bushing", "Bushing"
       "BumpStop", "BumpStop"
       "Kinematic", "Kinematic"
       "WeatherStrip", "WeatherStrip"
       "SeamWeld", "SeamWeld"
    """
    Bolt = 0  # ComposerConnectionTypeMemberType
    Spring = 1  # ComposerConnectionTypeMemberType
    Latch = 2  # ComposerConnectionTypeMemberType
    Bushing = 3  # ComposerConnectionTypeMemberType
    BumpStop = 4  # ComposerConnectionTypeMemberType
    Kinematic = 5  # ComposerConnectionTypeMemberType
    WeatherStrip = 6  # ComposerConnectionTypeMemberType
    SeamWeld = 7  # ComposerConnectionTypeMemberType
    
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
    


class PointSeriesLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX12.0.0
    """
    
    def GetPoints(self) -> 'list[NXOpen.Point]':
        """
        Retrieve location points.  
        
        Signature ``GetPoints()`` 
        
        :returns:  Points used for location  
        :rtype: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPoints(self, points: 'list[NXOpen.Point]') -> None:
        """
        Add location nodes.  
        
        Signature ``AddPoints(points)`` 
        
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def SetPoints(self, points: 'list[NXOpen.Point]') -> None:
        """
        Set location points.  
        
        Signature ``SetPoints(points)`` 
        
        :param points:  Points used for location  
        :type points: list of :py:class:`NXOpen.Point` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: PointSeriesLocation = ...  # unknown typename


class IStructuralDampingDynamic(NXOpen.INXObject):
    """
    This class represents an Interface to the StructuralDamping dynamic.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class INodalTargetCenter(NXOpen.INXObject):
    """
    This class represents an Interface to the Connection Target.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class NodalTargetSpider(NodalTarget, INodalTargetLegs, INodalTargetCenter):
    """
    Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetLegsEntities(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets entities from target's group of points.  
        
        These can be any combination of CAD (point, edge, face, body) or FE (node, edge, face, element and mesh) 
        objects able to return nodes.  
        
        Signature ``GetLegsEntities()`` 
        
        :returns:  Legs entities  
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddLegsEntities(self, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add entities to target's group of points.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``AddLegsEntities(entities)`` 
        
        :param entities:  Legs entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveLegsEntities(self, entities: 'list[NXOpen.TaggedObject]') -> None:
        """
        Remove entities from target's group of points.  
        
        Changes are not applied till an update is performed by calling :py:meth:`Update.DoUpdate` 
        
        Signature ``RemoveLegsEntities(entities)`` 
        
        :param entities:  Legs entities  
        :type entities: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    TargetCenter: NXOpen.TaggedObject = ...
    """
    Returns or sets  the target center 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetCenter`` 
    
    :returns:  Target center  
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetCenter`` 
    
    :param center: 
    :type center: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: NodalTargetSpider = ...  # unknown typename


class NodalTargetSinglePoint(NodalTarget, INodalTargetCenter):
    """
    Group of Points Target. Use this interface to set/get parameters of the Group of Points Target type.  
    
    .. versionadded:: NX12.0.0
    """
    TargetCenter: NXOpen.TaggedObject = ...
    """
    Returns or sets  the target center 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetCenter`` 
    
    :returns:  Target center  
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetCenter`` 
    
    :param center: 
    :type center: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: NodalTargetSinglePoint = ...  # unknown typename


class SeamWeldTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SeamWeldType():
    """
    Seam Weld Type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WithMaterial", "Seam weld done with material"
       "WithLaser", "Seam weld done by laser"
    """
    WithMaterial = 0  # SeamWeldTypeMemberType
    WithLaser = 1  # SeamWeldTypeMemberType
    
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
    


class CoordinatesLocation(Location):
    """
    Location interface. This defines connection locations with common properties like coordinates.  
    
    To obtain an instance of this object use the AddLocation creators on the Connections
    
    .. versionadded:: NX11.0.0
    """
    
    def GetCoordinates(self) -> NXOpen.Point3d:
        """
        Gets the coordinates from the specified location.  
        
        The location can be any type: coordinates, node or point.
        Its coordinates will be returned.  
        
        Signature ``GetCoordinates()`` 
        
        :returns:  Location coordinates  
        :rtype: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetCoordinates(self, coordinates: NXOpen.Point3d) -> None:
        """
        Set the coordinates.  
        
        Only for coordinates type location 
        
        Signature ``SetCoordinates(coordinates)`` 
        
        :param coordinates:  The location coordinates  
        :type coordinates: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: CoordinatesLocation = ...  # unknown typename


class Utils():
    """
    Contains universal connections utility methods   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Connections.Folder`
    
    .. versionadded:: NX12.0.0
    """
    
    def FilterConnectionsByType(self, iConnections: 'list[IConnection]', type: ConnectionType) -> 'list[IConnection]':
        """
        Filters a list of connections by type  
        
        Signature ``FilterConnectionsByType(iConnections, type)`` 
        
        :param iConnections:  The array of input connections  
        :type iConnections: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        :param type:  The connection type to filter by  
        :type type: :py:class:`NXOpen.CAE.Connections.ConnectionType` 
        :returns:  all connections matching the specified connection type  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    


class Folder(NXOpen.NXObject):
    """
    The Folder class offers a way to create a hierarchy of connections and sub-folders  
    
    To obtain an instance of this object use the add_folder creator in a parent folder or access connection root folder from :py:class:`CAE.IFEModel`
    
    .. versionadded:: NX12.0.0
    """
    
    def GetChildFolders(self) -> 'list[Folder]':
        """
        Get the child folders  
        
        Signature ``GetChildFolders()`` 
        
        :returns:  child folders 
        :rtype: list of :py:class:`NXOpen.CAE.Connections.Folder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetConnections(self) -> 'list[IConnection]':
        """
        Get the connections  
        
        Signature ``GetConnections()`` 
        
        :returns:  connections found in folder  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetAllConnections(self) -> 'list[IConnection]':
        """
        Get all the connections under this folder and its descendant folders  
        
        Signature ``GetAllConnections()`` 
        
        :returns:  all connections under this folder and its descendants  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateFolder(self, name: str) -> Folder:
        """
        Creates a :py:class:`CAE.Connections.Folder` in this folder with the specified name  
        
        Signature ``CreateFolder(name)`` 
        
        :param name:   Name that the created folder should have  
        :type name: str 
        :returns:  the created :py:class:`CAE.Connections.Folder`  
        :rtype: :py:class:`NXOpen.CAE.Connections.Folder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def AddFolder(self, subfolder: Folder) -> None:
        """
        Add a subfolder to this folder.  
        
        The subfolder is moved if found in other folder. 
        
        Signature ``AddFolder(subfolder)`` 
        
        :param subfolder:  the added folder  
        :type subfolder: :py:class:`NXOpen.CAE.Connections.Folder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def MoveConnectionToThisFolder(self, connection: IConnection) -> None:
        """
        Add a connection to this folder.  
        
        The connection is removed from previous parent folder. 
        
        Signature ``MoveConnectionToThisFolder(connection)`` 
        
        :param connection:  the connection that is moved  
        :type connection: :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def ImportSpotWeldFromWcd(self, file: str, inputFileUnit: NXOpen.Unit) -> 'list[SpotWeld]':
        """
        Create :py:class:`CAE.Connections.SpotWeld` connections in the current :py:class:`CAE.Connections.Folder` 
        using connection data imported from a WCD file.  
        
        Signature ``ImportSpotWeldFromWcd(file, inputFileUnit)`` 
        
        :param file:  name of the import file  
        :type file: str 
        :param inputFileUnit:  the length unit used in the input file  
        :type inputFileUnit: :py:class:`NXOpen.Unit` 
        :returns:  the created connections  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.SpotWeld` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def ImportConnectionsFromMcf(self, file: str, inputFileUnit: NXOpen.Unit) -> 'list[IConnection]':
        """
        Create :py:class:`CAE.Connections.IConnection` connections in the current :py:class:`CAE.Connections.Folder` 
        using connection data imported from a MCF file.  
        
        Signature ``ImportConnectionsFromMcf(file, inputFileUnit)`` 
        
        :param file:  name of the import file  
        :type file: str 
        :param inputFileUnit:  the length unit used in the input file  
        :type inputFileUnit: :py:class:`NXOpen.Unit` 
        :returns:  the created connections  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def CreateConnection(self, type: ConnectionType, name: str) -> IConnection:
        """
        Create a :py:class:`CAE.Connections.IConnection` in this folder of the specified type with the specified name  
        
        Signature ``CreateConnection(type, name)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.ConnectionType` 
        :param name:  name of the connection  
        :type name: str 
        :returns:  the created connection  
        :rtype: :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Parent: Folder = ...
    """
    Returns  the parent folder 
    
    <hr>
    
    Getter Method
    
    Signature ``Parent`` 
    
    :returns:  parent folder  
    :rtype: :py:class:`NXOpen.CAE.Connections.Folder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ConnectionUtils: Utils = ...
    """
    Returns a :py:class:`CAE.Connections.Utils` instance 
    
    Signature ``ConnectionUtils`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.Utils`
    """
    Null: Folder = ...  # unknown typename


class ConnectionDBData(NXOpen.TaggedObject):
    """
    Connection DB data.  
    
    Use this interface to set/get properties and parameters of the connection DB data.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetConnectionDBItemDatas(self) -> 'list[ConnectionDBItemData]':
        """
        Gets connection DB item datas.  
        
        Signature ``GetConnectionDBItemDatas()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Connections.ConnectionDBItemData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetConnectionDBItemDatas(self, components: 'list[ConnectionDBItemData]') -> None:
        """
        Sets connection DB item datas.  
        
        Signature ``SetConnectionDBItemDatas(components)`` 
        
        :param components: 
        :type components: list of :py:class:`NXOpen.CAE.Connections.ConnectionDBItemData` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Null: ConnectionDBData = ...  # unknown typename


class DiameterTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DiameterType():
    """
    Diameter definition types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "User", "User defined diameter"
       "Formula", "Formula defined diameter"
       "TableFile", "Table defined diameter"
    """
    User = 0  # DiameterTypeMemberType
    Formula = 1  # DiameterTypeMemberType
    TableFile = 2  # DiameterTypeMemberType
    
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
    


class ElementStatusTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElementStatusType():
    """
    Element status 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Invalid", "Invalid"
       "NotUpdated", "Not updated"
       "Updated", "Updated"
    """
    Invalid = 0  # ElementStatusTypeMemberType
    NotUpdated = 1  # ElementStatusTypeMemberType
    Updated = 2  # ElementStatusTypeMemberType
    
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
    


class ModelizationResultTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ModelizationResultType():
    """
    Modelization result type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Material", "Material"
       "Weights", "Interpolation element weights"
       "Section", "Section"
       "Csys", "Csys"
       "Stiffness", "Stiffness"
       "ViscousDamping", "ViscousDamping"
       "StructuralDamping", "StructuralDamping"
       "Dofs", "Dofs"
       "DynamicStiffness", "Dynamic Stiffness"
       "DynamicViscousDamping", "Dynamic ViscousDamping"
       "DynamicStructuralDamping", "Dynamic StructuralDamping"
    """
    NotSet = 0  # ModelizationResultTypeMemberType
    Material = 1  # ModelizationResultTypeMemberType
    Weights = 2  # ModelizationResultTypeMemberType
    Section = 3  # ModelizationResultTypeMemberType
    Csys = 4  # ModelizationResultTypeMemberType
    Stiffness = 5  # ModelizationResultTypeMemberType
    ViscousDamping = 6  # ModelizationResultTypeMemberType
    StructuralDamping = 7  # ModelizationResultTypeMemberType
    Dofs = 8  # ModelizationResultTypeMemberType
    DynamicStiffness = 9  # ModelizationResultTypeMemberType
    DynamicViscousDamping = 10  # ModelizationResultTypeMemberType
    DynamicStructuralDamping = 11  # ModelizationResultTypeMemberType
    
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
    


class NodalTargetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NodalTargetType():
    """
    Nodal Target types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SinglePoint", "Single Point"
       "SetOfPoints", "Set of Points"
       "Spider", "Spider"
       "NotSet", "None"
    """
    SinglePoint = 0  # NodalTargetTypeMemberType
    SetOfPoints = 1  # NodalTargetTypeMemberType
    Spider = 2  # NodalTargetTypeMemberType
    NotSet = 3  # NodalTargetTypeMemberType
    
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
    


class Bushing(IConnection, ICsys, IStiffness, IStructuralDamping, IViscousDamping, IStiffnessDynamic, IViscousDampingDynamic, IStructuralDampingDynamic, INodalTargetsContainer, INodalTargetsPairing):
    """
    Bushing connection.  
    
    Use this interface to set/get properties and parameters of the Bushing connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
        Set the target type 
        
        Signature ``SetTargetType(index, type)`` 
        
        :param index: 
        :type index: int 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetTarget(self, index: int) -> NodalTarget:
        """
        Get target  
        
        Signature ``GetTarget(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.NodalTarget` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    XStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the X stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Y stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the Z stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RX stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RY stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzStiffnessConstant: NXOpen.Expression = ...
    """
    Returns  the RZ stiffness constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStiffnessConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the X structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Y structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Z structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RX structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RY structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzStructuralDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RZ structural damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStructuralDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the X viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Y viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Z viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RX viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RY viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RZ viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    XStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the X stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``XStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    YStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Y stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``YStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ZStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Z stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RxStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RX stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RxStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RyStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RY stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RyStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RzStiffnessDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RZ stiffness dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStiffnessDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RzStiffnessDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    XViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the X viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``XViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    YViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Y viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``YViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ZViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Z viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``ZViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RxViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RX viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RxViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RxViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RyViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RY viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RyViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RyViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RzViscousDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RZ viscous damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RzViscousDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RzViscousDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    XStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the X structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``XStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    YStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Y structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``YStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ZStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the Z structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``ZStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RxStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RX structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RxStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RxStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RyStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RY structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RyStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RyStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    RzStructuralDampingDynamic: NXOpen.Fields.ScalarFieldWrapper = ...
    """
    Returns or sets  the RZ structural damping dynamic 
    
    <hr>
    
    Getter Method
    
    Signature ``RzStructuralDampingDynamic`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RzStructuralDampingDynamic`` 
    
    :param bridge: 
    :type bridge: :py:class:`NXOpen.Fields.ScalarFieldWrapper` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PairingMethod: NodalPairingMethod = ...
    """
    Returns or sets  the pairing method of targets 
    
    <hr>
    
    Getter Method
    
    Signature ``PairingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PairingMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchOrientation: NXOpen.Direction = ...
    """
    Returns or sets  the pairing search orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchConeAngle: NXOpen.Expression = ...
    """
    Returns  the search cone angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchConeAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SearchRange: NXOpen.Expression = ...
    """
    Returns  the search range 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Bushing = ...  # unknown typename


class CsysTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CsysType():
    """
    Csys types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Existing", "Existing CSYS"
       "Predefined", "Predefined CSYS"
       "Absolute", "Absolute CSYS"
       "LocalCartesian", "Local Cartesian CSYS"
       "LocalCylindrical", "Local Cylindrical CSYS"
       "LocalSpherical", "Local Spherical CSYS"
    """
    Existing = 0  # CsysTypeMemberType
    Predefined = 1  # CsysTypeMemberType
    Absolute = 2  # CsysTypeMemberType
    LocalCartesian = 3  # CsysTypeMemberType
    LocalCylindrical = 4  # CsysTypeMemberType
    LocalSpherical = 5  # CsysTypeMemberType
    
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
    


class Element(NXOpen.CAE.NamedPropertyTable, NXOpen.CAE.IExportableFEEntity):
    """
    This is the class to access a connection element  
    
    To obtain an instance of this object use the Create creator in :py:class:`CAE.Connections.ElementCollection`.
    
    .. versionadded:: NX12.0.0
    """
    
    def AddConnections(self, connections: 'list[IConnection]') -> None:
        """
        Adds connections to this element
        
        Signature ``AddConnections(connections)`` 
        
        :param connections: 
        :type connections: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def RemoveConnections(self, connections: 'list[IConnection]') -> None:
        """
        Removes a connection from this element.  
        
        This does not delete/destroy the connection, instead
        this element will no longer keep a reference to the connection.
        
        Signature ``RemoveConnections(connections)`` 
        
        :param connections: 
        :type connections: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetConnections(self) -> 'list[IConnection]':
        """
        Gets connections from this element
        
        Signature ``GetConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Connections.IConnection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GenerateElements(self) -> None:
        """
        Mesh the Connection Element.  
        
        Signature ``GenerateElements()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetSolverCardSyntax(self) -> 'list[str]':
        """
        Returns the solver card syntax strings for this entity.  
        
        Signature ``GetSolverCardSyntax()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    IsCompatibleType: bool = ...
    """
    Returns  the compatibility of the element
    (whether it accepts compatible or incompatible meshes)
    
    <hr>
    
    Getter Method
    
    Signature ``IsCompatibleType`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MinBarLength: NXOpen.Expression = ...
    """
    Returns the min bar length.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinBarLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Status: ElementStatusType = ...
    """
    Returns the status of the element
    
    <hr>
    
    Getter Method
    
    Signature ``Status`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ElementStatusType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Type: ElementType = ...
    """
    Returns the type of the element
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ElementType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: Element = ...  # unknown typename


class Damper(IConnection, IViscousDamping, ICsys, INodalTargetsContainer, INodalTargetsPairing):
    """
    Damper connection.  
    
    Use this interface to set/get properties and parameters of the Damper connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetSupportedCsysTypes(self) -> 'list[CsysType]':
        """
        Gets supported csys types of connection.  
        
        Signature ``GetSupportedCsysTypes()`` 
        
        :returns:  Supported CSys Types  
        :rtype: list of :py:class:`NXOpen.CAE.Connections.CsysType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTargetType(self, index: int, type: NodalTargetType) -> None:
        """
        Set the target type 
        
        Signature ``SetTargetType(index, type)`` 
        
        :param index: 
        :type index: int 
        :param type: 
        :type type: :py:class:`NXOpen.CAE.Connections.NodalTargetType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetTarget(self, index: int) -> NodalTarget:
        """
        Get target  
        
        Signature ``GetTarget(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Connections.NodalTarget` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    XViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the X viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``XViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    YViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Y viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``YViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    ZViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the Z viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``ZViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RxViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RX viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RxViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RyViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RY viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RyViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    RzViscousDampingConstant: NXOpen.Expression = ...
    """
    Returns  the RZ viscous damping constant 
    
    <hr>
    
    Getter Method
    
    Signature ``RzViscousDampingConstant`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CsysType: CsysType = ...
    """
    Returns or sets  the csys type 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CsysType`` 
    
    :param csysType: 
    :type csysType: :py:class:`NXOpen.CAE.Connections.CsysType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Csys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    PairingMethod: NodalPairingMethod = ...
    """
    Returns or sets  the pairing method of targets 
    
    <hr>
    
    Getter Method
    
    Signature ``PairingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PairingMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.CAE.Connections.NodalPairingMethod` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchOrientation: NXOpen.Direction = ...
    """
    Returns or sets  the pairing search orientation 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchOrientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchConeAngle: NXOpen.Expression = ...
    """
    Returns  the search cone angle 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchConeAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SearchRange: NXOpen.Expression = ...
    """
    Returns  the search range 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchRange`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: Damper = ...  # unknown typename


class ConnectionData(NXOpen.TaggedObject):
    """
    Composer connection.  
    
    Use this interface to set/get properties and parameters of the spot weld connection.  
    
    .. versionadded:: NX12.0.0
    """
    
    def GetPointNameCoord1(self) -> 'list[str]':
        """
        Get point name coord1   
        
        Signature ``GetPointNameCoord1()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPointNameCoord1(self, pointNameCoord1s: 'list[str]') -> None:
        """
        Set point name coord1  
        
        Signature ``SetPointNameCoord1(pointNameCoord1s)`` 
        
        :param pointNameCoord1s: 
        :type pointNameCoord1s: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPointNameCoord2(self) -> 'list[str]':
        """
        Get point name coord2   
        
        Signature ``GetPointNameCoord2()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPointNameCoord2(self, pointNameCoord2s: 'list[str]') -> None:
        """
        Set point name coord2  
        
        Signature ``SetPointNameCoord2(pointNameCoord2s)`` 
        
        :param pointNameCoord2s: 
        :type pointNameCoord2s: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPointNameCoord3(self) -> 'list[str]':
        """
        Get point name coord3   
        
        Signature ``GetPointNameCoord3()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPointNameCoord3(self, pointNameCoord3s: 'list[str]') -> None:
        """
        Set point name coord3  
        
        Signature ``SetPointNameCoord3(pointNameCoord3s)`` 
        
        :param pointNameCoord3s: 
        :type pointNameCoord3s: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPID1s(self) -> 'list[NXOpen.TaggedObject]':
        """
        Get pID1s  
        
        Signature ``GetPID1s()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPID1s(self, pID1s: 'list[NXOpen.TaggedObject]') -> None:
        """
        Set pID1s 
        
        Signature ``SetPID1s(pID1s)`` 
        
        :param pID1s: 
        :type pID1s: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPID2s(self) -> 'list[NXOpen.TaggedObject]':
        """
        Get pID2s  
        
        Signature ``GetPID2s()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPID2s(self, pID2s: 'list[NXOpen.TaggedObject]') -> None:
        """
        Set pID2s 
        
        Signature ``SetPID2s(pID2s)`` 
        
        :param pID2s: 
        :type pID2s: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetPID3s(self) -> 'list[NXOpen.TaggedObject]':
        """
        Get pID3s  
        
        Signature ``GetPID3s()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetPID3s(self, pID3s: 'list[NXOpen.TaggedObject]') -> None:
        """
        Set pID3s 
        
        Signature ``SetPID3s(pID3s)`` 
        
        :param pID3s: 
        :type pID3s: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetAxis(self) -> str:
        """
        Gets axis.  
        
        Signature ``GetAxis()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAxis(self, axis: str) -> None:
        """
        Sets axis.  
        
        Signature ``SetAxis(axis)`` 
        
        :param axis: 
        :type axis: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLineFEEdgeRecipe1(self) -> 'list[str]':
        """
        Get line / FE edge recipe1   
        
        Signature ``GetLineFEEdgeRecipe1()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLineFEEdgeRecipe1(self, lineFEEdgeRecipe1s: 'list[str]') -> None:
        """
        Set line / FE edge recipe1  
        
        Signature ``SetLineFEEdgeRecipe1(lineFEEdgeRecipe1s)`` 
        
        :param lineFEEdgeRecipe1s: 
        :type lineFEEdgeRecipe1s: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    
    def GetLineFEEdgeRecipe2(self) -> 'list[str]':
        """
        Get line / FE edge recipe2   
        
        Signature ``GetLineFEEdgeRecipe2()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLineFEEdgeRecipe2(self, lineFEEdgeRecipe2s: 'list[str]') -> None:
        """
        Set line / FE edge recipe1  
        
        Signature ``SetLineFEEdgeRecipe2(lineFEEdgeRecipe2s)`` 
        
        :param lineFEEdgeRecipe2s: 
        :type lineFEEdgeRecipe2s: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling")
        """
        ...
    
    Comp1: ComponentData = ...
    """
    Returns or sets  the comp1  
    
    <hr>
    
    Getter Method
    
    Signature ``Comp1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Comp1`` 
    
    :param comp1: 
    :type comp1: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Comp2: ComponentData = ...
    """
    Returns or sets  the comp2  
    
    <hr>
    
    Getter Method
    
    Signature ``Comp2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Comp2`` 
    
    :param comp2: 
    :type comp2: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Comp3: ComponentData = ...
    """
    Returns or sets  the comp3  
    
    <hr>
    
    Getter Method
    
    Signature ``Comp3`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Comp3`` 
    
    :param comp3: 
    :type comp3: :py:class:`NXOpen.CAE.Connections.ComponentData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ConnectionType: ComposerConnectionType = ...
    """
    Returns or sets  the connection type  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ComposerConnectionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectionType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.CAE.Connections.ComposerConnectionType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    DBItem: ConnectionDBItemData = ...
    """
    Returns or sets  the db item  
    
    <hr>
    
    Getter Method
    
    Signature ``DBItem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Connections.ConnectionDBItemData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DBItem`` 
    
    :param dbItem: 
    :type dbItem: :py:class:`NXOpen.CAE.Connections.ConnectionDBItemData` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof1: bool = ...
    """
    Returns or sets  the dof1 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof1`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof2: bool = ...
    """
    Returns or sets  the dof2 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof2`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof3: bool = ...
    """
    Returns or sets  the dof3 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof3`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof3`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof4: bool = ...
    """
    Returns or sets  the dof4 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof4`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof4`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof5: bool = ...
    """
    Returns or sets  the dof5 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof5`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof5`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Dof6: bool = ...
    """
    Returns or sets  the dof6 
    
    <hr>
    
    Getter Method
    
    Signature ``Dof6`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dof6`` 
    
    :param name: 
    :type name: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ExpansionRadius1: float = ...
    """
    Returns or sets  the expansion radius1 
    
    <hr>
    
    Getter Method
    
    Signature ``ExpansionRadius1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpansionRadius1`` 
    
    :param expansionRadius1: 
    :type expansionRadius1: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ExpansionRadius2: float = ...
    """
    Returns or sets  the expansion radius2 
    
    <hr>
    
    Getter Method
    
    Signature ``ExpansionRadius2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpansionRadius2`` 
    
    :param expansionRadius2: 
    :type expansionRadius2: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ExpansionRadiusFactor1: float = ...
    """
    Returns or sets  the expansion radius factor1 
    
    <hr>
    
    Getter Method
    
    Signature ``ExpansionRadiusFactor1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpansionRadiusFactor1`` 
    
    :param expansionRadiusFactor1: 
    :type expansionRadiusFactor1: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ExpansionRadiusFactor2: float = ...
    """
    Returns or sets  the expansion radius factor2 
    
    <hr>
    
    Getter Method
    
    Signature ``ExpansionRadiusFactor2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpansionRadiusFactor2`` 
    
    :param expansionRadiusFactor2: 
    :type expansionRadiusFactor2: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    FlangeSearchTolerance1: float = ...
    """
    Returns or sets  the expansion radius factor1 
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeSearchTolerance1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlangeSearchTolerance1`` 
    
    :param flangeSearchTolerance1: 
    :type flangeSearchTolerance1: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    FlangeSearchTolerance2: float = ...
    """
    Returns or sets  the expansion radius factor2 
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeSearchTolerance2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlangeSearchTolerance2`` 
    
    :param flangeSearchTolerance2: 
    :type flangeSearchTolerance2: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    FlangeType1: str = ...
    """
    Returns or sets  the flange type1  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeType1`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlangeType1`` 
    
    :param flangeType1: 
    :type flangeType1: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    FlangeType2: str = ...
    """
    Returns or sets  the flange type2  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeType2`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlangeType2`` 
    
    :param flangeType2: 
    :type flangeType2: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    HeadDiameter: float = ...
    """
    Returns or sets  the head diameter  
    
    <hr>
    
    Getter Method
    
    Signature ``HeadDiameter`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeadDiameter`` 
    
    :param headDiameter: 
    :type headDiameter: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LengthStep: float = ...
    """
    Returns or sets  the expansion radius factor2 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthStep`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LengthStep`` 
    
    :param lengthStep: 
    :type lengthStep: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LinePart1: str = ...
    """
    Returns or sets  the line part1  
    
    <hr>
    
    Getter Method
    
    Signature ``LinePart1`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LinePart1`` 
    
    :param linePart: 
    :type linePart: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    LinePart2: str = ...
    """
    Returns or sets  the line part2  
    
    <hr>
    
    Getter Method
    
    Signature ``LinePart2`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LinePart2`` 
    
    :param linePart: 
    :type linePart: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaximumDistanceTolerance1: float = ...
    """
    Returns or sets  the maximum distance tolerance1  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumDistanceTolerance1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumDistanceTolerance1`` 
    
    :param maximumDistanceTolerance1: 
    :type maximumDistanceTolerance1: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    MaximumDistanceTolerance2: float = ...
    """
    Returns or sets  the maximum distance tolerance2  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumDistanceTolerance2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumDistanceTolerance2`` 
    
    :param maximumDistanceTolerance2: 
    :type maximumDistanceTolerance2: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Name: str = ...
    """
    Returns or sets  the assembly name  
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchType1: str = ...
    """
    Returns or sets  the search type1  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchType1`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchType1`` 
    
    :param searchType1: 
    :type searchType1: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    SearchType2: str = ...
    """
    Returns or sets  the search type2  
    
    <hr>
    
    Getter Method
    
    Signature ``SearchType2`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SearchType2`` 
    
    :param searchType2: 
    :type searchType2: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    ShankDiameter: float = ...
    """
    Returns or sets  the shank diameter  
    
    <hr>
    
    Getter Method
    
    Signature ``ShankDiameter`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShankDiameter`` 
    
    :param shankDiameter: 
    :type shankDiameter: float 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling")
    """
    Null: ConnectionData = ...  # unknown typename


class HeightTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HeightType():
    """
    Types of height definitions 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Undefined", "Undefined height type, used for connections that don't use this parameter"
       "User", "User defined thickness"
       "MeanOfFlangesThickness", "Mean of flanges thickness"
       "DistanceBetweenFlanges", "Distance between flanges"
       "DistanceBetweenFlangesMeanOfFlangesThickness", "Distance between flanges - Mean of flanges thickness"
       "DistanceBetweenFlangesMaxOfFlangesThickness", "Distance between flanges - Max of flanges thickness"
    """
    Undefined = -1  # HeightTypeMemberType
    User = 0  # HeightTypeMemberType
    MeanOfFlangesThickness = 1  # HeightTypeMemberType
    DistanceBetweenFlanges = 2  # HeightTypeMemberType
    DistanceBetweenFlangesMeanOfFlangesThickness = 3  # HeightTypeMemberType
    DistanceBetweenFlangesMaxOfFlangesThickness = 4  # HeightTypeMemberType
    
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
    


class SeamWeldMaterialTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SeamWeldMaterialType():
    """
    Seam Weld Material type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Angle", "Seam weld angle material type"
       "Overlap", "Seam weld overlap material type"
       "Double", "Seam weld double material type"
    """
    Angle = 0  # SeamWeldMaterialTypeMemberType
    Overlap = 1  # SeamWeldMaterialTypeMemberType
    Double = 2  # SeamWeldMaterialTypeMemberType
    
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
    


