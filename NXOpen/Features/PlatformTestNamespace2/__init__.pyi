# module 'NXOpen.Features.PlatformTestNamespace2'
#
# Automatically generated 2025-06-09T14:38:46.474612
#

import typing

import NXOpen.Features



class TestBlock(NXOpen.Features.BodyFeature):
    """
    Represents a testblock feature in PlatformTestNamespace1 namespace .  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Features.PlatformTestNamespace2.TestBlockFeatureBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: TestBlock = ...  # unknown typename


class TestBlockFeatureBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a sheetmetal block feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.NXPlatformTestSession.CreateFeaturesTestBlockFeatureBuilder2`
    
    .. versionadded:: NX8.5.0
    """
    DoubleField: float = ...
    """
    Returns or sets  the double value stored in the feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``DoubleField`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DoubleField`` 
    
    :param doubleField: 
    :type doubleField: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    StringField: str = ...
    """
    Returns or sets  the string value stored in the feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``StringField`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StringField`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: TestBlockFeatureBuilder = ...  # unknown typename


