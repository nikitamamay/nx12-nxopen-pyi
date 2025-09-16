# module 'NXOpen.SIM'
#
# Automatically generated 2025-06-09T14:38:47.472711
#
"""Default documentation for NXOpen.SIM."""

import typing

import NXOpen
import NXOpen.CAM
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ImportMachineKitBuilder(NXOpen.Builder):
    """
    This class is used for the Import Machine Kit Dialog.  
    
    Calling :py:meth:`Builder.Commit` on this
    builder will start the import machine kit process
    and return None.
    
    Use the :py:class:`Part` class to import a Machine Kit object.
    
    .. versionadded:: NX11.0.0
    """
    OutputDirectory: str = ...
    """
    Returns or sets  the machine kit output directory specify where the finished machine folder will be stored.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputDirectory`` 
    
    :returns:  machine output directory  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputDirectory`` 
    
    :param outputDirectory:  machine output directory  
    :type outputDirectory: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    PrintReport: bool = ...
    """
    Returns or sets  the machine print report flat that specifies if a report will be plotted while import the machine or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrintReport`` 
    
    :returns:  print report flag  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``PrintReport`` 
    
    :param onOff:  print report flag  
    :type onOff: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: ImportMachineKitBuilder = ...  # unknown typename


class KinematicJunctionBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[KinematicJunctionBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: KinematicJunctionBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
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
    
    
    def FindIndex(self, obj: KinematicJunctionBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> KinematicJunctionBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
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
    def Erase(self, obj: KinematicJunctionBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: KinematicJunctionBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
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
    
    
    def GetContents(self) -> 'list[KinematicJunctionBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[KinematicJunctionBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
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
    def Swap(self, object1: KinematicJunctionBuilder, object2: KinematicJunctionBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: KinematicJunctionBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
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
    Null: KinematicJunctionBuilderList = ...  # unknown typename


class SinumerikCaExportBuilder(NXOpen.Builder):
    """
    This class is used for export a spf file.  
    
    A call to :py:meth:`SinumerikCaExportBuilder.ExportSpf` is used to export a spf file.
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`NXOpen.Part` class to create a SinumerikCaExportBuilder object.
    
    .. versionadded:: NX9.0.0
    """
    
    def ExportSpf(self, targetNode: str) -> None:
        """
        Export to Sinumerik Spf file 
        
        Signature ``ExportSpf(targetNode)`` 
        
        :param targetNode:  The name of the node to export to  
        :type targetNode: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
        """
        ...
    
    ChainElementIndex: int = ...
    """
    Returns or sets  the index used by chain elements when exporting the SPF file 
    
    <hr>
    
    Getter Method
    
    Signature ``ChainElementIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChainElementIndex`` 
    
    :param index: 
    :type index: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    CollisionPairIndex: int = ...
    """
    Returns or sets  the index used when exporting collision pairs to the SPF file 
    
    <hr>
    
    Getter Method
    
    Signature ``CollisionPairIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CollisionPairIndex`` 
    
    :param index: 
    :type index: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    DeleteChainsAtStart: bool = ...
    """
    Returns or sets  the flag which determines if chains are deleted at the beginning of the export 
    
    <hr>
    
    Getter Method
    
    Signature ``DeleteChainsAtStart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DeleteChainsAtStart`` 
    
    :param deleteChainsAtStart: 
    :type deleteChainsAtStart: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    FileName: str = ...
    """
    Returns or sets  the output filename of the SPF file 
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns:  The output name  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param name:  the output new name  
    :type name: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    ListOutput: bool = ...
    """
    Returns or sets  the flag which determines if the output is printed to a listing window 
    
    <hr>
    
    Getter Method
    
    Signature ``ListOutput`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListOutput`` 
    
    :param output: 
    :type output: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    ProtectionAreaElementIndex: int = ...
    """
    Returns or sets  the index used when exporting protection area elements to the SPF file 
    
    <hr>
    
    Getter Method
    
    Signature ``ProtectionAreaElementIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProtectionAreaElementIndex`` 
    
    :param index: 
    :type index: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    ProtectionAreaIndex: int = ...
    """
    Returns or sets  the index used when exporting protection areas to the SPF file 
    
    <hr>
    
    Getter Method
    
    Signature ``ProtectionAreaIndex`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProtectionAreaIndex`` 
    
    :param index: 
    :type index: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    Null: SinumerikCaExportBuilder = ...  # unknown typename


class LoadSnapshotBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.SIM.LoadSnapshotBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateSimulationLoadsnapshotBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def GetSnapshot(self, snapshotName: str, setupName: str) -> Snapshot:
        """
        Returns the snapshot  
        
        Signature ``GetSnapshot(snapshotName, setupName)`` 
        
        :param snapshotName: 
        :type snapshotName: str 
        :param setupName: 
        :type setupName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.Snapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    RunToSimTime: bool = ...
    """
    Returns or sets  the run to simulation time 
    
    <hr>
    
    Getter Method
    
    Signature ``RunToSimTime`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RunToSimTime`` 
    
    :param bRunToTime: 
    :type bRunToTime: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    Null: LoadSnapshotBuilder = ...  # unknown typename


class MachineToolConfigurationTechnologyTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationTechnologyTypes():
    """
    The machine technology types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Mill", "The mill technology type"
       "Turn", "The lathe technology type"
       "Millturn", "The millturn technology type"
       "NotSet", "No technology type"
    """
    Mill = 0  # MachineToolConfigurationTechnologyTypesMemberType
    Turn = 1  # MachineToolConfigurationTechnologyTypesMemberType
    Millturn = 2  # MachineToolConfigurationTechnologyTypesMemberType
    NotSet = 3  # MachineToolConfigurationTechnologyTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfigurationSwivelingTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationSwivelingTypes():
    """
    The machine swiveling types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Cycle800", "The CYCLE800 swiveling type"
       "Transarot", "The TRANS/AROT swiveling type"
    """
    Cycle800 = 0  # MachineToolConfigurationSwivelingTypesMemberType
    Transarot = 1  # MachineToolConfigurationSwivelingTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfigurationControllerLinesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationControllerLines():
    """
    The controller line 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Solutionline", "The solutionline controller line"
       "Powerline", "The powerline controller line"
    """
    Solutionline = 0  # MachineToolConfigurationControllerLinesMemberType
    Powerline = 1  # MachineToolConfigurationControllerLinesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfigurationPlaneTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationPlaneTypes():
    """
    The plane selection types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Operator", "The operator panel plane type"
       "G17", "The G17 plane type"
       "G18", "The G18 plane type"
       "G19", "The G19 plane type"
    """
    Operator = 0  # MachineToolConfigurationPlaneTypesMemberType
    G17 = 1  # MachineToolConfigurationPlaneTypesMemberType
    G18 = 2  # MachineToolConfigurationPlaneTypesMemberType
    G19 = 3  # MachineToolConfigurationPlaneTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfigurationMdynamicsTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationMdynamicsTypes():
    """
    The mdynamics types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fiveaxmill", "The Five Axis Milling MDynamics type"
    """
    Fiveaxmill = 0  # MachineToolConfigurationMdynamicsTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfigurationUnitTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MachineToolConfigurationUnitTypes():
    """
    The units type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Mm", "The millimeter unit type"
       "In", "The inch unit type"
    """
    Mm = 0  # MachineToolConfigurationUnitTypesMemberType
    In = 1  # MachineToolConfigurationUnitTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MachineToolConfiguration(NXOpen.Builder):
    """
    Represents a Machine Tool Configuration object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateMachineToolConfigurationBuilder`
    
    .. versionadded:: NX9.0.3
    """
    
    class TechnologyTypes():
        """
        The machine technology types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Mill", "The mill technology type"
           "Turn", "The lathe technology type"
           "Millturn", "The millturn technology type"
           "NotSet", "No technology type"
        """
        Mill = 0  # MachineToolConfigurationTechnologyTypesMemberType
        Turn = 1  # MachineToolConfigurationTechnologyTypesMemberType
        Millturn = 2  # MachineToolConfigurationTechnologyTypesMemberType
        NotSet = 3  # MachineToolConfigurationTechnologyTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SwivelingTypes():
        """
        The machine swiveling types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Cycle800", "The CYCLE800 swiveling type"
           "Transarot", "The TRANS/AROT swiveling type"
        """
        Cycle800 = 0  # MachineToolConfigurationSwivelingTypesMemberType
        Transarot = 1  # MachineToolConfigurationSwivelingTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ControllerLines():
        """
        The controller line 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Solutionline", "The solutionline controller line"
           "Powerline", "The powerline controller line"
        """
        Solutionline = 0  # MachineToolConfigurationControllerLinesMemberType
        Powerline = 1  # MachineToolConfigurationControllerLinesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PlaneTypes():
        """
        The plane selection types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Operator", "The operator panel plane type"
           "G17", "The G17 plane type"
           "G18", "The G18 plane type"
           "G19", "The G19 plane type"
        """
        Operator = 0  # MachineToolConfigurationPlaneTypesMemberType
        G17 = 1  # MachineToolConfigurationPlaneTypesMemberType
        G18 = 2  # MachineToolConfigurationPlaneTypesMemberType
        G19 = 3  # MachineToolConfigurationPlaneTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MdynamicsTypes():
        """
        The mdynamics types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fiveaxmill", "The Five Axis Milling MDynamics type"
        """
        Fiveaxmill = 0  # MachineToolConfigurationMdynamicsTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class UnitTypes():
        """
        The units type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Mm", "The millimeter unit type"
           "In", "The inch unit type"
        """
        Mm = 0  # MachineToolConfigurationUnitTypesMemberType
        In = 1  # MachineToolConfigurationUnitTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetMachineTechnology(self, channelName: str) -> MachineToolConfigurationTechnologyTypes:
        """
        Retrieves the machine technology  
        
        Signature ``GetMachineTechnology(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The machine technology  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationTechnologyTypes` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetMachineTechnology(self, channelName: str, technology: MachineToolConfigurationTechnologyTypes) -> None:
        """
        Sets the machine technology 
        
        Signature ``SetMachineTechnology(channelName, technology)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param technology:  The new machine technology  
        :type technology: :py:class:`NXOpen.SIM.MachineToolConfigurationTechnologyTypes` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelTcpmSupport(self, channelName: str) -> bool:
        """
        Retrieves machine TCPM support  
        
        Signature ``GetChannelTcpmSupport(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The TCPM support value  
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelTcpmSupport(self, channelName: str, value: bool) -> None:
        """
        Sets the TCPM support value 
        
        Signature ``SetChannelTcpmSupport(channelName, value)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param value:  The new TCPM support value  
        :type value: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelSwiveling(self, channelName: str) -> MachineToolConfigurationSwivelingTypes:
        """
        Retrieves channel's swiveling mode  
        
        Signature ``GetChannelSwiveling(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The swiveling mode value  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationSwivelingTypes` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelSwiveling(self, channelName: str, value: MachineToolConfigurationSwivelingTypes) -> None:
        """
        Sets the channel's swiveling mode 
        
        Signature ``SetChannelSwiveling(channelName, value)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param value:  The new swiveling mode value  
        :type value: :py:class:`NXOpen.SIM.MachineToolConfigurationSwivelingTypes` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelToolAsSubprogram(self, channelName: str) -> bool:
        """
        Retrieves a channel's subprogram support  
        
        Signature ``GetChannelToolAsSubprogram(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The tool as subprogram mode value  
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelToolAsSubprogram(self, channelName: str, value: bool) -> None:
        """
        Sets a channel's subprogram support 
        
        Signature ``SetChannelToolAsSubprogram(channelName, value)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param value:  The new tool as subprogram value  
        :type value: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelToolCommand(self, channelName: str) -> str:
        """
        Retrieves a channel's tool command  
        
        Signature ``GetChannelToolCommand(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The tool command   
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelToolCommand(self, channelName: str, newToolCommand: str) -> None:
        """
        Sets a channel's tool command 
        
        Signature ``SetChannelToolCommand(channelName, newToolCommand)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newToolCommand:  The new tool command  
        :type newToolCommand: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelToolPreselect(self, channelName: str) -> str:
        """
        Retrieves a channel's tool preselect  
        
        Signature ``GetChannelToolPreselect(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The tool preselect   
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelToolPreselect(self, channelName: str, newToolPreselect: str) -> None:
        """
        Sets a channel's tool preselect 
        
        Signature ``SetChannelToolPreselect(channelName, newToolPreselect)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newToolPreselect:  The new tool preselect  
        :type newToolPreselect: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetLookahead(self, channelName: str) -> int:
        """
        Retrieves the controller lookahead, which indicates how many lines are evaluate from the controller ahead.  
        
        Signature ``GetLookahead(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The controller lookahead  
        :rtype: int 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetLookahead(self, channelName: str, lookAhead: int) -> None:
        """
        Sets the controller lookahead, which indicates how many lines are evaluate from the controller ahead.  
        
        Signature ``SetLookahead(channelName, lookAhead)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param lookAhead:  The new controller lookahead  
        :type lookAhead: int 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelPlaneMill(self, channelName: str) -> MachineToolConfigurationPlaneTypes:
        """
        Retrieves the plane mill from a channel  
        
        Signature ``GetChannelPlaneMill(channelName)`` 
        
        :param channelName:  The channel in question  
        :type channelName: str 
        :returns:  The plane mill value  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationPlaneTypes` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelPlaneMill(self, channelName: str, newPlaneMill: MachineToolConfigurationPlaneTypes) -> None:
        """
        Sets the plane mill for a channel 
        
        Signature ``SetChannelPlaneMill(channelName, newPlaneMill)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newPlaneMill:  The new plane mill value  
        :type newPlaneMill: :py:class:`NXOpen.SIM.MachineToolConfigurationPlaneTypes` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetChannelPlaneTurn(self, channelName: str) -> MachineToolConfigurationPlaneTypes:
        """
        Retrieves the plane turn from a channel  
        
        Signature ``GetChannelPlaneTurn(channelName)`` 
        
        :param channelName:  The channel in question  
        :type channelName: str 
        :returns:  The plane turn value  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationPlaneTypes` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    
    
    def SetChannelPlaneTurn(self, channelName: str, newPlaneTurn: MachineToolConfigurationPlaneTypes) -> None:
        """
        Sets the plane turn for a channel 
        
        Signature ``SetChannelPlaneTurn(channelName, newPlaneTurn)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newPlaneTurn:  The new plane turn value  
        :type newPlaneTurn: :py:class:`NXOpen.SIM.MachineToolConfigurationPlaneTypes` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierSwivelMode(self, channelName: str, carrierName: str) -> int:
        """
        Retrieves the swiveling mode for a tool carrier.  
        
        Signature ``GetToolCarrierSwivelMode(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierSwivelMode(self, channelName: str, carrierName: str, newSwivelingMode: int) -> None:
        """
        Sets the swiveling mode for a tool carrier.  
        
        Signature ``SetToolCarrierSwivelMode(channelName, carrierName, newSwivelingMode)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newSwivelingMode:  The new swiveling mode  
        :type newSwivelingMode: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierDirectionSelection(self, channelName: str, carrierName: str) -> int:
        """
        Retrieves the direction selection for a tool carrier.  
        
        Signature ``GetToolCarrierDirectionSelection(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierDirectionSelection(self, channelName: str, carrierName: str, newDirectionSelection: int) -> None:
        """
        Sets the direction selection for a tool carrier.  
        
        Signature ``SetToolCarrierDirectionSelection(channelName, carrierName, newDirectionSelection)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newDirectionSelection:  The new swiveling mode  
        :type newDirectionSelection: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierRetraction(self, channelName: str, carrierName: str) -> int:
        """
        Retrieves the retraction for a tool carrier.  
        
        Signature ``GetToolCarrierRetraction(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierRetraction(self, channelName: str, carrierName: str, newRetraction: int) -> None:
        """
        Sets the retraction for a tool carrier.  
        
        Signature ``SetToolCarrierRetraction(channelName, carrierName, newRetraction)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newRetraction:  The new swiveling mode  
        :type newRetraction: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierXRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
        Retrieves the X retraction position for a tool carrier.  
        
        Signature ``GetToolCarrierXRetractionPosition(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierXRetractionPosition(self, channelName: str, carrierName: str, newXPosition: float) -> None:
        """
        Sets the X retraction position for a tool carrier.  
        
        Signature ``SetToolCarrierXRetractionPosition(channelName, carrierName, newXPosition)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newXPosition:  The new X position  
        :type newXPosition: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierYRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
        Retrieves the Y retraction position for a tool carrier.  
        
        Signature ``GetToolCarrierYRetractionPosition(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierYRetractionPosition(self, channelName: str, carrierName: str, newYPosition: float) -> None:
        """
        Sets the Y retraction position for a tool carrier.  
        
        Signature ``SetToolCarrierYRetractionPosition(channelName, carrierName, newYPosition)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newYPosition:  The new Y position  
        :type newYPosition: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolCarrierZRetractionPosition(self, channelName: str, carrierName: str) -> float:
        """
        Retrieves the Z retraction position for a tool carrier.  
        
        Signature ``GetToolCarrierZRetractionPosition(channelName, carrierName)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to query  
        :type carrierName: str 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolCarrierZRetractionPosition(self, channelName: str, carrierName: str, newZPosition: float) -> None:
        """
        Sets the Z retraction position for a tool carrier.  
        
        Signature ``SetToolCarrierZRetractionPosition(channelName, carrierName, newZPosition)`` 
        
        :param channelName:  The channel to which the carrier belongs  
        :type channelName: str 
        :param carrierName:  The name of the carrier to modify  
        :type carrierName: str 
        :param newZPosition:  The new Z position  
        :type newZPosition: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetMdynamics(self) -> MachineToolConfigurationMdynamicsTypes:
        """
        Retrieve the MDynamics information  
        
        Signature ``GetMdynamics()`` 
        
        :returns:  The mdynamics value  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationMdynamicsTypes` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetMdynamics(self, newMDynamicsValue: MachineToolConfigurationMdynamicsTypes) -> None:
        """
        Sets the Mdynamics value 
        
        Signature ``SetMdynamics(newMDynamicsValue)`` 
        
        :param newMDynamicsValue:  The new mdynamics value  
        :type newMDynamicsValue: :py:class:`NXOpen.SIM.MachineToolConfigurationMdynamicsTypes` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetToolRadiusCompensation(self) -> bool:
        """
        Retrieves the 3D Tool Radius Compensation information  
        
        Signature ``GetToolRadiusCompensation()`` 
        
        :returns:  The Tool Radius value  
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetToolRadiusCompensation(self, newCompensationValue: bool) -> None:
        """
        Sets the 3D Tool Radius Compensation information 
        
        Signature ``SetToolRadiusCompensation(newCompensationValue)`` 
        
        :param newCompensationValue:  The new Tool Radius Compensation value  
        :type newCompensationValue: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetResolutionMm(self) -> float:
        """
        Retrieves the millimeter resolution  
        
        Signature ``GetResolutionMm()`` 
        
        :returns:  The millimeter resolution value  
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetResolutionMm(self, newResolutionValue: float) -> None:
        """
        Sets the millimeter resolution value 
        
        Signature ``SetResolutionMm(newResolutionValue)`` 
        
        :param newResolutionValue:  The new millimeter resolution value  
        :type newResolutionValue: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetResolutionDeg(self) -> float:
        """
        Retrieves the degree resolution  
        
        Signature ``GetResolutionDeg()`` 
        
        :returns:  The degree resolution value  
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetResolutionDeg(self, newResolutionValue: float) -> None:
        """
        Sets the degree resolution value 
        
        Signature ``SetResolutionDeg(newResolutionValue)`` 
        
        :param newResolutionValue:  The new degree resolution value  
        :type newResolutionValue: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetControllerLanguage(self) -> str:
        """
        Retrieves the controller language  
        
        Signature ``GetControllerLanguage()`` 
        
        :returns:  The controller language  
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetControllerLanguage(self, newLanguage: str) -> None:
        """
        Sets the controller language 
        
        Signature ``SetControllerLanguage(newLanguage)`` 
        
        :param newLanguage:  The new controller language  
        :type newLanguage: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetControllerVersion(self) -> str:
        """
        Retrieves the controller version  
        
        Signature ``GetControllerVersion()`` 
        
        :returns:  The controller version  
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetControllerVersion(self, newVersion: str) -> None:
        """
        Sets the controller version 
        
        Signature ``SetControllerVersion(newVersion)`` 
        
        :param newVersion:  The new controller version  
        :type newVersion: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetArchiveControllerType(self) -> int:
        """
        Retrieves the archive controller type  
        
        Signature ``GetArchiveControllerType()`` 
        
        :returns:  The archive controller type  
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetArchiveControllerType(self, newArchiveControllerType: int) -> None:
        """
        Sets the archive controller type 
        
        Signature ``SetArchiveControllerType(newArchiveControllerType)`` 
        
        :param newArchiveControllerType:  The new archive controller type  
        :type newArchiveControllerType: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetArchiveControllerVersion(self) -> str:
        """
        Retrieves the archive controller version  
        
        Signature ``GetArchiveControllerVersion()`` 
        
        :returns:  The archive controller version  
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetArchiveControllerVersion(self, newArchiveControllerVersion: str) -> None:
        """
        Sets the archive controller version 
        
        Signature ``SetArchiveControllerVersion(newArchiveControllerVersion)`` 
        
        :param newArchiveControllerVersion:  The new archive controller version  
        :type newArchiveControllerVersion: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetUsedUnit(self) -> int:
        """
        Retrieves the used unit  
        
        Signature ``GetUsedUnit()`` 
        
        :returns:  The used unit  
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetUsedUnit(self, newUsedUnit: int) -> None:
        """
        Sets the used unit 
        
        Signature ``SetUsedUnit(newUsedUnit)`` 
        
        :param newUsedUnit:  The new used unit  
        :type newUsedUnit: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetCircularPrecision(self, channelName: str) -> float:
        """
        Retrieves the circular precision  
        
        Signature ``GetCircularPrecision(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The circular precision value  
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetCircularPrecision(self, channelName: str, newCircularPrecision: float) -> None:
        """
        Sets the circular precision 
        
        Signature ``SetCircularPrecision(channelName, newCircularPrecision)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newCircularPrecision:  The new circular precision value  
        :type newCircularPrecision: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetCircularPrecisionFactor(self, channelName: str) -> float:
        """
        Retrieves the circular precision factor  
        
        Signature ``GetCircularPrecisionFactor(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The circular precision factor  
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetCircularPrecisionFactor(self, channelName: str, newCircularPrecisionFactor: float) -> None:
        """
        Sets the circular precision factor 
        
        Signature ``SetCircularPrecisionFactor(channelName, newCircularPrecisionFactor)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newCircularPrecisionFactor:  The new circular precision factor  
        :type newCircularPrecisionFactor: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def GetDiameterGeoAxisName(self, channelName: str) -> str:
        """
        Retrieves the diameter geo axis name, which change the output behavior of length values during turning.  
        
        Signature ``GetDiameterGeoAxisName(channelName)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :returns:  The diameter geo axis name  
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDiameterGeoAxisName(self, channelName: str, newDiameterMode: str) -> None:
        """
        Sets the diameter geo axis name, which change the output behavior of length values during turning.  
        
        Signature ``SetDiameterGeoAxisName(channelName, newDiameterMode)`` 
        
        :param channelName:  The channel to modify  
        :type channelName: str 
        :param newDiameterMode:  The new diameter geo axis name  
        :type newDiameterMode: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    ControllerLine: MachineToolConfigurationControllerLines = ...
    """
    Returns or sets  the controller line 
    
    <hr>
    
    Getter Method
    
    Signature ``ControllerLine`` 
    
    :returns:  The controller line  
    :rtype: :py:class:`NXOpen.SIM.MachineToolConfigurationControllerLines` 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ControllerLine`` 
    
    :param line:  The new controller line  
    :type line: :py:class:`NXOpen.SIM.MachineToolConfigurationControllerLines` 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    ControllerType: str = ...
    """
    Returns or sets  the controller type 
    
    <hr>
    
    Getter Method
    
    Signature ``ControllerType`` 
    
    :returns:  The controller type  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ControllerType`` 
    
    :param controllerType:  The new controller type  
    :type controllerType: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    CycleTime: float = ...
    """
    Returns or sets  the cycle time 
    
    <hr>
    
    Getter Method
    
    Signature ``CycleTime`` 
    
    :returns:  The cycle time  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CycleTime`` 
    
    :param cycleTime:  The new cycle time  
    :type cycleTime: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    MachineName: str = ...
    """
    Returns or sets  the machine name 
    
    <hr>
    
    Getter Method
    
    Signature ``MachineName`` 
    
    :returns:  The machine name  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MachineName`` 
    
    :param name:  The new machine name  
    :type name: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    MachineVendor: str = ...
    """
    Returns or sets  the machine vendor 
    
    <hr>
    
    Getter Method
    
    Signature ``MachineVendor`` 
    
    :returns:  The machine vendor  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MachineVendor`` 
    
    :param vendor:  The new machine vendor  
    :type vendor: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    ToolCarrierName: str = ...
    """
    Returns or sets  the tool carrier name 
    
    <hr>
    
    Getter Method
    
    Signature ``ToolCarrierName`` 
    
    :returns:  The tool carrier name  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToolCarrierName`` 
    
    :param carrierName:  The new tool carrier name  
    :type carrierName: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    Null: MachineToolConfiguration = ...  # unknown typename


class KinematicComponent(NXOpen.NXObject):
    """
    Represents the KinematicComponent class object  
    
    Use the :py:class:`NXOpen.SIM.KinematicConfigurator` class to create a KinematicComponent object.
    
    .. versionadded:: NX7.5.0
    """
    
    def InsertComponent(self, newChild: KinematicComponent) -> None:
        """
        Adds a new child component 
        
        Signature ``InsertComponent(newChild)`` 
        
        :param newChild:  The child component to add  
        :type newChild: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def DeleteComponent(self, oldChild: KinematicComponent) -> None:
        """
        Deletes a child component 
        
        Signature ``DeleteComponent(oldChild)`` 
        
        :param oldChild:  The old child component to remove  
        :type oldChild: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def InsertJunction(self, junction: KinematicJunction) -> None:
        """
        Adds a new junction to the component 
        
        Signature ``InsertJunction(junction)`` 
        
        :param junction:  The junction to add  
        :type junction: :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteCaConfigProperties(self) -> None:
        """
        Deletes ca config properties 
        
        Signature ``DeleteCaConfigProperties()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
        """
        ...
    
    
    def GetJunctions(self) -> 'list[KinematicJunction]':
        """
        Gets a list of all junctions in the component 
        
        Signature ``GetJunctions()`` 
        
        :returns:  The list of junctions  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX8.5.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetAxis(self) -> KinematicAxis:
        """
        Gets an axis object in the component  
        
        Signature ``GetAxis()`` 
        
        :returns:  The axis object  
        :rtype: :py:class:`NXOpen.SIM.KinematicAxis` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    Null: KinematicComponent = ...  # unknown typename


class KinematicChannelBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[KinematicChannelBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: KinematicChannelBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
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
    
    
    def FindIndex(self, obj: KinematicChannelBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> KinematicChannelBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
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
    def Erase(self, obj: KinematicChannelBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: KinematicChannelBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
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
    
    
    def GetContents(self) -> 'list[KinematicChannelBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[KinematicChannelBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
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
    def Swap(self, object1: KinematicChannelBuilder, object2: KinematicChannelBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: KinematicChannelBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
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
    Null: KinematicChannelBuilderList = ...  # unknown typename


class SimDebugBuilderDriverTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderDriverType():
    """
    Represents the driver type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Cse", "CSE driver"
       "Mtd", "MTD driver"
    """
    Cse = 0  # SimDebugBuilderDriverTypeMemberType
    Mtd = 1  # SimDebugBuilderDriverTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderUiTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderUiType():
    """
    Represents the ui type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DisplayMomEvent", "Display Mom Event"
       "ShowPartAndTipJunctions", "Show Part And Tip Junction"
       "GenerateSpinningTools", "Generate Spinning Tools"
       "UseHybridGougeChecker", "Use Hybrid Gouge Checker"
       "UseMtbOldDialogs", "Use MTB Old Dialogs"
       "UseFastTicker", "Use Fast Ticker"
       "PrintOutTraceSerialNumbers", "Print Out Trace Serial Numbers"
       "PerformanceDisplayDetail", "Performance Display Detail"
       "PerformanceDisplayTime", "Performance Display Time"
       "PerformanceIndentTime", "Performance Indent Time"
       "PerformanceDisplayData", "Performance Display Data"
       "DctkWriteCollisionPairs", "Write Collision Pairs"
    """
    DisplayMomEvent = 0  # SimDebugBuilderUiTypeMemberType
    ShowPartAndTipJunctions = 1  # SimDebugBuilderUiTypeMemberType
    GenerateSpinningTools = 2  # SimDebugBuilderUiTypeMemberType
    UseHybridGougeChecker = 3  # SimDebugBuilderUiTypeMemberType
    UseMtbOldDialogs = 4  # SimDebugBuilderUiTypeMemberType
    UseFastTicker = 5  # SimDebugBuilderUiTypeMemberType
    PrintOutTraceSerialNumbers = 6  # SimDebugBuilderUiTypeMemberType
    PerformanceDisplayDetail = 7  # SimDebugBuilderUiTypeMemberType
    PerformanceDisplayTime = 8  # SimDebugBuilderUiTypeMemberType
    PerformanceIndentTime = 9  # SimDebugBuilderUiTypeMemberType
    PerformanceDisplayData = 10  # SimDebugBuilderUiTypeMemberType
    DctkWriteCollisionPairs = 11  # SimDebugBuilderUiTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderTraceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderTraceType():
    """
    Represents the trace type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ButtonDown", "Trace Button Down"
       "Vcr", "Trace Vcr"
       "Ipw", "Trace Ipw"
       "Performance", "Trace Performance"
       "Collision", "Trace Collision"
       "Gouge", "Trace Gouge"
       "Highlighting", "Trace Highlighting"
       "Details", "Trace Details"
       "PositionalIsv", "Trace Positional Isv"
       "SpinningNonSpinning", "Trace Spinning Nonspinning"
       "KinematicModel", "Trace Kinematic Model"
       "Event", "Trace Event"
       "LineServer", "Trace Line Server"
       "Sync", "Trace Sync"
       "DctkSettings", "Trace Dctk Settings"
       "DctkMovements", "Trace Dctk Movements"
       "DctkDisplay", "Trace Dctk Display"
       "DctkCollision", "Trace Dctk Collision"
       "ToolPathPicking", "Trace ToolPath Picking"
    """
    ButtonDown = 0  # SimDebugBuilderTraceTypeMemberType
    Vcr = 1  # SimDebugBuilderTraceTypeMemberType
    Ipw = 2  # SimDebugBuilderTraceTypeMemberType
    Performance = 3  # SimDebugBuilderTraceTypeMemberType
    Collision = 4  # SimDebugBuilderTraceTypeMemberType
    Gouge = 5  # SimDebugBuilderTraceTypeMemberType
    Highlighting = 6  # SimDebugBuilderTraceTypeMemberType
    Details = 7  # SimDebugBuilderTraceTypeMemberType
    PositionalIsv = 8  # SimDebugBuilderTraceTypeMemberType
    SpinningNonSpinning = 9  # SimDebugBuilderTraceTypeMemberType
    KinematicModel = 10  # SimDebugBuilderTraceTypeMemberType
    Event = 11  # SimDebugBuilderTraceTypeMemberType
    LineServer = 12  # SimDebugBuilderTraceTypeMemberType
    Sync = 13  # SimDebugBuilderTraceTypeMemberType
    DctkSettings = 14  # SimDebugBuilderTraceTypeMemberType
    DctkMovements = 15  # SimDebugBuilderTraceTypeMemberType
    DctkDisplay = 16  # SimDebugBuilderTraceTypeMemberType
    DctkCollision = 17  # SimDebugBuilderTraceTypeMemberType
    ToolPathPicking = 18  # SimDebugBuilderTraceTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderDumpTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderDumpType():
    """
    Represents the dump type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Dump Nothing"
       "KinematicModel", "Dump Kinematic Model"
       "Highlighting", "Dump Highlighting"
       "Ipw", "Dump IPW"
       "Collision", "Dump Collision"
       "OutputBuffer", "Dump Output Buffer"
       "Time", "Dump Time"
       "Details", "Dump Details"
       "SynchronizeUi", "Dump Synchronize UI"
       "SynchronizeManagerXtp", "Dump SynchronizeManagerXtp"
       "EngineParams", "Dump Engine Params"
       "MomVariables", "Dump Mom Variables"
       "DebugUi", "Dump Debug UI"
       "SimulationSettings", "Dump Simulation Settings"
       "SimManager", "Dump SimManager"
       "PathEvents", "Dump Path Events"
       "MachiningTimeAnalysis", "Dump Machining Time Analysis"
    """
    NotSet = 0  # SimDebugBuilderDumpTypeMemberType
    KinematicModel = 1  # SimDebugBuilderDumpTypeMemberType
    Highlighting = 2  # SimDebugBuilderDumpTypeMemberType
    Ipw = 3  # SimDebugBuilderDumpTypeMemberType
    Collision = 4  # SimDebugBuilderDumpTypeMemberType
    OutputBuffer = 5  # SimDebugBuilderDumpTypeMemberType
    Time = 6  # SimDebugBuilderDumpTypeMemberType
    Details = 7  # SimDebugBuilderDumpTypeMemberType
    SynchronizeUi = 8  # SimDebugBuilderDumpTypeMemberType
    SynchronizeManagerXtp = 9  # SimDebugBuilderDumpTypeMemberType
    EngineParams = 10  # SimDebugBuilderDumpTypeMemberType
    MomVariables = 11  # SimDebugBuilderDumpTypeMemberType
    DebugUi = 12  # SimDebugBuilderDumpTypeMemberType
    SimulationSettings = 13  # SimDebugBuilderDumpTypeMemberType
    SimManager = 14  # SimDebugBuilderDumpTypeMemberType
    PathEvents = 15  # SimDebugBuilderDumpTypeMemberType
    MachiningTimeAnalysis = 16  # SimDebugBuilderDumpTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderOutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderOutputType():
    """
    The output type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Syslog", "Output to syslog"
       "ListingWindow", "Output to listing window"
       "Autotest", "Output to autotest"
       "ToFile", "Output to file"
    """
    Syslog = 0  # SimDebugBuilderOutputTypeMemberType
    ListingWindow = 1  # SimDebugBuilderOutputTypeMemberType
    Autotest = 2  # SimDebugBuilderOutputTypeMemberType
    ToFile = 3  # SimDebugBuilderOutputTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderKinematicModelTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderKinematicModelType():
    """
    Represents the kinematic model type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Main", "Main Kinematic Model"
       "Simulation", "Simulation Kinematic Model"
       "Driver", "Driver Kinematic Model"
    """
    Main = 0  # SimDebugBuilderKinematicModelTypeMemberType
    Simulation = 1  # SimDebugBuilderKinematicModelTypeMemberType
    Driver = 2  # SimDebugBuilderKinematicModelTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilderPrintoutTagsOrPointersTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SimDebugBuilderPrintoutTagsOrPointersType():
    """
    Represents the printout tags or pointers type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Boolean", "Boolean"
       "Value", "Value"
       "Name", "Name"
    """
    Boolean = 0  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
    Value = 1  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
    Name = 2  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SimDebugBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.SIM.SimDebugBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateSimDebugBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class DriverType():
        """
        Represents the driver type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Cse", "CSE driver"
           "Mtd", "MTD driver"
        """
        Cse = 0  # SimDebugBuilderDriverTypeMemberType
        Mtd = 1  # SimDebugBuilderDriverTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class UiType():
        """
        Represents the ui type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DisplayMomEvent", "Display Mom Event"
           "ShowPartAndTipJunctions", "Show Part And Tip Junction"
           "GenerateSpinningTools", "Generate Spinning Tools"
           "UseHybridGougeChecker", "Use Hybrid Gouge Checker"
           "UseMtbOldDialogs", "Use MTB Old Dialogs"
           "UseFastTicker", "Use Fast Ticker"
           "PrintOutTraceSerialNumbers", "Print Out Trace Serial Numbers"
           "PerformanceDisplayDetail", "Performance Display Detail"
           "PerformanceDisplayTime", "Performance Display Time"
           "PerformanceIndentTime", "Performance Indent Time"
           "PerformanceDisplayData", "Performance Display Data"
           "DctkWriteCollisionPairs", "Write Collision Pairs"
        """
        DisplayMomEvent = 0  # SimDebugBuilderUiTypeMemberType
        ShowPartAndTipJunctions = 1  # SimDebugBuilderUiTypeMemberType
        GenerateSpinningTools = 2  # SimDebugBuilderUiTypeMemberType
        UseHybridGougeChecker = 3  # SimDebugBuilderUiTypeMemberType
        UseMtbOldDialogs = 4  # SimDebugBuilderUiTypeMemberType
        UseFastTicker = 5  # SimDebugBuilderUiTypeMemberType
        PrintOutTraceSerialNumbers = 6  # SimDebugBuilderUiTypeMemberType
        PerformanceDisplayDetail = 7  # SimDebugBuilderUiTypeMemberType
        PerformanceDisplayTime = 8  # SimDebugBuilderUiTypeMemberType
        PerformanceIndentTime = 9  # SimDebugBuilderUiTypeMemberType
        PerformanceDisplayData = 10  # SimDebugBuilderUiTypeMemberType
        DctkWriteCollisionPairs = 11  # SimDebugBuilderUiTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TraceType():
        """
        Represents the trace type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ButtonDown", "Trace Button Down"
           "Vcr", "Trace Vcr"
           "Ipw", "Trace Ipw"
           "Performance", "Trace Performance"
           "Collision", "Trace Collision"
           "Gouge", "Trace Gouge"
           "Highlighting", "Trace Highlighting"
           "Details", "Trace Details"
           "PositionalIsv", "Trace Positional Isv"
           "SpinningNonSpinning", "Trace Spinning Nonspinning"
           "KinematicModel", "Trace Kinematic Model"
           "Event", "Trace Event"
           "LineServer", "Trace Line Server"
           "Sync", "Trace Sync"
           "DctkSettings", "Trace Dctk Settings"
           "DctkMovements", "Trace Dctk Movements"
           "DctkDisplay", "Trace Dctk Display"
           "DctkCollision", "Trace Dctk Collision"
           "ToolPathPicking", "Trace ToolPath Picking"
        """
        ButtonDown = 0  # SimDebugBuilderTraceTypeMemberType
        Vcr = 1  # SimDebugBuilderTraceTypeMemberType
        Ipw = 2  # SimDebugBuilderTraceTypeMemberType
        Performance = 3  # SimDebugBuilderTraceTypeMemberType
        Collision = 4  # SimDebugBuilderTraceTypeMemberType
        Gouge = 5  # SimDebugBuilderTraceTypeMemberType
        Highlighting = 6  # SimDebugBuilderTraceTypeMemberType
        Details = 7  # SimDebugBuilderTraceTypeMemberType
        PositionalIsv = 8  # SimDebugBuilderTraceTypeMemberType
        SpinningNonSpinning = 9  # SimDebugBuilderTraceTypeMemberType
        KinematicModel = 10  # SimDebugBuilderTraceTypeMemberType
        Event = 11  # SimDebugBuilderTraceTypeMemberType
        LineServer = 12  # SimDebugBuilderTraceTypeMemberType
        Sync = 13  # SimDebugBuilderTraceTypeMemberType
        DctkSettings = 14  # SimDebugBuilderTraceTypeMemberType
        DctkMovements = 15  # SimDebugBuilderTraceTypeMemberType
        DctkDisplay = 16  # SimDebugBuilderTraceTypeMemberType
        DctkCollision = 17  # SimDebugBuilderTraceTypeMemberType
        ToolPathPicking = 18  # SimDebugBuilderTraceTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DumpType():
        """
        Represents the dump type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Dump Nothing"
           "KinematicModel", "Dump Kinematic Model"
           "Highlighting", "Dump Highlighting"
           "Ipw", "Dump IPW"
           "Collision", "Dump Collision"
           "OutputBuffer", "Dump Output Buffer"
           "Time", "Dump Time"
           "Details", "Dump Details"
           "SynchronizeUi", "Dump Synchronize UI"
           "SynchronizeManagerXtp", "Dump SynchronizeManagerXtp"
           "EngineParams", "Dump Engine Params"
           "MomVariables", "Dump Mom Variables"
           "DebugUi", "Dump Debug UI"
           "SimulationSettings", "Dump Simulation Settings"
           "SimManager", "Dump SimManager"
           "PathEvents", "Dump Path Events"
           "MachiningTimeAnalysis", "Dump Machining Time Analysis"
        """
        NotSet = 0  # SimDebugBuilderDumpTypeMemberType
        KinematicModel = 1  # SimDebugBuilderDumpTypeMemberType
        Highlighting = 2  # SimDebugBuilderDumpTypeMemberType
        Ipw = 3  # SimDebugBuilderDumpTypeMemberType
        Collision = 4  # SimDebugBuilderDumpTypeMemberType
        OutputBuffer = 5  # SimDebugBuilderDumpTypeMemberType
        Time = 6  # SimDebugBuilderDumpTypeMemberType
        Details = 7  # SimDebugBuilderDumpTypeMemberType
        SynchronizeUi = 8  # SimDebugBuilderDumpTypeMemberType
        SynchronizeManagerXtp = 9  # SimDebugBuilderDumpTypeMemberType
        EngineParams = 10  # SimDebugBuilderDumpTypeMemberType
        MomVariables = 11  # SimDebugBuilderDumpTypeMemberType
        DebugUi = 12  # SimDebugBuilderDumpTypeMemberType
        SimulationSettings = 13  # SimDebugBuilderDumpTypeMemberType
        SimManager = 14  # SimDebugBuilderDumpTypeMemberType
        PathEvents = 15  # SimDebugBuilderDumpTypeMemberType
        MachiningTimeAnalysis = 16  # SimDebugBuilderDumpTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OutputType():
        """
        The output type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Syslog", "Output to syslog"
           "ListingWindow", "Output to listing window"
           "Autotest", "Output to autotest"
           "ToFile", "Output to file"
        """
        Syslog = 0  # SimDebugBuilderOutputTypeMemberType
        ListingWindow = 1  # SimDebugBuilderOutputTypeMemberType
        Autotest = 2  # SimDebugBuilderOutputTypeMemberType
        ToFile = 3  # SimDebugBuilderOutputTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class KinematicModelType():
        """
        Represents the kinematic model type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Main", "Main Kinematic Model"
           "Simulation", "Simulation Kinematic Model"
           "Driver", "Driver Kinematic Model"
        """
        Main = 0  # SimDebugBuilderKinematicModelTypeMemberType
        Simulation = 1  # SimDebugBuilderKinematicModelTypeMemberType
        Driver = 2  # SimDebugBuilderKinematicModelTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PrintoutTagsOrPointersType():
        """
        Represents the printout tags or pointers type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Boolean", "Boolean"
           "Value", "Value"
           "Name", "Name"
        """
        Boolean = 0  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
        Value = 1  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
        Name = 2  # SimDebugBuilderPrintoutTagsOrPointersTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetUiSetting(self, type: SimDebugBuilderUiType) -> bool:
        """
        Gets the debug setting  
        
        Signature ``GetUiSetting(type)`` 
        
        :param type:  The ui type 
        :type type: :py:class:`NXOpen.SIM.SimDebugBuilderUiType` 
        :returns:  The state 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUiSetting(self, type: SimDebugBuilderUiType, state: bool) -> None:
        """
        Sets the debug setting 
        
        Signature ``SetUiSetting(type, state)`` 
        
        :param type:  The ui type 
        :type type: :py:class:`NXOpen.SIM.SimDebugBuilderUiType` 
        :param state:  The state 
        :type state: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetTrace(self, type: SimDebugBuilderTraceType) -> bool:
        """
        Gets the trace  
        
        Signature ``GetTrace(type)`` 
        
        :param type:  The trace type 
        :type type: :py:class:`NXOpen.SIM.SimDebugBuilderTraceType` 
        :returns:  The state 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetTrace(self, type: SimDebugBuilderTraceType, state: bool) -> None:
        """
        Sets the trace 
        
        Signature ``SetTrace(type, state)`` 
        
        :param type:  The trace type 
        :type type: :py:class:`NXOpen.SIM.SimDebugBuilderTraceType` 
        :param state:  The state 
        :type state: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ShowKinematicModelState(self) -> None:
        """
        Show the kinematic model state 
        
        Signature ``ShowKinematicModelState()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Driver: SimDebugBuilderDriverType = ...
    """
    Returns or sets  the driver 
    
    <hr>
    
    Getter Method
    
    Signature ``Driver`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilderDriverType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Driver`` 
    
    :param type:  The driver type 
    :type type: :py:class:`NXOpen.SIM.SimDebugBuilderDriverType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    Dump: SimDebugBuilderDumpType = ...
    """
    Returns or sets  the dump 
    
    <hr>
    
    Getter Method
    
    Signature ``Dump`` 
    
    :returns:  The dump type 
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilderDumpType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dump`` 
    
    :param type:  The dump type 
    :type type: :py:class:`NXOpen.SIM.SimDebugBuilderDumpType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    DumpOutput: SimDebugBuilderOutputType = ...
    """
    Returns or sets  the dump output 
    
    <hr>
    
    Getter Method
    
    Signature ``DumpOutput`` 
    
    :returns:  The dump output type 
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilderOutputType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DumpOutput`` 
    
    :param type:  The dump output type 
    :type type: :py:class:`NXOpen.SIM.SimDebugBuilderOutputType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    DumpToFileName: str = ...
    """
    Returns or sets  the output filename 
    
    <hr>
    
    Getter Method
    
    Signature ``DumpToFileName`` 
    
    :returns:  The output name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    
    <hr>
    
    Setter Method
    
    Signature ``DumpToFileName`` 
    
    :param name:  the output new name  
    :type name: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    KinematicModel: SimDebugBuilderKinematicModelType = ...
    """
    Returns or sets  the kinematic model 
    
    <hr>
    
    Getter Method
    
    Signature ``KinematicModel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilderKinematicModelType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``KinematicModel`` 
    
    :param type:  The kinematic model type 
    :type type: :py:class:`NXOpen.SIM.SimDebugBuilderKinematicModelType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    PrintoutTags: SimDebugBuilderPrintoutTagsOrPointersType = ...
    """
    Returns or sets  the printout tags type 
    
    <hr>
    
    Getter Method
    
    Signature ``PrintoutTags`` 
    
    :returns:  The printout tags type 
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilderPrintoutTagsOrPointersType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrintoutTags`` 
    
    :param type:  The printout tags type 
    :type type: :py:class:`NXOpen.SIM.SimDebugBuilderPrintoutTagsOrPointersType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    Null: SimDebugBuilder = ...  # unknown typename


class Snapshot(NXOpen.NXObject):
    """
    Represents the Snapshot class object  
    
    Use the :py:class:`NXOpen.SIM.Snapshot` class to create a Snapshot object.
    
    .. versionadded:: NX12.0.0
    """
    Null: Snapshot = ...  # unknown typename


class IsvControlPanelBuilderVisualizationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IsvControlPanelBuilderVisualizationType():
    """
    The Visualization type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MachineCodeSimulateCse", "Machine Code Simulate Cse"
       "MachineCodeSimulateMtd", "Machine Code Simulate Mtd"
       "ToolPathSimulation", "Tool Path Simulate"
    """
    MachineCodeSimulateCse = 0  # IsvControlPanelBuilderVisualizationTypeMemberType
    MachineCodeSimulateMtd = 1  # IsvControlPanelBuilderVisualizationTypeMemberType
    ToolPathSimulation = 2  # IsvControlPanelBuilderVisualizationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IsvControlPanelBuilderSingleStepTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IsvControlPanelBuilderSingleStepType():
    """
    The Single Step type that used in :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.MachineCodeSimulateMtd  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` or
    :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.ToolPathSimulation  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` simulation mode.
    The following :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepType` members are removed in NX10.0.2:
    - StepOut
    - StepIn
    - Display
    Replacement:
    Use the following :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType` member instead:
    - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.StepOut  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
    - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.StepIn  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
    - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.DisplayUpdate  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Block", "Block"
       "Move", "Move"
       "Event", "Event"
    """
    Block = 0  # IsvControlPanelBuilderSingleStepTypeMemberType
    Move = 1  # IsvControlPanelBuilderSingleStepTypeMemberType
    Event = 2  # IsvControlPanelBuilderSingleStepTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IsvControlPanelBuilderSingleStepModeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IsvControlPanelBuilderSingleStepModeType():
    """
    The Single Step Mode type that used in :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.MachineCodeSimulateCse  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` simulation mode.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "StepIn", "Step In"
       "StepOver", "Step Over"
       "StepOut", "Step Out"
       "DisplayUpdate", "Display"
    """
    StepIn = 0  # IsvControlPanelBuilderSingleStepModeTypeMemberType
    StepOver = 1  # IsvControlPanelBuilderSingleStepModeTypeMemberType
    StepOut = 2  # IsvControlPanelBuilderSingleStepModeTypeMemberType
    DisplayUpdate = 3  # IsvControlPanelBuilderSingleStepModeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IsvControlPanelBuilderDetailTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IsvControlPanelBuilderDetailType():
    """
    Type of record reported in the Simulation Details group 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Info", "Info"
       "Limit", "Limit"
       "Collision", "Collision"
       "Gouge", "Gouge"
       "Singularity", "Singularity"
    """
    Info = 0  # IsvControlPanelBuilderDetailTypeMemberType
    Limit = 1  # IsvControlPanelBuilderDetailTypeMemberType
    Collision = 2  # IsvControlPanelBuilderDetailTypeMemberType
    Gouge = 3  # IsvControlPanelBuilderDetailTypeMemberType
    Singularity = 4  # IsvControlPanelBuilderDetailTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IsvControlPanelBuilderVncModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class IsvControlPanelBuilderVncMode():
    """
    Type of VNC Mode  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Error", "ERROR"
       "Notconnected", "NOT CONNECTED"
       "Connected", "CONNECTED"
       "Booted", "BOOTED"
       "Configured", "CONFIGURED"
       "Initialized", "INITIALIZED"
       "ProgramsLoaded", "PROGRAMS LOADED"
       "Reset", "RESET"
       "Stop", "STOP"
       "Start", "START"
       "Run", "RUN"
    """
    Error = -1  # IsvControlPanelBuilderVncModeMemberType
    Notconnected = 0  # IsvControlPanelBuilderVncModeMemberType
    Connected = 1  # IsvControlPanelBuilderVncModeMemberType
    Booted = 2  # IsvControlPanelBuilderVncModeMemberType
    Configured = 3  # IsvControlPanelBuilderVncModeMemberType
    Initialized = 4  # IsvControlPanelBuilderVncModeMemberType
    ProgramsLoaded = 5  # IsvControlPanelBuilderVncModeMemberType
    Reset = 6  # IsvControlPanelBuilderVncModeMemberType
    Stop = 7  # IsvControlPanelBuilderVncModeMemberType
    Start = 8  # IsvControlPanelBuilderVncModeMemberType
    Run = 9  # IsvControlPanelBuilderVncModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class IsvControlPanelBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.SIM.IsvControlPanelBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateIsvControlPanelBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class VisualizationType():
        """
        The Visualization type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MachineCodeSimulateCse", "Machine Code Simulate Cse"
           "MachineCodeSimulateMtd", "Machine Code Simulate Mtd"
           "ToolPathSimulation", "Tool Path Simulate"
        """
        MachineCodeSimulateCse = 0  # IsvControlPanelBuilderVisualizationTypeMemberType
        MachineCodeSimulateMtd = 1  # IsvControlPanelBuilderVisualizationTypeMemberType
        ToolPathSimulation = 2  # IsvControlPanelBuilderVisualizationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SingleStepType():
        """
        The Single Step type that used in :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.MachineCodeSimulateMtd  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` or
        :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.ToolPathSimulation  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` simulation mode.
        The following :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepType` members are removed in NX10.0.2:
        - StepOut
        - StepIn
        - Display
        Replacement:
        Use the following :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType` member instead:
        - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.StepOut  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
        - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.StepIn  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
        - :py:class:` NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType.DisplayUpdate  < NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType>`
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Block", "Block"
           "Move", "Move"
           "Event", "Event"
        """
        Block = 0  # IsvControlPanelBuilderSingleStepTypeMemberType
        Move = 1  # IsvControlPanelBuilderSingleStepTypeMemberType
        Event = 2  # IsvControlPanelBuilderSingleStepTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SingleStepModeType():
        """
        The Single Step Mode type that used in :py:class:` NXOpen.SIM.IsvControlPanelBuilderVisualizationType.MachineCodeSimulateCse  < NXOpen.SIM.IsvControlPanelBuilderVisualizationType>` simulation mode.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "StepIn", "Step In"
           "StepOver", "Step Over"
           "StepOut", "Step Out"
           "DisplayUpdate", "Display"
        """
        StepIn = 0  # IsvControlPanelBuilderSingleStepModeTypeMemberType
        StepOver = 1  # IsvControlPanelBuilderSingleStepModeTypeMemberType
        StepOut = 2  # IsvControlPanelBuilderSingleStepModeTypeMemberType
        DisplayUpdate = 3  # IsvControlPanelBuilderSingleStepModeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DetailType():
        """
        Type of record reported in the Simulation Details group 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Info", "Info"
           "Limit", "Limit"
           "Collision", "Collision"
           "Gouge", "Gouge"
           "Singularity", "Singularity"
        """
        Info = 0  # IsvControlPanelBuilderDetailTypeMemberType
        Limit = 1  # IsvControlPanelBuilderDetailTypeMemberType
        Collision = 2  # IsvControlPanelBuilderDetailTypeMemberType
        Gouge = 3  # IsvControlPanelBuilderDetailTypeMemberType
        Singularity = 4  # IsvControlPanelBuilderDetailTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class VncMode():
        """
        Type of VNC Mode  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Error", "ERROR"
           "Notconnected", "NOT CONNECTED"
           "Connected", "CONNECTED"
           "Booted", "BOOTED"
           "Configured", "CONFIGURED"
           "Initialized", "INITIALIZED"
           "ProgramsLoaded", "PROGRAMS LOADED"
           "Reset", "RESET"
           "Stop", "STOP"
           "Start", "START"
           "Run", "RUN"
        """
        Error = -1  # IsvControlPanelBuilderVncModeMemberType
        Notconnected = 0  # IsvControlPanelBuilderVncModeMemberType
        Connected = 1  # IsvControlPanelBuilderVncModeMemberType
        Booted = 2  # IsvControlPanelBuilderVncModeMemberType
        Configured = 3  # IsvControlPanelBuilderVncModeMemberType
        Initialized = 4  # IsvControlPanelBuilderVncModeMemberType
        ProgramsLoaded = 5  # IsvControlPanelBuilderVncModeMemberType
        Reset = 6  # IsvControlPanelBuilderVncModeMemberType
        Stop = 7  # IsvControlPanelBuilderVncModeMemberType
        Start = 8  # IsvControlPanelBuilderVncModeMemberType
        Run = 9  # IsvControlPanelBuilderVncModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetVisualization(self) -> IsvControlPanelBuilderVisualizationType:
        """
        Gets the visualization 
        
        Signature ``GetVisualization()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVisualizationType` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetVisualization(self, type: IsvControlPanelBuilderVisualizationType) -> None:
        """
        Sets the visualization 
        
        Signature ``SetVisualization(type)`` 
        
        :param type:  The visualization type 
        :type type: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVisualizationType` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetShow3dMaterialRemoval(self) -> bool:
        """
        Gets the show 3d material removal 
        
        Signature ``GetShow3dMaterialRemoval()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetShow3dMaterialRemoval(self, state: bool) -> int:
        """
        Sets the show 3d material removal  
        
        Signature ``SetShow3dMaterialRemoval(state)`` 
        
        :param state:  The state 
        :type state: bool 
        :returns:  The dialog response, 
        if the user don't define workpiece the autoblock dialog will displayed.
        And if the user cancel it the response is UGII_CANCEL 
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetShowToolPath(self) -> bool:
        """
        Gets the show tool path 
        
        Signature ``GetShowToolPath()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetShowToolPath(self, state: bool) -> None:
        """
        Sets the show tool path 
        
        Signature ``SetShowToolPath(state)`` 
        
        :param state:  The state 
        :type state: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetSingleStep(self) -> IsvControlPanelBuilderSingleStepType:
        """
        Gets the single step in Tool Path Based Simulation 
        
        Signature ``GetSingleStep()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepType` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSingleStep(self, type: IsvControlPanelBuilderSingleStepType) -> None:
        """
        Sets the single step in Tool Path Based Simulation
        
        Signature ``SetSingleStep(type)`` 
        
        :param type:  The single step type 
        :type type: :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepType` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetSingleStepMode(self) -> IsvControlPanelBuilderSingleStepModeType:
        """
        Gets the single step mode in Machine Code Simulation 
        
        Signature ``GetSingleStepMode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    
    
    def SetSingleStepMode(self, type: IsvControlPanelBuilderSingleStepModeType) -> None:
        """
        Sets the single step mode in Machine Code Simulation
        
        Signature ``SetSingleStepMode(type)`` 
        
        :param type:  The single step mode type 
        :type type: :py:class:`NXOpen.SIM.IsvControlPanelBuilderSingleStepModeType` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def PlayToMachineTime(self, machineTime: str) -> None:
        """
        Play to Machine Time
        
        Signature ``PlayToMachineTime(machineTime)`` 
        
        :param machineTime:  The machine time in hh:mm:ss.s format 
        :type machineTime: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def PlayForward(self) -> None:
        """
        Simulation Control Panel: Play Forward
        
        Signature ``PlayForward()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def PlayBackward(self) -> None:
        """
        Simulation Control Panel: Play Backward
        
        Signature ``PlayBackward()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SingleStepForward(self) -> None:
        """
        Simulation Control Panel: Single Step Forward
        
        Signature ``SingleStepForward()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def AddIsInHistoryBuffer(self, handler: typing.Callable) -> int:
        """
        Registers the IsInHistoryBufferChanged callback.  
        
        Signature ``AddIsInHistoryBuffer(handler)`` 
        
        :param handler: 
        :type handler: CallableObject 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def RemoveIsInHistoryBuffer(self, handlerId: int) -> bool:
        """
        Unregisters the IsInHistoryBufferChanged callback.  
        
        Signature ``RemoveIsInHistoryBuffer(handlerId)`` 
        
        :param handlerId: 
        :type handlerId: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def AddVncStatus(self, handler: typing.Callable) -> int:
        """
        Registers the VNC Status callback.  
        
        Signature ``AddVncStatus(handler)`` 
        
        :param handler: 
        :type handler: CallableObject 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def RemoveVncStatus(self, handlerId: int) -> bool:
        """
        Unregisters the VNC Status callback.  
        
        Signature ``RemoveVncStatus(handlerId)`` 
        
        :param handlerId: 
        :type handlerId: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def AddSimStop(self, handler: typing.Callable) -> int:
        """
        Registers the SimStop callback.  
        
        Signature ``AddSimStop(handler)`` 
        
        :param handler: 
        :type handler: CallableObject 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def RemoveSimStop(self, handlerId: int) -> bool:
        """
        Unregisters the SimStop callback.  
        
        Signature ``RemoveSimStop(handlerId)`` 
        
        :param handlerId: 
        :type handlerId: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def AddSimEnd(self, handler: typing.Callable) -> int:
        """
        Registers the SimEnd callback.  
        
        Signature ``AddSimEnd(handler)`` 
        
        :param handler: 
        :type handler: CallableObject 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def RemoveSimEnd(self, handlerId: int) -> bool:
        """
        Unregisters the SimEnd callback.  
        
        Signature ``RemoveSimEnd(handlerId)`` 
        
        :param handlerId: 
        :type handlerId: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SingleStepBackward(self) -> None:
        """
        Simulation Control Panel: Single Step Backward
        
        Signature ``SingleStepBackward()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def StepToNextOperation(self) -> None:
        """
        Simulation Control Panel: Step to Next Operation
        
        Signature ``StepToNextOperation()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def StepToPreviousOperation(self) -> None:
        """
        Simulation Control Panel: Step to Previous Operation
        
        Signature ``StepToPreviousOperation()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SetSpeed(self, simSpeed: int) -> None:
        """
        Simulation Control Panel: Simulation Speed
        
        Signature ``SetSpeed(simSpeed)`` 
        
        :param simSpeed:  The simulation speed 
        :type simSpeed: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def JumpToMachineTime(self, machineTime: str) -> None:
        """
        Jump to machine time
        
        Signature ``JumpToMachineTime(machineTime)`` 
        
        :param machineTime:  The machine time in hh:mm:ss.s format 
        :type machineTime: str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def JumpToDetailsLine(self, line: int) -> None:
        """
        Jump to details line
        
        Signature ``JumpToDetailsLine(line)`` 
        
        :param line:  The details window line 
        :type line: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    @typing.overload
    def JumpToNcProgramLine(self, line: int) -> None:
        """
        Jump to nc program line in the active channel
        
        Signature ``JumpToNcProgramLine(line)`` 
        
        :param line:  The nc program window line 
        :type line: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def JumpToNcProgramLine(self, channelName: str, line: int) -> None:
        """
        Jump to nc program line in the specified channel
        
        Signature ``JumpToNcProgramLine(channelName, line)`` 
        
        :param channelName:  The channel name. If this is None or empty the active channel will be used. 
        :type channelName: str 
        :param line:  The nc program line 
        :type line: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SetCurrentProgramLine(self, channelName: str, line: int) -> None:
        """
        Set execution cursor to nc program line in the specified channel
        
        Signature ``SetCurrentProgramLine(channelName, line)`` 
        
        :param channelName:  The channel name. If this is None or empty the active channel will be used. 
        :type channelName: str 
        :param line:  The nc program line 
        :type line: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetMachiningTimeAnalysisClock(self, channelName: str) -> TimeAnalysis:
        """
        Return the Machining Time Analysis Clock for the specified channel.  
        
        Signature ``GetMachiningTimeAnalysisClock(channelName)`` 
        
        :param channelName:  The channel name. 
        :type channelName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.TimeAnalysis` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ApplySimulationOptions(self) -> None:
        """
        Apply the simulation options
        
        Signature ``ApplySimulationOptions()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ResetMachine(self) -> None:
        """
        Simulation Control Panel: (Full) Reset Machine
        
        Signature ``ResetMachine()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetDetailCount(self, type: IsvControlPanelBuilderDetailType) -> int:
        """
        Return the number of Details of the specified type  
        
        Signature ``GetDetailCount(type)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.SIM.IsvControlPanelBuilderDetailType` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetDetail(self, type: IsvControlPanelBuilderDetailType, position: int) -> tuple:
        """
        Return the Details Information to a specified type  
        
        Signature ``GetDetail(type, position)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.SIM.IsvControlPanelBuilderDetailType` 
        :param position: 
        :type position: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (result, time, description, ncLine, programName, channelName). result is a bool. time is a float. description is a str. ncLine is a int. programName is a str. channelName is a str. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    @typing.overload
    def MachineControlResetNc(self) -> None:
        """
        Machine Control Panel: NC Reset for all channels
        
        Signature ``MachineControlResetNc()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def MachineControlResetNc(self, channels: 'list[str]') -> None:
        """
        Machine Control Panel: NC Reset for specific channels
        
        Signature ``MachineControlResetNc(channels)`` 
        
        :param channels: 
        :type channels: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlResetPart(self) -> None:
        """
        Machine Control Panel: Reset Part
        
        Signature ``MachineControlResetPart()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlResetMachine(self) -> None:
        """
        Machine Control Panel: Fast Reset Machine
        
        Signature ``MachineControlResetMachine()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    @typing.overload
    def MachineControlClearAlarm(self) -> None:
        """
        Machine Control Panel: Clear Alarms for all channels
        
        Signature ``MachineControlClearAlarm()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def MachineControlClearAlarm(self, channels: 'list[str]') -> None:
        """
        Machine Control Panel: Clear Alarms for specific channels
        
        Signature ``MachineControlClearAlarm(channels)`` 
        
        :param channels: 
        :type channels: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlShowHmi(self) -> None:
        """
        Machine Control Panel: Show HMI
        
        Signature ``MachineControlShowHmi()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlSingleBlockMode(self, enable: bool) -> None:
        """
        Machine Control Panel: Activate Machine Single Block Mode
        
        Signature ``MachineControlSingleBlockMode(enable)`` 
        
        :param enable:  Enable or disable the single block mode 
        :type enable: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlDryRun(self, enable: bool) -> None:
        """
        Machine Control Panel: Activate Machine Dry Run
        
        Signature ``MachineControlDryRun(enable)`` 
        
        :param enable:  Enable or disable the dry run 
        :type enable: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlFeedRateOverride(self, value: int) -> None:
        """
        Machine Control Panel: Sets Machine Feed Rate Override
        
        Signature ``MachineControlFeedRateOverride(value)`` 
        
        :param value:  The feed rate override value 
        :type value: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlSaveMachineData(self) -> None:
        """
        Machine Control Panel: Save the Machine Data (SRAM)
        
        Signature ``MachineControlSaveMachineData()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlResetMachineData(self) -> None:
        """
        Machine Control Panel: Reset the Machine Data (SRAM) to the library Machine Data (SRAM)
        
        Signature ``MachineControlResetMachineData()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def Stop(self) -> None:
        """
        Simulation Control Panel: Stop the simulation
        
        Signature ``Stop()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlGetFeedRateOverrideMaximumValue(self) -> int:
        """
        Machine Control Panel: Gets the Machine Feed Rate Override Maximum Value 
        
        Signature ``MachineControlGetFeedRateOverrideMaximumValue()`` 
        
        :returns:  The feed rate override max value 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlGetCycleTime(self) -> int:
        """
        Gets the Machine Cycle Time 
        
        Signature ``MachineControlGetCycleTime()`` 
        
        :returns:  The cycle time in ms 
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlWriteVariable(self, channelName: str, variableName: str, variableValue: str, variableType: str) -> bool:
        """
        Write Variable e.  
        
        g. VDI Variable, Machine Data 
        
        Signature ``MachineControlWriteVariable(channelName, variableName, variableValue, variableType)`` 
        
        :param channelName:  The channel name, NULL or empty means all channels 
        :type channelName: str 
        :param variableName:  The variable name 
        :type variableName: str 
        :param variableValue:  The variable value 
        :type variableValue: str 
        :param variableType:  The variable type: VDI_SWITCH, VDI_INTEGER, VDI_SINGLESTEP 
        :type variableType: str 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlReadVariable(self, channelName: str, variableName: str) -> tuple:
        """
        Read Variable e.  
        
        g. VDI Variable, Machine Data 
        
        Signature ``MachineControlReadVariable(channelName, variableName)`` 
        
        :param channelName:  The channel name, NULL or empty means all channels 
        :type channelName: str 
        :param variableName:  The variable name 
        :type variableName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (success, variableValue, variableType). success is a bool. variableValue is a str.   The variable valuevariableType is a str.   The variable type: VDI_SWITCH, VDI_INTEGER, VDI_SINGLESTEP
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlGetChannels(self) -> 'list[str]':
        """
        Gets the Channel Names 
        
        Signature ``MachineControlGetChannels()`` 
        
        :returns:  the names of available channel  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    @typing.overload
    def MachineControlStopNc(self) -> None:
        """
        Machine Control Panel: NC Stop for all channels
        
        Signature ``MachineControlStopNc()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def MachineControlStopNc(self, channels: 'list[str]') -> None:
        """
        Machine Control Panel: NC Stop for specific channels
        
        Signature ``MachineControlStopNc(channels)`` 
        
        :param channels: 
        :type channels: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    @typing.overload
    def MachineControlStartNc(self) -> None:
        """
        Machine Control Panel: NC Start for all channels
        
        Signature ``MachineControlStartNc()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def MachineControlStartNc(self, channels: 'list[str]') -> None:
        """
        Machine Control Panel: NC Start for specific channels
        
        Signature ``MachineControlStartNc(channels)`` 
        
        :param channels: 
        :type channels: list of str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlBootVnck(self) -> bool:
        """
        Machine Control Panel: Boot the VNCK
        Once booted, the vnck-machine remains booted until the part is closed or a 'machine replace' is executed.
        To shut down the vnck-machine manually, :py:meth:`NXOpen.SIM.IsvControlPanelBuilder.MachineControlShutdownVnck()` can be invoked.
        
        The new behavior eliminates the wait required to start the machine. However, it happens that the machine must be restarted. 
        For this purpose :py:meth:`NXOpen.SIM.IsvControlPanelBuilder.MachineControlShutdownVnck()` and :py:meth:`NXOpen.SIM.IsvControlPanelBuilder.MachineControlBootVnck()` can be successively invoked.
        
        Signature ``MachineControlBootVnck()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def MachineControlShutdownVnck(self) -> None:
        """
        Machine Control Panel: Shut down the VNCK
        Used in conjunction with :py:meth:`NXOpen.SIM.IsvControlPanelBuilder.MachineControlBootVnck()`.
        
        Signature ``MachineControlShutdownVnck()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SaveSettingsToFile(self, filename: str) -> None:
        """
        Save simulation settings to xml file 
        
        Signature ``SaveSettingsToFile(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX9.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ReadSettingsFromFile(self, filename: str) -> None:
        """
        Read simulation settings from xml file 
        
        Signature ``ReadSettingsFromFile(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX9.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetPostprocessorFilename(self) -> tuple:
        """
        Get the post processor definition and tcl filename with full path 
        
        Signature ``GetPostprocessorFilename()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (tclFilename, definitionFilename). tclFilename is a str.   The tcl filename with full pathdefinitionFilename is a str.   The definition filename with full path
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ShowSnapshot(self, bRunToSimTime: bool, snapshot: Snapshot) -> None:
        """
        Show snapshot 
        
        Signature ``ShowSnapshot(bRunToSimTime, snapshot)`` 
        
        :param bRunToSimTime: 
        :type bRunToSimTime: bool 
        :param snapshot:  The snapshot  
        :type snapshot: :py:class:`NXOpen.SIM.Snapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetCurrentProgram(self, channelName: str, stackLevel: int) -> NcProgram:
        """
        Returns a program currently used in the simulation  
        
        Signature ``GetCurrentProgram(channelName, stackLevel)`` 
        
        :param channelName:  The channel name.  
        :type channelName: str 
        :param stackLevel:  The callstack level. During simulation the main program is on callstack level 0.  
        :type stackLevel: int 
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.NcProgram` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    IsInHistoryBuffer: bool = ...
    """
    Returns  the simulation is inside history buffer  
    
    <hr>
    
    Getter Method
    
    Signature ``IsInHistoryBuffer`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    """
    MachineConfiguratorFilename: str = ...
    """
    Returns  the machine configurator filename with full path
    
    <hr>
    
    Getter Method
    
    Signature ``MachineConfiguratorFilename`` 
    
    :returns:  The machine configurator filename with full path 
    :rtype: str 
    
    .. versionadded:: NX10.0.1
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    SimDebugBuilder: SimDebugBuilder = ...
    """
    Returns  the sim debug builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SimDebugBuilder`` 
    
    :returns:  the sim debug builder  
    :rtype: :py:class:`NXOpen.SIM.SimDebugBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    SimulationLoadSnapshotBuilder: LoadSnapshotBuilder = ...
    """
    Returns  the load snapshot builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SimulationLoadSnapshotBuilder`` 
    
    :returns:  the load snapshot builder  
    :rtype: :py:class:`NXOpen.SIM.LoadSnapshotBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    SimulationOptionsBuilder: NXOpen.CAM.SimulationOptionsBuilder = ...
    """
    Returns  the simulation options builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SimulationOptionsBuilder`` 
    
    :returns:  the simulation options builder  
    :rtype: :py:class:`NXOpen.CAM.SimulationOptionsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    SimulationSaveSnapshotBuilder: SaveSnapshotBuilder = ...
    """
    Returns  the save snapshot builder 
    
    <hr>
    
    Getter Method
    
    Signature ``SimulationSaveSnapshotBuilder`` 
    
    :returns:  the save snapshot builder  
    :rtype: :py:class:`NXOpen.SIM.SaveSnapshotBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    VncStatus: IsvControlPanelBuilderVncMode = ...
    """
    Returns  the mode of VNC 
    
    <hr>
    
    Getter Method
    
    Signature ``VncStatus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVncMode` 
    
    .. versionadded:: NX10.0.3
    
    License requirements: None.
    """
    Null: IsvControlPanelBuilder = ...  # unknown typename


class Breakpoint(NXOpen.NXObject):
    """
    Represents the Breakpoint class object  
    
    Use the :py:class:`NXOpen.SIM.NcProgramManagerBuilder` class to create a Breakpoint object.
    
    .. versionadded:: NX11.0.0
    """
    
    def Activate(self) -> None:
        """
        Activate the breakpoint.  
        
        Signature ``Activate()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def Deactivate(self) -> None:
        """
        Deactivate the breakpoint.  
        
        Signature ``Deactivate()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Delete the breakpoint.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Condition: str = ...
    """
    Returns or sets  the condition for a breakpoint.  
    
    <hr>
    
    Getter Method
    
    Signature ``Condition`` 
    
    :returns:  The condition of the breakpoint.  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Condition`` 
    
    :param condition:  The condition of the breakpoint.  
    :type condition: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
    """
    Null: Breakpoint = ...  # unknown typename


class KinematicSinumerikCaBuilderPlcInitStateTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicSinumerikCaBuilderPlcInitStateTypes():
    """
    The init state types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Active", "Active"
       "Inactive", "Inactive"
       "Preselect", "Preselect"
    """
    Active = 0  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
    Inactive = 1  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
    Preselect = 2  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicSinumerikCaBuilderPlcUsageTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicSinumerikCaBuilderPlcUsageTypes():
    """
    The usage types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CollisionCheck", "Collision Check"
       "Visualize", "Visualize"
       "All", "All"
    """
    CollisionCheck = 0  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
    Visualize = 1  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
    All = 2  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicSinumerikCaBuilder(NXOpen.Builder):
    """
    This class is used for edit sinumerik collision avoidance properties.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`KinematicConfigurator` class to create a KinematicSinumerikCaBuilder object.
    
    .. versionadded:: NX9.0.0
    """
    
    class PlcInitStateTypes():
        """
        The init state types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Active", "Active"
           "Inactive", "Inactive"
           "Preselect", "Preselect"
        """
        Active = 0  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
        Inactive = 1  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
        Preselect = 2  # KinematicSinumerikCaBuilderPlcInitStateTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PlcUsageTypes():
        """
        The usage types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CollisionCheck", "Collision Check"
           "Visualize", "Visualize"
           "All", "All"
        """
        CollisionCheck = 0  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
        Visualize = 1  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
        All = 2  # KinematicSinumerikCaBuilderPlcUsageTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    DetailLevel: int = ...
    """
    Returns or sets  the detail level for this protection area 
    
    <hr>
    
    Getter Method
    
    Signature ``DetailLevel`` 
    
    :returns:  the detail level value 0-3  
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DetailLevel`` 
    
    :param level:  the detail value value 0-3  
    :type level: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    MagazineIndex: int = ...
    """
    Returns or sets  the magazine index for this automatic protection area 
    
    <hr>
    
    Getter Method
    
    Signature ``MagazineIndex`` 
    
    :returns:  the magazine index  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MagazineIndex`` 
    
    :param index:  the magazine index  
    :type index: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    MagazineLocationIndex: int = ...
    """
    Returns or sets  the magazine location index for this automatic protection area
    
    <hr>
    
    Getter Method
    
    Signature ``MagazineLocationIndex`` 
    
    :returns:  the magazine location index  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MagazineLocationIndex`` 
    
    :param index:  the magazine location index  
    :type index: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    PlcBit: int = ...
    """
    Returns or sets  the PLC bit for this protection area
    
    <hr>
    
    Getter Method
    
    Signature ``PlcBit`` 
    
    :returns:  the plc bit value 0-63  
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlcBit`` 
    
    :param bit:  the plc bit value 0-63  
    :type bit: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    PlcInitState: KinematicSinumerikCaBuilderPlcInitStateTypes = ...
    """
    Returns or sets  the initial PLC state for this protection area 
    
    <hr>
    
    Getter Method
    
    Signature ``PlcInitState`` 
    
    :returns:  the init state  
    :rtype: :py:class:`NXOpen.SIM.KinematicSinumerikCaBuilderPlcInitStateTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlcInitState`` 
    
    :param state:  the init state  
    :type state: :py:class:`NXOpen.SIM.KinematicSinumerikCaBuilderPlcInitStateTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    PlcUsage: KinematicSinumerikCaBuilderPlcUsageTypes = ...
    """
    Returns or sets  the PLC usage for this protection area 
    
    <hr>
    
    Getter Method
    
    Signature ``PlcUsage`` 
    
    :returns:  the usage  
    :rtype: :py:class:`NXOpen.SIM.KinematicSinumerikCaBuilderPlcUsageTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlcUsage`` 
    
    :param usage:  the usage  
    :type usage: :py:class:`NXOpen.SIM.KinematicSinumerikCaBuilderPlcUsageTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    TOIndex: int = ...
    """
    Returns or sets  the TO-index for this automatic protection area 
    
    <hr>
    
    Getter Method
    
    Signature ``TOIndex`` 
    
    :returns:  the TO number  
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TOIndex`` 
    
    :param index:  the TO number  
    :type index: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    Null: KinematicSinumerikCaBuilder = ...  # unknown typename


class MachineKitBuilder(NXOpen.Builder):
    """
    This class is used for the Machine Kit Create Dialog.  
    
    Calling :py:meth:`Builder.Commit` on this
    builder will start the machine kit creation process
    and return None.
    
    Use the :py:class:`Part` class to create a MachineKitBuilder object.
    
    .. versionadded:: NX10.0.2
    """
    Name: str = ...
    """
    Returns or sets  the machine kit name.  
    
    The name is used for the database entry and the name of the folder. 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  machine kit name  
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param kitName:  machine kit name  
    :type kitName: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    OutputDirectory: str = ...
    """
    Returns or sets  the machine kit output directory.  
    
    This is the location of the machine folder. 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputDirectory`` 
    
    :returns:  machine kit output directory  
    :rtype: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputDirectory`` 
    
    :param outputDirectory:  machine kit output directory  
    :type outputDirectory: str 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: MachineKitBuilder = ...  # unknown typename


class KinematicChannelBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    This class is used for add kinematic channel to the channel configuratation list.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateKinematicChannelBuilder`
    
    .. versionadded:: NX9.0.3
    """
    
    def GetAssignedAxes(self) -> 'list[str]':
        """
        Gets a list of assigned axes of the channel 
        
        Signature ``GetAssignedAxes()`` 
        
        :returns:  the list of assigned axes  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetAssignedAxes(self, assignedAxes: 'list[str]') -> None:
        """
        Sets a list of assigned axes of the channel 
        
        Signature ``SetAssignedAxes(assignedAxes)`` 
        
        :param assignedAxes:  the list of assigned axes  
        :type assignedAxes: list of str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetAssignedAxis(self, axisName: str) -> None:
        """
        Sets an assigned axis of the channel 
        
        Signature ``SetAssignedAxis(axisName)`` 
        
        :param axisName:  the assigned axis  
        :type axisName: str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetUnassignedAxis(self, axisName: str) -> None:
        """
        Sets an unassigned axis of the channel 
        
        Signature ``SetUnassignedAxis(axisName)`` 
        
        :param axisName:  the unassigned axis  
        :type axisName: str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetReferencedSpindles(self) -> 'list[str]':
        """
        Gets a list of referenced spindles of the channel 
        
        Signature ``GetReferencedSpindles()`` 
        
        :returns:  the list of referenced spindles  
        :rtype: list of str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetReferencedSpindles(self, refSpindles: 'list[str]') -> None:
        """
        Sets a list of referenced spindles of the channel 
        
        Signature ``SetReferencedSpindles(refSpindles)`` 
        
        :param refSpindles:  the list of referenced spindles  
        :type refSpindles: list of str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetReferencedSpindle(self, spindleName: str) -> None:
        """
        Sets a referenced spindle of the channel 
        
        Signature ``SetReferencedSpindle(spindleName)`` 
        
        :param spindleName:  the referenced spindle  
        :type spindleName: str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetUnreferencedSpindle(self, spindleName: str) -> None:
        """
        Sets an unreferenced spindle of the channel 
        
        Signature ``SetUnreferencedSpindle(spindleName)`` 
        
        :param spindleName:  the unreferenced spindle  
        :type spindleName: str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
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
    
    GeometryAxisX: str = ...
    """
    Returns or sets  the geometry X axis of the channel 
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryAxisX`` 
    
    :returns:  the x axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryAxisX`` 
    
    :param xAxis:  the x axis  
    :type xAxis: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    GeometryAxisY: str = ...
    """
    Returns or sets  the geometry Y axis of the channel 
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryAxisY`` 
    
    :returns:  the y axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryAxisY`` 
    
    :param yAxis:  the y axis  
    :type yAxis: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    GeometryAxisZ: str = ...
    """
    Returns or sets  the geometry Z axis of the channel 
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryAxisZ`` 
    
    :returns:  the z axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryAxisZ`` 
    
    :param zAxis:  the z axis  
    :type zAxis: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    MainSpindle: str = ...
    """
    Returns or sets  the main spindle of the channel 
    
    <hr>
    
    Getter Method
    
    Signature ``MainSpindle`` 
    
    :returns:  the main spindle  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MainSpindle`` 
    
    :param mainSpindle:  the main spindle  
    :type mainSpindle: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Name: str = ...
    """
    Returns or sets  the name of the channel 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The channel's name  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  the channel's new name  
    :type name: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: KinematicChannelBuilder = ...  # unknown typename


class KinematicImportMcfBuilder(NXOpen.Builder):
    """
    Represents a builder for an import axis and channel data  from mcf  
    
    Use the :py:class:`Part` class to create a KinematicImportMcfBuilder object.
    
    .. versionadded:: NX9.0.3
    """
    IgnoreLimits: bool = ...
    """
    Returns or sets  the flag which determines if the Limits of the MCF and the Kim are merge.  
    
    the soft limits are set based on the hard Limits of the Machine Tool Builder
    or if the limits in the mcf are useful they will be taken from MCF.
    
    <hr>
    
    Getter Method
    
    Signature ``IgnoreLimits`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IgnoreLimits`` 
    
    :param replace: 
    :type replace: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    McfPath: str = ...
    """
    Returns or sets  the path from the mcf file 
    
    <hr>
    
    Getter Method
    
    Signature ``McfPath`` 
    
    :returns:  The MCF Path  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``McfPath`` 
    
    :param path:  The MCF Path  
    :type path: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    ReplaceChannel: bool = ...
    """
    Returns or sets  the flag which determines if the channel data of the Machine Tool Builder are 
    deleted befor they are replaced through the Channel data of the MCF-File
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceChannel`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceChannel`` 
    
    :param replace: 
    :type replace: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: KinematicImportMcfBuilder = ...  # unknown typename


class KinematicConfiguratorUniteTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicConfiguratorUniteTypes():
    """
    The unite types for spinning geometries 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Create", "Create the spinning geometries as individual bodies"
       "Unite", "Unite the spinning geometries into one body"
    """
    Create = 0  # KinematicConfiguratorUniteTypesMemberType
    Unite = 1  # KinematicConfiguratorUniteTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicConfigurator(NXOpen.NXObject):
    """
    Represents the ISV base class object  
    
    To obtain an instance of this class, use :py:meth:`NXOpen.Part.KinematicConfigurator`
    
    .. versionadded:: NX7.5.0
    """
    
    class UniteTypes():
        """
        The unite types for spinning geometries 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Create", "Create the spinning geometries as individual bodies"
           "Unite", "Unite the spinning geometries into one body"
        """
        Create = 0  # KinematicConfiguratorUniteTypesMemberType
        Unite = 1  # KinematicConfiguratorUniteTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateJunctionBuilder(self, parent: KinematicComponent, jct: KinematicJunction) -> KinematicJunctionBuilder:
        """
        Creates a builder for a kinematic junction  
        
        Signature ``CreateJunctionBuilder(parent, jct)`` 
        
        :param parent:  The parent component  
        :type parent: :py:class:`NXOpen.SIM.KinematicComponent` 
        :param jct:  The junction to edit.                                                                                   If NULL, a new junction is created  
        :type jct: :py:class:`NXOpen.SIM.KinematicJunction` 
        :returns:  The new junction builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicJunctionBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def CreateAxisBuilder(self, parent: KinematicComponent, jct: KinematicJunction, axis: KinematicAxis) -> KinematicAxisBuilder:
        """
        Creates a builder for a kinematic axis  
        
        Signature ``CreateAxisBuilder(parent, jct, axis)`` 
        
        :param parent:  The parent component  
        :type parent: :py:class:`NXOpen.SIM.KinematicComponent` 
        :param jct:  The junction used for the axis  
        :type jct: :py:class:`NXOpen.SIM.KinematicJunction` 
        :param axis:  The axis to edit. If NULL, a new axis is craeted  
        :type axis: :py:class:`NXOpen.SIM.KinematicAxis` 
        :returns:  The new axis builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicAxisBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetName(self, name: str) -> None:
        """
        Sets the custom name of the kinematic model 
        
        Signature ``SetName(name)`` 
        
        :param name:  The new kinematic model name  
        :type name: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def GetName(self) -> str:
        """
        Returns the custom name of the kinematic model  
        
        Signature ``GetName()`` 
        
        :returns:  The kinematic model name  
        :rtype: str 
        
        .. versionadded:: NX11.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def AddUserClassification(self, userClass: str) -> None:
        """
        Adds a new user class name to the list of user classes 
        
        Signature ``AddUserClassification(userClass)`` 
        
        :param userClass:  The new user class name  
        :type userClass: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteUserClassification(self, userClass: str) -> None:
        """
        Deletes a user class name from the list of user classes 
        
        Signature ``DeleteUserClassification(userClass)`` 
        
        :param userClass:  The user class name to delete.  
        :type userClass: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameUserClassification(self, oldName: str, newName: str) -> None:
        """
        Renames a user class name from the list 
        
        Signature ``RenameUserClassification(oldName, newName)`` 
        
        :param oldName:  The old user class name  
        :type oldName: str 
        :param newName:  The new user class name  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetUserClassifications(self) -> 'list[str]':
        """
        Get a list of all user classes 
        
        Signature ``GetUserClassifications()`` 
        
        :returns:  The list of user classes    
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddHoldingSystem(self, holdSys: str) -> None:
        """
        Adds a new user holding system to the list of holding systems 
        
        Signature ``AddHoldingSystem(holdSys)`` 
        
        :param holdSys:  The new holding system.  
        :type holdSys: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteHoldingSystem(self, holdSys: str) -> None:
        """
        Delete a holding system from the list 
        
        Signature ``DeleteHoldingSystem(holdSys)`` 
        
        :param holdSys:  The holding system to delete.  
        :type holdSys: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteAllHoldingSystems(self) -> None:
        """
        Delete all holding systems from the kinematic model 
        
        Signature ``DeleteAllHoldingSystems()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameHoldingSystem(self, oldName: str, newName: str) -> None:
        """
        Renames a holding system from the list 
        
        Signature ``RenameHoldingSystem(oldName, newName)`` 
        
        :param oldName:  The old holding system  
        :type oldName: str 
        :param newName:  The new holding system  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetHoldingSystems(self) -> 'list[str]':
        """
        Get a list of all holding systems 
        
        Signature ``GetHoldingSystems()`` 
        
        :returns:  The holding systems            
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddChannel(self, channel: str) -> None:
        """
        Adds a new user channel name to the list of channels 
        
        Signature ``AddChannel(channel)`` 
        
        :param channel:  The new channel name.  
        :type channel: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteChannel(self, channel: str) -> None:
        """
        Deletes a channel name from the list of channels 
        
        Signature ``DeleteChannel(channel)`` 
        
        :param channel:  The channel name to delete.  
        :type channel: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteAllChannels(self) -> None:
        """
        Deletes all channels from the kinematic model 
        
        Signature ``DeleteAllChannels()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameChannel(self, oldName: str, newName: str) -> None:
        """
        Renames a channel name from the list 
        
        Signature ``RenameChannel(oldName, newName)`` 
        
        :param oldName:  The old channel name  
        :type oldName: str 
        :param newName:  The new channel name  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetChannels(self) -> 'list[str]':
        """
        Get a list of all channels 
        
        Signature ``GetChannels()`` 
        
        :returns:  The list of channels    
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSpinningClone(self, source: KinematicComponent, combine: bool) -> KinematicComponent:
        """
        Creates a copy of the given component and spins its assigned geometry around a spinning axis.  
        
        For tool components, the X-axis of the tool tip junction is used as spinning axis. If none
        is defined and for other types of components, the X-axis of the WCS is used.
        The new component has the same parent as the source component.  
        
        Signature ``CreateSpinningClone(source, combine)`` 
        
        :param source:  The source component.  
        :type source: :py:class:`NXOpen.SIM.KinematicComponent` 
        :param combine:  Specifies whether to combine the spinning geometries into one, or not  
        :type combine: bool 
        :returns:  The new spinning component  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    @typing.overload
    def FindComponentsBySystemClass(self, sysclass: int) -> 'list[KinematicComponent]':
        """
        Finds component which are of the given system class in bitwise 
        
        Signature ``FindComponentsBySystemClass(sysclass)`` 
        
        :param sysclass:  The system class to look for in bitwise.  
        :type sysclass: int 
        :returns:  The found components  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX8.0.3
           Use :py:meth:`FindComponentsBySystemClass` with :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` instead.
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    @typing.overload
    def FindComponentsBySystemClass(self, sysclass: KinematicComponentBuilderSystemClass) -> 'list[KinematicComponent]':
        """
        Finds component which are of the given system class 
        
        Signature ``FindComponentsBySystemClass(sysclass)`` 
        
        :param sysclass:  The system class to look for.  
        :type sysclass: :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` 
        :returns:  The found components  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX8.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    @typing.overload
    def FindJunction(self, name: str) -> KinematicJunction:
        """
        Find the junction with the given name  
        
        Signature ``FindJunction(name)`` 
        
        :param name:  The name to look for  
        :type name: str 
        :returns:  The junction, if found  
        :rtype: :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    @typing.overload
    def FindJunction(self, csys: NXOpen.NXObject) -> KinematicJunction:
        """
        Finds a junction by its coordinate system  
        
        Signature ``FindJunction(csys)`` 
        
        :param csys:  the csys of a junction  
        :type csys: :py:class:`NXOpen.NXObject` 
        :returns:  The junction for the csys  
        :rtype: :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def FindAxis(self, name: str) -> tuple:
        """
        Find the axis with the given name  
        
        Signature ``FindAxis(name)`` 
        
        :param name:  The name to look for  
        :type name: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (axis, pComp, pJct). axis is a :py:class:`NXOpen.SIM.KinematicAxis`.   The axis, if found pComp is a :py:class:`NXOpen.SIM.KinematicComponent`.   The parent component of the axis pJct is a :py:class:`NXOpen.SIM.KinematicJunction`.   The parent junction of the axis 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def FindParentComponent(self, comp: KinematicComponent) -> KinematicComponent:
        """
        Finds the :py:class:`NXOpen.SIM.KinematicComponent` which is the parent of this component  
        
        Signature ``FindParentComponent(comp)`` 
        
        :param comp:  The component  
        :type comp: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The parent Component.  
        
        NULL if comp is root component  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def FindOwnerOfJunction(self, jct: KinematicJunction) -> KinematicComponent:
        """
        Finds the :py:class:`NXOpen.SIM.KinematicComponent` which is the owner of this junction  
        
        Signature ``FindOwnerOfJunction(jct)`` 
        
        :param jct:  The junction  
        :type jct: :py:class:`NXOpen.SIM.KinematicJunction` 
        :returns:  The owning component of the junction  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteModel(self) -> None:
        """
        Deletes the entire kinematic model 
        
        Signature ``DeleteModel()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteComponent(self, comp: KinematicComponent) -> None:
        """
        Deletes the given component 
        
        Signature ``DeleteComponent(comp)`` 
        
        :param comp:  the component to delete  
        :type comp: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteJunction(self, jct: KinematicJunction) -> None:
        """
        Deletes the given junction 
        
        Signature ``DeleteJunction(jct)`` 
        
        :param jct:  the component to delete  
        :type jct: :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteAxis(self, axis: KinematicAxis) -> None:
        """
        Deletes the given axis 
        
        Signature ``DeleteAxis(axis)`` 
        
        :param axis:  the component to delete  
        :type axis: :py:class:`NXOpen.SIM.KinematicAxis` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def InsertRootComponent(self, newRoot: KinematicComponent) -> None:
        """
        Adds a new root component to the :py:class:`NXOpen.SIM.KinematicConfigurator` object 
        
        Signature ``InsertRootComponent(newRoot)`` 
        
        :param newRoot:  The new root component  
        :type newRoot: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteRootComponent(self, oldRoot: KinematicComponent) -> None:
        """
        Delete a root component from the :py:class:`NXOpen.SIM.KinematicConfigurator` object 
        
        Signature ``DeleteRootComponent(oldRoot)`` 
        
        :param oldRoot:  The root component to remove  
        :type oldRoot: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetJunctions(self) -> 'list[KinematicJunction]':
        """
        Gets a list of all junctions in the kinematic 
        
        Signature ``GetJunctions()`` 
        
        :returns:  The list of junctions  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicJunction` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def GetJunctionNames(self) -> 'list[str]':
        """
        Gets a list of all junction names in the kinematic 
        
        Signature ``GetJunctionNames()`` 
        
        :returns:  The list of junction names  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetAxes(self) -> 'list[KinematicAxis]':
        """
        Gets a list of all axes in the kinematic 
        
        Signature ``GetAxes()`` 
        
        :returns:  The list of axes  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicAxis` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def GetAxisNames(self) -> 'list[str]':
        """
        Gets a list of all axis names in the kinematic 
        
        Signature ``GetAxisNames()`` 
        
        :returns:  The list of axis names  
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSimDebugBuilder(self) -> SimDebugBuilder:
        """
        Creates a sim debug builder  
        
        Signature ``CreateSimDebugBuilder()`` 
        
        :returns:  The new sim debug builder  
        :rtype: :py:class:`NXOpen.SIM.SimDebugBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateNcChannelSelectionData(self) -> NcChannelSelectionData:
        """
        Creates an NcChannelSelectionData object to which files and channels can be assigned.  
        
        This is used when constructing the builder.  
        
        Signature ``CreateNcChannelSelectionData()`` 
        
        :returns:  The NC channel selection data 
        :rtype: :py:class:`NXOpen.SIM.NcChannelSelectionData` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    @typing.overload
    def CreateIsvControlPanelBuilder(self, driverType: IsvControlPanelBuilderVisualizationType, objects: 'list[NXOpen.CAM.CAMObject]') -> IsvControlPanelBuilder:
        """
        Creates an isv control panel builder  
        
        Signature ``CreateIsvControlPanelBuilder(driverType, objects)`` 
        
        :param driverType:  The visualization type 
        :type driverType: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVisualizationType` 
        :param objects:  array of objects  
        :type objects: list of :py:class:`NXOpen.CAM.CAMObject` 
        :returns:  The isv control panel builder  
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    @typing.overload
    def CreateIsvControlPanelBuilder(self, driverType: IsvControlPanelBuilderVisualizationType, filename: str) -> IsvControlPanelBuilder:
        """
        Creates an isv control panel builder with given machine code file name.  
        
        Signature ``CreateIsvControlPanelBuilder(driverType, filename)`` 
        
        :param driverType:  The visualization type 
        :type driverType: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVisualizationType` 
        :param filename:  The full path machine code filename  
        :type filename: str 
        :returns:  The isv control panel builder  
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilder` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateIsvControlPanelBuilder` with :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateNcChannelSelectionData` instead.
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    @typing.overload
    def CreateIsvControlPanelBuilder(self, driverType: IsvControlPanelBuilderVisualizationType, channelData: NcChannelSelectionData) -> IsvControlPanelBuilder:
        """
        Creates an isv control panel builder with given machine code file name. 
        
        Signature ``CreateIsvControlPanelBuilder(driverType, channelData)`` 
        
        :param driverType:  The visualization type 
        :type driverType: :py:class:`NXOpen.SIM.IsvControlPanelBuilderVisualizationType` 
        :param channelData:  The NC channel selection data 
        :type channelData: :py:class:`NXOpen.SIM.NcChannelSelectionData` 
        :returns:  The isv control panel builder  
        :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSimulationOptionsBuilder(self, dialogType: NXOpen.CAM.SimulationOptionsBuilderDialogType) -> NXOpen.CAM.SimulationOptionsBuilder:
        """
        Creates a simulation options  
        
        Signature ``CreateSimulationOptionsBuilder(dialogType)`` 
        
        :param dialogType:  The dialog type  
        :type dialogType: :py:class:`NXOpen.CAM.SimulationOptionsBuilderDialogType` 
        :returns:  The new simulation options  
        :rtype: :py:class:`NXOpen.CAM.SimulationOptionsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateCollisionPairBuilder(self) -> NXOpen.CAM.CollisionPairBuilder:
        """
        Creates a collision pair builder  
        
        Signature ``CreateCollisionPairBuilder()`` 
        
        :returns:  The new collision pair builder  
        :rtype: :py:class:`NXOpen.CAM.CollisionPairBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateKinematicSinumerikCaBuilder(self, comp: KinematicComponent) -> KinematicSinumerikCaBuilder:
        """
        Creates a builder for a kinematic sinumerik ca config  
        
        Signature ``CreateKinematicSinumerikCaBuilder(comp)`` 
        
        :param comp:  the component to edit  
        :type comp: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The new kinematic sinumerik ca builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicSinumerikCaBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSinumerikCaSimplifyBodiesBuilder(self) -> SinumerikCaSimplifyBodiesBuilder:
        """
        Creates a builder for a sinumerik ca simplify bodies  
        
        Signature ``CreateSinumerikCaSimplifyBodiesBuilder()`` 
        
        :returns:  The new sinumerik ca simplify bodies builder  
        :rtype: :py:class:`NXOpen.SIM.SinumerikCaSimplifyBodiesBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSinumerikCaExportBuilder(self) -> SinumerikCaExportBuilder:
        """
        Creates a builder for a sinumerik ca export spf  
        
        Signature ``CreateSinumerikCaExportBuilder()`` 
        
        :returns:  The new sinumerik ca export builder  
        :rtype: :py:class:`NXOpen.SIM.SinumerikCaExportBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSinumerikCaFacetBuilder(self) -> SinumerikCaFacetBuilder:
        """
        Creates a builder for a sinumerik ca facet  
        
        Signature ``CreateSinumerikCaFacetBuilder()`` 
        
        :returns:  The new sinumerik ca facet builder  
        :rtype: :py:class:`NXOpen.SIM.SinumerikCaFacetBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSinumerikCaPlaceholderBuilder(self) -> SinumerikCaPlaceholderBuilder:
        """
        Creates a builder for a sinumerik ca placeholder  
        
        Signature ``CreateSinumerikCaPlaceholderBuilder()`` 
        
        :returns:  The new sinumerik ca placeholder builder  
        :rtype: :py:class:`NXOpen.SIM.SinumerikCaPlaceholderBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateConvertFromMcdBuilder(self) -> NXOpen.CAM.ConvertFromMCDBuilder:
        """
        Creates a builder to convert from MCD  
        
        Signature ``CreateConvertFromMcdBuilder()`` 
        
        :returns:  The new convert from mcd builder  
        :rtype: :py:class:`NXOpen.CAM.ConvertFromMCDBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DefineKinematicChains(self) -> KinematicChainConfiguration:
        """
        Creates a builder for a kinematic chain configurator  
        
        Signature ``DefineKinematicChains()`` 
        
        :returns:  The new kinematic chain configuration builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicChainConfiguration` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateKinematicChain(self) -> KinematicChain:
        """
        Creates a builder for a kinematic chain  
        
        Signature ``CreateKinematicChain()`` 
        
        :returns:  The new kinematic chain builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicChain` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateChannelConfigurationBuilder(self) -> KinematicChannelConfigurationBuilder:
        """
        Creates a builder for a kinematic channel configurator  
        
        Signature ``CreateChannelConfigurationBuilder()`` 
        
        :returns:  The new kinematic channel configuration builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicChannelConfigurationBuilder` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateKinematicChannelBuilder(self) -> KinematicChannelBuilder:
        """
        Creates a builder for a channel  
        
        Signature ``CreateKinematicChannelBuilder()`` 
        
        :returns:  The new kinematic channel builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicChannelBuilder` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateImportMcfBuilder(self) -> KinematicImportMcfBuilder:
        """
        Creates a builder for a import axis and channel data from mcf  
        
        Signature ``CreateImportMcfBuilder()`` 
        
        :returns:  The import axis and channel data builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicImportMcfBuilder` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateArchiveImportBuilder(self) -> ArchiveImportBuilder:
        """
        Creates a builder to import a Sinumerik archive file  
        
        Signature ``CreateArchiveImportBuilder()`` 
        
        :returns:  The new CamtImport builder  
        :rtype: :py:class:`NXOpen.SIM.ArchiveImportBuilder` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateMachineToolConfigurationBuilder(self) -> MachineToolConfiguration:
        """
        Creates a builder for the Machine Tool Configuration  
        
        Signature ``CreateMachineToolConfigurationBuilder()`` 
        
        :returns:  The new machine tool configuration builder  
        :rtype: :py:class:`NXOpen.SIM.MachineToolConfiguration` 
        
        .. versionadded:: NX9.0.3
        
        License requirements: nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def ImportNcArchive(self, ncFileName: str, printReport: bool) -> None:
        """
        Import the nc archive for the Machine Tool Configuration 
        
        Signature ``ImportNcArchive(ncFileName, printReport)`` 
        
        :param ncFileName:  The path to the nc archive file  
        :type ncFileName: str 
        :param printReport:  Print the report  
        :type printReport: bool 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CopyKinematicModel(self) -> KinematicModel:
        """
        Copy a kinematic model.  
        
        User need to call :py:meth:`NXOpen.SIM.KinematicConfigurator.DeleteKinematicModel` to delete the copy of kinematic model.
        
        Signature ``CopyKinematicModel()`` 
        
        :returns:  The copy of kinematic model  
        :rtype: :py:class:`NXOpen.SIM.KinematicModel` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteKinematicModel(self, kimModel: KinematicModel) -> None:
        """
        Delete the copy of kinematic model.  
        
        Signature ``DeleteKinematicModel(kimModel)`` 
        
        :param kimModel:  The copy of kinematic model  
        :type kimModel: :py:class:`NXOpen.SIM.KinematicModel` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateMachineLibraryBuilder(self) -> MachineLibraryBuilder:
        """
        Creates a builder for the machine tool Library dialog  
        
        Signature ``CreateMachineLibraryBuilder()`` 
        
        :returns:  The machine Library builder  
        :rtype: :py:class:`NXOpen.SIM.MachineLibraryBuilder` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateMachineKitBuilder(self) -> MachineKitBuilder:
        """
        Creates a builder for the machine tool kit  
        
        Signature ``CreateMachineKitBuilder()`` 
        
        :returns:  The machine kit builder  
        :rtype: :py:class:`NXOpen.SIM.MachineKitBuilder` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateNcProgramManagerBuilder(self) -> NcProgramManagerBuilder:
        """
        Creates a builder for the nc program manager  
        
        Signature ``CreateNcProgramManagerBuilder()`` 
        
        :returns:  The nc program manager builder  
        :rtype: :py:class:`NXOpen.SIM.NcProgramManagerBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def ExportMachineKitBuilder(self, machineName: str) -> ExportMachineKitBuilder:
        """
        Creates a builder for export the machine tool kit  
        
        Signature ``ExportMachineKitBuilder(machineName)`` 
        
        :param machineName:  The library reference (libref) of the machine to export 
        :type machineName: str 
        :returns:  The machine kit builder  
        :rtype: :py:class:`NXOpen.SIM.ExportMachineKitBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def ImportMachineKitBuilder(self, kitPath: str) -> ImportMachineKitBuilder:
        """
        Creates a builder for import the machine tool kit  
        
        Signature ``ImportMachineKitBuilder(kitPath)`` 
        
        :param kitPath:  path of the machine tool kit file 
        :type kitPath: str 
        :returns:  The import machine kit builder  
        :rtype: :py:class:`NXOpen.SIM.ImportMachineKitBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSimulationSavesnapshotBuilder(self) -> SaveSnapshotBuilder:
        """
        Creates a builder for the save snapshot  
        
        Signature ``CreateSimulationSavesnapshotBuilder()`` 
        
        :returns:  The save snapshot builder  
        :rtype: :py:class:`NXOpen.SIM.SaveSnapshotBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateSimulationLoadsnapshotBuilder(self) -> LoadSnapshotBuilder:
        """
        Creates a builder for the load snapshot  
        
        Signature ``CreateSimulationLoadsnapshotBuilder()`` 
        
        :returns:  The load snapshot builder  
        :rtype: :py:class:`NXOpen.SIM.LoadSnapshotBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    IsvControlPanelBuilder: IsvControlPanelBuilder = ...
    """
    Returns  the isv control panel builder 
    
    <hr>
    
    Getter Method
    
    Signature ``IsvControlPanelBuilder`` 
    
    :returns:  the isv control panel builder  
    :rtype: :py:class:`NXOpen.SIM.IsvControlPanelBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    ComponentCollection: KinematicComponentCollection = ...
    """
    Returns the ComponentCollection instance belonging to this SimKim 
    
    Signature ``ComponentCollection`` 
    
    .. versionadded:: NX7.5.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.KinematicComponentCollection`
    """
    Null: KinematicConfigurator = ...  # unknown typename


class NcProgramManagerBuilder(NXOpen.Builder):
    """
    Represents a NcProgramManagerBuilder builder object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateNcProgramManagerBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def AddMatchingBreakpoint(self, condition: str) -> None:
        """
        Add a matching breakpoint to program manager.  
        
        Signature ``AddMatchingBreakpoint(condition)`` 
        
        :param condition:  The condition for the line and program independent breakpoint to be added.  
        :type condition: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def AddBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
        Add a breakpoint to a program line.  
        
        Signature ``AddBreakpoint(program, lineNumber)`` 
        
        :param program:  The program in which the breakpoint is to be added.  
        :type program: :py:class:`NXOpen.SIM.NcProgram` 
        :param lineNumber:  The line number of the breakpoint (zero based).  
        :type lineNumber: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ActivateBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
        Activate a breakpoint in a program line.  
        
        Signature ``ActivateBreakpoint(program, lineNumber)`` 
        
        :param program:  The program in which the breakpoint is to be activated.  
        :type program: :py:class:`NXOpen.SIM.NcProgram` 
        :param lineNumber:  The line number of the breakpoint (zero based).  
        :type lineNumber: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def DeactivateBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
        Deactivate a breakpoint in a program line.  
        
        Signature ``DeactivateBreakpoint(program, lineNumber)`` 
        
        :param program:  The program in which the breakpoint is to be deactivated.  
        :type program: :py:class:`NXOpen.SIM.NcProgram` 
        :param lineNumber:  The line number of the breakpoint (zero based).  
        :type lineNumber: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def DeleteBreakpoint(self, program: NcProgram, lineNumber: int) -> None:
        """
        Remove a breakpoint from a program line.  
        
        Signature ``DeleteBreakpoint(program, lineNumber)`` 
        
        :param program:  The program in which the breakpoint is to be deleted  
        :type program: :py:class:`NXOpen.SIM.NcProgram` 
        :param lineNumber:  The line number of the breakpoint (zero based).  
        :type lineNumber: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def GetBreakpoints(self) -> 'list[Breakpoint]':
        """
        Get all breakpoints.  
        
        Signature ``GetBreakpoints()`` 
        
        :returns:  array of all breakpoints  
        :rtype: list of :py:class:`NXOpen.SIM.Breakpoint` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeactivateAllBreakpoints(self) -> None:
        """
        Deactivate all active breakpoints.  
        
        Signature ``DeactivateAllBreakpoints()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def ActivateAllBreakpoints(self) -> None:
        """
        Activate all deactivated breakpoints.  
        
        Signature ``ActivateAllBreakpoints()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def DeleteAllBreakpoints(self) -> None:
        """
        Delete all breakpoints.  
        
        Signature ``DeleteAllBreakpoints()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Null: NcProgramManagerBuilder = ...  # unknown typename


class NcProgram(NXOpen.NXObject):
    """
    Represents the NcProgram class object  
    
    Use the :py:class:`NXOpen.SIM.NcProgramManagerBuilder` class to create a NcProgram object.
    
    .. versionadded:: NX11.0.0
    """
    
    def AddBreakpoint(self, line: int) -> None:
        """
        Add a breakpoint.  
        
        Signature ``AddBreakpoint(line)`` 
        
        :param line:  The line number of the breakpoint (zero based).  
        :type line: int 
        
        .. versionadded:: NX11.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`SIM.NcProgram.InsertBreakpoint` instead which returns the added Breakpoint.
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def InsertBreakpoint(self, line: int) -> Breakpoint:
        """
        Add a breakpoint.  
        
        Signature ``InsertBreakpoint(line)`` 
        
        :param line:  The line number of the breakpoint (zero based).  
        :type line: int 
        :returns: 
        :rtype: :py:class:`NXOpen.SIM.Breakpoint` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Null: NcProgram = ...  # unknown typename


class KinematicJunction(NXOpen.NXObject):
    """
    Represents the KinematicJunction class object  
    
    Use the :py:class:`NXOpen.SIM.KinematicConfigurator` class to create a SimKimJunction object.
    
    .. versionadded:: NX7.5.0
    """
    Null: KinematicJunction = ...  # unknown typename


class SinumerikCaFacetBuilder(NXOpen.Builder):
    """
    This class is used for set the facet tolerance.  
    
    A call to :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`Part` class to create a SinumerikCaFacetBuilder object.
    
    .. versionadded:: NX9.0.0
    """
    FacetTolerance: float = ...
    """
    Returns or sets  the facet tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``FacetTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FacetTolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    Null: SinumerikCaFacetBuilder = ...  # unknown typename


class KinematicChainList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[KinematicChain]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicChain` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: KinematicChain) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.SIM.KinematicChain` 
        
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
    
    
    def FindIndex(self, obj: KinematicChain) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.SIM.KinematicChain` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> KinematicChain:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.SIM.KinematicChain` 
        
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
    def Erase(self, obj: KinematicChain) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicChain` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: KinematicChain, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.SIM.KinematicChain` 
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
    
    
    def GetContents(self) -> 'list[KinematicChain]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicChain` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[KinematicChain]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.SIM.KinematicChain` 
        
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
    def Swap(self, object1: KinematicChain, object2: KinematicChain) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.SIM.KinematicChain` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.SIM.KinematicChain` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: KinematicChain) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.SIM.KinematicChain` 
        
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
    Null: KinematicChainList = ...  # unknown typename


class SaveSnapshotBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.SIM.SaveSnapshotBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateSimulationSavesnapshotBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def SetSnapshotName(self, name: str) -> None:
        """
        Sets the snapshot name 
        
        Signature ``SetSnapshotName(name)`` 
        
        :param name:  The snapshot name  
        :type name: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SetSetupName(self, name: str) -> None:
        """
        Sets the setup name 
        
        Signature ``SetSetupName(name)`` 
        
        :param name:  The setup name  
        :type name: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Null: SaveSnapshotBuilder = ...  # unknown typename


class TimeAnalysis(NXOpen.TaggedObject):
    """
    Represents the TimeAnalysis class object  
    
    These objects are created by the simulation for each channel.
    
    .. versionadded:: NX11.0.2
    """
    
    def Start(self) -> None:
        """
        Start the Time Analysis
        
        Signature ``Start()`` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def Stop(self) -> None:
        """
        Stop the Time Analysis
        
        Signature ``Stop()`` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def Reset(self) -> None:
        """
        Reset the Time Analysis
        
        Signature ``Reset()`` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Null: TimeAnalysis = ...  # unknown typename


class SinumerikCaPlaceholderBuilder(NXOpen.Builder):
    """
    This class is used for select or unselect component of the placeholder tools.  
    
    A call to :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`Part` class to create a SinumerikCaPlaceholderBuilder object.
    
    .. versionadded:: NX9.0.0
    """
    
    def SelectComponent(self, compName: str) -> None:
        """
        The select placeholder tools component 
        
        Signature ``SelectComponent(compName)`` 
        
        :param compName:  The selected placeholder component name  
        :type compName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
        """
        ...
    
    
    def UnselectComponent(self, compName: str) -> None:
        """
        The select placeholder tools component 
        
        Signature ``UnselectComponent(compName)`` 
        
        :param compName:  The unselected placeholder component name  
        :type compName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_sinumerik_ca ("Sinumerik Collision Avoidance")
        """
        ...
    
    Null: SinumerikCaPlaceholderBuilder = ...  # unknown typename


class KinematicChainConfiguration(NXOpen.Builder):
    """
    This class is used for define kinematic chains.  
    
    Calling :py:meth:`Builder.Commit` on this builder will return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.DefineKinematicChains`
    
    .. versionadded:: NX9.0.0
    """
    List: KinematicChainList = ...
    """
    Returns  the kinematic chain list 
    
    <hr>
    
    Getter Method
    
    Signature ``List`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.KinematicChainList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: KinematicChainConfiguration = ...  # unknown typename


class MachineLibraryBuilder(NXOpen.Builder):
    """
    This class is used for the Machine Library Dialog.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`Part` class to create a MachineLibraryBuilder object.
    
    .. versionadded:: NX10.0.2
    """
    
    def EditMachineLibrary(self, machineName: str, attName: str, value: str) -> None:
        """
        Edit a specific machine of the database.  
        
        That will write the machine_database.dat. 
        
        Signature ``EditMachineLibrary(machineName, attName, value)`` 
        
        :param machineName:  machine name (libref) 
        :type machineName: str 
        :param attName:  library attribute name 
        :type attName: str 
        :param value:  the new value that will be set 
        :type value: str 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def InsertEntryToMachineLibrary(self, selectedMachineName: str) -> str:
        """
        Insert a machine entry to the machine_database.  
        
        dat. The libref is the name of the machine entry,
        that is copied, the libref appended by a count and the new entry is put in the list as next entry.
        If the libref is empty, a default entry is add to the bottom of the list.  
        
        Signature ``InsertEntryToMachineLibrary(selectedMachineName)`` 
        
        :param selectedMachineName:  machine name (libref), that will copied 
        :type selectedMachineName: str 
        :returns:  machine name (libref), of the new machien entry 
        :rtype: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RemoveEntryFromMachineLibrary(self, machineName: str) -> None:
        """
        Removes a machine entry from the machine_database.  
        
        dat. The libref is the name of the machine entry,
        that will reomved from the Library. 
        
        Signature ``RemoveEntryFromMachineLibrary(machineName)`` 
        
        :param machineName:  machine name (libref) 
        :type machineName: str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetAllMachineNames(self) -> 'list[str]':
        """
        Returns a array of the machine names(librefs) that are in the machine database.  
        
        This function allocates the memory for machineNames. The caller is responsible to deallocate the memory. 
        
        Signature ``GetAllMachineNames()`` 
        
        :returns:  array of all machine names (libref) 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetAllAttributeNames(self) -> 'list[str]':
        """
        Returns a array of the library attributes.  
        
        This function allocates the memory for attributeNames. The caller is responsible to deallocate the memory. 
        
        Signature ``GetAllAttributeNames()`` 
        
        :returns:  array of all attribute names 
        :rtype: list of str 
        
        .. versionadded:: NX10.0.3
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetValue(self, machineName: str, attName: str) -> str:
        """
        Returns the attribute value of a specific machine.  
        
        Signature ``GetValue(machineName, attName)`` 
        
        :param machineName:  machine name (libref) 
        :type machineName: str 
        :param attName:  library attribute name 
        :type attName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    Null: MachineLibraryBuilder = ...  # unknown typename


class KinematicAxis(NXOpen.NXObject):
    """
    Represents the SimKimAxis class object  
    
    Use the :py:class:`NXOpen.SIM.KinematicAxisBuilder` class to create a KinematicAxis object.
    
    .. versionadded:: NX7.5.0
    """
    Null: KinematicAxis = ...  # unknown typename


class KinematicModel(NXOpen.NXObject):
    """
    Represents the Kinematic Model class object. 
    
    Example how to move machine axes:
    
    Dim kinematicModel As NXOpen.SIM.KinematicModel
    kinematicModel = kinematicConfigurator.CopyKinematicModel()
    
    Dim kinematicAxis_X1 As NXOpen.SIM.KinematicAxis
    kinematicAxis_X1 = kinematicModel.FindMachineAxis("X1")
    
    Dim kinematicAxis_Y1 As NXOpen.SIM.KinematicAxis
    kinematicAxis_Y1 = kinematicModel.FindMachineAxis("Y1")
    
    Dim kinematicAxis_Z1 As NXOpen.SIM.KinematicAxis
    kinematicAxis_Z1 = kinematicModel.FindMachineAxis("Z1")
    
    kinematicModel.SetMachineAxisValue(kinematicAxis_X1, 100)
    kinematicModel.SetMachineAxisValue(kinematicAxis_Y1, 150)
    kinematicModel.SetMachineAxisValue(kinematicAxis_Z1, 200)
    
    'Move the axes X1, Y1, Z1 to the position 100, 150, 200 on the graphic window simultaneously
    kinematicModel.UpdateMachineDisplay()
    ...
    
    kinematicConfigurator.DeleteKinematicModel(kinematicModel)
    
    Use the :py:class:`NXOpen.SIM.KinematicConfigurator` class to create a KinematicModel object.
    
    .. versionadded:: NX10.0.1
    """
    
    def FindMachineAxis(self, name: str) -> KinematicAxis:
        """
        Find the machine axis with the given name.  
        
        Signature ``FindMachineAxis(name)`` 
        
        :param name:  The name to look for  
        :type name: str 
        :returns:  The axis, if found  
        :rtype: :py:class:`NXOpen.SIM.KinematicAxis` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def SetMachineAxisValue(self, axis: KinematicAxis, value: float) -> None:
        """
        Sets the machine axis to the given value.  
        
        User need to call :py:meth:`NXOpen.SIM.KinematicModel.UpdateMachineDisplay` to see the axis moving in the graphic window.
        
        Signature ``SetMachineAxisValue(axis, value)`` 
        
        :param axis:  the machine axis to be moved  
        :type axis: :py:class:`NXOpen.SIM.KinematicAxis` 
        :param value:  the value  
        :type value: float 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def UpdateMachineDisplay(self) -> None:
        """
        Update machine display.  
        
        This call is needed after call :py:meth:`NXOpen.SIM.KinematicModel.SetMachineAxisValue` to see the axis moving in the graphic window.
        
        Signature ``UpdateMachineDisplay()`` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    Null: KinematicModel = ...  # unknown typename


class KinematicChainTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicChainTypes():
    """
    Represents the kinematic chain type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "Unknown"
       "Milling", "Milling"
       "Turning", "Turning"
       "Polar", "Polar"
       "Robot", "Robot"
    """
    Unknown = -1  # KinematicChainTypesMemberType
    Milling = 0  # KinematicChainTypesMemberType
    Turning = 1  # KinematicChainTypesMemberType
    Polar = 2  # KinematicChainTypesMemberType
    Robot = 3  # KinematicChainTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicChainCoordinatePlaneTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicChainCoordinatePlaneTypes():
    """
    Represents the coordinate plane type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Zx", "ZX"
       "Xy", "XY"
    """
    Zx = 0  # KinematicChainCoordinatePlaneTypesMemberType
    Xy = 1  # KinematicChainCoordinatePlaneTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicChain(NXOpen.Builder):
    """
    This class is used for add kinematic chain to the list.  
    
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateKinematicChain`
    
    .. versionadded:: NX9.0.0
    """
    
    class Types():
        """
        Represents the kinematic chain type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "Unknown"
           "Milling", "Milling"
           "Turning", "Turning"
           "Polar", "Polar"
           "Robot", "Robot"
        """
        Unknown = -1  # KinematicChainTypesMemberType
        Milling = 0  # KinematicChainTypesMemberType
        Turning = 1  # KinematicChainTypesMemberType
        Polar = 2  # KinematicChainTypesMemberType
        Robot = 3  # KinematicChainTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CoordinatePlaneTypes():
        """
        Represents the coordinate plane type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Zx", "ZX"
           "Xy", "XY"
        """
        Zx = 0  # KinematicChainCoordinatePlaneTypesMemberType
        Xy = 1  # KinematicChainCoordinatePlaneTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    Axial: str = ...
    """
    Returns or sets  the axial axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Axial`` 
    
    :returns:  the axial axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Axial`` 
    
    :param axis:  the axial axis  
    :type axis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    CoordinateAxes: str = ...
    """
    Returns or sets  the coordinate axes name of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinateAxes`` 
    
    :returns:  the coordinate axes  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CoordinateAxes`` 
    
    :param axis:  the coordinate axes  
    :type axis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    CoordinatePlane: KinematicChainCoordinatePlaneTypes = ...
    """
    Returns or sets  the coordinate plane type of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordinatePlane`` 
    
    :returns:  the coordinate plane type  
    :rtype: :py:class:`NXOpen.SIM.KinematicChainCoordinatePlaneTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CoordinatePlane`` 
    
    :param type:  the coordinate plane type  
    :type type: :py:class:`NXOpen.SIM.KinematicChainCoordinatePlaneTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Device: str = ...
    """
    Returns or sets  the device component of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Device`` 
    
    :returns:  the chain device  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Device`` 
    
    :param device:  the chain device  
    :type device: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Name: str = ...
    """
    Returns or sets  the name of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The chain's name  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  the chain's new name  
    :type name: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Radial: str = ...
    """
    Returns or sets  the radial axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Radial`` 
    
    :returns:  the radial axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Radial`` 
    
    :param axis:  the radial axis  
    :type axis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    ReferencePointJunction: str = ...
    """
    Returns or sets  the reference point junction of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencePointJunction`` 
    
    :returns:  the reference point junction  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencePointJunction`` 
    
    :param refPointJunction:  the reference point junction  
    :type refPointJunction: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary1: str = ...
    """
    Returns or sets  the rotary1 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary1`` 
    
    :returns:  the rotary1  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary1`` 
    
    :param rotary1:  the rotary1  
    :type rotary1: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary2: str = ...
    """
    Returns or sets  the rotary2 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary2`` 
    
    :returns:  the rotary2  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary2`` 
    
    :param rotary2:  the rotary2  
    :type rotary2: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary3: str = ...
    """
    Returns or sets  the rotary3 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary3`` 
    
    :returns:  the rotary3  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary3`` 
    
    :param rotary3:  the rotary3  
    :type rotary3: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary4: str = ...
    """
    Returns or sets  the rotary4 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary4`` 
    
    :returns:  the rotary4  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary4`` 
    
    :param rotary4:  the rotary4  
    :type rotary4: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary5: str = ...
    """
    Returns or sets  the rotary5 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary5`` 
    
    :returns:  the rotary5  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary5`` 
    
    :param rotary5:  the rotary5  
    :type rotary5: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Rotary6: str = ...
    """
    Returns or sets  the rotary6 axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Rotary6`` 
    
    :returns:  the rotary6  
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Rotary6`` 
    
    :param rotary6:  the rotary6  
    :type rotary6: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Setup: str = ...
    """
    Returns or sets  the setup component of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Setup`` 
    
    :returns:  the chain setup  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Setup`` 
    
    :param setup:  the chain setup  
    :type setup: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Type: KinematicChainTypes = ...
    """
    Returns or sets  the type of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns:  the chain type  
    :rtype: :py:class:`NXOpen.SIM.KinematicChainTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param chainType:  the chain type  
    :type chainType: :py:class:`NXOpen.SIM.KinematicChainTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    X: str = ...
    """
    Returns or sets  the X axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``X`` 
    
    :returns:  the x axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``X`` 
    
    :param xAxis:  the x axis  
    :type xAxis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Y: str = ...
    """
    Returns or sets  the Y axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Y`` 
    
    :returns:  the Y axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Y`` 
    
    :param yAxis:  the Y axis  
    :type yAxis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Z: str = ...
    """
    Returns or sets  the Z axis of the kinematic chain 
    
    <hr>
    
    Getter Method
    
    Signature ``Z`` 
    
    :returns:  the z axis  
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Z`` 
    
    :param zAxis:  the z axis  
    :type zAxis: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: KinematicChain = ...  # unknown typename


class NcChannelSelectionData(NXOpen.NXObject):
    """
    Represents the NcChannelSelectionData class object  
    
    Use the :py:class:`NXOpen.SIM.NcChannelSelectionData` class to create a NcChannelSelectionData object.
    
    .. versionadded:: NX9.0.0
    """
    
    @typing.overload
    def AssignFile(self, channel: int, file: str) -> None:
        """
        Assign a file to a channel using the channel number. 
        
        Signature ``AssignFile(channel, file)`` 
        
        :param channel:  The channel number  
        :type channel: int 
        :param file:  The file to be assigned  
        :type file: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    @typing.overload
    def AssignFile(self, channel: str, file: str) -> None:
        """
        Assign a file to a channel using the channel name. 
        
        Signature ``AssignFile(channel, file)`` 
        
        :param channel:  The channel name  
        :type channel: str 
        :param file:  The file to be assigned  
        :type file: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    Null: NcChannelSelectionData = ...  # unknown typename


class KinematicAxisBuilderAxisDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicAxisBuilderAxisDirectionType():
    """
    The axis direction type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PositiveX", "positive X-axis"
       "NegativeX", "negative X-axis"
       "PositiveY", "positive Y-axis"
       "NegativeY", "negative Y-axis"
       "PositiveZ", "positive Z-axis"
       "NegativeZ", "negative Z-axis"
    """
    PositiveX = 0  # KinematicAxisBuilderAxisDirectionTypeMemberType
    NegativeX = 1  # KinematicAxisBuilderAxisDirectionTypeMemberType
    PositiveY = 2  # KinematicAxisBuilderAxisDirectionTypeMemberType
    NegativeY = 3  # KinematicAxisBuilderAxisDirectionTypeMemberType
    PositiveZ = 4  # KinematicAxisBuilderAxisDirectionTypeMemberType
    NegativeZ = 5  # KinematicAxisBuilderAxisDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicAxisBuilderAxisMotionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicAxisBuilderAxisMotionType():
    """
    The axis motions type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LinearNcAxis", "linear NC-axis"
       "RotaryNcAxis", "rotary NC-axis"
       "Linear", "linear axis"
       "Rotary", "rotary axis"
       "RotaryUnlimitedNcAxis", "rotary unlimited NC-axis"
       "SpindleNcAxis", "spindle NC-axis"
       "RotaryUnlimited", "rotary axis unlimited"
       "Spindle", "spindle"
    """
    LinearNcAxis = 0  # KinematicAxisBuilderAxisMotionTypeMemberType
    RotaryNcAxis = 1  # KinematicAxisBuilderAxisMotionTypeMemberType
    Linear = 2  # KinematicAxisBuilderAxisMotionTypeMemberType
    Rotary = 3  # KinematicAxisBuilderAxisMotionTypeMemberType
    RotaryUnlimitedNcAxis = 4  # KinematicAxisBuilderAxisMotionTypeMemberType
    SpindleNcAxis = 5  # KinematicAxisBuilderAxisMotionTypeMemberType
    RotaryUnlimited = 6  # KinematicAxisBuilderAxisMotionTypeMemberType
    Spindle = 7  # KinematicAxisBuilderAxisMotionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicAxisBuilder(NXOpen.Builder):
    """
    Represents the SimKimAxisBuilder class object  
    
    Use the :py:class:`NXOpen.SIM.KinematicConfigurator` class to create a KinematicAxisBuilder object.
    
    .. versionadded:: NX7.5.0
    """
    
    class AxisDirectionType():
        """
        The axis direction type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PositiveX", "positive X-axis"
           "NegativeX", "negative X-axis"
           "PositiveY", "positive Y-axis"
           "NegativeY", "negative Y-axis"
           "PositiveZ", "positive Z-axis"
           "NegativeZ", "negative Z-axis"
        """
        PositiveX = 0  # KinematicAxisBuilderAxisDirectionTypeMemberType
        NegativeX = 1  # KinematicAxisBuilderAxisDirectionTypeMemberType
        PositiveY = 2  # KinematicAxisBuilderAxisDirectionTypeMemberType
        NegativeY = 3  # KinematicAxisBuilderAxisDirectionTypeMemberType
        PositiveZ = 4  # KinematicAxisBuilderAxisDirectionTypeMemberType
        NegativeZ = 5  # KinematicAxisBuilderAxisDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AxisMotionType():
        """
        The axis motions type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LinearNcAxis", "linear NC-axis"
           "RotaryNcAxis", "rotary NC-axis"
           "Linear", "linear axis"
           "Rotary", "rotary axis"
           "RotaryUnlimitedNcAxis", "rotary unlimited NC-axis"
           "SpindleNcAxis", "spindle NC-axis"
           "RotaryUnlimited", "rotary axis unlimited"
           "Spindle", "spindle"
        """
        LinearNcAxis = 0  # KinematicAxisBuilderAxisMotionTypeMemberType
        RotaryNcAxis = 1  # KinematicAxisBuilderAxisMotionTypeMemberType
        Linear = 2  # KinematicAxisBuilderAxisMotionTypeMemberType
        Rotary = 3  # KinematicAxisBuilderAxisMotionTypeMemberType
        RotaryUnlimitedNcAxis = 4  # KinematicAxisBuilderAxisMotionTypeMemberType
        SpindleNcAxis = 5  # KinematicAxisBuilderAxisMotionTypeMemberType
        RotaryUnlimited = 6  # KinematicAxisBuilderAxisMotionTypeMemberType
        Spindle = 7  # KinematicAxisBuilderAxisMotionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    CoarsePrecision: float = ...
    """
    Returns or sets  the coarse precision.  
    
    This defines the exact stop precision used to determine if a target point has been
    reached, so that the next NC-block can be executed. 
    
    <hr>
    
    Getter Method
    
    Signature ``CoarsePrecision`` 
    
    :returns:  the Coarse Precision  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``CoarsePrecision`` 
    
    :param coarse:  the Coarse Precision  
    :type coarse: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Direction: KinematicAxisBuilderAxisDirectionType = ...
    """
    Returns or sets  the axis direction 
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns:  the axis direction  
    :rtype: :py:class:`NXOpen.SIM.KinematicAxisBuilderAxisDirectionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param axisDir:  the axis direction  
    :type axisDir: :py:class:`NXOpen.SIM.KinematicAxisBuilderAxisDirectionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    FinePrecision: float = ...
    """
    Returns or sets  the fine precision.  
    
    This defines the exact stop precision used to determine if a target point has been
    reached, so that the next NC-block can be executed. 
    
    <hr>
    
    Getter Method
    
    Signature ``FinePrecision`` 
    
    :returns:  the Fine Precision  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``FinePrecision`` 
    
    :param fine:  the Fine Precision  
    :type fine: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    InitialValue: float = ...
    """
    Returns or sets  the initial value 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialValue`` 
    
    :returns:  the initial value  
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialValue`` 
    
    :param initial:  the initial value  
    :type initial: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    JerkLimit: float = ...
    """
    Returns or sets  the jerk limit.  
    
    The jerk limit value limits jumps in acceleration. 
    
    <hr>
    
    Getter Method
    
    Signature ``JerkLimit`` 
    
    :returns:  the jerk limit  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``JerkLimit`` 
    
    :param jerk:  the jerk limit  
    :type jerk: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    JumpVelocity: float = ...
    """
    Returns or sets  the jump velocity.  
    
    The jump velocity define a lag time at the beginning of the motion. 
    
    <hr>
    
    Getter Method
    
    Signature ``JumpVelocity`` 
    
    :returns:  the jerk limit  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``JumpVelocity`` 
    
    :param jump:  the Jump Velocity  
    :type jump: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Junction: KinematicJunction = ...
    """
    Returns or sets  the junction 
    
    <hr>
    
    Getter Method
    
    Signature ``Junction`` 
    
    :returns:  the junction  
    :rtype: :py:class:`NXOpen.SIM.KinematicJunction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Junction`` 
    
    :param jct:  the junction  
    :type jct: :py:class:`NXOpen.SIM.KinematicJunction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Kv: float = ...
    """
    Returns or sets  the kv.  
    
    the Kv-Factor is a parameter of the drives. It influences the dragging error (difference
    between ideal motion profile and actual motion profile). 
    
    <hr>
    
    Getter Method
    
    Signature ``Kv`` 
    
    :returns:  the Kv  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Kv`` 
    
    :param kv:  the Kv  
    :type kv: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Limit: bool = ...
    """
    Returns or sets  the axis limits flag
    
    This property is deprecated. Use :py:meth:`SIM.KinematicAxisBuilder.AxisMotionType` instead.
    
    <hr>
    
    Getter Method
    
    Signature ``Limit`` 
    
    :returns:  the axis limits flag  
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX9.0.3
       Use :py:meth:`SIM.KinematicAxisBuilder.AxisMotionType` instead.
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Limit`` 
    
    :param onOff:  the axis limits flag  
    :type onOff: bool 
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX9.0.3
       Use :py:meth:`SIM.KinematicAxisBuilder.AxisMotionType` instead.
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    LowerLimit: float = ...
    """
    Returns or sets  the lower limit 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerLimit`` 
    
    :returns:  the lower limit  
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``LowerLimit`` 
    
    :param lower:  the lower limit  
    :type lower: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    LowerSoftLimit: float = ...
    """
    Returns or sets  the lower soft limit.  
    
    The soft limit on the real machine is checked by the controller to avoid that the machine
    travels into the mechanical stop (Hard Limit) with full speed (prevent damage) 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerSoftLimit`` 
    
    :returns:  the lower soft limit  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``LowerSoftLimit`` 
    
    :param lower:  the lower soft limit  
    :type lower: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    MaxAcceleration: float = ...
    """
    Returns or sets  the max acceleration.  
    
    The maximum acceleration defines how fast the axis can accelerate. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxAcceleration`` 
    
    :returns:  the Max Acceleration  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``MaxAcceleration`` 
    
    :param max:  the Max Acceleration  
    :type max: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    MaxDeceleration: float = ...
    """
    Returns or sets  the max deceleration.  
    
    The maximum deceleration defines how fast the axis can decelerate. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxDeceleration`` 
    
    :returns:  the Max Deceleration  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``MaxDeceleration`` 
    
    :param max:  the Max Deceleration  
    :type max: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    MaximumVelocity: float = ...
    """
    Returns or sets  the maximum velocity 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumVelocity`` 
    
    :returns:  the maximum velocity  
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumVelocity`` 
    
    :param velocity:  the maximum velocity  
    :type velocity: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Name: str = ...
    """
    Returns or sets  the kinematic axis's name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The axis's name  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  the axis's new name  
    :type name: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Number: int = ...
    """
    Returns or sets  the kinematic axis's number.  
    
    The axis number is used in cases where an axis is programmed through a number 
    instead of through an address (e.g. on Siemens 840D: AX1=10 instead of X10).
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns:  The axis's number  
    :rtype: int 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number:  the axis's new number  
    :type number: int 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Type: KinematicAxisBuilderAxisMotionType = ...
    """
    Returns or sets  the axis motion 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns:  the axis type  
    :rtype: :py:class:`NXOpen.SIM.KinematicAxisBuilderAxisMotionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type:  the axis type  
    :type type: :py:class:`NXOpen.SIM.KinematicAxisBuilderAxisMotionType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    UpperLimit: float = ...
    """
    Returns or sets  the upper limit 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperLimit`` 
    
    :returns:  the upper limit  
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``UpperLimit`` 
    
    :param upper:  the upper limit  
    :type upper: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    UpperSoftLimit: float = ...
    """
    Returns or sets  the upper soft limit.  
    
    The soft limit on the real machine is checked by the controller to avoid that the machine
    travels into the mechanical stop (Hard Limit) with full speed (prevent damage) 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperSoftLimit`` 
    
    :returns:  the upper soft limit  
    :rtype: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``UpperSoftLimit`` 
    
    :param upper:  the upper soft limit  
    :type upper: float 
    
    .. versionadded:: NX9.0.3
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: KinematicAxisBuilder = ...  # unknown typename


class ExportMachineKitBuilder(NXOpen.Builder):
    """
    This class is used for the Export Machine Kit Dialog.  
    
    Calling :py:meth:`Builder.Commit` on this
    builder will start the export machine kit process
    and return None.
    
    Use  :py:meth:`NXOpen.SIM.KinematicConfigurator.ExportMachineKitBuilder` class to obtain an instance of this class.
    
    .. versionadded:: NX11.0.0
    """
    
    def GetAllKitPaths(self) -> 'list[str]':
        """
        Returns a array of the the file paths that are already in the machine kit.  
        
        If you want to modify what
        will export with the kit, you need to specify the whole kit path. This function gives the opportunity. 
        This function allocates the memory for kitPaths. The caller is responsible to deallocate the memory. 
        
        Signature ``GetAllKitPaths()`` 
        
        :returns:  array of all files of the machine kit 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddKitFile(self, directory: str, file: str) -> None:
        """
        Add a file to the machine kit at the given directory.  
        
        The directory can be get in the function GetAllKitPaths.
        
        Signature ``AddKitFile(directory, file)`` 
        
        :param directory:  directory in kit 
        :type directory: str 
        :param file:  file path on the hrd drive 
        :type file: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddKitFolder(self, directory: str, folder: str) -> None:
        """
        Add a folder, all containing files and subfolder to the machine kit at the given directory.  
        
        The directory can be get in the function GetAllKitPaths.
        
        Signature ``AddKitFolder(directory, folder)`` 
        
        :param directory:  directory in kit 
        :type directory: str 
        :param folder:  folder path on the hrd drive 
        :type folder: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddKitDirectory(self, directory: str, subDirectory: str) -> None:
        """
        Add a subdirectory to the machine kit at the given directory.  
        
        The directory can be get in the function GetAllKitPaths.
        
        Signature ``AddKitDirectory(directory, subDirectory)`` 
        
        :param directory:  directory in kit 
        :type directory: str 
        :param subDirectory:  subdirectory name 
        :type subDirectory: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameKitDirectory(self, directory: str, newDirectoryName: str) -> None:
        """
        Rename a directory to the machine kit at the given directory.  
        
        The directory can be get in the function GetAllKitPaths.
        
        Signature ``RenameKitDirectory(directory, newDirectoryName)`` 
        
        :param directory:  directory path in kit 
        :type directory: str 
        :param newDirectoryName:  new name of the directory 
        :type newDirectoryName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RemovePathInKit(self, directory: str) -> None:
        """
        Removes the given file or directory in the machine kit.  
        
        The directory can be get in the function GetAllKitPaths.
        
        Signature ``RemovePathInKit(directory)`` 
        
        :param directory:  directory in kit 
        :type directory: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    KitName: str = ...
    """
    Returns or sets  the kit name specify the name of the package.  
    
    The name should be unique in the target directory.
    
    <hr>
    
    Getter Method
    
    Signature ``KitName`` 
    
    :returns:  kit name  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``KitName`` 
    
    :param kitName:  kit name  
    :type kitName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    OutputDirectory: str = ...
    """
    Returns or sets  the machine kit output directory specify where the finished package will be stored.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputDirectory`` 
    
    :returns:  machine kit output directory  
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputDirectory`` 
    
    :param outputDirectory:  machine kit output directory  
    :type outputDirectory: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    PrintReport: bool = ...
    """
    Returns or sets  the machine kit print report checkbox specify if a report will be plotted while create the kit or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrintReport`` 
    
    :returns:  print report flag  
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``PrintReport`` 
    
    :param onOff:  print report flag  
    :type onOff: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: ExportMachineKitBuilder = ...  # unknown typename


class KinematicChannelConfigurationBuilder(NXOpen.Builder):
    """
    This class is used for channel configuration.  
    
    Calling :py:meth:`Builder.Commit` on this builder will return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateChannelConfigurationBuilder`
    
    .. versionadded:: NX9.0.3
    """
    KinematicChannels: KinematicChannelBuilderList = ...
    """
    Returns  the list of kinematic channel 
    
    <hr>
    
    Getter Method
    
    Signature ``KinematicChannels`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.KinematicChannelBuilderList` 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    Null: KinematicChannelConfigurationBuilder = ...  # unknown typename


class KinematicComponentCollection(NXOpen.TaggedObjectCollection):
    """
    Represents the SimKimComponent Collection   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.SIM.KinematicConfigurator`
    
    .. versionadded:: NX7.5.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, sid: str) -> KinematicComponent:
        """
        Finds the SIM.  
        
        KinematicComponent object with the given identifier as recorded in a journal. 
        
        Signature ``FindObject(sid)`` 
        
        :param sid:  the name of the object  
        :type sid: str 
        :returns:  the found object  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponent` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateComponentBuilder(self, parent: KinematicComponent, comp: KinematicComponent) -> KinematicComponentBuilder:
        """
        Creates a builder for a kinematic component  
        
        Signature ``CreateComponentBuilder(parent, comp)`` 
        
        :param parent:  The parent for the new component.                                                                                         Can be NULL  
        :type parent: :py:class:`NXOpen.SIM.KinematicComponent` 
        :param comp:  The component to edit. If NULL, a                                                                                         new component will be created   
        :type comp: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The component builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def CreateMachineBaseComponentBuilder(self, machine: KinematicComponent) -> KinematicComponentBuilder:
        """
        Creates a builder for a machine base component.  
        
        Signature ``CreateMachineBaseComponentBuilder(machine)`` 
        
        :param machine:  The machine base component to edit.                                                                                    If NULL, then a new machine base component                                                                                    is created  
        :type machine: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The new machine base component builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def CreateToolBaseComponentBuilder(self, tool: KinematicComponent) -> KinematicComponentBuilder:
        """
        Creates a bulder for tool base component.  
        
        Signature ``CreateToolBaseComponentBuilder(tool)`` 
        
        :param tool:  The tool component to edit. If NULL,                                                                                    then a new tool base component is                                                                                     created  
        :type tool: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The new tool base component builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def CreateHeadBaseComponentBuilder(self, head: KinematicComponent) -> KinematicComponentBuilder:
        """
        Creates a bulder for head base component.  
        
        Signature ``CreateHeadBaseComponentBuilder(head)`` 
        
        :param head:  The head component to edit. If NULL,                                                                                    then a new head base component is                                                                                     created  
        :type head: :py:class:`NXOpen.SIM.KinematicComponent` 
        :returns:  The new head base component builder  
        :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    


class KinematicJunctionBuilderSystemClassMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicJunctionBuilderSystemClass():
    """
    The junction system classes 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no specal class"
       "Mount", "a mounting junction"
       "MachineZero", "the machine zero junction"
       "ToolZero", "the tool mounting point"
       "ToolTip", "The tool tip junction"
       "LatheWpZx", "Lathe Work Plane Z/X"
       "LatheWpXy", "Lathe Work Plane X/Y"
    """
    NotSet = 0  # KinematicJunctionBuilderSystemClassMemberType
    Mount = 1  # KinematicJunctionBuilderSystemClassMemberType
    MachineZero = 2  # KinematicJunctionBuilderSystemClassMemberType
    ToolZero = 3  # KinematicJunctionBuilderSystemClassMemberType
    ToolTip = 4  # KinematicJunctionBuilderSystemClassMemberType
    LatheWpZx = 5  # KinematicJunctionBuilderSystemClassMemberType
    LatheWpXy = 6  # KinematicJunctionBuilderSystemClassMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicJunctionBuilder(NXOpen.Builder):
    """
    Represents the SimKimJunctionBuilder class object  
    
    Use the :py:class:`NXOpen.SIM.KinematicConfigurator` class to create a KinematicJunctionBuilder object.
    
    .. versionadded:: NX7.5.0
    """
    
    class SystemClass():
        """
        The junction system classes 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no specal class"
           "Mount", "a mounting junction"
           "MachineZero", "the machine zero junction"
           "ToolZero", "the tool mounting point"
           "ToolTip", "The tool tip junction"
           "LatheWpZx", "Lathe Work Plane Z/X"
           "LatheWpXy", "Lathe Work Plane X/Y"
        """
        NotSet = 0  # KinematicJunctionBuilderSystemClassMemberType
        Mount = 1  # KinematicJunctionBuilderSystemClassMemberType
        MachineZero = 2  # KinematicJunctionBuilderSystemClassMemberType
        ToolZero = 3  # KinematicJunctionBuilderSystemClassMemberType
        ToolTip = 4  # KinematicJunctionBuilderSystemClassMemberType
        LatheWpZx = 5  # KinematicJunctionBuilderSystemClassMemberType
        LatheWpXy = 6  # KinematicJunctionBuilderSystemClassMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateDefaultCsys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Create the default CSYS based on WCS  
        
        Signature ``CreateDefaultCsys()`` 
        
        :returns:  the default csys  
        :rtype: :py:class:`NXOpen.CartesianCoordinateSystem` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def CreateTooltipCsys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Create the tooltip CSYS  
        
        Signature ``CreateTooltipCsys()`` 
        
        :returns:  the tooltip csys  
        :rtype: :py:class:`NXOpen.CartesianCoordinateSystem` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def IsMachineZero(self) -> bool:
        """
        Test if this is a machine zero junction  
        
        Signature ``IsMachineZero()`` 
        
        :returns:  true if it is the machine zero junction  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def IsToolMount(self) -> bool:
        """
        Test if the junction is a tool mount junctions  
        
        Signature ``IsToolMount()`` 
        
        :returns:  true if it is a tool mount junction  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def IsToolTip(self) -> bool:
        """
        Test if the junction is a tool tip junctions  
        
        Signature ``IsToolTip()`` 
        
        :returns:  true if it is a tool tip junction  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    Classification: KinematicJunctionBuilderSystemClass = ...
    """
    Returns or sets  the classification of the junction 
    
    <hr>
    
    Getter Method
    
    Signature ``Classification`` 
    
    :returns:  the classification of the junction  
    :rtype: :py:class:`NXOpen.SIM.KinematicJunctionBuilderSystemClass` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    
    <hr>
    
    Setter Method
    
    Signature ``Classification`` 
    
    :param jctClass:  the classification of the junction  
    :type jctClass: :py:class:`NXOpen.SIM.KinematicJunctionBuilderSystemClass` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    """
    Csys: NXOpen.CartesianCoordinateSystem = ...
    """
    Returns or sets  the CSYS associated with the junction 
    
    <hr>
    
    Getter Method
    
    Signature ``Csys`` 
    
    :returns:  the csys  
    :rtype: :py:class:`NXOpen.CartesianCoordinateSystem` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    
    <hr>
    
    Setter Method
    
    Signature ``Csys`` 
    
    :param csys:  the csys  
    :type csys: :py:class:`NXOpen.CartesianCoordinateSystem` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    """
    Name: str = ...
    """
    Returns or sets  the kim junction's name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The junction's name  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  the junction's new name  
    :type name: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    """
    Null: KinematicJunctionBuilder = ...  # unknown typename


class ArchiveImportBuilder(NXOpen.Builder):
    """
    Represents a ArchiveImportBuilder builder object.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicConfigurator.CreateArchiveImportBuilder`
    
    .. versionadded:: NX9.0.3
    """
    FileName: str = ...
    """
    Returns or sets  the archive file name from which to import data 
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns:  The archive file name  
    :rtype: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param fileName:  The new archive file name  
    :type fileName: str 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    ImportCollisionAvoidance: bool = ...
    """
    Returns or sets  the setting for importing collision avoidance data.  
    
    If true then collision avoidance data will be imported instead of the machine configuration. 
    
    <hr>
    
    Getter Method
    
    Signature ``ImportCollisionAvoidance`` 
    
    :returns:  The setting for importing collision avoidance data  
    :rtype: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ImportCollisionAvoidance`` 
    
    :param importSetting:  The new setting for importing collision avoidance data 
    :type importSetting: bool 
    
    .. versionadded:: NX9.0.3
    
    License requirements: None.
    """
    Null: ArchiveImportBuilder = ...  # unknown typename


class SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes():
    """
    The object to replaces with types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Nothing", "Nothing"
       "ConvexHull", "Convex Hull"
       "BoundingSphere", "Bounding Sphere"
       "BoundingBlock", "Bounding Block"
       "BoundingCylinder", "Bounding Cylinder"
       "InscribedCylinder", "Inscribed Cylinder"
    """
    Nothing = 0  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    ConvexHull = 1  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    BoundingSphere = 2  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    BoundingBlock = 3  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    BoundingCylinder = 4  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    InscribedCylinder = 5  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SinumerikCaSimplifyBodiesBuilderCloseGapTypes():
    """
    Represents the close gap types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sharp", "Sharp"
       "Beveled", "Beveled"
       "NoOffset", "No Offset"
    """
    Sharp = 0  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
    Beveled = 1  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
    NoOffset = 2  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SinumerikCaSimplifyBodiesBuilder(NXOpen.Builder):
    """
    This class is used for replace geometry.  
    
    A call to :py:meth:`SinumerikCaSimplifyBodiesBuilder.DoReplace` will replace the geometry.
    Calling :py:meth:`Builder.Commit` on this builder will only return None.
    
    Use the :py:class:`Part` class to create a SinumerikCaSimplifyBodiesBuilder object.
    
    .. versionadded:: NX9.0.0
    """
    
    class ObjectToReplaceWithTypes():
        """
        The object to replaces with types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Nothing", "Nothing"
           "ConvexHull", "Convex Hull"
           "BoundingSphere", "Bounding Sphere"
           "BoundingBlock", "Bounding Block"
           "BoundingCylinder", "Bounding Cylinder"
           "InscribedCylinder", "Inscribed Cylinder"
        """
        Nothing = 0  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        ConvexHull = 1  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        BoundingSphere = 2  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        BoundingBlock = 3  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        BoundingCylinder = 4  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        InscribedCylinder = 5  # SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CloseGapTypes():
        """
        Represents the close gap types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sharp", "Sharp"
           "Beveled", "Beveled"
           "NoOffset", "No Offset"
        """
        Sharp = 0  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
        Beveled = 1  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
        NoOffset = 2  # SinumerikCaSimplifyBodiesBuilderCloseGapTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def DoReplace(self) -> None:
        """
        Replace the simplify bodies 
        
        Signature ``DoReplace()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
        """
        ...
    
    AddOffset: NXOpen.Expression = ...
    """
    Returns  the  Additional offset.  
    
    Will expand the wrap. 
    
    <hr>
    
    Getter Method
    
    Signature ``AddOffset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Associative: bool = ...
    """
    Returns or sets   the Remove parms switch 
    
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
    
    :param associative: 
    :type associative: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    CloseGaps: SinumerikCaSimplifyBodiesBuilderCloseGapTypes = ...
    """
    Returns or sets  the  Method used to close the gaps after offset of the wrap 
    
    <hr>
    
    Getter Method
    
    Signature ``CloseGaps`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderCloseGapTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CloseGaps`` 
    
    :param closeGaps: 
    :type closeGaps: :py:class:`NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderCloseGapTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    CoordSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``CoordSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CoordSystem`` 
    
    :param coordSystem: 
    :type coordSystem: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the Distance tolerance used to facet the solids.  
    
    Also used for default offset calculation. 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distTol: 
    :type distTol: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    ObjectToReplace: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the object to replace 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectToReplace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    PlanesList: NXOpen.PlaneList = ...
    """
    Returns  the Planes to split the geometry, tightens the wrap along this plane 
    
    <hr>
    
    Getter Method
    
    Signature ``PlanesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PlaneList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ReplaceWith: SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes = ...
    """
    Returns or sets  the object to replace with 
    
    <hr>
    
    Getter Method
    
    Signature ``ReplaceWith`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReplaceWith`` 
    
    :param objectToReplaceWith: 
    :type objectToReplaceWith: :py:class:`NXOpen.SIM.SinumerikCaSimplifyBodiesBuilderObjectToReplaceWithTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_isv_mtb ("Machine Tool Builder") OR nx_sinumerik_ca ("Sinumerik Collision Avoidance")
    """
    SplitOffset: NXOpen.Expression = ...
    """
    Returns  the Offset applied to both sides of the splitting planes.  
    
    <hr>
    
    Getter Method
    
    Signature ``SplitOffset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SinumerikCaSimplifyBodiesBuilder = ...  # unknown typename


class KinematicComponentBuilderRegisterTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicComponentBuilderRegisterTypes():
    """
    The register types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SameAsPocketId", "the pocket id defined the register"
       "Specify", "the register is specified"
    """
    SameAsPocketId = 0  # KinematicComponentBuilderRegisterTypesMemberType
    Specify = 1  # KinematicComponentBuilderRegisterTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicComponentBuilderWorkPositionAngleTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicComponentBuilderWorkPositionAngleTypes():
    """
    The Working Position Angle type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no angle specified"
       "SpecifyAngle", "angle is specified"
    """
    NotSet = 0  # KinematicComponentBuilderWorkPositionAngleTypesMemberType
    SpecifyAngle = 1  # KinematicComponentBuilderWorkPositionAngleTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicComponentBuilderSystemClassMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class KinematicComponentBuilderSystemClass():
    """
    The SIM KIM system classes 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Machine", "Machine Base classification"
       "Tool", "Tool classification"
       "Turret", "Device classification"
       "Pocket", "Static Holder classification"
       "Temporary", "Temporary classification"
       "Part", "Part - Setup classification"
       "Workpiece", "Workpiece - Setup classification"
       "SetupElement", "Any setup element classification"
       "Basic", "On available in a BASIC machine. If this bit is set, then the machine part can be used for simulation when only UG_ISV_BASIC license is available"
       "LatheSpindle", "Lathe Spindle classification"
       "PocketOnHead", "Dynamic Holder classification"
       "ToolCutting", "Tool Cutting classification"
       "Spinning", "Spinning classification"
       "Head", "Head class"
       "ToolNonCutting", " - "
    """
    Machine = 0  # KinematicComponentBuilderSystemClassMemberType
    Tool = 1  # KinematicComponentBuilderSystemClassMemberType
    Turret = 2  # KinematicComponentBuilderSystemClassMemberType
    Pocket = 3  # KinematicComponentBuilderSystemClassMemberType
    Temporary = 4  # KinematicComponentBuilderSystemClassMemberType
    Part = 5  # KinematicComponentBuilderSystemClassMemberType
    Workpiece = 6  # KinematicComponentBuilderSystemClassMemberType
    SetupElement = 7  # KinematicComponentBuilderSystemClassMemberType
    Basic = 8  # KinematicComponentBuilderSystemClassMemberType
    LatheSpindle = 9  # KinematicComponentBuilderSystemClassMemberType
    PocketOnHead = 10  # KinematicComponentBuilderSystemClassMemberType
    ToolCutting = 11  # KinematicComponentBuilderSystemClassMemberType
    Spinning = 12  # KinematicComponentBuilderSystemClassMemberType
    Head = 13  # KinematicComponentBuilderSystemClassMemberType
    ToolNonCutting = 14  # KinematicComponentBuilderSystemClassMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class KinematicComponentBuilder(NXOpen.Builder):
    """
    Represents the KinematicComponentBuilder class object  
    
    To create a new instance of this class, use :py:meth:`NXOpen.SIM.KinematicComponentCollection.CreateHeadBaseComponentBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    class RegisterTypes():
        """
        The register types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SameAsPocketId", "the pocket id defined the register"
           "Specify", "the register is specified"
        """
        SameAsPocketId = 0  # KinematicComponentBuilderRegisterTypesMemberType
        Specify = 1  # KinematicComponentBuilderRegisterTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class WorkPositionAngleTypes():
        """
        The Working Position Angle type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no angle specified"
           "SpecifyAngle", "angle is specified"
        """
        NotSet = 0  # KinematicComponentBuilderWorkPositionAngleTypesMemberType
        SpecifyAngle = 1  # KinematicComponentBuilderWorkPositionAngleTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SystemClass():
        """
        The SIM KIM system classes 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Machine", "Machine Base classification"
           "Tool", "Tool classification"
           "Turret", "Device classification"
           "Pocket", "Static Holder classification"
           "Temporary", "Temporary classification"
           "Part", "Part - Setup classification"
           "Workpiece", "Workpiece - Setup classification"
           "SetupElement", "Any setup element classification"
           "Basic", "On available in a BASIC machine. If this bit is set, then the machine part can be used for simulation when only UG_ISV_BASIC license is available"
           "LatheSpindle", "Lathe Spindle classification"
           "PocketOnHead", "Dynamic Holder classification"
           "ToolCutting", "Tool Cutting classification"
           "Spinning", "Spinning classification"
           "Head", "Head class"
           "ToolNonCutting", " - "
        """
        Machine = 0  # KinematicComponentBuilderSystemClassMemberType
        Tool = 1  # KinematicComponentBuilderSystemClassMemberType
        Turret = 2  # KinematicComponentBuilderSystemClassMemberType
        Pocket = 3  # KinematicComponentBuilderSystemClassMemberType
        Temporary = 4  # KinematicComponentBuilderSystemClassMemberType
        Part = 5  # KinematicComponentBuilderSystemClassMemberType
        Workpiece = 6  # KinematicComponentBuilderSystemClassMemberType
        SetupElement = 7  # KinematicComponentBuilderSystemClassMemberType
        Basic = 8  # KinematicComponentBuilderSystemClassMemberType
        LatheSpindle = 9  # KinematicComponentBuilderSystemClassMemberType
        PocketOnHead = 10  # KinematicComponentBuilderSystemClassMemberType
        ToolCutting = 11  # KinematicComponentBuilderSystemClassMemberType
        Spinning = 12  # KinematicComponentBuilderSystemClassMemberType
        Head = 13  # KinematicComponentBuilderSystemClassMemberType
        ToolNonCutting = 14  # KinematicComponentBuilderSystemClassMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetGeometries(self, geos: 'list[NXOpen.NXObject]') -> None:
        """
        Sets geometry elements for the component 
        
        Signature ``SetGeometries(geos)`` 
        
        :param geos:  the geometry elements  
        :type geos: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetGeometries(self) -> 'list[NXOpen.NXObject]':
        """
        Returns the geometry elements assigned to this component 
        
        Signature ``GetGeometries()`` 
        
        :returns:  The geometry elements  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteAllGeometries(self) -> None:
        """
        Deletes all geometry elements from the component 
        
        Signature ``DeleteAllGeometries()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddGeometry(self, geo: NXOpen.NXObject) -> None:
        """
        Adds a single geometry element 
        
        Signature ``AddGeometry(geo)`` 
        
        :param geo:  The geometry element to add  
        :type geo: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def DeleteGeometry(self, geo: NXOpen.NXObject) -> None:
        """
        Deletes a single geometry element from the component 
        
        Signature ``DeleteGeometry(geo)`` 
        
        :param geo:  The geometry to remove  
        :type geo: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetSaveIpw(self) -> bool:
        """
        Does the system save an IPW with the component?  
        
        Signature ``GetSaveIpw()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def SetSaveIpw(self, saveIpw: bool) -> None:
        """
        Save an IPW with the component 
        
        Signature ``SetSaveIpw(saveIpw)`` 
        
        :param saveIpw: 
        :type saveIpw: bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification")
        """
        ...
    
    
    def AddSystemClass(self, sysClass: KinematicComponentBuilderSystemClass) -> None:
        """
        Add a system class 
        
        Signature ``AddSystemClass(sysClass)`` 
        
        :param sysClass:  the system class to add  
        :type sysClass: :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def DeleteSystemClass(self, sysClasses: KinematicComponentBuilderSystemClass) -> None:
        """
        Delete a system class 
        
        Signature ``DeleteSystemClass(sysClasses)`` 
        
        :param sysClasses:  the system class to delete  
        :type sysClasses: :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetSystemClasses(self) -> 'list[KinematicComponentBuilderSystemClass]':
        """
        Returns the component's system classes 
        
        Signature ``GetSystemClasses()`` 
        
        :returns:  the component's system classes  
        :rtype: list of :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteAllSystemClasses(self) -> None:
        """
        Delete all system classes of the component 
        
        Signature ``DeleteAllSystemClasses()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def IsOfSystemClass(self, sysClass: KinematicComponentBuilderSystemClass) -> bool:
        """
        Test if the compomnent is a member of the given system class  
        
        Signature ``IsOfSystemClass(sysClass)`` 
        
        :param sysClass:  the system class to test  
        :type sysClass: :py:class:`NXOpen.SIM.KinematicComponentBuilderSystemClass` 
        :returns:  TRUE if component is of the system class  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
        """
        ...
    
    
    def AddUserClassName(self, uclass: str) -> None:
        """
        Adds a user class to the component 
        
        Signature ``AddUserClassName(uclass)`` 
        
        :param uclass:  The user cass to add  
        :type uclass: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteUserClassName(self, uclass: str) -> None:
        """
        Deletes a user class from the component 
        
        Signature ``DeleteUserClassName(uclass)`` 
        
        :param uclass:  The user cass to remove  
        :type uclass: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetUserClassNames(self) -> 'list[str]':
        """
        Get a list of user classes of the component  
        
        Signature ``GetUserClassNames()`` 
        
        :returns:  The user classes of the component  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddChannelName(self, channel: str) -> None:
        """
        Adds a channel name to the component 
        
        Signature ``AddChannelName(channel)`` 
        
        :param channel:  The channel name to add  
        :type channel: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteChannelName(self, channel: str) -> None:
        """
        Deletes a channel name from the component 
        
        Signature ``DeleteChannelName(channel)`` 
        
        :param channel:  The channel name to remove  
        :type channel: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetChannelNames(self) -> 'list[str]':
        """
        Get a list of channel names of the component  
        
        Signature ``GetChannelNames()`` 
        
        :returns:  The channel names of the component  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def AddHoldingSystem(self, holdSys: str) -> None:
        """
        Adds a holding system to the component 
        
        Signature ``AddHoldingSystem(holdSys)`` 
        
        :param holdSys:  The holding system to add  
        :type holdSys: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def DeleteHoldingSystem(self, holdSys: str) -> None:
        """
        Deletes a holding system from the component 
        
        Signature ``DeleteHoldingSystem(holdSys)`` 
        
        :param holdSys:  The holding system to remove  
        :type holdSys: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def GetHoldingSystems(self) -> 'list[str]':
        """
        Get a list of holding systems of the component  
        
        Signature ``GetHoldingSystems()`` 
        
        :returns:  The channel names of the component  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameUserClass(self, oldName: str, newName: str) -> None:
        """
        Renames a user class from the component 
        
        Signature ``RenameUserClass(oldName, newName)`` 
        
        :param oldName:  The old user class  
        :type oldName: str 
        :param newName:  The new user class  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameHoldingSystem(self, oldName: str, newName: str) -> None:
        """
        Renames a holding system from the component 
        
        Signature ``RenameHoldingSystem(oldName, newName)`` 
        
        :param oldName:  The old holding system  
        :type oldName: str 
        :param newName:  The new holding system  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    
    def RenameChannelName(self, oldName: str, newName: str) -> None:
        """
        Renames a channel name from the component 
        
        Signature ``RenameChannelName(oldName, newName)`` 
        
        :param oldName:  The old channel name  
        :type oldName: str 
        :param newName:  The new channel name  
        :type newName: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
        """
        ...
    
    AdjustRegister: int = ...
    """
    Returns or sets  the adjust register 
    
    <hr>
    
    Getter Method
    
    Signature ``AdjustRegister`` 
    
    :returns:  the adjust regsiter  
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``AdjustRegister`` 
    
    :param adjustReg:  the adjust regsiter  
    :type adjustReg: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    AdjustRegisterType: KinematicComponentBuilderRegisterTypes = ...
    """
    Returns or sets  the adjust register type 
    
    <hr>
    
    Getter Method
    
    Signature ``AdjustRegisterType`` 
    
    :returns:  the adjust register type  
    :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilderRegisterTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``AdjustRegisterType`` 
    
    :param regType:  the adjust register type  
    :type regType: :py:class:`NXOpen.SIM.KinematicComponentBuilderRegisterTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    CutcomRegister: int = ...
    """
    Returns or sets  the cutcom register 
    
    <hr>
    
    Getter Method
    
    Signature ``CutcomRegister`` 
    
    :returns:  the cutcom register  
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``CutcomRegister`` 
    
    :param cutcomReg:  the cutcom register  
    :type cutcomReg: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    CutcomRegisterType: KinematicComponentBuilderRegisterTypes = ...
    """
    Returns or sets  the cutcom register type 
    
    <hr>
    
    Getter Method
    
    Signature ``CutcomRegisterType`` 
    
    :returns:  the cutcom register type  
    :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilderRegisterTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``CutcomRegisterType`` 
    
    :param regType:  the cutcom register type  
    :type regType: :py:class:`NXOpen.SIM.KinematicComponentBuilderRegisterTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    CutterId: str = ...
    """
    Returns or sets  the cutter id string to identify a cutter within a multitool 
    
    <hr>
    
    Getter Method
    
    Signature ``CutterId`` 
    
    :returns:  the cutter id string  
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``CutterId`` 
    
    :param cutterIdString:  the new cutter id  string  
    :type cutterIdString: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    DeviceId: str = ...
    """
    Returns or sets  the device id 
    
    <hr>
    
    Getter Method
    
    Signature ``DeviceId`` 
    
    :returns:  the component's device id  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``DeviceId`` 
    
    :param deviceId:  the new device id  
    :type deviceId: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    HolderId: int = ...
    """
    Returns or sets  the holder id 
    
    <hr>
    
    Getter Method
    
    Signature ``HolderId`` 
    
    :returns:  the holder id  
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``HolderId`` 
    
    :param holderId:  the holder id  
    :type holderId: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    HolderIdString: str = ...
    """
    Returns or sets  the holder id in string 
    
    <hr>
    
    Getter Method
    
    Signature ``HolderIdString`` 
    
    :returns:  the holder id in string  
    :rtype: str 
    
    .. versionadded:: NX7.5.5
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``HolderIdString`` 
    
    :param holderIdString:  the new holder id in string  
    :type holderIdString: str 
    
    .. versionadded:: NX7.5.5
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    JunctionList: KinematicJunctionBuilderList = ...
    """
    Returns  the junction list 
    
    <hr>
    
    Getter Method
    
    Signature ``JunctionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SIM.KinematicJunctionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    """
    Name: str = ...
    """
    Returns or sets  the kim component's name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  The component's name  
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name:  the component's new name  
    :type name: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder") OR resource_manager_nx ("Teamcenter Resource Manager")
    """
    NumberOfTools: int = ...
    """
    Returns or sets  the number of tools 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfTools`` 
    
    :returns:  the max number of tools  
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfTools`` 
    
    :param numTools:  the number of tools  
    :type numTools: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    WorkPositionAngle: float = ...
    """
    Returns or sets  the working position angle 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkPositionAngle`` 
    
    :returns:  the working position angle  
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``WorkPositionAngle`` 
    
    :param angle:  the working position angle  
    :type angle: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    WorkPositionAngleType: KinematicComponentBuilderWorkPositionAngleTypes = ...
    """
    Returns or sets  the working position angle type 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkPositionAngleType`` 
    
    :returns:  The working position angle type  
    :rtype: :py:class:`NXOpen.SIM.KinematicComponentBuilderWorkPositionAngleTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    
    <hr>
    
    Setter Method
    
    Signature ``WorkPositionAngleType`` 
    
    :param type:  The working position angle type  
    :type type: :py:class:`NXOpen.SIM.KinematicComponentBuilderWorkPositionAngleTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ug_isv_full ("Full functionality for Integrated Simulation and Verification") OR nx_isv_mtb ("Machine Tool Builder")
    """
    Null: KinematicComponentBuilder = ...  # unknown typename


