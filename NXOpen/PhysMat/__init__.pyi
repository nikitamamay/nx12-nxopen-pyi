# module 'NXOpen.PhysMat'
#
# Automatically generated 2025-06-09T14:38:47.234733
#
"""Default documentation for NXOpen.PhysMat."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class PhysicalMaterialAssignBuilder(NXOpen.Builder):
    """
    Represents a Physical Material Assign Builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PhysicalMaterialCollection.CreateMaterialAssignBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: PhysicalMaterialAssignBuilder = ...  # unknown typename


class PhysicalMaterialLibMgrBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.PhysMat.PhysicalMaterialLibMgrBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.PhysicalMaterialCollection.CreateMaterialLibmgrBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: PhysicalMaterialLibMgrBuilder = ...  # unknown typename


class PhysicalMaterialListBuilder(NXOpen.Builder):
    """
    This builder is used by the Materials list component that allows copying, editing, deleting.  
    
    etc.
    materials.
    
    To create a new instance of this class, use :py:meth:`NXOpen.PhysicalMaterialCollection.CreateListBlockBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: PhysicalMaterialListBuilder = ...  # unknown typename


