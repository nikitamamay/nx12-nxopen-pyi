# module 'NXOpen.DMU'
#
# Automatically generated 2025-06-09T14:38:45.589882
#
"""Default documentation for NXOpen.DMU."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class DMUManager():
    """
    Represents an object that manages DMU application specific objects and preferences.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX12.0.0
    """
    
    def CreateSnapshotCollection(self, part: NXOpen.Part) -> SnapshotCollection:
        """
        Creates the :py:class:`NXOpen.DMU.SnapshotCollection` in the part.  
        
        At max only one instance of :py:class:`NXOpen.DMU.SnapshotCollection`
        can be created in a part.
        
        Signature ``CreateSnapshotCollection(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.DMU.SnapshotCollection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def GetSnapshotCollection(self, part: NXOpen.Part) -> SnapshotCollection:
        """
        Returns the :py:class:`NXOpen.DMU.SnapshotCollection` in the part.  
        
        Signature ``GetSnapshotCollection(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.DMU.SnapshotCollection` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ResetToDesignState(self, part: NXOpen.Part) -> None:
        """
        Resets the changes made to the part, related to the assets which can be captured in the 
        :py:class:`NXOpen.DMU.ISnapshot`.  
        
        Signature ``ResetToDesignState(part)`` 
        
        :param part:  Part that will get reset to design state 
        :type part: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @staticmethod
    def GetDMUManager():
        ...
    


class DMUDebugSession():
    """
    Represents a class that is used for DMU testing.  
    
    This class shouldn't be made available to customers 
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX12.0.0
    """
    
    def ValidateWorksets(self) -> None:
        """
        Prints validation information for worksets 
        
        Signature ``ValidateWorksets()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ValidateSnapshots(self, part: NXOpen.Part) -> None:
        """
        Prints validation information for snapshots in the given part 
        
        Signature ``ValidateSnapshots(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def ValidateAllObjects(self) -> None:
        """
        Prints validation information for all objects 
        
        Signature ``ValidateAllObjects()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    @staticmethod
    def GetDMUDebugSession():
        ...
    


class ISnapshot(NXOpen.INXObject):
    """
    Represents the :py:class:`NXOpen.DMU.ISnapshot` object.  
    
    .. versionadded:: NX12.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class Snapshot(NXOpen.NXObject, ISnapshot):
    """
    Represents the :py:class:`NXOpen.DMU.Snapshot` object.  
    
    To create a new instance of this class, use the :py:class:`NXOpen.DMU.SnapshotCollection` class. 
    
    Instances of this class can be created through DMU.SnapshotCollection object
    
    .. versionadded:: NX12.0.0
    """
    
    def Apply(self) -> None:
        """
        Applies a :py:class:`NXOpen.DMU.ISnapshot` on current model.  
        
        Signature ``Apply()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Delete(self) -> None:
        """
        Deletes a :py:class:`NXOpen.DMU.ISnapshot` object.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def Replace(self) -> None:
        """
        Replaces a :py:class:`NXOpen.DMU.ISnapshot` object with current state of model.  
        
        Signature ``Replace()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def UpdateAssets(self, assetsToBeCaptured: 'list[str]', assetsToBeRemoved: 'list[str]') -> None:
        """
        Captures and removes selective assets to :py:class:`NXOpen.DMU.ISnapshot`.  
        
        If the asset already exists while capture, then it will get over-written.
        
        Signature ``UpdateAssets(assetsToBeCaptured, assetsToBeRemoved)`` 
        
        :param assetsToBeCaptured:  the ids of the assets to be captured  
        :type assetsToBeCaptured: list of str 
        :param assetsToBeRemoved:  the ids of the assets to be removed  
        :type assetsToBeRemoved: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: Snapshot = ...  # unknown typename


class SnapshotCollection(NXOpen.NXObject):
    """
    Represents the collection object for all snapshot in a part.  
    
    No KF support.
    
    .. versionadded:: NX12.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSnapshot(self) -> ISnapshot:
        """
        Creates a :py:class:`NXOpen.DMU.ISnapshot` in the collection.  
        
        Signature ``CreateSnapshot()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.DMU.ISnapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def InsertSnapshot(self, targetSnapshot: ISnapshot) -> ISnapshot:
        """
        Creates and inserts a :py:class:`NXOpen.DMU.ISnapshot` in the collection before the target :py:class:`NXOpen.DMU.ISnapshot`.  
        
        Signature ``InsertSnapshot(targetSnapshot)`` 
        
        :param targetSnapshot: 
        :type targetSnapshot: :py:class:`NXOpen.DMU.ISnapshot` 
        :returns: 
        :rtype: :py:class:`NXOpen.DMU.ISnapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def MoveSnapshotsBefore(self, targetSnapshot: ISnapshot, sourceSnapshots: 'list[ISnapshot]') -> None:
        """
        Moves sourceSnapshots :py:class:`NXOpen.DMU.ISnapshot` in the collection before the targetSnapshot :py:class:`NXOpen.DMU.ISnapshot`.  
        
        Signature ``MoveSnapshotsBefore(targetSnapshot, sourceSnapshots)`` 
        
        :param targetSnapshot: 
        :type targetSnapshot: :py:class:`NXOpen.DMU.ISnapshot` 
        :param sourceSnapshots: 
        :type sourceSnapshots: list of :py:class:`NXOpen.DMU.ISnapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    
    def MoveSnapshotsAfter(self, targetSnapshot: ISnapshot, sourceSnapshots: 'list[ISnapshot]') -> None:
        """
        Moves sourceSnapshots :py:class:`NXOpen.DMU.ISnapshot` in the collection after the targetSnapshot :py:class:`NXOpen.DMU.ISnapshot`.  
        
        Signature ``MoveSnapshotsAfter(targetSnapshot, sourceSnapshots)`` 
        
        :param targetSnapshot: 
        :type targetSnapshot: :py:class:`NXOpen.DMU.ISnapshot` 
        :param sourceSnapshots: 
        :type sourceSnapshots: list of :py:class:`NXOpen.DMU.ISnapshot` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: assemblies ("ASSEMBLIES MODULE")
        """
        ...
    
    Null: SnapshotCollection = ...  # unknown typename


