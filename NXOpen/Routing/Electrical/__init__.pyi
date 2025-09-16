# module 'NXOpen.Routing.Electrical'
#
# Automatically generated 2025-06-09T14:38:47.454797
#

import typing

import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing



class CableDefinition(NXOpen.Routing.AssemblyDefinition):
    """
    Holds the collection of wires in a :py:class:`NXOpen.Routing.Electrical.CableDevice`.  
    
    A cable consists of both a :py:class:`NXOpen.Routing.Electrical.CableDevice`
    and a :py:class:`NXOpen.Routing.Electrical.CableDefinition`.
    A :py:class:`NXOpen.Routing.Electrical.CableDevice` object uses a 
    :py:class:`NXOpen.Routing.Electrical.CableDefinition` to hold
    a collection of :py:class:`NXOpen.Routing.Electrical.WireDevice` objects and/or
    :py:class:`NXOpen.Routing.Electrical.CableDevice` objects contained
    by the cable. This definition corresponds to AP212 Assembly_definition.
    
    See the NX Routing help for detailed information on the Connection data model.
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: CableDefinition = ...  # unknown typename


class ShieldDefinition(CableDefinition):
    """
    Represents Routing Electrical ShieldDefinition object   
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: ShieldDefinition = ...  # unknown typename


class PathConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    A collection of :py:class:`NXOpen.Routing.Electrical.PathConnection` objects.
    
    See NX Open Routing help for detailed information on the Connection data model.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreatePathConnection(self) -> PathConnection:
        """
        Create a :py:class:`NXOpen.Routing.Electrical.PathConnection` object.  
        
        Signature ``CreatePathConnection()`` 
        
        :returns:  A :py:class:`NXOpen.Routing.Electrical.PathConnection`  
        :rtype: :py:class:`NXOpen.Routing.Electrical.PathConnection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class PathArrangementBuilder(NXOpen.Builder):
    """
    Builder class to manage Path Arrangements.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.RouteManager.CreatePathArrangementBuilder`
    
    .. versionadded:: NX10.0.3
    """
    
    def ClearHarnessData(self) -> None:
        """
        Clears the builder data associated with stored harness, namely the ReferencePort and
        * the HarnessOccurrence, along with internal data.  
        
        Note that the PrototypePortPartOccurrence
        * and the PrototypePort are not cleared with this call.  
        
        Signature ``ClearHarnessData()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def DeletePathArrangement(self) -> None:
        """
        Deletes path arrangement through builder 
        
        Signature ``DeletePathArrangement()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def EstablishPathArrangement(self) -> None:
        """
        Retrieves the Path Arrangement object based on the data stored in the builder.  
        
        If one does not
        yet exist, a new one will be created. The retrieved object is stored internally in the biuilder.
        This method is called after setting HarnessPartOccurrence and ReferencePort 
        
        Signature ``EstablishPathArrangement()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetPathArrangementOrigin(self, point: NXOpen.Point3d) -> None:
        """
        Sets a new origin for the point on the harness path.  
        
        This point should be in the
        context of the current root part. 
        
        Signature ``SetPathArrangementOrigin(point)`` 
        
        :param point:  Origin of the path arrangement in the context of the root part.  
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def InitializeBuilderFromArrangedPort(self, port: NXOpen.Routing.Port) -> None:
        """
        Initializes builder from arranged port 
        
        Signature ``InitializeBuilderFromArrangedPort(port)`` 
        
        :param port:  Routing port whose associated path arrangement object is used to populate the data in the builder  
        :type port: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    HarnessPartOccurrence: NXOpen.Assemblies.Component = ...
    """
    Returns or sets  the harness component in the context of the part that was used to create the extracted port.  
    
    <hr>
    
    Getter Method
    
    Signature ``HarnessPartOccurrence`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``HarnessPartOccurrence`` 
    
    :param partOcc: 
    :type partOcc: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    """
    PrototypePort: NXOpen.Routing.Port = ...
    """
    Returns or sets  the prototype of the extract port that is used as the reference port.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrototypePort`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.Port` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PrototypePort`` 
    
    :param port: 
    :type port: :py:class:`NXOpen.Routing.Port` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    """
    PrototypePortPartOccurrence: NXOpen.Assemblies.Component = ...
    """
    Returns or sets  the component part that contains the prototype of the extract port that is used as the reference
    port.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrototypePortPartOccurrence`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PrototypePortPartOccurrence`` 
    
    :param partOcc: 
    :type partOcc: :py:class:`NXOpen.Assemblies.Component` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    """
    ReferencePort: NXOpen.TaggedObject = ...
    """
    Returns or sets  the port on which the offset is based when defining the path arrangement.  
    
    The port property
    can be either a port or a port occurrence. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencePort`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencePort`` 
    
    :param port: 
    :type port: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: PathArrangementBuilder = ...  # unknown typename


class ElectricalStockDeviceRouteTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElectricalStockDeviceRouteTypes():
    """
    Route types (manual/auto). 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DefaultRoute", " - "
       "AutoRoute", " - "
       "ManualRoute", " - "
    """
    DefaultRoute = -1  # ElectricalStockDeviceRouteTypesMemberType
    AutoRoute = 0  # ElectricalStockDeviceRouteTypesMemberType
    ManualRoute = 1  # ElectricalStockDeviceRouteTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ElectricalStockDeviceRouteLevelMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElectricalStockDeviceRouteLevel():
    """
    Routing level. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pin", " - "
       "Comp", " - "
       "Mixed", " - "
       "Partial", " - "
    """
    Pin = 0  # ElectricalStockDeviceRouteLevelMemberType
    Comp = 1  # ElectricalStockDeviceRouteLevelMemberType
    Mixed = 2  # ElectricalStockDeviceRouteLevelMemberType
    Partial = 3  # ElectricalStockDeviceRouteLevelMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ElectricalStockDeviceAutoRouteSelMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElectricalStockDeviceAutoRouteSel():
    """
    Auto-route selections. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BundleDiameter", " - "
       "LeastBundles", " - "
       "DesignRules", " - "
       "LeastSegments", " - "
       "ShortestLength", " - "
    """
    BundleDiameter = 0  # ElectricalStockDeviceAutoRouteSelMemberType
    LeastBundles = 1  # ElectricalStockDeviceAutoRouteSelMemberType
    DesignRules = 2  # ElectricalStockDeviceAutoRouteSelMemberType
    LeastSegments = 3  # ElectricalStockDeviceAutoRouteSelMemberType
    ShortestLength = 4  # ElectricalStockDeviceAutoRouteSelMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ElectricalStockDevice(NXOpen.Routing.StockDevice):
    """
    The Electrical Stock Device is a non instantiable superclass to classify
    all electrical stock-based single devices.  
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    
    class RouteTypes():
        """
        Route types (manual/auto). 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DefaultRoute", " - "
           "AutoRoute", " - "
           "ManualRoute", " - "
        """
        DefaultRoute = -1  # ElectricalStockDeviceRouteTypesMemberType
        AutoRoute = 0  # ElectricalStockDeviceRouteTypesMemberType
        ManualRoute = 1  # ElectricalStockDeviceRouteTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class RouteLevel():
        """
        Routing level. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pin", " - "
           "Comp", " - "
           "Mixed", " - "
           "Partial", " - "
        """
        Pin = 0  # ElectricalStockDeviceRouteLevelMemberType
        Comp = 1  # ElectricalStockDeviceRouteLevelMemberType
        Mixed = 2  # ElectricalStockDeviceRouteLevelMemberType
        Partial = 3  # ElectricalStockDeviceRouteLevelMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AutoRouteSel():
        """
        Auto-route selections. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BundleDiameter", " - "
           "LeastBundles", " - "
           "DesignRules", " - "
           "LeastSegments", " - "
           "ShortestLength", " - "
        """
        BundleDiameter = 0  # ElectricalStockDeviceAutoRouteSelMemberType
        LeastBundles = 1  # ElectricalStockDeviceAutoRouteSelMemberType
        DesignRules = 2  # ElectricalStockDeviceAutoRouteSelMemberType
        LeastSegments = 3  # ElectricalStockDeviceAutoRouteSelMemberType
        ShortestLength = 4  # ElectricalStockDeviceAutoRouteSelMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CalculateCutLength(self) -> float:
        """
        Calculates and sets cut length on object.  
        
        Signature ``CalculateCutLength()`` 
        
        :returns:  Calculated cut length  
        :rtype: float 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestHarnessDefinition(self) -> HarnessDefinition:
        """
        Get nearest :py:class:`NXOpen.Routing.Electrical.HarnessDefinition` encountered up the parent-child hierarchy.  
        
        Signature ``FindNearestHarnessDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDefinition` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindTopmostCableDefinition(self) -> CableDefinition:
        """
        Get topmost :py:class:`NXOpen.Routing.Electrical.CableDefinition` encountered up the parent-child hierarchy.  
        
        Signature ``FindTopmostCableDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableDefinition` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindFromConnector(self) -> ConnectorDevice:
        """
        Find the from connector for this stock device.  
        
        If there is no
        from connector, None is returned.  
        
        Signature ``FindFromConnector()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindToConnector(self) -> ConnectorDevice:
        """
        Find the to connector for this stock device.  
        
        If there is no
        to connector, None is returned.  
        
        Signature ``FindToConnector()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
        Find the nearest :py:class:`NXOpen.Routing.Electrical.HarnessDevice` encountered up the parent-child hierarchy.  
        
        Signature ``FindNearestHarnessDevice()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindImplementedConnection(self) -> Connection:
        """
        Find the :py:class:`NXOpen.Routing.Electrical.Connection` implemented by this device.  
        
        Signature ``FindImplementedConnection()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.Connection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def HasIntermediateComponents(self) -> bool:
        """
        Does this stock device have intermediate components?  
        
        Signature ``HasIntermediateComponents()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetIntermediateComponents(self) -> 'list[ConnectorDevice]':
        """
        Get intermediate components  
        
        Signature ``GetIntermediateComponents()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetIntermediateTerminals(self) -> 'list[NXOpen.Routing.LogicalTerminal]':
        """
        Get the intermediate terminals associated to this stock device.  
        
        Signature ``GetIntermediateTerminals()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.LogicalTerminal` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ManuallyRoute(self, routeLevel: ElectricalStockDeviceRouteLevel, segments: 'list[NXOpen.Routing.ISegment]') -> None:
        """
        Manually routes a :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice`.  
        
        on given :py:class:`NXOpen.Routing.ISegment`. The input segments should form a continuous 
        path between two :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` objects. 
        
        Signature ``ManuallyRoute(routeLevel, segments)`` 
        
        :param routeLevel:  Routing type.  
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceRouteLevel` 
        :param segments: 
        :type segments: list of :py:class:`NXOpen.Routing.ISegment` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ChangeHarness(self, harnessDevice: HarnessDevice) -> None:
        """
        Adds this stockdevice as child of given HarnessDevice.  
        
        Signature ``ChangeHarness(harnessDevice)`` 
        
        :param harnessDevice: 
        :type harnessDevice: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    ColorName: str = ...
    """
    Returns or sets  the color name.  
    
    <hr>
    
    Getter Method
    
    Signature ``ColorName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ColorName`` 
    
    :param colorName: 
    :type colorName: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    CutLength: float = ...
    """
    Returns or sets  the cut length.  
    
    <hr>
    
    Getter Method
    
    Signature ``CutLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CutLength`` 
    
    :param cutLength: 
    :type cutLength: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    NxColorValue: int = ...
    """
    Returns or sets  the NX color value.  
    
    <hr>
    
    Getter Method
    
    Signature ``NxColorValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``NxColorValue`` 
    
    :param nxColorValue: 
    :type nxColorValue: int 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: ElectricalStockDevice = ...  # unknown typename


class CableDevice(ElectricalStockDevice):
    """
    Corresponds to a cable instance of an :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice`.  
    
    A cable consists of both a :py:class:`NXOpen.Routing.Electrical.CableDevice`
    and a :py:class:`NXOpen.Routing.Electrical.CableDefinition`.
    A :py:class:`NXOpen.Routing.Electrical.CableDevice` object uses a 
    :py:class:`NXOpen.Routing.Electrical.CableDefinition` to hold
    a collection of :py:class:`NXOpen.Routing.Electrical.WireDevice` objects and/or
    :py:class:`NXOpen.Routing.Electrical.CableDevice` objects contained
    by the cable.
    
    See the NX Routing help for detailed information on the Connection data model.
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    
    def GetAssemblyDefinition(self) -> CableDefinition:
        """
        Returns the associated :py:class:`NXOpen.Routing.Electrical.CableDefinition`.  
        
        Signature ``GetAssemblyDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableDefinition` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ImportCablePart(self, partName: str) -> None:
        """
        Loads the given cable part and imports the connections from given part and adds them as
        children to the :py:class:`NXOpen.Routing.Electrical.CableDevice`.  
        
        Signature ``ImportCablePart(partName)`` 
        
        :param partName: Must be fullpath and PART_NAME for a regular part and PART_NAME for                       part family or part table parts 
        :type partName: str 
        
        .. versionadded:: NX6.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetConduitPartNumber(self) -> str:
        """
        Returns the part number of the conduit applied over this :py:class:`NXOpen.Routing.Electrical.CableDevice`
        object.  
        
        Signature ``GetConduitPartNumber()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def SetConduitPartNumber(self, conduitPartNumber: str) -> None:
        """
        Sets the part number of the conduit to be applied over this :py:class:`NXOpen.Routing.Electrical.CableDevice`
        object.  
        
        Signature ``SetConduitPartNumber(conduitPartNumber)`` 
        
        :param conduitPartNumber: 
        :type conduitPartNumber: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: CableDevice = ...  # unknown typename


class ShieldDevice(CableDevice):
    """
    The Electrical ShieldDevice corresponds to a shield instance of
    :py:class:`Routing.Electrical.ElectricalStockDevice`.  
    
    An electrical shield device is both an assembly definition and a electrical stock device.
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: ShieldDevice = ...  # unknown typename


class ConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.Connection` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.3
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def GetConnections(self) -> 'list[Connection]':
        """
        Get Connections  
        
        Signature ``GetConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.Connection` 
        
        .. versionadded:: NX4.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class ConnectionRouteLevelMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectionRouteLevel():
    """
    Routing level. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotRouted", " - "
       "Pin", "Route to the pin on the connector component."
       "Component", "Route to the connector component directly without regard for the pins."
       "Mixed", "Route to the pin, if possible, otherwise route to the component."
    """
    NotRouted = 0  # ConnectionRouteLevelMemberType
    Pin = 1  # ConnectionRouteLevelMemberType
    Component = 2  # ConnectionRouteLevelMemberType
    Mixed = 3  # ConnectionRouteLevelMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Connection(NXOpen.Routing.LogicalConnection):
    """
    The electrical usage of a :py:class:`NXOpen.Routing.LogicalConnection`, restricted to
    one From and one To terminal.
    
    See NX Open Routing help for detailed information on the Connection data model.
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    
    class RouteLevel():
        """
        Routing level. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotRouted", " - "
           "Pin", "Route to the pin on the connector component."
           "Component", "Route to the connector component directly without regard for the pins."
           "Mixed", "Route to the pin, if possible, otherwise route to the component."
        """
        NotRouted = 0  # ConnectionRouteLevelMemberType
        Pin = 1  # ConnectionRouteLevelMemberType
        Component = 2  # ConnectionRouteLevelMemberType
        Mixed = 3  # ConnectionRouteLevelMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetIntermediateTerminals(self) -> 'list[NXOpen.Routing.LogicalTerminal]':
        """
        Get the intermediate terminals associated with this connection.  
        
        Intermediate Terminals are
        optional and need not exist for a :py:class:`NXOpen.Routing.Electrical.Connection` to be valid in NX. 
        
        Signature ``GetIntermediateTerminals()`` 
        
        :returns:  Collection of intermediate :py:class:`NXOpen.Routing.LogicalTerminal` - May be None 
        :rtype: list of :py:class:`NXOpen.Routing.LogicalTerminal` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ReplaceIntermediateTerminals(self, intermediateTerminals: 'list[NXOpen.Routing.LogicalTerminal]') -> None:
        """
        Replaces the intermediate terminals associated with this connection.  
        
        Signature ``ReplaceIntermediateTerminals(intermediateTerminals)`` 
        
        :param intermediateTerminals:  Collection of intermediate :py:class:`NXOpen.Routing.LogicalTerminal` - Use None to remove all intermdiate terminals  
        :type intermediateTerminals: list of :py:class:`NXOpen.Routing.LogicalTerminal` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AddIntermediateTerminal(self, intermediateTerminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
        Add an intermediate terminal to this connection 
        
        Signature ``AddIntermediateTerminal(intermediateTerminal)`` 
        
        :param intermediateTerminal:  Can not be None  
        :type intermediateTerminal: :py:class:`NXOpen.Routing.LogicalTerminal` 
        :returns:  Was the :py:class:`NXOpen.Routing.LogicalTerminal` added successfully?   
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def RemoveIntermediateTerminal(self, intermediateTerminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
        Remove an intermediate terminal from this connection 
        
        Signature ``RemoveIntermediateTerminal(intermediateTerminal)`` 
        
        :param intermediateTerminal:  may be None  
        :type intermediateTerminal: :py:class:`NXOpen.Routing.LogicalTerminal` 
        :returns:  Was the :py:class:`NXOpen.Routing.LogicalTerminal` removed successfully?   
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetRoutingMethod(self) -> str:
        """
        Gets the method used to route this connection.  
        
        Signature ``GetRoutingMethod()`` 
        
        :returns:  
          * "A" Connection is auto routed
          * "M" Connection is manual routed
          * "N" Connection is not routed
        
        :rtype: str 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetRoutedLevel(self) -> str:
        """
        Gets the level used to route this connection.  
        
        Signature ``GetRoutedLevel()`` 
        
        :returns:  
          * "C" Connection routed at component level
          * "P" Connection routed at pin level
          * "M" Connection routed at mixed level
        
        :rtype: str 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetRoutedLevelEnum(self) -> ConnectionRouteLevel:
        """
        Similar to :py:meth:`NXOpen.Routing.Electrical.Connection.GetRoutedLevel`,
        but returns the :py:class:`NXOpen.Routing.Electrical.ConnectionRouteLevel` enumeration instead of a string.  
        
        Signature ``GetRoutedLevelEnum()`` 
        
        :returns:  Route level.  
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectionRouteLevel` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def IsRouted(self) -> bool:
        """
        Is this connection routed?  
        
        Signature ``IsRouted()`` 
        
        :returns:  Is this connection routed?  
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestParentDevice(self) -> NXOpen.Routing.SingleDevice:
        """
        Queries this connection for the nearest parent device.  
        
        The nearest parent device is either
        a cable, shield, or harness   
        
        Signature ``FindNearestParentDevice()`` 
        
        :returns:  Will be None if connection is not in a harness, cable, or shield.  
        :rtype: :py:class:`NXOpen.Routing.SingleDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
        Query this connection to find the nearest harness.  
        
        Only finds a harness that is a parent to this connection at some level up the connection heirarchy.  
        
        Signature ``FindNearestHarnessDevice()`` 
        
        :returns:  May be None if connection is not in a harness  
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestCableDevice(self) -> CableDevice:
        """
        Query this connection to find the nearest harness.  
        
        Only finds a cable that is a parent to this connection at some level up the connection heirarchy. 
        
        Signature ``FindNearestCableDevice()`` 
        
        :returns:  Will be None if connection is not in a cable  
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindFromConnector(self) -> ConnectorDevice:
        """
        Get the From Connector for this connection.  
        
        From does not imply an ordering.  
        
        Signature ``FindFromConnector()`` 
        
        :returns:  May be None   
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindToConnector(self) -> ConnectorDevice:
        """
        Get the To Connector for this connection.  
        
        To does not imply an ordering  
        
        Signature ``FindToConnector()`` 
        
        :returns:  May be None  
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindPaths(self, routeLevel: ConnectionRouteLevel) -> 'list[NXOpen.Routing.Path]':
        """
        Returns all the possible paths this connection can use.  
        
        Signature ``FindPaths(routeLevel)`` 
        
        :param routeLevel: 
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ConnectionRouteLevel` 
        :returns:  Possible paths this connection can use.  
        :rtype: list of :py:class:`NXOpen.Routing.Path` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def Unroute(self) -> None:
        """
        Unroutes this connection.  
        
        Signature ``Unroute()`` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AutomaticallyRoute(self, routeLevel: ConnectionRouteLevel) -> None:
        """
        Automatically routes this connection on the shortest path using the given routing level.  
        
        Signature ``AutomaticallyRoute(routeLevel)`` 
        
        :param routeLevel: 
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ConnectionRouteLevel` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AssignPath(self, routeLevel: ConnectionRouteLevel, path: NXOpen.Routing.Path) -> None:
        """
        Assigns the given path to this connection and routes the connection on the path using the given routing level.  
        
        Use :py:meth:`NXOpen.Routing.Electrical.Connection.FindPaths` to find all available paths for this connection.
        
        Signature ``AssignPath(routeLevel, path)`` 
        
        :param routeLevel: 
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ConnectionRouteLevel` 
        :param path:  The path on which to route this connection.  
        :type path: :py:class:`NXOpen.Routing.Path` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    FromTerminal: NXOpen.Routing.LogicalTerminal = ...
    """
    Returns or sets  the From terminal.  
    
    The From terminal is one end of an electrical connection.  From does not imply an ordering.
    
    <hr>
    
    Getter Method
    
    Signature ``FromTerminal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.LogicalTerminal` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``FromTerminal`` 
    
    :param fromTerminal:  May not be None  
    :type fromTerminal: :py:class:`NXOpen.Routing.LogicalTerminal` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    MaximumPathLength: float = ...
    """
    Returns or sets  the maximum path length for this connection.  
    
    Maximum path length is the longest allowable length
    of all segments referred to by this connection.
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumPathLength`` 
    
    :returns:  May be zero  
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumPathLength`` 
    
    :param pathLength:  May be zero  
    :type pathLength: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    MinimumPathLength: float = ...
    """
    Returns or sets  the minimum path length for this connection.  
    
    Minimum path length is the shortest allowable length
    of all segments referred to by this connection.
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumPathLength`` 
    
    :returns:  May be zero  
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumPathLength`` 
    
    :param pathLength:  May be zero  
    :type pathLength: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    PathLengthMultiplier: str = ...
    """
    Returns or sets  the path length multiplier.  
    
    Used to calculate cut length.
    Cut length = length * multiplier + offset 
    
    <hr>
    
    Getter Method
    
    Signature ``PathLengthMultiplier`` 
    
    :returns:  May be zero (cut length will be zero)  
    :rtype: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PathLengthMultiplier`` 
    
    :param pathLengthMultiplier:  May be zero (cut length will be zero)   
    :type pathLengthMultiplier: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    PathLengthOffset: str = ...
    """
    Returns or sets  the path length offset.  
    
    Used to calculate cut length.
    Cut length = length * multiplier + offset 
    
    <hr>
    
    Getter Method
    
    Signature ``PathLengthOffset`` 
    
    :returns:  May be zero   
    :rtype: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PathLengthOffset`` 
    
    :param pathLengthOffset:  May be zero  
    :type pathLengthOffset: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    ToTerminal: NXOpen.Routing.LogicalTerminal = ...
    """
    Returns or sets  the To terminal.  
    
    The To terminal is one end of an electrical connection.  To does not imply an ordering
    
    <hr>
    
    Getter Method
    
    Signature ``ToTerminal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.LogicalTerminal` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ToTerminal`` 
    
    :param toTerminal: May not be None 
    :type toTerminal: :py:class:`NXOpen.Routing.LogicalTerminal` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: Connection = ...  # unknown typename


class PathConnection(Connection):
    """
    Describes a connection that has a path
    
    From and To terminals are not coincident and need a path definition to be routable.            
    See NX Open Routing help for detailed information on the Connection data model.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.PathConnectionCollection.CreatePathConnection`
    
    .. versionadded:: NX4.0.2
    """
    Null: PathConnection = ...  # unknown typename


class JumperConnection(PathConnection):
    """
    A jumper connection connects ports on the same connector.
    
    A path may or may not be associated with this type of connection.  
    Specifies that terminals on the same part instance are connected somehow.
    See NX Open Routing help for detailed information on the Connection data model.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.JumperConnectionCollection.CreateJumperConnection`
    
    .. versionadded:: NX4.0.2
    """
    Null: JumperConnection = ...  # unknown typename


class ElectricalStockDeviceCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` (ESD) objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def AutoRouteConnections(self, routeLevel: ElectricalStockDeviceRouteLevel, routeSel: ElectricalStockDeviceAutoRouteSel, stockDevices: 'list[ElectricalStockDevice]') -> tuple:
        """
        Automatically routes the selected stock devices.  
        
        Routing can be done
        on pin, component or mixed level and it is based on shortest length
        (See :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` for more details).  
        
        Signature ``AutoRouteConnections(routeLevel, routeSel, stockDevices)`` 
        
        :param routeLevel: 
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceRouteLevel` 
        :param routeSel: 
        :type routeSel: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceAutoRouteSel` 
        :param stockDevices: 
        :type stockDevices: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        :returns: a tuple 
        :rtype: A tuple consisting of (noOfRoutedStockDevices, errorList). noOfRoutedStockDevices is a int. errorList is a :py:class:`NXOpen.ErrorList`.   Any errors that occurred during Automatic Routing. 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AssignStock(self, stockDevices: 'list[ElectricalStockDevice]', routeType: ElectricalStockDeviceRouteTypes) -> None:
        """
        Assign :py:class:`NXOpen.Routing.Stock` to input stock devices.  
        
        The assigned :py:class:`NXOpen.Routing.Stock` is a bundle stock,
        and the routine will perform the bundling calculations. This routine
        should also be called after performing :py:meth:`NXOpen.Routing.Electrical.ElectricalStockDevice.ManuallyRoute`. 
        
        Signature ``AssignStock(stockDevices, routeType)`` 
        
        :param stockDevices: 
        :type stockDevices: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        :param routeType: 
        :type routeType: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceRouteTypes` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def RemoveStock(self, stockDevices: 'list[ElectricalStockDevice]') -> 'list[ElectricalStockDevice]':
        """
        Removes :py:class:`NXOpen.Routing.Stock` from input stock devices.  
        
        Removes all segments from input wires and updates harnesses associated 
        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
        the :py:class:`NXOpen.Routing.Wire`.  
        
        Signature ``RemoveStock(stockDevices)`` 
        
        :param stockDevices: 
        :type stockDevices: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AutoRouteAll(self, routeLevel: ElectricalStockDeviceRouteLevel, routeSel: ElectricalStockDeviceAutoRouteSel) -> tuple:
        """
        Automatically routes all of the stock devices in the work part.  
        
        Routing can be done
        on pin, component or mixed level and it is based on shortest length
        (See :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` for more details).  
        
        Signature ``AutoRouteAll(routeLevel, routeSel)`` 
        
        :param routeLevel: 
        :type routeLevel: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceRouteLevel` 
        :param routeSel: 
        :type routeSel: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDeviceAutoRouteSel` 
        :returns: a tuple 
        :rtype: A tuple consisting of (noOfRoutedStockDevices, errorList). noOfRoutedStockDevices is a int. errorList is a :py:class:`NXOpen.ErrorList`.   Any errors that occurred during Automatic Routing. 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def Unroute(self, stockDevices: 'list[ElectricalStockDevice]') -> 'list[ElectricalStockDevice]':
        """
        Removes all bundle :py:class:`NXOpen.Routing.Stock` from input stock devices.  
        
        Removes all segments from input wires and updates harnesses associated 
        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
        the :py:class:`NXOpen.Routing.Wire`. Use this when no rebundling is 
        necessary  
        
        Signature ``Unroute(stockDevices)`` 
        
        :param stockDevices: 
        :type stockDevices: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def UnrouteAll(self) -> 'list[ElectricalStockDevice]':
        """
        Removes all bundle :py:class:`NXOpen.Routing.Stock` from all stock devices.  
        
        Removes all segments from input wires and updates harnesses associated 
        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
        the :py:class:`NXOpen.Routing.Wire`. Use this when no rebundling is 
        necessary  
        
        Signature ``UnrouteAll()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class SystemDeviceCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.SystemDevice` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    @typing.overload
    def CreateSystemDevice(self) -> SystemDevice:
        """
        Creates :py:class:`NXOpen.Routing.Electrical.SystemDevice`.  
        
        Signature ``CreateSystemDevice()`` 
        
        :returns:  The new System Device.  
        :rtype: :py:class:`NXOpen.Routing.Electrical.SystemDevice` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def CreateSystemDevice(self, systemName: str) -> SystemDevice:
        """
        Creates :py:class:`NXOpen.Routing.Electrical.SystemDevice` with given name.  
        
        Signature ``CreateSystemDevice(systemName)`` 
        
        :param systemName:  The name of the new system.                                                             (None not allowed)  
        :type systemName: str 
        :returns:  The new System Device.  
        :rtype: :py:class:`NXOpen.Routing.Electrical.SystemDevice` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetSystemSingleDevices(self) -> 'list[SystemDevice]':
        """
        Get System Devices.  
        
        Signature ``GetSystemSingleDevices()`` 
        
        :returns:  The array of System Devices in the given part.  
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.SystemDevice` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class CablewaysBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.Routing.Electrical.CablewaysBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.RouteManager.CreateCablewaysBuilder`
    
    Default values.
    
    ==============================  =====
    Property                        Value
    ==============================  =====
    AllowNewCables                  0 
    ------------------------------  -----
    AllowOverFill                   0 
    ------------------------------  -----
    CableTrayArea.Value             0 
    ------------------------------  -----
    CableTrayMaximumHeight.Value    0 
    ------------------------------  -----
    CabletrayHeight.Value           0 
    ------------------------------  -----
    CabletrayWidth.Value            0 
    ------------------------------  -----
    FillPercentage.Value            0 
    ------------------------------  -----
    SpecifiedFillPercentage.Value   0 
    ==============================  =====
    
    .. versionadded:: NX7.5.0
    """
    AllowNewCables: bool = ...
    """
    Returns or sets  the allow new cables toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowNewCables`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_cabling ("Routing Cabling")
    
    <hr>
    
    Setter Method
    
    Signature ``AllowNewCables`` 
    
    :param allowNewCables: 
    :type allowNewCables: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    AllowOverFill: bool = ...
    """
    Returns or sets  the Allow Overfill toggle 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowOverFill`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    
    <hr>
    
    Setter Method
    
    Signature ``AllowOverFill`` 
    
    :param allowOverfill: 
    :type allowOverfill: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    CableTrayArea: NXOpen.Expression = ...
    """
    Returns  the cabletray area expression 
    
    <hr>
    
    Getter Method
    
    Signature ``CableTrayArea`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    CableTrayMaximumHeight: NXOpen.Expression = ...
    """
    Returns  the cabletray maximum height expression 
    
    <hr>
    
    Getter Method
    
    Signature ``CableTrayMaximumHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    CabletrayHeight: NXOpen.Expression = ...
    """
    Returns  the cabletray height expression 
    
    <hr>
    
    Getter Method
    
    Signature ``CabletrayHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    CabletrayWidth: NXOpen.Expression = ...
    """
    Returns  the cabletray width expression 
    
    <hr>
    
    Getter Method
    
    Signature ``CabletrayWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    FillPercentage: NXOpen.Expression = ...
    """
    Returns  the fill percentage expression 
    
    <hr>
    
    Getter Method
    
    Signature ``FillPercentage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    RouteObjectCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the route object collector 
    
    <hr>
    
    Getter Method
    
    Signature ``RouteObjectCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    SpecifiedFillPercentage: NXOpen.Expression = ...
    """
    Returns  the specified fill percentage expression 
    
    <hr>
    
    Getter Method
    
    Signature ``SpecifiedFillPercentage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_cabling ("Routing Cabling")
    """
    Null: CablewaysBuilder = ...  # unknown typename


class ConnectorDeviceCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` (CD) objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    @typing.overload
    def CreateConnectorDevice(self, connectorType: ConnectorDeviceComponentType, componentName: str) -> ConnectorDevice:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.ConnectorDevice`.  
        
        Signature ``CreateConnectorDevice(connectorType, componentName)`` 
        
        :param connectorType: 
        :type connectorType: :py:class:`NXOpen.Routing.Electrical.ConnectorDeviceComponentType` 
        :param componentName: 
        :type componentName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def CreateConnectorDevice(self, harnessDevice: HarnessDevice, equipmentName: str, connectorName: str, connectorType: ConnectorDeviceComponentType) -> ConnectorDevice:
        """
        Finds or Creates a :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` for given equipmentName and or 
        connectorName. Builds :py:class:`NXOpen.Routing.Electrical.ElectricalDeviceRelationship` between 
        equipment and connector, if equipmentName and connectorName are not None.
        Adds connector to harnessDevice, if connectorName and harnessDevice are not None.  
        
        Signature ``CreateConnectorDevice(harnessDevice, equipmentName, connectorName, connectorType)`` 
        
        :param harnessDevice:  can be Routing.HarnessDevice.NULL  
        :type harnessDevice: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        :param equipmentName:  can be None if connectorName is not None  
        :type equipmentName: str 
        :param connectorName:  can be None if equipmentName is not None  
        :type connectorName: str 
        :param connectorType: 
        :type connectorType: :py:class:`NXOpen.Routing.Electrical.ConnectorDeviceComponentType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetConnectorSingleDevices(self) -> 'list[ConnectorDevice]':
        """
        Get connectors from the work part.  
        
        Signature ``GetConnectorSingleDevices()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetEquipmentSingleDevices(self) -> 'list[ConnectorDevice]':
        """
        Get equipment from the work part.  
        
        Signature ``GetEquipmentSingleDevices()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def AutoAssignConnectors(self, connectors: 'list[ConnectorDevice]') -> None:
        """
        Auto assignment is done using one
        of the three matching methods, Part Name, Component Name or Attribute.  
        
        Signature ``AutoAssignConnectors(connectors)`` 
        
        :param connectors: 
        :type connectors: list of :py:class:`NXOpen.Routing.Electrical.ConnectorDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class HarnessDefinition(NXOpen.Routing.AssemblyDefinition):
    """
    Represents a :py:class:`NXOpen.Routing.Electrical.HarnessDefinition`   
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    
    def GetChildConnections(self) -> 'list[Connection]':
        """
        Returns all of the Connection objects that are implemented by single devices
        that are children of this harness
        
        Signature ``GetChildConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.Connection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: HarnessDefinition = ...  # unknown typename


class SystemDefinition(HarnessDefinition):
    """
    Represents a :py:class:`NXOpen.Routing.Electrical.SystemDefinition`   
    
    Creator not available in KF.
    
    .. versionadded:: NX6.0.0
    """
    Null: SystemDefinition = ...  # unknown typename


class HarnessDevice(NXOpen.Routing.SingleDevice):
    """
    The Electrical HarnessDevice corresponds to a harness instance of the 
    :py:class:`Routing.SingleDevice`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.HarnessDeviceCollection.CreateHarnessDevice`
    
    .. versionadded:: NX4.0.2
    """
    
    def GetHarnessDefinition(self) -> HarnessDefinition:
        """
        Get harness definition.  
        
        Signature ``GetHarnessDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDefinition` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: HarnessDevice = ...  # unknown typename


class CableConnection(Connection):
    """
    Connection used by a :py:class:`NXOpen.Routing.Electrical.CableDevice`.  
    
    Use is similar to a :py:class:`NXOpen.Routing.Electrical.PathConnection`, 
    except that a cable connection may have many paths due to many wire and/or cable children.
    
    See the NX Routing help for detailed information on the Connection data model.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.CableConnectionCollection.CreateCableConnection`
    
    .. versionadded:: NX4.0.2
    """
    
    def IsCableRouted(self) -> bool:
        """
        Is this cable routed?  
        
        Signature ``IsCableRouted()`` 
        
        :returns:  
          * <tt>true</tt> The cable is routed.
          * <tt>false</tt> The cable not routed.
        
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: CableConnection = ...  # unknown typename


class ElectricalNavigatorFilter(NXOpen.NavigatorFilter):
    """
    Represents a Routing Electrical Navigator Filter object.  
    
    To create an  instance of this class use :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilterCollection`
    
    .. versionadded:: NX5.0.1
    """
    Null: ElectricalNavigatorFilter = ...  # unknown typename


class SortConnectionsPluginData(NXOpen.TaggedObject):
    """
    Data object created by Routing just before routing connections.  
    
    Routing sends this object to any registered Sort Connections plugin with the
    "Stock Devices to sort" filled in.
    
    It is the Sort Connections plugin responsibility to sort the Stock Devices and
    to put the sorted Stock Devices into "Sorted Stock Devices".
    
    For more information, see :py:class:`Routing.CustomManager` and the
    :py:meth:`Routing.CustomManager.SetSortConnectionsPlugin`
    
    An instance of this object will be sent to the Sort Connections plugin.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetStockDevicesToSort(self) -> 'list[ElectricalStockDevice]':
        """
        Gets the stock devices such as :py:class:`Routing.Electrical.WireDevice`s
        that implement connections Routing is about to route along their paths.  
        
        Signature ``GetStockDevicesToSort()`` 
        
        :returns:  The :py:class:`Routing.Electrical.ElectricalStockDevice`s to sort in the order in which
        you want to route them.  
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def SetSortedStockDevices(self, stockDevices: 'list[ElectricalStockDevice]') -> None:
        """
        Sets the stock devices sorted in the order in which you want their connections to route.  
        
        Signature ``SetSortedStockDevices(stockDevices)`` 
        
        :param stockDevices:  The :py:class:`Routing.Electrical.ElectricalStockDevice`s sorted in the order in which                    you want to route them.  
        :type stockDevices: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: SortConnectionsPluginData = ...  # unknown typename


class JumperConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    A collection of :py:class:`NXOpen.Routing.Electrical.JumperConnection` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateJumperConnection(self) -> JumperConnection:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.JumperConnection` object.  
        
        Signature ``CreateJumperConnection()`` 
        
        :returns:  A :py:class:`NXOpen.Routing.Electrical.JumperConnection`  
        :rtype: :py:class:`NXOpen.Routing.Electrical.JumperConnection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class ElectricalStockDefinitionSectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElectricalStockDefinitionSectionType():
    """
    Stock section type.   
    
    .. versionadded:: NX4.0.2
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Circular", " - "
       "Rectangular", " - "
    """
    Circular = 0  # ElectricalStockDefinitionSectionTypeMemberType
    Rectangular = 1  # ElectricalStockDefinitionSectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ElectricalStockDefinition(NXOpen.Routing.StockDefinition):
    """
    Represents :py:class:`NXOpen.Routing.Electrical.ElectricalStockDefinition` object   
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    
    class SectionType():
        """
        Stock section type.   
        
        .. versionadded:: NX4.0.2
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Circular", " - "
           "Rectangular", " - "
        """
        Circular = 0  # ElectricalStockDefinitionSectionTypeMemberType
        Rectangular = 1  # ElectricalStockDefinitionSectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CrossSectionType: ElectricalStockDefinitionSectionType = ...
    """
    Returns or sets   the cross section type of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDefinitionSectionType` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CrossSectionType`` 
    
    :param sectionType: 
    :type sectionType: :py:class:`NXOpen.Routing.Electrical.ElectricalStockDefinitionSectionType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Gauge: float = ...
    """
    Returns or sets   the gauge of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``Gauge`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Gauge`` 
    
    :param gaugeValue: 
    :type gaugeValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Height: float = ...
    """
    Returns or sets   the height of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param heightValue: 
    :type heightValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    LinearDensity: float = ...
    """
    Returns or sets   the linear density of stock  
    
    <hr>
    
    Getter Method
    
    Signature ``LinearDensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``LinearDensity`` 
    
    :param densityValue: 
    :type densityValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    MinBendRadius: float = ...
    """
    Returns or sets   the min bend radius of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``MinBendRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MinBendRadius`` 
    
    :param radiusValue: 
    :type radiusValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Width: float = ...
    """
    Returns or sets  the width of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param widthValue: 
    :type widthValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    WireType: str = ...
    """
    Returns or sets   the wire type of stock 
    
    <hr>
    
    Getter Method
    
    Signature ``WireType`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``WireType`` 
    
    :param wireType: 
    :type wireType: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: ElectricalStockDefinition = ...  # unknown typename


class ElectricalFormatCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a Routing :py:class:`NXOpen.Routing.Electrical.ElectricalFormatCollection` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX5.0.1
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateFormat(self, name: str, type: ElectricalFormatType) -> ElectricalFormat:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` object.  
        
        Signature ``CreateFormat(name, type)`` 
        
        :param name: 
        :type name: str 
        :param type: 
        :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetDisplayFormat(self, type: ElectricalFormatType) -> ElectricalFormat:
        """
        Get the displayed :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` object for the
        given navigator type.  
        
        Signature ``GetDisplayFormat(type)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def SetDisplayFormat(self, type: ElectricalFormatType, format: ElectricalFormat) -> None:
        """
        Set the :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` object as displayed
        format for the given navigator type.  
        
        Signature ``SetDisplayFormat(type, format)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
        :param format: 
        :type format: :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class CablewaysLayoutViewCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.CablewaysLayoutView` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX7.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateLayoutView(self, segment: NXOpen.Curve) -> CablewaysLayoutView:
        """
        Creates :py:class:`NXOpen.Routing.Electrical.CablewaysLayoutView` object.  
        
        Only one :py:class:`NXOpen.Routing.Electrical.CablewaysLayoutView` object
        can exist per segment, so if the object already exists, it returns the same.
        
        Signature ``CreateLayoutView(segment)`` 
        
        :param segment:  Segment on which layout view should be created or whose view is asked.  
        :type segment: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CablewaysLayoutView` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    


class ElectricalDeviceRelationship(NXOpen.Routing.DeviceRelationship):
    """
    Represents a relationship between Routing Electrical devices.
    
    Use this class to associate electrical connectors to electrical equipment outside of a harness.
    
    (example)
    Use an ElectricalDeviceRelationship to represent connectors C1 and C2 mounted on a piece of equipment, D1.
    The Relating object is D1 and the Related objects are C1 and C2.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.ElectricalDeviceRelationshipCollection.CreateElectricalDeviceRelationship`
    
    .. versionadded:: NX4.0.2
    """
    Null: ElectricalDeviceRelationship = ...  # unknown typename


class CablewaysLayoutView(NXOpen.NXObject):
    """
    Represents the CablewaysLayoutView class.  
    
    No creator as of now
    
    .. versionadded:: NX7.5.0
    """
    
    def CondemnLayoutViewEntities(self) -> None:
        """
        Condemns the layout view entities.  
        
        Signature ``CondemnLayoutViewEntities()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def UncondemnLayoutViewEntities(self) -> None:
        """
        Uncondemns the layout view entities.  
        
        Signature ``UncondemnLayoutViewEntities()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    @typing.overload
    def PositionLayoutView(self, orientation: NXOpen.Matrix3x3, origin: NXOpen.Point3d) -> None:
        """
        Positions the layout view in the 3D space as per input orientation matrix and origin. 
        
        Signature ``PositionLayoutView(orientation, origin)`` 
        
        :param orientation: 
        :type orientation: :py:class:`NXOpen.Matrix3x3` 
        :param origin: 
        :type origin: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    @typing.overload
    def PositionLayoutView(self, toOrientation: NXOpen.Xform) -> None:
        """
        Positions the layout view in the 3D space as per the :py:class:`NXOpen.Xform`. 
        
        Signature ``PositionLayoutView(toOrientation)`` 
        
        :param toOrientation: 
        :type toOrientation: :py:class:`NXOpen.Xform` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def FlipView(self) -> None:
        """
        Flips the layout view along view direction.  
        
        Signature ``FlipView()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def GetViewDirection(self) -> bool:
        """
        Returns the view direction.  
        
        Signature ``GetViewDirection()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def HighlightView(self) -> None:
        """
        Highlights the layout view.  
        
        Signature ``HighlightView()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def UnhighlightView(self) -> None:
        """
        Unhighlights the layout view.  
        
        Signature ``UnhighlightView()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    
    def GetViewMatrixAndOrigin(self) -> tuple:
        """
        Returns the orientation matrix and origin associated with the layout view.  
        
        Signature ``GetViewMatrixAndOrigin()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (orientation, origin). orientation is a :py:class:`NXOpen.Matrix3x3`. origin is a :py:class:`NXOpen.Point3d`. 
        
        .. versionadded:: NX7.5.0
        
        License requirements: routing_cabling ("Routing Cabling")
        """
        ...
    
    Null: CablewaysLayoutView = ...  # unknown typename


class CablewaysLayoutBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.Routing.Electrical.CablewaysLayoutBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.RouteManager.CreateCablewaysLayoutBuilder`
    
    .. versionadded:: NX7.5.0
    """
    Null: CablewaysLayoutBuilder = ...  # unknown typename


class ConnectorDeviceComponentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectorDeviceComponentType():
    """
    Component type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Connector", " - "
       "Splice", " - "
       "Device", " - "
       "Other", " - "
    """
    NotSet = 0  # ConnectorDeviceComponentTypeMemberType
    Connector = 1  # ConnectorDeviceComponentTypeMemberType
    Splice = 2  # ConnectorDeviceComponentTypeMemberType
    Device = 3  # ConnectorDeviceComponentTypeMemberType
    Other = 4  # ConnectorDeviceComponentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConnectorDeviceAssignMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectorDeviceAssign():
    """
    Assignment method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Auto", " - "
       "Manual", " - "
    """
    NotSet = 0  # ConnectorDeviceAssignMemberType
    Auto = 1  # ConnectorDeviceAssignMemberType
    Manual = 2  # ConnectorDeviceAssignMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConnectorDevice(NXOpen.Routing.SingleDevice):
    """
    The Electrical ConnectorDevice corresponds to a connector instance of
    :py:class:`NXOpen.Routing.SingleDevice`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.ConnectorDeviceCollection.CreateConnectorDevice`
    
    .. versionadded:: NX4.0.2
    """
    
    class ComponentType():
        """
        Component type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Connector", " - "
           "Splice", " - "
           "Device", " - "
           "Other", " - "
        """
        NotSet = 0  # ConnectorDeviceComponentTypeMemberType
        Connector = 1  # ConnectorDeviceComponentTypeMemberType
        Splice = 2  # ConnectorDeviceComponentTypeMemberType
        Device = 3  # ConnectorDeviceComponentTypeMemberType
        Other = 4  # ConnectorDeviceComponentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Assign():
        """
        Assignment method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Auto", " - "
           "Manual", " - "
        """
        NotSet = 0  # ConnectorDeviceAssignMemberType
        Auto = 1  # ConnectorDeviceAssignMemberType
        Manual = 2  # ConnectorDeviceAssignMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetPartDefinition(self) -> ElectricalPartDefinitionShadow:
        """
        Get part definition.  
        
        Signature ``GetPartDefinition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def SetPartDefinition(self, elecPartDefinitionShadow: ElectricalPartDefinitionShadow) -> None:
        """
        Sets part definition.  
        
        Signature ``SetPartDefinition(elecPartDefinitionShadow)`` 
        
        :param elecPartDefinitionShadow: 
        :type elecPartDefinitionShadow: :py:class:`NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetTerminals(self) -> 'list[NXOpen.Routing.LogicalTerminal]':
        """
        Get terminals.  
        
        Signature ``GetTerminals()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.LogicalTerminal` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def RemoveTerminal(self, routeTerminalToRemove: NXOpen.Routing.LogicalTerminal) -> bool:
        """
        Remove a terminal.  
        
        Signature ``RemoveTerminal(routeTerminalToRemove)`` 
        
        :param routeTerminalToRemove: 
        :type routeTerminalToRemove: :py:class:`NXOpen.Routing.LogicalTerminal` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetAssignMethod(self) -> ConnectorDeviceAssign:
        """
        Get assign method.  
        
        Signature ``GetAssignMethod()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDeviceAssign` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestHarnessDevice(self) -> HarnessDevice:
        """
        Get the nearest :py:class:`NXOpen.Routing.Electrical.HarnessDevice` encountered up the parent-child hierarchy.  
        
        Signature ``FindNearestHarnessDevice()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindNearestCableDevice(self) -> CableDevice:
        """
        Get the nearest :py:class:`NXOpen.Routing.Electrical.CableDevice` encountered up the parent-child hierarchy.  
        
        Signature ``FindNearestCableDevice()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def IsNxDevice(self, elecHarnessDevice: HarnessDevice) -> bool:
        """
        Is the device a NX device?  
        
        Signature ``IsNxDevice(elecHarnessDevice)`` 
        
        :param elecHarnessDevice: 
        :type elecHarnessDevice: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def IsNxConnector(self, elecHarnessDevice: HarnessDevice) -> bool:
        """
        Is the device a connector?  
        
        Signature ``IsNxConnector(elecHarnessDevice)`` 
        
        :param elecHarnessDevice: 
        :type elecHarnessDevice: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def IsUsedInRoutedConnection(self, elecHarnessDevice: HarnessDevice) -> bool:
        """
        Is the device used in a routed connection?  
        
        Signature ``IsUsedInRoutedConnection(elecHarnessDevice)`` 
        
        :param elecHarnessDevice: 
        :type elecHarnessDevice: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def UnassignConnector(self) -> None:
        """
        Unassign connector.  
        
        Signature ``UnassignConnector()`` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ManuallyAssignConnector(self, elecConnectorPartOccurrence: NXOpen.Assemblies.Component) -> None:
        """
        Assign a connector manually.  
        
        Signature ``ManuallyAssignConnector(elecConnectorPartOccurrence)`` 
        
        :param elecConnectorPartOccurrence:  Component to assign.  
        :type elecConnectorPartOccurrence: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindRoutedStockDevices(self) -> 'list[ElectricalStockDevice]':
        """
        Find routed stock devices.  
        
        Signature ``FindRoutedStockDevices()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def IsAssigned(self) -> bool:
        """
        Get status of a connector device (assigned or not).  
        
        Signature ``IsAssigned()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindStockDevices(self) -> 'list[ElectricalStockDevice]':
        """
        Find stock devices.  
        
        Signature ``FindStockDevices()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindConnections(self) -> 'list[Connection]':
        """
        Find connections.  
        
        Signature ``FindConnections()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.Connection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetTerminal(self, terminalName: str, createTerminal: bool) -> NXOpen.Routing.LogicalTerminal:
        """
        Get :py:class:`NXOpen.Routing.LogicalTerminal` given the name of the terminal.  
        
        If a terminal does not exists creates a terminal 
        
        Signature ``GetTerminal(terminalName, createTerminal)`` 
        
        :param terminalName: 
        :type terminalName: str 
        :param createTerminal:  TRUE - creates a new terminal if one does not exist with given name 
        :type createTerminal: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.LogicalTerminal` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindMatchingParts(self) -> 'list[NXOpen.Routing.CharacteristicList]':
        """
        Find parts matching the connector device.  
        
        Searches for "PART_NAME" 
        property on connector device to search for matches in the part tables
        Returns  all matching rows from the part tables.  
        
        Signature ``FindMatchingParts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.CharacteristicList` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def FindPlacer(self) -> tuple:
        """
        Searches for a placement port for the connector device.  
        
        The placement
        port is defined in the component list by attribute "DEVICE_PIN" or
        "EQUIPMENT_PIN". If the attribute is not defined, searches for the 
        first available port on the relating device.  
        
        Signature ``FindPlacer()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (placer, placerPos). placer is a :py:class:`NXOpen.Routing.Port`. placerPos is a float. 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def PlaceConnectorOnPort(self, match: NXOpen.Routing.CharacteristicList, placer: NXOpen.Routing.Port) -> NXOpen.Assemblies.Component:
        """
        Loads the parts based on the :py:class:`NXOpen.Routing.CharacteristicList`
        adds the instance of the part to the current work part and places the 
        instance on the placer.  
        
        Signature ``PlaceConnectorOnPort(match, placer)`` 
        
        :param match: 
        :type match: :py:class:`NXOpen.Routing.CharacteristicList` 
        :param placer: 
        :type placer: :py:class:`NXOpen.Routing.Port` 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def ProxyAssignConnector(self, proxy: NXOpen.Routing.Port) -> None:
        """
        Assign a connector to a proxy port.  
        
        Signature ``ProxyAssignConnector(proxy)`` 
        
        :param proxy:  Assigned port.  
        :type proxy: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    ComponentName: str = ...
    """
    Returns or sets  the component name.  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ComponentName`` 
    
    :param componentName: 
    :type componentName: str 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    ConnectorType: ConnectorDeviceComponentType = ...
    """
    Returns or sets  the connector type.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectorType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.Electrical.ConnectorDeviceComponentType` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectorType`` 
    
    :param elecRlistComponent: 
    :type elecRlistComponent: :py:class:`NXOpen.Routing.Electrical.ConnectorDeviceComponentType` 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: ConnectorDevice = ...  # unknown typename


class ElectricalDeviceRelationshipCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.ElectricalDeviceRelationship` objects.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateElectricalDeviceRelationship(self) -> ElectricalDeviceRelationship:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.ElectricalDeviceRelationship` object.  
        
        Signature ``CreateElectricalDeviceRelationship()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalDeviceRelationship` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class NonPathConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    A collection of :py:class:`NXOpen.Routing.Electrical.NonPathConnection` objects.
    
    See NX Open Routing help for detailed information on the Connection data model.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateNonPathConnection(self) -> NonPathConnection:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.NonPathConnection` object.  
        
        Signature ``CreateNonPathConnection()`` 
        
        :returns:  A :py:class:`NXOpen.Routing.Electrical.NonPathConnection`   
        :rtype: :py:class:`NXOpen.Routing.Electrical.NonPathConnection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class CableStockDefinition(ElectricalStockDefinition):
    """
    Describes a cable's stock.  
    
    Contains characteristics of the material that makes up the cable.
    
    See the NX Routing help for detailed information on the Connection data model.
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    CableLocation: int = ...
    """
    Returns or sets the cable stock's location 
    
    <hr>
    
    Getter Method
    
    Signature ``CableLocation`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CableLocation`` 
    
    :param locationValue: 
    :type locationValue: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    CoverThickness: float = ...
    """
    Returns or sets the thickness of the cable's covering.  
    
    <hr>
    
    Getter Method
    
    Signature ``CoverThickness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CoverThickness`` 
    
    :param thicknessValue: 
    :type thicknessValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    WireSpacing: float = ...
    """
    Returns or sets the separation between wires in a cable.  
    
    <hr>
    
    Getter Method
    
    Signature ``WireSpacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX4.0.2
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``WireSpacing`` 
    
    :param spacingValue: 
    :type spacingValue: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: CableStockDefinition = ...  # unknown typename


class SystemDevice(HarnessDevice):
    """
    The Electrical SystemDevice corresponds to a system instance of the 
    :py:class:`NXOpen.Routing.SingleDevice`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.SystemDeviceCollection.CreateSystemDevice`
    
    .. versionadded:: NX6.0.0
    """
    
    def GetSystemDefinition(self) -> SystemDefinition:
        """
        Returns the :py:class:`NXOpen.Routing.Electrical.SystemDefinition`
        used by this :py:class:`NXOpen.Routing.Electrical.SystemDevice`.  
        
        Signature ``GetSystemDefinition()`` 
        
        :returns:  The :py:class:`NXOpen.Routing.Electrical.SystemDefinition` used by this :py:class:`NXOpen.Routing.Electrical.SystemDevice`.  
        :rtype: :py:class:`NXOpen.Routing.Electrical.SystemDefinition` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    Null: SystemDevice = ...  # unknown typename


class CableConnectionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.Routing.Electrical.CableConnection` objects.  
    
    See the NX Routing help for detailed information on the Connection data model.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateCableConnection(self) -> CableConnection:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.CableConnection` object.  
        
        Signature ``CreateCableConnection()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableConnection` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateShieldConnection(self) -> CableConnection:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.CableConnection` object
        implemented by a :py:class:`NXOpen.Routing.Electrical.ShieldDevice`.  
        
        Signature ``CreateShieldConnection()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.CableConnection` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class ElectricalNavigatorFilterCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a Routing :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilterCollection` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX5.0.1
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateFilter(self, name: str, clause: str) -> ElectricalNavigatorFilter:
        """
        Creates a :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` object.  
        
        Signature ``CreateFilter(name, clause)`` 
        
        :param name:  Name of the filter  
        :type name: str 
        :param clause:  Clause of the filter  
        :type clause: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetDisplayFilter(self, type: ElectricalFormatType) -> ElectricalNavigatorFilter:
        """
        Get the displayed :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` object
        for the given navigator type  
        
        Signature ``GetDisplayFilter(type)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def SetDisplayFilter(self, type: ElectricalFormatType, filter: ElectricalNavigatorFilter) -> None:
        """
        Set the :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` object as 
        displayed filter for given navigator type.  
        
        Signature ``SetDisplayFilter(type, filter)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
        :param filter: 
        :type filter: :py:class:`NXOpen.Routing.Electrical.ElectricalNavigatorFilter` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class AssignProxyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Routing.Electrical.AssignProxyBuilder`.  
    
    This is used 
    to create a proxy port and assign it to a connector.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.RouteManager.CreateAssignProxyBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the position of the proxy port to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the direction of the proxy port to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: AssignProxyBuilder = ...  # unknown typename


class NonPathConnection(Connection):
    """
    Describes a connection that does not have a path
    
    A pathless connection represents the abilitiy for objects to be 
    connected even though there is not an explicit path between them.
    See NX Open Routing help for detailed information on the Connection data model.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Routing.Electrical.NonPathConnectionCollection.CreateNonPathConnection`
    
    .. versionadded:: NX4.0.2
    """
    Null: NonPathConnection = ...  # unknown typename


class WireDevice(ElectricalStockDevice):
    """
    The Electrical WireDevice corresponds to a wire instance of
    :py:class:`NXOpen.Routing.Electrical.ElectricalStockDevice`.  
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: WireDevice = ...  # unknown typename


class ElectricalFormatTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ElectricalFormatType():
    """
    Describes how system reports the lengths of the stock. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Connections", " - "
       "Components", " - "
    """
    Connections = 0  # ElectricalFormatTypeMemberType
    Components = 1  # ElectricalFormatTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ElectricalFormat(NXOpen.TaggedObject):
    """
    Represents a Routing Electrical ElectricalFormat.  
    
    To create an  instance of this class use :py:class:`NXOpen.Routing.Electrical.ElectricalFormatCollection`
    
    .. versionadded:: NX5.0.1
    """
    
    class Type():
        """
        Describes how system reports the lengths of the stock. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Connections", " - "
           "Components", " - "
        """
        Connections = 0  # ElectricalFormatTypeMemberType
        Components = 1  # ElectricalFormatTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    FormatType: ElectricalFormatType = ...
    """
    Returns or sets  the type of :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` 
    
    <hr>
    
    Getter Method
    
    Signature ``FormatType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
    
    .. versionadded:: NX5.0.1
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``FormatType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Routing.Electrical.ElectricalFormatType` 
    
    .. versionadded:: NX5.0.1
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Name: str = ...
    """
    Returns or sets  the name of :py:class:`NXOpen.Routing.Electrical.ElectricalFormat` 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.1
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX5.0.1
    
    License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    """
    Null: ElectricalFormat = ...  # unknown typename


class ShieldStockDefinition(CableStockDefinition):
    """
    Represents Routing Electrical ShieldStockDefinition object   
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: ShieldStockDefinition = ...  # unknown typename


class HarnessDeviceCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`Routing.Electrical.HarnessDevice` objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Routing.RouteManager`
    
    .. versionadded:: NX4.0.2
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    @typing.overload
    def CreateHarnessDevice(self) -> HarnessDevice:
        """
        Creates :py:class:`Routing.Electrical.HarnessDevice`.  
        
        Signature ``CreateHarnessDevice()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    @typing.overload
    def CreateHarnessDevice(self, harnessName: str) -> HarnessDevice:
        """
        Creates :py:class:`Routing.Electrical.HarnessDevice` with given name.  
        
        Signature ``CreateHarnessDevice(harnessName)`` 
        
        :param harnessName: 
        :type harnessName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    
    
    def GetHarnessSingleDevices(self) -> 'list[HarnessDevice]':
        """
        Get harnesses  
        
        Signature ``GetHarnessSingleDevices()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Routing.Electrical.HarnessDevice` 
        
        .. versionadded:: NX4.0.2
        
        License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
        """
        ...
    


class ElectricalPartDefinitionShadow(NXOpen.Routing.PartDefinitionShadow):
    """
    Represents :py:class:`NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow` object   
    
    Creator not available in KF.
    
    .. versionadded:: NX4.0.2
    """
    Null: ElectricalPartDefinitionShadow = ...  # unknown typename


