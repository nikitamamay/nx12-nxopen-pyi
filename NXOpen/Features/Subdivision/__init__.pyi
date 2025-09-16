# module 'NXOpen.Features.Subdivision'
#
# Automatically generated 2025-06-09T14:38:46.474612
#

import typing

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities



class SubdivisionSweepBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionSweepBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionSweepBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionSweepBuilderContinuityTypeMemberType
    
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
    


class SubdivisionSweepBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSweepBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSweepBuilder`
    
    Default values.
    
    ========  =====
    Property  Value
    ========  =====
    CanSew    1 
    ========  =====
    
    .. versionadded:: NX10.0.0
    """
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionSweepBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionSweepBuilderContinuityTypeMemberType
        
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
        
    
    CanSew: bool = ...
    """
    Returns or sets  the value indicating if open edges of the swept mesh can be sewn with selected input open edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanSew`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanSew`` 
    
    :param canSew: 
    :type canSew: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Continuity: SubdivisionSweepBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to edges
    of the swept region that are sewn with the primary existing region. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSweepBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionSweepBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Guides: CageSectionDataList = ...
    """
    Returns  the guide objects.  
    
    <hr>
    
    Getter Method
    
    Signature ``Guides`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.CageSectionDataList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Sections: CageSectionDataList = ...
    """
    Returns  the section objects.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sections`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.CageSectionDataList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionSweepBuilder = ...  # unknown typename


class SubdivisionSplitFaceBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionSplitFaceBuilderTypes():
    """
    Represents the split type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "Uniform split type."
       "ThroughLines", "Through lines split type."
    """
    Uniform = 0  # SubdivisionSplitFaceBuilderTypesMemberType
    ThroughLines = 1  # SubdivisionSplitFaceBuilderTypesMemberType
    
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
    


class SubdivisionSplitFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSplitFaceBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class Types():
        """
        Represents the split type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "Uniform split type."
           "ThroughLines", "Through lines split type."
        """
        Uniform = 0  # SubdivisionSplitFaceBuilderTypesMemberType
        ThroughLines = 1  # SubdivisionSplitFaceBuilderTypesMemberType
        
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
        
    
    
    def AddSplitPoint(self, location: NXOpen.Point3d, object: NXOpen.DisplayableObject) -> None:
        """
        Add split face point.  
        
        Signature ``AddSplitPoint(location, object)`` 
        
        :param location:  the loction on the object to split face.  
        :type location: :py:class:`NXOpen.Point3d` 
        :param object:  the selected subdivision edge or vertex to split face.  
        :type object: :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def ClearSplitPoints(self) -> None:
        """
        Clear split face point.  
        
        Signature ``ClearSplitPoints()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def UpdateSplitPositions(self, splitLineIndex: int, positions: 'list[NXOpen.Point3d]') -> None:
        """
        Update split positions.  
        
        Signature ``UpdateSplitPositions(splitLineIndex, positions)`` 
        
        :param splitLineIndex:  index to indicate which split line to update positions from.  
        :type splitLineIndex: int 
        :param positions:  the point positions.  
        :type positions: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    FacesToSplit: SelectCageObjectData = ...
    """
    Returns  the faces to split.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacesToSplit`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Number: int = ...
    """
    Returns or sets  the desired split number in one face.  
    
    <hr>
    
    Getter Method
    
    Signature ``Number`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Number`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ReferenceEdge: SelectCageObjectData = ...
    """
    Returns  the reference edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Type: SubdivisionSplitFaceBuilderTypes = ...
    """
    Returns or sets  the split type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionSplitFaceBuilder = ...  # unknown typename


class SubdivisionPrimitiveShapeBuilderExTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionPrimitiveShapeBuilderExTypes():
    """
    Type of primitive. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sphere", " - "
       "Cylinder", " - "
       "Block", " - "
       "Circle", " - "
       "Rectangle", " - "
       "Torus", " - "
    """
    Sphere = 0  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    Cylinder = 1  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    Block = 2  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    Circle = 3  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    Rectangle = 4  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    Torus = 5  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
    
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
    


class SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel():
    """
    Level of subdivisions of cubical cage to construct spherical primitive. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Base", " - "
       "First", " - "
       "Second", " - "
    """
    Base = 0  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
    First = 1  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
    Second = 2  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
    
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
    


class SubdivisionPrimitiveShapeBuilderEx(NXOpen.Builder):
    """
    Represents a :py:class:`Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionPrimitiveShapeBuilderEx`
    
    Default values.
    
    =================  ========================================
    Property           Value
    =================  ========================================
    CircularSegments   4 
    -----------------  ----------------------------------------
    Height.Value       100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    HeightZ.Value      100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    InnerSize.Value    50 (millimeters part), 2 (inches part) 
    -----------------  ----------------------------------------
    LengthX.Value      100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    LinearSegments     1 
    -----------------  ----------------------------------------
    OuterSize.Value    100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    RadialSegments     8 
    -----------------  ----------------------------------------
    Size.Value         100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    WidthY.Value       100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    XSegments          1 
    -----------------  ----------------------------------------
    YSegments          1 
    -----------------  ----------------------------------------
    ZSegments          1 
    =================  ========================================
    
    .. versionadded:: NX11.0.0
    """
    
    class Types():
        """
        Type of primitive. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sphere", " - "
           "Cylinder", " - "
           "Block", " - "
           "Circle", " - "
           "Rectangle", " - "
           "Torus", " - "
        """
        Sphere = 0  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        Cylinder = 1  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        Block = 2  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        Circle = 3  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        Rectangle = 4  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        Torus = 5  # SubdivisionPrimitiveShapeBuilderExTypesMemberType
        
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
        
    
    
    class SphereSubdivisionLevel():
        """
        Level of subdivisions of cubical cage to construct spherical primitive. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Base", " - "
           "First", " - "
           "Second", " - "
        """
        Base = 0  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
        First = 1  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
        Second = 2  # SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevelMemberType
        
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
        
    
    
    def UpdateMesh(self) -> None:
        """
        Updates the mesh data after changes in the origin.  
        
        Signature ``UpdateMesh()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    CircularSegments: int = ...
    """
    Returns or sets  the number of segments in circular direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``CircularSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CircularSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height.  
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    HeightZ: NXOpen.Expression = ...
    """
    Returns  the height in Z direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``HeightZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    InnerSize: NXOpen.Expression = ...
    """
    Returns  the inner size of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``InnerSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LengthX: NXOpen.Expression = ...
    """
    Returns  the length in X direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``LengthX`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LinearSegments: int = ...
    """
    Returns or sets  the number of segments in linear direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``LinearSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LinearSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Origin: NXOpen.Point = ...
    """
    Returns or sets  the origin.  
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    OuterSize: NXOpen.Expression = ...
    """
    Returns  the outer size of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``OuterSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    RadialSegments: int = ...
    """
    Returns or sets  the number of segments in radial direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``RadialSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RadialSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Size: NXOpen.Expression = ...
    """
    Returns  the size.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    SphereSubdivisionLevelOption: SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel = ...
    """
    Returns or sets  the subdivision level.  
    
    <hr>
    
    Getter Method
    
    Signature ``SphereSubdivisionLevelOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SphereSubdivisionLevelOption`` 
    
    :param level: 
    :type level: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExSphereSubdivisionLevel` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Type: SubdivisionPrimitiveShapeBuilderExTypes = ...
    """
    Returns or sets  the type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderExTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    WidthY: NXOpen.Expression = ...
    """
    Returns  the width in Y direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``WidthY`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    XSegments: int = ...
    """
    Returns or sets  the number of segments in X direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``XSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    YSegments: int = ...
    """
    Returns or sets  the number of segments in Y direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``YSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ZSegments: int = ...
    """
    Returns or sets  the number of segments in Z direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``ZSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionPrimitiveShapeBuilderEx = ...  # unknown typename


class CageSectionData(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents subdivision cage section selection.  
    
    .. versionadded:: NX10.0.0
    """
    
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
    
    CanReverseDirection: bool = ...
    """
    Returns or sets  the flag indicating if section direction is reversed.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanReverseDirection`` 
    
    :param reverse: 
    :type reverse: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SelectionObject: SelectCageObjectData = ...
    """
    Returns  the selection object.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CageSectionData = ...  # unknown typename


class MirrorCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.MirrorCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateMirrorCageBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def UpdateOnMirrorPlane(self) -> None:
        """
        Updates the builder based on changes in the mirror plane.  
        
        Signature ``UpdateOnMirrorPlane()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    MirrorPlane: NXOpen.Plane = ...
    """
    Returns or sets  the mirror plane 
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorPlane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Objects: SelectCageObjectData = ...
    """
    Returns  the objects to be mirrored 
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: MirrorCageBuilder = ...  # unknown typename


class PasteCageData(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.PasteCageData` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreatePasteCageData`
    
    .. versionadded:: NX11.0.0
    """
    CanMoveToolOnly: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :param canMove: 
    :type canMove: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    The tool allows user to transform the pasted topology. 
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: PasteCageData = ...  # unknown typename


class SubdivisionSetWeightBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSetWeightBuilder`
    
    Default values.
    
    ==============  =====
    Property        Value
    ==============  =====
    WeightPercent   0 
    ==============  =====
    
    .. versionadded:: NX9.0.0
    """
    TargetObject: SelectCageObjectData = ...
    """
    Returns  the target object.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    WeightPercent: int = ...
    """
    Returns or sets  the value indicating percentage weight.  
    
    Weight defines attraction of the limit surface towards cage topology. 
    
    <hr>
    
    Getter Method
    
    Signature ``WeightPercent`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeightPercent`` 
    
    :param weightPercent: 
    :type weightPercent: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionSetWeightBuilder = ...  # unknown typename


class CagePolylineBuilder(NXOpen.Features.PolylineBuilder):
    """
    Cage polyline builder class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateCagePolylineBuilder`
    
    Default values.
    
    ===================  =====
    Property             Value
    ===================  =====
    DrawingPlaneOption   View 
    -------------------  -----
    MovementMethod       View 
    -------------------  -----
    WCSOption            X 
    ===================  =====
    
    .. versionadded:: NX10.0.0
    """
    Null: CagePolylineBuilder = ...  # unknown typename


class OffsetCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.OffsetCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateOffsetCageBuilder`
    
    Default values.
    
    =====================  ===========================================
    Property               Value
    =====================  ===========================================
    NumberOfCopies         1 
    ---------------------  -------------------------------------------
    OffsetDistance.Value   10.0 (millimeters part), 0.5 (inches part) 
    =====================  ===========================================
    
    .. versionadded:: NX11.0.0
    """
    CanReverseOffsetDirection: bool = ...
    """
    Returns or sets  the flag indicating if offset direction can be reversed.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanReverseOffsetDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanReverseOffsetDirection`` 
    
    :param reverse: 
    :type reverse: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    NumberOfCopies: int = ...
    """
    Returns or sets  the number of copies to offset 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfCopies`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfCopies`` 
    
    :param numberOfCopies: 
    :type numberOfCopies: int 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Objects: SelectCageObjectData = ...
    """
    Returns  the objects to be offset 
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    OffsetDistance: NXOpen.Expression = ...
    """
    Returns  the offset distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: OffsetCageBuilder = ...  # unknown typename


class SplitSubdivisionBodyBuilderInputBodyOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SplitSubdivisionBodyBuilderInputBodyOptions():
    """
    Options indicating actions to be taken on input :py:class:`Features.Subdivision.SubdivisionBody` features 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep the feature as they are"
       "Hide", "Hide the features"
       "Delete", "Delete the features"
    """
    Keep = 0  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
    Hide = 1  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
    Delete = 2  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
    
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
    


class SplitSubdivisionBodyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Features.Subdivision.SplitSubdivisionBodyBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSplitSubdivisionBodyBuilder`
    
    Default values.
    
    ================  =======
    Property          Value
    ================  =======
    InputBodyOption   Delete 
    ================  =======
    
    .. versionadded:: NX11.0.0
    """
    
    class InputBodyOptions():
        """
        Options indicating actions to be taken on input :py:class:`Features.Subdivision.SubdivisionBody` features 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep the feature as they are"
           "Hide", "Hide the features"
           "Delete", "Delete the features"
        """
        Keep = 0  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
        Hide = 1  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
        Delete = 2  # SplitSubdivisionBodyBuilderInputBodyOptionsMemberType
        
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
        
    
    InputBodyOption: SplitSubdivisionBodyBuilderInputBodyOptions = ...
    """
    Returns or sets  the input body option 
    
    <hr>
    
    Getter Method
    
    Signature ``InputBodyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilderInputBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputBodyOption`` 
    
    :param inputBody: 
    :type inputBody: :py:class:`NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilderInputBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SubdivisionBodiesToSplit: SelectSubdivisionBodyList = ...
    """
    Returns  the :py:class:`Features.Subdivision.SubdivisionBody` features to split 
    
    <hr>
    
    Getter Method
    
    Signature ``SubdivisionBodiesToSplit`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectSubdivisionBodyList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: SplitSubdivisionBodyBuilder = ...  # unknown typename


class CageSectionDataList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[CageSectionData]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: CageSectionData) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
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
    
    
    def FindIndex(self, obj: CageSectionData) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> CageSectionData:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
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
    def Erase(self, obj: CageSectionData) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: CageSectionData, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
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
    
    
    def GetContents(self) -> 'list[CageSectionData]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[CageSectionData]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
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
    def Swap(self, object1: CageSectionData, object2: CageSectionData) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: CageSectionData) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
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
    Null: CageSectionDataList = ...  # unknown typename


class ExportSubdivisionGeometryBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateExportSubdivisionGeometryBuilder`
    
    .. versionadded:: NX11.0.0
    """
    FeatureSet: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the Feature to export 
    
    <hr>
    
    Getter Method
    
    Signature ``FeatureSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    FileName: str = ...
    """
    Returns or sets  the file name.  
    
    The export file will only store the topology and geometry positions of the Subdivision Cage, and 
    not contains auxiliary data of the Subdivision feature, such as the weights, sharpness and constraints.
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: ExportSubdivisionGeometryBuilder = ...  # unknown typename


class SubdivisionRevolveBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionRevolveBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionRevolveBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionRevolveBuilderContinuityTypeMemberType
    
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
    


class SubdivisionRevolveBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionRevolveBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionRevolveBuilder`
    
    Default values.
    
    =================  =====
    Property           Value
    =================  =====
    CanSew             1 
    -----------------  -----
    EndAngle.Value     360 
    -----------------  -----
    NumOfSegments      8 
    -----------------  -----
    StartAngle.Value   0 
    =================  =====
    
    .. versionadded:: NX10.0.0
    """
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionRevolveBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionRevolveBuilderContinuityTypeMemberType
        
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
        
    
    AxisPoint: NXOpen.SelectNXObject = ...
    """
    Returns  the origin of the axis of revolution.  
    
    <hr>
    
    Getter Method
    
    Signature ``AxisPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    AxisVector: NXOpen.Direction = ...
    """
    Returns or sets  the axis of revolution.  
    
    <hr>
    
    Getter Method
    
    Signature ``AxisVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AxisVector`` 
    
    :param axisVector: 
    :type axisVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanSew: bool = ...
    """
    Returns or sets  the value indicating if open edges of the revolve mesh can be sewn with selected input open edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanSew`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanSew`` 
    
    :param canSew: 
    :type canSew: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Continuity: SubdivisionRevolveBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to edges
    of the revolved region that are sewn with the primary existing region. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionRevolveBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionRevolveBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    EndAngle: NXOpen.Expression = ...
    """
    Returns  the end of angular dimension.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    NumOfSegments: int = ...
    """
    Returns or sets  the number of segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumOfSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumOfSegments`` 
    
    :param numOfSegments: 
    :type numOfSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SectionObject: SelectCageObjectData = ...
    """
    Returns  the section as revolving profile.  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    StartAngle: NXOpen.Expression = ...
    """
    Returns  the start of angular dimension.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionRevolveBuilder = ...  # unknown typename


class CageManipulatorDataObjectSelectionData_Struct():
    """
    Contains object selection information.  
    
    .. versionadded:: NX9.0.0
    
    .
    Constructor: 
    NXOpen.Features.Subdivision.CageManipulatorData.ObjectSelectionData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    SelectedObject: NXOpen.NXObject = ...
    """
    The selected object.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    SelectionPosition: NXOpen.Point3d = ...
    """
    The point at which object is selected, the point
    under the cursor when seen in view direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    ViewDirection: NXOpen.Vector3d = ...
    """
    The view direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    IsSnappedPosition: bool = ...
    """
    Is SelectionPosition a snapped location.  
    
    <hr>
    
    Field Value
    Type:bool
    """


class SubdivisionDeleteObjectBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Features.Subdivision.SubdivisionDeleteObjectBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteObjectBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Objects: SelectCageObjectData = ...
    """
    Returns  the objects to be deleted.  
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: SubdivisionDeleteObjectBuilder = ...  # unknown typename


class StartSymmetricModelingBuilderMirrorProcedureOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class StartSymmetricModelingBuilderMirrorProcedureOption():
    """
    The options used to establish symmetric model   
    
    .. deprecated::  NX10.0.0
       This enumeration is redundent and hence not necessary.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CutBody", "Cuts the mesh"
       "ProjectEdge", "Projects the edges"
    """
    CutBody = 0  # StartSymmetricModelingBuilderMirrorProcedureOptionMemberType
    ProjectEdge = 1  # StartSymmetricModelingBuilderMirrorProcedureOptionMemberType
    
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
    


class StartSymmetricModelingBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.StartSymmetricModelingBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateStartSymmetricModelingBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class MirrorProcedureOption():
        """
        The options used to establish symmetric model   
        
        .. deprecated::  NX10.0.0
           This enumeration is redundent and hence not necessary.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CutBody", "Cuts the mesh"
           "ProjectEdge", "Projects the edges"
        """
        CutBody = 0  # StartSymmetricModelingBuilderMirrorProcedureOptionMemberType
        ProjectEdge = 1  # StartSymmetricModelingBuilderMirrorProcedureOptionMemberType
        
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
        
    
    EdgesToProject: SelectCageObjectData = ...
    """
    Returns  the edges to project 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgesToProject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    MirrorProcedureOptions: StartSymmetricModelingBuilderMirrorProcedureOption = ...
    """
    Returns or sets  the mirror procedure options 
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorProcedureOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.StartSymmetricModelingBuilderMirrorProcedureOption` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       This property is redundent and hence not necessary.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorProcedureOptions`` 
    
    :param mirrorProcedureOptions: 
    :type mirrorProcedureOptions: :py:class:`NXOpen.Features.Subdivision.StartSymmetricModelingBuilderMirrorProcedureOption` 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       This property is redundent and hence not necessary.
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SwitchSide: bool = ...
    """
    Returns or sets  the flag indicating if the mirror side should be switched 
    
    <hr>
    
    Getter Method
    
    Signature ``SwitchSide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SwitchSide`` 
    
    :param switchSide: 
    :type switchSide: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: StartSymmetricModelingBuilder = ...  # unknown typename


class SubdivisionExtrudeCageBuilderTransformationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionExtrudeCageBuilderTransformationMethodType():
    """
    Transformation method types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DragLinear", "Drag extruded topology in linear direction"
       "Transform", "Transform extruded topology"
    """
    DragLinear = 0  # SubdivisionExtrudeCageBuilderTransformationMethodTypeMemberType
    Transform = 1  # SubdivisionExtrudeCageBuilderTransformationMethodTypeMemberType
    
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
    


class SubdivisionExtrudeCageBuilderDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionExtrudeCageBuilderDirectionType():
    """
    Represents the extrude direction. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inferred", " - "
       "Vector", " - "
       "Perpendicular", " - "
    """
    Inferred = 0  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
    Vector = 1  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
    Perpendicular = 2  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
    
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
    


class SubdivisionExtrudeCageBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionExtrudeCageBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionExtrudeCageBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionExtrudeCageBuilderContinuityTypeMemberType
    
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
    


class SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionExtrudeCageBuilderScalingMethodType():
    """
    Scaling method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Scale in the specified direction"
       "Planar", "Scale in the plane normal to specified direction"
       "Uniform", "Scale uniformly all the directions"
    """
    Linear = 0  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
    Planar = 1  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
    Uniform = 2  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
    
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
    


class SubdivisionExtrudeCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionExtrudeCageBuilder`
    
    Default values.
    
    ===========================  =====
    Property                     Value
    ===========================  =====
    CanRelocateToolToSelection   true 
    ---------------------------  -----
    CanReorientToolToSelection   true 
    ---------------------------  -----
    NumberOfSegments             1 
    ===========================  =====
    
    .. versionadded:: NX9.0.0
    """
    
    class TransformationMethodType():
        """
        Transformation method types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DragLinear", "Drag extruded topology in linear direction"
           "Transform", "Transform extruded topology"
        """
        DragLinear = 0  # SubdivisionExtrudeCageBuilderTransformationMethodTypeMemberType
        Transform = 1  # SubdivisionExtrudeCageBuilderTransformationMethodTypeMemberType
        
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
        
    
    
    class DirectionType():
        """
        Represents the extrude direction. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inferred", " - "
           "Vector", " - "
           "Perpendicular", " - "
        """
        Inferred = 0  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
        Vector = 1  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
        Perpendicular = 2  # SubdivisionExtrudeCageBuilderDirectionTypeMemberType
        
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
        
    
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionExtrudeCageBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionExtrudeCageBuilderContinuityTypeMemberType
        
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
        
    
    
    class ScalingMethodType():
        """
        Scaling method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Scale in the specified direction"
           "Planar", "Scale in the plane normal to specified direction"
           "Uniform", "Scale uniformly all the directions"
        """
        Linear = 0  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
        Planar = 1  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
        Uniform = 2  # SubdivisionExtrudeCageBuilderScalingMethodTypeMemberType
        
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
        
    
    
    def Extrude(self) -> None:
        """
        Perform extrude operation.  
        
        Signature ``Extrude()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    CanMoveToolOnly: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :param canMove: 
    :type canMove: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanRelocateToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be relocated based on cage topology selection.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :param canRelocate: 
    :type canRelocate: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanReorientToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :param canReorient: 
    :type canReorient: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Continuity: SubdivisionExtrudeCageBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to the outer
    edges of the faces or boundary edges specified by :py:meth:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder.SelectionObject`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    DirectionOption: SubdivisionExtrudeCageBuilderDirectionType = ...
    """
    Returns or sets  the direction option 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderDirectionType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionOption`` 
    
    :param directionOption: 
    :type directionOption: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderDirectionType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Distance: NXOpen.Expression = ...
    """
    Returns  the distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NumberOfSegments: int = ...
    """
    Returns or sets  the number of segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfSegments`` 
    
    :param numOfSegments: 
    :type numOfSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ScalingMethod: SubdivisionExtrudeCageBuilderScalingMethodType = ...
    """
    Returns or sets  the scaling method.  
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderScalingMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingMethod`` 
    
    :param scalingMethod: 
    :type scalingMethod: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderScalingMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SelectionObject: SelectCageObjectData = ...
    """
    Returns  the selection object.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TransformationMethod: SubdivisionExtrudeCageBuilderTransformationMethodType = ...
    """
    Returns or sets  the transformation method.  
    
    <hr>
    
    Getter Method
    
    Signature ``TransformationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderTransformationMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransformationMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilderTransformationMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector for extrude.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionExtrudeCageBuilder = ...  # unknown typename


class ImportSubdivisionGeometryBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateImportSubdivisionGeometryBuilder`
    
    .. versionadded:: NX10.0.0
    """
    CanCreateSingleFeature: bool = ...
    """
    Returns or sets  the flag indicating if single feature should be created for all the disjoint regions of the subdivision geometry.  
    
    When false, separate feature will be created for each disjoint region. 
    
    <hr>
    
    Getter Method
    
    Signature ``CanCreateSingleFeature`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanCreateSingleFeature`` 
    
    :param canCreateSingleFeature: 
    :type canCreateSingleFeature: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FileName: str = ...
    """
    Returns or sets  the file name.  
    
    Expects a file in standard ASCII Wavefront OBJ format used for base mesh definition of a subdivision geometry. 
    Usage of OBJ files representing triangulated polygon mesh, similar to ones used for graphical rendering or higher resolution
    subdivision mesh is not recommended to be used. The solid model created from such mesh will have
    excessive amount of topology and the import operation will be inefficient.
    
    <hr>
    
    Getter Method
    
    Signature ``FileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FileName`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: ImportSubdivisionGeometryBuilder = ...  # unknown typename


class SubdivisionTubeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionTubeBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionTubeBuilder`
    
    Default values.
    
    =================  =======================================
    Property           Value
    =================  =======================================
    NumberOfSegments   4 
    -----------------  ---------------------------------------
    Size.Value         50 (millimeters part), 2 (inches part) 
    =================  =======================================
    
    .. versionadded:: NX10.0.0
    """
    NumberOfSegments: int = ...
    """
    Returns or sets  the number of segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfSegments`` 
    
    :param numberOfSegments: 
    :type numberOfSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    PathObject: SelectCageObjectData = ...
    """
    Returns  the object as path of tube.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Size: NXOpen.Expression = ...
    """
    Returns  the size of tube in cross section.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionTubeBuilder = ...  # unknown typename


class MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MergeSubdivisionBodiesBuilderInputBodyOptions():
    """
    Options indicating actions to be taken on input :py:class:`Features.Subdivision.SubdivisionBody` features 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep the features as they are"
       "Hide", "Hide the features"
       "Delete", "Delete the features"
    """
    Keep = 0  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
    Hide = 1  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
    Delete = 2  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
    
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
    


class MergeSubdivisionBodiesBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Features.Subdivision.MergeSubdivisionBodiesBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateMergeSubdivisionBodiesBuilder`
    
    Default values.
    
    ================  =======
    Property          Value
    ================  =======
    InputBodyOption   Delete 
    ================  =======
    
    .. versionadded:: NX11.0.0
    """
    
    class InputBodyOptions():
        """
        Options indicating actions to be taken on input :py:class:`Features.Subdivision.SubdivisionBody` features 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep the features as they are"
           "Hide", "Hide the features"
           "Delete", "Delete the features"
        """
        Keep = 0  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
        Hide = 1  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
        Delete = 2  # MergeSubdivisionBodiesBuilderInputBodyOptionsMemberType
        
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
        
    
    InputBodyOption: MergeSubdivisionBodiesBuilderInputBodyOptions = ...
    """
    Returns or sets  the input body option 
    
    <hr>
    
    Getter Method
    
    Signature ``InputBodyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilderInputBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputBodyOption`` 
    
    :param inputBody: 
    :type inputBody: :py:class:`NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilderInputBodyOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SubdivisionBodiesToMerge: SelectSubdivisionBodyList = ...
    """
    Returns  the :py:class:`Features.Subdivision.SubdivisionBody` features to merge 
    
    <hr>
    
    Getter Method
    
    Signature ``SubdivisionBodiesToMerge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectSubdivisionBodyList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: MergeSubdivisionBodiesBuilder = ...  # unknown typename


class SubdivisionSewCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSewCageBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSewCageBuilder`
    
    .. versionadded:: NX10.0.0
    """
    SelectedEdges1: SelectCageObjectData = ...
    """
    Returns  the first set of edges 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedEdges1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SelectedEdges2: SelectCageObjectData = ...
    """
    Returns  the second set of edges 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedEdges2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionSewCageBuilder = ...  # unknown typename


class SubdivisionBodyCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of subdivision body feature tools.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX9.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateSubdivisionPrimitiveShapeBuilder(self) -> SubdivisionPrimitiveShapeBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder`.  
        
        Signature ``CreateSubdivisionPrimitiveShapeBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionPrimitiveShapeBuilderEx` instead
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionPrimitiveShapeBuilderEx(self) -> SubdivisionPrimitiveShapeBuilderEx:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx`.  
        
        Signature ``CreateSubdivisionPrimitiveShapeBuilderEx()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionExtrudeCageBuilder(self) -> SubdivisionExtrudeCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder`.  
        
        Signature ``CreateSubdivisionExtrudeCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionExtrudeCageBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSetWeightBuilder(self) -> SubdivisionSetWeightBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder`.  
        
        Signature ``CreateSubdivisionSetWeightBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSetWeightBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSetContinuityBuilder(self) -> SubdivisionSetContinuityBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder`.  
        
        Signature ``CreateSubdivisionSetContinuityBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionDeleteFaceBuilder(self) -> SubdivisionDeleteFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder`.  
        
        Signature ``CreateSubdivisionDeleteFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder` 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteCageBuilder` instead.
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateTransformCageData(self) -> TransformCageData:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.TransformCageData`.  
        
        Signature ``CreateTransformCageData()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageData` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionFillBuilder(self) -> SubdivisionFillBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionFillBuilder`.  
        
        Signature ``CreateSubdivisionFillBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionFillBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionBridgeFaceBuilder(self) -> SubdivisionBridgeFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder`.  
        
        Signature ``CreateSubdivisionBridgeFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateStartSymmetricModelingBuilder(self) -> StartSymmetricModelingBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.StartSymmetricModelingBuilder`.  
        
        Signature ``CreateStartSymmetricModelingBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.StartSymmetricModelingBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def StopSymmetricModeling(self) -> None:
        """
        Stops the symmetric modeling.  
        
        Signature ``StopSymmetricModeling()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionProjectCageBuilder(self) -> SubdivisionProjectCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder`.  
        
        Signature ``CreateSubdivisionProjectCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionMergeFaceBuilder(self) -> SubdivisionMergeFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder`.  
        
        Signature ``CreateSubdivisionMergeFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSplitFaceBuilder(self) -> SubdivisionSplitFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder`.  
        
        Signature ``CreateSubdivisionSplitFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSplitFaceBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSubdivideFaceBuilder(self) -> SubdivisionSubdivideFaceBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder`.  
        
        Signature ``CreateSubdivisionSubdivideFaceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateImportSubdivisionGeometryBuilder(self) -> ImportSubdivisionGeometryBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder`.  
        
        Signature ``CreateImportSubdivisionGeometryBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.ImportSubdivisionGeometryBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateCagePolylineBuilder(self, polyline: NXOpen.Polyline) -> CagePolylineBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.CagePolylineBuilder`.  
        
        Signature ``CreateCagePolylineBuilder(polyline)`` 
        
        :param polyline:  :py:class:`NXOpen.Polyline` 
        :type polyline: :py:class:`NXOpen.Polyline` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.CagePolylineBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateExtractCagePolylineBuilder(self) -> ExtractCagePolylineBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.ExtractCagePolylineBuilder`.  
        
        Signature ``CreateExtractCagePolylineBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.ExtractCagePolylineBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionRevolveBuilder(self) -> SubdivisionRevolveBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionRevolveBuilder`.  
        
        Signature ``CreateSubdivisionRevolveBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionRevolveBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionTubeBuilder(self) -> SubdivisionTubeBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionTubeBuilder`.  
        
        Signature ``CreateSubdivisionTubeBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionTubeBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateCopyCageBuilder(self) -> CopyCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.CopyCageBuilder`.  
        
        Signature ``CreateCopyCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.CopyCageBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateEmptyCageSectionBuilder(self) -> CageSectionData:
        """
        Creates an empty cage section builder object.  
        
        Signature ``CreateEmptyCageSectionBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.CageSectionData` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionLoftBuilder(self) -> SubdivisionLoftBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionLoftBuilder`.  
        
        Signature ``CreateSubdivisionLoftBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionLoftBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSweepBuilder(self) -> SubdivisionSweepBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSweepBuilder`.  
        
        Signature ``CreateSubdivisionSweepBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSweepBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionSewCageBuilder(self) -> SubdivisionSewCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionSewCageBuilder`.  
        
        Signature ``CreateSubdivisionSewCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSewCageBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionDeleteCageBuilder(self) -> SubdivisionDeleteCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder`.  
        
        Signature ``CreateSubdivisionDeleteCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder` 
        
        .. versionadded:: NX10.0.0
        
        .. deprecated::  NX11.0.0
           Use :py:meth:`Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteObjectBuilder` instead.
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSplitSubdivisionBodyBuilder(self) -> SplitSubdivisionBodyBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder`.  
        
        Signature ``CreateSplitSubdivisionBodyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SplitSubdivisionBodyBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateMergeSubdivisionBodiesBuilder(self) -> MergeSubdivisionBodiesBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder`.  
        
        Signature ``CreateMergeSubdivisionBodiesBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.MergeSubdivisionBodiesBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateCopyCageData(self) -> CopyCageData:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.CopyCageData`.  
        
        Signature ``CreateCopyCageData()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.CopyCageData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreatePasteCageData(self) -> PasteCageData:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.PasteCageData`.  
        
        Signature ``CreatePasteCageData()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.PasteCageData` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateDefineWorkRegionBuilder(self) -> DefineWorkRegionBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilder`.  
        
        Signature ``CreateDefineWorkRegionBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateMirrorCageBuilder(self) -> MirrorCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.MirrorCageBuilder`.  
        
        Signature ``CreateMirrorCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.MirrorCageBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateOffsetCageBuilder(self) -> OffsetCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.OffsetCageBuilder`.  
        
        Signature ``CreateOffsetCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.OffsetCageBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionDeleteObjectBuilder(self) -> SubdivisionDeleteObjectBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder`.  
        
        Signature ``CreateSubdivisionDeleteObjectBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateDeleteConstraintBuilder(self) -> DeleteConstraintBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.DeleteConstraintBuilder`.  
        
        Signature ``CreateDeleteConstraintBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.DeleteConstraintBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateSubdivisionConnectCageBuilder(self) -> SubdivisionConnectCageBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder`.  
        
        Signature ``CreateSubdivisionConnectCageBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def CreateExportSubdivisionGeometryBuilder(self) -> ExportSubdivisionGeometryBuilder:
        """
        Creates a :py:class:`NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder`.  
        
        Signature ``CreateExportSubdivisionGeometryBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Subdivision.ExportSubdivisionGeometryBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    


class TransformCageDataTransformationMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformCageDataTransformationMethodType():
    """
    Transformation method types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Drag", "Edit cage topology by direct dragging"
       "Transform", "Edit cage topology by transformations"
    """
    Drag = 0  # TransformCageDataTransformationMethodTypeMemberType
    Transform = 1  # TransformCageDataTransformationMethodTypeMemberType
    
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
    


class TransformCageDataMovementMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformCageDataMovementMethodType():
    """
    Movement types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WCS", "Movement along WCS principal axis or plane"
       "View", "Movement in view plane"
       "Vector", "Movement along arbitrary direction"
       "Plane", "Movement in arbitrary plane"
       "Normal", "Movement along a face normal"
       "Edge", "Movement along an edge"
    """
    WCS = 0  # TransformCageDataMovementMethodTypeMemberType
    View = 1  # TransformCageDataMovementMethodTypeMemberType
    Vector = 2  # TransformCageDataMovementMethodTypeMemberType
    Plane = 3  # TransformCageDataMovementMethodTypeMemberType
    Normal = 4  # TransformCageDataMovementMethodTypeMemberType
    Edge = 5  # TransformCageDataMovementMethodTypeMemberType
    
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
    


class TransformCageDataWCSOptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformCageDataWCSOptionType():
    """
    WCS principal axis or plane types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InferredAxis", "Along axis inferred during movement"
       "X", "Along X axis"
       "Y", "Along Y axis"
       "Z", "Along Z axis"
       "YZ", "In YZ plane"
       "XZ", "In XZ plane"
       "XY", "In XY plane"
    """
    InferredAxis = 0  # TransformCageDataWCSOptionTypeMemberType
    X = 1  # TransformCageDataWCSOptionTypeMemberType
    Y = 2  # TransformCageDataWCSOptionTypeMemberType
    Z = 3  # TransformCageDataWCSOptionTypeMemberType
    YZ = 4  # TransformCageDataWCSOptionTypeMemberType
    XZ = 5  # TransformCageDataWCSOptionTypeMemberType
    XY = 6  # TransformCageDataWCSOptionTypeMemberType
    
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
    


class TransformCageDataScalingMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformCageDataScalingMethodType():
    """
    Scaling method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Scale in the specified direction"
       "Planar", "Scale in the plane normal to specified direction"
       "Uniform", "Scale uniformly all the directions"
    """
    Linear = 0  # TransformCageDataScalingMethodTypeMemberType
    Planar = 1  # TransformCageDataScalingMethodTypeMemberType
    Uniform = 2  # TransformCageDataScalingMethodTypeMemberType
    
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
    


class TransformCageDataFallOffMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformCageDataFallOffMethodType():
    """
    Falloff method types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No falloff"
       "Selected", "Selected vertices falloff"
       "All", "All vertices falloff"
    """
    NotSet = 0  # TransformCageDataFallOffMethodTypeMemberType
    Selected = 1  # TransformCageDataFallOffMethodTypeMemberType
    All = 2  # TransformCageDataFallOffMethodTypeMemberType
    
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
    


class TransformCageData(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.TransformCageData` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateTransformCageData`
    
    Default values.
    
    ===========================  =====
    Property                     Value
    ===========================  =====
    CanRelocateToolToSelection   true 
    ---------------------------  -----
    CanReorientToolToSelection   true 
    ===========================  =====
    
    .. versionadded:: NX9.0.0
    """
    
    class TransformationMethodType():
        """
        Transformation method types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Drag", "Edit cage topology by direct dragging"
           "Transform", "Edit cage topology by transformations"
        """
        Drag = 0  # TransformCageDataTransformationMethodTypeMemberType
        Transform = 1  # TransformCageDataTransformationMethodTypeMemberType
        
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
        
    
    
    class MovementMethodType():
        """
        Movement types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WCS", "Movement along WCS principal axis or plane"
           "View", "Movement in view plane"
           "Vector", "Movement along arbitrary direction"
           "Plane", "Movement in arbitrary plane"
           "Normal", "Movement along a face normal"
           "Edge", "Movement along an edge"
        """
        WCS = 0  # TransformCageDataMovementMethodTypeMemberType
        View = 1  # TransformCageDataMovementMethodTypeMemberType
        Vector = 2  # TransformCageDataMovementMethodTypeMemberType
        Plane = 3  # TransformCageDataMovementMethodTypeMemberType
        Normal = 4  # TransformCageDataMovementMethodTypeMemberType
        Edge = 5  # TransformCageDataMovementMethodTypeMemberType
        
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
        
    
    
    class WCSOptionType():
        """
        WCS principal axis or plane types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InferredAxis", "Along axis inferred during movement"
           "X", "Along X axis"
           "Y", "Along Y axis"
           "Z", "Along Z axis"
           "YZ", "In YZ plane"
           "XZ", "In XZ plane"
           "XY", "In XY plane"
        """
        InferredAxis = 0  # TransformCageDataWCSOptionTypeMemberType
        X = 1  # TransformCageDataWCSOptionTypeMemberType
        Y = 2  # TransformCageDataWCSOptionTypeMemberType
        Z = 3  # TransformCageDataWCSOptionTypeMemberType
        YZ = 4  # TransformCageDataWCSOptionTypeMemberType
        XZ = 5  # TransformCageDataWCSOptionTypeMemberType
        XY = 6  # TransformCageDataWCSOptionTypeMemberType
        
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
        
    
    
    class ScalingMethodType():
        """
        Scaling method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Scale in the specified direction"
           "Planar", "Scale in the plane normal to specified direction"
           "Uniform", "Scale uniformly all the directions"
        """
        Linear = 0  # TransformCageDataScalingMethodTypeMemberType
        Planar = 1  # TransformCageDataScalingMethodTypeMemberType
        Uniform = 2  # TransformCageDataScalingMethodTypeMemberType
        
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
        
    
    
    class FallOffMethodType():
        """
        Falloff method types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No falloff"
           "Selected", "Selected vertices falloff"
           "All", "All vertices falloff"
        """
        NotSet = 0  # TransformCageDataFallOffMethodTypeMemberType
        Selected = 1  # TransformCageDataFallOffMethodTypeMemberType
        All = 2  # TransformCageDataFallOffMethodTypeMemberType
        
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
        
    
    
    def ResetFallOffToLinear(self) -> None:
        """
        Resets the falloff scale to linear.  
        
        Signature ``ResetFallOffToLinear()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    CageManipulator: CageManipulatorData = ...
    """
    Returns  the cage manipulation data.  
    
    <hr>
    
    Getter Method
    
    Signature ``CageManipulator`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.CageManipulatorData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CanMoveToolOnly: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be moved without transforming the selected cage topology.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :param canMove: 
    :type canMove: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanRelocateToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be relocated based on cage topology selection.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :param canRelocate: 
    :type canRelocate: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanReorientToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if transformer tool can be reoriented based on cage topology selection.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :param canReorient: 
    :type canReorient: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FallOffFactor: float = ...
    """
    Returns or sets  the falloff factor.  
    
    <hr>
    
    Getter Method
    
    Signature ``FallOffFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FallOffFactor`` 
    
    :param factor: 
    :type factor: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FallOffMethod: TransformCageDataFallOffMethodType = ...
    """
    Returns or sets  the falloff method.  
    
    <hr>
    
    Getter Method
    
    Signature ``FallOffMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageDataFallOffMethodType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FallOffMethod`` 
    
    :param fallOffMethod: 
    :type fallOffMethod: :py:class:`NXOpen.Features.Subdivision.TransformCageDataFallOffMethodType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FallOffObjects: SelectCageObjectData = ...
    """
    Returns  the falloff objects.  
    
    <hr>
    
    Getter Method
    
    Signature ``FallOffObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MovementMethod: TransformCageDataMovementMethodType = ...
    """
    Returns or sets  the movement method.  
    
    <hr>
    
    Getter Method
    
    Signature ``MovementMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageDataMovementMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MovementMethod`` 
    
    :param movementMethod: 
    :type movementMethod: :py:class:`NXOpen.Features.Subdivision.TransformCageDataMovementMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    MovementPlane: NXOpen.Plane = ...
    """
    Returns or sets  the movement plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``MovementPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MovementPlane`` 
    
    :param movementPlane: 
    :type movementPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    MovementVector: NXOpen.Direction = ...
    """
    Returns or sets  the movement vector.  
    
    <hr>
    
    Getter Method
    
    Signature ``MovementVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MovementVector`` 
    
    :param movementVector: 
    :type movementVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ScalingMethod: TransformCageDataScalingMethodType = ...
    """
    Returns or sets  the scaling method.  
    
    <hr>
    
    Getter Method
    
    Signature ``ScalingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageDataScalingMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ScalingMethod`` 
    
    :param scalingMethod: 
    :type scalingMethod: :py:class:`NXOpen.Features.Subdivision.TransformCageDataScalingMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    TransformationMethod: TransformCageDataTransformationMethodType = ...
    """
    Returns or sets  the transformation method.  
    
    <hr>
    
    Getter Method
    
    Signature ``TransformationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageDataTransformationMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransformationMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Features.Subdivision.TransformCageDataTransformationMethodType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    WCSOption: TransformCageDataWCSOptionType = ...
    """
    Returns or sets  the WCS option.  
    
    <hr>
    
    Getter Method
    
    Signature ``WCSOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.TransformCageDataWCSOptionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WCSOption`` 
    
    :param wcsOption: 
    :type wcsOption: :py:class:`NXOpen.Features.Subdivision.TransformCageDataWCSOptionType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: TransformCageData = ...  # unknown typename


class SubdivisionDeleteFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteFaceBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteFaceBuilder`
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder` instead.
    """
    FaceToDelete: SelectCageObjectData = ...
    """
    Returns  the face to delete.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceToDelete`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionDeleteFaceBuilder = ...  # unknown typename


class DeleteConstraintBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.DeleteConstraintBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateDeleteConstraintBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Objects: SelectCageObjectData = ...
    """
    Returns  the constrained objects whose constraint to be deleted.  
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: DeleteConstraintBuilder = ...  # unknown typename


class SubdivisionPrimitiveShapeBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionPrimitiveShapeBuilderTypes():
    """
    Type of primitive. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sphere", " - "
       "Cylinder", " - "
       "Block", " - "
       "Circle", " - "
       "Rectangle", " - "
       "Torus", " - "
    """
    Sphere = 0  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    Cylinder = 1  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    Block = 2  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    Circle = 3  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    Rectangle = 4  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    Torus = 5  # SubdivisionPrimitiveShapeBuilderTypesMemberType
    
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
    


class SubdivisionPrimitiveShapeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionPrimitiveShapeBuilder`
    
    Default values.
    
    =================  ========================================
    Property           Value
    =================  ========================================
    CircularSegments   4 
    -----------------  ----------------------------------------
    Height.Value       100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    HeightZ.Value      100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    InnerSize.Value    50 (millimeters part), 2 (inches part) 
    -----------------  ----------------------------------------
    LengthX.Value      100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    OuterSize.Value    100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    RadialSegments     8 
    -----------------  ----------------------------------------
    Size.Value         100 (millimeters part), 4 (inches part) 
    -----------------  ----------------------------------------
    WidthY.Value       100 (millimeters part), 4 (inches part) 
    =================  ========================================
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderEx` instead.
    """
    
    class Types():
        """
        Type of primitive. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sphere", " - "
           "Cylinder", " - "
           "Block", " - "
           "Circle", " - "
           "Rectangle", " - "
           "Torus", " - "
        """
        Sphere = 0  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        Cylinder = 1  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        Block = 2  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        Circle = 3  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        Rectangle = 4  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        Torus = 5  # SubdivisionPrimitiveShapeBuilderTypesMemberType
        
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
        
    
    
    def UpdateMesh(self) -> None:
        """
        Updates the mesh data after changes in the origin.  
        
        Signature ``UpdateMesh()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    CircularSegments: int = ...
    """
    Returns or sets  the number of segments in circular sectional direction of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``CircularSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CircularSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height.  
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    HeightZ: NXOpen.Expression = ...
    """
    Returns  the height in z direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``HeightZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    InnerSize: NXOpen.Expression = ...
    """
    Returns  the inner size of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``InnerSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    LengthX: NXOpen.Expression = ...
    """
    Returns  the length in x direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``LengthX`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Origin: NXOpen.Point = ...
    """
    Returns or sets  the origin.  
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param origin: 
    :type origin: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    OuterSize: NXOpen.Expression = ...
    """
    Returns  the outer size of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``OuterSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    RadialSegments: int = ...
    """
    Returns or sets  the number of segments in radial direction of torus.  
    
    <hr>
    
    Getter Method
    
    Signature ``RadialSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RadialSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Size: NXOpen.Expression = ...
    """
    Returns  the size.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Type: SubdivisionPrimitiveShapeBuilderTypes = ...
    """
    Returns or sets  the type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.Subdivision.SubdivisionPrimitiveShapeBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    WidthY: NXOpen.Expression = ...
    """
    Returns  the width in y direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``WidthY`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionPrimitiveShapeBuilder = ...  # unknown typename


class SubdivisionSubdivideFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSubdivideFaceBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSubdivideFaceBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    def Subdivide(self) -> None:
        """
        Perform subdivide operation.  
        
        Signature ``Subdivide()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    FacesToSubdivide: SelectCageObjectData = ...
    """
    Returns  the faces to subdivide.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacesToSubdivide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Scale: NXOpen.Expression = ...
    """
    Returns  the scale factor.  
    
    The value is from 0 to 100. 0 refers to the original size of the face, 100 refers to the center of the face. 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionSubdivideFaceBuilder = ...  # unknown typename


class SubdivisionFillBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionFillBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionFillBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionFillBuilderContinuityTypeMemberType
    
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
    


class SubdivisionFillBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionFillBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionFillBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionFillBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionFillBuilderContinuityTypeMemberType
        
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
        
    
    CanConnectSymmetrically: bool = ...
    """
    Returns or sets  the flag indicating if selected edges are to be connected with their symmetric counterpart.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanConnectSymmetrically`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanConnectSymmetrically`` 
    
    :param connectSymmetrically: 
    :type connectSymmetrically: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Continuity: SubdivisionFillBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to edges
    specified by :py:meth:`NXOpen.Features.Subdivision.SubdivisionFillBuilder.SelectedEdges`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionFillBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionFillBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SelectedEdges: SelectCageObjectData = ...
    """
    Returns  the edges to form a face.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectedEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionFillBuilder = ...  # unknown typename


class SelectSubdivisionBodyList(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a list of objects on a selection list.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def Add(self, object: SubdivisionBody) -> bool:
        """
        Adds an object to the list
        
        Signature ``Add(object)`` 
        
        :param object:  object to add  
        :type object: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, objects: 'list[SubdivisionBody]') -> bool:
        """
        Adds a set of objects to the list
        
        Signature ``Add(objects)`` 
        
        :param objects:  objects to add  
        :type objects: list of :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Adds the objects from a SelectionMethod to the list
        
        Signature ``Add(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: SubdivisionBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
        Adds the object with the objects view and objects point
        
        Signature ``Add(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added to list;
        False if the object was already a member
        of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``Add(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Add(self, selection: SubdivisionBody, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> bool:
        """
        The object being selected with CAE set object information.
        
        Signature ``Add(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        :returns:  True if succesully added all objects to the list;
        False if there was at least one object that was already a
        member of the list and duplicates are not allowed  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObjectList.Add`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def Remove(self, object: SubdivisionBody) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, object: SubdivisionBody, view: NXOpen.View) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(object, view)`` 
        
        :param object:  Object to remove  
        :type object: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view:  with this view 
        :type view: :py:class:`NXOpen.View` 
        :returns:  True if succesully removed from list;
        False if the object / view was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: SubdivisionBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SubdivisionBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
        Remove specified object from list.
        
        Signature ``Remove(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1: first  selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :param view2: second  selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Remove(self, inputSelectionMethod: NXOpen.SelectionMethod) -> bool:
        """
        Removes the objects from a SelectionMethod from the list
        
        Signature ``Remove(inputSelectionMethod)`` 
        
        :param inputSelectionMethod:  selection method containing objects to add  
        :type inputSelectionMethod: :py:class:`NXOpen.SelectionMethod` 
        :returns:  True if succesully removed all objects from the list;
        False if there was at least one object that was not a
        member of the list  
        :rtype: bool 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveArray(self, objects: 'list[SubdivisionBody]') -> bool:
        """
        Remove specified objects from list.  
        
        Signature ``RemoveArray(objects)`` 
        
        :param objects:  Objects to remove  
        :type objects: list of :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :returns:  True if succesully removed from list;
        False if the object was not a member of the list  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Clear(self) -> None:
        """
        Removes all items from the list.  
        
        Signature ``Clear()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Contains(self, object: SubdivisionBody) -> bool:
        """
        Returns whether the specified object is already in the list or not.  
        
        Signature ``Contains(object)`` 
        
        :param object:  object to check  
        :type object: :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        :returns:  true if object is in the list, false otherwise  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetArray(self, objects: 'list[SubdivisionBody]') -> None:
        """
        Overloaded method SetArray
        
        * ``SetArray(objects)`` 
        * ``SetArray(vars)`` 
        
        <hr>
        
        Sets the list of objects in the selection list. This will clear any existing
        items in the list.
        
        Signature ``SetArray(objects)`` 
        
        :param objects:  items to put in the list 
        :type objects: list of :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetArray(self) -> 'list[SubdivisionBody]':
        """
        Overloaded method GetArray
        
        * ``GetArray()`` 
        * ``GetArray()`` 
        
        <hr>
        
        Returns the list of objects in the selection list.
        
        Signature ``GetArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.Features.Subdivision.SubdivisionBody` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        
        <hr>
        """
        ...
    
    
    def GetSelectObjectArray(self) -> 'list[NXOpen.SelectObject]':
        """
        Returns the list of SelectObjects in the selection list.  
        
        Signature ``GetSelectObjectArray()`` 
        
        :returns:  items in list  
        :rtype: list of :py:class:`NXOpen.SelectObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
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
    
    DuplicatesAllowed: bool = ...
    """
    Returns  whether duplicate objects are allowed in the selection list.  
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicatesAllowed`` 
    
    :returns:  Whether duplicate objects are allowed  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Size: int = ...
    """
    Returns  the number of objects in the list.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns:  number of objects in the list  
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectSubdivisionBodyList = ...  # unknown typename


class SubdivisionSetContinuityBuilderContinuityTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionSetContinuityBuilderContinuityTypes():
    """
    Represents the continuity type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", " - "
       "Sharp", " - "
    """
    Smooth = 0  # SubdivisionSetContinuityBuilderContinuityTypesMemberType
    Sharp = 1  # SubdivisionSetContinuityBuilderContinuityTypesMemberType
    
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
    


class SubdivisionSetContinuityBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionSetContinuityBuilder`
    
    Default values.
    
    ===============  =======
    Property         Value
    ===============  =======
    ContinuityType   Smooth 
    ===============  =======
    
    .. versionadded:: NX9.0.0
    """
    
    class ContinuityTypes():
        """
        Represents the continuity type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", " - "
           "Sharp", " - "
        """
        Smooth = 0  # SubdivisionSetContinuityBuilderContinuityTypesMemberType
        Sharp = 1  # SubdivisionSetContinuityBuilderContinuityTypesMemberType
        
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
        
    
    ContinuityType: SubdivisionSetContinuityBuilderContinuityTypes = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface. 
    
    <hr>
    
    Getter Method
    
    Signature ``ContinuityType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilderContinuityTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContinuityType`` 
    
    :param continuityType: 
    :type continuityType: :py:class:`NXOpen.Features.Subdivision.SubdivisionSetContinuityBuilderContinuityTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    TargetObject: SelectCageObjectData = ...
    """
    Returns  the target object.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionSetContinuityBuilder = ...  # unknown typename


class CopyCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.CopyCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateCopyCageBuilder`
    
    Default values.
    
    ===========================  =====
    Property                     Value
    ===========================  =====
    CanRelocateToolToSelection   1 
    ---------------------------  -----
    CanReorientToolToSelection   1 
    ---------------------------  -----
    NumberOfCopies               1 
    ===========================  =====
    
    .. versionadded:: NX10.0.0
    """
    
    def ResetTransformerToCentroidOfSelection(self) -> None:
        """
        Repositions the :py:class:`NXOpen.GeometricUtilities.TransformerData` to the centroid of the selected entities.  
        
        Signature ``ResetTransformerToCentroidOfSelection()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def SetTransformerToObject(self, selectionData: CageManipulatorDataObjectSelectionData_Struct) -> None:
        """
        Repositions the :py:class:`NXOpen.GeometricUtilities.TransformerData` to the specified entity.  
        
        Signature ``SetTransformerToObject(selectionData)`` 
        
        :param selectionData: 
        :type selectionData: :py:class:`NXOpen.Features.Subdivision.CageManipulatorDataObjectSelectionData_Struct` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    CanMoveToolOnly: bool = ...
    """
    Returns or sets  the flag indicating if tool can be moved alone without moving selected topology 
    
    <hr>
    
    Getter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanMoveToolOnly`` 
    
    :param canMoveToolOnly: 
    :type canMoveToolOnly: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanRelocateToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if tool should relocate to selection 
    
    <hr>
    
    Getter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanRelocateToolToSelection`` 
    
    :param canRelocateToolToSelection: 
    :type canRelocateToolToSelection: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    CanReorientToolToSelection: bool = ...
    """
    Returns or sets  the flag indicating if tool should reorient to selection 
    
    <hr>
    
    Getter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanReorientToolToSelection`` 
    
    :param canReorientToolToSelection: 
    :type canReorientToolToSelection: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    NumberOfCopies: int = ...
    """
    Returns or sets  the number of copies 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfCopies`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfCopies`` 
    
    :param numberOfCopies: 
    :type numberOfCopies: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Objects: SelectCageObjectData = ...
    """
    Returns  the objects to be copied 
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CopyCageBuilder = ...  # unknown typename


class SubdivisionConnectCageBuilderContinuityTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionConnectCageBuilderContinuityTypes():
    """
    Represents the continuity type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", " - "
       "Sharp", " - "
    """
    Smooth = 0  # SubdivisionConnectCageBuilderContinuityTypesMemberType
    Sharp = 1  # SubdivisionConnectCageBuilderContinuityTypesMemberType
    
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
    


class SubdivisionConnectCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionConnectCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionConnectCageBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class ContinuityTypes():
        """
        Represents the continuity type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", " - "
           "Sharp", " - "
        """
        Smooth = 0  # SubdivisionConnectCageBuilderContinuityTypesMemberType
        Sharp = 1  # SubdivisionConnectCageBuilderContinuityTypesMemberType
        
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
        
    
    CageEdgeToEdit: SelectCageObjectData = ...
    """
    Returns  the cage edge to edit 
    
    <hr>
    
    Getter Method
    
    Signature ``CageEdgeToEdit`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ContinuityType: SubdivisionConnectCageBuilderContinuityTypes = ...
    """
    Returns or sets  the continuity.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContinuityType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionConnectCageBuilderContinuityTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContinuityType`` 
    
    :param continuityType: 
    :type continuityType: :py:class:`NXOpen.Features.Subdivision.SubdivisionConnectCageBuilderContinuityTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ExternalReference: NXOpen.Section = ...
    """
    Returns  the external edges 
    
    <hr>
    
    Getter Method
    
    Signature ``ExternalReference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: SubdivisionConnectCageBuilder = ...  # unknown typename


class DefineWorkRegionBuilderWorkRegionDefinitionMethodsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DefineWorkRegionBuilderWorkRegionDefinitionMethods():
    """
    Method of defining work region. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "Treat all the region as work region"
       "Selected", "Specify a region as work region"
    """
    All = 0  # DefineWorkRegionBuilderWorkRegionDefinitionMethodsMemberType
    Selected = 1  # DefineWorkRegionBuilderWorkRegionDefinitionMethodsMemberType
    
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
    


class DefineWorkRegionBuilderFrozenRegionDefinitionMethodsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DefineWorkRegionBuilderFrozenRegionDefinitionMethods():
    """
    Method of defining frozen region. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hidden", "Do not display the frozen region"
       "Colored", "Mark frozen region with color and do not allow its selection"
    """
    Hidden = 0  # DefineWorkRegionBuilderFrozenRegionDefinitionMethodsMemberType
    Colored = 1  # DefineWorkRegionBuilderFrozenRegionDefinitionMethodsMemberType
    
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
    


class DefineWorkRegionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`Features.Subdivision.DefineWorkRegionBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateDefineWorkRegionBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class WorkRegionDefinitionMethods():
        """
        Method of defining work region. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "Treat all the region as work region"
           "Selected", "Specify a region as work region"
        """
        All = 0  # DefineWorkRegionBuilderWorkRegionDefinitionMethodsMemberType
        Selected = 1  # DefineWorkRegionBuilderWorkRegionDefinitionMethodsMemberType
        
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
        
    
    
    class FrozenRegionDefinitionMethods():
        """
        Method of defining frozen region. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hidden", "Do not display the frozen region"
           "Colored", "Mark frozen region with color and do not allow its selection"
        """
        Hidden = 0  # DefineWorkRegionBuilderFrozenRegionDefinitionMethodsMemberType
        Colored = 1  # DefineWorkRegionBuilderFrozenRegionDefinitionMethodsMemberType
        
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
        
    
    FrozenColor: NXOpen.NXColor = ...
    """
    Returns or sets  the frozen region color 
    
    <hr>
    
    Getter Method
    
    Signature ``FrozenColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FrozenColor`` 
    
    :param frozenColor: 
    :type frozenColor: Id 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FrozenRegionDefinitionMethod: DefineWorkRegionBuilderFrozenRegionDefinitionMethods = ...
    """
    Returns or sets  the frozen region method 
    
    <hr>
    
    Getter Method
    
    Signature ``FrozenRegionDefinitionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilderFrozenRegionDefinitionMethods` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FrozenRegionDefinitionMethod`` 
    
    :param frozenRegionDefinitionMethod: 
    :type frozenRegionDefinitionMethod: :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilderFrozenRegionDefinitionMethods` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    WorkRegionDefinitionMethod: DefineWorkRegionBuilderWorkRegionDefinitionMethods = ...
    """
    Returns or sets  the work region definition method 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkRegionDefinitionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilderWorkRegionDefinitionMethods` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WorkRegionDefinitionMethod`` 
    
    :param workRegionDefinitionMethod: 
    :type workRegionDefinitionMethod: :py:class:`NXOpen.Features.Subdivision.DefineWorkRegionBuilderWorkRegionDefinitionMethods` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    WorkRegionObjects: SelectCageObjectData = ...
    """
    Returns  the work region objects 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkRegionObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: DefineWorkRegionBuilder = ...  # unknown typename


class SubdivisionLoftBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionLoftBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionLoftBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionLoftBuilderContinuityTypeMemberType
    
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
    


class SubdivisionLoftBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionLoftBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionLoftBuilder`
    
    Default values.
    
    =================  =====
    Property           Value
    =================  =====
    CanSew             1 
    -----------------  -----
    NumberOfSegments   1 
    =================  =====
    
    .. versionadded:: NX10.0.0
    """
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionLoftBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionLoftBuilderContinuityTypeMemberType
        
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
        
    
    CanSew: bool = ...
    """
    Returns or sets  the value indicating if open edges of the loft mesh can be sewn with selected input open edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanSew`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanSew`` 
    
    :param canSew: 
    :type canSew: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Continuity: SubdivisionLoftBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to edges
    of the lofted region that are sewn with the primary existing region. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionLoftBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionLoftBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    IsClosed: bool = ...
    """
    Returns or sets  the value indicating if the output mesh is closed.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsClosed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsClosed`` 
    
    :param isClosed: 
    :type isClosed: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    NumberOfSegments: int = ...
    """
    Returns or sets  the number of segments 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfSegments`` 
    
    :param numberOfSegments: 
    :type numberOfSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Sections: CageSectionDataList = ...
    """
    Returns  the section objects for lofting 
    
    <hr>
    
    Getter Method
    
    Signature ``Sections`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.CageSectionDataList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionLoftBuilder = ...  # unknown typename


class SubdivisionBridgeFaceBuilderContinuityTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionBridgeFaceBuilderContinuityType():
    """
    Type of continuity. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Smooth", "Smooth continuity"
       "Sharp", "Sharp continuity"
    """
    Smooth = 0  # SubdivisionBridgeFaceBuilderContinuityTypeMemberType
    Sharp = 1  # SubdivisionBridgeFaceBuilderContinuityTypeMemberType
    
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
    


class SubdivisionBridgeFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionBridgeFaceBuilder`
    
    Default values.
    
    ============  =====
    Property      Value
    ============  =====
    NumSegments   1 
    ============  =====
    
    .. versionadded:: NX9.0.0
    """
    
    class ContinuityType():
        """
        Type of continuity. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Smooth", "Smooth continuity"
           "Sharp", "Sharp continuity"
        """
        Smooth = 0  # SubdivisionBridgeFaceBuilderContinuityTypeMemberType
        Sharp = 1  # SubdivisionBridgeFaceBuilderContinuityTypeMemberType
        
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
        
    
    Continuity: SubdivisionBridgeFaceBuilderContinuityType = ...
    """
    Returns or sets  the continuity.  
    
    The continuity is used to specify creases in the limit surface corresponding to the outer
    edges of the faces specified by :py:meth:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.FaceSet1` and 
    :py:meth:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilder.FaceSet2`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Continuity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Continuity`` 
    
    :param continuity: 
    :type continuity: :py:class:`NXOpen.Features.Subdivision.SubdivisionBridgeFaceBuilderContinuityType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    FaceSet1: SelectCageObjectData = ...
    """
    Returns  the first face set.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    FaceSet2: SelectCageObjectData = ...
    """
    Returns  the second face set.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NumSegments: int = ...
    """
    Returns or sets  the number of segments in the output bridge faces 
    
    <hr>
    
    Getter Method
    
    Signature ``NumSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumSegments`` 
    
    :param numSegments: 
    :type numSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionBridgeFaceBuilder = ...  # unknown typename


class CageManipulatorDataObjectMoveData_Struct():
    """
    Contains object movement information.  
    
    .. versionadded:: NX9.0.0
    
    .
    Constructor: 
    NXOpen.Features.Subdivision.CageManipulatorData.ObjectMoveData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    DraggedObject: NXOpen.NXObject = ...
    """
    The dragged object.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    BeginDragCursorPosition: NXOpen.Point3d = ...
    """
    The point from which object dragging is initiated, the point
    under the cursor when seen in view direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    BeginDragObjectPosition: NXOpen.Point3d = ...
    """
    The point on object near cursor from which object dragging is initiated 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    View: NXOpen.View = ...
    """
    The view in which object is dragged.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.View`
    """
    MicropositioningScale: float = ...
    """
    The micropositioning scale.  
    
    <hr>
    
    Field Value
    Type:float
    """
    ViewDirection: NXOpen.Vector3d = ...
    """
    The view direction.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """


class SelectCageObjectData(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents subdivision cage topology object selection.  
    
    .. versionadded:: NX9.0.0
    """
    
    def ClearAndAdd(self, objects: 'list[NXOpen.NXObject]', view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
        Clears the currently present objects and adds new objects.  
        
        Signature ``ClearAndAdd(objects, view, point)`` 
        
        :param objects:  Objects to process.  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param view:  Selected object view when selecting a single object.  
        :type view: :py:class:`NXOpen.View` 
        :param point:  Selected object point when selecting a single object.  
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def SetCursorLocation(self, point: NXOpen.Point3d) -> None:
        """
        Sets the cursor location in absolute coordinates.  
        
        Signature ``SetCursorLocation(point)`` 
        
        :param point: 
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def SetViewDirection(self, direction: NXOpen.Vector3d) -> None:
        """
        Sets the view direction.  
        
        Signature ``SetViewDirection(direction)`` 
        
        :param direction: 
        :type direction: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
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
    
    CanDeselectObjectsAutomatically: bool = ...
    """
    Returns or sets  the flag indicating if previously selected objects can be de-selected during selection of new objects.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanDeselectObjectsAutomatically`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX11.0.0
       There is no replacement for this unused property.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanDeselectObjectsAutomatically`` 
    
    :param canDeselect: 
    :type canDeselect: bool 
    
    .. versionadded:: NX9.0.0
    
    .. deprecated::  NX11.0.0
       There is no replacement for this unused property.
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    SelectionList: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the object list.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SelectCageObjectData = ...  # unknown typename


class CageManipulatorData(SelectCageObjectData):
    """
    Subdivision cage manipulation tool.  
    
    .. versionadded:: NX9.0.0
    """
    
    class ObjectMoveData():
        """
        Contains object movement information.  
        
        .. versionadded:: NX9.0.0
        
        .
        Constructor: 
        NXOpen.Features.Subdivision.CageManipulatorData.ObjectMoveData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        DraggedObject: NXOpen.NXObject = ...
        """
        The dragged object.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        BeginDragCursorPosition: NXOpen.Point3d = ...
        """
        The point from which object dragging is initiated, the point
        under the cursor when seen in view direction.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        BeginDragObjectPosition: NXOpen.Point3d = ...
        """
        The point on object near cursor from which object dragging is initiated 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        View: NXOpen.View = ...
        """
        The view in which object is dragged.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.View`
        """
        MicropositioningScale: float = ...
        """
        The micropositioning scale.  
        
        <hr>
        
        Field Value
        Type:float
        """
        ViewDirection: NXOpen.Vector3d = ...
        """
        The view direction.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
    
    
    class ObjectSelectionData():
        """
        Contains object selection information.  
        
        .. versionadded:: NX9.0.0
        
        .
        Constructor: 
        NXOpen.Features.Subdivision.CageManipulatorData.ObjectSelectionData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        SelectedObject: NXOpen.NXObject = ...
        """
        The selected object.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        SelectionPosition: NXOpen.Point3d = ...
        """
        The point at which object is selected, the point
        under the cursor when seen in view direction.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        ViewDirection: NXOpen.Vector3d = ...
        """
        The view direction.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        IsSnappedPosition: bool = ...
        """
        Is SelectionPosition a snapped location.  
        
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def PrepareToMove(self, moveData: CageManipulatorDataObjectMoveData_Struct) -> None:
        """
        Prepares data to move the objects.  
        
        Signature ``PrepareToMove(moveData)`` 
        
        :param moveData: 
        :type moveData: :py:class:`NXOpen.Features.Subdivision.CageManipulatorDataObjectMoveData_Struct` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    @typing.overload
    def Move(self, moveToPoint: NXOpen.Point3d, isSnapGesture: bool) -> None:
        """
        Moves the objects by dragging. 
        
        Signature ``Move(moveToPoint, isSnapGesture)`` 
        
        :param moveToPoint: 
        :type moveToPoint: :py:class:`NXOpen.Point3d` 
        :param isSnapGesture:  Are we processing a snap gesture.  
        :type isSnapGesture: bool 
        
        .. versionadded:: NX9.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Features.Subdivision.CageManipulatorData.Move` with optional constraint point instead.
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    @typing.overload
    def Move(self, moveToPoint: NXOpen.Point3d, point: NXOpen.Point, isSnapGesture: bool) -> None:
        """
        Moves the objects by dragging. A constraint point can be assigned when moving a vertex. 
        
        Signature ``Move(moveToPoint, point, isSnapGesture)`` 
        
        :param moveToPoint: 
        :type moveToPoint: :py:class:`NXOpen.Point3d` 
        :param point:  Optional constraint point  
        :type point: :py:class:`NXOpen.Point` 
        :param isSnapGesture:  Are we processing a snap gesture.  
        :type isSnapGesture: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def EndMove(self) -> None:
        """
        Releases the data prepared at the beginning of the move.  
        
        Signature ``EndMove()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def StepMove(self, step: float) -> None:
        """
        Moves the objects by step value.  
        
        Signature ``StepMove(step)`` 
        
        :param step: 
        :type step: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def ResetTransformerToCentroidOfSelection(self) -> None:
        """
        Repositions the :py:class:`NXOpen.GeometricUtilities.TransformerData` to the centroid of the selected entities.  
        
        Signature ``ResetTransformerToCentroidOfSelection()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def SetTransformerToObject(self, selectionData: CageManipulatorDataObjectSelectionData_Struct) -> None:
        """
        Repositions the :py:class:`NXOpen.GeometricUtilities.TransformerData` to the specified entity.  
        
        Signature ``SetTransformerToObject(selectionData)`` 
        
        :param selectionData: 
        :type selectionData: :py:class:`NXOpen.Features.Subdivision.CageManipulatorDataObjectSelectionData_Struct` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    Transformer: NXOpen.GeometricUtilities.TransformerData = ...
    """
    Returns  the transformation tool.  
    
    <hr>
    
    Getter Method
    
    Signature ``Transformer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.TransformerData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: CageManipulatorData = ...  # unknown typename


class SubdivisionBody(NXOpen.Features.BodyFeature):
    """
    Represents a subdivision body feature.  
    
    An instance of this class can be obtained from :py:meth:`SubdivisionTaskEnvironment.ActiveSubdivisionBodyFeature`
    
    .. versionadded:: NX9.0.0
    """
    Null: SubdivisionBody = ...  # unknown typename


class SubdivisionDeleteCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteCageBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionDeleteCageBuilder`
    
    .. versionadded:: NX10.0.0
    
    .. deprecated::  NX11.0.0
       Use :py:class:`NXOpen.Features.Subdivision.SubdivisionDeleteObjectBuilder` instead.
    """
    SelectCageObject: SelectCageObjectData = ...
    """
    Returns  the select cage object 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectCageObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: SubdivisionDeleteCageBuilder = ...  # unknown typename


class ExtractCagePolylineBuilderInputCurveOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExtractCagePolylineBuilderInputCurveOption():
    """
    Input curves options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Keep", "Keep input curves as they are"
       "Hide", "Hide input curves"
       "Delete", "Delete input curves"
    """
    Keep = 0  # ExtractCagePolylineBuilderInputCurveOptionMemberType
    Hide = 1  # ExtractCagePolylineBuilderInputCurveOptionMemberType
    Delete = 2  # ExtractCagePolylineBuilderInputCurveOptionMemberType
    
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
    


class ExtractCagePolylineBuilder(NXOpen.Builder):
    """
    Extract cage polyline builder class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateExtractCagePolylineBuilder`
    
    Default values.
    
    =================  =====
    Property           Value
    =================  =====
    NumberOfSegments   4 
    =================  =====
    
    .. versionadded:: NX10.0.0
    """
    
    class InputCurveOption():
        """
        Input curves options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Keep", "Keep input curves as they are"
           "Hide", "Hide input curves"
           "Delete", "Delete input curves"
        """
        Keep = 0  # ExtractCagePolylineBuilderInputCurveOptionMemberType
        Hide = 1  # ExtractCagePolylineBuilderInputCurveOptionMemberType
        Delete = 2  # ExtractCagePolylineBuilderInputCurveOptionMemberType
        
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
        
    
    CurveToExtract: NXOpen.ScCollector = ...
    """
    Returns  the curve to extract 
    
    <hr>
    
    Getter Method
    
    Signature ``CurveToExtract`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InputCurveOptions: ExtractCagePolylineBuilderInputCurveOption = ...
    """
    Returns or sets  the input curve options 
    
    <hr>
    
    Getter Method
    
    Signature ``InputCurveOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.ExtractCagePolylineBuilderInputCurveOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputCurveOptions`` 
    
    :param inputCurveOptions: 
    :type inputCurveOptions: :py:class:`NXOpen.Features.Subdivision.ExtractCagePolylineBuilderInputCurveOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    NumberOfSegments: int = ...
    """
    Returns or sets  the number of segments 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfSegments`` 
    
    :param numberOfSegments: 
    :type numberOfSegments: int 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: ExtractCagePolylineBuilder = ...  # unknown typename


class SubdivisionProjectCageBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionProjectCageBuilderTypes():
    """
    The type of projection 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ToTarget", "Project on target"
       "ToAverage", "Project using best fit plane or axis"
       "AlignNormal", "Align edges normal to the specified plane"
    """
    ToTarget = 0  # SubdivisionProjectCageBuilderTypesMemberType
    ToAverage = 1  # SubdivisionProjectCageBuilderTypesMemberType
    AlignNormal = 2  # SubdivisionProjectCageBuilderTypesMemberType
    
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
    


class SubdivisionProjectCageBuilderTargetTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionProjectCageBuilderTargetTypes():
    """
    Target types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InferredPlane", " - "
       "InferredAxis", " - "
       "YcZcPlane", " - "
       "XcZcPlane", " - "
       "XcYcPlane", " - "
       "XcAxis", " - "
       "YcAxis", " - "
       "ZcAxis", " - "
       "Object", " - "
       "Plane", " - "
       "DynamicPlane", " - "
    """
    InferredPlane = 0  # SubdivisionProjectCageBuilderTargetTypesMemberType
    InferredAxis = 1  # SubdivisionProjectCageBuilderTargetTypesMemberType
    YcZcPlane = 2  # SubdivisionProjectCageBuilderTargetTypesMemberType
    XcZcPlane = 3  # SubdivisionProjectCageBuilderTargetTypesMemberType
    XcYcPlane = 4  # SubdivisionProjectCageBuilderTargetTypesMemberType
    XcAxis = 5  # SubdivisionProjectCageBuilderTargetTypesMemberType
    YcAxis = 6  # SubdivisionProjectCageBuilderTargetTypesMemberType
    ZcAxis = 7  # SubdivisionProjectCageBuilderTargetTypesMemberType
    Object = 8  # SubdivisionProjectCageBuilderTargetTypesMemberType
    Plane = 9  # SubdivisionProjectCageBuilderTargetTypesMemberType
    DynamicPlane = 10  # SubdivisionProjectCageBuilderTargetTypesMemberType
    
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
    


class SubdivisionProjectCageBuilderModeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SubdivisionProjectCageBuilderModeOptions():
    """
    Best fit mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Fit a line"
       "Planar", "Fit a plane"
    """
    Linear = 0  # SubdivisionProjectCageBuilderModeOptionsMemberType
    Planar = 1  # SubdivisionProjectCageBuilderModeOptionsMemberType
    
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
    


class SubdivisionProjectCageBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionProjectCageBuilder`
    
    Default values.
    
    ===========  ==============
    Property     Value
    ===========  ==============
    Mode         Planar 
    -----------  --------------
    TargetType   InferredPlane 
    ===========  ==============
    
    .. versionadded:: NX9.0.0
    """
    
    class Types():
        """
        The type of projection 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ToTarget", "Project on target"
           "ToAverage", "Project using best fit plane or axis"
           "AlignNormal", "Align edges normal to the specified plane"
        """
        ToTarget = 0  # SubdivisionProjectCageBuilderTypesMemberType
        ToAverage = 1  # SubdivisionProjectCageBuilderTypesMemberType
        AlignNormal = 2  # SubdivisionProjectCageBuilderTypesMemberType
        
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
        
    
    
    class TargetTypes():
        """
        Target types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InferredPlane", " - "
           "InferredAxis", " - "
           "YcZcPlane", " - "
           "XcZcPlane", " - "
           "XcYcPlane", " - "
           "XcAxis", " - "
           "YcAxis", " - "
           "ZcAxis", " - "
           "Object", " - "
           "Plane", " - "
           "DynamicPlane", " - "
        """
        InferredPlane = 0  # SubdivisionProjectCageBuilderTargetTypesMemberType
        InferredAxis = 1  # SubdivisionProjectCageBuilderTargetTypesMemberType
        YcZcPlane = 2  # SubdivisionProjectCageBuilderTargetTypesMemberType
        XcZcPlane = 3  # SubdivisionProjectCageBuilderTargetTypesMemberType
        XcYcPlane = 4  # SubdivisionProjectCageBuilderTargetTypesMemberType
        XcAxis = 5  # SubdivisionProjectCageBuilderTargetTypesMemberType
        YcAxis = 6  # SubdivisionProjectCageBuilderTargetTypesMemberType
        ZcAxis = 7  # SubdivisionProjectCageBuilderTargetTypesMemberType
        Object = 8  # SubdivisionProjectCageBuilderTargetTypesMemberType
        Plane = 9  # SubdivisionProjectCageBuilderTargetTypesMemberType
        DynamicPlane = 10  # SubdivisionProjectCageBuilderTargetTypesMemberType
        
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
        
    
    
    class ModeOptions():
        """
        Best fit mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Fit a line"
           "Planar", "Fit a plane"
        """
        Linear = 0  # SubdivisionProjectCageBuilderModeOptionsMemberType
        Planar = 1  # SubdivisionProjectCageBuilderModeOptionsMemberType
        
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
        
    
    
    def OnTargetPlane(self) -> None:
        """
        Update builder data based on target plane definition 
        
        Signature ``OnTargetPlane()`` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    
    def OnTargetDynamicPlane(self) -> None:
        """
        Update builder data based on target dynamic plane definition 
        
        Signature ``OnTargetDynamicPlane()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    Mode: SubdivisionProjectCageBuilderModeOptions = ...
    """
    Returns or sets  the mode 
    
    <hr>
    
    Getter Method
    
    Signature ``Mode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderModeOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Mode`` 
    
    :param mode: 
    :type mode: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderModeOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    ObjectsToProject: SelectCageObjectData = ...
    """
    Returns  the objects to project 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectsToProject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Target: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the target 
    
    <hr>
    
    Getter Method
    
    Signature ``Target`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TargetCageObjects: SelectCageObjectData = ...
    """
    Returns  the target cage objects to infer a plane or axis from 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetCageObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TargetDynamicPlane: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the target dynamic plane 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetDynamicPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetDynamicPlane`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    TargetPlane: NXOpen.Plane = ...
    """
    Returns or sets  the target plane 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetPlane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.1
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    TargetType: SubdivisionProjectCageBuilderTargetTypes = ...
    """
    Returns or sets  the target type 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTargetTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetType`` 
    
    :param targetType: 
    :type targetType: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTargetTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Type: SubdivisionProjectCageBuilderTypes = ...
    """
    Returns or sets  the type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.Subdivision.SubdivisionProjectCageBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_subdivision (" NX SUBDIVISION")
    """
    Null: SubdivisionProjectCageBuilder = ...  # unknown typename


class CopyCageData(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.CopyCageData`.  
    
    Copies Control Cage, Cage Face and Cage Polyline type objects on the clipboard.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateCopyCageData`
    
    .. versionadded:: NX11.0.0
    """
    
    def GetObjects(self) -> 'list[NXOpen.NXObject]':
        """
        Returns the objects to be copied.  
        
        Signature ``GetObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetObjects(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Sets the objects to be copied.  
        
        Signature ``SetObjects(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_subdivision (" NX SUBDIVISION")
        """
        ...
    
    Null: CopyCageData = ...  # unknown typename


class SubdivisionMergeFaceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Features.Subdivision.SubdivisionMergeFaceBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.Subdivision.SubdivisionBodyCollection.CreateSubdivisionMergeFaceBuilder`
    
    .. versionadded:: NX9.0.0
    """
    FacesToMerge: SelectCageObjectData = ...
    """
    Returns  the faces to merge.  
    
    <hr>
    
    Getter Method
    
    Signature ``FacesToMerge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.Subdivision.SelectCageObjectData` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SubdivisionMergeFaceBuilder = ...  # unknown typename


