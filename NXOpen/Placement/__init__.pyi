# module 'NXOpen.Placement'
#
# Automatically generated 2025-06-09T14:38:47.234733
#
"""Default documentation for NXOpen.Placement."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PlacementSolution(NXOpen.NXObject):
    """
    This class represents the placement solution
    
    Use :py:meth:`Placement.PlacementEngineBuilder.ComputePlacementSolutions` to get the instance of this class.
    
    .. versionadded:: NX11.0.0
    """
    Null: PlacementSolution = ...  # unknown typename


class PlacementEngineBuilder(NXOpen.Builder):
    """
    Represents a builder class that will create and work with placement solutions.  
    
    An instance of this class can be obtained from :py:meth:`NXOpen.MechanicalRouting.PartPlacementBuilder.InitializePlacementEngineBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def ComputePlacementSolutions(self) -> 'list[PlacementSolution]':
        """
        Computes and returns the placement solutions
        
        Signature ``ComputePlacementSolutions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Placement.PlacementSolution` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFilteredPlacementSolutions(self, placementSolutions: 'list[PlacementSolution]') -> None:
        """
        Sets the input PlacementSolutions as the filtered solutions on the PlacementEngineBuilder in the given order.  
        
        Different clients can have their own methodology for filtering the solutions 
        e.g. Part Placement can decide to filter out solutions based on a particular port on the input placeable object.
        
        Signature ``SetFilteredPlacementSolutions(placementSolutions)`` 
        
        :param placementSolutions: 
        :type placementSolutions: list of :py:class:`NXOpen.Placement.PlacementSolution` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ApplyPlacementSolution(self, placementSolution: PlacementSolution) -> None:
        """
        Sets the transform on part being placed using the supplied placement solution.  
        
        Signature ``ApplyPlacementSolution(placementSolution)`` 
        
        :param placementSolution: 
        :type placementSolution: :py:class:`NXOpen.Placement.PlacementSolution` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PlacementEngineBuilder = ...  # unknown typename


