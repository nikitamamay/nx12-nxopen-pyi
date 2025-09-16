# module 'NXOpen.Features.ShipDesign.GeneralArrangement'
#
# Automatically generated 2025-06-09T14:38:46.458877
#

import typing

import NXOpen



class ProjectInitializationBuilder(NXOpen.Builder):
    """
    This class is used to Initialize general arrangement project.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.ShipCollection.CreateProjectInitializationBuilder`
    
    .. versionadded:: NX12.0.0
    """
    ProjectName: str = ...
    """
    Returns or sets  the project name 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectName`` 
    
    :param projectName: 
    :type projectName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: solid_modeling ("SOLIDS MODELING")
    """
    Null: ProjectInitializationBuilder = ...  # unknown typename


class FaceCharacteristicsBuilder(NXOpen.Builder):
    """
    Represents a builder to be used to add face characteristics attributes and color to specified faces.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.ShipCollection.CreateFaceCharacteristicsBuilder`
    
    .. versionadded:: NX12.0.0
    """
    CharacteristicColor: NXOpen.NXColor = ...
    """
    Returns or sets  the characteristic color to assign to the selected face.  
    
    <hr>
    
    Getter Method
    
    Signature ``CharacteristicColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CharacteristicColor`` 
    
    :param characteristicColor: 
    :type characteristicColor: Id 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    """
    CharacteristicValue: int = ...
    """
    Returns or sets  the characteristic value to assign to the selected face.  
    
    <hr>
    
    Getter Method
    
    Signature ``CharacteristicValue`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CharacteristicValue`` 
    
    :param characteristicValue: 
    :type characteristicValue: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_ship_gen_arrange ("Ship General Arrangement")
    """
    SelectFace: NXOpen.ScCollector = ...
    """
    Returns  the face to assign the specific characteristics.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: FaceCharacteristicsBuilder = ...  # unknown typename


