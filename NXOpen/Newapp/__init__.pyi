# module 'NXOpen.Newapp'
#
# Automatically generated 2025-06-09T14:38:47.187736
#
"""Default documentation for NXOpen.Newapp."""

import typing

import NXOpen
import NXOpen.Features



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ApplicationManager():
    """
    Represents the Application Manager class.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX9.0.0
    """
    
    def CreateTestFeatureBuilder(self, part: NXOpen.Part, feat: NXOpen.Features.TestFeature) -> NXOpen.Features.TestFeatureBuilder:
        """
        Creates a Newapp.  
        
        TestFeature feature  
        
        Signature ``CreateTestFeatureBuilder(part, feat)`` 
        
        :param part:  the part that will own the feature  
        :type part: :py:class:`NXOpen.Part` 
        :param feat: 
        :type feat: :py:class:`NXOpen.Features.TestFeature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.TestFeatureBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @staticmethod
    def GetApplicationManager():
        ...
    


