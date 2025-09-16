# module 'NXOpen.ModlDirect'
#
# Automatically generated 2025-06-09T14:38:47.049045
#
"""Default documentation for NXOpen.ModlDirect."""

import typing

import NXOpen
import NXOpen.GeometricUtilities



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class SelectBlend(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.ModlDirect.SelectBlend`
    Allows user to specify blend faces.  
    
    .. versionadded:: NX5.0.2
    """
    
    def RecognizeBlends(self, baseFaces: 'list[NXOpen.Face]') -> 'list[NXOpen.Face]':
        """
        Auto regonize the adjacent blends of input base faces 
        
        Signature ``RecognizeBlends(baseFaces)`` 
        
        :param baseFaces:  the base faces  
        :type baseFaces: list of :py:class:`NXOpen.Face` 
        :returns:  the adjacent blend faces  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
        """
        ...
    
    
    def IncludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
        Include the use selected blend face 
        
        Signature ``IncludeBlend(blendFace)`` 
        
        :param blendFace:  the blend face to include  
        :type blendFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
        """
        ...
    
    
    def ExcludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
        Exclude the user de-selected blend face 
        
        Signature ``ExcludeBlend(blendFace)`` 
        
        :param blendFace:  the blend face to exclude  
        :type blendFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
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
    
    FaceCollector: NXOpen.ScCollector = ...
    """
    Returns  the blend faces collector.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceCollector`` 
    
    :returns:  the blend face collector  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: None.
    """
    Null: SelectBlend = ...  # unknown typename


