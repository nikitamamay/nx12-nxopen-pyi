# module 'NXOpen.PLAS'
#
# Automatically generated 2025-06-09T14:38:47.234733
#
"""Default documentation for NXOpen.PLAS."""

import typing

import NXOpen
import NXOpen.PDM



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class Run(NXOpen.PDM.ElementGroup):
    """
    Represents the Run class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.PLAS.RunBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    def ReparentBranch(self, destinationRun: Run, oldbranch: NXOpen.PDM.OrderedElementGroup) -> NXOpen.PDM.OrderedElementGroup:
        """
        Moves branch from one run to another.  
        
        the original branch will be destroyed  
        
        Signature ``ReparentBranch(destinationRun, oldbranch)`` 
        
        :param destinationRun: 
        :type destinationRun: :py:class:`NXOpen.PLAS.Run` 
        :param oldbranch: 
        :type oldbranch: :py:class:`NXOpen.PDM.OrderedElementGroup` 
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.OrderedElementGroup` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetBranches(self) -> 'list[NXOpen.PDM.OrderedElementGroup]':
        """
        Get the branches in the run.  
        
        Signature ``GetBranches()`` 
        
        :returns:  the collection of branches in the run  
        :rtype: list of :py:class:`NXOpen.PDM.OrderedElementGroup` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Run = ...  # unknown typename


class PlasManager():
    """
    A manager to deal with all objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX11.0.1
    """
    
    def CreateRunBuilder(self, run: Run) -> RunBuilder:
        """
        Creates a :py:class:`PLAS.RunBuilder`.  
        
        Signature ``CreateRunBuilder(run)`` 
        
        :param run:  :py:class:`PLAS.Run` to be edited, if None then create a new one  
        :type run: :py:class:`NXOpen.PLAS.Run` 
        :returns: 
        :rtype: :py:class:`NXOpen.PLAS.RunBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    ActiveRun: Run = ...
    """
    Returns or sets  the active run 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveRun`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.PLAS.Run` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveRun`` 
    
    :param run: 
    :type run: :py:class:`NXOpen.PLAS.Run` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """


class RunBuilder(NXOpen.Builder, NXOpen.IAttributeSourceObjectBuilder):
    """
    Represents a RunBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.PLAS.PlasManager.CreateRunBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    def GetLogicalObject(self) -> NXOpen.PDM.LogicalObject:
        """
        Gets the known logical object.  
        
        Signature ``GetLogicalObject()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.1
        
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
    
    IsUnassigned: bool = ...
    """
    Returns or sets  whether the run is unassigned 
    
    <hr>
    
    Getter Method
    
    Signature ``IsUnassigned`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUnassigned`` 
    
    :param isUnassigned: 
    :type isUnassigned: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LineTypePathId: str = ...
    """
    Returns or sets  the line type path ID of the run.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineTypePathId`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LineTypePathId`` 
    
    :param lineTypePathId: 
    :type lineTypePathId: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    ObjectApplication: str = ...
    """
    Returns or sets  the application name of the run.  
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectApplication`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ObjectApplication`` 
    
    :param objectApplication: 
    :type objectApplication: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    PipeSpecPathId: str = ...
    """
    Returns or sets  the pipe specification object of this run.  
    
    <hr>
    
    Getter Method
    
    Signature ``PipeSpecPathId`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PipeSpecPathId`` 
    
    :param pipeSpecPathId: 
    :type pipeSpecPathId: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: RunBuilder = ...  # unknown typename


