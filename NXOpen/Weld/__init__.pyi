# module 'NXOpen.Weld'
#
# Automatically generated 2025-06-09T14:38:48.519707
#
"""Default documentation for NXOpen.Weld."""

import typing

import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Die
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Routing



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class FilletBuilderEnumExtendEdgesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumExtendEdges():
    """
    the options for populating the edge selections. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Manual", " - "
       "Automatic", " - "
    """
    Manual = 0  # FilletBuilderEnumExtendEdgesMemberType
    Automatic = 1  # FilletBuilderEnumExtendEdgesMemberType
    
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
    


class FilletBuilderEnumConstructionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumConstructionMethod():
    """
    the options for which construction method to use. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", " - "
       "RollAround", " - "
    """
    Default = 0  # FilletBuilderEnumConstructionMethodMemberType
    RollAround = 1  # FilletBuilderEnumConstructionMethodMemberType
    
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
    


class FilletBuilderEnumExtensionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumExtensionMethod():
    """
    the Extension enum. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Automatic", " - "
       "ByValue", " - "
    """
    Automatic = 0  # FilletBuilderEnumExtensionMethodMemberType
    ByValue = 1  # FilletBuilderEnumExtensionMethodMemberType
    
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
    


class FilletBuilderEnumContourMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumContour():
    """
    the Contour enum. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Convex", " - "
       "Flush", " - "
       "Concave", " - "
    """
    NotSet = 0  # FilletBuilderEnumContourMemberType
    Convex = 1  # FilletBuilderEnumContourMemberType
    Flush = 2  # FilletBuilderEnumContourMemberType
    Concave = 3  # FilletBuilderEnumContourMemberType
    
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
    


class FilletBuilderEnumSkipWeldMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumSkipWeldMethod():
    """
    the Skipweld enum. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NumberLength", " - "
       "NumberSpacing", " - "
       "SpacingLength", " - "
    """
    NumberLength = 0  # FilletBuilderEnumSkipWeldMethodMemberType
    NumberSpacing = 1  # FilletBuilderEnumSkipWeldMethodMemberType
    SpacingLength = 2  # FilletBuilderEnumSkipWeldMethodMemberType
    
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
    


class FilletBuilderEnumWeldingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumWeldingType():
    """
    the WeldingType enum. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "T", " - "
       "Lap", " - "
       "Corner", " - "
    """
    T = 0  # FilletBuilderEnumWeldingTypeMemberType
    Lap = 1  # FilletBuilderEnumWeldingTypeMemberType
    Corner = 2  # FilletBuilderEnumWeldingTypeMemberType
    
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
    


class FilletBuilderEnumFillFaceHolesTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FilletBuilderEnumFillFaceHolesType():
    """
    the fill method to be applied. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Set1", " - "
       "Set2", " - "
       "Both", " - "
    """
    NotSet = 0  # FilletBuilderEnumFillFaceHolesTypeMemberType
    Set1 = 1  # FilletBuilderEnumFillFaceHolesTypeMemberType
    Set2 = 2  # FilletBuilderEnumFillFaceHolesTypeMemberType
    Both = 3  # FilletBuilderEnumFillFaceHolesTypeMemberType
    
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
    


class FilletBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.Fillet` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateFilletBuilder`
    
    Default values.
    
    ===========================  ================================================
    Property                     Value
    ===========================  ================================================
    AddCosmeticEnd               0 
    ---------------------------  ------------------------------------------------
    AllowBroken                  0 
    ---------------------------  ------------------------------------------------
    AssignWeldPMI                0 
    ---------------------------  ------------------------------------------------
    Associative                  1 
    ---------------------------  ------------------------------------------------
    ContourHeight.Value          1.875 (millimeters part), .073818 (inches part) 
    ---------------------------  ------------------------------------------------
    ContourType                  None 
    ---------------------------  ------------------------------------------------
    EnumMethod                   NumberLength 
    ---------------------------  ------------------------------------------------
    ExtendEdges                  Manual 
    ---------------------------  ------------------------------------------------
    ExtensionDistance.Value      0.0254 (millimeters part), 0.001 (inches part) 
    ---------------------------  ------------------------------------------------
    ExtensionMethod              Automatic 
    ---------------------------  ------------------------------------------------
    FaceFillGapDistance          0.0 (millimeters part), 0.0 (inches part) 
    ---------------------------  ------------------------------------------------
    FieldWeld                    0 
    ---------------------------  ------------------------------------------------
    FillFaceHoles                None 
    ---------------------------  ------------------------------------------------
    FilletType                   T 
    ---------------------------  ------------------------------------------------
    FirstLeg.Value               6.25 (millimeters part), .246062 (inches part) 
    ---------------------------  ------------------------------------------------
    NumberOfWelds.Value          3 
    ---------------------------  ------------------------------------------------
    SecondLeg.Value              6.25 (millimeters part), .246062 (inches part) 
    ---------------------------  ------------------------------------------------
    SegmentLength.Value          3 (millimeters part), .118110 (inches part) 
    ---------------------------  ------------------------------------------------
    Spacing.Value                3 (millimeters part), .118110 (inches part) 
    ---------------------------  ------------------------------------------------
    ThroatThickToggle            0 
    ---------------------------  ------------------------------------------------
    ToggleCreateSkipWelds        0 
    ---------------------------  ------------------------------------------------
    ToggleRecreateDeletedWelds   0 
    ===========================  ================================================
    
    .. versionadded:: NX8.0.0
    """
    
    class EnumExtendEdges():
        """
        the options for populating the edge selections. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Manual", " - "
           "Automatic", " - "
        """
        Manual = 0  # FilletBuilderEnumExtendEdgesMemberType
        Automatic = 1  # FilletBuilderEnumExtendEdgesMemberType
        
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
        
    
    
    class EnumConstructionMethod():
        """
        the options for which construction method to use. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", " - "
           "RollAround", " - "
        """
        Default = 0  # FilletBuilderEnumConstructionMethodMemberType
        RollAround = 1  # FilletBuilderEnumConstructionMethodMemberType
        
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
        
    
    
    class EnumExtensionMethod():
        """
        the Extension enum. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Automatic", " - "
           "ByValue", " - "
        """
        Automatic = 0  # FilletBuilderEnumExtensionMethodMemberType
        ByValue = 1  # FilletBuilderEnumExtensionMethodMemberType
        
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
        
    
    
    class EnumContour():
        """
        the Contour enum. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Convex", " - "
           "Flush", " - "
           "Concave", " - "
        """
        NotSet = 0  # FilletBuilderEnumContourMemberType
        Convex = 1  # FilletBuilderEnumContourMemberType
        Flush = 2  # FilletBuilderEnumContourMemberType
        Concave = 3  # FilletBuilderEnumContourMemberType
        
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
        
    
    
    class EnumSkipWeldMethod():
        """
        the Skipweld enum. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NumberLength", " - "
           "NumberSpacing", " - "
           "SpacingLength", " - "
        """
        NumberLength = 0  # FilletBuilderEnumSkipWeldMethodMemberType
        NumberSpacing = 1  # FilletBuilderEnumSkipWeldMethodMemberType
        SpacingLength = 2  # FilletBuilderEnumSkipWeldMethodMemberType
        
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
        
    
    
    class EnumWeldingType():
        """
        the WeldingType enum. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "T", " - "
           "Lap", " - "
           "Corner", " - "
        """
        T = 0  # FilletBuilderEnumWeldingTypeMemberType
        Lap = 1  # FilletBuilderEnumWeldingTypeMemberType
        Corner = 2  # FilletBuilderEnumWeldingTypeMemberType
        
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
        
    
    
    class EnumFillFaceHolesType():
        """
        the fill method to be applied. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Set1", " - "
           "Set2", " - "
           "Both", " - "
        """
        NotSet = 0  # FilletBuilderEnumFillFaceHolesTypeMemberType
        Set1 = 1  # FilletBuilderEnumFillFaceHolesTypeMemberType
        Set2 = 2  # FilletBuilderEnumFillFaceHolesTypeMemberType
        Both = 3  # FilletBuilderEnumFillFaceHolesTypeMemberType
        
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
        
    
    AddCosmeticEnd: bool = ...
    """
    Returns or sets  the value identify if a cosmtic end should be added to each end of the fillet.  
    
    <hr>
    
    Getter Method
    
    Signature ``AddCosmeticEnd`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddCosmeticEnd`` 
    
    :param addCosmeticEnd: 
    :type addCosmeticEnd: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    AllowBroken: bool = ...
    """
    Returns or sets  the toggle to allow broken link.  
    
    <hr>
    
    Getter Method
    
    Signature ``AllowBroken`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowBroken`` 
    
    :param allowBroken: 
    :type allowBroken: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    AssignWeldPMI: bool = ...
    """
    Returns or sets  the toggle to assign weld pmi.  
    
    <hr>
    
    Getter Method
    
    Signature ``AssignWeldPMI`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssignWeldPMI`` 
    
    :param assignWeldPMI: 
    :type assignWeldPMI: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Associative: bool = ...
    """
    Returns or sets  the value identify if WAVE links should remain unbroken.  
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative: 
    :type associative: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ConstructionMethod: FilletBuilderEnumConstructionMethod = ...
    """
    Returns or sets  the value for determining the construction method.  
    
    Default method should be used for all conditions, unless you know the situation if for the roll around condition. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstructionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumConstructionMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstructionMethod`` 
    
    :param constructionMethod: 
    :type constructionMethod: :py:class:`NXOpen.Weld.FilletBuilderEnumConstructionMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ContourHeight: NXOpen.Expression = ...
    """
    Returns  the linear dimension contour height.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContourHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ContourType: FilletBuilderEnumContour = ...
    """
    Returns or sets  the contour.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContourType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumContour` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContourType`` 
    
    :param contour: 
    :type contour: :py:class:`NXOpen.Weld.FilletBuilderEnumContour` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DirectToggle: bool = ...
    """
    Returns or sets  the toggle to change direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectToggle`` 
    
    :param directToggle: 
    :type directToggle: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DirectionVector1: bool = ...
    """
    Returns or sets  the face normal direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionVector1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionVector1`` 
    
    :param directionVector1: 
    :type directionVector1: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DirectionVector2: bool = ...
    """
    Returns or sets  the face normal direction for the second face.  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionVector2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionVector2`` 
    
    :param directionVector2: 
    :type directionVector2: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistTolerance: float = ...
    """
    Returns or sets  the distance tolerance.  
    
    <hr>
    
    Getter Method
    
    Signature ``DistTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistTolerance`` 
    
    :param distTolerance: 
    :type distTolerance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EdgeSet1: NXOpen.Section = ...
    """
    Returns  the edge set1.  
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeSet1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    EdgeSet2: NXOpen.Section = ...
    """
    Returns  the edge set2.  
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeSet2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    EndDist: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the on path dimension end distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndDist`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    EndVector: bool = ...
    """
    Returns or sets  the end direction reversed or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndVector`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndVector`` 
    
    :param endVector: 
    :type endVector: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EnumMethod: FilletBuilderEnumSkipWeldMethod = ...
    """
    Returns or sets  the enum method for skip welds.  
    
    <hr>
    
    Getter Method
    
    Signature ``EnumMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumSkipWeldMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EnumMethod`` 
    
    :param enumMethod: 
    :type enumMethod: :py:class:`NXOpen.Weld.FilletBuilderEnumSkipWeldMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtendEdges: FilletBuilderEnumExtendEdges = ...
    """
    Returns or sets  the value for how to populate the edge sets.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumExtendEdges` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendEdges`` 
    
    :param extendEdges: 
    :type extendEdges: :py:class:`NXOpen.Weld.FilletBuilderEnumExtendEdges` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtensionDistance: NXOpen.Expression = ...
    """
    Returns  the linear dimension extension distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtensionDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ExtensionMethod: FilletBuilderEnumExtensionMethod = ...
    """
    Returns or sets  the extension method.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtensionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumExtensionMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtensionMethod`` 
    
    :param extensionMethod: 
    :type extensionMethod: :py:class:`NXOpen.Weld.FilletBuilderEnumExtensionMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceFillGapDistance: float = ...
    """
    Returns or sets  the distance the fillet will span when there are gaps in the sheet definition.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceFillGapDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceFillGapDistance`` 
    
    :param faceFillGapDistance: 
    :type faceFillGapDistance: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceSet1: NXOpen.ScCollector = ...
    """
    Returns  the face set1.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FaceSet2: NXOpen.ScCollector = ...
    """
    Returns  the face set2.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FieldWeld: bool = ...
    """
    Returns or sets  the field weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``FieldWeld`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FieldWeld`` 
    
    :param fieldWeld: 
    :type fieldWeld: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FillFaceHoles: FilletBuilderEnumFillFaceHolesType = ...
    """
    Returns or sets  the value to identify if the face set should be filled during construction.  
    
    Only holes fully bounded by a single face will be filled. 
    
    <hr>
    
    Getter Method
    
    Signature ``FillFaceHoles`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumFillFaceHolesType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillFaceHoles`` 
    
    :param fillFaceHolesType: 
    :type fillFaceHolesType: :py:class:`NXOpen.Weld.FilletBuilderEnumFillFaceHolesType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FilletType: FilletBuilderEnumWeldingType = ...
    """
    Returns or sets  the fillet type.  
    
    <hr>
    
    Getter Method
    
    Signature ``FilletType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.FilletBuilderEnumWeldingType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilletType`` 
    
    :param filletType: 
    :type filletType: :py:class:`NXOpen.Weld.FilletBuilderEnumWeldingType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FirstLeg: NXOpen.Expression = ...
    """
    Returns  the linear dimension first leg.  
    
    <hr>
    
    Getter Method
    
    Signature ``FirstLeg`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    NumberOfWelds: NXOpen.Expression = ...
    """
    Returns  the expression number indicates number of welds in skip welds.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfWelds`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Pmi: NXOpen.NXObject = ...
    """
    Returns or sets  the pmi symbol.  
    
    <hr>
    
    Getter Method
    
    Signature ``Pmi`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Pmi`` 
    
    :param pmi: 
    :type pmi: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SecondLeg: NXOpen.Expression = ...
    """
    Returns  the linear dimension second leg.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondLeg`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SeedFace1: NXOpen.Face = ...
    """
    Returns or sets  the first seed face.  
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace1`` 
    
    :param seedFace1: 
    :type seedFace1: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedFace2: NXOpen.Face = ...
    """
    Returns or sets  the second seed face.  
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace2`` 
    
    :param seedFace2: 
    :type seedFace2: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedPoint1: NXOpen.Point3d = ...
    """
    Returns or sets  the point on the first face.  
    
    <hr>
    
    Getter Method
    
    Signature ``SeedPoint1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedPoint1`` 
    
    :param seedPoint1: 
    :type seedPoint1: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedPoint2: NXOpen.Point3d = ...
    """
    Returns or sets  the point on the second face.  
    
    <hr>
    
    Getter Method
    
    Signature ``SeedPoint2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedPoint2`` 
    
    :param seedPoint1: 
    :type seedPoint1: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SegmentLength: NXOpen.Expression = ...
    """
    Returns  the linear dimension length indicates segment length for each weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Spacing: NXOpen.Expression = ...
    """
    Returns  the linear dimension spacing indicates distance between each weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    StartDist: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the on path dimension start distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartDist`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    StartVector: bool = ...
    """
    Returns or sets  the start direction reversed or not.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartVector`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartVector`` 
    
    :param startVector: 
    :type startVector: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ThroatThickToggle: bool = ...
    """
    Returns or sets  the toggle throat thickness.  
    
    <hr>
    
    Getter Method
    
    Signature ``ThroatThickToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ThroatThickToggle`` 
    
    :param throatThickToggle: 
    :type throatThickToggle: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ToggleCreateSkipWelds: bool = ...
    """
    Returns or sets  the toggle to create skip welds.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToggleCreateSkipWelds`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToggleCreateSkipWelds`` 
    
    :param toggleCreateSkipWelds: 
    :type toggleCreateSkipWelds: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ToggleRecreateDeletedWelds: bool = ...
    """
    Returns or sets  the toggle to recreate deleted welds.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToggleRecreateDeletedWelds`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToggleRecreateDeletedWelds`` 
    
    :param toggleRecreateDeletedWelds: 
    :type toggleRecreateDeletedWelds: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Uparameter1: float = ...
    """
    Returns or sets  the u parameter for first face.  
    
    <hr>
    
    Getter Method
    
    Signature ``Uparameter1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Uparameter1`` 
    
    :param u1: 
    :type u1: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: ugweld ("UG WELD")
    """
    Uparameter2: float = ...
    """
    Returns or sets  the u parameter for second face.  
    
    <hr>
    
    Getter Method
    
    Signature ``Uparameter2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Uparameter2`` 
    
    :param u2: 
    :type u2: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: ugweld ("UG WELD")
    """
    Vparameter1: float = ...
    """
    Returns or sets  the v parameter for first face.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vparameter1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vparameter1`` 
    
    :param v1: 
    :type v1: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: ugweld ("UG WELD")
    """
    Vparameter2: float = ...
    """
    Returns or sets  the v parameter for second face.  
    
    <hr>
    
    Getter Method
    
    Signature ``Vparameter2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Vparameter2`` 
    
    :param v2: 
    :type v2: float 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX10.0.0
       Removed with no replacement.
    
    License requirements: ugweld ("UG WELD")
    """
    WeldingCharacteristics: CharacteristicsBuilder = ...
    """
    Returns  the welding characteristics.  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldingCharacteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: FilletBuilder = ...  # unknown typename


class WeldObjectBuilderCommandNameMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldObjectBuilderCommandName():
    """
    Commands that a callback will be invoked after dialog completion. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No command. Used to initialize value."
       "Groove", "Groove Weld command"
       "Fillet", "Fillet Weld command"
       "UserDefined", "User Defined Weld command"
       "WeldPoint", "Weld Point command"
       "Bead", "Bead command"
       "Fill", "Fill command"
       "ImportCsv", "Import CSV command"
       "EasySpot", "Easy Spot command"
       "DatumLocator", "Datum Locator command"
       "MeasurementLocator", "Measurement Locator command"
       "EasyMeasurementPattern", "Easy Measurement Pattern command"
       "PlugSlot", "Plug Slot command"
       "Joint", "Welding Joint command"
       "DatumSurface", "Datum Surface command"
       "DatumPin", "Datum Pin command"
       "SurfaceWeld", "Surface Weld command"
       "Compound", "Compound Weld command"
       "WeldAttribute", "Edit Weld Attribute"
       "JointDefinition", "Edit Joint Definition Parameters"
       "Jointmark", "Joint Mark command"
       "WeldPointWizard", "Weld Point Wizard command"
       "Transform", "Weld Transform command"
    """
    NotSet = 0  # WeldObjectBuilderCommandNameMemberType
    Groove = 1  # WeldObjectBuilderCommandNameMemberType
    Fillet = 2  # WeldObjectBuilderCommandNameMemberType
    UserDefined = 3  # WeldObjectBuilderCommandNameMemberType
    WeldPoint = 4  # WeldObjectBuilderCommandNameMemberType
    Bead = 5  # WeldObjectBuilderCommandNameMemberType
    Fill = 6  # WeldObjectBuilderCommandNameMemberType
    ImportCsv = 7  # WeldObjectBuilderCommandNameMemberType
    EasySpot = 8  # WeldObjectBuilderCommandNameMemberType
    DatumLocator = 9  # WeldObjectBuilderCommandNameMemberType
    MeasurementLocator = 10  # WeldObjectBuilderCommandNameMemberType
    EasyMeasurementPattern = 11  # WeldObjectBuilderCommandNameMemberType
    PlugSlot = 12  # WeldObjectBuilderCommandNameMemberType
    Joint = 13  # WeldObjectBuilderCommandNameMemberType
    DatumSurface = 14  # WeldObjectBuilderCommandNameMemberType
    DatumPin = 15  # WeldObjectBuilderCommandNameMemberType
    SurfaceWeld = 16  # WeldObjectBuilderCommandNameMemberType
    Compound = 17  # WeldObjectBuilderCommandNameMemberType
    WeldAttribute = 18  # WeldObjectBuilderCommandNameMemberType
    JointDefinition = 19  # WeldObjectBuilderCommandNameMemberType
    Jointmark = 20  # WeldObjectBuilderCommandNameMemberType
    WeldPointWizard = 21  # WeldObjectBuilderCommandNameMemberType
    Transform = 22  # WeldObjectBuilderCommandNameMemberType
    
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
    


class WeldObjectBuilderFeatureInfo_Struct():
    """
    Structure used to identify if each feature is newly created or edited.  
    
    .
    Constructor: 
    NXOpen.Weld.WeldObjectBuilder.FeatureInfo()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Feature: NXOpen.Features.Feature = ...
    """
    the newly created or edited feature 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Features.Feature`
    """
    IsNewlyCreated: bool = ...
    """
    true if a new feature, false if an existing feature was edited.  
    
    <hr>
    
    Field Value
    Type:bool
    """


class WeldObjectBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.WeldObjectBuilder` class used to collect welding objects created or edited from a command.  
    
    .. versionadded:: NX8.0.1
    """
    
    class CommandName():
        """
        Commands that a callback will be invoked after dialog completion. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No command. Used to initialize value."
           "Groove", "Groove Weld command"
           "Fillet", "Fillet Weld command"
           "UserDefined", "User Defined Weld command"
           "WeldPoint", "Weld Point command"
           "Bead", "Bead command"
           "Fill", "Fill command"
           "ImportCsv", "Import CSV command"
           "EasySpot", "Easy Spot command"
           "DatumLocator", "Datum Locator command"
           "MeasurementLocator", "Measurement Locator command"
           "EasyMeasurementPattern", "Easy Measurement Pattern command"
           "PlugSlot", "Plug Slot command"
           "Joint", "Welding Joint command"
           "DatumSurface", "Datum Surface command"
           "DatumPin", "Datum Pin command"
           "SurfaceWeld", "Surface Weld command"
           "Compound", "Compound Weld command"
           "WeldAttribute", "Edit Weld Attribute"
           "JointDefinition", "Edit Joint Definition Parameters"
           "Jointmark", "Joint Mark command"
           "WeldPointWizard", "Weld Point Wizard command"
           "Transform", "Weld Transform command"
        """
        NotSet = 0  # WeldObjectBuilderCommandNameMemberType
        Groove = 1  # WeldObjectBuilderCommandNameMemberType
        Fillet = 2  # WeldObjectBuilderCommandNameMemberType
        UserDefined = 3  # WeldObjectBuilderCommandNameMemberType
        WeldPoint = 4  # WeldObjectBuilderCommandNameMemberType
        Bead = 5  # WeldObjectBuilderCommandNameMemberType
        Fill = 6  # WeldObjectBuilderCommandNameMemberType
        ImportCsv = 7  # WeldObjectBuilderCommandNameMemberType
        EasySpot = 8  # WeldObjectBuilderCommandNameMemberType
        DatumLocator = 9  # WeldObjectBuilderCommandNameMemberType
        MeasurementLocator = 10  # WeldObjectBuilderCommandNameMemberType
        EasyMeasurementPattern = 11  # WeldObjectBuilderCommandNameMemberType
        PlugSlot = 12  # WeldObjectBuilderCommandNameMemberType
        Joint = 13  # WeldObjectBuilderCommandNameMemberType
        DatumSurface = 14  # WeldObjectBuilderCommandNameMemberType
        DatumPin = 15  # WeldObjectBuilderCommandNameMemberType
        SurfaceWeld = 16  # WeldObjectBuilderCommandNameMemberType
        Compound = 17  # WeldObjectBuilderCommandNameMemberType
        WeldAttribute = 18  # WeldObjectBuilderCommandNameMemberType
        JointDefinition = 19  # WeldObjectBuilderCommandNameMemberType
        Jointmark = 20  # WeldObjectBuilderCommandNameMemberType
        WeldPointWizard = 21  # WeldObjectBuilderCommandNameMemberType
        Transform = 22  # WeldObjectBuilderCommandNameMemberType
        
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
        
    
    
    class FeatureInfo():
        """
        Structure used to identify if each feature is newly created or edited.  
        
        .
        Constructor: 
        NXOpen.Weld.WeldObjectBuilder.FeatureInfo()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Feature: NXOpen.Features.Feature = ...
        """
        the newly created or edited feature 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Features.Feature`
        """
        IsNewlyCreated: bool = ...
        """
        true if a new feature, false if an existing feature was edited.  
        
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def GetFeatureInformation(self) -> 'list[WeldObjectBuilderFeatureInfo_Struct]':
        """
        Gets the created and modifed features 
        
        Signature ``GetFeatureInformation()`` 
        
        :returns:  features created or edited  
        :rtype: list of :py:class:`NXOpen.Weld.WeldObjectBuilderFeatureInfo_Struct` 
        
        .. versionadded:: NX8.0.1
        
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
    
    CommandUsed: WeldObjectBuilderCommandName = ...
    """
    Returns  the command name that was last used to create or modify features 
    
    <hr>
    
    Getter Method
    
    Signature ``CommandUsed`` 
    
    :returns:  command name used  
    :rtype: :py:class:`NXOpen.Weld.WeldObjectBuilderCommandName` 
    
    .. versionadded:: NX8.0.1
    
    License requirements: None.
    """
    Null: WeldObjectBuilder = ...  # unknown typename


class SelectDatumPin(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a single object selection.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def SetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumPin) -> None:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumPin` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumPin) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumPin` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumPin, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
        The object being selected with the object's view and object's point
        
        Signature ``SetValue(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumPin` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: DatumPin, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DatumPin, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``SetValue(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Weld.DatumPin` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1:  first selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Weld.DatumPin` 
        :param view2:  second selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumPin, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> None:
        """
        The object being selected with CAE set object information.
        
        Signature ``SetValue(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumPin` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.SetValue`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def GetValue(self) -> DatumPin:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :returns:  selected object  
        :rtype: :py:class:`NXOpen.Weld.DatumPin` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self, selection: DatumPin) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumPin` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the object's view and point.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, view, point). selection is a :py:class:`NXOpen.Weld.DatumPin`.   selected object view is a :py:class:`NXOpen.View`.   selected object viewpoint is a :py:class:`NXOpen.Point3d`.   selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the objects view and point and snap information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (snapType, selection1, view1, point1, selection2, view2, point2). snapType is a :py:class:`NXOpen.InferSnapTypeSnapType`.    snap point typeselection1 is a :py:class:`NXOpen.Weld.DatumPin`.   first selected object view1 is a :py:class:`NXOpen.View`.   first selected object viewpoint1 is a :py:class:`NXOpen.Point3d`.   first selected object pointselection2 is a :py:class:`NXOpen.Weld.DatumPin`.   second selected object view2 is a :py:class:`NXOpen.View`.   second selected object viewpoint2 is a :py:class:`NXOpen.Point3d`.   second selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with CAE set object information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, caeSubType, caeSubId). selection is a :py:class:`NXOpen.Weld.DatumPin`.   selected object caeSubType is a :py:class:`NXOpen.CaeObjectTypeCaeSubType`.   CAE set object sub typecaeSubId is a int.   CAE set object sub id
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.GetValue`.
        
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
    
    Value: DatumPin = ...
    """
    Returns or sets  the object being selected
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns:  selected object  
    :rtype: :py:class:`NXOpen.Weld.DatumPin` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param selection:  selected object  
    :type selection: :py:class:`NXOpen.Weld.DatumPin` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectDatumPin = ...  # unknown typename


class JointmarkFaceSetsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Used to create or edit a set of faces for Jointmark   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.JointmarkBuilder.NewFaceSets`
    
    .. versionadded:: NX9.0.0
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
    
    FaceSelect: NXOpen.ScCollector = ...
    """
    Returns  the selected face collector 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSelect`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: JointmarkFaceSetsBuilder = ...  # unknown typename


class CompoundWeldBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.CompoundWeld` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateCompoundWeldBuilder`
    
    .. versionadded:: NX9.0.0
    """
    Side1Welds: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the weld features defining side 1 of the compound weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``Side1Welds`` 
    
    :returns:  Weld Features  
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Side2Welds: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the weld features defining side 2 of the compound weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``Side2Welds`` 
    
    :returns:  Weld Features  
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: CompoundWeldBuilder = ...  # unknown typename


class WeldPointExitBuilderCommandNameMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointExitBuilderCommandName():
    """
    The command name used for the newly created features. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No command. Used to initialize value."
       "WeldPoint", "Weld Point command"
       "DatumLocator", "Datum Locator command"
       "MeasurementLocator", "Measurement Locator command"
       "Jointmark", "Joint Mark command"
       "WeldPointWizard", "Weld Point Wizard command"
    """
    NotSet = 0  # WeldPointExitBuilderCommandNameMemberType
    WeldPoint = 1  # WeldPointExitBuilderCommandNameMemberType
    DatumLocator = 2  # WeldPointExitBuilderCommandNameMemberType
    MeasurementLocator = 3  # WeldPointExitBuilderCommandNameMemberType
    Jointmark = 4  # WeldPointExitBuilderCommandNameMemberType
    WeldPointWizard = 5  # WeldPointExitBuilderCommandNameMemberType
    
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
    


class WeldPointExitBuilderMethodUsedMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointExitBuilderMethodUsed():
    """
    The method use to create the features. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No method specified. Used to initialize value."
       "Mirror", "Feature was created using the mirror method."
       "Translate", "Feature was created using the translate method."
       "GuideCurve", "Feature was created using the guide curves method."
       "Points", "Feature was created using the points method."
       "GuideCurveMovedOff", "Feature was created using the guide curves method, but user moved it off."
    """
    NotSet = 0  # WeldPointExitBuilderMethodUsedMemberType
    Mirror = 1  # WeldPointExitBuilderMethodUsedMemberType
    Translate = 2  # WeldPointExitBuilderMethodUsedMemberType
    GuideCurve = 3  # WeldPointExitBuilderMethodUsedMemberType
    Points = 4  # WeldPointExitBuilderMethodUsedMemberType
    GuideCurveMovedOff = 5  # WeldPointExitBuilderMethodUsedMemberType
    
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
    


class WeldPointExitBuilderFeatureInfo_Struct():
    """
    Structure used to identify newly created features.  
    
    .
    Constructor: 
    NXOpen.Weld.WeldPointExitBuilder.FeatureInfo()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Feature: NXOpen.Features.Feature = ...
    """
    the newly created or edited feature 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Features.Feature`
    """
    MethodUsed: WeldPointExitBuilderMethodUsed = ...
    """
    the method used to create the feature 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Weld.WeldPointExitBuilderMethodUsed`
    """
    Parent: NXOpen.Features.Feature = ...
    """
    the parent if method used was mirror or translate 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Features.Feature`
    """
    IsNewlyCreated: bool = ...
    """
    true if a new feature, false if an existing feature was edited.  
    
    <hr>
    
    Field Value
    Type:bool
    """


class WeldPointExitBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.WeldPointExitBuilder` class used to pass welding object from the Weld Point command to a user callback.  
    
    This object is not used on edit. 
    
    .. versionadded:: NX8.0.2
    """
    
    class CommandName():
        """
        The command name used for the newly created features. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No command. Used to initialize value."
           "WeldPoint", "Weld Point command"
           "DatumLocator", "Datum Locator command"
           "MeasurementLocator", "Measurement Locator command"
           "Jointmark", "Joint Mark command"
           "WeldPointWizard", "Weld Point Wizard command"
        """
        NotSet = 0  # WeldPointExitBuilderCommandNameMemberType
        WeldPoint = 1  # WeldPointExitBuilderCommandNameMemberType
        DatumLocator = 2  # WeldPointExitBuilderCommandNameMemberType
        MeasurementLocator = 3  # WeldPointExitBuilderCommandNameMemberType
        Jointmark = 4  # WeldPointExitBuilderCommandNameMemberType
        WeldPointWizard = 5  # WeldPointExitBuilderCommandNameMemberType
        
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
        
    
    
    class MethodUsed():
        """
        The method use to create the features. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No method specified. Used to initialize value."
           "Mirror", "Feature was created using the mirror method."
           "Translate", "Feature was created using the translate method."
           "GuideCurve", "Feature was created using the guide curves method."
           "Points", "Feature was created using the points method."
           "GuideCurveMovedOff", "Feature was created using the guide curves method, but user moved it off."
        """
        NotSet = 0  # WeldPointExitBuilderMethodUsedMemberType
        Mirror = 1  # WeldPointExitBuilderMethodUsedMemberType
        Translate = 2  # WeldPointExitBuilderMethodUsedMemberType
        GuideCurve = 3  # WeldPointExitBuilderMethodUsedMemberType
        Points = 4  # WeldPointExitBuilderMethodUsedMemberType
        GuideCurveMovedOff = 5  # WeldPointExitBuilderMethodUsedMemberType
        
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
        
    
    
    class FeatureInfo():
        """
        Structure used to identify newly created features.  
        
        .
        Constructor: 
        NXOpen.Weld.WeldPointExitBuilder.FeatureInfo()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Feature: NXOpen.Features.Feature = ...
        """
        the newly created or edited feature 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Features.Feature`
        """
        MethodUsed: WeldPointExitBuilderMethodUsed = ...
        """
        the method used to create the feature 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Weld.WeldPointExitBuilderMethodUsed`
        """
        Parent: NXOpen.Features.Feature = ...
        """
        the parent if method used was mirror or translate 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Features.Feature`
        """
        IsNewlyCreated: bool = ...
        """
        true if a new feature, false if an existing feature was edited.  
        
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    def GetFeatureInformation(self) -> 'list[WeldPointExitBuilderFeatureInfo_Struct]':
        """
        Gets the information for the newly created features.  
        
        Signature ``GetFeatureInformation()`` 
        
        :returns:  features created  
        :rtype: list of :py:class:`NXOpen.Weld.WeldPointExitBuilderFeatureInfo_Struct` 
        
        .. versionadded:: NX8.0.2
        
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
    
    CommandUsed: WeldPointExitBuilderCommandName = ...
    """
    Returns  the command name that was last used to create features.  
    
    This callback is not called on edit. 
    
    <hr>
    
    Getter Method
    
    Signature ``CommandUsed`` 
    
    :returns:  command name used  
    :rtype: :py:class:`NXOpen.Weld.WeldPointExitBuilderCommandName` 
    
    .. versionadded:: NX8.0.2
    
    License requirements: None.
    """
    Null: WeldPointExitBuilder = ...  # unknown typename


class WeldOverlapStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldOverlapStatus():
    """
    the create status for overlap 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Invalid", "invalid status"
       "Creation", "create overlap"
       "NonCreation", "don't create overlap"
    """
    Invalid = -1  # WeldOverlapStatusMemberType
    Creation = 0  # WeldOverlapStatusMemberType
    NonCreation = 1  # WeldOverlapStatusMemberType
    
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
    


class WeldDatumControlDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldDatumControlDirection():
    """
    the control direction for datum 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Invalid", "Invalid direction"
       "X", "X direction"
       "Y", "Y direction"
       "Z", "Z direction"
    """
    Invalid = -1  # WeldDatumControlDirectionMemberType
    X = 0  # WeldDatumControlDirectionMemberType
    Y = 1  # WeldDatumControlDirectionMemberType
    Z = 2  # WeldDatumControlDirectionMemberType
    
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
    


class WeldGroupIdColorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGroupIdColor():
    """
    the group id color indexes 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None group id color"
       "First", "First Group Id Color Index"
       "Second", "Second Group Id Color Index"
       "Third", "Third Group Id Color Index"
       "Fourth", "Fourth Group Id Color Index"
       "Fifth", "Fifth Group Id Color Index"
       "Sixth", "Sixth Group Id Color Index"
       "Seventh", "Seventh Group Id Color Index"
       "Eighth", "Eighth Group Id Color Index"
       "Ninth", "Ninth Group Id Color Index"
       "Tenth", "Tenth Group Id Color Index"
       "Eleventh", "Eleventh Group Id Color Index"
       "Twelfth", "Twelvth Group Id Color Index"
       "Thirteenth", "Thirteenth Group Id Color Index"
       "Fourteenth", "Fourteenth Group Id Color Index"
    """
    NotSet = 0  # WeldGroupIdColorMemberType
    First = 1  # WeldGroupIdColorMemberType
    Second = 2  # WeldGroupIdColorMemberType
    Third = 3  # WeldGroupIdColorMemberType
    Fourth = 4  # WeldGroupIdColorMemberType
    Fifth = 5  # WeldGroupIdColorMemberType
    Sixth = 6  # WeldGroupIdColorMemberType
    Seventh = 7  # WeldGroupIdColorMemberType
    Eighth = 8  # WeldGroupIdColorMemberType
    Ninth = 9  # WeldGroupIdColorMemberType
    Tenth = 10  # WeldGroupIdColorMemberType
    Eleventh = 11  # WeldGroupIdColorMemberType
    Twelfth = 12  # WeldGroupIdColorMemberType
    Thirteenth = 13  # WeldGroupIdColorMemberType
    Fourteenth = 14  # WeldGroupIdColorMemberType
    
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
    


class IFeature(NXOpen.INXObject):
    """
    Represents a Weld Assistant or Structure Welding created feature   
    
    .. versionadded:: NX11.0.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class WeldBead(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a Weld Bead feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.WeldBeadBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: WeldBead = ...  # unknown typename


class WeldBeadSizeBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[WeldBeadSizeBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: WeldBeadSizeBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
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
    
    
    def FindIndex(self, obj: WeldBeadSizeBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> WeldBeadSizeBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
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
    def Erase(self, obj: WeldBeadSizeBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: WeldBeadSizeBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
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
    
    
    def GetContents(self) -> 'list[WeldBeadSizeBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[WeldBeadSizeBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
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
    def Swap(self, object1: WeldBeadSizeBuilder, object2: WeldBeadSizeBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: WeldBeadSizeBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
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
    Null: WeldBeadSizeBuilderList = ...  # unknown typename


class UserDefinedWeld(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a User Defined Weld feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.UserDefinedWeldBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: UserDefinedWeld = ...  # unknown typename


class ConnectedPart(NXOpen.TransientObject):
    """
    Represents weld connected part to customize the retrieval of connected part information.  
    
    .. versionadded:: NX11.0.0
    """
    
    def Dispose(self) -> None:
        """
        Free resources associated with the instance.  
        
        After this method
        is called, it is illegal to use the object.  In .NET, this method
        is automatically called when the object is deleted by the garbage
        collector. 
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberSets(self) -> int:
        """
        Get the number of connected sets.  
        
        Use this to limit the number of iterations when calling :py:meth:`NXOpen.Weld.ConnectedPart.GetSetInformation`.  
        
        Signature ``GetNumberSets()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSetInformation(self, setIndex: int) -> 'list[NXOpen.NXObject]':
        """
        Get the individual connected set data.  
        
        Signature ``GetSetInformation(setIndex)`` 
        
        :param setIndex:  Index of set to gather information for  
        :type setIndex: int 
        :returns:  Array of connected set information. Should be freed. 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    


class WeldRootUpdateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldRootUpdate():
    """
    Arc process type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Automatic", "Automatically compute the root opening"
       "NotSet", "Use user specified root opening"
    """
    Automatic = 0  # WeldRootUpdateMemberType
    NotSet = 1  # WeldRootUpdateMemberType
    
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
    


class StructureWeldBuilder(NXOpen.Builder):
    """
    This class is used to create or edit the information shared among all Structure Weld builders.  
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetCommittedComponents(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        This method returns the component parts that are created by  :py:meth:`Builder.Commit`.  
        
        Signature ``GetCommittedComponents()`` 
        
        :returns:  The components created by Commit  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    Null: StructureWeldBuilder = ...  # unknown typename


class WeldJointBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderTypes():
    """
    Creation method. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CreateAutomatic", "Automatic weld joint creation."
       "CreateManual", "Manual weld joint creation."
       "CreateMultiple", "Create multiple weld joints from manual input."
       "CreateAttributes", "Create weld joints from attributed ship structures data."
    """
    CreateAutomatic = 0  # WeldJointBuilderTypesMemberType
    CreateManual = 1  # WeldJointBuilderTypesMemberType
    CreateMultiple = 2  # WeldJointBuilderTypesMemberType
    CreateAttributes = 3  # WeldJointBuilderTypesMemberType
    
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
    


class WeldJointBuilderWeldTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderWeldTypes():
    """
    Weld types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Any", "Any Joint type."
       "Groove", "Groove joint."
       "Fillet", "T-Joint."
       "Corner", "Corner joint."
       "Lap", "Lap joint."
       "Socket", "Socket joint for pipe welding."
       "Mechanical", "Mechanical joint for pipe welding."
       "Sleeve", "Sleeve joint for pipe welding."
       "Boss", "Boss joint for pipe welding."
    """
    Any = 0  # WeldJointBuilderWeldTypesMemberType
    Groove = 1  # WeldJointBuilderWeldTypesMemberType
    Fillet = 2  # WeldJointBuilderWeldTypesMemberType
    Corner = 3  # WeldJointBuilderWeldTypesMemberType
    Lap = 4  # WeldJointBuilderWeldTypesMemberType
    Socket = 5  # WeldJointBuilderWeldTypesMemberType
    Mechanical = 6  # WeldJointBuilderWeldTypesMemberType
    Sleeve = 7  # WeldJointBuilderWeldTypesMemberType
    Boss = 8  # WeldJointBuilderWeldTypesMemberType
    
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
    


class WeldJointBuilderDestinationTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderDestinationTypes():
    """
    Where to create new joints. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WorkPart", "Create new joints in work part."
       "NewComponent", "Create a new componenent for each joint under the work part."
    """
    WorkPart = 0  # WeldJointBuilderDestinationTypesMemberType
    NewComponent = 1  # WeldJointBuilderDestinationTypesMemberType
    
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
    


class WeldJointBuilderSplitTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderSplitTypes():
    """
    Joint splitting options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EqualSegments", "Specified number of equal segments."
       "Limits", "At limits defined by :py:meth:`NXOpen.Weld.WeldJointBuilder.LimitList`."
       "Angle", "At specifed angle."
       "ComputedAngle", "At angle computed from geometry and tables."
       "Length", "At equal arc length."
       "NotSet", "No split."
       "Skip", "Skip joint."
    """
    EqualSegments = 0  # WeldJointBuilderSplitTypesMemberType
    Limits = 1  # WeldJointBuilderSplitTypesMemberType
    Angle = 2  # WeldJointBuilderSplitTypesMemberType
    ComputedAngle = 3  # WeldJointBuilderSplitTypesMemberType
    Length = 4  # WeldJointBuilderSplitTypesMemberType
    NotSet = 5  # WeldJointBuilderSplitTypesMemberType
    Skip = 6  # WeldJointBuilderSplitTypesMemberType
    
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
    


class WeldJointBuilderJointMidPointData_Struct():
    """
    Joint evaluation information at the mid point.  
    
    Results are returned in absolute and ship coordinates .
    Constructor: 
    NXOpen.Weld.WeldJointBuilder.JointMidPointData()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    JointMidPoint: NXOpen.Point3d = ...
    """
    The mid point of the joint in absolute coordinates.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Point3d`
    """
    JointTangent: NXOpen.Vector3d = ...
    """
    The tangent at the joint mid point in absolute coordinates.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    PrimaryFaceNormal: NXOpen.Vector3d = ...
    """
    The primary body face normal in absolute coordinates at the joint mid point.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    SecondaryFaceNormal: NXOpen.Vector3d = ...
    """
    The secondary body face normal in absolute coordinates at the joint mid point.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    GroovePrimaryDirection: NXOpen.Vector3d = ...
    """
    The direction in absolute coordinates towards the primary faces, and way from secondary faces.  
    
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Vector3d`
    """
    GrooveAlignedWithPrimary: bool = ...
    """
    Indicates if the primary faces for the groove are farthest along a positive principal axis.  
    
    <hr>
    
    Field Value
    Type:bool
    """


class WeldJointBuilderCoordinateSystemMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderCoordinateSystem():
    """
    Coordinate system specification. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Absolute", "Desired points and vectors should be in absolute coordinates."
       "Ship", "Desired points and vectors should be in ship coordinate system."
    """
    Absolute = 0  # WeldJointBuilderCoordinateSystemMemberType
    Ship = 1  # WeldJointBuilderCoordinateSystemMemberType
    
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
    


class WeldJointBuilderApplicationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldJointBuilderApplication():
    """
    Application where joints are created. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "StructureWelding", "Structure Welding Application."
       "Routing", "Routing Application."
    """
    StructureWelding = 0  # WeldJointBuilderApplicationMemberType
    Routing = 1  # WeldJointBuilderApplicationMemberType
    
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
    


class WeldJointBuilder(StructureWeldBuilder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateJointBuilder`
    
    Default values.
    
    ===============  =====
    Property         Value
    ===============  =====
    NumberSegments   2 
    ---------------  -----
    SplitAngle       5.0 
    ===============  =====
    
    .. versionadded:: NX8.0.0
    """
    
    class Types():
        """
        Creation method. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CreateAutomatic", "Automatic weld joint creation."
           "CreateManual", "Manual weld joint creation."
           "CreateMultiple", "Create multiple weld joints from manual input."
           "CreateAttributes", "Create weld joints from attributed ship structures data."
        """
        CreateAutomatic = 0  # WeldJointBuilderTypesMemberType
        CreateManual = 1  # WeldJointBuilderTypesMemberType
        CreateMultiple = 2  # WeldJointBuilderTypesMemberType
        CreateAttributes = 3  # WeldJointBuilderTypesMemberType
        
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
        
    
    
    class WeldTypes():
        """
        Weld types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Any", "Any Joint type."
           "Groove", "Groove joint."
           "Fillet", "T-Joint."
           "Corner", "Corner joint."
           "Lap", "Lap joint."
           "Socket", "Socket joint for pipe welding."
           "Mechanical", "Mechanical joint for pipe welding."
           "Sleeve", "Sleeve joint for pipe welding."
           "Boss", "Boss joint for pipe welding."
        """
        Any = 0  # WeldJointBuilderWeldTypesMemberType
        Groove = 1  # WeldJointBuilderWeldTypesMemberType
        Fillet = 2  # WeldJointBuilderWeldTypesMemberType
        Corner = 3  # WeldJointBuilderWeldTypesMemberType
        Lap = 4  # WeldJointBuilderWeldTypesMemberType
        Socket = 5  # WeldJointBuilderWeldTypesMemberType
        Mechanical = 6  # WeldJointBuilderWeldTypesMemberType
        Sleeve = 7  # WeldJointBuilderWeldTypesMemberType
        Boss = 8  # WeldJointBuilderWeldTypesMemberType
        
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
        
    
    
    class DestinationTypes():
        """
        Where to create new joints. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WorkPart", "Create new joints in work part."
           "NewComponent", "Create a new componenent for each joint under the work part."
        """
        WorkPart = 0  # WeldJointBuilderDestinationTypesMemberType
        NewComponent = 1  # WeldJointBuilderDestinationTypesMemberType
        
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
        
    
    
    class SplitTypes():
        """
        Joint splitting options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "EqualSegments", "Specified number of equal segments."
           "Limits", "At limits defined by :py:meth:`NXOpen.Weld.WeldJointBuilder.LimitList`."
           "Angle", "At specifed angle."
           "ComputedAngle", "At angle computed from geometry and tables."
           "Length", "At equal arc length."
           "NotSet", "No split."
           "Skip", "Skip joint."
        """
        EqualSegments = 0  # WeldJointBuilderSplitTypesMemberType
        Limits = 1  # WeldJointBuilderSplitTypesMemberType
        Angle = 2  # WeldJointBuilderSplitTypesMemberType
        ComputedAngle = 3  # WeldJointBuilderSplitTypesMemberType
        Length = 4  # WeldJointBuilderSplitTypesMemberType
        NotSet = 5  # WeldJointBuilderSplitTypesMemberType
        Skip = 6  # WeldJointBuilderSplitTypesMemberType
        
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
        
    
    
    class JointMidPointData():
        """
        Joint evaluation information at the mid point.  
        
        Results are returned in absolute and ship coordinates .
        Constructor: 
        NXOpen.Weld.WeldJointBuilder.JointMidPointData()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        JointMidPoint: NXOpen.Point3d = ...
        """
        The mid point of the joint in absolute coordinates.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Point3d`
        """
        JointTangent: NXOpen.Vector3d = ...
        """
        The tangent at the joint mid point in absolute coordinates.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        PrimaryFaceNormal: NXOpen.Vector3d = ...
        """
        The primary body face normal in absolute coordinates at the joint mid point.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        SecondaryFaceNormal: NXOpen.Vector3d = ...
        """
        The secondary body face normal in absolute coordinates at the joint mid point.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        GroovePrimaryDirection: NXOpen.Vector3d = ...
        """
        The direction in absolute coordinates towards the primary faces, and way from secondary faces.  
        
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Vector3d`
        """
        GrooveAlignedWithPrimary: bool = ...
        """
        Indicates if the primary faces for the groove are farthest along a positive principal axis.  
        
        <hr>
        
        Field Value
        Type:bool
        """
    
    
    class CoordinateSystem():
        """
        Coordinate system specification. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Absolute", "Desired points and vectors should be in absolute coordinates."
           "Ship", "Desired points and vectors should be in ship coordinate system."
        """
        Absolute = 0  # WeldJointBuilderCoordinateSystemMemberType
        Ship = 1  # WeldJointBuilderCoordinateSystemMemberType
        
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
        
    
    
    class Application():
        """
        Application where joints are created. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "StructureWelding", "Structure Welding Application."
           "Routing", "Routing Application."
        """
        StructureWelding = 0  # WeldJointBuilderApplicationMemberType
        Routing = 1  # WeldJointBuilderApplicationMemberType
        
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
        
    
    
    def Delete(self) -> None:
        """
        Deletes all joints set by :py:meth:`NXOpen.Weld.WeldJointBuilder.Joint`.  
        
        Signature ``Delete()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def Split(self) -> None:
        """
        Splits all joints set by :py:meth:`NXOpen.Weld.WeldJointBuilder.Joint` defined by :py:class:`NXOpen.Weld.WeldJointBuilderSplitTypes`.  
        
        Signature ``Split()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def UpdateJointType(self, type: WeldJointBuilderWeldTypes) -> None:
        """
        Updates all joints set by :py:meth:`NXOpen.Weld.WeldJointBuilder.Joint` to have the given type.  
        
        Signature ``UpdateJointType(type)`` 
        
        :param type: 
        :type type: :py:class:`NXOpen.Weld.WeldJointBuilderWeldTypes` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def DeleteAllUnMarkedJoints(self) -> None:
        """
        Deletes any joints that were not marked with a call to :py:meth:`NXOpen.Weld.WeldJointBuilder.MarkJointsToKeep`.  
        
        Signature ``DeleteAllUnMarkedJoints()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def AddCharacteristicsInheritaceInformation(self) -> None:
        """
        Add welding characteristics inheritance information.  
        
        Signature ``AddCharacteristicsInheritaceInformation()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def DeleteCharacteristicsInheritaceInformation(self) -> None:
        """
        Delete welding characteristics inheritance information.  
        
        Signature ``DeleteCharacteristicsInheritaceInformation()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def MarkJointsToKeep(self) -> None:
        """
        Marks all currently created welding joints so they do not get deleted when :py:meth:`NXOpen.Weld.WeldJointBuilder.DeleteAllUnMarkedJoints` is called from the dialog.  
        
        Signature ``MarkJointsToKeep()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def ShowJoints(self) -> None:
        """
        Show joints will create joints using the method set by :py:class:`NXOpen.Weld.WeldJointBuilderTypes`.  
        
        For :py:class:` NXOpen.Weld.WeldJointBuilderTypes.CreateAutomatic  < NXOpen.Weld.WeldJointBuilderTypes>` and :py:class:` NXOpen.Weld.WeldJointBuilderTypes.CreateAttributes  < NXOpen.Weld.WeldJointBuilderTypes>`
        components need to be set using :py:meth:`NXOpen.Weld.WeldJointBuilder.ShipComponent`.  For :py:class:` NXOpen.Weld.WeldJointBuilderTypes.CreateManual  < NXOpen.Weld.WeldJointBuilderTypes>`,
        the following need to be set:
        When :py:class:`NXOpen.Weld.WeldJointBuilderWeldTypes` is :py:class:` NXOpen.Weld.WeldJointBuilderWeldTypes.Fillet  < NXOpen.Weld.WeldJointBuilderWeldTypes>`, the following 
        methods need to be called to set the input data: :py:meth:`NXOpen.Weld.WeldJointBuilder.MasterEdge`, :py:meth:`NXOpen.Weld.WeldJointBuilder.PlacementFace`,
        :py:meth:`NXOpen.Weld.WeldJointBuilder.TargetFace`.  
        When :py:class:`NXOpen.Weld.WeldJointBuilderWeldTypes` is :py:class:` NXOpen.Weld.WeldJointBuilderWeldTypes.Groove  < NXOpen.Weld.WeldJointBuilderWeldTypes>`, the following 
        methods need to be called to set the input data: :py:meth:`NXOpen.Weld.WeldJointBuilder.PrimaryFace`, :py:meth:`NXOpen.Weld.WeldJointBuilder.PrimaryEdge`,
        :py:meth:`NXOpen.Weld.WeldJointBuilder.SecondaryFace`, :py:meth:`NXOpen.Weld.WeldJointBuilder.SecondaryEdge`. 
        
        Signature ``ShowJoints()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetJointLimits(self, curve: NXOpen.Curve) -> NXOpen.Die.DieLimitsBuilder:
        """
        Get the limits of an individual joint.  
        
        Signature ``GetJointLimits(curve)`` 
        
        :param curve: 
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: :py:class:`NXOpen.Die.DieLimitsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSingleJoint(self, curve: NXOpen.Curve) -> JointItemBuilder:
        """
        Gets the :py:class:`NXOpen.Weld.JointItemBuilder` object associated to the input curve.  
        
        Signature ``GetSingleJoint(curve)`` 
        
        :param curve:  Joint curve  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetJointChanged(self, curve: NXOpen.Curve) -> bool:
        """
        Indicates whether joint was changed.  
        
        Signature ``GetJointChanged(curve)`` 
        
        :param curve:  Joint curve to check  
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetJointChanged(self, curve: NXOpen.Curve, changed: bool) -> None:
        """
        Indicate that joint was changed.  
        
        Signature ``SetJointChanged(curve, changed)`` 
        
        :param curve:  Joint curve to check  
        :type curve: :py:class:`NXOpen.Curve` 
        :param changed: 
        :type changed: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateLimitsPath(self, jointCurve: NXOpen.Curve) -> NXOpen.Curve:
        """
        Creates the path to be used for the limits.  
        
        Signature ``CreateLimitsPath(jointCurve)`` 
        
        :param jointCurve:  Joint curve used to create path.  
        :type jointCurve: :py:class:`NXOpen.Curve` 
        :returns:  Resulting path.  
        :rtype: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UpdateCollectors(self, jointCurve: NXOpen.Curve) -> None:
        """
        Updates the main collectors by copying data from Joint.  
        
        Signature ``UpdateCollectors(jointCurve)`` 
        
        :param jointCurve:  Joint curve to use to update collectors  
        :type jointCurve: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def UpdateJointAfterLimitsChange(self) -> None:
        """
        Updates the joint curve after the limits change. 
        
        Signature ``UpdateJointAfterLimitsChange()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def UpdateJointAfterLimitsChange(self, limits: NXOpen.Die.DieLimitsBuilder) -> None:
        """
        Updates the joint curve after the limits change. 
        
        Signature ``UpdateJointAfterLimitsChange(limits)`` 
        
        :param limits:  limits that changed  
        :type limits: :py:class:`NXOpen.Die.DieLimitsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyLimits(self, limits: NXOpen.Die.DieLimitsBuilder) -> None:
        """
        Copy input limits to builder limits 
        
        Signature ``CopyLimits(limits)`` 
        
        :param limits:  limits to copy  
        :type limits: :py:class:`NXOpen.Die.DieLimitsBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateSingleJointFromFeature(self, featureCurve: NXOpen.Curve, updateBuilder: bool) -> None:
        """
        Creates a joint from a feature.  
        
        Signature ``CreateSingleJointFromFeature(featureCurve, updateBuilder)`` 
        
        :param featureCurve:  Weld Joint feature curve  
        :type featureCurve: :py:class:`NXOpen.Curve` 
        :param updateBuilder:  indicates where builder should be updated with information from the feature  
        :type updateBuilder: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetVariableBevelAngles(self, variableAngles: 'list[float]') -> None:
        """
        This method is for use with the variable bevel callback.  
        
        Signature ``SetVariableBevelAngles(variableAngles)`` 
        
        :param variableAngles:  the variable angles.  
        :type variableAngles: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetVariableBevelAngles(self) -> 'list[float]':
        """
        Gets variable bevel angles.  
        
        This method is for use with the variable bevel callback. 
        
        Signature ``GetVariableBevelAngles()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetConnectedParts(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Gets connected parts for joint.  
        
        Only connected parts that are partially or fully loaded will be returned. Any components that are unloaded will not be returned. 
        
        Signature ``GetConnectedParts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    
    
    def FindPortsInParts(self, parts: 'list[NXOpen.Part]') -> 'list[NXOpen.Routing.Port]':
        """
        Gets ports from the parts.  
        
        Signature ``FindPortsInParts(parts)`` 
        
        :param parts:  the parts used to find the ports.  
        :type parts: list of :py:class:`NXOpen.Part` 
        :returns:  the collection of ports in the parts  
        :rtype: list of :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPrimaryThickness(self, curve: NXOpen.Curve) -> float:
        """
        Gets the primary thickness for a specified joint  
        
        Signature ``GetPrimaryThickness(curve)`` 
        
        :param curve: 
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSecondaryThickness(self, curve: NXOpen.Curve) -> float:
        """
        Gets the primary secondary for a specified joint  
        
        Signature ``GetSecondaryThickness(curve)`` 
        
        :param curve: 
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAngleBetween(self) -> float:
        """
        Gets the angle between the fillet weld mold faces, and the target faces, or butt weld primary and secondary faces.  
        
        Signature ``GetAngleBetween()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIsLongPoint(self) -> bool:
        """
        Gets the long point status.  
        
        A long point indicates only trimming and no extension is needed to to meeting the body being welded to.  
        
        Signature ``GetIsLongPoint()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsCornerOpen(self) -> bool:
        """
        Returns status value of true if corner joint is an open case which means the placement face only touches the target face at the master edge.  
        
        Signature ``IsCornerOpen()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    
    
    def IsPipeJoint(self) -> bool:
        """
        Returns status value of true if this is a pipe welding joint.  
        
        Signature ``IsPipeJoint()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewItem(self) -> JointItemBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointItemBuilder` object.  
        
        Signature ``NewItem()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetNewlyCreatedJoints(self) -> tuple:
        """
        Gets the :py:class:`NXOpen.Weld.JointItemBuilder` objects and curves which were just created by :py:meth:`NXOpen.Weld.WeldJointBuilder.ShowJoints`.  
        
        Signature ``GetNewlyCreatedJoints()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (curves, newItemBuilder). curves is a list of :py:class:`NXOpen.Curve`. newItemBuilder is a list of :py:class:`NXOpen.Weld.JointItemBuilder`. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def SetCallbackMessage(self, message: str) -> None:
        """
        Sets a message to display after callback processing ends 
        
        Signature ``SetCallbackMessage(message)`` 
        
        :param message:  Message to display to user  
        :type message: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def SetErrorMessage(self, message: str) -> None:
        """
        Sets an error message to display 
        
        Signature ``SetErrorMessage(message)`` 
        
        :param message:  Message to display to user  
        :type message: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetMidPointInformation(self, desiredCoordinateSystem: WeldJointBuilderCoordinateSystem) -> tuple:
        """
        Gets the joint curve mid point, tangent, and face normals at the mid point from the primary and secondary bodies.  
        
        Signature ``GetMidPointInformation(desiredCoordinateSystem)`` 
        
        :param desiredCoordinateSystem:  Coordinate system of data returned in jointMidPointData  
        :type desiredCoordinateSystem: :py:class:`NXOpen.Weld.WeldJointBuilderCoordinateSystem` 
        :returns: a tuple 
        :rtype: A tuple consisting of (success, jointMidPointData). success is a bool.   Equals true if data was returned. jointMidPointData is a :py:class:`NXOpen.Weld.WeldJointBuilderJointMidPointData_Struct`.   The joint mid point, tangent and face normals. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    AssociativeSplit: bool = ...
    """
    Returns or sets  whether split joints should be associative 
    
    <hr>
    
    Getter Method
    
    Signature ``AssociativeSplit`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssociativeSplit`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    BackingFace: NXOpen.ScCollector = ...
    """
    Returns  the backing face.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.BackingFace` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``BackingFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    BossColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the boss joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``BossColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ButtColor: int = ...
    """
    Returns or sets  the color for butt weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``ButtColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ButtColor`` 
    
    :param color: 
    :type color: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    ButtColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the butt joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``ButtColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ButtFont: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the curve font for butt weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``ButtFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ButtFont`` 
    
    :param font: 
    :type font: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    ButtWidth: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the curve with for butt weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``ButtWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ButtWidth`` 
    
    :param width: 
    :type width: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    CombineConnectedJoints: bool = ...
    """
    Returns or sets  the indication to combine connected joints if they belong to the same body 
    
    <hr>
    
    Getter Method
    
    Signature ``CombineConnectedJoints`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CombineConnectedJoints`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX9.0.2
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    CornerColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the corner joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``CornerColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    CreateMethod: WeldJointBuilderTypes = ...
    """
    Returns or sets  the creation method 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateMethod`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldJointBuilderTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    CreatedApplication: WeldJointBuilderApplication = ...
    """
    Returns or sets  the application where joint is created 
    
    <hr>
    
    Getter Method
    
    Signature ``CreatedApplication`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderApplication` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreatedApplication`` 
    
    :param application: 
    :type application: :py:class:`NXOpen.Weld.WeldJointBuilderApplication` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Destination: WeldJointBuilderDestinationTypes = ...
    """
    Returns or sets  the destination to create new joints 
    
    <hr>
    
    Getter Method
    
    Signature ``Destination`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderDestinationTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Destination`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldJointBuilderDestinationTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    DuplicateCheck: bool = ...
    """
    Returns or sets  the indication to not allow new joints to be created if they are duplicates of exising joints 
    
    <hr>
    
    Getter Method
    
    Signature ``DuplicateCheck`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DuplicateCheck`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    FilletColor: int = ...
    """
    Returns or sets  the color for T-joint weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``FilletColor`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilletColor`` 
    
    :param color: 
    :type color: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    FilletFont: NXOpen.DisplayableObjectObjectFont = ...
    """
    Returns or sets  the curve font for T-joint weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``FilletFont`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilletFont`` 
    
    :param font: 
    :type font: :py:class:`NXOpen.DisplayableObjectObjectFont` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    FilletWidth: NXOpen.DisplayableObjectObjectWidth = ...
    """
    Returns or sets  the curve with for T-joint weld type joints 
    
    <hr>
    
    Getter Method
    
    Signature ``FilletWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FilletWidth`` 
    
    :param width: 
    :type width: :py:class:`NXOpen.DisplayableObjectObjectWidth` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Joint: NXOpen.SelectCurveList = ...
    """
    Returns  the welding joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``Joint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectCurveList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    JointList: JointItemBuilderList = ...
    """
    Returns  the list of :py:class:`NXOpen.Weld.JointItemBuilder` objects.  
    
    When editing a :py:class:`NXOpen.Weld.WeldJoint` the :py:meth:`NXOpen.Weld.WeldJointBuilder.Joint` should be used
    to access the output curves of the feature.  :py:meth:`NXOpen.Weld.WeldJointBuilder.GetSingleJoint` is then used to access the 
    :py:class:`NXOpen.Weld.JointItemBuilder` from the curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``JointList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointItemBuilderList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    JointPrefix: str = ...
    """
    Returns or sets  the prefix for the weld ID attribute, and the prefix for the name of the component if :py:class:`NXOpen.Weld.WeldJointBuilderDestinationTypes` is :py:class:` NXOpen.Weld.WeldJointBuilderDestinationTypes.NewComponent  < NXOpen.Weld.WeldJointBuilderDestinationTypes>`  
    
    <hr>
    
    Getter Method
    
    Signature ``JointPrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``JointPrefix`` 
    
    :param prefix:     
    :type prefix: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    LapColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the lap joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``LapColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    LimitList: NXOpen.Die.DieLimitsBuilderList = ...
    """
    Returns  the list of limit builders.  
    
    <hr>
    
    Getter Method
    
    Signature ``LimitList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Die.DieLimitsBuilderList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Limits: NXOpen.Die.DieLimitsBuilder = ...
    """
    Returns  the limits of the joint curve span.  
    
    <hr>
    
    Getter Method
    
    Signature ``Limits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Die.DieLimitsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MasterEdge: NXOpen.ScCollector = ...
    """
    Returns  the master edge of a fillet weld.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.MasterEdge` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``MasterEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MaximumFaceGap: float = ...
    """
    Returns or sets  the maximum face gap used when determining if two bodies intersect.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumFaceGap`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumFaceGap`` 
    
    :param gapValue: 
    :type gapValue: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    MechanicalColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the mechanical joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``MechanicalColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NamePrefix: str = ...
    """
    Returns or sets  the prefix used for the welding joint Design Feature name in Collaborative Product Development mode  
    
    <hr>
    
    Getter Method
    
    Signature ``NamePrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NamePrefix`` 
    
    :param prefix:     
    :type prefix: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    NumberSegments: int = ...
    """
    Returns or sets  the number of segments to divide a joint when using :py:class:` NXOpen.Weld.WeldJointBuilderSplitTypes.EqualSegments  < NXOpen.Weld.WeldJointBuilderSplitTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberSegments`` 
    
    :param numberSegments: 
    :type numberSegments: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    PlacementFace: NXOpen.ScCollector = ...
    """
    Returns  the placement face of a fillet weld.  
    
    For example, on a profile it is the face that touches the plate. 
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.PlacementFace` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PrimaryEdge: NXOpen.ScCollector = ...
    """
    Returns  the primary edge of a butt weld.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.PrimaryEdge` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PrimaryFace: NXOpen.ScCollector = ...
    """
    Returns  the primary face of a butt weld.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.PrimaryFace` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SecondaryEdge: NXOpen.ScCollector = ...
    """
    Returns  the secondary edge of a butt weld.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.SecondaryEdge` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SecondaryFace: NXOpen.ScCollector = ...
    """
    Returns  the secondary face of a butt weld.  
    
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.SecondaryFace` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ShipComponent: NXOpen.SelectNXObjectList = ...
    """
    Returns  the components on which the welding joints will be created.  
    
    Used when :py:class:`NXOpen.Weld.WeldJointBuilderTypes`.
    is set to :py:class:` NXOpen.Weld.WeldJointBuilderTypes.CreateAutomatic  < NXOpen.Weld.WeldJointBuilderTypes>` or 
    :py:class:` NXOpen.Weld.WeldJointBuilderTypes.CreateAttributes  < NXOpen.Weld.WeldJointBuilderTypes>`
    After setting the components, :py:meth:`NXOpen.Weld.WeldJointBuilder.ShowJoints` should be called to create the welding joints. 
    
    <hr>
    
    Getter Method
    
    Signature ``ShipComponent`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SleeveColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the sleeve joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``SleeveColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SocketColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the socket joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``SocketColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    SpacingLength: float = ...
    """
    Returns or sets  the spacing length when using :py:class:` NXOpen.Weld.WeldJointBuilderSplitTypes.Skip  < NXOpen.Weld.WeldJointBuilderSplitTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingLength`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SplitAngle: float = ...
    """
    Returns or sets  the split angle to divide a joint when using :py:class:` NXOpen.Weld.WeldJointBuilderSplitTypes.Angle  < NXOpen.Weld.WeldJointBuilderSplitTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SplitAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SplitAngle`` 
    
    :param angle: 
    :type angle: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SplitLength: float = ...
    """
    Returns or sets  the segment length when using :py:class:` NXOpen.Weld.WeldJointBuilderSplitTypes.Skip  < NXOpen.Weld.WeldJointBuilderSplitTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``SplitLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SplitLength`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SplitOption: WeldJointBuilderSplitTypes = ...
    """
    Returns or sets  the method used to split the joint 
    
    <hr>
    
    Getter Method
    
    Signature ``SplitOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderSplitTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SplitOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.Weld.WeldJointBuilderSplitTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SubsetPart: NXOpen.Part = ...
    """
    Returns or sets  the subset part where Design Control Elements are to be created 
    
    <hr>
    
    Getter Method
    
    Signature ``SubsetPart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX9.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SubsetPart`` 
    
    :param part: 
    :type part: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX9.0.1
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    TJointColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the T-joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``TJointColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TargetFace: NXOpen.ScCollector = ...
    """
    Returns  the target face of a fillet weld.  
    
    For example, the plate face that the profile lies on. 
    This should only be used when creating a :py:class:`NXOpen.Weld.WeldJoint` feature.  
    When editing a feature the :py:meth:`NXOpen.Weld.JointItemBuilder.TargetFace` of the :py:class:`NXOpen.Weld.JointItemBuilder` should be used
    to access the data.
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Type: WeldJointBuilderTypes = ...
    """
    Returns or sets  the creation type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldJointBuilderTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    WeldType: WeldJointBuilderWeldTypes = ...
    """
    Returns or sets  the weld type 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldJointBuilderWeldTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldJointBuilderWeldTypes` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    WeldingCharacteristics: CharacteristicsBuilder = ...
    """
    Returns  the collection of welding characteristics defined by attributes.  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldingCharacteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    WorkPart: NXOpen.Part = ...
    """
    Returns or sets  the saved work part 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkPart`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WorkPart`` 
    
    :param part: 
    :type part: :py:class:`NXOpen.Part` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Null: WeldJointBuilder = ...  # unknown typename


class ExportWeldBuilderAttributeOriginTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExportWeldBuilderAttributeOriginType():
    """
    the Attribute Origin enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Object", " - "
       "Df", " - "
    """
    Object = 0  # ExportWeldBuilderAttributeOriginTypeMemberType
    Df = 1  # ExportWeldBuilderAttributeOriginTypeMemberType
    
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
    


class ExportWeldBuilderOutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExportWeldBuilderOutputType():
    """
    the Output Type enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "IntermediateFile", " - "
       "InformationWindow", " - "
    """
    IntermediateFile = 0  # ExportWeldBuilderOutputTypeMemberType
    InformationWindow = 1  # ExportWeldBuilderOutputTypeMemberType
    
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
    


class ExportWeldBuilder(NXOpen.Builder):
    """
    Represents a ExportWeldBuilder class   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateExportWeldBuilder`
    
    Default values.
    
    ================  =================
    Property          Value
    ================  =================
    AttributeOrigin   Object 
    ----------------  -----------------
    Output            IntermediateFile 
    ================  =================
    
    .. versionadded:: NX6.0.0
    """
    
    class AttributeOriginType():
        """
        the Attribute Origin enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Object", " - "
           "Df", " - "
        """
        Object = 0  # ExportWeldBuilderAttributeOriginTypeMemberType
        Df = 1  # ExportWeldBuilderAttributeOriginTypeMemberType
        
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
        the Output Type enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "IntermediateFile", " - "
           "InformationWindow", " - "
        """
        IntermediateFile = 0  # ExportWeldBuilderOutputTypeMemberType
        InformationWindow = 1  # ExportWeldBuilderOutputTypeMemberType
        
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
        
    
    
    def GetExportedAttributes(self) -> 'list[str]':
        """
        Get the attributes of weld points to be exported to CSV file  
        
        Signature ``GetExportedAttributes()`` 
        
        :returns:  Exported attributes string  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetExportedAttributes(self, exportedAttributes: 'list[str]') -> None:
        """
        Set the attributes of weld points to be exported to CSV file 
        
        Signature ``SetExportedAttributes(exportedAttributes)`` 
        
        :param exportedAttributes:  Exported attributes string  
        :type exportedAttributes: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetConnectedPartAttributes(self) -> 'list[str]':
        """
        Get the connected part attributes of weld points  
        
        Signature ``GetConnectedPartAttributes()`` 
        
        :returns:  Connected part attributes string  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetConnectedPartAttributes(self, connectedPartAttributes: 'list[str]') -> None:
        """
        Set the connected part attributes of weld points 
        
        Signature ``SetConnectedPartAttributes(connectedPartAttributes)`` 
        
        :param connectedPartAttributes:  Connected part attributes string  
        :type connectedPartAttributes: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReadAttributesFromWelds(self) -> None:
        """
        Read attributes from selected welds and save to exported attributes and connected part attributes 
        
        Signature ``ReadAttributesFromWelds()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SaveAsDefault(self) -> None:
        """
        Save exported attributes as default template.  
        
        Before use it, you must set template file name. 
        
        Signature ``SaveAsDefault()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def RestoreDefault(self) -> None:
        """
        Restore default template to update exported attributes.  
        
        Before use it, you must set template file name. 
        
        Signature ``RestoreDefault()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SaveToFile(self) -> None:
        """
        Save exported attributes to a template file.  
        
        Before use it, you must set template file name. 
        
        Signature ``SaveToFile()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def OpenFromFile(self) -> None:
        """
        Open a template file to update exported attributes.  
        
        Before use it, you must set template file name. 
        
        Signature ``OpenFromFile()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    AttributeOrigin: ExportWeldBuilderAttributeOriginType = ...
    """
    Returns or sets  the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``AttributeOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.ExportWeldBuilderAttributeOriginType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``AttributeOrigin`` 
    
    :param attributeOrigin: 
    :type attributeOrigin: :py:class:`NXOpen.Weld.ExportWeldBuilderAttributeOriginType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    ConnectedPartAttrToggle: bool = ...
    """
    Returns or sets  the connected part attribute toggle to control if read connected part attributes from weld points 
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedPartAttrToggle`` 
    
    :returns:  Connected part attribute toggle value  
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectedPartAttrToggle`` 
    
    :param connectedPartAttrToggle:  Connected part attribute toggle value  
    :type connectedPartAttrToggle: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CsvFileName: str = ...
    """
    Returns or sets  the CSV file name 
    
    <hr>
    
    Getter Method
    
    Signature ``CsvFileName`` 
    
    :returns:  CSV file name  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CsvFileName`` 
    
    :param csvFileName:  CSV file name  
    :type csvFileName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Output: ExportWeldBuilderOutputType = ...
    """
    Returns or sets  the option defining where to write the output data.  
    
    Data will be written to either a comma separated value file or the output window. 
    
    <hr>
    
    Getter Method
    
    Signature ``Output`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.ExportWeldBuilderOutputType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Output`` 
    
    :param outputType: 
    :type outputType: :py:class:`NXOpen.Weld.ExportWeldBuilderOutputType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TemplateFileName: str = ...
    """
    Returns or sets  the template file name 
    
    <hr>
    
    Getter Method
    
    Signature ``TemplateFileName`` 
    
    :returns:  Template file name  
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TemplateFileName`` 
    
    :param templateFileName:  Template file name  
    :type templateFileName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldPoints: NXOpen.SelectNXObjectList = ...
    """
    Returns  the weld points to be exported to CSV file 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldPoints`` 
    
    :returns:  Selected weld points list  
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: ExportWeldBuilder = ...  # unknown typename


class ExportWeldJointBuilder(ExportWeldBuilder):
    """
    Represents exporting weld joints.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateExportWeldJointBuilder`
    
    Default values.
    
    =======================  ===========================================
    Property                 Value
    =======================  ===========================================
    AttributeOrigin          Object 
    -----------------------  -------------------------------------------
    ChordalTolerance.Value   2.54 (millimeters part), 0.1 (inches part) 
    -----------------------  -------------------------------------------
    Output                   IntermediateFile 
    =======================  ===========================================
    
    .. versionadded:: NX8.5.0
    """
    ChordalTolerance: NXOpen.Expression = ...
    """
    Returns  the minimum chordal length used to create a discrete version of the weld path, points along it will be output into 
    xml file to represent the weld path 
    
    <hr>
    
    Getter Method
    
    Signature ``ChordalTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    OutputFilletFaceInfo: bool = ...
    """
    Returns or sets  the indication to output face normals at each point if leg lengths are defined.  
    
    Will also output a separate record if leg lengths are defined for the opposite side 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputFilletFaceInfo`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputFilletFaceInfo`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    WorkCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the local coordinate system used to calculate the output points on welding joint.  
    
    If no coordinate system is provided, the points will be calculated in terms of the global coordinate system. 
    
    <hr>
    
    Getter Method
    
    Signature ``WorkCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WorkCoordinateSystem`` 
    
    :param coordSystem: 
    :type coordSystem: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Null: ExportWeldJointBuilder = ...  # unknown typename


class WeldAdvisorCheckerTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldAdvisorCheckerType():
    """
    the type of checker 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CoincidentPoint", "Mimimum Distance"
       "MinimumPointDistance", "minimum point distance"
       "MinimumEdgeDistance", "minimum edge distance"
       "StackUpGap", "stack up gap"
       "FacePlanarity", "face planarity"
       "FaceParallelism", "face parallelism"
       "PointFaceDistance", "point face distance"
       "CsysFaceNormalAngle", "csys face normal angle"
       "MetalStackUp", "metal stack up"
       "MetalMinimumPointDatumDistance", "minimum point datum distance"
       "MetalMinimumPointMeasurementDistance", "minimum point measurement distance"
       "SpacingPerPanelCombination", "spacing per panel combination"
       "WeldFlange", "weld flange"
       "Bead", "sealer bead"
       "Number", "number of checkers"
    """
    CoincidentPoint = 0  # WeldAdvisorCheckerTypeMemberType
    MinimumPointDistance = 1  # WeldAdvisorCheckerTypeMemberType
    MinimumEdgeDistance = 2  # WeldAdvisorCheckerTypeMemberType
    StackUpGap = 3  # WeldAdvisorCheckerTypeMemberType
    FacePlanarity = 4  # WeldAdvisorCheckerTypeMemberType
    FaceParallelism = 5  # WeldAdvisorCheckerTypeMemberType
    PointFaceDistance = 6  # WeldAdvisorCheckerTypeMemberType
    CsysFaceNormalAngle = 7  # WeldAdvisorCheckerTypeMemberType
    MetalStackUp = 8  # WeldAdvisorCheckerTypeMemberType
    MetalMinimumPointDatumDistance = 9  # WeldAdvisorCheckerTypeMemberType
    MetalMinimumPointMeasurementDistance = 10  # WeldAdvisorCheckerTypeMemberType
    SpacingPerPanelCombination = 11  # WeldAdvisorCheckerTypeMemberType
    WeldFlange = 12  # WeldAdvisorCheckerTypeMemberType
    Bead = 13  # WeldAdvisorCheckerTypeMemberType
    Number = 14  # WeldAdvisorCheckerTypeMemberType
    
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
    


class LocatorReferenceBuilder(NXOpen.Builder):
    """
    This class is used by "Locator Reference" to add the additional component for a weld datum DF.  
    
    When commit is called, the selected additional components will be added to weld datum parms.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateLocatorReferenceBuilder`
    
    .. versionadded:: NX10.0.2
    """
    
    def SetAdditionalReferenceFromFeature(self, additionalReference: NXOpen.Features.Feature) -> None:
        """
        Set additional references.  
        
        Use to set additional references from feature. 
        
        Signature ``SetAdditionalReferenceFromFeature(additionalReference)`` 
        
        :param additionalReference: 
        :type additionalReference: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    AdditionalReferences: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the additional references 
    
    <hr>
    
    Getter Method
    
    Signature ``AdditionalReferences`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    SelectLocator: NXOpen.SelectNXObjectList = ...
    """
    Returns  the selecte locator 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectLocator`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    """
    Null: LocatorReferenceBuilder = ...  # unknown typename


class WeldTaperMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldTaperMethod():
    """
    Settings for groove taper method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FromEndFace", "Taper will be measured from groove end caps"
       "FromSideFace", "Taper will be measured from groove side face"
    """
    FromEndFace = 0  # WeldTaperMethodMemberType
    FromSideFace = 1  # WeldTaperMethodMemberType
    
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
    


class WeldGrooveExtensionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveExtension():
    """
    Groove Extension Type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Tangent", "Extend selected edges to form an intersection."
       "Project", "Project selected edges to opposite face set."
       "ReverseProject", "Project selected edges to oppsoite face set using normals from selected edges."
    """
    Tangent = 0  # WeldGrooveExtensionMemberType
    Project = 1  # WeldGrooveExtensionMemberType
    ReverseProject = 2  # WeldGrooveExtensionMemberType
    
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
    


class WeldImportBuilder(NXOpen.Builder):
    """
    Creates Weld features by reading a csv file   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateImportBuilder`
    
    .. versionadded:: NX7.5.1
    """
    ConfirmWarningMessages: bool = ...
    """
    Returns or sets  the option to indicate if warning messages need to be confirmed.  
    
    If false setting, all warnings will be accepted. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConfirmWarningMessages`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConfirmWarningMessages`` 
    
    :param option: 
    :type option: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    CreateFeatureGroups: bool = ...
    """
    Returns or sets  the option to create Feature Group features to collect Weld Point features that have the same connected part combinations.  
    
    Connected parts A-B-C and C-B-A will be in the same group. 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateFeatureGroups`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateFeatureGroups`` 
    
    :param createFeatureGroupos: 
    :type createFeatureGroupos: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    """
    InputFile: str = ...
    """
    Returns or sets  the input csv file 
    
    <hr>
    
    Getter Method
    
    Signature ``InputFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InputFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    """
    TemplateFile: str = ...
    """
    Returns or sets  the template file indicating attribute mapping.  
    
    <hr>
    
    Getter Method
    
    Signature ``TemplateFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TemplateFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    """
    Null: WeldImportBuilder = ...  # unknown typename


class WeldMeasurementSizeMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldMeasurementSizeMethod():
    """
    the size method for measurement 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Invalid", "Invalid size method"
       "Auto", "auto size method"
       "Manual", "manual size method"
    """
    Invalid = -1  # WeldMeasurementSizeMethodMemberType
    Auto = 0  # WeldMeasurementSizeMethodMemberType
    Manual = 1  # WeldMeasurementSizeMethodMemberType
    
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
    


class CharacteristicsValueBuilderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CharacteristicsValueBuilderType():
    """
    Settings to indicate the type of value contained in the attribute. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "String", "Indicates the attribute value contains a string."
       "Integer", "Indicates the attribute value contains a integer."
       "Double", "Indicates the attribute value contains a double."
       "Option", "Indicates the attribute value contains a pre set list of strings."
       "NotSet", "Indicates there is no attribute value."
    """
    String = 0  # CharacteristicsValueBuilderTypeMemberType
    Integer = 1  # CharacteristicsValueBuilderTypeMemberType
    Double = 2  # CharacteristicsValueBuilderTypeMemberType
    Option = 3  # CharacteristicsValueBuilderTypeMemberType
    NotSet = 4  # CharacteristicsValueBuilderTypeMemberType
    
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
    


class CharacteristicsValueBuilder(NXOpen.NXObject):
    """
    The object containing the information about the attribute to be 
    placed on the output of the weld feature.  
    
    The inheritance option only applies to the :py:class:`NXOpen.Weld.WeldJoint`.
    
    .. versionadded:: NX7.5.0
    """
    
    class Type():
        """
        Settings to indicate the type of value contained in the attribute. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "String", "Indicates the attribute value contains a string."
           "Integer", "Indicates the attribute value contains a integer."
           "Double", "Indicates the attribute value contains a double."
           "Option", "Indicates the attribute value contains a pre set list of strings."
           "NotSet", "Indicates there is no attribute value."
        """
        String = 0  # CharacteristicsValueBuilderTypeMemberType
        Integer = 1  # CharacteristicsValueBuilderTypeMemberType
        Double = 2  # CharacteristicsValueBuilderTypeMemberType
        Option = 3  # CharacteristicsValueBuilderTypeMemberType
        NotSet = 4  # CharacteristicsValueBuilderTypeMemberType
        
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
        
    
    
    def GetOptionStrings(self) -> 'list[str]':
        """
        The list of strings that are available to be set when AttributeType is :py:class:`Weld.CharacteristicsValueBuilderType.Option <Weld.CharacteristicsValueBuilderType>`.  
        
        Signature ``GetOptionStrings()`` 
        
        :returns:  Strings that are allowed for values.  
        :rtype: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    Active: bool = ...
    """
    Returns or sets  the indication if the attribute is to be placed on the output.  
    
    true indicates
    the attribute will be placed on the output, false indicates the attribute will not
    be placed on the output. Note that if Required is true, then this property cannot be 
    set. 
    
    <hr>
    
    Getter Method
    
    Signature ``Active`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Active`` 
    
    :param active: 
    :type active: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    AttributeType: CharacteristicsValueBuilderType = ...
    """
    Returns  the type of this attribute.  
    
    <hr>
    
    Getter Method
    
    Signature ``AttributeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilderType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Inherited: bool = ...
    """
    Returns or sets  the indication if the attribute value is inherited from the source object.  
    
    <hr>
    
    Getter Method
    
    Signature ``Inherited`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Inherited`` 
    
    :param inherited: 
    :type inherited: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Required: bool = ...
    """
    Returns  the indication if the attribute is required to be placed on the output.  
    
    true indicates
    the attribute will always be placed on the output, false indicates the attribute does not 
    have to be placed on the output. 
    
    <hr>
    
    Getter Method
    
    Signature ``Required`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Title: str = ...
    """
    Returns  the title of this attribute.  
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ValueChanged: bool = ...
    """
    Returns or sets  the indication if the attribute value has been changed.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValueChanged`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueChanged`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX8.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    ValueDouble: float = ...
    """
    Returns or sets  the value of this attribute when AttributeType is :py:class:`Weld.CharacteristicsValueBuilderType.Double <Weld.CharacteristicsValueBuilderType>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValueDouble`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueDouble`` 
    
    :param valueDouble: 
    :type valueDouble: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ValueInteger: int = ...
    """
    Returns or sets  the value of this attribute when AttributeType is :py:class:`Weld.CharacteristicsValueBuilderType.Integer <Weld.CharacteristicsValueBuilderType>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValueInteger`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueInteger`` 
    
    :param valueInteger: 
    :type valueInteger: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ValueString: str = ...
    """
    Returns or sets  the value of this attribute when AttributeType is :py:class:`Weld.CharacteristicsValueBuilderType.String <Weld.CharacteristicsValueBuilderType>` or
    :py:class:`Weld.CharacteristicsValueBuilderType.Option <Weld.CharacteristicsValueBuilderType>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValueString`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValueString`` 
    
    :param valueString: 
    :type valueString: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: CharacteristicsValueBuilder = ...  # unknown typename


class Jointmark(NXOpen.Features.Feature, IFeature):
    """
    Represents a Weld Jointmark Feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.JointmarkBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Jointmark = ...  # unknown typename


class WeldAdvisorCustomerDefaultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldAdvisorCustomerDefault():
    """
    the customer default value types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ResistanceSpot", "Resistance Spot"
       "ArcSpot", "Arc Spot"
       "Clinch", "Clinch"
       "Dollop", "Dollop"
       "WeldNut", "Weld Nut"
       "WeldStud", "Weld Stud"
       "Custom1Point", "Custom1 Point"
       "Custom2Point", "Custom2 Point"
       "Custom3Point", "Custom3 Point"
       "Custom4Point", "Custom4 Point"
       "Custom5Point", "Custom5 Point"
       "Datum", "datum, used for implementing weld advisor parameters"
       "Measurement", "measurement, used for implementing weld advisor parameters"
       "Num", "number of types"
    """
    ResistanceSpot = 0  # WeldAdvisorCustomerDefaultMemberType
    ArcSpot = 1  # WeldAdvisorCustomerDefaultMemberType
    Clinch = 2  # WeldAdvisorCustomerDefaultMemberType
    Dollop = 3  # WeldAdvisorCustomerDefaultMemberType
    WeldNut = 4  # WeldAdvisorCustomerDefaultMemberType
    WeldStud = 5  # WeldAdvisorCustomerDefaultMemberType
    Custom1Point = 6  # WeldAdvisorCustomerDefaultMemberType
    Custom2Point = 7  # WeldAdvisorCustomerDefaultMemberType
    Custom3Point = 8  # WeldAdvisorCustomerDefaultMemberType
    Custom4Point = 9  # WeldAdvisorCustomerDefaultMemberType
    Custom5Point = 10  # WeldAdvisorCustomerDefaultMemberType
    Datum = 11  # WeldAdvisorCustomerDefaultMemberType
    Measurement = 12  # WeldAdvisorCustomerDefaultMemberType
    Num = 13  # WeldAdvisorCustomerDefaultMemberType
    
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
    


class AutoWeldSymbolsBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Weld.AutoWeldSymbolsBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateAutoWeldSymbolsBuilder`
    
    .. versionadded:: NX8.0.0
    """
    DraftingViews: NXOpen.Drawings.SelectDraftingViewList = ...
    """
    Returns  the candidate views for weld symbol creation  
    
    <hr>
    
    Getter Method
    
    Signature ``DraftingViews`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Drawings.SelectDraftingViewList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Welds: NXOpen.SelectNXObjectList = ...
    """
    Returns  the weld objects used to create the weld symbols in the drafting views 
    
    <hr>
    
    Getter Method
    
    Signature ``Welds`` 
    
    :returns:  Selected weld objects list.  
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: AutoWeldSymbolsBuilder = ...  # unknown typename


class WeldPointSpacingMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointSpacingMethod():
    """
    Guide spacing method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Distance", "Place multiple spot welds based on distance"
       "NumPoints", "Place multiple spot welds based on number of points"
    """
    Distance = 0  # WeldPointSpacingMethodMemberType
    NumPoints = 1  # WeldPointSpacingMethodMemberType
    
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
    


class WeldPointMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointMethod():
    """
    Settings for method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Multiple", "use guide curve(s) or edge(s) to generate spot weld points"
       "Single", "use point constructor to generate spot weld points"
       "Mirror", "mirror existing points"
       "Translate", "translate existing points"
       "FromPoints", "create fix/single/none points using existing points"
    """
    Multiple = 0  # WeldPointMethodMemberType
    Single = 1  # WeldPointMethodMemberType
    Mirror = 2  # WeldPointMethodMemberType
    Translate = 3  # WeldPointMethodMemberType
    FromPoints = 4  # WeldPointMethodMemberType
    
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
    


class CharacteristicsSelectionBuilder(NXOpen.NXObject):
    """
    This builder allows you to define the attribute values to be set on the
    output of the weld feature.  
    
    The inheritance option only applies to the :py:class:`NXOpen.Weld.WeldJoint`.
    
    .. versionadded:: NX7.5.0
    """
    
    @typing.overload
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> CharacteristicsValueBuilder:
        """
        Create an integer attribute list entry and add it to the list.  
        
        Signature ``CreateIntegerAttributeListEntry(required, onObject, locked, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`CreateIntegerAttributeListEntry` with inherited parameter instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> CharacteristicsValueBuilder:
        """
        Create an integer attribute list entry and add it to the list.  
        
        Signature ``CreateIntegerAttributeListEntry(required, onObject, locked, inherited, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param inherited:  Is attribute to be inherited, and over-written, by a source entity attribute? Only used by certain application tools.  
        :type inherited: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> CharacteristicsValueBuilder:
        """
        Create a double attribute list entry and add it to the list.  
        
        Signature ``CreateDoubleAttributeListEntry(required, onObject, locked, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: float 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`CreateDoubleAttributeListEntry` with inherited parameter instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> CharacteristicsValueBuilder:
        """
        Create a double attribute list entry and add it to the list.  
        
        Signature ``CreateDoubleAttributeListEntry(required, onObject, locked, inherited, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param inherited:  Is attribute to be inherited, and over-written, by a source entity attribute? Only used by certain application tools.  
        :type inherited: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: float 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str) -> CharacteristicsValueBuilder:
        """
        Create an attribute list entry, that has no value, and add it to the list.  
        
        Signature ``CreateAttributeListEntry(required, onObject, locked, iconName, pointMarker, color, title)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`CreateAttributeListEntry` with inherited parameter instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str) -> CharacteristicsValueBuilder:
        """
        Create an attribute list entry, that has no value, and add it to the list.  
        
        Signature ``CreateAttributeListEntry(required, onObject, locked, inherited, iconName, pointMarker, color, title)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param inherited:  Is attribute to be inherited, and over-written, by a source entity attribute? Only used by certain application tools.  
        :type inherited: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> CharacteristicsValueBuilder:
        """
        Create a string attribute list entry and add it to the list.  
        
        Signature ``CreateStringAttributeListEntry(required, onObject, locked, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`CreateStringAttributeListEntry` with inherited parameter instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> CharacteristicsValueBuilder:
        """
        Create a string attribute list entry and add it to the list.  
        
        Signature ``CreateStringAttributeListEntry(required, onObject, locked, inherited, iconName, pointMarker, color, title, currentValue)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param inherited:  Is attribute to be inherited, and over-written, by a source entity attribute? Only used by certain application tools.  
        :type inherited: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: 'list[str]') -> CharacteristicsValueBuilder:
        """
        Create an option attribute list entry and add it to the list.  
        
        Signature ``CreateOptionAttributeListEntry(required, onObject, locked, iconName, pointMarker, color, title, currentValue, options)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: str 
        :param options:  Options available to be chosen.  
        :type options: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX10.0.0
           Use :py:class:`CreateOptionAttributeListEntry` with inherited parameter instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: 'list[str]') -> CharacteristicsValueBuilder:
        """
        Create an option attribute list entry and add it to the list.  
        
        Signature ``CreateOptionAttributeListEntry(required, onObject, locked, inherited, iconName, pointMarker, color, title, currentValue, options)`` 
        
        :param required:  Is attribute required to be on output object?  
        :type required: bool 
        :param onObject:  Is attribute already on existing object?  
        :type onObject: bool 
        :param locked:  Is attribute locked?  
        :type locked: bool 
        :param inherited:  Is attribute to be inherited, and over-written, by a source entity attribute? Only used by certain application tools.  
        :type inherited: bool 
        :param iconName:  Name of icon to place in list.  
        :type iconName: str 
        :param pointMarker:  marker to apply to point representing weld spot, see POINT_marker_t in point.h.  
        :type pointMarker: int 
        :param color:  color to apply to object.  
        :type color: int 
        :param title:  Title of attribute.  
        :type title: str 
        :param currentValue:  Current value setting of attribute.  
        :type currentValue: str 
        :param options:  Options available to be chosen.  
        :type options: list of str 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    AttributeList: NXOpen.NXObjectList = ...
    """
    Returns  the list of potential attributes for this weld feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``AttributeList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectObjectList: NXOpen.SelectNXObjectList = ...
    """
    Returns  the selection object containing data that is to be attributed.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectObjectList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: CharacteristicsSelectionBuilder = ...  # unknown typename


class WeldPointBuilder(NXOpen.Builder):
    """
    Represents a Spot Weld feature   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldPointBuilder`
    
    Default values.
    
    ==============================  ==============================================
    Property                        Value
    ==============================  ==============================================
    ConnectingOnlyOnePart           false 
    ------------------------------  ----------------------------------------------
    CreationDirection               Default 
    ------------------------------  ----------------------------------------------
    CsysAssemblyState               false 
    ------------------------------  ----------------------------------------------
    CsysWorkPartState               false 
    ------------------------------  ----------------------------------------------
    CustomCylinderAbove             0.5 (millimeters part), 0.02 (inches part) 
    ------------------------------  ----------------------------------------------
    CustomRadius                    0.5 (millimeters part), 0.02 (inches part) 
    ------------------------------  ----------------------------------------------
    CustomTotalCylinderLength       1 (millimeters part), 0.04 (inches part) 
    ------------------------------  ----------------------------------------------
    DatumFirstReferenceDirection    X 
    ------------------------------  ----------------------------------------------
    DatumMajorDirection             X 
    ------------------------------  ----------------------------------------------
    DatumSecondReferenceDirection   X 
    ------------------------------  ----------------------------------------------
    DistanceTolerance               0.025 (millimeters part), 0.001 (inches part) 
    ------------------------------  ----------------------------------------------
    EndDistance                     6.25 (millimeters part), 0.25 (inches part) 
    ------------------------------  ----------------------------------------------
    EndDistanceLocation             Length 
    ------------------------------  ----------------------------------------------
    ExtendMethod                    Boundary 
    ------------------------------  ----------------------------------------------
    Location                        AlongGuideEdge 
    ------------------------------  ----------------------------------------------
    MeasurementDefaultHeight        10 (millimeters part), 0.4 (inches part) 
    ------------------------------  ----------------------------------------------
    MeasurementDefaultWidth         3 (millimeters part), 0.12 (inches part) 
    ------------------------------  ----------------------------------------------
    MeasurementHoleSize             0.0 (millimeters part), 0.0 (inches part) 
    ------------------------------  ----------------------------------------------
    MeasurementSlotLength           0.0 (millimeters part), 0.0 (inches part) 
    ------------------------------  ----------------------------------------------
    MeasurementSlotWidth            0.0 (millimeters part), 0.0 (inches part) 
    ------------------------------  ----------------------------------------------
    MeasurementStudSize             0.0 (millimeters part), 0 (inches part) 
    ------------------------------  ----------------------------------------------
    MirrorByType                    false 
    ------------------------------  ----------------------------------------------
    NumberConnectedPanels           2 
    ------------------------------  ----------------------------------------------
    OffsetDistance                  6.25 (millimeters part), 0.25 (inches part) 
    ------------------------------  ----------------------------------------------
    OutputType                      Fixed 
    ------------------------------  ----------------------------------------------
    PointMethod                     Multiple 
    ------------------------------  ----------------------------------------------
    PointsGuideDistance             0.0 (millimeters part), 0.0 (inches part) 
    ------------------------------  ----------------------------------------------
    ProjectionMethod                None 
    ------------------------------  ----------------------------------------------
    ReferenceSheetSpacingMethod     Distance 
    ------------------------------  ----------------------------------------------
    ReferenceSheetType              Overlap 
    ------------------------------  ----------------------------------------------
    ShowThroughAssemblyState        false 
    ------------------------------  ----------------------------------------------
    ShowThroughWorkPartState        false 
    ------------------------------  ----------------------------------------------
    SizeMethod                      Auto 
    ------------------------------  ----------------------------------------------
    SolidType                       SolidNone 
    ------------------------------  ----------------------------------------------
    SpacingCalculateMethod          Arclength 
    ------------------------------  ----------------------------------------------
    SpacingNumber                   12.5 (millimeters part), 0.5 (inches part) 
    ------------------------------  ----------------------------------------------
    StartDistance                   6.25 (millimeters part), 0.25 (inches part) 
    ------------------------------  ----------------------------------------------
    StartDistanceLocation           Length 
    ------------------------------  ----------------------------------------------
    TranslateXDistance              0 (millimeters part), 0 (inches part) 
    ------------------------------  ----------------------------------------------
    TranslateYDistance              0 (millimeters part), 0 (inches part) 
    ------------------------------  ----------------------------------------------
    TranslateZDistance              0 (millimeters part), 0 (inches part) 
    ------------------------------  ----------------------------------------------
    WeldType                        ResistanceSpot 
    ==============================  ==============================================
    
    .. versionadded:: NX6.0.0
    """
    
    def GetSectionCurves(self, section: NXOpen.Section) -> 'list[NXOpen.Curve]':
        """
        Gets the curves contained in the input section 
        
        Signature ``GetSectionCurves(section)`` 
        
        :param section:  the section container for the curves  
        :type section: :py:class:`NXOpen.Section` 
        :returns:  the curves of the section  
        :rtype: list of :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFaceSet(self, facesetIndex: int) -> tuple:
        """
        Gets the user selected faces for the indicated face set 
        
        Signature ``GetFaceSet(facesetIndex)`` 
        
        :param facesetIndex:  Which faceset to get the faces for. 0 is the first  
        :type facesetIndex: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (objects, frecs). objects is a list of :py:class:`NXOpen.DisplayableObject`.   the face set reference objects frecs is a list of :py:class:`NXOpen.Features.Feature`.   the face set wave linked frecs 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetFaceSet(self, facesetIndex: WeldFacesetIndex, objects: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Sets the user selected faces for the indicated face set 
        
        Signature ``SetFaceSet(facesetIndex, objects)`` 
        
        :param facesetIndex:  Which faceset to get the faces for. 0 is the first  
        :type facesetIndex: :py:class:`NXOpen.Weld.WeldFacesetIndex` 
        :param objects:  the face set reference objects  
        :type objects: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CommitReferenceSheets(self, createStatus: WeldOverlapStatus) -> None:
        """
        The commit for reference sheets 
        
        Signature ``CommitReferenceSheets(createStatus)`` 
        
        :param createStatus:  create status 
        :type createStatus: :py:class:`NXOpen.Weld.WeldOverlapStatus` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ClearFaceSets(self) -> None:
        """
        The clear for all existed facesets 
        
        Signature ``ClearFaceSets()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CommitFaceSets(self) -> None:
        """
        Signature ``CommitFaceSets()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetCurrentReferenceSheet(self) -> int:
        """
        The current refsheet  
        
        Signature ``GetCurrentReferenceSheet()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetCurrentReferenceSheet(self, currentRefSheet: int) -> None:
        """
        Set current refsheet
        
        Signature ``SetCurrentReferenceSheet(currentRefSheet)`` 
        
        :param currentRefSheet:  current refsheet 
        :type currentRefSheet: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateSingleWeldPoint(self, pointCoord: NXOpen.Point3d) -> None:
        """
        The creation for single weld point
        
        Signature ``CreateSingleWeldPoint(pointCoord)`` 
        
        :param pointCoord:  point coordinate 
        :type pointCoord: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetFirstSection(self, section: NXOpen.Section) -> None:
        """
        The commit for first section 
        
        Signature ``SetFirstSection(section)`` 
        
        :param section: the section from uicomp 
        :type section: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateFirstSection(self, totalSection: NXOpen.Section) -> None:
        """
        Update first section 
        
        Signature ``UpdateFirstSection(totalSection)`` 
        
        :param totalSection:  the total section 
        :type totalSection: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateSecondSection(self, totalSection: NXOpen.Section) -> None:
        """
        Update second section 
        
        Signature ``UpdateSecondSection(totalSection)`` 
        
        :param totalSection:  the total section 
        :type totalSection: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetSecondSection(self, section: NXOpen.Section) -> None:
        """
        Create second section 
        
        Signature ``SetSecondSection(section)`` 
        
        :param section: the section from uicomp 
        :type section: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateOffsetCurve(self) -> NXOpen.Section:
        """
        Create offset curve  
        
        Signature ``CreateOffsetCurve()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CalculateWeldPoints(self) -> 'list[NXOpen.Point3d]':
        """
        To calculate all weld points
        
        Signature ``CalculateWeldPoints()`` 
        
        :returns:  weld points  
        :rtype: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetPoint(self, index: int) -> None:
        """
        Set the selected point 
        
        Signature ``SetPoint(index)`` 
        
        :param index:  point index 
        :type index: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetCharacteristics(self, attrTitle: str, attrType: WeldAttribType, attrValue: str) -> None:
        """
        Set or edit characteristics for selected points 
        
        Signature ``SetCharacteristics(attrTitle, attrType, attrValue)`` 
        
        :param attrTitle: attribute title 
        :type attrTitle: str 
        :param attrType: attribute type 
        :type attrType: :py:class:`NXOpen.Weld.WeldAttribType` 
        :param attrValue: attribute value 
        :type attrValue: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateCsys(self, origin: NXOpen.Point3d, matrix: NXOpen.Matrix3x3) -> None:
        """
        Update coordinate system for selected points
        
        Signature ``UpdateCsys(origin, matrix)`` 
        
        :param origin:  origin point  
        :type origin: :py:class:`NXOpen.Point3d` 
        :param matrix:  rotate matrix  
        :type matrix: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def MovePoint(self, origin: NXOpen.Point3d) -> None:
        """
        Move selected points
        
        Signature ``MovePoint(origin)`` 
        
        :param origin:  the new position to be located 
        :type origin: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateCenterLine(self) -> NXOpen.Section:
        """
        To create center line 
        
        Signature ``CreateCenterLine()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CommitSection(self, path: NXOpen.Section) -> None:
        """
        Commit created section
        
        Signature ``CommitSection(path)`` 
        
        :param path:  the created path 
        :type path: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetSelectionType(self, selectionType: WeldSelectionType) -> None:
        """
        Set the selection type 
        
        Signature ``SetSelectionType(selectionType)`` 
        
        :param selectionType:  selection type  
        :type selectionType: :py:class:`NXOpen.Weld.WeldSelectionType` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def FlipZAxis(self) -> None:
        """
        Flip the z axis 
        
        Signature ``FlipZAxis()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateSectionPlaneCurves(self) -> NXOpen.Section:
        """
        Create section curve 
        
        Signature ``CreateSectionPlaneCurves()`` 
        
        :returns:  section curve 
        :rtype: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX7.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMirrorTranslateReferenceObjects(self, refs: 'list[NXOpen.TaggedObject]') -> None:
        """
        Add or remove mirror translate reference objects
        
        Signature ``SetMirrorTranslateReferenceObjects(refs)`` 
        
        :param refs:  the mirror translate reference objects to be added 
        :type refs: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMirrorTranslateReferenceObjects(self) -> 'list[NXOpen.DisplayableObject]':
        """
        Get mirror translate reference objects
        
        Signature ``GetMirrorTranslateReferenceObjects()`` 
        
        :returns:  the mirror translate reference objects 
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CalculateDatumMeasurementDefaultDirection(self) -> None:
        """
        Calculate location and default direction of datum and measurement, need to set the current point prior to calling this method 
        
        Signature ``CalculateDatumMeasurementDefaultDirection()`` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def RemoveCharacteristics(self, attrTitle: str, attrType: WeldAttribType, attrValue: str) -> None:
        """
        Remove characteristics for selected points, need to set the current point prior to calling this method  
        
        Signature ``RemoveCharacteristics(attrTitle, attrType, attrValue)`` 
        
        :param attrTitle: attribute title 
        :type attrTitle: str 
        :param attrType: attribute type 
        :type attrType: :py:class:`NXOpen.Weld.WeldAttribType` 
        :param attrValue: attribute value 
        :type attrValue: str 
        
        .. versionadded:: NX7.5.5
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def RemoveWeldPoint(self) -> None:
        """
        Remove the current selected point, need to set the current point prior to calling this method  
        
        Signature ``RemoveWeldPoint()`` 
        
        .. versionadded:: NX7.5.5
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetNumFaceSets(self) -> int:
        """
        Get the amount of face sets   
        
        Signature ``GetNumFaceSets()`` 
        
        :returns:  total amount of face sets  
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFirstSection(self) -> NXOpen.Section:
        """
        Get the first section.  
        
        For guide curves method, this section contains curves that used to create weld path, 
        For centerline method, this section contians the first group of curves used to create centerline  
        
        Signature ``GetFirstSection()`` 
        
        :returns: the section  
        :rtype: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSecondSection(self) -> NXOpen.Section:
        """
        Get the second section.  
        
        this method for centerline method weld only, this section contains 
        the second group of curves used to create centerline  
        
        Signature ``GetSecondSection()`` 
        
        :returns: the section  
        :rtype: :py:class:`NXOpen.Section` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetReferenceSheets(self) -> NXOpen.Features.Feature:
        """
        The refernence sheet feature  
        
        Signature ``GetReferenceSheets()`` 
        
        :returns:  the reference sheet 
        :rtype: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetCsys(self) -> tuple:
        """
        Get coordinate system for point
        
        Signature ``GetCsys()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (origin, matrix). origin is a :py:class:`NXOpen.Point3d`.   origin point matrix is a :py:class:`NXOpen.Matrix3x3`.   rotate matrix 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ProjectPoints(self) -> None:
        """
        Project selected points along the specified vector to reference sheets
        
        Signature ``ProjectPoints()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    ConnectingOnlyOnePart: bool = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectingOnlyOnePart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectingOnlyOnePart`` 
    
    :param connectingOnlyOnePart: 
    :type connectingOnlyOnePart: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreationDirection: WeldCreationDirection = ...
    """
    Returns or sets  the creation direction type.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreationDirection`` 
    
    :returns:  creation direction type  
    :rtype: :py:class:`NXOpen.Weld.WeldCreationDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CreationDirection`` 
    
    :param creationDirection:  creation direction type  
    :type creationDirection: :py:class:`NXOpen.Weld.WeldCreationDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CsysAssemblyState: bool = ...
    """
    Returns or sets  the assy coordinate system state 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysAssemblyState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CsysAssemblyState`` 
    
    :param assyCsysState: 
    :type assyCsysState: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CsysWorkPartState: bool = ...
    """
    Returns or sets  the work coordinate systemstate 
    
    <hr>
    
    Getter Method
    
    Signature ``CsysWorkPartState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CsysWorkPartState`` 
    
    :param workCsysState: 
    :type workCsysState: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomCylinderAbove: float = ...
    """
    Returns or sets  the distance the custom cylinder should be created above the
    weld point 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomCylinderAbove`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomCylinderAbove`` 
    
    :param customCylinderAbove: 
    :type customCylinderAbove: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomRadius: float = ...
    """
    Returns or sets  the radius to create the sphere, cylinder, or cone with 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomRadius`` 
    
    :param customRadius: 
    :type customRadius: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomTotalCylinderLength: float = ...
    """
    Returns or sets  the total length of the cylinder to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomTotalCylinderLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomTotalCylinderLength`` 
    
    :param totalCylinderLength: 
    :type totalCylinderLength: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumFirstReferenceDirection: WeldDatumControlDirection = ...
    """
    Returns or sets  the datum reference direction type.  
    
    <hr>
    
    Getter Method
    
    Signature ``DatumFirstReferenceDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DatumFirstReferenceDirection`` 
    
    :param datumRefDir: 
    :type datumRefDir: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumMajorDirection: WeldDatumControlDirection = ...
    """
    Returns or sets  the datum major direction type.  
    
    <hr>
    
    Getter Method
    
    Signature ``DatumMajorDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DatumMajorDirection`` 
    
    :param datumMajorDir: 
    :type datumMajorDir: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumSecondReferenceDirection: WeldDatumControlDirection = ...
    """
    Returns or sets  the datum reference direction type.  
    
    <hr>
    
    Getter Method
    
    Signature ``DatumSecondReferenceDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DatumSecondReferenceDirection`` 
    
    :param datumRefDir: 
    :type datumRefDir: :py:class:`NXOpen.Weld.WeldDatumControlDirection` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance for the weld point 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EndDistance: str = ...
    """
    Returns or sets  the end dist 
    
    <hr>
    
    Getter Method
    
    Signature ``EndDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``EndDistance`` 
    
    :param endDistStr:  expression string  
    :type endDistStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EndDistanceLocation: WeldParasetLocation = ...
    """
    Returns or sets  the end dist location 
    
    <hr>
    
    Getter Method
    
    Signature ``EndDistanceLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldParasetLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``EndDistanceLocation`` 
    
    :param endDistLocation: 
    :type endDistLocation: :py:class:`NXOpen.Weld.WeldParasetLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtendMethod: WeldPointExtendMethod = ...
    """
    Returns or sets  the offset curve extend method.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPointExtendMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendMethod`` 
    
    :param extendMethod: 
    :type extendMethod: :py:class:`NXOpen.Weld.WeldPointExtendMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Location: WeldPointLocation = ...
    """
    Returns or sets  the processing method to use for generating weld points along reference section(s) 
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPointLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param location: 
    :type location: :py:class:`NXOpen.Weld.WeldPointLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementDefaultHeight: float = ...
    """
    Returns or sets  the default height of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementDefaultHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementDefaultHeight`` 
    
    :param measurementDefaultHeight: 
    :type measurementDefaultHeight: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementDefaultWidth: float = ...
    """
    Returns or sets  the default width of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementDefaultWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementDefaultWidth`` 
    
    :param measurementDefaultWidth: 
    :type measurementDefaultWidth: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementHoleSize: float = ...
    """
    Returns or sets  the hole_size of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementHoleSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementHoleSize`` 
    
    :param holeSize: 
    :type holeSize: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementSlotLength: float = ...
    """
    Returns or sets  the slot height of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementSlotLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementSlotLength`` 
    
    :param slotLength: 
    :type slotLength: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementSlotWidth: float = ...
    """
    Returns or sets  the slot width of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementSlotWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementSlotWidth`` 
    
    :param slotWidth: 
    :type slotWidth: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementStudSize: float = ...
    """
    Returns or sets  the stud size of the object for measurement to be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementStudSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementStudSize`` 
    
    :param studSize: 
    :type studSize: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MirrorByType: bool = ...
    """
    Returns or sets  the mirror by type 
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorByType`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorByType`` 
    
    :param mirrorByType: 
    :type mirrorByType: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MirrorPlane: NXOpen.Plane = ...
    """
    Returns or sets  the plane that a point is to be mirrored about.  
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorPlane`` 
    
    :param mirrorPlane: 
    :type mirrorPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    NumberConnectedPanels: int = ...
    """
    Returns or sets  the num connected panels.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberConnectedPanels`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``NumberConnectedPanels`` 
    
    :param numConnectedPanels: 
    :type numConnectedPanels: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    OffsetDistance: str = ...
    """
    Returns or sets  the offset distance from edges in guide_collector1 to place weld points  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``OffsetDistance`` 
    
    :param offsetDistance: 
    :type offsetDistance: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    OutputType: OutputType = ...
    """
    Returns or sets  the output type.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputType`` 
    
    :returns:  output type  
    :rtype: :py:class:`NXOpen.Weld.OutputType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputType`` 
    
    :param outputType:  output type  
    :type outputType: :py:class:`NXOpen.Weld.OutputType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    PointMethod: WeldPointMethod = ...
    """
    Returns or sets   the method for creating weld points.  
    
    Weld points can be created using guide
    entities or :py:class:`Point` objects. 
    
    <hr>
    
    Getter Method
    
    Signature ``PointMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPointMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``PointMethod`` 
    
    :param ptMethod: 
    :type ptMethod: :py:class:`NXOpen.Weld.WeldPointMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    PointsGuideDistance: float = ...
    """
    Returns or sets  the distance percentage from the start of the curve where the
    weld point should be.  
    
    0.0 is the start of the curve
    100.0 is the end of the curve. 
    
    <hr>
    
    Getter Method
    
    Signature ``PointsGuideDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``PointsGuideDistance`` 
    
    :param pointsGuideDist: 
    :type pointsGuideDist: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ProjectDirection: NXOpen.Vector3d = ...
    """
    Returns or sets  the project direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectDirection`` 
    
    :returns:  Project direction  
    :rtype: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectDirection`` 
    
    :param direction:  Project direction  
    :type direction: :py:class:`NXOpen.Vector3d` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ProjectDirectionObject: NXOpen.Direction = ...
    """
    Returns or sets  the project direction NXOpen object 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectDirectionObject`` 
    
    :returns:  Project direction  
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectDirectionObject`` 
    
    :param direction:  Project direction  
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ProjectionMethod: WeldProjectionMethod = ...
    """
    Returns or sets  the project method type.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldProjectionMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionMethod`` 
    
    :param projMethod: 
    :type projMethod: :py:class:`NXOpen.Weld.WeldProjectionMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReferenceSheetSpacingMethod: WeldPointSpacingMethod = ...
    """
    Returns or sets  the refsheet spacing method 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSheetSpacingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPointSpacingMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSheetSpacingMethod`` 
    
    :param spacingMethod: 
    :type spacingMethod: :py:class:`NXOpen.Weld.WeldPointSpacingMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReferenceSheetType: WeldPointReferenceSheetType = ...
    """
    Returns or sets   the type of sheet to create to place weld points on.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSheetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPointReferenceSheetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSheetType`` 
    
    :param refSheetType: 
    :type refSheetType: :py:class:`NXOpen.Weld.WeldPointReferenceSheetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SectionPlaneEntity: NXOpen.Plane = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionPlaneEntity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionPlaneEntity`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SequenceNumber: int = ...
    """
    Returns or sets  the sequence number for the weld point feature.  
    
    Each Weld point feature contains a single point.
    If multiple Weld points are to be created, you must specify the sequence of the point you want.
    For example if you are expecting 3 points to be created. You must create 3 weld point features.
    The features will have sequence numbers 0,1 and 2.  
    
    <hr>
    
    Getter Method
    
    Signature ``SequenceNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SequenceNumber`` 
    
    :param sequenceNumber: 
    :type sequenceNumber: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ShowThroughAssemblyState: bool = ...
    """
    Returns or sets  the through assy coordinate system state 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowThroughAssemblyState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowThroughAssemblyState`` 
    
    :param thruAssyState: 
    :type thruAssyState: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ShowThroughWorkPartState: bool = ...
    """
    Returns or sets  the through work coordinate system state 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowThroughWorkPartState`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowThroughWorkPartState`` 
    
    :param thruWorkState: 
    :type thruWorkState: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SizeMethod: WeldMeasurementSizeMethod = ...
    """
    Returns or sets  the measurement size method.  
    
    <hr>
    
    Getter Method
    
    Signature ``SizeMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldMeasurementSizeMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SizeMethod`` 
    
    :param sizeMethod: 
    :type sizeMethod: :py:class:`NXOpen.Weld.WeldMeasurementSizeMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SolidType: WeldCustom = ...
    """
    Returns or sets  the output solid type.  
    
    <hr>
    
    Getter Method
    
    Signature ``SolidType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldCustom` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SolidType`` 
    
    :param solidType: 
    :type solidType: :py:class:`NXOpen.Weld.WeldCustom` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingCalculateMethod: WeldSpacingCalcMethod = ...
    """
    Returns or sets  the project method type.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingCalculateMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldSpacingCalcMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingCalculateMethod`` 
    
    :param spacingCalcMethod: 
    :type spacingCalcMethod: :py:class:`NXOpen.Weld.WeldSpacingCalcMethod` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingNumber: str = ...
    """
    Returns or sets  the spacing number 
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingNumber`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingNumber`` 
    
    :param spacingOrNumberStr:  expression string  
    :type spacingOrNumberStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartDistance: str = ...
    """
    Returns or sets  the start dist
    
    <hr>
    
    Getter Method
    
    Signature ``StartDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``StartDistance`` 
    
    :param startDistStr:  expression string  
    :type startDistStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartDistanceLocation: WeldParasetLocation = ...
    """
    Returns or sets  the start dist location 
    
    <hr>
    
    Getter Method
    
    Signature ``StartDistanceLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldParasetLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``StartDistanceLocation`` 
    
    :param startDistLocation:  start distance location  
    :type startDistLocation: :py:class:`NXOpen.Weld.WeldParasetLocation` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system that a point is to be translated about.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateCsys`` 
    
    :param translateCsys: 
    :type translateCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateXDistance: str = ...
    """
    Returns or sets the tran x dist 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateXDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateXDistance`` 
    
    :param transXDistStr:  expression string  
    :type transXDistStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateYDistance: str = ...
    """
    Returns or sets the trans y dist 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateYDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateYDistance`` 
    
    :param transYDistStr:  expression string  
    :type transYDistStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateZDistance: str = ...
    """
    Returns or sets  the translate distance for weld points in z axis direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateZDistance`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateZDistance`` 
    
    :param transZDistStr:  expression string  
    :type transZDistStr: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldType: WeldFeatureSetType = ...
    """
    Returns or sets  the weld type.  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``WeldType`` 
    
    :param curWeldType: 
    :type curWeldType: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldPointBuilder = ...  # unknown typename


class WeldBeadPathBuilderOffsetMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadPathBuilderOffsetMethodType():
    """
    Settings to indicate the desired offset method. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InFace", "offset in selected primary faces"
       "Centerline", "centerline of overlapping sheets"
    """
    InFace = 0  # WeldBeadPathBuilderOffsetMethodTypeMemberType
    Centerline = 1  # WeldBeadPathBuilderOffsetMethodTypeMemberType
    
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
    


class WeldBeadPathBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents the path the bead shape will be swept along.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldBeadBuilder.NewPath`
    
    .. versionadded:: NX7.5.0
    """
    
    class OffsetMethodType():
        """
        Settings to indicate the desired offset method. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InFace", "offset in selected primary faces"
           "Centerline", "centerline of overlapping sheets"
        """
        InFace = 0  # WeldBeadPathBuilderOffsetMethodTypeMemberType
        Centerline = 1  # WeldBeadPathBuilderOffsetMethodTypeMemberType
        
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
        
    
    
    def UpdatePath(self) -> tuple:
        """
        Computes the preview path, and evaluation information for indicating desired face side of the preview path.  
        
        Signature ``UpdatePath()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (pointFound, evaluationPoint, pathTangent, faceNormalWithFin, faceNormalOppositeFin). pointFound is a bool.   Point and evaluation results are valid evaluationPoint is a :py:class:`NXOpen.Point3d`.   Point that reference vectors are computed atpathTangent is a :py:class:`NXOpen.Vector3d`.   Tangent to path at evaluationPoint faceNormalWithFin is a :py:class:`NXOpen.Vector3d`.   Normal if path is in direction of parasolid fin faceNormalOppositeFin is a :py:class:`NXOpen.Vector3d`.   Normal if path is opposite direction of parasolid fin.
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSweepPath(self) -> NXOpen.Spline:
        """
        The portion of the preview curve that can be used to adjust the start or end limits.  
        
        Signature ``GetSweepPath()`` 
        
        :returns:  The sweep path curve used for setting limits.  
        :rtype: :py:class:`NXOpen.Spline` 
        
        .. versionadded:: NX10.0.3
        
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
    
    CreateEndToStart: bool = ...
    """
    Returns or sets  the indication if the sweep should be created from the edge location to the start location.  
    
    True
    indicates the sweep will be created from the end to the start location of the path, false
    indicates the sweep will be from the start to the end location of the path. This option is
    only used if the path section is closed.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateEndToStart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateEndToStart`` 
    
    :param createEndToStart: 
    :type createEndToStart: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    EndPath: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the location at which to end the sweep of the bead shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndPath`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    OffsetAlongNormal: NXOpen.Expression = ...
    """
    Returns  the offset along normal 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetAlongNormal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    OffsetInFace: NXOpen.Expression = ...
    """
    Returns  the expression containing the distance to offset the path normal to the face.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetInFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    OffsetMethod: WeldBeadPathBuilderOffsetMethodType = ...
    """
    Returns or sets  the desired path offset method.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadPathBuilderOffsetMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OffsetMethod`` 
    
    :param offsetMethod: 
    :type offsetMethod: :py:class:`NXOpen.Weld.WeldBeadPathBuilderOffsetMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PathSection: NXOpen.Section = ...
    """
    Returns  the section defining the path.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ReverseOffsetDirection: bool = ...
    """
    Returns or sets  the reverse the direction to offset the path section.  
    
    The update path method 
    provides the information for the default directions. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseOffsetDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseOffsetDirection`` 
    
    :param reverseOffsetDirection: 
    :type reverseOffsetDirection: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartPath: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the location at which to start the sweep of the bead shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartPath`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: WeldBeadPathBuilder = ...  # unknown typename


class WeldFacesetIndexMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldFacesetIndex():
    """
    the index of user picked face sets 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "First", "first face set"
       "Second", "second face set"
       "Third", "third face set"
       "Forth", "forth face set"
    """
    First = 0  # WeldFacesetIndexMemberType
    Second = 1  # WeldFacesetIndexMemberType
    Third = 2  # WeldFacesetIndexMemberType
    Forth = 3  # WeldFacesetIndexMemberType
    
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
    


class WeldProjectionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldProjectionMethod():
    """
    Settings project method type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "creates only a point"
       "FaceNormal", "creates a sphere"
       "AlongVector", "creates a cylinder"
    """
    NotSet = 0  # WeldProjectionMethodMemberType
    FaceNormal = 1  # WeldProjectionMethodMemberType
    AlongVector = 2  # WeldProjectionMethodMemberType
    
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
    


class DatumPin(NXOpen.Features.Feature):
    """
    Represents a Weld Datum Pin feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.DatumPinBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: DatumPin = ...  # unknown typename


class JointExitBuilderPositionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointExitBuilderPositions():
    """
    Settings to indicate the desired position of edge preporation thickness and angle. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UpperChamfer", "the upper chamfer position"
       "Upper", "the upper position"
       "Middle", "the middle position"
       "Lower", "the lower position"
       "LowerChamfer", "the lower chamfer position"
    """
    UpperChamfer = 0  # JointExitBuilderPositionsMemberType
    Upper = 1  # JointExitBuilderPositionsMemberType
    Middle = 2  # JointExitBuilderPositionsMemberType
    Lower = 3  # JointExitBuilderPositionsMemberType
    LowerChamfer = 4  # JointExitBuilderPositionsMemberType
    
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
    


class JointExitBuilderBodySideMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointExitBuilderBodySide():
    """
    Settings to indicate the side the positions should be applied to. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "First", "the first side. For fillet welds only this needs to be specified."
       "Second", "the other side. This is only used for butt welds."
    """
    First = 0  # JointExitBuilderBodySideMemberType
    Second = 1  # JointExitBuilderBodySideMemberType
    
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
    


class JointExitBuilderFilletSizes_Struct():
    """
    The structure for defining fillet weld lengths.  
    
    .
    Constructor: 
    NXOpen.Weld.JointExitBuilder.FilletSizes()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    ThroatThickness: float = ...
    """
    The fillet weld throat thickness 
    <hr>
    
    Field Value
    Type:float
    """
    LegLength1: float = ...
    """
    The fillet weld first length.  
    
    <hr>
    
    Field Value
    Type:float
    """
    LegLength2: float = ...
    """
    The fillet weld second length.  
    
    <hr>
    
    Field Value
    Type:float
    """


class JointExitBuilder(WeldJointBuilder):
    """
    Used to set custom edge preparation parameters of a :py:class:`NXOpen.Weld.WeldJoint` feaure.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateJointExitBuilder`
    
    Default values.
    
    ===============  =====
    Property         Value
    ===============  =====
    NumberSegments   2 
    ---------------  -----
    RootOpening      0 
    ---------------  -----
    SplitAngle       5.0 
    ===============  =====
    
    .. versionadded:: NX8.0.0
    """
    
    class Positions():
        """
        Settings to indicate the desired position of edge preporation thickness and angle. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UpperChamfer", "the upper chamfer position"
           "Upper", "the upper position"
           "Middle", "the middle position"
           "Lower", "the lower position"
           "LowerChamfer", "the lower chamfer position"
        """
        UpperChamfer = 0  # JointExitBuilderPositionsMemberType
        Upper = 1  # JointExitBuilderPositionsMemberType
        Middle = 2  # JointExitBuilderPositionsMemberType
        Lower = 3  # JointExitBuilderPositionsMemberType
        LowerChamfer = 4  # JointExitBuilderPositionsMemberType
        
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
        
    
    
    class BodySide():
        """
        Settings to indicate the side the positions should be applied to. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "First", "the first side. For fillet welds only this needs to be specified."
           "Second", "the other side. This is only used for butt welds."
        """
        First = 0  # JointExitBuilderBodySideMemberType
        Second = 1  # JointExitBuilderBodySideMemberType
        
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
        
    
    
    class FilletSizes():
        """
        The structure for defining fillet weld lengths.  
        
        .
        Constructor: 
        NXOpen.Weld.JointExitBuilder.FilletSizes()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        ThroatThickness: float = ...
        """
        The fillet weld throat thickness 
        <hr>
        
        Field Value
        Type:float
        """
        LegLength1: float = ...
        """
        The fillet weld first length.  
        
        <hr>
        
        Field Value
        Type:float
        """
        LegLength2: float = ...
        """
        The fillet weld second length.  
        
        <hr>
        
        Field Value
        Type:float
        """
    
    
    def GetEdgePrepValues(self, position: JointExitBuilderPositions) -> tuple:
        """
        Gets the thickness and angle combination to set for the desired weld position 
        
        Signature ``GetEdgePrepValues(position)`` 
        
        :param position:  Position of edge preparation values to set.  
        :type position: :py:class:`NXOpen.Weld.JointExitBuilderPositions` 
        :returns: a tuple 
        :rtype: A tuple consisting of (thickness, angle). thickness is a float.   The thickness depth for this position. angle is a float.   The angle of edge preporation for this position. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEdgePrepValues(self, position: JointExitBuilderPositions, thickness: float, angle: float) -> None:
        """
        This method should be called multiple times.  
        
        First set the BodySide then call this method for each Position.
        For Butt welds this function should be used to set each side. After the primary side is set, change
        the BodySide and call this method for the secondary side. For Fillet welds, only the primary side needs to be set.
        
        Signature ``SetEdgePrepValues(position, thickness, angle)`` 
        
        :param position:  Position of edge preparation values to set.  
        :type position: :py:class:`NXOpen.Weld.JointExitBuilderPositions` 
        :param thickness:  The thickness depth for this position.  
        :type thickness: float 
        :param angle:  The angle of edge preporation for this position.  
        :type angle: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetFilletLengths(self) -> JointExitBuilderFilletSizes_Struct:
        """
        Gets the fillet weld values for the side of the welding joint.  
        
        Signature ``GetFilletLengths()`` 
        
        :returns:  The fillet sizes for the side of the welding joint  
        :rtype: :py:class:`NXOpen.Weld.JointExitBuilderFilletSizes_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFilletLengths(self, sizes: JointExitBuilderFilletSizes_Struct) -> None:
        """
        Sets the fillet weld values for the side of the welding joint.  
        
        Signature ``SetFilletLengths(sizes)`` 
        
        :param sizes:  The fillet sizes for the side of the welding joint  
        :type sizes: :py:class:`NXOpen.Weld.JointExitBuilderFilletSizes_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetOppositeFilletLengths(self) -> JointExitBuilderFilletSizes_Struct:
        """
        Gets the fillet weld values for the opposite side of the welding joint.  
        
        Signature ``GetOppositeFilletLengths()`` 
        
        :returns:  The fillet sizes for the opposite side of the welding joint  
        :rtype: :py:class:`NXOpen.Weld.JointExitBuilderFilletSizes_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOppositeFilletLengths(self, sizes: JointExitBuilderFilletSizes_Struct) -> None:
        """
        Sets the fillet weld values for the opposite side of the welding joint.  
        
        Signature ``SetOppositeFilletLengths(sizes)`` 
        
        :param sizes:  The fillet sizes for the opposite side of the welding joint  
        :type sizes: :py:class:`NXOpen.Weld.JointExitBuilderFilletSizes_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def SetBothFilletLengths(self, sizes: JointExitBuilderFilletSizes_Struct) -> None:
        """
        Sets the symmetric fillet weld values for a welding joint.  
        
        Signature ``SetBothFilletLengths(sizes)`` 
        
        :param sizes:  The symmetric fillet sizes for both sides of the welding joint  
        :type sizes: :py:class:`NXOpen.Weld.JointExitBuilderFilletSizes_Struct` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    FinishMethod: NXOpen.Annotations.FinishMethod = ...
    """
    Returns or sets  the weld finish method 
    
    <hr>
    
    Getter Method
    
    Signature ``FinishMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.FinishMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FinishMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Annotations.FinishMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    OtherSideSymbol: NXOpen.Annotations.Symbol = ...
    """
    Returns or sets  the symbol for welding other side when it is not being prepared 
    
    <hr>
    
    Getter Method
    
    Signature ``OtherSideSymbol`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.Symbol` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OtherSideSymbol`` 
    
    :param symbol: 
    :type symbol: :py:class:`NXOpen.Annotations.Symbol` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    RootOpening: float = ...
    """
    Returns or sets  the desired gap between bodies being welded 
    
    <hr>
    
    Getter Method
    
    Signature ``RootOpening`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RootOpening`` 
    
    :param rootOpening: 
    :type rootOpening: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Side: JointExitBuilderBodySide = ...
    """
    Returns or sets  the side edge preparation values will be applied to 
    
    <hr>
    
    Getter Method
    
    Signature ``Side`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointExitBuilderBodySide` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Side`` 
    
    :param side: 
    :type side: :py:class:`NXOpen.Weld.JointExitBuilderBodySide` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SymbolType: NXOpen.Annotations.Symbol = ...
    """
    Returns or sets  the symbol to override the symbol computed from the joint parameters, if :py:class:`NXOpen.Annotations.Symbol` is not :py:class:` NXOpen.AnnotationsSymbol.None  < NXOpen.AnnotationsSymbol>`.  
    
    Currently only :py:class:` NXOpen.AnnotationsSymbol.JButt  < NXOpen.AnnotationsSymbol>` and :py:class:` NXOpen.AnnotationsSymbol.UButt  < NXOpen.AnnotationsSymbol>` are implemented. All other values
    will be treated as :py:class:` NXOpen.AnnotationsSymbol.None  < NXOpen.AnnotationsSymbol>`
    
    <hr>
    
    Getter Method
    
    Signature ``SymbolType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.Symbol` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SymbolType`` 
    
    :param symbol: 
    :type symbol: :py:class:`NXOpen.Annotations.Symbol` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Null: JointExitBuilder = ...  # unknown typename


class DatumCommonBuilderCustomTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumCommonBuilderCustomTypes():
    """
    The custom type of the datum specified for creation. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "A datum surface or pin specified in the customer defaults by the Default type."
       "Custom1", "A datum surface or pin specified in the customer defaults by the Custom1 type."
       "Custom2", "A datum surface or pin specified in the customer defaults by the Custom2 type."
       "Custom3", "A datum surface or pin specified in the customer defaults by the Custom3 type."
       "Custom4", "A datum surface or pin specified in the customer defaults by the Custom4 type."
       "Custom5", "A datum surface or pin specified in the customer defaults by the Custom5 type."
       "Custom6", "A datum surface or pin specified in the customer defaults by the Custom6 type."
       "Custom7", "A datum surface or pin specified in the customer defaults by the Custom7 type."
    """
    Default = 0  # DatumCommonBuilderCustomTypesMemberType
    Custom1 = 1  # DatumCommonBuilderCustomTypesMemberType
    Custom2 = 2  # DatumCommonBuilderCustomTypesMemberType
    Custom3 = 3  # DatumCommonBuilderCustomTypesMemberType
    Custom4 = 4  # DatumCommonBuilderCustomTypesMemberType
    Custom5 = 5  # DatumCommonBuilderCustomTypesMemberType
    Custom6 = 6  # DatumCommonBuilderCustomTypesMemberType
    Custom7 = 7  # DatumCommonBuilderCustomTypesMemberType
    
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
    


class DatumCommonBuilderControlMethodTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumCommonBuilderControlMethodTypes():
    """
    Settings for the method used to define the control direction. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PrincipalAxis", "A principal axis. Absolute X,Y, or Z"
       "UseSectionPlane", "Not a principal axis, use Section Plane"
    """
    PrincipalAxis = 0  # DatumCommonBuilderControlMethodTypesMemberType
    UseSectionPlane = 1  # DatumCommonBuilderControlMethodTypesMemberType
    
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
    


class DatumCommonBuilderSolidTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumCommonBuilderSolidTypes():
    """
    Settings for defining the solid type to create for the datum object. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sphere", "Datum solid will be a sphere"
       "Cylinder", "Datum solid will be a cylinder"
       "Cone", "Datum solid will be a cone"
    """
    Sphere = 0  # DatumCommonBuilderSolidTypesMemberType
    Cylinder = 1  # DatumCommonBuilderSolidTypesMemberType
    Cone = 2  # DatumCommonBuilderSolidTypesMemberType
    
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
    


class DatumCommonBuilderCreationDirectionMethodsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumCommonBuilderCreationDirectionMethods():
    """
    Settings to define the creation direction. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "Use the default construction method"
       "Opposite", "Reverse the construction orientation"
    """
    Default = 0  # DatumCommonBuilderCreationDirectionMethodsMemberType
    Opposite = 1  # DatumCommonBuilderCreationDirectionMethodsMemberType
    
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
    


class DatumCommonBuilder(NXOpen.Builder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.DatumSurface`  or :py:class:`NXOpen.Weld.DatumPin` feature.  
    
    This is an abstract class and cannot be directly instantiated
    
    .. versionadded:: NX8.5.0
    """
    
    class CustomTypes():
        """
        The custom type of the datum specified for creation. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "A datum surface or pin specified in the customer defaults by the Default type."
           "Custom1", "A datum surface or pin specified in the customer defaults by the Custom1 type."
           "Custom2", "A datum surface or pin specified in the customer defaults by the Custom2 type."
           "Custom3", "A datum surface or pin specified in the customer defaults by the Custom3 type."
           "Custom4", "A datum surface or pin specified in the customer defaults by the Custom4 type."
           "Custom5", "A datum surface or pin specified in the customer defaults by the Custom5 type."
           "Custom6", "A datum surface or pin specified in the customer defaults by the Custom6 type."
           "Custom7", "A datum surface or pin specified in the customer defaults by the Custom7 type."
        """
        Default = 0  # DatumCommonBuilderCustomTypesMemberType
        Custom1 = 1  # DatumCommonBuilderCustomTypesMemberType
        Custom2 = 2  # DatumCommonBuilderCustomTypesMemberType
        Custom3 = 3  # DatumCommonBuilderCustomTypesMemberType
        Custom4 = 4  # DatumCommonBuilderCustomTypesMemberType
        Custom5 = 5  # DatumCommonBuilderCustomTypesMemberType
        Custom6 = 6  # DatumCommonBuilderCustomTypesMemberType
        Custom7 = 7  # DatumCommonBuilderCustomTypesMemberType
        
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
        
    
    
    class ControlMethodTypes():
        """
        Settings for the method used to define the control direction. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PrincipalAxis", "A principal axis. Absolute X,Y, or Z"
           "UseSectionPlane", "Not a principal axis, use Section Plane"
        """
        PrincipalAxis = 0  # DatumCommonBuilderControlMethodTypesMemberType
        UseSectionPlane = 1  # DatumCommonBuilderControlMethodTypesMemberType
        
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
        
    
    
    class SolidTypes():
        """
        Settings for defining the solid type to create for the datum object. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sphere", "Datum solid will be a sphere"
           "Cylinder", "Datum solid will be a cylinder"
           "Cone", "Datum solid will be a cone"
        """
        Sphere = 0  # DatumCommonBuilderSolidTypesMemberType
        Cylinder = 1  # DatumCommonBuilderSolidTypesMemberType
        Cone = 2  # DatumCommonBuilderSolidTypesMemberType
        
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
        
    
    
    class CreationDirectionMethods():
        """
        Settings to define the creation direction. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "Use the default construction method"
           "Opposite", "Reverse the construction orientation"
        """
        Default = 0  # DatumCommonBuilderCreationDirectionMethodsMemberType
        Opposite = 1  # DatumCommonBuilderCreationDirectionMethodsMemberType
        
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
        
    
    
    def UpdateWithDerivedDatum(self) -> None:
        """
        Initialize the builder with the inputs from an existing datum.  
        
        The builder type and derived datum type must be the same. 
        
        Signature ``UpdateWithDerivedDatum()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    AdditionalReferences: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the additional references.  
    
    Use to define addtion parts the datum connects. 
    
    <hr>
    
    Getter Method
    
    Signature ``AdditionalReferences`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics.  
    
    Used to specify additional attributes. 
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    ControlMethod: DatumCommonBuilderControlMethodTypes = ...
    """
    Returns or sets  the control method.  
    
    The method for fixing the datum orientation. 
    
    <hr>
    
    Getter Method
    
    Signature ``ControlMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumCommonBuilderControlMethodTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ControlMethod`` 
    
    :param controlMethod: 
    :type controlMethod: :py:class:`NXOpen.Weld.DatumCommonBuilderControlMethodTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreateDirectionVector: bool = ...
    """
    Returns or sets  the option to control if a reference datum axis should be output with this feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreateDirectionVector`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreateDirectionVector`` 
    
    :param createDirectionVector: 
    :type createDirectionVector: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreatePlane: bool = ...
    """
    Returns or sets  the option to control if a reference datum plane should be output with the this feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreatePlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreatePlane`` 
    
    :param createPlane: 
    :type createPlane: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreatePoint: bool = ...
    """
    Returns or sets  the option to control if a reference point should be output with this feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreatePoint`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreatePoint`` 
    
    :param createPoint: 
    :type createPoint: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreationDirection: DatumCommonBuilderCreationDirectionMethods = ...
    """
    Returns or sets  the creation direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``CreationDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumCommonBuilderCreationDirectionMethods` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CreationDirection`` 
    
    :param creationDirection: 
    :type creationDirection: :py:class:`NXOpen.Weld.DatumCommonBuilderCreationDirectionMethods` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomAboveLength: float = ...
    """
    Returns or sets  the length above the datum reference point.  
    
    This is used if a cylinder or cone are created. 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomAboveLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomAboveLength`` 
    
    :param directionLength: 
    :type directionLength: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomRadius: float = ...
    """
    Returns or sets  the radius of the solid sphere, cylinder or cone created.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomRadius`` 
    
    :param customRadius: 
    :type customRadius: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomTotalLength: float = ...
    """
    Returns or sets  the total length of the cylinder or cone along the direction axis.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomTotalLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomTotalLength`` 
    
    :param customTotalLength: 
    :type customTotalLength: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomType: DatumCommonBuilderCustomTypes = ...
    """
    Returns or sets  the custom datum type.  
    
    This cooresponds to an entry in the customer defaults. 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumCommonBuilderCustomTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomType`` 
    
    :param customType: 
    :type customType: :py:class:`NXOpen.Weld.DatumCommonBuilderCustomTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CustomTypeName: str = ...
    """
    Returns or sets  the custom name used to create the datum.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomTypeName`` 
    
    :returns:  Name of custom data type used from customer defaults  
    :rtype: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomTypeName`` 
    
    :param customTypeName:  Custom datum type from customer defaults to use   
    :type customTypeName: str 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Derived: bool = ...
    """
    Returns or sets  the indicator if this should be marked as a derived from another datum.  
    
    <hr>
    
    Getter Method
    
    Signature ``Derived`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Derived`` 
    
    :param derived: 
    :type derived: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    DirectionAxis: NXOpen.Axis = ...
    """
    Returns or sets  the direction axis.  
    
    This defines the datum origin and specifed axis. 
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionAxis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Axis` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionAxis`` 
    
    :param directionAxis: 
    :type directionAxis: :py:class:`NXOpen.Axis` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    DirectionLength: float = ...
    """
    Returns or sets  the length of the datum axis vector created.  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionLength`` 
    
    :param directionLength: 
    :type directionLength: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ModelingTolerance: float = ...
    """
    Returns or sets  the modeling distance tolerance.  
    
    <hr>
    
    Getter Method
    
    Signature ``ModelingTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModelingTolerance`` 
    
    :param modelingTolerance: 
    :type modelingTolerance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PlaneHeight: float = ...
    """
    Returns or sets  the plane height along the direction axis.  
    
    Controls the boundary of a datum plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneHeight`` 
    
    :param planeHeight: 
    :type planeHeight: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PlaneWidth: float = ...
    """
    Returns or sets  the plane width perpendicular to the direction axis.  
    
    Controls the boundary of a datum plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneWidth`` 
    
    :param planeWidth: 
    :type planeWidth: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PrincipalAxisX: bool = ...
    """
    Returns or sets  the principal axis x.  
    
    Used to specify datum is controlling the x axis. 
    
    <hr>
    
    Getter Method
    
    Signature ``PrincipalAxisX`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrincipalAxisX`` 
    
    :param principalAxisX: 
    :type principalAxisX: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PrincipalAxisY: bool = ...
    """
    Returns or sets  the principal axis y.  
    
    Used to specify the datum is controlling the y axis. 
    
    <hr>
    
    Getter Method
    
    Signature ``PrincipalAxisY`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrincipalAxisY`` 
    
    :param principalAxisY: 
    :type principalAxisY: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PrincipalAxisZ: bool = ...
    """
    Returns or sets  the principal axis z.  
    
    Used to specify the datum is controlling the z axis. 
    
    <hr>
    
    Getter Method
    
    Signature ``PrincipalAxisZ`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrincipalAxisZ`` 
    
    :param principalAxisZ: 
    :type principalAxisZ: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ProjectAlongDirection: bool = ...
    """
    Returns or sets  the project along direction.  
    
    Two coordiantes can be specified and the third obtained from projection. 
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectAlongDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectAlongDirection`` 
    
    :param projectAlongDirection: 
    :type projectAlongDirection: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SectionPlaneNormal: NXOpen.Direction = ...
    """
    Returns or sets  the section plane normal.  
    
    This is sometimes referred to as the clamping plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionPlaneNormal`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SectionPlaneNormal`` 
    
    :param sectionPlaneNormal: 
    :type sectionPlaneNormal: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SolidType: DatumCommonBuilderSolidTypes = ...
    """
    Returns or sets  the solid body type specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``SolidType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumCommonBuilderSolidTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolidType`` 
    
    :param solidType: 
    :type solidType: :py:class:`NXOpen.Weld.DatumCommonBuilderSolidTypes` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: DatumCommonBuilder = ...  # unknown typename


class DatumPinBuilder(DatumCommonBuilder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.DatumPin` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateDatumPinBuilder`
    
    Default values.
    
    ======================  =========================================
    Property                Value
    ======================  =========================================
    ControlMethod           PrincipalAxis 
    ----------------------  -----------------------------------------
    CreateDirectionVector   1 
    ----------------------  -----------------------------------------
    CreatePlane             1 
    ----------------------  -----------------------------------------
    CreatePoint             1 
    ----------------------  -----------------------------------------
    Derived                 0 
    ----------------------  -----------------------------------------
    DirectionLength         20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    ModelingTolerance       0.0254 
    ----------------------  -----------------------------------------
    PlaneHeight             20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    PlaneWidth              20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    PrincipalAxisX          0 
    ----------------------  -----------------------------------------
    PrincipalAxisY          0 
    ----------------------  -----------------------------------------
    PrincipalAxisZ          0 
    ======================  =========================================
    
    .. versionadded:: NX8.5.0
    """
    
    def MoveToCenter(self) -> None:
        """
        Moves a point to the center of a circle or slot boundary 
        
        Signature ``MoveToCenter()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def InitializeAxis(self) -> None:
        """
        Update the axis origin to the center of the slot or circle, and direction to the normal of the boundary.  
        
        If the boundary is not planar an approximate direction will be computed from boundary bounding box. 
        
        Signature ``InitializeAxis()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateAxisData(self) -> None:
        """
        Updates data related to the axis.  
        
        The origin will be adjusted based on grid snapping, and projection direction.   In addition the control direction information will be updated.  
        
        Signature ``UpdateAxisData()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    BoundaryCurve: NXOpen.ScCollector = ...
    """
    Returns  the resting face 
    
    <hr>
    
    Getter Method
    
    Signature ``BoundaryCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DerivedDatum: SelectDatumPin = ...
    """
    Returns  the derived datum 
    
    <hr>
    
    Getter Method
    
    Signature ``DerivedDatum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.SelectDatumPin` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: DatumPinBuilder = ...  # unknown typename


class JointItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[JointItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: JointItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: JointItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.JointItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> JointItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
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
    def Erase(self, obj: JointItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: JointItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[JointItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[JointItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.JointItemBuilder` 
        
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
    def Swap(self, object1: JointItemBuilder, object2: JointItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.JointItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: JointItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.JointItemBuilder` 
        
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
    Null: JointItemBuilderList = ...  # unknown typename


class WeldFeatureSetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldFeatureSetType():
    """
    the feature set types 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FilletWeld", "Fillet Weld"
       "GrooveWeld", "Groove Weld"
       "ResistanceSpot", "Resistance Spot"
       "ArcSpot", "Arc Spot"
       "Clinch", "Clinch"
       "Dollop", "Dollop"
       "WeldNut", "Weld Nut"
       "WeldStud", "Weld Stud"
       "Custom1Point", "Custom1 Point"
       "Custom2Point", "Custom2 Point"
       "Custom3Point", "Custom3 Point"
       "Custom4Point", "Custom4 Point"
       "Custom5Point", "Custom5 Point"
       "BiwDatumSurface", "Datum Surface"
       "BiwDatumPin", "Datum Pin"
       "BiwDatumCustomer1", "Datum Customer1"
       "BiwDatumCustomer2", "Datum Customer2"
       "BiwDatumCustomer3", "Datum Customer3"
       "BiwMeasurementSurface", "Measurement Surface"
       "BiwMeasurementHole", "Measurement Hole"
       "BiwMeasurementSlot", "Measurement Slot"
       "BiwMeasurementStud", "Measurement Stud"
       "BiwMeasurementTrim", "Measurement Trim"
       "BiwMeasurementHem", "Measurement Hem"
       "BiwMeasurementCustomer1", "Measurement Customer1"
       "BiwMeasurementCustomer2", "Measurement Customer2"
       "BiwMeasurementCustomer3", "Measurement Customer3"
    """
    FilletWeld = 0  # WeldFeatureSetTypeMemberType
    GrooveWeld = 1  # WeldFeatureSetTypeMemberType
    ResistanceSpot = 2  # WeldFeatureSetTypeMemberType
    ArcSpot = 3  # WeldFeatureSetTypeMemberType
    Clinch = 4  # WeldFeatureSetTypeMemberType
    Dollop = 5  # WeldFeatureSetTypeMemberType
    WeldNut = 6  # WeldFeatureSetTypeMemberType
    WeldStud = 7  # WeldFeatureSetTypeMemberType
    Custom1Point = 8  # WeldFeatureSetTypeMemberType
    Custom2Point = 9  # WeldFeatureSetTypeMemberType
    Custom3Point = 10  # WeldFeatureSetTypeMemberType
    Custom4Point = 11  # WeldFeatureSetTypeMemberType
    Custom5Point = 12  # WeldFeatureSetTypeMemberType
    BiwDatumSurface = 13  # WeldFeatureSetTypeMemberType
    BiwDatumPin = 14  # WeldFeatureSetTypeMemberType
    BiwDatumCustomer1 = 15  # WeldFeatureSetTypeMemberType
    BiwDatumCustomer2 = 16  # WeldFeatureSetTypeMemberType
    BiwDatumCustomer3 = 17  # WeldFeatureSetTypeMemberType
    BiwMeasurementSurface = 18  # WeldFeatureSetTypeMemberType
    BiwMeasurementHole = 19  # WeldFeatureSetTypeMemberType
    BiwMeasurementSlot = 20  # WeldFeatureSetTypeMemberType
    BiwMeasurementStud = 21  # WeldFeatureSetTypeMemberType
    BiwMeasurementTrim = 22  # WeldFeatureSetTypeMemberType
    BiwMeasurementHem = 23  # WeldFeatureSetTypeMemberType
    BiwMeasurementCustomer1 = 24  # WeldFeatureSetTypeMemberType
    BiwMeasurementCustomer2 = 25  # WeldFeatureSetTypeMemberType
    BiwMeasurementCustomer3 = 26  # WeldFeatureSetTypeMemberType
    
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
    


class AutoPoint(NXOpen.Features.Feature):
    """
    This class will automatically create weld points from selected components   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.AutoPointBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: AutoPoint = ...  # unknown typename


class JointmarkBuilderMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderMethod():
    """
    The type of construction method for creating Jointmark 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "GuideCurve", "Guide Curve"
       "Mirror", "Mirror"
       "Points", "Points"
       "Translate", "Translate"
       "ExistingPoints", "Existing Points. Only allowed for :py:class:`NXOpen.Weld.PointMark` class."
    """
    GuideCurve = 0  # JointmarkBuilderMethodMemberType
    Mirror = 1  # JointmarkBuilderMethodMemberType
    Points = 2  # JointmarkBuilderMethodMemberType
    Translate = 3  # JointmarkBuilderMethodMemberType
    ExistingPoints = 4  # JointmarkBuilderMethodMemberType
    
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
    


class JointmarkBuilderReferenceSheetTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderReferenceSheetTypes():
    """
    The type of sheets to create 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Overlap", "Overlap"
       "Top", "Top"
    """
    Overlap = 0  # JointmarkBuilderReferenceSheetTypesMemberType
    Top = 1  # JointmarkBuilderReferenceSheetTypesMemberType
    
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
    


class JointmarkBuilderConnectedPanelTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderConnectedPanelTypes():
    """
    The type of sheets to create 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Two", " - "
       "Three", " - "
       "Four", " - "
    """
    Two = 0  # JointmarkBuilderConnectedPanelTypesMemberType
    Three = 1  # JointmarkBuilderConnectedPanelTypesMemberType
    Four = 2  # JointmarkBuilderConnectedPanelTypesMemberType
    
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
    


class JointmarkBuilderReuseMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderReuseMethod():
    """
    The method to indicate if all reuse features have the same connected parts 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SameConnectingParts", " - "
       "AnyConnectingParts", " - "
    """
    SameConnectingParts = 0  # JointmarkBuilderReuseMethodMemberType
    AnyConnectingParts = 1  # JointmarkBuilderReuseMethodMemberType
    
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
    


class JointmarkBuilderProjectionDirectionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderProjectionDirectionOptions():
    """
    The projection direction used to project points onto the reference sheet 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "AlongFaceNormal", " - "
       "PricipalAxis", " - "
       "X", " - "
       "Y", " - "
       "Z", " - "
    """
    NotSet = 0  # JointmarkBuilderProjectionDirectionOptionsMemberType
    AlongFaceNormal = 1  # JointmarkBuilderProjectionDirectionOptionsMemberType
    PricipalAxis = 2  # JointmarkBuilderProjectionDirectionOptionsMemberType
    X = 3  # JointmarkBuilderProjectionDirectionOptionsMemberType
    Y = 4  # JointmarkBuilderProjectionDirectionOptionsMemberType
    Z = 5  # JointmarkBuilderProjectionDirectionOptionsMemberType
    
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
    


class JointmarkBuilderOrientationMethodTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkBuilderOrientationMethodTypes():
    """
    The type of orientation method for defining the default coordinate system. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SurfaceNormal", "Surface Normals."
       "CoordinateSystem", "Use fixed csys instead of surface normals."
    """
    SurfaceNormal = 0  # JointmarkBuilderOrientationMethodTypesMemberType
    CoordinateSystem = 1  # JointmarkBuilderOrientationMethodTypesMemberType
    
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
    


class JointmarkBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.Jointmark` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateJointmarkBuilder`
    
    Default values.
    
    =====================  ====================
    Property               Value
    =====================  ====================
    Associativity          1 
    ---------------------  --------------------
    ConnectPart            0 
    ---------------------  --------------------
    ConstructionMethod     GuideCurve 
    ---------------------  --------------------
    CreateSingleFeatures   0 
    ---------------------  --------------------
    OrientationMethod      SurfaceNormal 
    ---------------------  --------------------
    ReferenceSheetType     Overlap 
    ---------------------  --------------------
    ReuseFeaturesMethod    SameConnectingParts 
    ---------------------  --------------------
    ShowWorkCsys           1 
    =====================  ====================
    
    .. versionadded:: NX9.0.0
    """
    
    class Method():
        """
        The type of construction method for creating Jointmark 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "GuideCurve", "Guide Curve"
           "Mirror", "Mirror"
           "Points", "Points"
           "Translate", "Translate"
           "ExistingPoints", "Existing Points. Only allowed for :py:class:`NXOpen.Weld.PointMark` class."
        """
        GuideCurve = 0  # JointmarkBuilderMethodMemberType
        Mirror = 1  # JointmarkBuilderMethodMemberType
        Points = 2  # JointmarkBuilderMethodMemberType
        Translate = 3  # JointmarkBuilderMethodMemberType
        ExistingPoints = 4  # JointmarkBuilderMethodMemberType
        
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
        
    
    
    class ReferenceSheetTypes():
        """
        The type of sheets to create 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Overlap", "Overlap"
           "Top", "Top"
        """
        Overlap = 0  # JointmarkBuilderReferenceSheetTypesMemberType
        Top = 1  # JointmarkBuilderReferenceSheetTypesMemberType
        
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
        
    
    
    class ConnectedPanelTypes():
        """
        The type of sheets to create 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Two", " - "
           "Three", " - "
           "Four", " - "
        """
        Two = 0  # JointmarkBuilderConnectedPanelTypesMemberType
        Three = 1  # JointmarkBuilderConnectedPanelTypesMemberType
        Four = 2  # JointmarkBuilderConnectedPanelTypesMemberType
        
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
        
    
    
    class ReuseMethod():
        """
        The method to indicate if all reuse features have the same connected parts 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SameConnectingParts", " - "
           "AnyConnectingParts", " - "
        """
        SameConnectingParts = 0  # JointmarkBuilderReuseMethodMemberType
        AnyConnectingParts = 1  # JointmarkBuilderReuseMethodMemberType
        
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
        
    
    
    class ProjectionDirectionOptions():
        """
        The projection direction used to project points onto the reference sheet 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "AlongFaceNormal", " - "
           "PricipalAxis", " - "
           "X", " - "
           "Y", " - "
           "Z", " - "
        """
        NotSet = 0  # JointmarkBuilderProjectionDirectionOptionsMemberType
        AlongFaceNormal = 1  # JointmarkBuilderProjectionDirectionOptionsMemberType
        PricipalAxis = 2  # JointmarkBuilderProjectionDirectionOptionsMemberType
        X = 3  # JointmarkBuilderProjectionDirectionOptionsMemberType
        Y = 4  # JointmarkBuilderProjectionDirectionOptionsMemberType
        Z = 5  # JointmarkBuilderProjectionDirectionOptionsMemberType
        
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
        
    
    
    class OrientationMethodTypes():
        """
        The type of orientation method for defining the default coordinate system. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SurfaceNormal", "Surface Normals."
           "CoordinateSystem", "Use fixed csys instead of surface normals."
        """
        SurfaceNormal = 0  # JointmarkBuilderOrientationMethodTypesMemberType
        CoordinateSystem = 1  # JointmarkBuilderOrientationMethodTypesMemberType
        
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
        
    
    
    def UpdateFeatures(self) -> None:
        """
        Updates all the items on the points list based on the construction method and related inputs.  
        
        Signature ``UpdateFeatures()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdatePoint(self) -> None:
        """
        Updates the selected point by projecting it to the guide curve.  
        
        Signature ``UpdatePoint()`` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def RediscoverFaces(self) -> None:
        """
        Use the Weld Assistant Connected Face Finder command to rediscover faces based on the current feature point positions.  
        
        Signature ``RediscoverFaces()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateReferenceData(self) -> None:
        """
        Create a temporary overlap or top sheet and guide curve.  
        
        Use with independent :py:class:`NXOpen.Weld.PointMarkPoint` features. 
        
        Signature ``CreateReferenceData()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def DeleteReferenceData(self) -> None:
        """
        Delete temporary overlap or top sheet feature.  
        
        Use with independent :py:class:`NXOpen.Weld.PointMarkPoint` features. 
        
        Signature ``DeleteReferenceData()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetDisplayCsys(self, status: bool) -> None:
        """
        Indicates whether the csys should be displayed on creation 
        
        Signature ``SetDisplayCsys(status)`` 
        
        :param status: 
        :type status: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetShowThruState(self, status: bool) -> None:
        """
        Indicates whether the output objects should show thru on creation 
        
        Signature ``SetShowThruState(status)`` 
        
        :param status: 
        :type status: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def NewGuide(self) -> JointmarkGuideBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointmarkGuideBuilder` object.  
        
        Signature ``NewGuide()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def NewFaceSets(self) -> JointmarkFaceSetsBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` object.  
        
        Signature ``NewFaceSets()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def NewPoints(self) -> JointmarkPointsBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointmarkPointsBuilder` object.  
        
        Signature ``NewPoints()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateReferenceSheet(self, facesModified: bool) -> NXOpen.Features.Feature:
        """
        Prepares a Reference Sheet for placing Jointmark features.  
        
        If the sheet is suppressed, it will be unsuppressed.  
        
        Signature ``UpdateReferenceSheet(facesModified)`` 
        
        :param facesModified:  Indicates if Reference Sheet needs to be updated.  
        :type facesModified: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetReferenceSheet(self) -> NXOpen.Features.Feature:
        """
        Returns the Reference Sheet feature 
        
        Signature ``GetReferenceSheet()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSheetEdges(self) -> 'list[NXOpen.Edge]':
        """
        Edges of created sheet 
        
        Signature ``GetSheetEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateSymbolCurve(self, path: str, name: str) -> NXOpen.Curve:
        """
        Create curve From PMI symbol  
        
        Signature ``CreateSymbolCurve(path, name)`` 
        
        :param path:  Symbol path  
        :type path: str 
        :param name:  Symbol id    
        :type name: str 
        :returns:  Curve from symbol  
        :rtype: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def AppendPoints(self, mode: bool, curve: NXOpen.Curve) -> None:
        """
        Creates a list of points on the overlap sheet.  
        
        In addition, a curve selected by the user will be placed at these points. 
        
        Signature ``AppendPoints(mode, curve)`` 
        
        :param mode:  Create or Edit  
        :type mode: bool 
        :param curve:  Curve to place at these points 
        :type curve: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def MapFeaturesToPoints(self) -> None:
        """
        Maps the selected reuse features to the new preview point locations.  
        
        Signature ``MapFeaturesToPoints()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def FromReuseFeatures(self) -> tuple:
        """
        Initializes face sets, guide curve, and points builders from reuse features.  
        
        Signature ``FromReuseFeatures()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (faceSetsUpdated, guideCurvesUpdated, pointSelectionUpdated). faceSetsUpdated is a bool.   Indicates if the face set list was updated. guideCurvesUpdated is a bool.   Indicates if the guide curve list was updated. pointSelectionUpdated is a bool.   Indicates if point selection object was updated. 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSelectedReferences(self) -> 'list[NXOpen.NXObject]':
        """
        Gets the selected points, or point features, references.  
        
        Does not apply to the guide curves method. 
        
        Signature ``GetSelectedReferences()`` 
        
        :returns: The array of references. These may be points or point features.  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetCreateReferenceDataMessages(self) -> 'list[str]':
        """
        Get all the messages created by :py:meth:`NXOpen.Weld.JointmarkBuilder.CreateReferenceData`.  
        
        Signature ``GetCreateReferenceDataMessages()`` 
        
        :returns:  The array of messages generated during the process of discovering the reference data.  
        :rtype: list of str 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def MoveReferenceSheet(self) -> None:
        """
        Move the Reference Sheet to work layer, and unlink from grouping feature.  
        
        Signature ``MoveReferenceSheet()`` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def AskConnectedFaces(self) -> ConnectedPart:
        """
        Find the connected face information.  
        
        The data is stored in :py:class:`NXOpen.Weld.ConnectedPart` containing the appropriate
        connected part face occurrence information. 
        
        Signature ``AskConnectedFaces()`` 
        
        :returns:  Connected face information. None if none are found.  
        :rtype: :py:class:`NXOpen.Weld.ConnectedPart` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Associativity: bool = ...
    """
    Returns or sets  the automatic update option also known as associativity.  
    
    If true, the curve representing the Jointmark feature will change its location if the guide curve is updated
    
    <hr>
    
    Getter Method
    
    Signature ``Associativity`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Associativity`` 
    
    :param associativity: 
    :type associativity: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics 
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ConnectPart: bool = ...
    """
    Returns or sets  the option of connecting only one part.  
    
    If true, Jointmark feature is created on a single component.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectPart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectPart`` 
    
    :param connectPart: 
    :type connectPart: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ConnectedPanelType: JointmarkBuilderConnectedPanelTypes = ...
    """
    Returns or sets  the number of connected panels at a point.  
    
    This is used when the construction method is Existing Points 
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedPanelType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderConnectedPanelTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectedPanelType`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.JointmarkBuilderConnectedPanelTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ConstructionMethod: JointmarkBuilderMethod = ...
    """
    Returns or sets  the construction method for creating Jointmark 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstructionMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstructionMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.JointmarkBuilderMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreateSingleFeatures: bool = ...
    """
    Returns or sets  the control option to determine if individual features should be created.  
    
    Only allowed for :py:class:`NXOpen.Weld.PointMark` class. 
    
    <hr>
    
    Getter Method
    
    Signature ``CreateSingleFeatures`` 
    
    :returns:  true- single features. false - fully associative features are created.  
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CreateSingleFeatures`` 
    
    :param createSingleFeatures:  true- Full associative features are created. false- single non associative features. 
    :type createSingleFeatures: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceSetsList: JointmarkFaceSetsBuilderList = ...
    """
    Returns  the list of face sets  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSetsList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilderList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FixedCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the fixed csys that overrides the default Csys orientation.  
    
    <hr>
    
    Getter Method
    
    Signature ``FixedCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``FixedCsys`` 
    
    :param fixedCsys: 
    :type fixedCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    GuideCurvesList: JointmarkGuideBuilderList = ...
    """
    Returns  the list of guide curves 
    
    <hr>
    
    Getter Method
    
    Signature ``GuideCurvesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilderList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    NotifyIfParentPointMoved: bool = ...
    """
    Returns or sets  the option to indicate if an alert should be issued when the parent point moves.  
    
    Valid when using :py:class:`NXOpen.Weld.JointmarkBuilderMethod.ExistingPoints <NXOpen.Weld.JointmarkBuilderMethod>` and associativity is off. 
    
    <hr>
    
    Getter Method
    
    Signature ``NotifyIfParentPointMoved`` 
    
    :returns:  true- provide notificaton when parent moves. false - do not provide notification.  
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``NotifyIfParentPointMoved`` 
    
    :param notifyIfParentPointMoved:  true- provide notificaton when parent moves. false - do not provide notification.  
    :type notifyIfParentPointMoved: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    OrientationMethod: JointmarkBuilderOrientationMethodTypes = ...
    """
    Returns or sets  the orientation method for defining a csys 
    
    <hr>
    
    Getter Method
    
    Signature ``OrientationMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderOrientationMethodTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``OrientationMethod`` 
    
    :param orientationMethod: 
    :type orientationMethod: :py:class:`NXOpen.Weld.JointmarkBuilderOrientationMethodTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane used for mirror
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    PointList: JointmarkPointsBuilderList = ...
    """
    Returns  the list of points
    
    <hr>
    
    Getter Method
    
    Signature ``PointList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkPointsBuilderList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ProjectionDirectionOption: JointmarkBuilderProjectionDirectionOptions = ...
    """
    Returns or sets  the projection direction option used to project :py:meth:`NXOpen.Weld.JointmarkBuilder.SelectPointsObject` onto the :py:meth:`NXOpen.Weld.JointmarkBuilder.GetReferenceSheet`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionDirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderProjectionDirectionOptions` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ProjectionDirectionOption`` 
    
    :param projectionOption: 
    :type projectionOption: :py:class:`NXOpen.Weld.JointmarkBuilderProjectionDirectionOptions` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ugweld ("UG WELD")
    """
    ReferenceSheetType: JointmarkBuilderReferenceSheetTypes = ...
    """
    Returns or sets  the type of reference sheet
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSheetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderReferenceSheetTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSheetType`` 
    
    :param refSheet: 
    :type refSheet: :py:class:`NXOpen.Weld.JointmarkBuilderReferenceSheetTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReuseFeatures: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the selected reuse features 
    
    <hr>
    
    Getter Method
    
    Signature ``ReuseFeatures`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReuseFeaturesMethod: JointmarkBuilderReuseMethod = ...
    """
    Returns or sets  the method used to infer feature parameters if all connected parts are the same, or skip inferring due to connected parts being different.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReuseFeaturesMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkBuilderReuseMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ReuseFeaturesMethod`` 
    
    :param reuseMethod: 
    :type reuseMethod: :py:class:`NXOpen.Weld.JointmarkBuilderReuseMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    SelectMirrorObject: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects for mirror.  
    
    These objects can be features or curves representing Jointmark 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectMirrorObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SelectPointsObject: NXOpen.SelectPointList = ...
    """
    Returns  the selected objects for Points 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectPointsObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectPointList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SelectTranslateObject: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the selected objects to translate.  
    
    These objects can be features or curves representing Jointmark 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectTranslateObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ShowWorkCsys: bool = ...
    """
    Returns or sets  the option to control if the work coordinate system should be showing.  
    
    <hr>
    
    Getter Method
    
    Signature ``ShowWorkCsys`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowWorkCsys`` 
    
    :param showWorkCsys: 
    :type showWorkCsys: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system that defines the translate offset directions.  
    
    If not specified the absolute csys will be used.
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateCsys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateX: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the x translation distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateX`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    TranslateY: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the y translation distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateY`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TranslateZ: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the z translation distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector which points to Y axis 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: JointmarkBuilder = ...  # unknown typename


class PointMarkBuilderWeldTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PointMarkBuilderWeldTypes():
    """
    The weld type to create. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ResistanceSpot", "Resistance Spot"
       "ArcSpot", "Arc Spot"
       "Clinch", "Clinch"
       "Dollop", "Dollop"
       "WeldNut", "Weld Nut"
       "WeldStud", "Weld Stud"
       "Custom1", "Custom 1 as defined in customer defaults"
       "Custom2", "Custom 2 as defined in customer defaults"
       "Custom3", "Custom 3 as defined in customer defaults"
       "Custom4", "Custom 4 as defined in customer defaults"
       "Custom5", "Custom 5 as defined in customer defaults"
    """
    ResistanceSpot = 0  # PointMarkBuilderWeldTypesMemberType
    ArcSpot = 1  # PointMarkBuilderWeldTypesMemberType
    Clinch = 2  # PointMarkBuilderWeldTypesMemberType
    Dollop = 3  # PointMarkBuilderWeldTypesMemberType
    WeldNut = 4  # PointMarkBuilderWeldTypesMemberType
    WeldStud = 5  # PointMarkBuilderWeldTypesMemberType
    Custom1 = 6  # PointMarkBuilderWeldTypesMemberType
    Custom2 = 7  # PointMarkBuilderWeldTypesMemberType
    Custom3 = 8  # PointMarkBuilderWeldTypesMemberType
    Custom4 = 9  # PointMarkBuilderWeldTypesMemberType
    Custom5 = 10  # PointMarkBuilderWeldTypesMemberType
    
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
    


class PointMarkBuilder(JointmarkBuilder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.PointMark` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreatePointMarkBuilder`
    
    Default values.
    
    =====================  ====================
    Property               Value
    =====================  ====================
    Associativity          1 
    ---------------------  --------------------
    ConnectPart            0 
    ---------------------  --------------------
    ConstructionMethod     GuideCurve 
    ---------------------  --------------------
    CreateSingleFeatures   0 
    ---------------------  --------------------
    OrientationMethod      SurfaceNormal 
    ---------------------  --------------------
    ReferenceSheetType     Overlap 
    ---------------------  --------------------
    ReuseFeaturesMethod    SameConnectingParts 
    ---------------------  --------------------
    ShowWorkCsys           1 
    =====================  ====================
    
    .. versionadded:: NX10.0.0
    """
    
    class WeldTypes():
        """
        The weld type to create. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ResistanceSpot", "Resistance Spot"
           "ArcSpot", "Arc Spot"
           "Clinch", "Clinch"
           "Dollop", "Dollop"
           "WeldNut", "Weld Nut"
           "WeldStud", "Weld Stud"
           "Custom1", "Custom 1 as defined in customer defaults"
           "Custom2", "Custom 2 as defined in customer defaults"
           "Custom3", "Custom 3 as defined in customer defaults"
           "Custom4", "Custom 4 as defined in customer defaults"
           "Custom5", "Custom 5 as defined in customer defaults"
        """
        ResistanceSpot = 0  # PointMarkBuilderWeldTypesMemberType
        ArcSpot = 1  # PointMarkBuilderWeldTypesMemberType
        Clinch = 2  # PointMarkBuilderWeldTypesMemberType
        Dollop = 3  # PointMarkBuilderWeldTypesMemberType
        WeldNut = 4  # PointMarkBuilderWeldTypesMemberType
        WeldStud = 5  # PointMarkBuilderWeldTypesMemberType
        Custom1 = 6  # PointMarkBuilderWeldTypesMemberType
        Custom2 = 7  # PointMarkBuilderWeldTypesMemberType
        Custom3 = 8  # PointMarkBuilderWeldTypesMemberType
        Custom4 = 9  # PointMarkBuilderWeldTypesMemberType
        Custom5 = 10  # PointMarkBuilderWeldTypesMemberType
        
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
        
    
    
    def NewPointsOverride(self) -> PointMarkPointBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.PointMarkPointBuilder` object.  
        
        Signature ``NewPointsOverride()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.PointMarkPointBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def AppendPointsOverride(self, create: bool) -> None:
        """
        Creates a list of points on the overlap sheet.  
        
        In addition, a curve selected by the user will be placed at these points. 
        
        Signature ``AppendPointsOverride(create)`` 
        
        :param create:  Create or Edit  
        :type create: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    ShowSolids: bool = ...
    """
    Returns or sets  the display mode.  
    
    This is only used on create. On edit the display mode will be that of the latest state of the edited features. 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowSolids`` 
    
    :returns:  true- Show Weld.PointMarkPoint features in solid mode. fale- show in point mode. 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ShowSolids`` 
    
    :param showSolids:  true- Show Weld.PointMarkPoint features in solid mode. fale- show in point mode. 
    :type showSolids: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldType: PointMarkBuilderWeldTypes = ...
    """
    Returns or sets  the weld type references in the customer defaults to create.  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.PointMarkBuilderWeldTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``WeldType`` 
    
    :param weldType: 
    :type weldType: :py:class:`NXOpen.Weld.PointMarkBuilderWeldTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: PointMarkBuilder = ...  # unknown typename


class PointMarkPoint(NXOpen.Features.Feature, IFeature):
    """
    Represents a Weld.  
    
    PointMarkPoint Feature. 
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.PointMarkBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetPointMarker(self) -> int:
        """
        Gets the Symbol(Point Marker) information  
        
        Signature ``GetPointMarker()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PointMarkPoint = ...  # unknown typename


class DatumIconBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.DatumIconBuilder` class used to control the part navigator icon for Datum Pin and Surface Locators.  
    
    This class is used to set the Datum Surface or Datum Pin
    icon, but never both at the same time. If the icon is not being set for a feature, that feature will be set to None.
    See example in DatumIconCallback.cxx in ugweld/samples kit. 
    
    .. versionadded:: NX9.0.0
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
    
    CustomType: DatumCommonBuilderCustomTypes = ...
    """
    Returns  the custom datum type from the customer defaults that was used.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumCommonBuilderCustomTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DatumPin: DatumPin = ...
    """
    Returns  the DatumPin feature.  
    
    This will be None if setting the icon for a DatumSurface 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumPin`` 
    
    :returns:  :py:class:`NXOpen.Weld.DatumPin` to assign icon to.  
    :rtype: :py:class:`NXOpen.Weld.DatumPin` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    DatumSurface: DatumSurface = ...
    """
    Returns  the DatumSurface feature.  
    
    This will be None if setting the icon for a DatumPin. 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumSurface`` 
    
    :returns:  :py:class:`NXOpen.Weld.DatumSurface` to assign icon to.  
    :rtype: :py:class:`NXOpen.Weld.DatumSurface` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Derived: bool = ...
    """
    Returns  the indicator if this datum was derived from another datum.  
    
    <hr>
    
    Getter Method
    
    Signature ``Derived`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    IconName: str = ...
    """
    Returns or sets  the bit map name for the icon to be used.  
    
    If the bit map cannot be found a default one will be used. 
    
    <hr>
    
    Getter Method
    
    Signature ``IconName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IconName`` 
    
    :param iconName: 
    :type iconName: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: DatumIconBuilder = ...  # unknown typename


class EdgePrepValuesBuilderOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EdgePrepValuesBuilderOption():
    """
    Option to indicate how the values are to be used. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Entered", "Use the values entered as edge prep values."
       "Computed", "Use the computed values as edge prep values."
    """
    Entered = 0  # EdgePrepValuesBuilderOptionMemberType
    Computed = 1  # EdgePrepValuesBuilderOptionMemberType
    
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
    


class EdgePrepValuesBuilderApplyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EdgePrepValuesBuilderApply():
    """
    Option to indicate how the values are to be updated. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ToAllValues", "Update all values of each selected joint."
       "ToChangedValuesOnly", "Update only the changed values to each selected joint."
    """
    ToAllValues = 0  # EdgePrepValuesBuilderApplyMemberType
    ToChangedValuesOnly = 1  # EdgePrepValuesBuilderApplyMemberType
    
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
    


class EdgePrepValuesBuilder(NXOpen.Builder):
    """
    Used to view or edit the values used to define the welding joint and edge preparation.  
    
    This sub feature is created via the main feature builder.
    
    Default values.
    
    ================================  =====
    Property                          Value
    ================================  =====
    JointExitBuilder.NumberSegments   2 
    --------------------------------  -----
    JointExitBuilder.RootOpening      0 
    --------------------------------  -----
    JointExitBuilder.SplitAngle       5.0 
    --------------------------------  -----
    RootOpening                       0 
    ================================  =====
    
    .. versionadded:: NX8.0.0
    """
    
    class Option():
        """
        Option to indicate how the values are to be used. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Entered", "Use the values entered as edge prep values."
           "Computed", "Use the computed values as edge prep values."
        """
        Entered = 0  # EdgePrepValuesBuilderOptionMemberType
        Computed = 1  # EdgePrepValuesBuilderOptionMemberType
        
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
        
    
    
    class Apply():
        """
        Option to indicate how the values are to be updated. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ToAllValues", "Update all values of each selected joint."
           "ToChangedValuesOnly", "Update only the changed values to each selected joint."
        """
        ToAllValues = 0  # EdgePrepValuesBuilderApplyMemberType
        ToChangedValuesOnly = 1  # EdgePrepValuesBuilderApplyMemberType
        
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
        
    
    
    def RecreateCurves(self) -> None:
        """
        Recreates the curves after changes to edge prep values.  
        
        Signature ``RecreateCurves()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def DeleteExitBuilder(self) -> None:
        """
        Deletes the :py:class:`NXOpen.Weld.JointExitBuilder`.  
        
        Signature ``DeleteExitBuilder()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def ReadEdgePrepValues(self, feature: NXOpen.Features.Feature) -> None:
        """
        Reads the edge prep values from the feature.  
        
        Signature ``ReadEdgePrepValues(feature)`` 
        
        :param feature:  Welding Joint feature  
        :type feature: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def ReadEdgePrepValuesFromCurve(self, curve: NXOpen.Curve) -> None:
        """
        Reads the edge prep values from joint curve.  
        
        Signature ``ReadEdgePrepValuesFromCurve(curve)`` 
        
        :param curve:  Welding Joint curve  
        :type curve: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetSegmentFromIndex(self, value: int) -> NXOpen.Curve:
        """
        Creates the path to be used for the limits.  
        
        Signature ``GetSegmentFromIndex(value)`` 
        
        :param value:  index of curve.  
        :type value: int 
        :returns:  Segment.  
        :rtype: :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    EdgesPrepared: bool = ...
    """
    Returns or sets  the indication that the edges are prepared for welding 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgesPrepared`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EdgesPrepared`` 
    
    :param prepared: 
    :type prepared: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Joint: NXOpen.SelectCurveList = ...
    """
    Returns  the welding joint curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``Joint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectCurveList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    JointExitBuilder: JointExitBuilder = ...
    """
    Returns  the :py:class:`NXOpen.Weld.JointExitBuilder`.  
    
    <hr>
    
    Getter Method
    
    Signature ``JointExitBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointExitBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    PrimaryThicknessUser: float = ...
    """
    Returns or sets  the user defined value for primary thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryThicknessUser`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrimaryThicknessUser`` 
    
    :param thickness: 
    :type thickness: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    RootOpening: float = ...
    """
    Returns or sets  the root opening 
    
    <hr>
    
    Getter Method
    
    Signature ``RootOpening`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RootOpening`` 
    
    :param rootOpening: 
    :type rootOpening: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    SecondaryThicknessUser: float = ...
    """
    Returns or sets  the user defined value for secondary thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryThicknessUser`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondaryThicknessUser`` 
    
    :param thickness: 
    :type thickness: float 
    
    .. versionadded:: NX10.0.2
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    ValueSegment: NXOpen.SelectCurve = ...
    """
    Returns  the selected segment.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValueSegment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectCurve` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ValuesApplyOption: EdgePrepValuesBuilderApply = ...
    """
    Returns or sets  the apply values option which indicates whether the all the values of each selected joint should be updated or just the values that were changed in the :py:class:`NXOpen.Weld.JointExitBuilder`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesApplyOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EdgePrepValuesBuilderApply` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesApplyOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.Weld.EdgePrepValuesBuilderApply` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    ValuesOption: EdgePrepValuesBuilderOption = ...
    """
    Returns or sets  the values option which indicates whether the entered or computed values should be used.  
    
    <hr>
    
    Getter Method
    
    Signature ``ValuesOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EdgePrepValuesBuilderOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ValuesOption`` 
    
    :param option: 
    :type option: :py:class:`NXOpen.Weld.EdgePrepValuesBuilderOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Null: EdgePrepValuesBuilder = ...  # unknown typename


class WeldFillStripBuilder(NXOpen.Builder):
    """
    A builder used to create or edit a single strip of the :py:class:`NXOpen.Weld.WeldFillBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldFillBuilder.NewFillStrip`
    
    .. versionadded:: NX7.5.0
    """
    
    def MoveToPoint(self, newCenter: NXOpen.Point3d) -> None:
        """
        Moves the fill strip to the input center.  
        
        Signature ``MoveToPoint(newCenter)`` 
        
        :param newCenter:  New center of the fill strip  
        :type newCenter: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def MoveDelta(self, lengthDelta: float, widthDelta: float) -> None:
        """
        Moves the fill strip the input length and width values.  
        
        Signature ``MoveDelta(lengthDelta, widthDelta)`` 
        
        :param lengthDelta:  Distance to move strip in the length direction.  
        :type lengthDelta: float 
        :param widthDelta:  Distance to move strip in the width direction.  
        :type widthDelta: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def Split(self) -> WeldFillStripBuilder:
        """
        Splits the fill strip at the center and creates a new strip.  
        
        Signature ``Split()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def StretchPositive(self, lengthDelta: float) -> None:
        """
        Stretches the fill strip the input length in the length direction.  
        
        Signature ``StretchPositive(lengthDelta)`` 
        
        :param lengthDelta:  Distance to stretch the strip in the length direction.  
        :type lengthDelta: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def StretchNegative(self, lengthDelta: float) -> None:
        """
        Stretches the fill strip the input length opposite of the length direction.  
        
        Signature ``StretchNegative(lengthDelta)`` 
        
        :param lengthDelta:  Distance to stretch the strip opposite of the length direction.  
        :type lengthDelta: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def AlignPositive(self, alignStrip: WeldFillStripBuilder) -> None:
        """
        Aligns the end of the fill strip, along the length direction from center, to the
        same end of the input fill strip.  
        
        Signature ``AlignPositive(alignStrip)`` 
        
        :param alignStrip:  Fill strip to align to.  
        :type alignStrip: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def AlignNegative(self, alignStrip: WeldFillStripBuilder) -> None:
        """
        Aligns the end of the fill strip, opposite of the length direction from center, to the
        same end of the input fill strip.  
        
        Signature ``AlignNegative(alignStrip)`` 
        
        :param alignStrip:  Fill strip to align to.  
        :type alignStrip: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def JoinPositive(self, joinStrip: WeldFillStripBuilder) -> None:
        """
        Joins the end of the fill strip, along the length direction from center, to the
        other fill strip input.  
        
        Note the caller must delete the joinStrip if desired. 
        
        Signature ``JoinPositive(joinStrip)`` 
        
        :param joinStrip:  Fill strip to join with.  
        :type joinStrip: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def JoinNegative(self, joinStrip: WeldFillStripBuilder) -> None:
        """
        Joins the end of the fill strip, opposite of the length direction from center, to the
        other fill strip input.  
        
        Note the caller must delete the joinStrip if desired. 
        
        Signature ``JoinNegative(joinStrip)`` 
        
        :param joinStrip:  Fill strip to join with.  
        :type joinStrip: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    Center: NXOpen.Point3d = ...
    """
    Returns  the center of the fill strip.  
    
    <hr>
    
    Getter Method
    
    Signature ``Center`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Length: float = ...
    """
    Returns or sets  the length of the fill strip.  
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Length`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ToBeDeleted: bool = ...
    """
    Returns or sets  the flag indicating that the strip should be deleted.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToBeDeleted`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToBeDeleted`` 
    
    :param flag: 
    :type flag: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: WeldFillStripBuilder = ...  # unknown typename


class WeldSelectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldSelectionType():
    """
    the type of selction 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "General", "general type"
       "Surface", "surface"
       "Curve", "curve"
    """
    General = 0  # WeldSelectionTypeMemberType
    Surface = 1  # WeldSelectionTypeMemberType
    Curve = 2  # WeldSelectionTypeMemberType
    
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
    


class WeldPreferenceBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Weld.WeldPreferenceBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreatePreferenceBuilder`
    
    Default values.
    
    ==========================  =====
    Property                    Value
    ==========================  =====
    CurrentGroupIDColorIndex    None 
    --------------------------  -----
    DatumIdLowerRange           1 
    --------------------------  -----
    DatumIdUpperRange           1000 
    --------------------------  -----
    DatumObjectLayer            255 
    --------------------------  -----
    MeasurementIdLowerRange     1 
    --------------------------  -----
    MeasurementIdUpperRange     1000 
    --------------------------  -----
    MeasurementObjectLayer      255 
    --------------------------  -----
    WeldArcGridLineEndCapDisp   0.1 
    --------------------------  -----
    WeldArcGridLineTopDisp      0.66 
    --------------------------  -----
    WeldConstLayer              231 
    --------------------------  -----
    WeldIdLowerRange            1 
    --------------------------  -----
    WeldIdUpperRange            1000 
    --------------------------  -----
    WeldObjectLayer             255 
    --------------------------  -----
    WeldSymbolDecimalPlaces     3 
    ==========================  =====
    
    .. versionadded:: NX6.0.0
    """
    
    def GetDatumSelectedPrefix(self) -> 'list[str]':
        """
        The datum selected prefix  
        
        Signature ``GetDatumSelectedPrefix()`` 
        
        :returns:  Selected datum prefix  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDatumSelectedPrefix(self, datumSelectedPrefix: 'list[str]') -> None:
        """
        The datum selected prefix 
        
        Signature ``SetDatumSelectedPrefix(datumSelectedPrefix)`` 
        
        :param datumSelectedPrefix:  Selected datum prefix  
        :type datumSelectedPrefix: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetDatumSelectedSuffix(self) -> 'list[str]':
        """
        The datum selected suffix  
        
        Signature ``GetDatumSelectedSuffix()`` 
        
        :returns:  Selected datum suffix  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDatumSelectedSuffix(self, datumSelectedSuffix: 'list[str]') -> None:
        """
        Selected datum suffix 
        
        Signature ``SetDatumSelectedSuffix(datumSelectedSuffix)`` 
        
        :param datumSelectedSuffix:  Selected datum suffix  
        :type datumSelectedSuffix: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMeasurementSelectedPrefix(self) -> 'list[str]':
        """
        The measurement selected prefix  
        
        Signature ``GetMeasurementSelectedPrefix()`` 
        
        :returns:  Selected measurement prefix  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMeasurementSelectedPrefix(self, measurementSelectedPrefix: 'list[str]') -> None:
        """
        The measurement selected prefix 
        
        Signature ``SetMeasurementSelectedPrefix(measurementSelectedPrefix)`` 
        
        :param measurementSelectedPrefix:  Selected measurement prefix  
        :type measurementSelectedPrefix: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMeasurementSelectedSuffix(self) -> 'list[str]':
        """
        The measurement selected suffix  
        
        Signature ``GetMeasurementSelectedSuffix()`` 
        
        :returns:  Selected measurement suffix  
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetMeasurementSelectedSuffix(self, measurementSelectedSuffix: 'list[str]') -> None:
        """
        Selected measurement suffix 
        
        Signature ``SetMeasurementSelectedSuffix(measurementSelectedSuffix)`` 
        
        :param measurementSelectedSuffix:  Selected measurement suffix  
        :type measurementSelectedSuffix: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    CurrentGroupIDColorIndex: WeldGroupIdColor = ...
    """
    Returns or sets  the group idcolor assigned 
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentGroupIDColorIndex`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGroupIdColor` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CurrentGroupIDColorIndex`` 
    
    :param currentGroupIDColorIndex: 
    :type currentGroupIDColorIndex: :py:class:`NXOpen.Weld.WeldGroupIdColor` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumIdLowerRange: int = ...
    """
    Returns or sets  the datum id lower range 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumIdLowerRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumIdLowerRange`` 
    
    :param datumIdLowerRange: 
    :type datumIdLowerRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumIdUpperRange: int = ...
    """
    Returns or sets  the datum id upper range 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumIdUpperRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumIdUpperRange`` 
    
    :param datumIdUpperRange: 
    :type datumIdUpperRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumNamePrefix: str = ...
    """
    Returns or sets  the datum name prefix 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumNamePrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumNamePrefix`` 
    
    :param datumNamePrefix: 
    :type datumNamePrefix: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumObjectColor: NXOpen.NXColor = ...
    """
    Returns or sets  the datum object color 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumObjectColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumObjectColor`` 
    
    :param datumObjectColor: 
    :type datumObjectColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumObjectLayer: int = ...
    """
    Returns or sets  the datum object layer 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumObjectLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumObjectLayer`` 
    
    :param datumObjectLayer: 
    :type datumObjectLayer: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DatumPartNumber: str = ...
    """
    Returns or sets  the datum part number 
    
    <hr>
    
    Getter Method
    
    Signature ``DatumPartNumber`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumPartNumber`` 
    
    :param datumPartNumber: 
    :type datumPartNumber: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementIdLowerRange: int = ...
    """
    Returns or sets  the measurement id lower range 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementIdLowerRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementIdLowerRange`` 
    
    :param measurementIdLowerRange: 
    :type measurementIdLowerRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementIdUpperRange: int = ...
    """
    Returns or sets  the measurement id upper range 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementIdUpperRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementIdUpperRange`` 
    
    :param measurementIdUpperRange: 
    :type measurementIdUpperRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementNamePrefix: str = ...
    """
    Returns or sets  the measurement name prefix 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementNamePrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementNamePrefix`` 
    
    :param measurementNamePrefix: 
    :type measurementNamePrefix: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementObjectColor: NXOpen.NXColor = ...
    """
    Returns or sets  the measurement object color 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementObjectColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementObjectColor`` 
    
    :param measurementObjectColor: 
    :type measurementObjectColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementObjectLayer: int = ...
    """
    Returns or sets  the measurement object layer 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementObjectLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementObjectLayer`` 
    
    :param measurementObjectLayer: 
    :type measurementObjectLayer: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MeasurementPartNumber: str = ...
    """
    Returns or sets  the measurement part number 
    
    <hr>
    
    Getter Method
    
    Signature ``MeasurementPartNumber`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeasurementPartNumber`` 
    
    :param measurementPartNumber: 
    :type measurementPartNumber: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldArcGridLineEndCapDisp: float = ...
    """
    Returns or sets  the weld arc grid line end cap disp 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldArcGridLineEndCapDisp`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldArcGridLineEndCapDisp`` 
    
    :param weldArcGridLineEndCapDisp: 
    :type weldArcGridLineEndCapDisp: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldArcGridLineTopDisp: float = ...
    """
    Returns or sets  the weld arc grid line top disp 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldArcGridLineTopDisp`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldArcGridLineTopDisp`` 
    
    :param weldArcGridLineTopDisp: 
    :type weldArcGridLineTopDisp: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldAssoColor: NXOpen.NXColor = ...
    """
    Returns or sets  the weld asso color 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldAssoColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldAssoColor`` 
    
    :param weldAssoColor: 
    :type weldAssoColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldConstLayer: int = ...
    """
    Returns or sets  the weld const layer 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldConstLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldConstLayer`` 
    
    :param weldConstLayer: 
    :type weldConstLayer: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldFixedColor: NXOpen.NXColor = ...
    """
    Returns or sets  the weld fixed color 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldFixedColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldFixedColor`` 
    
    :param weldFixedColor: 
    :type weldFixedColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldGroupIdLowerRange: str = ...
    """
    Returns or sets  the weld group id lower range 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldGroupIdLowerRange`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldGroupIdLowerRange`` 
    
    :param weldGroupIdLowerRange: 
    :type weldGroupIdLowerRange: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldGroupIdUpperRange: str = ...
    """
    Returns or sets  the weld group id upper range 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldGroupIdUpperRange`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldGroupIdUpperRange`` 
    
    :param weldGroupIdUpperRange: 
    :type weldGroupIdUpperRange: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldIdLowerRange: int = ...
    """
    Returns or sets  the weld id lower range 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldIdLowerRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldIdLowerRange`` 
    
    :param weldIdLowerRange: 
    :type weldIdLowerRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldIdUpperRange: int = ...
    """
    Returns or sets  the weld id upper range 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldIdUpperRange`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldIdUpperRange`` 
    
    :param weldIdUpperRange: 
    :type weldIdUpperRange: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldNamePrefix: str = ...
    """
    Returns or sets  the weld name prefix 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldNamePrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldNamePrefix`` 
    
    :param weldNamePrefix: 
    :type weldNamePrefix: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldObjectLayer: int = ...
    """
    Returns or sets  the weld object layer 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldObjectLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldObjectLayer`` 
    
    :param weldObjectLayer: 
    :type weldObjectLayer: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldPartNumber: str = ...
    """
    Returns or sets  the weld part number 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldPartNumber`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldPartNumber`` 
    
    :param weldPartNumber: 
    :type weldPartNumber: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldRetainedColor: NXOpen.NXColor = ...
    """
    Returns or sets  the weld retained color 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldRetainedColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldRetainedColor`` 
    
    :param weldRetainedColor: 
    :type weldRetainedColor: Id 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldSymbolDecimalPlaces: int = ...
    """
    Returns or sets  the weld sym dec places 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldSymbolDecimalPlaces`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldSymbolDecimalPlaces`` 
    
    :param weldSymbolDecimalPlaces: 
    :type weldSymbolDecimalPlaces: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldPreferenceBuilder = ...  # unknown typename


class JointItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Used to create or edit a :py:class:`Weld.WeldJoint` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldJointBuilder.NewItem`
    
    .. versionadded:: NX8.0.0
    """
    
    def DeleteCurve(self) -> None:
        """
        Deletes the joint curve from the builder.  
        
        Signature ``DeleteCurve()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReadEdgePrepValues(self) -> EdgePrepValuesBuilder:
        """
        Read edge prep values set by the user plugin function.  
        
        Signature ``ReadEdgePrepValues()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.EdgePrepValuesBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def SaveEdgePrepValues(self, valuesBuilder: EdgePrepValuesBuilder) -> None:
        """
        Save edge prep values to the Welding Joint.  
        
        Signature ``SaveEdgePrepValues(valuesBuilder)`` 
        
        :param valuesBuilder: 
        :type valuesBuilder: :py:class:`NXOpen.Weld.EdgePrepValuesBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetPortEngagement(self) -> float:
        """
        Returns the engagement distance of the parent port of the pipe joint  
        
        Signature ``GetPortEngagement()`` 
        
        :returns:  Engagement distance  
        :rtype: float 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def SetCallbackMessage(self, message: str) -> None:
        """
        Sets a message to display after callback processing ends 
        
        Signature ``SetCallbackMessage(message)`` 
        
        :param message:  Message to display to user  
        :type message: str 
        
        .. versionadded:: NX11.0.2
        
        License requirements: structure_weld ("STRUCTURE WELD")
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
    
    BackingFace: NXOpen.ScCollector = ...
    """
    Returns  the backing face.  
    
    <hr>
    
    Getter Method
    
    Signature ``BackingFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Curve: NXOpen.Curve = ...
    """
    Returns  the joint curve 
    
    <hr>
    
    Getter Method
    
    Signature ``Curve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Curve` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Limits: NXOpen.Die.DieLimitsBuilder = ...
    """
    Returns  the limits of the joint curve span.  
    
    <hr>
    
    Getter Method
    
    Signature ``Limits`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Die.DieLimitsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MasterEdge: NXOpen.ScCollector = ...
    """
    Returns  the master edge of a T-joint weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``MasterEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PlacementFace: NXOpen.ScCollector = ...
    """
    Returns  the placement face of a T-joint weld.  
    
    For example, on a profile it is the face that touches the plate. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PrimaryEdge: NXOpen.ScCollector = ...
    """
    Returns  the primary edge of a butt weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    PrimaryFace: NXOpen.ScCollector = ...
    """
    Returns  the primary face of a butt weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrimaryFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    RoutingObject: NXOpen.Routing.SelectPort = ...
    """
    Returns  the routing port.  
    
    <hr>
    
    Getter Method
    
    Signature ``RoutingObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.SelectPort` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SecondaryEdge: NXOpen.ScCollector = ...
    """
    Returns  the secondary edge of a butt weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SecondaryFace: NXOpen.ScCollector = ...
    """
    Returns  the secondary face of a butt weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``SecondaryFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    TargetFace: NXOpen.ScCollector = ...
    """
    Returns  the target face of a T-joint weld.  
    
    For example, the plate face that the profile lies on. 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    UseCallbackValues: bool = ...
    """
    Returns or sets  the indication to use the values of the callback to define the joint 
    
    <hr>
    
    Getter Method
    
    Signature ``UseCallbackValues`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseCallbackValues`` 
    
    :param status: 
    :type status: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    WeldType: int = ...
    """
    Returns or sets  the weld type 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldType`` 
    
    :param type: 
    :type type: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    WeldingCharacteristics: CharacteristicsBuilder = ...
    """
    Returns  the collection of welding characteristics defined by attributes.  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldingCharacteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: JointItemBuilder = ...  # unknown typename


class WeldCustomMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldCustom():
    """
    Settings for output solid type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SolidNone", "creates only a point"
       "SolidSphere", "creates a sphere"
       "SolidCylinder", "creates a cylinder"
       "SolidCone", "creates a cone"
       "SolidDefault", "creates a default solid"
    """
    SolidNone = 0  # WeldCustomMemberType
    SolidSphere = 1  # WeldCustomMemberType
    SolidCylinder = 2  # WeldCustomMemberType
    SolidCone = 3  # WeldCustomMemberType
    SolidDefault = 4  # WeldCustomMemberType
    
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
    


class OutputTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OutputType():
    """
    Settings for output type   
    
    .. versionadded:: NX6.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Associative", "output data will be associated to inputs. If inputs change the outputs will change also"
       "Fixed", "output data will not change if inputs change"
    """
    Associative = 0  # OutputTypeMemberType
    Fixed = 1  # OutputTypeMemberType
    
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
    


class JointmarkFaceSetsBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[JointmarkFaceSetsBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: JointmarkFaceSetsBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
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
    
    
    def FindIndex(self, obj: JointmarkFaceSetsBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> JointmarkFaceSetsBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
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
    def Erase(self, obj: JointmarkFaceSetsBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: JointmarkFaceSetsBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
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
    
    
    def GetContents(self) -> 'list[JointmarkFaceSetsBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[JointmarkFaceSetsBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
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
    def Swap(self, object1: JointmarkFaceSetsBuilder, object2: JointmarkFaceSetsBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: JointmarkFaceSetsBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.JointmarkFaceSetsBuilder` 
        
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
    Null: JointmarkFaceSetsBuilderList = ...  # unknown typename


class WeldPmiBuilderOrientationPlaneTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPmiBuilderOrientationPlaneType():
    """
    This represents the Orientation Plane Type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "XYPlane", " - "
       "XZPlane", " - "
       "YZPlane", " - "
       "ModelView", " - "
       "LastUserDefined", " - "
       "UserDefined", " - "
    """
    XYPlane = 0  # WeldPmiBuilderOrientationPlaneTypeMemberType
    XZPlane = 1  # WeldPmiBuilderOrientationPlaneTypeMemberType
    YZPlane = 2  # WeldPmiBuilderOrientationPlaneTypeMemberType
    ModelView = 3  # WeldPmiBuilderOrientationPlaneTypeMemberType
    LastUserDefined = 4  # WeldPmiBuilderOrientationPlaneTypeMemberType
    UserDefined = 5  # WeldPmiBuilderOrientationPlaneTypeMemberType
    
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
    


class WeldPmiBuilder(NXOpen.Builder):
    """
    Create PMI symbols for multiple structure welds, this builder's Commit can produce more than one object, 
    the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldPmiBuilder`
    
    Default values.
    
    ============  ==========
    Property      Value
    ============  ==========
    PlaneType     ModelView 
    ------------  ----------
    SpaceFactor   1.0 
    ============  ==========
    
    .. versionadded:: NX9.0.0
    """
    
    class OrientationPlaneType():
        """
        This represents the Orientation Plane Type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "XYPlane", " - "
           "XZPlane", " - "
           "YZPlane", " - "
           "ModelView", " - "
           "LastUserDefined", " - "
           "UserDefined", " - "
        """
        XYPlane = 0  # WeldPmiBuilderOrientationPlaneTypeMemberType
        XZPlane = 1  # WeldPmiBuilderOrientationPlaneTypeMemberType
        YZPlane = 2  # WeldPmiBuilderOrientationPlaneTypeMemberType
        ModelView = 3  # WeldPmiBuilderOrientationPlaneTypeMemberType
        LastUserDefined = 4  # WeldPmiBuilderOrientationPlaneTypeMemberType
        UserDefined = 5  # WeldPmiBuilderOrientationPlaneTypeMemberType
        
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
        
    
    Objects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the objects (either features or curves) that are used to create PMI symbols.  
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns:  Selected weld objects list.  
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    PlaneType: WeldPmiBuilderOrientationPlaneType = ...
    """
    Returns or sets  the plane type.  
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPmiBuilderOrientationPlaneType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneType`` 
    
    :param planeType: 
    :type planeType: :py:class:`NXOpen.Weld.WeldPmiBuilderOrientationPlaneType` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    SpaceFactor: float = ...
    """
    Returns or sets  the space factor.  
    
    The value is greater than zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpaceFactor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpaceFactor`` 
    
    :param spaceFactor: 
    :type spaceFactor: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Style: NXOpen.Annotations.StyleBuilder = ...
    """
    Returns  the :py:class:`Annotations.StyleBuilder` for the annotation.  
    
    <hr>
    
    Getter Method
    
    Signature ``Style`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.StyleBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UserCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the user specified coordinate system.  
    
    <hr>
    
    Getter Method
    
    Signature ``UserCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserCoordinateSystem`` 
    
    :param userCsys: 
    :type userCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Null: WeldPmiBuilder = ...  # unknown typename


class GrooveBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Groove Weld feature   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldGrooveBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def SetFirstFacesetStartAdjacentFaces(self, objects: 'list[NXOpen.Face]') -> None:
        """
        Sets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with. 
        
        Signature ``SetFirstFacesetStartAdjacentFaces(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFirstFacesetStartAdjacentFaces(self) -> 'list[NXOpen.Face]':
        """
        Gets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with.  
        
        Signature ``GetFirstFacesetStartAdjacentFaces()`` 
        
        :returns:  the adjacent face reference objects  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: None.
        """
        ...
    
    
    def SetFirstFacesetEndAdjacentFaces(self, objects: 'list[NXOpen.Face]') -> None:
        """
        Sets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with. 
        
        Signature ``SetFirstFacesetEndAdjacentFaces(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFirstFacesetEndAdjacentFaces(self) -> 'list[NXOpen.Face]':
        """
        Gets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with.  
        
        Signature ``GetFirstFacesetEndAdjacentFaces()`` 
        
        :returns:  the adjacent face reference objects  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: None.
        """
        ...
    
    
    def SetSecondFacesetStartAdjacentFaces(self, objects: 'list[NXOpen.Face]') -> None:
        """
        Sets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with. 
        
        Signature ``SetSecondFacesetStartAdjacentFaces(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSecondFacesetStartAdjacentFaces(self) -> 'list[NXOpen.Face]':
        """
        Gets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with.  
        
        Signature ``GetSecondFacesetStartAdjacentFaces()`` 
        
        :returns:  the adjacent face reference objects  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: None.
        """
        ...
    
    
    def SetSecondFacesetEndAdjacentFaces(self, objects: 'list[NXOpen.Face]') -> None:
        """
        Sets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with. 
        
        Signature ``SetSecondFacesetEndAdjacentFaces(objects)`` 
        
        :param objects: 
        :type objects: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSecondFacesetEndAdjacentFaces(self) -> 'list[NXOpen.Face]':
        """
        Gets the adjacent faces of the target solid.  
        
        These faces are used to
        trim the groove weld solid with.  
        
        Signature ``GetSecondFacesetEndAdjacentFaces()`` 
        
        :returns:  the adjacent face reference objects  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           This functionality is no longer supported.
        
        License requirements: None.
        """
        ...
    
    
    def GetContourHeight(self) -> NXOpen.Expression:
        """
        Gets the contour height needed to describe groove weld shape  
        
        Signature ``GetContourHeight()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.ContourHeight`instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetContourHeight(self, contourHeight: str) -> None:
        """
        Sets the contour height needed to describe groove weld 
        
        Signature ``SetContourHeight(contourHeight)`` 
        
        :param contourHeight: 
        :type contourHeight: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.ContourHeight`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetRootOpening(self) -> NXOpen.Expression:
        """
        Gets the root opening height needed to describe groove weld  
        
        Signature ``GetRootOpening()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.RootOpening``instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetRootOpening(self, rootOpening: str) -> None:
        """
        Sets the root opening height needed to describe groove weld 
        
        Signature ``SetRootOpening(rootOpening)`` 
        
        :param rootOpening: 
        :type rootOpening: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.RootOpening``instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetRootPenetration(self) -> NXOpen.Expression:
        """
        Gets the root penetration needed to describe groove weld  
        
        Signature ``GetRootPenetration()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.RootPenetration``instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetRootPenetration(self, rootPenetration: str) -> None:
        """
        Sets the root penetration needed to describe groove weld 
        
        Signature ``SetRootPenetration(rootPenetration)`` 
        
        :param rootPenetration: 
        :type rootPenetration: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.RootPenetration``instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetGrooveAngle(self) -> NXOpen.Expression:
        """
        Gets the groove angle needed to describe groove weld  
        
        Signature ``GetGrooveAngle()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.GrooveAngle`instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetGrooveAngle(self, grooveAngle: str) -> None:
        """
        Sets the groove angle needed to describe groove weld 
        
        Signature ``SetGrooveAngle(grooveAngle)`` 
        
        :param grooveAngle: 
        :type grooveAngle: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.GrooveAngle`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetGrooveRadius(self) -> NXOpen.Expression:
        """
        Gets the groove radius needed to describe groove weld  
        
        Signature ``GetGrooveRadius()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.GrooveRadius`instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetGrooveRadius(self, grooveAngle: str) -> None:
        """
        Sets the groove radius needed to describe groove weld 
        
        Signature ``SetGrooveRadius(grooveAngle)`` 
        
        :param grooveAngle: 
        :type grooveAngle: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.GrooveRadius`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetPenetrationDepth(self) -> NXOpen.Expression:
        """
        Gets the penetration depth needed to describe groove weld  
        
        Signature ``GetPenetrationDepth()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.PenetrationDepth`instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetPenetrationDepth(self, penetrationDepth: str) -> None:
        """
        Sets the penetration depth needed to describe groove weld 
        
        Signature ``SetPenetrationDepth(penetrationDepth)`` 
        
        :param penetrationDepth: 
        :type penetrationDepth: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.PenetrationDepth`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSecondPenetrationDepth(self) -> NXOpen.Expression:
        """
        Gets the second penetration depth needed to describe groove weld.  
        
        This is only needed if face heights are different.  
        
        Signature ``GetSecondPenetrationDepth()`` 
        
        :returns:  expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SecondPenetrationDepth`instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetSecondPenetrationDepth(self, secondPenetrationDepth: str) -> None:
        """
        Sets the penetration depth needed to describe groove weld 
        
        Signature ``SetSecondPenetrationDepth(secondPenetrationDepth)`` 
        
        :param secondPenetrationDepth: 
        :type secondPenetrationDepth: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SecondPenetrationDepth`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetDistanceFromStart(self, startDistance: str) -> None:
        """
        Set the distance from the start of the faces to build the groove weld 
        
        Signature ``SetDistanceFromStart(startDistance)`` 
        
        :param startDistance: 
        :type startDistance: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.StartDistance`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetDistanceFromEnd(self, endDistance: str) -> None:
        """
        Sets the distance from the end of the faces to build the groove weld 
        
        Signature ``SetDistanceFromEnd(endDistance)`` 
        
        :param endDistance: 
        :type endDistance: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EndDistance`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetTaperAtStart(self, startTaper: str) -> None:
        """
        Sets the taper angle at the start.  
        
        A positive number will taper towards
        the inside of the weld. 
        
        Signature ``SetTaperAtStart(startTaper)`` 
        
        :param startTaper: 
        :type startTaper: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.StartAngle`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetTaperAtEnd(self, endTaper: str) -> None:
        """
        Sets the taper angle at the end.  
        
        A positive number will taper towards
        the inside of the weld. 
        
        Signature ``SetTaperAtEnd(endTaper)`` 
        
        :param endTaper: 
        :type endTaper: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EndAngle`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetSpacingDistance(self, spacingDistance: str) -> None:
        """
        Sets the desired spacing between skip welds.  
        
        Signature ``SetSpacingDistance(spacingDistance)`` 
        
        :param spacingDistance: 
        :type spacingDistance: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Spacing`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetNumberOfSegments(self, numSegments: str) -> None:
        """
        Sets the desired number of segments for the groove weld.  
        
        Signature ``SetNumberOfSegments(numSegments)`` 
        
        :param numSegments: 
        :type numSegments: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.NumberOfWelds`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetSegmentLength(self, segmentLength: str) -> None:
        """
        Sets the desired segment lengh for the skip weld.  
        
        Signature ``SetSegmentLength(segmentLength)`` 
        
        :param segmentLength: 
        :type segmentLength: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SegmentLength`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    BottomExtension: WeldGrooveExtension = ...
    """
    Returns or sets  the extension method for the bottom edges 
    
    <hr>
    
    Getter Method
    
    Signature ``BottomExtension`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveExtension` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BottomExtension`` 
    
    :param extensionType: 
    :type extensionType: :py:class:`NXOpen.Weld.WeldGrooveExtension` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    ContourShape: WeldContourShape = ...
    """
    Returns or sets  the contour contour shape.  
    
    This is the shape on the top of the groove weld 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourShape`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldContourShape` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.ContourType`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContourShape`` 
    
    :param contourShape: 
    :type contourShape: :py:class:`NXOpen.Weld.WeldContourShape` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.ContourType`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceFromEnd: NXOpen.Expression = ...
    """
    Returns  the distance from the end of the faces to build the groove weld 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromEnd`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EndDistance`instead.
    
    License requirements: None.
    """
    DistanceFromStart: NXOpen.Expression = ...
    """
    Returns  the distance from the start of the faces to build the groove weld 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromStart`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.StartDistance`instead.
    
    License requirements: None.
    """
    FirstFaceset: NXOpen.ScCollector = ...
    """
    Returns or sets  the first set of faces 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFaceset`` 
    
    :returns:  connected set of faces  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.FaceSet1`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FirstFaceset`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.FaceSet1`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    FirstFacesetBottomEdges: NXOpen.Section = ...
    """
    Returns or sets  the first set bottom edges to extend 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFacesetBottomEdges`` 
    
    :returns:  connected set of edges  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet1`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FirstFacesetBottomEdges`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet1`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    FirstFacesetHelpPoint: NXOpen.Point3d = ...
    """
    Returns or sets  the first set help point.  
    
    If multiple solutions exist, the desired solution 
    used will be the one closest to this point 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFacesetHelpPoint`` 
    
    :returns:  desired solution is closest to this point  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SeedPoint1``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FirstFacesetHelpPoint`` 
    
    :param helpPoint: 
    :type helpPoint: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SeedPoint1``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    FirstFacesetTopEdges: NXOpen.Section = ...
    """
    Returns or sets  the first set top edges to extend 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFacesetTopEdges`` 
    
    :returns:  connected set of edges  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet1`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FirstFacesetTopEdges`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet1`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    GrooveShape: WeldGrooveShape = ...
    """
    Returns or sets  the shape of the groove weld to create 
    
    <hr>
    
    Getter Method
    
    Signature ``GrooveShape`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveShape` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Types`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GrooveShape`` 
    
    :param grooveShape: 
    :type grooveShape: :py:class:`NXOpen.Weld.WeldGrooveShape` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Types`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    GrooveType: WeldGrooveType = ...
    """
    Returns or sets  the groove creation type 
    
    <hr>
    
    Getter Method
    
    Signature ``GrooveType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeType``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GrooveType`` 
    
    :param grooveType: 
    :type grooveType: :py:class:`NXOpen.Weld.WeldGrooveType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeType``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    IsFieldWeld: bool = ...
    """
    Returns or sets  the field weld status.  
    
    If true then this is a field weld,
    if false it is not. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsFieldWeld`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Characteristics`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsFieldWeld`` 
    
    :param fieldWeld: 
    :type fieldWeld: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Characteristics`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    IsFirstFacesetNormalReversed: bool = ...
    """
    Returns or sets  the side of the faceset to build the groove feature.  
    
    The feature will
    be built opposite the face closest to the help point 
    
    <hr>
    
    Getter Method
    
    Signature ``IsFirstFacesetNormalReversed`` 
    
    :returns:  groove weld is built opposite face normal.  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsFirstFacesetNormalReversed`` 
    
    :param reversed: 
    :type reversed: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    IsNumberOfSegments: bool = ...
    """
    Returns or sets  the is number of segments option.  
    
    This is used when creating skip welds to
    compute the spacing between them. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsNumberOfSegments`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsNumberOfSegments`` 
    
    :param isNumberOfSegments: 
    :type isNumberOfSegments: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    IsSecondFacesetNormalReversed: bool = ...
    """
    Returns or sets  the side of the faceset to build the groove feature.  
    
    The feature will
    be built opposite the face closest to the help point 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSecondFacesetNormalReversed`` 
    
    :returns:  groove weld is built opposite face normal.  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSecondFacesetNormalReversed`` 
    
    :param reversed: 
    :type reversed: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    IsSegmentLength: bool = ...
    """
    Returns or sets  the is segment length option.  
    
    This is used when creating skip welds to
    compute the spacing between them. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSegmentLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSegmentLength`` 
    
    :param isSegmentLength: 
    :type isSegmentLength: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    IsSpacing: bool = ...
    """
    Returns or sets  the is spacing option.  
    
    This is used when creating skip welds to 
    compute the spacing between them. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSpacing`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsSpacing`` 
    
    :param isSpacing: 
    :type isSpacing: bool 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Method``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    Method: WeldArcMethod = ...
    """
    Returns or sets  the method 
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldArcMethod` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.CreateSkipWelds``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.WeldArcMethod` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.CreateSkipWelds``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    NumberOfSegments: NXOpen.Expression = ...
    """
    Returns  the number of weld welds for a skip weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfSegments`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.NumberOfWelds`instead.
    
    License requirements: None.
    """
    NumberRequiredFaceSets: int = ...
    """
    Returns or sets  the number of connected parts.  
    
    Either one for two. 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberRequiredFaceSets`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SingleFaceSet``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberRequiredFaceSets`` 
    
    :param numberRequiredFaceSets: 
    :type numberRequiredFaceSets: int 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SingleFaceSet``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    OutputGeometryType: WeldFeatureOutput = ...
    """
    Returns or sets  the output geometry type 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputGeometryType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFeatureOutput` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputGeometryType`` 
    
    :param outputGeometryType: 
    :type outputGeometryType: :py:class:`NXOpen.Weld.WeldFeatureOutput` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    OutputType: OutputType = ...
    """
    Returns or sets  the output type.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.OutputType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputType`` 
    
    :param outputType: 
    :type outputType: :py:class:`NXOpen.Weld.OutputType` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    PrepareEdges: WeldPrepareEdges = ...
    """
    Returns or sets  the apply edge preportion indicator.  
    
    <hr>
    
    Getter Method
    
    Signature ``PrepareEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldPrepareEdges` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.PrepareEdges``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PrepareEdges`` 
    
    :param prepareEdges: 
    :type prepareEdges: :py:class:`NXOpen.Weld.WeldPrepareEdges` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.PrepareEdges``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    RootUpdate: WeldRootUpdate = ...
    """
    Returns or sets  the process type 
    
    <hr>
    
    Getter Method
    
    Signature ``RootUpdate`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldRootUpdate` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RootUpdate`` 
    
    :param rootUpdate: 
    :type rootUpdate: :py:class:`NXOpen.Weld.WeldRootUpdate` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    SecondFaceset: NXOpen.ScCollector = ...
    """
    Returns or sets  the second set of faces 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFaceset`` 
    
    :returns:  connected set of faces  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.FaceSet2`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondFaceset`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.FaceSet2`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    SecondFacesetBottomEdges: NXOpen.Section = ...
    """
    Returns or sets  the second set bottom edges to extend 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFacesetBottomEdges`` 
    
    :returns:  connected set of edges  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet2`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondFacesetBottomEdges`` 
    
    :param edgeCollector: 
    :type edgeCollector: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet2`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    SecondFacesetHelpPoint: NXOpen.Point3d = ...
    """
    Returns or sets  the second set help point.  
    
    If multiple solutions exist, the desired solution 
    used will be the one closest to this point 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFacesetHelpPoint`` 
    
    :returns:  desired solution is closest to this point  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SeedPoint2``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondFacesetHelpPoint`` 
    
    :param helpPoint: 
    :type helpPoint: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SeedPoint2``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    SecondFacesetTopEdges: NXOpen.Section = ...
    """
    Returns or sets  the second set top edges to extend 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFacesetTopEdges`` 
    
    :returns:  connected set of edges  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet2`instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SecondFacesetTopEdges`` 
    
    :param edgeCollector: 
    :type edgeCollector: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EdgeSet2`instead.
    
    License requirements: ugweld ("UG WELD")
    """
    SegmentLength: NXOpen.Expression = ...
    """
    Returns  the segment length for a skip weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentLength`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.SegmentLength`instead.
    
    License requirements: None.
    """
    SequenceNumber: int = ...
    """
    Returns or sets  the sequence number for the groove feature.  
    
    Each groove feature contains a solid.
    If multiple groove wels are to be created, you must specify the sequence of the groove weld you want.
    For example if you are expecting 3 welds to be created. You must create 3 groove weld features.
    The features will have sequence numbers 0,1 and 2.  
    
    <hr>
    
    Getter Method
    
    Signature ``SequenceNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SequenceNumber`` 
    
    :param sequenceNumber: 
    :type sequenceNumber: int 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingDistance: NXOpen.Expression = ...
    """
    Returns  the desired spacing between skip welds.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingDistance`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.Spacing`instead.
    
    License requirements: None.
    """
    TaperAtEnd: NXOpen.Expression = ...
    """
    Returns  the taper angle at the end.  
    
    A positive number will taper towards
    the inside of the weld. 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperAtEnd`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.EndAngle`instead.
    
    License requirements: None.
    """
    TaperAtStart: NXOpen.Expression = ...
    """
    Returns  the taper angle at the start.  
    
    A positive number will taper towards
    the inside of the weld. 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperAtStart`` 
    
    :returns:  expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.StartAngle`instead.
    
    License requirements: None.
    """
    TaperMethod: WeldTaperMethod = ...
    """
    Returns or sets  the taper method to use if tapering is specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``TaperMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldTaperMethod` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.TaperMethod``instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TaperMethod`` 
    
    :param taperMethod: 
    :type taperMethod: :py:class:`NXOpen.Weld.WeldTaperMethod` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       Use :py:meth:`NXOpen.Weld.WeldGrooveBuilder.TaperMethod``instead.
    
    License requirements: ugweld ("UG WELD")
    """
    TopExtension: WeldGrooveExtension = ...
    """
    Returns or sets  the the extension method for the top edges 
    
    <hr>
    
    Getter Method
    
    Signature ``TopExtension`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveExtension` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TopExtension`` 
    
    :param extensionType: 
    :type extensionType: :py:class:`NXOpen.Weld.WeldGrooveExtension` 
    
    .. versionadded:: NX5.0.0
    
    .. deprecated::  NX9.0.0
       This functionality is no longer supported.
    
    License requirements: ugweld ("UG WELD")
    """
    Null: GrooveBuilder = ...  # unknown typename


class JointmarkPointsBuilderPointPositionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkPointsBuilderPointPosition():
    """
    The point classification 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None specifed."
       "MovedAlongGuide", "User moved point from default location along the guide curve"
       "MovedOffGuide", "User moved point from default location off the guide curve"
    """
    NotSet = 0  # JointmarkPointsBuilderPointPositionMemberType
    MovedAlongGuide = 1  # JointmarkPointsBuilderPointPositionMemberType
    MovedOffGuide = 2  # JointmarkPointsBuilderPointPositionMemberType
    
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
    


class JointmarkPointsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Used to create or edit a point in the list of points for Jointmark   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.JointmarkBuilder.NewPoints`
    
    .. versionadded:: NX9.0.0
    """
    
    class PointPosition():
        """
        The point classification 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None specifed."
           "MovedAlongGuide", "User moved point from default location along the guide curve"
           "MovedOffGuide", "User moved point from default location off the guide curve"
        """
        NotSet = 0  # JointmarkPointsBuilderPointPositionMemberType
        MovedAlongGuide = 1  # JointmarkPointsBuilderPointPositionMemberType
        MovedOffGuide = 2  # JointmarkPointsBuilderPointPositionMemberType
        
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
        
    
    
    def UpdateCsys(self, matrix: NXOpen.Matrix3x3) -> None:
        """
        Update the csys using a new matrix.  
        
        Signature ``UpdateCsys(matrix)`` 
        
        :param matrix:  rotate matrix  
        :type matrix: :py:class:`NXOpen.Matrix3x3` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
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
    
    Angle: NXOpen.Expression = ...
    """
    Returns   the angle through which X and Y axis to rotate 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FlipDirection: bool = ...
    """
    Returns or sets  the flip of  Z axis.  
    
    Z axis representing the normal can be flipped 
    
    <hr>
    
    Getter Method
    
    Signature ``FlipDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``FlipDirection`` 
    
    :param flip: 
    :type flip: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MappingFeature: NXOpen.Features.SelectFeature = ...
    """
    Returns  the selected feature to move to the location specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``MappingFeature`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFeature` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the point  at which the feature is created 
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: JointmarkPointsBuilder = ...  # unknown typename


class PointMarkPointBuilder(JointmarkPointsBuilder):
    """
    Used to create or edit a point in the list of points for Jointmark   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.PointMarkBuilder.NewPointsOverride`
    
    .. versionadded:: NX10.0.0
    """
    Null: PointMarkPointBuilder = ...  # unknown typename


class PlugSlot(NXOpen.Features.BodyFeature, IFeature):
    """
    create a PlugSlot feature for Weld   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.PlugSlotBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PlugSlot = ...  # unknown typename


class WeldPointDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointDirection():
    """
    Spot direction 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "StartToEnd", "Direction is from start to end"
       "EndToStart", "Direction is from end to start"
    """
    StartToEnd = 0  # WeldPointDirectionMemberType
    EndToStart = 1  # WeldPointDirectionMemberType
    
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
    


class EasyPatternBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EasyPatternBuilderTypes():
    """
    Controls the type of pattern. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TrimAndSurface", "Trim vector and surface vectors."
       "HemAndSurface", "Hem vector and surface vectors."
    """
    TrimAndSurface = 0  # EasyPatternBuilderTypesMemberType
    HemAndSurface = 1  # EasyPatternBuilderTypesMemberType
    
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
    


class EasyPatternBuilderPlaneMethodTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EasyPatternBuilderPlaneMethodTypes():
    """
    The plane to cut sections in to determine placement measurement patterns. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InferPlanes", "Determine the best XC,YC, or ZC plane."
       "ParallelXCPlanes", "Patterns are on the XC plane."
       "ParallelYCPlanes", "Patterns are on the YC plane."
       "ParallelZCPlanes", "Patterns are on the ZC plane."
    """
    InferPlanes = 0  # EasyPatternBuilderPlaneMethodTypesMemberType
    ParallelXCPlanes = 1  # EasyPatternBuilderPlaneMethodTypesMemberType
    ParallelYCPlanes = 2  # EasyPatternBuilderPlaneMethodTypesMemberType
    ParallelZCPlanes = 3  # EasyPatternBuilderPlaneMethodTypesMemberType
    
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
    


class EasyPatternBuilderSpacingMethodTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EasyPatternBuilderSpacingMethodTypes():
    """
    Indicates whether planes should be cut a grid lines, or if a single plane should be used. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Grid", "Use Grid spacing to cut sections."
       "SinglePlane", "Use a single plane to cut a sections."
    """
    Grid = 0  # EasyPatternBuilderSpacingMethodTypesMemberType
    SinglePlane = 1  # EasyPatternBuilderSpacingMethodTypesMemberType
    
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
    


class EasyPatternBuilderHemMethodTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EasyPatternBuilderHemMethodTypes():
    """
    Indicates the method to use to compute the hem vector location. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MidPoint", "Use the mid point of a section cut."
       "NormalToBody", "Use Normal to Body Method."
    """
    MidPoint = 0  # EasyPatternBuilderHemMethodTypesMemberType
    NormalToBody = 1  # EasyPatternBuilderHemMethodTypesMemberType
    
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
    


class EasyPatternBuilder(NXOpen.Builder):
    """
    Represents the easy pattern builder.  
    
    This is used to create hem, trim and surface measurement
    points at various plane locations. 
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateEasyPatternBuilder`
    
    Default values.
    
    =====================  ===========================================
    Property               Value
    =====================  ===========================================
    BackEdgeOffset         2 (millimeters part), 0.08 (inches part) 
    ---------------------  -------------------------------------------
    GridAngleTolerance     15 
    ---------------------  -------------------------------------------
    GridIncrement          25 (millimeters part), 1.0 (inches part) 
    ---------------------  -------------------------------------------
    Height                 25 (millimeters part), 1.0 (inches part) 
    ---------------------  -------------------------------------------
    HemMethod              MidPoint 
    ---------------------  -------------------------------------------
    LengthAndWidth         5 (millimeters part), 0.02 (inches part) 
    ---------------------  -------------------------------------------
    MaximumSpacing         20 (millimeters part), 0.8 (inches part) 
    ---------------------  -------------------------------------------
    MinimumFlangeWidth     6.0 (millimeters part), 0.25 (inches part) 
    ---------------------  -------------------------------------------
    NumberSurfaceVectors   1 
    ---------------------  -------------------------------------------
    PlaneLocation          0 
    ---------------------  -------------------------------------------
    PlaneMethod            InferPlanes 
    ---------------------  -------------------------------------------
    SpacingMethod          Grid 
    ---------------------  -------------------------------------------
    TrimEdgeOffset         2 (millimeters part), 0.08 (inches part) 
    =====================  ===========================================
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        Controls the type of pattern. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TrimAndSurface", "Trim vector and surface vectors."
           "HemAndSurface", "Hem vector and surface vectors."
        """
        TrimAndSurface = 0  # EasyPatternBuilderTypesMemberType
        HemAndSurface = 1  # EasyPatternBuilderTypesMemberType
        
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
        
    
    
    class PlaneMethodTypes():
        """
        The plane to cut sections in to determine placement measurement patterns. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InferPlanes", "Determine the best XC,YC, or ZC plane."
           "ParallelXCPlanes", "Patterns are on the XC plane."
           "ParallelYCPlanes", "Patterns are on the YC plane."
           "ParallelZCPlanes", "Patterns are on the ZC plane."
        """
        InferPlanes = 0  # EasyPatternBuilderPlaneMethodTypesMemberType
        ParallelXCPlanes = 1  # EasyPatternBuilderPlaneMethodTypesMemberType
        ParallelYCPlanes = 2  # EasyPatternBuilderPlaneMethodTypesMemberType
        ParallelZCPlanes = 3  # EasyPatternBuilderPlaneMethodTypesMemberType
        
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
        
    
    
    class SpacingMethodTypes():
        """
        Indicates whether planes should be cut a grid lines, or if a single plane should be used. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Grid", "Use Grid spacing to cut sections."
           "SinglePlane", "Use a single plane to cut a sections."
        """
        Grid = 0  # EasyPatternBuilderSpacingMethodTypesMemberType
        SinglePlane = 1  # EasyPatternBuilderSpacingMethodTypesMemberType
        
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
        
    
    
    class HemMethodTypes():
        """
        Indicates the method to use to compute the hem vector location. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MidPoint", "Use the mid point of a section cut."
           "NormalToBody", "Use Normal to Body Method."
        """
        MidPoint = 0  # EasyPatternBuilderHemMethodTypesMemberType
        NormalToBody = 1  # EasyPatternBuilderHemMethodTypesMemberType
        
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
        
    
    BackEdgeOffset: float = ...
    """
    Returns or sets  the back edge offset.  
    
    This offset distance is measured from the end of the section cut curve. The start of the curve is at path curve specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``BackEdgeOffset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BackEdgeOffset`` 
    
    :param backEdgeOffset: 
    :type backEdgeOffset: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance.  
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    GridAngleTolerance: float = ...
    """
    Returns or sets  the grid angle tolerance.  
    
    This is used for the inferred grid spacing method.  
    
    <hr>
    
    Getter Method
    
    Signature ``GridAngleTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridAngleTolerance`` 
    
    :param gridAngleTolerance: 
    :type gridAngleTolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    GridIncrement: float = ...
    """
    Returns or sets  the grid increment.  
    
    The grid spacing value use to generate planes. 
    
    <hr>
    
    Getter Method
    
    Signature ``GridIncrement`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridIncrement`` 
    
    :param gridIncrement: 
    :type gridIncrement: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Height: float = ...
    """
    Returns or sets  the height of the measurement solid to create.  
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Height`` 
    
    :param height: 
    :type height: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    HemMethod: EasyPatternBuilderHemMethodTypes = ...
    """
    Returns or sets  the hem method.  
    
    This controls the method used for determining the hem point location and vector direction. 
    
    <hr>
    
    Getter Method
    
    Signature ``HemMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EasyPatternBuilderHemMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HemMethod`` 
    
    :param hemMethod: 
    :type hemMethod: :py:class:`NXOpen.Weld.EasyPatternBuilderHemMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    LengthAndWidth: float = ...
    """
    Returns or sets  the length and width of the measurement solid to create.  
    
    <hr>
    
    Getter Method
    
    Signature ``LengthAndWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LengthAndWidth`` 
    
    :param lengthAndWidth: 
    :type lengthAndWidth: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    MaximumSpacing: float = ...
    """
    Returns or sets  the maximum spacing between the trim edge offset and the back edge offset.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumSpacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.5
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumSpacing`` 
    
    :param maximumSpacing: 
    :type maximumSpacing: float 
    
    .. versionadded:: NX7.5.5
    
    License requirements: ugweld ("UG WELD")
    """
    MinimumFlangeWidth: float = ...
    """
    Returns or sets  the value used to control when only one surface measurement vector will be created.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumFlangeWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumFlangeWidth`` 
    
    :param minimumFlangeWidth: 
    :type minimumFlangeWidth: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: ugweld ("UG WELD")
    """
    NumberSurfaceVectors: int = ...
    """
    Returns or sets  the number surface vectors to create for each pattern.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberSurfaceVectors`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberSurfaceVectors`` 
    
    :param numberSurfaceVectors: 
    :type numberSurfaceVectors: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PatternPath: NXOpen.Section = ...
    """
    Returns  the pattern path.  
    
    This path is used to determine the pattern spacing. 
    
    <hr>
    
    Getter Method
    
    Signature ``PatternPath`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PlaneLocation: float = ...
    """
    Returns or sets  the plane location.  
    
    The single plane location to create a pattern. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneLocation`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneLocation`` 
    
    :param planeLocation: 
    :type planeLocation: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PlaneMethod: EasyPatternBuilderPlaneMethodTypes = ...
    """
    Returns or sets  the plane method.  
    
    This is used to control plane orientations for the measurement points. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EasyPatternBuilderPlaneMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneMethod`` 
    
    :param planeMethod: 
    :type planeMethod: :py:class:`NXOpen.Weld.EasyPatternBuilderPlaneMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the reverse direction.  
    
    This will reverse direction of all measurement points created. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingMethod: EasyPatternBuilderSpacingMethodTypes = ...
    """
    Returns or sets  the spacing method.  
    
    This method controls whether multiple patterns are created or a single pattern. 
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EasyPatternBuilderSpacingMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingMethod`` 
    
    :param spacingMethod: 
    :type spacingMethod: :py:class:`NXOpen.Weld.EasyPatternBuilderSpacingMethodTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SurfaceVectorFace: NXOpen.ScCollector = ...
    """
    Returns  the surface vector face.  
    
    This is the face surface vectors will be created on. 
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceVectorFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TrimEdgeOffset: float = ...
    """
    Returns or sets  the trim edge offset distance.  
    
    This is the offset distance from the path specified. 
    
    <hr>
    
    Getter Method
    
    Signature ``TrimEdgeOffset`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimEdgeOffset`` 
    
    :param trimEdgeOffset: 
    :type trimEdgeOffset: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Type: EasyPatternBuilderTypes = ...
    """
    Returns or sets  the type of pattern to created.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.EasyPatternBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.EasyPatternBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: EasyPatternBuilder = ...  # unknown typename


class Groove(NXOpen.Features.Feature, IFeature):
    """
    Represents a WeldGroove feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.GrooveBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Groove = ...  # unknown typename


class WeldManager(NXOpen.TaggedObjectCollection):
    """
    Manages weld features and assistant tools.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Features.FeatureCollection`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateWeldGrooveBuilder(self, weldGroove: NXOpen.Features.Feature) -> GrooveBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.GrooveBuilder` object.  
        
        Signature ``CreateWeldGrooveBuilder(weldGroove)`` 
        
        :param weldGroove:  Groove Weld to be edited, if None then create a new one  
        :type weldGroove: :py:class:`NXOpen.Features.Feature` 
        :returns:  WeldGroove feature builder 
        :rtype: :py:class:`NXOpen.Weld.GrooveBuilder` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:class:`NXOpen.Weld.WeldGrooveBuilder`instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateWeldPointBuilder(self, weldPoint: NXOpen.Features.Feature) -> WeldPointBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldPointBuilder` object.  
        
        Signature ``CreateWeldPointBuilder(weldPoint)`` 
        
        :param weldPoint:  :py:class:`NXOpen.Weld.WeldPointBuilder`                                                          to be edited, if None then create a new one  
        :type weldPoint: :py:class:`NXOpen.Features.Feature` 
        :returns:  WeldPoint feature builder 
        :rtype: :py:class:`NXOpen.Weld.WeldPointBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateImportBuilder(self) -> WeldImportBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldImportBuilder` object.  
        
        Signature ``CreateImportBuilder()`` 
        
        :returns:  Import weld builder  
        :rtype: :py:class:`NXOpen.Weld.WeldImportBuilder` 
        
        .. versionadded:: NX7.5.1
        
        License requirements: None.
        """
        ...
    
    
    def CreateJointBuilder(self, weldJoint: WeldJoint) -> WeldJointBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldJointBuilder`  
        
        Signature ``CreateJointBuilder(weldJoint)`` 
        
        :param weldJoint:  :py:class:`NXOpen.Weld.WeldJoint` to be edited  
        :type weldJoint: :py:class:`NXOpen.Weld.WeldJoint` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldJointBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateJointExitBuilder(self, weldJoint: WeldJoint) -> JointExitBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointExitBuilder`  
        
        Signature ``CreateJointExitBuilder(weldJoint)`` 
        
        :param weldJoint:  :py:class:`NXOpen.Weld.WeldJoint` to be edited  
        :type weldJoint: :py:class:`NXOpen.Weld.WeldJoint` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointExitBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateJointExitBuilderCurve(self, curve: NXOpen.Curve) -> JointExitBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointExitBuilder` using the curve of a :py:class:`NXOpen.Weld.WeldJoint`  
        
        Signature ``CreateJointExitBuilderCurve(curve)`` 
        
        :param curve: 
        :type curve: :py:class:`NXOpen.Curve` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointExitBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateExportWeldBuilder(self) -> ExportWeldBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.ExportWeldBuilder` object.  
        
        Signature ``CreateExportWeldBuilder()`` 
        
        :returns:  ExportWeld assistant builder 
        :rtype: :py:class:`NXOpen.Weld.ExportWeldBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateEdgePrepValuesBuilder(self) -> EdgePrepValuesBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.EdgePrepValuesBuilder` object.  
        
        Signature ``CreateEdgePrepValuesBuilder()`` 
        
        :returns:  Edge Prep Values builder 
        :rtype: :py:class:`NXOpen.Weld.EdgePrepValuesBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateAutoPointBuilder(self, unused: NXOpen.Features.Feature) -> AutoPointBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.AutoPointBuilder` object.  
        
        Signature ``CreateAutoPointBuilder(unused)`` 
        
        :param unused:  Builder only creates  
        :type unused: :py:class:`NXOpen.Features.Feature` 
        :returns:  AutoPoint assistant builder 
        :rtype: :py:class:`NXOpen.Weld.AutoPointBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreatePreferenceBuilder(self) -> WeldPreferenceBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldPreferenceBuilder` object.  
        
        Signature ``CreatePreferenceBuilder()`` 
        
        :returns:  WeldPref assistant builder 
        :rtype: :py:class:`NXOpen.Weld.WeldPreferenceBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateUserDefinedWeldBuilder(self, featureSet: NXOpen.Features.Feature) -> UserDefinedWeldBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.UserDefinedWeldBuilder`  
        
        Signature ``CreateUserDefinedWeldBuilder(featureSet)`` 
        
        :param featureSet:  Builder only creates  
        :type featureSet: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.UserDefinedWeldBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    @typing.overload
    def CreateCharacteristicsBuilder(self, object: NXOpen.NXObject, weldType: int) -> CharacteristicsBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.CharacteristicsBuilder`, used to specify
        welding characteristics for any welding feature.  
        
        Signature ``CreateCharacteristicsBuilder(object, weldType)`` 
        
        :param object:  object having attributes to be edited.  
        :type object: :py:class:`NXOpen.NXObject` 
        :param weldType:  type of weld feature being created/edited, see uf_weld_types.h.  
        :type weldType: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.0
           Use overloaded function with enum instead.
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    @typing.overload
    def CreateCharacteristicsBuilder(self, object: NXOpen.NXObject, charxType: CharacteristicsBuilderType) -> CharacteristicsBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.CharacteristicsBuilder`, used to specify
        welding characteristics for any welding feature.  
        
        Signature ``CreateCharacteristicsBuilder(object, charxType)`` 
        
        :param object:  object having attributes to be edited.  
        :type object: :py:class:`NXOpen.NXObject` 
        :param charxType:  The type of characteristics being processed  
        :type charxType: :py:class:`NXOpen.Weld.CharacteristicsBuilderType` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateWeldAdvisorBuilder(self) -> WeldAdvisorBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldAdvisorBuilder` object.  
        
        Signature ``CreateWeldAdvisorBuilder()`` 
        
        :returns:  Weld Advisor builder 
        :rtype: :py:class:`NXOpen.Weld.WeldAdvisorBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateFillBuilder(self, fillFeature: Fill) -> WeldFillBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldFillBuilder`, used to create or edit
        a :py:class:`NXOpen.Weld.Fill` feature.  
        
        Signature ``CreateFillBuilder(fillFeature)`` 
        
        :param fillFeature:  :py:class:`NXOpen.Weld.Fill` to be edited  
        :type fillFeature: :py:class:`NXOpen.Weld.Fill` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldFillBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateWeldBeadBuilder(self, beadFeature: NXOpen.Features.Feature) -> WeldBeadBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldBeadBuilder` object.  
        
        Signature ``CreateWeldBeadBuilder(beadFeature)`` 
        
        :param beadFeature:  Weld Bead to be edited  
        :type beadFeature: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldBeadBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateEasyPatternBuilder(self, patternFeatureSet: NXOpen.Features.Feature) -> EasyPatternBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.EasyPatternBuilder` object.  
        
        Signature ``CreateEasyPatternBuilder(patternFeatureSet)`` 
        
        :param patternFeatureSet:  Pattern feature set.   
        :type patternFeatureSet: :py:class:`NXOpen.Features.Feature` 
        :returns:  EasyPattern assistant builder 
        :rtype: :py:class:`NXOpen.Weld.EasyPatternBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreatePlugSlotBuilder(self, feature: NXOpen.Features.Feature) -> PlugSlotBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.PlugSlotBuilder` object.  
        
        Signature ``CreatePlugSlotBuilder(feature)`` 
        
        :param feature:  Weld PlugSlott to be edited  
        :type feature: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.PlugSlotBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateFilletBuilder(self, feature: NXOpen.Features.Feature) -> FilletBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.FilletBuilder` object.  
        
        Signature ``CreateFilletBuilder(feature)`` 
        
        :param feature:  Weld Fillet to be edited  
        :type feature: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.FilletBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateEdgePrepBuilder(self, edgePrepFeature: EdgePrep) -> EdgePrepBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.EdgePrepBuilder` object.  
        
        Signature ``CreateEdgePrepBuilder(edgePrepFeature)`` 
        
        :param edgePrepFeature:  Weld Edge Prep Feature to be edited  
        :type edgePrepFeature: :py:class:`NXOpen.Weld.EdgePrep` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.EdgePrepBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateAutoWeldSymbolsBuilder(self) -> AutoWeldSymbolsBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.AutoWeldSymbolsBuilder` object.  
        
        Signature ``CreateAutoWeldSymbolsBuilder()`` 
        
        :returns:  Auto Weld Symbol assistant builder 
        :rtype: :py:class:`NXOpen.Weld.AutoWeldSymbolsBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateWeldObjectBuilder(self) -> WeldObjectBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldObjectBuilder` object.  
        
        Signature ``CreateWeldObjectBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldObjectBuilder` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateExportWeldJointBuilder(self) -> ExportWeldJointBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.ExportWeldJointBuilder` object.  
        
        Signature ``CreateExportWeldJointBuilder()`` 
        
        :returns:  Export Weld Joint builder 
        :rtype: :py:class:`NXOpen.Weld.ExportWeldJointBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateDatumSurfaceBuilder(self, feature: DatumSurface) -> DatumSurfaceBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.DatumSurfaceBuilder` object.  
        
        Signature ``CreateDatumSurfaceBuilder(feature)`` 
        
        :param feature:  :py:class:`NXOpen.Weld.DatumSurface` to be edited  
        :type feature: :py:class:`NXOpen.Weld.DatumSurface` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.DatumSurfaceBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateDatumPinBuilder(self, feature: DatumPin) -> DatumPinBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.DatumPinBuilder` object.  
        
        Signature ``CreateDatumPinBuilder(feature)`` 
        
        :param feature:  :py:class:`NXOpen.Weld.DatumPin` to be edited  
        :type feature: :py:class:`NXOpen.Weld.DatumPin` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.DatumPinBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateWeldLabelBuilder(self, annotation: NXOpen.Annotations.Annotation) -> WeldLabelBuilder:
        """
        The welding annotation to edit, otherwise if None, then create a new one  
        
        Signature ``CreateWeldLabelBuilder(annotation)`` 
        
        :param annotation:  The Welding annotation.  
        :type annotation: :py:class:`NXOpen.Annotations.Annotation` 
        :returns:  weld label builder 
        :rtype: :py:class:`NXOpen.Weld.WeldLabelBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateWeldGroove1Builder(self, grooveFeature: NXOpen.Features.Feature) -> WeldGrooveBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldGrooveBuilder` object.  
        
        Signature ``CreateWeldGroove1Builder(grooveFeature)`` 
        
        :param grooveFeature:  Weld Groove to be edited  
        :type grooveFeature: :py:class:`NXOpen.Features.Feature` 
        :returns:       
        :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateWeldPointExitBuilder(self) -> WeldPointExitBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldPointExitBuilder` object.  
        
        Signature ``CreateWeldPointExitBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldPointExitBuilder` 
        
        .. versionadded:: NX8.0.2
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateJointmarkBuilder(self, jointmarkFeature: Jointmark) -> JointmarkBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointmarkBuilder` object.  
        
        Signature ``CreateJointmarkBuilder(jointmarkFeature)`` 
        
        :param jointmarkFeature:  Jointmark to be edited  
        :type jointmarkFeature: :py:class:`NXOpen.Weld.Jointmark` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointmarkBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def EditSingleJointmarkFeature(self, elementFeature: NXOpen.Features.Feature) -> JointmarkBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.JointmarkBuilder` object from a single element feature.  
        
        Signature ``EditSingleJointmarkFeature(elementFeature)`` 
        
        :param elementFeature:  Single jointmark element to be edited  
        :type elementFeature: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.JointmarkBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateSurfaceWeldBuilder(self, surfaceWeld: SurfaceWeld) -> SurfaceWeldBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.SurfaceWeldBuilder`  
        
        Signature ``CreateSurfaceWeldBuilder(surfaceWeld)`` 
        
        :param surfaceWeld:  :py:class:`NXOpen.Weld.SurfaceWeld` to be edited.  
        
        None to create a new surface weld.  
        :type surfaceWeld: :py:class:`NXOpen.Weld.SurfaceWeld` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.SurfaceWeldBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateConnectedFaceFinderOperation(self) -> ConnectedFaceFinderBuilder:
        """
        Creates a builder for running the Connected Face Finder utility.  
        
        Signature ``CreateConnectedFaceFinderOperation()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.ConnectedFaceFinderBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateConnectedFaceFinderBuilder(self, weldFeatures: 'list[NXOpen.Features.Feature]') -> ConnectedFaceFinderBuilder:
        """
        Creates a builder for running the Connected Face Finder utility.  
        
        Only used internally for Mirror or Transform on the fly.  
        
        Signature ``CreateConnectedFaceFinderBuilder(weldFeatures)`` 
        
        :param weldFeatures:  MUST be an set of weld features used for Mirror or Translate on the fly.  
        :type weldFeatures: list of :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.ConnectedFaceFinderBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateCompoundWeldBuilder(self, compoundWeld: CompoundWeld) -> CompoundWeldBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.CompoundWeldBuilder`  
        
        Signature ``CreateCompoundWeldBuilder(compoundWeld)`` 
        
        :param compoundWeld:  :py:class:`NXOpen.Weld.CompoundWeld` to be edited  
        :type compoundWeld: :py:class:`NXOpen.Weld.CompoundWeld` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CompoundWeldBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateInformationBuilder(self) -> InformationBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.InformationBuilder`  
        
        Signature ``CreateInformationBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.InformationBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreateWeldPmiBuilder(self) -> WeldPmiBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldPmiBuilder` object.  
        
        Signature ``CreateWeldPmiBuilder()`` 
        
        :returns:  weld PMI builder 
        :rtype: :py:class:`NXOpen.Weld.WeldPmiBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def CreatePointMarkBuilder(self, pointMarkFeature: PointMark) -> PointMarkBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.PointMarkBuilder` object.  
        
        Signature ``CreatePointMarkBuilder(pointMarkFeature)`` 
        
        :param pointMarkFeature:  PointMark feature to be edited  
        :type pointMarkFeature: :py:class:`NXOpen.Weld.PointMark` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.PointMarkBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def EditSinglePointMarkFeature(self, elementFeature: PointMarkPoint) -> PointMarkBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.PointMarkBuilder` object from a single element feature.  
        
        Signature ``EditSinglePointMarkFeature(elementFeature)`` 
        
        :param elementFeature:  Single PointMarkPoints element to be edited  
        :type elementFeature: :py:class:`NXOpen.Weld.PointMarkPoint` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.PointMarkBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateLocatorReferenceBuilder(self) -> LocatorReferenceBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.LocatorReferenceBuilder`  
        
        Signature ``CreateLocatorReferenceBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.LocatorReferenceBuilder` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateBeadDesignFeature(self) -> None:
        """
        Create a Weld Bead Design Feature part and make it the session work part.  
        
        The design feature will be created in the active subset work part. 
        
        Signature ``CreateBeadDesignFeature()`` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateTransformBuilder(self, feature: Transform) -> TransformBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.TransformBuilder` object.  
        
        Signature ``CreateTransformBuilder(feature)`` 
        
        :param feature:  Feature to be edited  
        :type feature: :py:class:`NXOpen.Weld.Transform` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.TransformBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    


class ConnectedFaceFinderBuilder(NXOpen.Builder):
    """
    Represents a builder to run the Connected Face Finder operation.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateConnectedFaceFinderBuilder`
    
    Default values.
    
    ========================================  =====
    Property                                  Value
    ========================================  =====
    ConnectionFinder.Filter                   All 
    ----------------------------------------  -----
    ConnectionFinder.ListFeatureSet           1 
    ----------------------------------------  -----
    ConnectionFinder.UpdateCoordinateSystem   1 
    ========================================  =====
    
    .. versionadded:: NX9.0.0
    """
    
    def PerformAnalysis(self) -> None:
        """
        Process the selected retained welds and populate the list with appropriate faces to reconnect the weld too.  
        
        Signature ``PerformAnalysis()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    ConnectionFinder: ConnectionFinderBuilder = ...
    """
    Returns  the connection finder object that manages the interaction.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectionFinder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.ConnectionFinderBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ListFeatureSet: bool = ...
    """
    Returns or sets  the option if set to true will list the search results according to the feature sets that the specified weld point belongs to.  
    
    <hr>
    
    Getter Method
    
    Signature ``ListFeatureSet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListFeatureSet`` 
    
    :param listFeatureSet: 
    :type listFeatureSet: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RetainedWelds: NXOpen.SelectTaggedObjectList = ...
    """
    Returns  the retained weld objects that need to be reconnected.  
    
    <hr>
    
    Getter Method
    
    Signature ``RetainedWelds`` 
    
    :returns:  Weld Feature tag.  
    :rtype: :py:class:`NXOpen.SelectTaggedObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: ConnectedFaceFinderBuilder = ...  # unknown typename


class CustomManager(NXOpen.TaggedObjectCollection):
    """
    Represents weld interface to customize the creation of welding joint features.  
    
    The "welding joint handler" customization callback is called after the feature is created.
    One can then set edge preparation parameters, change the color of the feature output curve,
    add attributes to the feature, or any additional customization.
    
    The "variable bevel handler" customization callback is used to define the limits where a welding joint
    should be split at. 
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def AddWeldJointHandler(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method that is called whenever a welding joint is created or updated  
        
        Signature ``AddWeldJointHandler(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveWeldJointHandler(self, id: int) -> None:
        """
        Unregisters the welding joint handler 
        
        Signature ``RemoveWeldJointHandler(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddVariableBevelHandler(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method to define variable bevel angles.  
        
        The method will be called from the Weld Joint user Interface.  
        
        Signature ``AddVariableBevelHandler(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveVariableBevelHandler(self, id: int) -> None:
        """
        Unregisters the variable bevel handler 
        
        Signature ``RemoveVariableBevelHandler(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddModifyFeatureHandler(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method to be notified when weld features are created or edited.  
        
        Signature ``AddModifyFeatureHandler(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def RemoveModifyFeatureHandler(self, id: int) -> None:
        """
        Unregisters the modify feature handler 
        
        Signature ``RemoveModifyFeatureHandler(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def AddPointExitHandler(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method to be notified when weld point features are created.  
        
        Signature ``AddPointExitHandler(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX8.0.2
        
        License requirements: None.
        """
        ...
    
    
    def RemovePointExitHandler(self, id: int) -> None:
        """
        Unregisters the point feature handler 
        
        Signature ``RemovePointExitHandler(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX8.0.2
        
        License requirements: None.
        """
        ...
    
    
    def AddDatumIconHandler(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method to be notified when the part navigator is updating the surface or pin datum icon.  
        
        Signature ``AddDatumIconHandler(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveDatumIconHandler(self, id: int) -> None:
        """
        Unregisters the datum common icon handler 
        
        Signature ``RemoveDatumIconHandler(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddPipeJointSetType(self, handler: typing.Callable) -> int:
        """
        Registers a user defined method that is called whenever a welding joint is created  
        
        Signature ``AddPipeJointSetType(handler)`` 
        
        :param handler:  method to register  
        :type handler: CallableObject 
        :returns:  identifier of registered method (used to unregister the method)  
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemovePipeJointSetType(self, id: int) -> None:
        """
        Unregisters the pipe joint set type handler 
        
        Signature ``RemovePipeJointSetType(id)`` 
        
        :param id:  identifier for method to unregister  
        :type id: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ShowSolids(self, showSolids: bool) -> None:
        """
        Method to change display mode of all Weld.  
        
        PointMarkPoint feature that are fully loaded in an assembly 
        
        Signature ``ShowSolids(showSolids)`` 
        
        :param showSolids:  true to show solids, false to show points.  
        :type showSolids: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def LocateWelds(self, searchEntireAssembly: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool) -> 'list[NXOpen.NXObject]':
        """
        Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output 
        
        Signature ``LocateWelds(searchEntireAssembly, wantSolids, wantCurves, wantPoints)`` 
        
        :param searchEntireAssembly: 
        :type searchEntireAssembly: bool 
        :param wantSolids: 
        :type wantSolids: bool 
        :param wantCurves: 
        :type wantCurves: bool 
        :param wantPoints: 
        :type wantPoints: bool 
        :returns:  Array of objects passing the search criteria specified.  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def LocateWelds(self, searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool) -> 'list[NXOpen.NXObject]':
        """
        Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output 
        
        Signature ``LocateWelds(searchEntireAssembly, excludeInvisibleComponents, wantSolids, wantCurves, wantPoints)`` 
        
        :param searchEntireAssembly: 
        :type searchEntireAssembly: bool 
        :param excludeInvisibleComponents: 
        :type excludeInvisibleComponents: bool 
        :param wantSolids: 
        :type wantSolids: bool 
        :param wantCurves: 
        :type wantCurves: bool 
        :param wantPoints: 
        :type wantPoints: bool 
        :returns:  Array of objects passing the search criteria specified.  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def LocateWelds(self, searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool, wantStructureWelds: bool) -> 'list[NXOpen.NXObject]':
        """
        Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output. Structure welds can also be included in the search. 
        
        Signature ``LocateWelds(searchEntireAssembly, excludeInvisibleComponents, wantSolids, wantCurves, wantPoints, wantStructureWelds)`` 
        
        :param searchEntireAssembly: 
        :type searchEntireAssembly: bool 
        :param excludeInvisibleComponents: 
        :type excludeInvisibleComponents: bool 
        :param wantSolids: 
        :type wantSolids: bool 
        :param wantCurves: 
        :type wantCurves: bool 
        :param wantPoints: 
        :type wantPoints: bool 
        :param wantStructureWelds: 
        :type wantStructureWelds: bool 
        :returns:  Array of objects passing the search criteria specified.  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def ConvertLegacy(self) -> None:
        """
        Method to convert all legacy weld points to the :py:class:`NXOpen.Weld.PointMarkPoint` class 
        
        Signature ``ConvertLegacy()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ConvertLegacy(self, fsetFeatures: 'list[NXOpen.Features.Feature]') -> None:
        """
        Method to convert selected legacy weld point feature sets to the :py:class:`NXOpen.Weld.PointMarkPoint` class 
        
        Signature ``ConvertLegacy(fsetFeatures)`` 
        
        :param fsetFeatures:  The pre-NX10 weld feature sets to convert 
        :type fsetFeatures: list of :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ConvertLegacy(self, fsetFeatures: 'list[NXOpen.Features.Feature]', createSingleFeatures: bool) -> None:
        """
        Method to convert weld point feature sets to the :py:class:`NXOpen.Weld.PointMarkPoint` class 
        
        Signature ``ConvertLegacy(fsetFeatures, createSingleFeatures)`` 
        
        :param fsetFeatures:  The pre-NX10 weld feature sets to convert 
        :type fsetFeatures: list of :py:class:`NXOpen.Features.Feature` 
        :param createSingleFeatures:  true to create single features with no master feature, false to create a master feature.  
        :type createSingleFeatures: bool 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def CreateFeatureGroupsForCommonConnectedParts(self, weldFeatures: 'list[JointmarkElement]') -> None:
        """
        Method to creates Feature Groups to collect individual weld point features that have the same connected part attributes.  
        
        Calling with numWeldFeatures equal to zero will cause all :py:class:`NXOpen.Weld.JointmarkElement` in the work part to be grouped.
        Connected parts A-B-C and C-B-A will be in the same group.
        
        Signature ``CreateFeatureGroupsForCommonConnectedParts(weldFeatures)`` 
        
        :param weldFeatures:  Individual features (those without a master feature) to group . 
        :type weldFeatures: list of :py:class:`NXOpen.Weld.JointmarkElement` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: None.
        """
        ...
    
    
    def AskConnectedParts(self, weldTag: NXOpen.NXObject) -> ConnectedPart:
        """
        Find the connected part information for the weld feature, curve, point or body.  
        
        :py:meth:`NXOpen.Weld.CustomManager.LocateWelds` can be used to retrieve weld data from a part.
        
        The data is stored in :py:class:`NXOpen.Weld.ConnectedPart` containing the appropriate
        connected part information. If the weld input is an occurrence then a body or part occurences
        will be returned in the output structures for reading the attributes on the connected parts.
        
        Signature ``AskConnectedParts(weldTag)`` 
        
        :param weldTag:  Weld feature, curve, point or solid body.  
        :type weldTag: :py:class:`NXOpen.NXObject` 
        :returns:  Connected parts information. None if none are found.  
        :rtype: :py:class:`NXOpen.Weld.ConnectedPart` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImpactAnalysisCheck(self, selectedObjects: 'list[NXOpen.NXObject]') -> None:
        """
        Method to perform the Weld Impace Analysis command.  
        
        This will fully load connected parts of the selected objects and generate navigator alert messages if input faces,  or feature specific parameters have changed. 
        
        Signature ``ImpactAnalysisCheck(selectedObjects)`` 
        
        :param selectedObjects:  Array of objects to perform an Impact Analysis for.  
        :type selectedObjects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ImpactAnalysisConfirm(self, selectedObjects: 'list[NXOpen.NXObject]') -> None:
        """
        Method to approve all alerts generated by the Weld Assistant Impact Analysis command.  
        
        New alert messages are based on the approved objects. 
        
        Signature ``ImpactAnalysisConfirm(selectedObjects)`` 
        
        :param selectedObjects:  Array of objects to approve Impact Analysis alerts for.  
        :type selectedObjects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ConvertTransformWeld(self, selectedObjects: 'list[NXOpen.Features.Feature]') -> None:
        """
        Method to convert :py:class:`NXOpen.Weld.Transform` to their parent type.  
        
        For example, if a :py:class:`NXOpen.Weld.WeldBead` is
        the parent, this function will convert the :py:class:`NXOpen.Weld.Transform` to a :py:class:`NXOpen.Weld.WeldBead` in the location of the  
        the :py:class:`NXOpen.Weld.Transform`. 
        
        Signature ``ConvertTransformWeld(selectedObjects)`` 
        
        :param selectedObjects:  Array of features to convert.  
        :type selectedObjects: list of :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def HasSourceFacesInWeldPart(self, weldFeature: NXOpen.Features.Feature) -> 'list[bool]':
        """
        Method to determine if a :py:class:`NXOpen.Weld.JointmarkElement` feature has source faces in the weld part.  
        
        Signature ``HasSourceFacesInWeldPart(weldFeature)`` 
        
        :param weldFeature:  The feature to check  
        :type weldFeature: :py:class:`NXOpen.Features.Feature` 
        :returns:  Indicates if source faces are in the weld part.  
        :rtype: list of bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    


class WeldBeadSizeBuilderSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadSizeBuilderSize():
    """
    Settings to indicate which standard size to use from the customer defaults file. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default1", "Default1 from the customer defaults"
       "Default2", "Default2 from the customer defaults"
       "Default3", "Default3 from the customer defaults"
       "Default4", "Default4 from the customer defaults"
       "Default5", "Default5 from the customer defaults"
       "Custom", "Manually keyin value."
    """
    Default1 = 0  # WeldBeadSizeBuilderSizeMemberType
    Default2 = 1  # WeldBeadSizeBuilderSizeMemberType
    Default3 = 2  # WeldBeadSizeBuilderSizeMemberType
    Default4 = 3  # WeldBeadSizeBuilderSizeMemberType
    Default5 = 4  # WeldBeadSizeBuilderSizeMemberType
    Custom = 5  # WeldBeadSizeBuilderSizeMemberType
    
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
    


class WeldBeadSizeBuilderTriangleMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadSizeBuilderTriangleMethodType():
    """
    Settings to indicate the type of method used to build a triangle shape. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LegLength", "Triangle defined by leg lengths"
       "ThroatThickness", "Trangle defined by throat thickness"
    """
    LegLength = 0  # WeldBeadSizeBuilderTriangleMethodTypeMemberType
    ThroatThickness = 1  # WeldBeadSizeBuilderTriangleMethodTypeMemberType
    
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
    


class WeldBeadSizeBuilderTriangleTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadSizeBuilderTriangleTypes():
    """
    Settings to indicate the type of triangle. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OneSided", "Basically a right triangle"
       "TwoSided", "Basically an isosceles triangle"
    """
    OneSided = 0  # WeldBeadSizeBuilderTriangleTypesMemberType
    TwoSided = 1  # WeldBeadSizeBuilderTriangleTypesMemberType
    
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
    


class WeldBeadSizeBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    This builder is used to define the bead shape.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldBeadBuilder.NewSize`
    
    .. versionadded:: NX7.5.0
    """
    
    class Size():
        """
        Settings to indicate which standard size to use from the customer defaults file. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default1", "Default1 from the customer defaults"
           "Default2", "Default2 from the customer defaults"
           "Default3", "Default3 from the customer defaults"
           "Default4", "Default4 from the customer defaults"
           "Default5", "Default5 from the customer defaults"
           "Custom", "Manually keyin value."
        """
        Default1 = 0  # WeldBeadSizeBuilderSizeMemberType
        Default2 = 1  # WeldBeadSizeBuilderSizeMemberType
        Default3 = 2  # WeldBeadSizeBuilderSizeMemberType
        Default4 = 3  # WeldBeadSizeBuilderSizeMemberType
        Default5 = 4  # WeldBeadSizeBuilderSizeMemberType
        Custom = 5  # WeldBeadSizeBuilderSizeMemberType
        
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
        
    
    
    class TriangleMethodType():
        """
        Settings to indicate the type of method used to build a triangle shape. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LegLength", "Triangle defined by leg lengths"
           "ThroatThickness", "Trangle defined by throat thickness"
        """
        LegLength = 0  # WeldBeadSizeBuilderTriangleMethodTypeMemberType
        ThroatThickness = 1  # WeldBeadSizeBuilderTriangleMethodTypeMemberType
        
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
        
    
    
    class TriangleTypes():
        """
        Settings to indicate the type of triangle. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OneSided", "Basically a right triangle"
           "TwoSided", "Basically an isosceles triangle"
        """
        OneSided = 0  # WeldBeadSizeBuilderTriangleTypesMemberType
        TwoSided = 1  # WeldBeadSizeBuilderTriangleTypesMemberType
        
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
    
    CustomSection: NXOpen.Section = ...
    """
    Returns   the section containing the custom bead shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``CustomSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PathLocation: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the location on the path to place the bead shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    RectangleBase: float = ...
    """
    Returns or sets  the base length of a rectangle shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``RectangleBase`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RectangleBase`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RectangleHeight: float = ...
    """
    Returns or sets  the height of a rectangle shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``RectangleHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RectangleHeight`` 
    
    :param height: 
    :type height: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SemiMajor: float = ...
    """
    Returns or sets  the semi the semi major size of an ellipse shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``SemiMajor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SemiMajor`` 
    
    :param semiMajor: 
    :type semiMajor: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SemiMinor: float = ...
    """
    Returns or sets  the semi minor size of an ellipse shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``SemiMinor`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SemiMinor`` 
    
    :param semiMinor: 
    :type semiMinor: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    SizeString: WeldBeadSizeBuilderSize = ...
    """
    Returns or sets  the standard size setting.  
    
    <hr>
    
    Getter Method
    
    Signature ``SizeString`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderSize` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SizeString`` 
    
    :param sizeString: 
    :type sizeString: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderSize` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ThroatThickness: float = ...
    """
    Returns or sets  the throat thickness of a triangular shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``ThroatThickness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ThroatThickness`` 
    
    :param throatThickness: 
    :type throatThickness: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TriangleBase: float = ...
    """
    Returns or sets  the horizontal leg length of a triangular shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``TriangleBase`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TriangleBase`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TriangleHeight: float = ...
    """
    Returns or sets  the vertical leg length of a triangular shaped bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``TriangleHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TriangleHeight`` 
    
    :param length: 
    :type length: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TriangleMethod: WeldBeadSizeBuilderTriangleMethodType = ...
    """
    Returns or sets  the method used to construct the triangle shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``TriangleMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderTriangleMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TriangleMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderTriangleMethodType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TriangleType: WeldBeadSizeBuilderTriangleTypes = ...
    """
    Returns or sets  the method used to indicate the type of triangle to create.  
    
    <hr>
    
    Getter Method
    
    Signature ``TriangleType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderTriangleTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TriangleType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderTriangleTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TubeDiameter: float = ...
    """
    Returns or sets  the diameter size of the tube shape.  
    
    <hr>
    
    Getter Method
    
    Signature ``TubeDiameter`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TubeDiameter`` 
    
    :param tubeDiameter: 
    :type tubeDiameter: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldBeadSizeBuilder = ...  # unknown typename


class DatumSurface(NXOpen.Features.Feature):
    """
    Represents a Weld Datum Surface feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.DatumSurfaceBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: DatumSurface = ...  # unknown typename


class WeldGrooveBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderTypes():
    """
    The types of Groove to create 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SquareButt", "Square Butt"
       "VGroove", "V Groove"
       "BevelGroove", "Bevel Groove"
       "UGroove", "U Groove"
       "JGroove", "J Groove"
       "FlaredVGroove", "Flared V Groove"
       "FlaredBevelGroove", "Flared Bevel Groove"
       "FillinFlaredVGroove", " - "
       "FillinFlaredBevelGroove", "Fillin Flared Bevel Groove"
    """
    SquareButt = 0  # WeldGrooveBuilderTypesMemberType
    VGroove = 1  # WeldGrooveBuilderTypesMemberType
    BevelGroove = 2  # WeldGrooveBuilderTypesMemberType
    UGroove = 3  # WeldGrooveBuilderTypesMemberType
    JGroove = 4  # WeldGrooveBuilderTypesMemberType
    FlaredVGroove = 5  # WeldGrooveBuilderTypesMemberType
    FlaredBevelGroove = 6  # WeldGrooveBuilderTypesMemberType
    FillinFlaredVGroove = 7  # WeldGrooveBuilderTypesMemberType
    FillinFlaredBevelGroove = 8  # WeldGrooveBuilderTypesMemberType
    
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
    


class WeldGrooveBuilderContourMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderContour():
    """
    The options for Contour Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Convex", "Convex"
       "Flush", "Flush"
       "Concave", " - "
    """
    NotSet = 0  # WeldGrooveBuilderContourMemberType
    Convex = 1  # WeldGrooveBuilderContourMemberType
    Flush = 2  # WeldGrooveBuilderContourMemberType
    Concave = 3  # WeldGrooveBuilderContourMemberType
    
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
    


class WeldGrooveBuilderSkipWeldMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderSkipWeldMethod():
    """
    The options for creating Skip Weld  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NumberLength", "Number and Length"
       "NumberSpacing", "Number and Spacing"
       "SpacingLength", "Spacing and Length"
    """
    NumberLength = 0  # WeldGrooveBuilderSkipWeldMethodMemberType
    NumberSpacing = 1  # WeldGrooveBuilderSkipWeldMethodMemberType
    SpacingLength = 2  # WeldGrooveBuilderSkipWeldMethodMemberType
    
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
    


class WeldGrooveBuilderEdgeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderEdge():
    """
    A value indicating whether the edges have been prepared  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotPrepared", "Not Prepared"
       "Prepared", "Prepared"
    """
    NotPrepared = 0  # WeldGrooveBuilderEdgeMemberType
    Prepared = 1  # WeldGrooveBuilderEdgeMemberType
    
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
    


class WeldGrooveBuilderPrepareMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderPrepare():
    """
    The type of edges to be prepared 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "EntireLength", "Entire Length"
       "WeldLimits", "Weld Limits"
       "Complex", "Complex"
    """
    NotSet = 0  # WeldGrooveBuilderPrepareMemberType
    EntireLength = 1  # WeldGrooveBuilderPrepareMemberType
    WeldLimits = 2  # WeldGrooveBuilderPrepareMemberType
    Complex = 3  # WeldGrooveBuilderPrepareMemberType
    
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
    


class WeldGrooveBuilderTaperMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveBuilderTaper():
    """
    The type of Taper Method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FromEndFace", "From End Face"
       "FromTopFace", "From Top Face"
    """
    FromEndFace = 0  # WeldGrooveBuilderTaperMemberType
    FromTopFace = 1  # WeldGrooveBuilderTaperMemberType
    
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
    


class WeldGrooveBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.WeldGroove` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldGroove1Builder`
    
    Default values.
    
    =============================  ============================================
    Property                       Value
    =============================  ============================================
    AssignWeldPMI                  0 
    -----------------------------  --------------------------------------------
    ContourHeight.Value            3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    ContourType                    None 
    -----------------------------  --------------------------------------------
    CreateSkipWelds                0 
    -----------------------------  --------------------------------------------
    EdgeType                       NotPrepared 
    -----------------------------  --------------------------------------------
    EndAngle.Value                 0 
    -----------------------------  --------------------------------------------
    GrooveAngle.Value              45.0 
    -----------------------------  --------------------------------------------
    GrooveRadius.Value             1.0 (millimeters part), 0.04 (inches part) 
    -----------------------------  --------------------------------------------
    IsRootOpening                  0 
    -----------------------------  --------------------------------------------
    IsRootPenetration              0 
    -----------------------------  --------------------------------------------
    Method                         NumberLength 
    -----------------------------  --------------------------------------------
    NumberOfWelds.Value            3 
    -----------------------------  --------------------------------------------
    PenetrationDepth.Value         3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    PrepareEdges                   EntireLength 
    -----------------------------  --------------------------------------------
    RecreateDeletedWelds           0 
    -----------------------------  --------------------------------------------
    RootOpening.Value              3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    RootPenetration.Value          3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    SecondPenetrationDepth.Value   0 (millimeters part), 0 (inches part) 
    -----------------------------  --------------------------------------------
    SegmentLength.Value            3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    SingleFaceSet                  0 
    -----------------------------  --------------------------------------------
    Spacing.Value                  3.0 (millimeters part), 0.118 (inches part) 
    -----------------------------  --------------------------------------------
    StartAngle.Value               0 
    -----------------------------  --------------------------------------------
    TaperMethod                    FromTopFace 
    -----------------------------  --------------------------------------------
    Type                           SquareButt 
    -----------------------------  --------------------------------------------
    UseFillin                      0 
    -----------------------------  --------------------------------------------
    WeldSymmetric                  1 
    =============================  ============================================
    
    .. versionadded:: NX9.0.0
    """
    
    class Types():
        """
        The types of Groove to create 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SquareButt", "Square Butt"
           "VGroove", "V Groove"
           "BevelGroove", "Bevel Groove"
           "UGroove", "U Groove"
           "JGroove", "J Groove"
           "FlaredVGroove", "Flared V Groove"
           "FlaredBevelGroove", "Flared Bevel Groove"
           "FillinFlaredVGroove", " - "
           "FillinFlaredBevelGroove", "Fillin Flared Bevel Groove"
        """
        SquareButt = 0  # WeldGrooveBuilderTypesMemberType
        VGroove = 1  # WeldGrooveBuilderTypesMemberType
        BevelGroove = 2  # WeldGrooveBuilderTypesMemberType
        UGroove = 3  # WeldGrooveBuilderTypesMemberType
        JGroove = 4  # WeldGrooveBuilderTypesMemberType
        FlaredVGroove = 5  # WeldGrooveBuilderTypesMemberType
        FlaredBevelGroove = 6  # WeldGrooveBuilderTypesMemberType
        FillinFlaredVGroove = 7  # WeldGrooveBuilderTypesMemberType
        FillinFlaredBevelGroove = 8  # WeldGrooveBuilderTypesMemberType
        
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
        
    
    
    class Contour():
        """
        The options for Contour Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "Convex", "Convex"
           "Flush", "Flush"
           "Concave", " - "
        """
        NotSet = 0  # WeldGrooveBuilderContourMemberType
        Convex = 1  # WeldGrooveBuilderContourMemberType
        Flush = 2  # WeldGrooveBuilderContourMemberType
        Concave = 3  # WeldGrooveBuilderContourMemberType
        
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
        
    
    
    class SkipWeldMethod():
        """
        The options for creating Skip Weld  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NumberLength", "Number and Length"
           "NumberSpacing", "Number and Spacing"
           "SpacingLength", "Spacing and Length"
        """
        NumberLength = 0  # WeldGrooveBuilderSkipWeldMethodMemberType
        NumberSpacing = 1  # WeldGrooveBuilderSkipWeldMethodMemberType
        SpacingLength = 2  # WeldGrooveBuilderSkipWeldMethodMemberType
        
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
        
    
    
    class Edge():
        """
        A value indicating whether the edges have been prepared  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotPrepared", "Not Prepared"
           "Prepared", "Prepared"
        """
        NotPrepared = 0  # WeldGrooveBuilderEdgeMemberType
        Prepared = 1  # WeldGrooveBuilderEdgeMemberType
        
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
        
    
    
    class Prepare():
        """
        The type of edges to be prepared 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "EntireLength", "Entire Length"
           "WeldLimits", "Weld Limits"
           "Complex", "Complex"
        """
        NotSet = 0  # WeldGrooveBuilderPrepareMemberType
        EntireLength = 1  # WeldGrooveBuilderPrepareMemberType
        WeldLimits = 2  # WeldGrooveBuilderPrepareMemberType
        Complex = 3  # WeldGrooveBuilderPrepareMemberType
        
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
        
    
    
    class Taper():
        """
        The type of Taper Method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FromEndFace", "From End Face"
           "FromTopFace", "From Top Face"
        """
        FromEndFace = 0  # WeldGrooveBuilderTaperMemberType
        FromTopFace = 1  # WeldGrooveBuilderTaperMemberType
        
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
        
    
    AssignWeldPMI: bool = ...
    """
    Returns or sets  a value indicating whether the assign weld pmi is true  
    
    <hr>
    
    Getter Method
    
    Signature ``AssignWeldPMI`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``AssignWeldPMI`` 
    
    :param assignWeldPMI: 
    :type assignWeldPMI: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics 
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ContourHeight: NXOpen.Expression = ...
    """
    Returns  the contour height 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ContourType: WeldGrooveBuilderContour = ...
    """
    Returns or sets  the contour type 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderContour` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ContourType`` 
    
    :param contour: 
    :type contour: :py:class:`NXOpen.Weld.WeldGrooveBuilderContour` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    CreateSkipWelds: bool = ...
    """
    Returns or sets  a value indicating whether to create skip welds   
    
    <hr>
    
    Getter Method
    
    Signature ``CreateSkipWelds`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``CreateSkipWelds`` 
    
    :param createSkipWelds: 
    :type createSkipWelds: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EdgeSet1: NXOpen.Section = ...
    """
    Returns  the first edge set 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeSet1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EdgeSet2: NXOpen.Section = ...
    """
    Returns  the second edge set 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeSet2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EdgeType: WeldGrooveBuilderEdge = ...
    """
    Returns or sets  the edge type 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderEdge` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``EdgeType`` 
    
    :param edgeType: 
    :type edgeType: :py:class:`NXOpen.Weld.WeldGrooveBuilderEdge` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EndAngle: NXOpen.Expression = ...
    """
    Returns  the taper angle at the end of the weld 
    
    <hr>
    
    Getter Method
    
    Signature ``EndAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    EndDistance: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the end limit as defined by the distance along the edge  
    
    <hr>
    
    Getter Method
    
    Signature ``EndDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceSet1: NXOpen.ScCollector = ...
    """
    Returns  the face set1 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceSet2: NXOpen.ScCollector = ...
    """
    Returns  the face set2 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceSet2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    GrooveAngle: NXOpen.Expression = ...
    """
    Returns  the groove angle 
    
    <hr>
    
    Getter Method
    
    Signature ``GrooveAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    GrooveRadius: NXOpen.Expression = ...
    """
    Returns  the groove radius 
    
    <hr>
    
    Getter Method
    
    Signature ``GrooveRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    IsRootOpening: bool = ...
    """
    Returns or sets  a value indicating whether root opening is true  
    
    <hr>
    
    Getter Method
    
    Signature ``IsRootOpening`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``IsRootOpening`` 
    
    :param isRootOpening: 
    :type isRootOpening: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    IsRootPenetration: bool = ...
    """
    Returns or sets  a value indicating whether root depth is true  
    
    <hr>
    
    Getter Method
    
    Signature ``IsRootPenetration`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``IsRootPenetration`` 
    
    :param isRootPenetration: 
    :type isRootPenetration: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Method: WeldGrooveBuilderSkipWeldMethod = ...
    """
    Returns or sets  the method for creating skip welds 
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderSkipWeldMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.WeldGrooveBuilderSkipWeldMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    NumberOfWelds: NXOpen.Expression = ...
    """
    Returns  the number of welds 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfWelds`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    PenetrationDepth: NXOpen.Expression = ...
    """
    Returns  the penetration depth 
    
    <hr>
    
    Getter Method
    
    Signature ``PenetrationDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    PrepareEdges: WeldGrooveBuilderPrepare = ...
    """
    Returns or sets  the type of edges to prepare 
    
    <hr>
    
    Getter Method
    
    Signature ``PrepareEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderPrepare` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``PrepareEdges`` 
    
    :param prepareEdges: 
    :type prepareEdges: :py:class:`NXOpen.Weld.WeldGrooveBuilderPrepare` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RecreateDeletedWelds: bool = ...
    """
    Returns or sets  a value indicating whether to recreate deleted welds  
    
    <hr>
    
    Getter Method
    
    Signature ``RecreateDeletedWelds`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``RecreateDeletedWelds`` 
    
    :param recreateDeletedWelds: 
    :type recreateDeletedWelds: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RootOpening: NXOpen.Expression = ...
    """
    Returns  the root opening 
    
    <hr>
    
    Getter Method
    
    Signature ``RootOpening`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RootPenetration: NXOpen.Expression = ...
    """
    Returns  the root penetration 
    
    <hr>
    
    Getter Method
    
    Signature ``RootPenetration`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SecondPenetrationDepth: NXOpen.Expression = ...
    """
    Returns  the second penetration depth 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondPenetrationDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedFace1: NXOpen.Face = ...
    """
    Returns or sets  the first seed face 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace1`` 
    
    :param seedFace1: 
    :type seedFace1: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedFace2: NXOpen.Face = ...
    """
    Returns or sets  the second seed face 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace2`` 
    
    :param seedFace2: 
    :type seedFace2: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedPoint1: NXOpen.Point3d = ...
    """
    Returns or sets  the point on the first face 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedPoint1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SeedPoint1`` 
    
    :param seedPoint1: 
    :type seedPoint1: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SeedPoint2: NXOpen.Point3d = ...
    """
    Returns or sets  the point on the second face 
    
    <hr>
    
    Getter Method
    
    Signature ``SeedPoint2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SeedPoint2`` 
    
    :param seedPoint1: 
    :type seedPoint1: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SegmentLength: NXOpen.Expression = ...
    """
    Returns  the length of weld 
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SingleFaceSet: bool = ...
    """
    Returns or sets  a value indicating whether the single face set is true  
    
    <hr>
    
    Getter Method
    
    Signature ``SingleFaceSet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SingleFaceSet`` 
    
    :param singleFaceSet: 
    :type singleFaceSet: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Spacing: NXOpen.Expression = ...
    """
    Returns  the spacing between welds 
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartAngle: NXOpen.Expression = ...
    """
    Returns  the taper angle at the start of the weld 
    
    <hr>
    
    Getter Method
    
    Signature ``StartAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartDistance: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the start limit as defined by the distance along the edge  
    
    <hr>
    
    Getter Method
    
    Signature ``StartDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    TaperMethod: WeldGrooveBuilderTaper = ...
    """
    Returns or sets  the taper method 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderTaper` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``TaperMethod`` 
    
    :param taperMethod: 
    :type taperMethod: :py:class:`NXOpen.Weld.WeldGrooveBuilderTaper` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Type: WeldGrooveBuilderTypes = ...
    """
    Returns or sets  the type of the groove 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldGrooveBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldGrooveBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Uparameter1: float = ...
    """
    Returns or sets  the u parameter for first face 
    
    <hr>
    
    Getter Method
    
    Signature ``Uparameter1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Uparameter1`` 
    
    :param u1: 
    :type u1: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Uparameter2: float = ...
    """
    Returns or sets  the u parameter for second face 
    
    <hr>
    
    Getter Method
    
    Signature ``Uparameter2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Uparameter2`` 
    
    :param u2: 
    :type u2: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    UseFillin: bool = ...
    """
    Returns or sets  a value indicating whether to use fillin 
    
    <hr>
    
    Getter Method
    
    Signature ``UseFillin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``UseFillin`` 
    
    :param useFillin: 
    :type useFillin: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Vparameter1: float = ...
    """
    Returns or sets  the v parameter for first face 
    
    <hr>
    
    Getter Method
    
    Signature ``Vparameter1`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Vparameter1`` 
    
    :param v1: 
    :type v1: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Vparameter2: float = ...
    """
    Returns or sets  the v parameter for second face 
    
    <hr>
    
    Getter Method
    
    Signature ``Vparameter2`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Vparameter2`` 
    
    :param v2: 
    :type v2: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    WeldSymmetric: bool = ...
    """
    Returns or sets  a value indicating whether the second depth is the same as the first depth  
    
    <hr>
    
    Getter Method
    
    Signature ``WeldSymmetric`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``WeldSymmetric`` 
    
    :param weldSymmetric: 
    :type weldSymmetric: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldGrooveBuilder = ...  # unknown typename


class WeldAdvisorBuilder(NXOpen.Builder):
    """
    Represents a weld advisor test   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldAdvisorBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def SetObjects(self, objects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the objects to be checked 
        
        Signature ``SetObjects(objects)`` 
        
        :param objects:  Objects to be checked 
        :type objects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the objects to be checked 
        
        Signature ``GetObjects()`` 
        
        :returns:  Objects to be checked 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetCheckers(self, checkers: 'list[WeldAdvisorCheckerType]') -> None:
        """
        Sets the checkers be executed  
        
        Signature ``SetCheckers(checkers)`` 
        
        :param checkers:  Checkers to be executed 
        :type checkers: list of :py:class:`NXOpen.Weld.WeldAdvisorCheckerType` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetCheckers(self) -> 'list[WeldAdvisorCheckerType]':
        """
        Gets the checkers be executed  
        
        Signature ``GetCheckers()`` 
        
        :returns:  Checkers to be executed 
        :rtype: list of :py:class:`NXOpen.Weld.WeldAdvisorCheckerType` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReportResult(self, filePath: str) -> None:
        """
        The report results to xml file  
        
        Signature ``ReportResult(filePath)`` 
        
        :param filePath:  the file to save result  
        :type filePath: str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SaveResult(self) -> None:
        """
        The save all to part  
        
        Signature ``SaveResult()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFailedObjects(self, checker: WeldAdvisorCheckerType) -> tuple:
        """
        The failed results 
        
        Signature ``GetFailedObjects(checker)`` 
        
        :param checker:  checker type 
        :type checker: :py:class:`NXOpen.Weld.WeldAdvisorCheckerType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (weldId, weldObjects). weldId is a list of str.   weld idweldObjects is a list of :py:class:`NXOpen.Weld.LogInfo`.   failed objects
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetReferenceObjects(self, weldObject: NXOpen.TaggedObject, checker: WeldAdvisorCheckerType) -> 'list[LogInfo]':
        """
        The objects that failed weld objects referenced 
        
        Signature ``GetReferenceObjects(weldObject, checker)`` 
        
        :param weldObject:  the weld object 
        :type weldObject: :py:class:`NXOpen.TaggedObject` 
        :param checker:  checker type 
        :type checker: :py:class:`NXOpen.Weld.WeldAdvisorCheckerType` 
        :returns: reference objects 
        :rtype: list of :py:class:`NXOpen.Weld.LogInfo` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMinimumEdgeDistance(self, type: WeldAdvisorCustomerDefault, minEdgeDist: float) -> None:
        """
        The weld advisor parameter Minimum Edge Distance 
        
        Signature ``SetMinimumEdgeDistance(type, minEdgeDist)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param minEdgeDist:  The weld advisor parameter Minimum Edge Distance  
        :type minEdgeDist: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMinimumEdgeDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Minimum Edge Distance  
        
        Signature ``GetMinimumEdgeDistance(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Minimum Edge Distance  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMinimumEdgeDistanceWithSealer(self, type: WeldAdvisorCustomerDefault, minEdgeDistWithSealer: float) -> None:
        """
        The weld advisor parameter Minimum Edge Distance With Sealer 
        
        Signature ``SetMinimumEdgeDistanceWithSealer(type, minEdgeDistWithSealer)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param minEdgeDistWithSealer:  The weld advisor parameter Minimum Edge Distance With Sealer  
        :type minEdgeDistWithSealer: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMinimumEdgeDistanceWithSealer(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Minimum Edge Distance With Sealer  
        
        Signature ``GetMinimumEdgeDistanceWithSealer(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Minimum Edge Distance With Sealer  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMinimumPointDistance(self, type: WeldAdvisorCustomerDefault, minPointDist: float) -> None:
        """
        The weld advisor parameter Minimum Spacing 
        
        Signature ``SetMinimumPointDistance(type, minPointDist)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param minPointDist:  The weld advisor parameter Minimum Spacing  
        :type minPointDist: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMinimumPointDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Minimum Spacing  
        
        Signature ``GetMinimumPointDistance(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Minimum Spacing  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMaximumStackUpGap(self, type: WeldAdvisorCustomerDefault, maxFaceDist: float) -> None:
        """
        The weld advisor parameter Maximum Stack Up Gap 
        
        Signature ``SetMaximumStackUpGap(type, maxFaceDist)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param maxFaceDist:  The weld advisor parameter Maximum Stack Up Gap  
        :type maxFaceDist: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMaximumStackUpGap(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Maximum Stack Up Gap  
        
        Signature ``GetMaximumStackUpGap(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Maximum Stack Up Gap  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMaximumPointFaceDistance(self, type: WeldAdvisorCustomerDefault, pointFaceDist: float) -> None:
        """
        The weld advisor parameter Maximum Point Face Distance 
        
        Signature ``SetMaximumPointFaceDistance(type, pointFaceDist)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param pointFaceDist:  The weld advisor parameter Maximum Point Face Distance  
        :type pointFaceDist: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMaximumPointFaceDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Maximum Point Face Distance  
        
        Signature ``GetMaximumPointFaceDistance(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Maximum Point Face Distance  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMaximumCsysFaceNormalAngle(self, type: WeldAdvisorCustomerDefault, csysFaceNmlAngle: float) -> None:
        """
        The weld advisor parameter Maximum CSYS Face Normal Angle 
        
        Signature ``SetMaximumCsysFaceNormalAngle(type, csysFaceNmlAngle)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param csysFaceNmlAngle:  The weld advisor parameter Maximum CSYS Face Normal Angle  
        :type csysFaceNmlAngle: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMaximumCsysFaceNormalAngle(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Maximum CSYS Face Normal Angle  
        
        Signature ``GetMaximumCsysFaceNormalAngle(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Maximum CSYS Face Normal Angle  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetCheckZoneRadius(self, type: WeldAdvisorCustomerDefault, faceRadius: float) -> None:
        """
        The weld advisor parameter Check Zone Radius 
        
        Signature ``SetCheckZoneRadius(type, faceRadius)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param faceRadius:  The weld advisor parameter Check Zone Radius  
        :type faceRadius: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetCheckZoneRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Check Zone Radius  
        
        Signature ``GetCheckZoneRadius(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Check Zone Radius  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetSealerCheckZoneRadius(self, type: WeldAdvisorCustomerDefault, faceRadiusWithSealer: float) -> None:
        """
        The weld advisor parameter Sealer Check Zone Radius 
        
        Signature ``SetSealerCheckZoneRadius(type, faceRadiusWithSealer)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param faceRadiusWithSealer:  The weld advisor parameter Sealer Check Zone Radius  
        :type faceRadiusWithSealer: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetSealerCheckZoneRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Sealer Check Zone Radius  
        
        Signature ``GetSealerCheckZoneRadius(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Sealer Check Zone Radius  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetPlanarityTolerance(self, type: WeldAdvisorCustomerDefault, facePlanarityTolerance: float) -> None:
        """
        The weld advisor parameter Planarity Tolerance 
        
        Signature ``SetPlanarityTolerance(type, facePlanarityTolerance)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param facePlanarityTolerance:  The weld advisor parameter Planarity Tolerance  
        :type facePlanarityTolerance: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetPlanarityTolerance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Planarity Tolerance  
        
        Signature ``GetPlanarityTolerance(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Planarity Tolerance  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetParallelismTolerance(self, type: WeldAdvisorCustomerDefault, faceParallelismTolerance: float) -> None:
        """
        The weld advisor parameter Parallelism Tolerance 
        
        Signature ``SetParallelismTolerance(type, faceParallelismTolerance)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param faceParallelismTolerance:  The weld advisor parameter Parallelism Tolerance  
        :type faceParallelismTolerance: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetParallelismTolerance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Parallelism Tolerance  
        
        Signature ``GetParallelismTolerance(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Parallelism Tolerance  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetFlangeCheckRadius(self, type: WeldAdvisorCustomerDefault, flangeRadius: float) -> None:
        """
        The weld advisor parameter Flange Check Radius 
        
        Signature ``SetFlangeCheckRadius(type, flangeRadius)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param flangeRadius:  The weld advisor parameter Flange Check Radius  
        :type flangeRadius: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFlangeCheckRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Flange Check Radius  
        
        Signature ``GetFlangeCheckRadius(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Flange Check Radius  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetFlangeCheckHeight(self, type: WeldAdvisorCustomerDefault, flangeHeight: float) -> None:
        """
        The weld advisor parameter Flange Check Height 
        
        Signature ``SetFlangeCheckHeight(type, flangeHeight)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param flangeHeight:  The weld advisor parameter Flange Check Height  
        :type flangeHeight: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFlangeCheckHeight(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Flange Check Height  
        
        Signature ``GetFlangeCheckHeight(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Flange Check Height  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMinimumClosedAngle(self, type: WeldAdvisorCustomerDefault, minClosedAngle: float) -> None:
        """
        The weld advisor parameter Minimum Closed Angle 
        
        Signature ``SetMinimumClosedAngle(type, minClosedAngle)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param minClosedAngle:  The weld advisor parameter Minimum Closed Angle  
        :type minClosedAngle: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMinimumClosedAngle(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Minimum Closed Angle  
        
        Signature ``GetMinimumClosedAngle(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Minimum Closed Angle  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMaximumTotalMetalThickness(self, type: WeldAdvisorCustomerDefault, totalMetalThickness: float) -> None:
        """
        The weld advisor parameter Maximum Total Metal Thickness 
        
        Signature ``SetMaximumTotalMetalThickness(type, totalMetalThickness)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param totalMetalThickness:  The weld advisor parameter Maximum Total Metal Thickness  
        :type totalMetalThickness: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMaximumTotalMetalThickness(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Maximum Total Metal Thickness  
        
        Signature ``GetMaximumTotalMetalThickness(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Maximum Total Metal Thickness  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetThicknessRatio(self, type: WeldAdvisorCustomerDefault, thicknessRatio: float) -> None:
        """
        The weld advisor parameter Thickness Ratio 
        
        Signature ``SetThicknessRatio(type, thicknessRatio)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param thicknessRatio:  The weld advisor parameter Thickness Ratio  
        :type thicknessRatio: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetThicknessRatio(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Thickness Ratio  
        
        Signature ``GetThicknessRatio(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Thickness Ratio  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetThicknessOuterRatio(self, type: WeldAdvisorCustomerDefault, thicknessOuterRatio: float) -> None:
        """
        The weld advisor parameter Thickness Outer Ratio 
        
        Signature ``SetThicknessOuterRatio(type, thicknessOuterRatio)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param thicknessOuterRatio:  The weld advisor parameter Thickness Outer Ratio  
        :type thicknessOuterRatio: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetThicknessOuterRatio(self, type: WeldAdvisorCustomerDefault) -> float:
        """
        The weld advisor parameter Thickness Outer Ratio  
        
        Signature ``GetThicknessOuterRatio(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Thickness Outer Ratio  
        :rtype: float 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetMaximumNumberLoosePanels(self, type: WeldAdvisorCustomerDefault, maxNumOfLoosePanels: int) -> None:
        """
        The weld advisor parameter Maximum Number of Loose Panels 
        
        Signature ``SetMaximumNumberLoosePanels(type, maxNumOfLoosePanels)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :param maxNumOfLoosePanels:  The weld advisor parameter Maximum Number of Loose Panels  
        :type maxNumOfLoosePanels: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetMaximumNumberLoosePanels(self, type: WeldAdvisorCustomerDefault) -> int:
        """
        The weld advisor parameter Maximum Number of Loose Panels  
        
        Signature ``GetMaximumNumberLoosePanels(type)`` 
        
        :param type:  weld type  
        :type type: :py:class:`NXOpen.Weld.WeldAdvisorCustomerDefault` 
        :returns:  The weld advisor parameter Maximum Number of Loose Panels  
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def InitializeSettings(self) -> None:
        """
        The initialization for settings 
        
        Signature ``InitializeSettings()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SetIncludeSealer(self, includeSealer: bool) -> None:
        """
        The sealer included or not 
        
        Signature ``SetIncludeSealer(includeSealer)`` 
        
        :param includeSealer:  include sealer or not 
        :type includeSealer: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetIncludeSealer(self) -> bool:
        """
        The sealer included or not  
        
        Signature ``GetIncludeSealer()`` 
        
        :returns:  include sealer  
        :rtype: bool 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def DeleteFeaturesFromResult(self, objects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Delete the features from the check result 
        
        Signature ``DeleteFeaturesFromResult(objects)`` 
        
        :param objects:  features to be deleted 
        :type objects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    Null: WeldAdvisorBuilder = ...  # unknown typename


class WeldParasetLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldParasetLocation():
    """
    the index of user picked refsheet location 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Length", "arc length"
       "Percent", "percent arc length"
       "ThroughPoint", "through point"
    """
    Length = 0  # WeldParasetLocationMemberType
    Percent = 1  # WeldParasetLocationMemberType
    ThroughPoint = 2  # WeldParasetLocationMemberType
    
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
    


class WeldPointExtendMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointExtendMethod():
    """
    Offset curve extend method 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Do not extend offset curves."
       "Boundary", "Extend offset curves to the faces boundary."
    """
    NotSet = 0  # WeldPointExtendMethodMemberType
    Boundary = 1  # WeldPointExtendMethodMemberType
    
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
    


class WeldFillStripBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[WeldFillStripBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: WeldFillStripBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
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
    
    
    def FindIndex(self, obj: WeldFillStripBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> WeldFillStripBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
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
    def Erase(self, obj: WeldFillStripBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: WeldFillStripBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
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
    
    
    def GetContents(self) -> 'list[WeldFillStripBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[WeldFillStripBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
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
    def Swap(self, object1: WeldFillStripBuilder, object2: WeldFillStripBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: WeldFillStripBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
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
    Null: WeldFillStripBuilderList = ...  # unknown typename


class TransformBuilderTransformationTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformBuilderTransformationTypes():
    """
    The transformation types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Mirror", "Mirror"
       "Translate", "Translate"
    """
    Mirror = 0  # TransformBuilderTransformationTypesMemberType
    Translate = 1  # TransformBuilderTransformationTypesMemberType
    
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
    


class TransformBuilderConnectedPartMethodsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformBuilderConnectedPartMethods():
    """
    The type to define the method used to find connected parts 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TransformBody", "Use the location of the transform body to help find connected parts"
       "ParentFaces", "Use transformed parent faces to find connected parts"
    """
    TransformBody = 0  # TransformBuilderConnectedPartMethodsMemberType
    ParentFaces = 1  # TransformBuilderConnectedPartMethodsMemberType
    
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
    


class TransformBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.TransformBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateTransformBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    class TransformationTypes():
        """
        The transformation types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Mirror", "Mirror"
           "Translate", "Translate"
        """
        Mirror = 0  # TransformBuilderTransformationTypesMemberType
        Translate = 1  # TransformBuilderTransformationTypesMemberType
        
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
        
    
    
    class ConnectedPartMethods():
        """
        The type to define the method used to find connected parts 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TransformBody", "Use the location of the transform body to help find connected parts"
           "ParentFaces", "Use transformed parent faces to find connected parts"
        """
        TransformBody = 0  # TransformBuilderConnectedPartMethodsMemberType
        ParentFaces = 1  # TransformBuilderConnectedPartMethodsMemberType
        
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
        
    
    Associative: bool = ...
    """
    Returns or sets  the indication to create associative feature 
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative: 
    :type associative: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the collection of welding characteristics defined by attributes.  
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    ConnectedPartMethod: TransformBuilderConnectedPartMethods = ...
    """
    Returns or sets  the method used to find connected parts 
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedPartMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.TransformBuilderConnectedPartMethods` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectedPartMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.Weld.TransformBuilderConnectedPartMethods` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ConnectedPartTolerance: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the connected part tolerance.  
    
    This is used to find connected part information for the transformed weld. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedPartTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Features: NXOpen.Features.SelectBodyFeatureList = ...
    """
    Returns  the weld features to transform 
    
    <hr>
    
    Getter Method
    
    Signature ``Features`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectBodyFeatureList` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    MirrorPlane: NXOpen.Plane = ...
    """
    Returns or sets  the mirror plane, used when :py:class:`NXOpen.Weld.TransformBuilderTransformationTypes` is set to :py:class:` NXOpen.Weld.TransformBuilderTransformationTypes.Mirror  < NXOpen.Weld.TransformBuilderTransformationTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorPlane`` 
    
    :param mirrorPlane: 
    :type mirrorPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system that defines the translate offset directions.  
    
    If not specified the absolute coordinate system will be used.
    Used when :py:class:`NXOpen.Weld.TransformBuilderTransformationTypes` is set to :py:class:` NXOpen.Weld.TransformBuilderTransformationTypes.Translate  < NXOpen.Weld.TransformBuilderTransformationTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslateCsys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    TranslateX: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the x translation distance.  
    
    Used when :py:class:`NXOpen.Weld.TransformBuilderTransformationTypes` is set to :py:class:` NXOpen.Weld.TransformBuilderTransformationTypes.Translate  < NXOpen.Weld.TransformBuilderTransformationTypes>` 
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateX`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TranslateY: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the y translation distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateY`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    TranslateZ: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the z translation distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``TranslateZ`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Type: TransformBuilderTransformationTypes = ...
    """
    Returns or sets  the transformation type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.TransformBuilderTransformationTypes` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param transType: 
    :type transType: :py:class:`NXOpen.Weld.TransformBuilderTransformationTypes` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    Null: TransformBuilder = ...  # unknown typename


class WeldJoint(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a weld joint feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.WeldJointBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: WeldJoint = ...  # unknown typename


class WeldCpdUtils():
    """
    Provides methods for access a WeldCpdUtils class object in NX.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX9.0.0
    """
    
    def GetJointCurvesFromWeldFeature(self, featureTag: NXOpen.NXObject) -> 'list[NXOpen.Curve]':
        """
        Return joint curves of a given welding joint feature.  
        
        Signature ``GetJointCurvesFromWeldFeature(featureTag)`` 
        
        :param featureTag:  weld feature  
        :type featureTag: :py:class:`NXOpen.NXObject` 
        :returns:  joint curves  
        :rtype: list of :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDesignFeatureFromWeldFeature(self, featureTag: NXOpen.NXObject) -> 'list[NXOpen.NXObject]':
        """
        Return Design Features of a given welding joint feature.  
        
        Signature ``GetDesignFeatureFromWeldFeature(featureTag)`` 
        
        :param featureTag:  weld feature  
        :type featureTag: :py:class:`NXOpen.NXObject` 
        :returns:  design features  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    


class WeldLabelBuilderOrientationPlaneTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldLabelBuilderOrientationPlaneType():
    """
    This represents the Orientation Plane Type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "XYPlane", " - "
       "XZPlane", " - "
       "YZPlane", " - "
       "ModelView", " - "
       "LastUserDefined", " - "
       "UserDefined", " - "
    """
    XYPlane = 0  # WeldLabelBuilderOrientationPlaneTypeMemberType
    XZPlane = 1  # WeldLabelBuilderOrientationPlaneTypeMemberType
    YZPlane = 2  # WeldLabelBuilderOrientationPlaneTypeMemberType
    ModelView = 3  # WeldLabelBuilderOrientationPlaneTypeMemberType
    LastUserDefined = 4  # WeldLabelBuilderOrientationPlaneTypeMemberType
    UserDefined = 5  # WeldLabelBuilderOrientationPlaneTypeMemberType
    
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
    


class WeldLabelBuilder(NXOpen.Builder):
    """
    Create weld labels for multiple welds and BIW locators, this builder's Commit can produce more than one object, 
    the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldLabelBuilder`
    
    Default values.
    
    =================================  ===========================================
    Property                           Value
    =================================  ===========================================
    IncludeLeader                      1 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.CustomSymbolScale   1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolAspectRatio   1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolHeight        25.4 (millimeters part), 1.0 (inches part) 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolLength        25.4 (millimeters part), 1.0 (inches part) 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolPreferences   UseCurrent 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolScale         1.0 
    ---------------------------------  -------------------------------------------
    Text.TextBlock.SymbolSizeMethod    ScaleAndAspectRatio 
    =================================  ===========================================
    
    .. versionadded:: NX8.5.0
    """
    
    class OrientationPlaneType():
        """
        This represents the Orientation Plane Type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "XYPlane", " - "
           "XZPlane", " - "
           "YZPlane", " - "
           "ModelView", " - "
           "LastUserDefined", " - "
           "UserDefined", " - "
        """
        XYPlane = 0  # WeldLabelBuilderOrientationPlaneTypeMemberType
        XZPlane = 1  # WeldLabelBuilderOrientationPlaneTypeMemberType
        YZPlane = 2  # WeldLabelBuilderOrientationPlaneTypeMemberType
        ModelView = 3  # WeldLabelBuilderOrientationPlaneTypeMemberType
        LastUserDefined = 4  # WeldLabelBuilderOrientationPlaneTypeMemberType
        UserDefined = 5  # WeldLabelBuilderOrientationPlaneTypeMemberType
        
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
        
    
    IncludeLeader: bool = ...
    """
    Returns or sets  the leader option, indicates whether to create a leader 
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeLeader`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeLeader`` 
    
    :param leader: 
    :type leader: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Leader: NXOpen.Annotations.LeaderBuilder = ...
    """
    Returns  the :py:class:`NXOpen.Annotations.LeaderBuilder` for the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Leader`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.LeaderBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Objects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the objects that are used to create labels.  
    
    <hr>
    
    Getter Method
    
    Signature ``Objects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Origin: NXOpen.Annotations.OriginBuilder = ...
    """
    Returns  the :py:class:`NXOpen.Annotations.OriginBuilder` for the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.OriginBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    PlaneType: WeldLabelBuilderOrientationPlaneType = ...
    """
    Returns or sets  the plane type.  
    
    <hr>
    
    Getter Method
    
    Signature ``PlaneType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldLabelBuilderOrientationPlaneType` 
    
    .. versionadded:: NX8.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlaneType`` 
    
    :param planeType: 
    :type planeType: :py:class:`NXOpen.Weld.WeldLabelBuilderOrientationPlaneType` 
    
    .. versionadded:: NX8.5.2
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Style: NXOpen.Annotations.StyleBuilder = ...
    """
    Returns  the :py:class:`NXOpen.Annotations.StyleBuilder` for the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Style`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.StyleBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Text: NXOpen.Annotations.TextWithEditControlsBuilder = ...
    """
    Returns  the :py:class:`NXOpen.Annotations.TextWithEditControlsBuilder` for the annotation 
    
    <hr>
    
    Getter Method
    
    Signature ``Text`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Annotations.TextWithEditControlsBuilder` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    UserCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the user specified coordinate system.  
    
    <hr>
    
    Getter Method
    
    Signature ``UserCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserCsys`` 
    
    :param userCsys: 
    :type userCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.2
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Null: WeldLabelBuilder = ...  # unknown typename


class WeldBeadPathBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[WeldBeadPathBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: WeldBeadPathBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
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
    
    
    def FindIndex(self, obj: WeldBeadPathBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> WeldBeadPathBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
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
    def Erase(self, obj: WeldBeadPathBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: WeldBeadPathBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
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
    
    
    def GetContents(self) -> 'list[WeldBeadPathBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[WeldBeadPathBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
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
    def Swap(self, object1: WeldBeadPathBuilder, object2: WeldBeadPathBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: WeldBeadPathBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
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
    Null: WeldBeadPathBuilderList = ...  # unknown typename


class DatumSurfaceBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DatumSurfaceBuilderTypes():
    """
    Settings to indicate the construction type used for the datum surface. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Direct", "direct location"
       "Mirror", "mirror location"
    """
    Direct = 0  # DatumSurfaceBuilderTypesMemberType
    Mirror = 1  # DatumSurfaceBuilderTypesMemberType
    
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
    


class DatumSurfaceBuilder(DatumCommonBuilder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.DatumSurface` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateDatumSurfaceBuilder`
    
    Default values.
    
    ======================  =========================================
    Property                Value
    ======================  =========================================
    ControlMethod           PrincipalAxis 
    ----------------------  -----------------------------------------
    CreateDirectionVector   1 
    ----------------------  -----------------------------------------
    CreatePlane             1 
    ----------------------  -----------------------------------------
    CreatePoint             1 
    ----------------------  -----------------------------------------
    Derived                 0 
    ----------------------  -----------------------------------------
    DirectionLength         20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    GridSnapTolerance       1 (millimeters part), 0.05 (inches part) 
    ----------------------  -----------------------------------------
    ModelingTolerance       0.0254 
    ----------------------  -----------------------------------------
    PlaneHeight             20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    PlaneWidth              20 (millimeters part), 1.0 (inches part) 
    ----------------------  -----------------------------------------
    PrincipalAxisX          0 
    ----------------------  -----------------------------------------
    PrincipalAxisY          0 
    ----------------------  -----------------------------------------
    PrincipalAxisZ          0 
    ----------------------  -----------------------------------------
    ProjectAlongDirection   1 
    ----------------------  -----------------------------------------
    SnapPointToGrid         1 
    ----------------------  -----------------------------------------
    XCoordinate             0.0 
    ----------------------  -----------------------------------------
    YCoordinate             0.0 
    ----------------------  -----------------------------------------
    ZCoordinate             0.0 
    ======================  =========================================
    
    .. versionadded:: NX8.5.0
    """
    
    class Types():
        """
        Settings to indicate the construction type used for the datum surface. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Direct", "direct location"
           "Mirror", "mirror location"
        """
        Direct = 0  # DatumSurfaceBuilderTypesMemberType
        Mirror = 1  # DatumSurfaceBuilderTypesMemberType
        
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
        
    
    
    def MoveMinimumDistance(self) -> None:
        """
        Moves a point to the nearest location on the resting face 
        
        Signature ``MoveMinimumDistance()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def InitializeAxis(self, approximatePoint: NXOpen.Point3d) -> None:
        """
        Update the axis origin to a point specified, and direction to closest principal axis to face normal.  
        
        The point will be adjusted by snapping to a grid. 
        
        Signature ``InitializeAxis(approximatePoint)`` 
        
        :param approximatePoint: 
        :type approximatePoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateAxisData(self) -> None:
        """
        Updates data related to the axis.  
        
        The origin will be adjusted based on grid snapping, and projection direction.   In addition the control direction information will be updated.  
        
        Signature ``UpdateAxisData()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def UpdateWithReferenceDatum(self) -> None:
        """
        Initialize the builder with the inputs from an existing datum surface locator.  
        
        Signature ``UpdateWithReferenceDatum()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    DerivedDatum: SelectDatumSurface = ...
    """
    Returns  the derived datum 
    
    <hr>
    
    Getter Method
    
    Signature ``DerivedDatum`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.SelectDatumSurface` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    GridSnapTolerance: float = ...
    """
    Returns or sets  the grid snap tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``GridSnapTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GridSnapTolerance`` 
    
    :param gridSnapTolerance: 
    :type gridSnapTolerance: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    MirrorPlane: NXOpen.Plane = ...
    """
    Returns or sets  the plane used for mirroring a reference surface locator.  
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorPlane`` 
    
    :param mirrorPlane: 
    :type mirrorPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    RestingFace: NXOpen.ScCollector = ...
    """
    Returns  the resting face 
    
    <hr>
    
    Getter Method
    
    Signature ``RestingFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    SnapPointToGrid: bool = ...
    """
    Returns or sets  the snap point to grid option.  
    
    Specified locations will be adjusted based on the grid snap tolerance  
    
    <hr>
    
    Getter Method
    
    Signature ``SnapPointToGrid`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SnapPointToGrid`` 
    
    :param snapPointToGrid: 
    :type snapPointToGrid: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Type: DatumSurfaceBuilderTypes = ...
    """
    Returns or sets  the construction type used to create the datum surface.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.DatumSurfaceBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.DatumSurfaceBuilderTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    XCoordinate: float = ...
    """
    Returns or sets  the x coordinate position for the surface datum location.  
    
    <hr>
    
    Getter Method
    
    Signature ``XCoordinate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``XCoordinate`` 
    
    :param xCoordinate: 
    :type xCoordinate: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    YCoordinate: float = ...
    """
    Returns or sets  the y coordinate position for the surface datum location 
    
    <hr>
    
    Getter Method
    
    Signature ``YCoordinate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``YCoordinate`` 
    
    :param yCoordinate: 
    :type yCoordinate: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ZCoordinate: float = ...
    """
    Returns or sets  the z coordinate position for the datum surface location 
    
    <hr>
    
    Getter Method
    
    Signature ``ZCoordinate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZCoordinate`` 
    
    :param zCoordinate: 
    :type zCoordinate: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: DatumSurfaceBuilder = ...  # unknown typename


class WeldCreationDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldCreationDirection():
    """
    the type of creation direction 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "Default construction direction"
       "Opposite", "Opposite construction direction"
    """
    Default = 0  # WeldCreationDirectionMemberType
    Opposite = 1  # WeldCreationDirectionMemberType
    
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
    


class WeldAttribTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldAttribType():
    """
    the type of attribute
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Integer", "integer"
       "Real", "real"
       "Null", "null"
       "String", "stringt"
    """
    Integer = 1  # WeldAttribTypeMemberType
    Real = 2  # WeldAttribTypeMemberType
    Null = 4  # WeldAttribTypeMemberType
    String = 5  # WeldAttribTypeMemberType
    
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
    


class PlugSlotBuilderEnumContourMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlugSlotBuilderEnumContour():
    """
    contour type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Convex", " - "
       "Flush", " - "
       "Concave", " - "
    """
    NotSet = 0  # PlugSlotBuilderEnumContourMemberType
    Convex = 1  # PlugSlotBuilderEnumContourMemberType
    Flush = 2  # PlugSlotBuilderEnumContourMemberType
    Concave = 3  # PlugSlotBuilderEnumContourMemberType
    
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
    


class PlugSlotBuilderArcProcessEnumMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PlugSlotBuilderArcProcessEnum():
    """
    arc process for the weld feature 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Gmaw", " - "
       "Gtaw", " - "
       "Gtac", " - "
       "Smaw", " - "
       "Paw", " - "
    """
    Gmaw = 0  # PlugSlotBuilderArcProcessEnumMemberType
    Gtaw = 1  # PlugSlotBuilderArcProcessEnumMemberType
    Gtac = 2  # PlugSlotBuilderArcProcessEnumMemberType
    Smaw = 3  # PlugSlotBuilderArcProcessEnumMemberType
    Paw = 4  # PlugSlotBuilderArcProcessEnumMemberType
    
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
    


class PlugSlotBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Weld.PlugSlot` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreatePlugSlotBuilder`
    
    Default values.
    
    ====================  ==========================================
    Property              Value
    ====================  ==========================================
    AssignWeldPMI         0 
    --------------------  ------------------------------------------
    ContourDepth.Value    2.54 (millimeters part), .1 (inches part) 
    --------------------  ------------------------------------------
    ContourHeight.Value   2.54 (millimeters part), .1 (inches part) 
    --------------------  ------------------------------------------
    ContourType           None 
    --------------------  ------------------------------------------
    FieldWeld             0 
    ====================  ==========================================
    
    .. versionadded:: NX8.0.0
    """
    
    class EnumContour():
        """
        contour type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Convex", " - "
           "Flush", " - "
           "Concave", " - "
        """
        NotSet = 0  # PlugSlotBuilderEnumContourMemberType
        Convex = 1  # PlugSlotBuilderEnumContourMemberType
        Flush = 2  # PlugSlotBuilderEnumContourMemberType
        Concave = 3  # PlugSlotBuilderEnumContourMemberType
        
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
        
    
    
    class ArcProcessEnum():
        """
        arc process for the weld feature 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Gmaw", " - "
           "Gtaw", " - "
           "Gtac", " - "
           "Smaw", " - "
           "Paw", " - "
        """
        Gmaw = 0  # PlugSlotBuilderArcProcessEnumMemberType
        Gtaw = 1  # PlugSlotBuilderArcProcessEnumMemberType
        Gtac = 2  # PlugSlotBuilderArcProcessEnumMemberType
        Smaw = 3  # PlugSlotBuilderArcProcessEnumMemberType
        Paw = 4  # PlugSlotBuilderArcProcessEnumMemberType
        
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
        
    
    AssignWeldPMI: bool = ...
    """
    Returns or sets  the assign weld pmi 
    
    <hr>
    
    Getter Method
    
    Signature ``AssignWeldPMI`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssignWeldPMI`` 
    
    :param assignWeldPMI: 
    :type assignWeldPMI: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics 
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ContourDepth: NXOpen.Expression = ...
    """
    Returns  the contour depth 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ContourHeight: NXOpen.Expression = ...
    """
    Returns  the contour height needed for cap
    
    <hr>
    
    Getter Method
    
    Signature ``ContourHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ContourType: PlugSlotBuilderEnumContour = ...
    """
    Returns or sets  the contour type 
    
    <hr>
    
    Getter Method
    
    Signature ``ContourType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.PlugSlotBuilderEnumContour` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContourType`` 
    
    :param contourType: 
    :type contourType: :py:class:`NXOpen.Weld.PlugSlotBuilderEnumContour` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Edge1: NXOpen.Section = ...
    """
    Returns  the edge of the hole or slot on face1 
    
    <hr>
    
    Getter Method
    
    Signature ``Edge1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Face1: NXOpen.ScCollector = ...
    """
    Returns  the face1 
    
    <hr>
    
    Getter Method
    
    Signature ``Face1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Face2: NXOpen.ScCollector = ...
    """
    Returns  the face2 
    
    <hr>
    
    Getter Method
    
    Signature ``Face2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FieldWeld: bool = ...
    """
    Returns or sets  the field weld 
    
    <hr>
    
    Getter Method
    
    Signature ``FieldWeld`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FieldWeld`` 
    
    :param fieldWeld: 
    :type fieldWeld: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SeedFace1: NXOpen.Face = ...
    """
    Returns or sets  the top face on face1
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace1`` 
    
    :param seedFace1: 
    :type seedFace1: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SeedFace2: NXOpen.Face = ...
    """
    Returns or sets  the bottom face from which the weld will be extruded towards the top
    
    <hr>
    
    Getter Method
    
    Signature ``SeedFace2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SeedFace2`` 
    
    :param seedFace2: 
    :type seedFace2: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: PlugSlotBuilder = ...  # unknown typename


class JointmarkPointsBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[JointmarkPointsBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: JointmarkPointsBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
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
    
    
    def FindIndex(self, obj: JointmarkPointsBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> JointmarkPointsBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
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
    def Erase(self, obj: JointmarkPointsBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: JointmarkPointsBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
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
    
    
    def GetContents(self) -> 'list[JointmarkPointsBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[JointmarkPointsBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
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
    def Swap(self, object1: JointmarkPointsBuilder, object2: JointmarkPointsBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: JointmarkPointsBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.JointmarkPointsBuilder` 
        
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
    Null: JointmarkPointsBuilderList = ...  # unknown typename


class AutoPointBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AutoPointBuilderTypes():
    """
    Settings to indicate whether new features should be created, or if features will be reused. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "New", "new points are being created"
       "Move", "move existing points"
    """
    New = 0  # AutoPointBuilderTypesMemberType
    Move = 1  # AutoPointBuilderTypesMemberType
    
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
    


class AutoPointBuilderInterferenceDetailsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AutoPointBuilderInterferenceDetails():
    """
    Settings to indicate whether an interference is near an existing weld point. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoWeldsNearBodies", "Indicates no existing weld points are in this interference area"
       "Same", "Indicates weld points exist and part name are the same."
       "Replaced", "Indicates weld points exist and part names have changed."
       "Added", "Indicates weld points exist and parts were added."
       "Deleted", "Indicates weld points exist and parts were removed."
    """
    NoWeldsNearBodies = 0  # AutoPointBuilderInterferenceDetailsMemberType
    Same = 1  # AutoPointBuilderInterferenceDetailsMemberType
    Replaced = 2  # AutoPointBuilderInterferenceDetailsMemberType
    Added = 3  # AutoPointBuilderInterferenceDetailsMemberType
    Deleted = 4  # AutoPointBuilderInterferenceDetailsMemberType
    
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
    


class AutoPointBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Weld.AutoPointBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateAutoPointBuilder`
    
    Default values.
    
    =============================  ============================================
    Property                       Value
    =============================  ============================================
    DistanceFromEnds               15.0 (millimeters part), 0.5 (inches part) 
    -----------------------------  --------------------------------------------
    FaceGapDistance                1.5 (millimeters part), 0.05 (inches part) 
    -----------------------------  --------------------------------------------
    MaximumBendRadius              16 (millimeters part), 0.75 (inches part) 
    -----------------------------  --------------------------------------------
    MaximumCenterlineWidth         100 (millimeters part), 4 (inches part) 
    -----------------------------  --------------------------------------------
    MaximumSingleThickness         2 (millimeters part), 0.08 (inches part) 
    -----------------------------  --------------------------------------------
    MaximumSpacingBetweenPoints    50 (millimeters part), 2.0 (inches part) 
    -----------------------------  --------------------------------------------
    MimimumNumberPointsOnOverlap   3 
    -----------------------------  --------------------------------------------
    MinimumFlangeWidth             6.0 (millimeters part), 0.25 (inches part) 
    -----------------------------  --------------------------------------------
    MinimumSpacingBetweenPoints    25 (millimeters part), 1.0 (inches part) 
    -----------------------------  --------------------------------------------
    OffsetDistanceFromEdge         6.25 (millimeters part), 0.25 (inches part) 
    -----------------------------  --------------------------------------------
    ReuseMatchTolerance            1.0 (millimeters part), 0.04 (inches part) 
    -----------------------------  --------------------------------------------
    UniformSpacingTolerance        4 (millimeters part), 0.16 (inches part) 
    =============================  ============================================
    
    .. versionadded:: NX6.0.0
    """
    
    class Types():
        """
        Settings to indicate whether new features should be created, or if features will be reused. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "New", "new points are being created"
           "Move", "move existing points"
        """
        New = 0  # AutoPointBuilderTypesMemberType
        Move = 1  # AutoPointBuilderTypesMemberType
        
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
        
    
    
    class InterferenceDetails():
        """
        Settings to indicate whether an interference is near an existing weld point. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoWeldsNearBodies", "Indicates no existing weld points are in this interference area"
           "Same", "Indicates weld points exist and part name are the same."
           "Replaced", "Indicates weld points exist and part names have changed."
           "Added", "Indicates weld points exist and parts were added."
           "Deleted", "Indicates weld points exist and parts were removed."
        """
        NoWeldsNearBodies = 0  # AutoPointBuilderInterferenceDetailsMemberType
        Same = 1  # AutoPointBuilderInterferenceDetailsMemberType
        Replaced = 2  # AutoPointBuilderInterferenceDetailsMemberType
        Added = 3  # AutoPointBuilderInterferenceDetailsMemberType
        Deleted = 4  # AutoPointBuilderInterferenceDetailsMemberType
        
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
        
    
    
    def FindNumberOfInterferenceRegions(self) -> int:
        """
        Finds all the interference areas between the selected components.  
        
        This
        must be executed or no weld points will be created. The number of regions is 
        used as an index to get the interference status. The first index is 0.  
        
        Signature ``FindNumberOfInterferenceRegions()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CreateFeatureSet(self, interferenceIndex: int) -> NXOpen.NXObject:
        """
        Creates a feature set containing weld points for a given interference.  
        
        Signature ``CreateFeatureSet(interferenceIndex)`` 
        
        :param interferenceIndex:   Index to the desired interference  
        :type interferenceIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetInterferenceDetails(self, interferenceIndex: int) -> AutoPointBuilderInterferenceDetails:
        """
        The status indicating if the interference has existing weld points touching it.  
        
        The
        index for this function is described in the find number of interference regions method.  
        
        Signature ``GetInterferenceDetails(interferenceIndex)`` 
        
        :param interferenceIndex:   Index to the desired interference  
        :type interferenceIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.AutoPointBuilderInterferenceDetails` 
        
        .. versionadded:: NX7.5.4
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    @typing.overload
    def GetWeldType(self) -> None:
        """Returns or sets  the weld point type to create"""
        ...
    
    @typing.overload
    def GetWeldType(self) -> WeldFeatureSetType:
        """
        Getter Method
        
        Signature ``WeldType`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX10.0.0
           Use overloaded function with PointMark enum instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetWeldType(self, weldPointType: WeldFeatureSetType) -> None:
        """
        Setter Method
        
        Signature ``WeldType`` 
        
        :param weldPointType: 
        :type weldPointType: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX10.0.0
           Use overloaded function with PointMark enum instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    @typing.overload
    def GetWeldType(self) -> PointMarkBuilderWeldTypes:
        """
        Gets the weld type references in the customer defaults to create.  
        
        Signature ``GetWeldType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.PointMarkBuilderWeldTypes` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetWeldType(self) -> None:
        """Returns or sets  the weld point type to create"""
        ...
    
    @typing.overload
    def SetWeldType(self, weldPointType: WeldFeatureSetType) -> None:
        """
        Getter Method
        
        Signature ``WeldType`` 
        
        :param weldPointType: 
        :type weldPointType: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX10.0.0
           Use overloaded function with PointMark enum instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    @typing.overload
    def SetWeldType(self, weldPointType: WeldFeatureSetType) -> None:
        """
        Setter Method
        
        Signature ``WeldType`` 
        
        :param weldPointType: 
        :type weldPointType: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX10.0.0
           Use overloaded function with PointMark enum instead.
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    @typing.overload
    def SetWeldType(self, weldType: PointMarkBuilderWeldTypes) -> None:
        """
        Sets the weld type references in the customer defaults to create. 
        
        Signature ``SetWeldType(weldType)`` 
        
        :param weldType: 
        :type weldType: :py:class:`NXOpen.Weld.PointMarkBuilderWeldTypes` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    ComponentsToJoin: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the components that should be welded together.  
    
    This can be one components, or many. 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsToJoin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ComponentsTreatAsUnit: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the components to treat as unit.  
    
    No interferences will be found within this component. 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsTreatAsUnit`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    DistanceFromEnds: float = ...
    """
    Returns or sets  the distance from the ends to start creating weld points at 
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceFromEnds`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceFromEnds`` 
    
    :param distanceFromEnds: 
    :type distanceFromEnds: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceGapDistance: float = ...
    """
    Returns or sets  the face gap distance.  
    
    This will be used to find interferences between bodies. 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceGapDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceGapDistance`` 
    
    :param faceGapDistance: 
    :type faceGapDistance: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MaximumBendRadius: float = ...
    """
    Returns or sets  the bend radius of a flange.  
    
    Points will not be put on faces with a 
    radius smaller than this value. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumBendRadius`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumBendRadius`` 
    
    :param maximumBendRadius: 
    :type maximumBendRadius: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: ugweld ("UG WELD")
    """
    MaximumCenterlineWidth: float = ...
    """
    Returns or sets  the maximum centerline width.  
    
    Points will be created using the centerline method
    if the smallest width is less than this value. If greater, points will be
    created using the offset from edge method. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumCenterlineWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumCenterlineWidth`` 
    
    :param maximumCenterlineWidth: 
    :type maximumCenterlineWidth: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MaximumSingleThickness: float = ...
    """
    Returns or sets  the maximum single metal thinkness for all the selected components.  
    
    If the distance between top faces of two panels (or sheets) is greater
    than single thickness plus face gap distance, a point will not be created
    at that location. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumSingleThickness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumSingleThickness`` 
    
    :param maximumSingleThickness: 
    :type maximumSingleThickness: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: ugweld ("UG WELD")
    """
    MaximumSpacingBetweenPoints: float = ...
    """
    Returns or sets  the maximum spacing between points 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumSpacingBetweenPoints`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumSpacingBetweenPoints`` 
    
    :param maximumSpacingBetweenPoints: 
    :type maximumSpacingBetweenPoints: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MimimumNumberPointsOnOverlap: int = ...
    """
    Returns or sets  the mimimum number points to create on an overlap sheet 
    
    <hr>
    
    Getter Method
    
    Signature ``MimimumNumberPointsOnOverlap`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MimimumNumberPointsOnOverlap`` 
    
    :param mimimumNumberPointsOnOverlap: 
    :type mimimumNumberPointsOnOverlap: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    MinimumFlangeWidth: float = ...
    """
    Returns or sets  the minimum flange width.  
    
    If opposite sides of a flange are smaller than
    minimum flange width, it will be ignored. 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumFlangeWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumFlangeWidth`` 
    
    :param minimumFlangeWidth: 
    :type minimumFlangeWidth: float 
    
    .. versionadded:: NX6.0.2
    
    License requirements: ugweld ("UG WELD")
    """
    MinimumSpacingBetweenPoints: float = ...
    """
    Returns or sets  the minimum spacing between points 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumSpacingBetweenPoints`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MinimumSpacingBetweenPoints`` 
    
    :param minimumSpacingBetweenPoints: 
    :type minimumSpacingBetweenPoints: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    OffsetDistanceFromEdge: float = ...
    """
    Returns or sets  the offset distance from edge 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetDistanceFromEdge`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OffsetDistanceFromEdge`` 
    
    :param offsetDistanceFromEdge: 
    :type offsetDistanceFromEdge: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReuseFeatures: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the feature to reuse intead of creating new.  
    
    These features will be updated instead of creating new. 
    
    <hr>
    
    Getter Method
    
    Signature ``ReuseFeatures`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    """
    ReuseMatchTolerance: float = ...
    """
    Returns or sets  the distance used to determine if the location of an existing weld feature is coincident with the 
    newly calculated location.  
    
    If the locations are coincident, then the existing weld feature location will be reused.
    
    <hr>
    
    Getter Method
    
    Signature ``ReuseMatchTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReuseMatchTolerance`` 
    
    :param reuseMatchTolerance: 
    :type reuseMatchTolerance: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: ugweld ("UG WELD")
    """
    Type: AutoPointBuilderTypes = ...
    """
    Returns or sets  the type of creation.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.AutoPointBuilderTypes` 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.AutoPointBuilderTypes` 
    
    .. versionadded:: NX7.5.1
    
    License requirements: ugweld ("UG WELD")
    """
    UniformSpacingTolerance: float = ...
    """
    Returns or sets  the distance that maximum spacing can be exceeded to achieve uniform spacing 
    
    <hr>
    
    Getter Method
    
    Signature ``UniformSpacingTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UniformSpacingTolerance`` 
    
    :param uniformSpacingTolerance: 
    :type uniformSpacingTolerance: float 
    
    .. versionadded:: NX7.5.1
    
    License requirements: ugweld ("UG WELD")
    """
    WeldType: WeldFeatureSetType = ...
    """
    Returns or sets  the weld point type to create 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX10.0.0
       Use overloaded function with PointMark enum instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WeldType`` 
    
    :param weldPointType: 
    :type weldPointType: :py:class:`NXOpen.Weld.WeldFeatureSetType` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX10.0.0
       Use overloaded function with PointMark enum instead.
    
    License requirements: ugweld ("UG WELD")
    """
    Null: AutoPointBuilder = ...  # unknown typename


class WeldSpacingCalcMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldSpacingCalcMethod():
    """
    Settings spacing method type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Arclength", "spaces based on arc length"
       "ParallelXPlane", "spaces based on parallel x planes"
       "ParallelYPlane", "spaces based on parallel y planes"
       "ParallelZPlane", "spaces based on parallel z planes"
       "MiddleOfCurve", "spaces based on middle of curve"
       "NormalToBody", "spaces based on normal to body"
    """
    Arclength = 0  # WeldSpacingCalcMethodMemberType
    ParallelXPlane = 1  # WeldSpacingCalcMethodMemberType
    ParallelYPlane = 2  # WeldSpacingCalcMethodMemberType
    ParallelZPlane = 3  # WeldSpacingCalcMethodMemberType
    MiddleOfCurve = 4  # WeldSpacingCalcMethodMemberType
    NormalToBody = 5  # WeldSpacingCalcMethodMemberType
    
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
    


class Fill(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a Weld Fill feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.WeldFillBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Fill = ...  # unknown typename


class WeldPointReferenceSheetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointReferenceSheetType():
    """
    Settings for the reference sheet 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Overlap", "spot welds are based on the intersection of face sets"
       "Top", "spot welds are based on the first face set"
       "NotSet", "spot welds are points in 3d space"
    """
    Overlap = 0  # WeldPointReferenceSheetTypeMemberType
    Top = 1  # WeldPointReferenceSheetTypeMemberType
    NotSet = 2  # WeldPointReferenceSheetTypeMemberType
    
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
    


class WeldArcMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldArcMethod():
    """
    Settings for output type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Continuous", "creates a single solid"
       "Skip", "creates multiple solids"
    """
    Continuous = 0  # WeldArcMethodMemberType
    Skip = 1  # WeldArcMethodMemberType
    
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
    


class LogInfo():
    """
    Represents entity and its log message   
    
    .. versionadded:: NX7.5.0
    
    .
    Constructor: 
    NXOpen.Weld.LogInfo()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Entity: NXOpen.TaggedObject = ...
    """
    weld object
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.TaggedObject`
    """
    LogMessage: str = ...
    """
    log message
    <hr>
    
    Field Value
    Type:str
    """


class WeldGrooveTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveType():
    """
    Groove Creation Type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EdgesNotPrepared", "Edges are not prepared"
       "EdgesPrepared", "Edges are prepared"
    """
    EdgesNotPrepared = 0  # WeldGrooveTypeMemberType
    EdgesPrepared = 1  # WeldGrooveTypeMemberType
    
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
    


class WeldPrepareEdgesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPrepareEdges():
    """
    Settings for prepare edges 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Output edges will not be prepared"
       "EntireEdge", "Output edges will be prepared for entire edge length"
       "WeldLimits", "Output edges will be prepared for the weld length only"
       "Complex", "Same as entire edge, but use if a portion of target body is below the desired weld"
    """
    NotSet = 0  # WeldPrepareEdgesMemberType
    EntireEdge = 1  # WeldPrepareEdgesMemberType
    WeldLimits = 2  # WeldPrepareEdgesMemberType
    Complex = 3  # WeldPrepareEdgesMemberType
    
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
    


class WeldBeadBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadBuilderTypes():
    """
    Settings to indicate the sweep shape of the bead. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Ellipse", "ellipse shape"
       "Tube", "tube shape"
       "Sketch", "sketch shape"
       "Triangle", "triangle shape"
       "Rectangle", "rectangle shape"
    """
    Ellipse = 0  # WeldBeadBuilderTypesMemberType
    Tube = 1  # WeldBeadBuilderTypesMemberType
    Sketch = 2  # WeldBeadBuilderTypesMemberType
    Triangle = 3  # WeldBeadBuilderTypesMemberType
    Rectangle = 4  # WeldBeadBuilderTypesMemberType
    
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
    


class WeldBeadBuilderBeadLocationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadBuilderBeadLocationMethod():
    """
    Settings to indicate the desired location of the bead. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SecondaryParts", "on the secondary parts"
       "PrimaryParts", "on the primary parts"
       "InSpace", "in space. No on any parts"
    """
    SecondaryParts = 0  # WeldBeadBuilderBeadLocationMethodMemberType
    PrimaryParts = 1  # WeldBeadBuilderBeadLocationMethodMemberType
    InSpace = 2  # WeldBeadBuilderBeadLocationMethodMemberType
    
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
    


class WeldBeadBuilderFaceInferMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadBuilderFaceInferMethodType():
    """
    Settings to indicate the method for obtaining faces used when creating the guide curve path. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TangentFaces", "use faces tangent to selected faces to create the bead path curve"
       "NotSet", "only use selected faces to create the bead path curve"
    """
    TangentFaces = 0  # WeldBeadBuilderFaceInferMethodTypeMemberType
    NotSet = 1  # WeldBeadBuilderFaceInferMethodTypeMemberType
    
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
    


class WeldBeadBuilderOutputTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldBeadBuilderOutputTypes():
    """
    Settings to indicate the update behaviour of the bead feature 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fixed", "Bead does not recreate itself on update."
       "Associative", "Bead follows normal update behaviour."
    """
    Fixed = 0  # WeldBeadBuilderOutputTypesMemberType
    Associative = 1  # WeldBeadBuilderOutputTypesMemberType
    
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
    


class WeldBeadBuilder(NXOpen.Builder):
    """
    Used to create or edit a :py:class:`NXOpen.Weld.WeldBead` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateWeldBeadBuilder`
    
    Default values.
    
    ================  ===============
    Property          Value
    ================  ===============
    BeadLocation      SecondaryParts 
    ----------------  ---------------
    FaceInferMethod   None 
    ----------------  ---------------
    TangentAngle      45.0 
    ================  ===============
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        Settings to indicate the sweep shape of the bead. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Ellipse", "ellipse shape"
           "Tube", "tube shape"
           "Sketch", "sketch shape"
           "Triangle", "triangle shape"
           "Rectangle", "rectangle shape"
        """
        Ellipse = 0  # WeldBeadBuilderTypesMemberType
        Tube = 1  # WeldBeadBuilderTypesMemberType
        Sketch = 2  # WeldBeadBuilderTypesMemberType
        Triangle = 3  # WeldBeadBuilderTypesMemberType
        Rectangle = 4  # WeldBeadBuilderTypesMemberType
        
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
        
    
    
    class BeadLocationMethod():
        """
        Settings to indicate the desired location of the bead. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SecondaryParts", "on the secondary parts"
           "PrimaryParts", "on the primary parts"
           "InSpace", "in space. No on any parts"
        """
        SecondaryParts = 0  # WeldBeadBuilderBeadLocationMethodMemberType
        PrimaryParts = 1  # WeldBeadBuilderBeadLocationMethodMemberType
        InSpace = 2  # WeldBeadBuilderBeadLocationMethodMemberType
        
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
        
    
    
    class FaceInferMethodType():
        """
        Settings to indicate the method for obtaining faces used when creating the guide curve path. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TangentFaces", "use faces tangent to selected faces to create the bead path curve"
           "NotSet", "only use selected faces to create the bead path curve"
        """
        TangentFaces = 0  # WeldBeadBuilderFaceInferMethodTypeMemberType
        NotSet = 1  # WeldBeadBuilderFaceInferMethodTypeMemberType
        
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
        
    
    
    class OutputTypes():
        """
        Settings to indicate the update behaviour of the bead feature 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fixed", "Bead does not recreate itself on update."
           "Associative", "Bead follows normal update behaviour."
        """
        Fixed = 0  # WeldBeadBuilderOutputTypesMemberType
        Associative = 1  # WeldBeadBuilderOutputTypesMemberType
        
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
        
    
    
    def NewPath(self) -> WeldBeadPathBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldBeadPathBuilder` object.  
        
        Signature ``NewPath()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldBeadPathBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def NewSize(self) -> WeldBeadSizeBuilder:
        """
        Creates a :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` object.  
        
        Signature ``NewSize()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetPreviewPath(self) -> NXOpen.Spline:
        """
        The preview curve that will be used to create the bead solid.  
        
        Signature ``GetPreviewPath()`` 
        
        :returns:  The preview curve.  
        :rtype: :py:class:`NXOpen.Spline` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: None.
        """
        ...
    
    
    def CreatePreviewPath(self) -> NXOpen.Spline:
        """
        Creates a preview curve that will be used to create the bead solid.  
        
        Signature ``CreatePreviewPath()`` 
        
        :returns:  The preview curve.  
        :rtype: :py:class:`NXOpen.Spline` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    BeadLocation: WeldBeadBuilderBeadLocationMethod = ...
    """
    Returns or sets  the desired bead location.  
    
    <hr>
    
    Getter Method
    
    Signature ``BeadLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadBuilderBeadLocationMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BeadLocation`` 
    
    :param beadLocation: 
    :type beadLocation: :py:class:`NXOpen.Weld.WeldBeadBuilderBeadLocationMethod` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics to assign to the object created.  
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance for constructing the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtendToBoundary: bool = ...
    """
    Returns or sets  the option to control if the bead guide curve should extend to the nearest face boundary.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendToBoundary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendToBoundary`` 
    
    :param extendToBoundary: 
    :type extendToBoundary: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    FaceInferMethod: WeldBeadBuilderFaceInferMethodType = ...
    """
    Returns or sets  the method to use when inferring faces to create the bead guide curve path.  
    
    <hr>
    
    Getter Method
    
    Signature ``FaceInferMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadBuilderFaceInferMethodType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FaceInferMethod`` 
    
    :param faceInferMethod: 
    :type faceInferMethod: :py:class:`NXOpen.Weld.WeldBeadBuilderFaceInferMethodType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD")
    """
    OutputType: WeldBeadBuilderOutputTypes = ...
    """
    Returns or sets  the output type which controls the update behaviour of the bead feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadBuilderOutputTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldBeadBuilderOutputTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PathList: WeldBeadPathBuilderList = ...
    """
    Returns  the list containing the defined path segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadPathBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectBottomParts: NXOpen.ScCollector = ...
    """
    Returns  the collector containing the secondary bodies the bead is attached to.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectBottomParts`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectTopParts: NXOpen.ScCollector = ...
    """
    Returns  the collector containing the primary bodies the bead is attached to.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectTopParts`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SizeList: WeldBeadSizeBuilderList = ...
    """
    Returns  the list containing the sizes used to create the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``SizeList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadSizeBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TangentAngle: float = ...
    """
    Returns or sets  the tangent angle used to find faces tangent to the seed face specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``TangentAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TangentAngle`` 
    
    :param tangentAngle: 
    :type tangentAngle: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Type: WeldBeadBuilderTypes = ...
    """
    Returns or sets  the shape of the bead to create.  
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldBeadBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Weld.WeldBeadBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldBeadBuilder = ...  # unknown typename


class UserDefinedWeldBuilderWeldTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedWeldBuilderWeldTypes():
    """
    Weld types for 4GD classes. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Groove", "Groove Weld type."
       "Fillet", "Fillet Weld type."
       "PlugSlot", "Plug Slot Weld type."
       "Bead", "Bead Weld type."
       "Fill", "Fill Weld type."
    """
    Groove = 0  # UserDefinedWeldBuilderWeldTypesMemberType
    Fillet = 1  # UserDefinedWeldBuilderWeldTypesMemberType
    PlugSlot = 2  # UserDefinedWeldBuilderWeldTypesMemberType
    Bead = 3  # UserDefinedWeldBuilderWeldTypesMemberType
    Fill = 4  # UserDefinedWeldBuilderWeldTypesMemberType
    
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
    


class UserDefinedWeldBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Weld.UserDefinedWeldBuilder` builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateUserDefinedWeldBuilder`
    
    Default values.
    
    ==============  =====
    Property        Value
    ==============  =====
    AssignWeldPMI   0 
    ==============  =====
    
    .. versionadded:: NX7.5.0
    """
    
    class WeldTypes():
        """
        Weld types for 4GD classes. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Groove", "Groove Weld type."
           "Fillet", "Fillet Weld type."
           "PlugSlot", "Plug Slot Weld type."
           "Bead", "Bead Weld type."
           "Fill", "Fill Weld type."
        """
        Groove = 0  # UserDefinedWeldBuilderWeldTypesMemberType
        Fillet = 1  # UserDefinedWeldBuilderWeldTypesMemberType
        PlugSlot = 2  # UserDefinedWeldBuilderWeldTypesMemberType
        Bead = 3  # UserDefinedWeldBuilderWeldTypesMemberType
        Fill = 4  # UserDefinedWeldBuilderWeldTypesMemberType
        
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
        
    
    AssignWeldPMI: bool = ...
    """
    Returns or sets  the assign weld pmi.  
    
    <hr>
    
    Getter Method
    
    Signature ``AssignWeldPMI`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AssignWeldPMI`` 
    
    :param assignWeldPMI: 
    :type assignWeldPMI: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics.  
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Class4gd: UserDefinedWeldBuilderWeldTypes = ...
    """
    Returns or sets  the 4GD class option.  
    
    <hr>
    
    Getter Method
    
    Signature ``Class4gd`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.UserDefinedWeldBuilderWeldTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Class4gd`` 
    
    :param assignWeldPMI: 
    :type assignWeldPMI: :py:class:`NXOpen.Weld.UserDefinedWeldBuilderWeldTypes` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: ugweld ("UG WELD")
    """
    SelectBody: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the select body.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectConnectParts: NXOpen.ScCollector = ...
    """
    Returns  the select connect parts.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectConnectParts`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectEdge: NXOpen.SelectDisplayableObjectList = ...
    """
    Returns  the select edge.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: UserDefinedWeldBuilder = ...  # unknown typename


class JointmarkElement(NXOpen.Features.Feature, IFeature):
    """
    Represents a Weld.  
    
    JointmarkElement Feature. 
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.JointmarkBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: JointmarkElement = ...  # unknown typename


class SelectDatumSurface(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a single object selection.  
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def SetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumSurface) -> None:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumSurface) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumSurface, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
        The object being selected with the object's view and object's point
        
        Signature ``SetValue(selection, view, point)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
        :param view:  selected object view 
        :type view: :py:class:`NXOpen.View` 
        :param point:  selected object point 
        :type point: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, snapType: NXOpen.InferSnapTypeSnapType, selection1: DatumSurface, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DatumSurface, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
        The object being selected with the objects view and objects point and snap information.
        
        Signature ``SetValue(snapType, selection1, view1, point1, selection2, view2, point2)`` 
        
        :param snapType:   snap point type 
        :type snapType: :py:class:`NXOpen.InferSnapTypeSnapType` 
        :param selection1:  first selected object  
        :type selection1: :py:class:`NXOpen.Weld.DatumSurface` 
        :param view1:  first selected object view 
        :type view1: :py:class:`NXOpen.View` 
        :param point1:  first selected object point 
        :type point1: :py:class:`NXOpen.Point3d` 
        :param selection2:  second selected object  
        :type selection2: :py:class:`NXOpen.Weld.DatumSurface` 
        :param view2:  second selected object view 
        :type view2: :py:class:`NXOpen.View` 
        :param point2:  second selected object point 
        :type point2: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, selection: DatumSurface, caeSubType: NXOpen.CaeObjectTypeCaeSubType, caeSubId: int) -> None:
        """
        The object being selected with CAE set object information.
        
        Signature ``SetValue(selection, caeSubType, caeSubId)`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
        :param caeSubType:  CAE set object sub type 
        :type caeSubType: :py:class:`NXOpen.CaeObjectTypeCaeSubType` 
        :param caeSubId:  CAE set object sub id 
        :type caeSubId: int 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.SetValue`.
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetValue(self) -> None:
        """Returns or sets  the object being selected"""
        ...
    
    @typing.overload
    def GetValue(self) -> DatumSurface:
        """
        Getter Method
        
        Signature ``Value`` 
        
        :returns:  selected object  
        :rtype: :py:class:`NXOpen.Weld.DatumSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self, selection: DatumSurface) -> None:
        """
        Setter Method
        
        Signature ``Value`` 
        
        :param selection:  selected object  
        :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the object's view and point.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, view, point). selection is a :py:class:`NXOpen.Weld.DatumSurface`.   selected object view is a :py:class:`NXOpen.View`.   selected object viewpoint is a :py:class:`NXOpen.Point3d`.   selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with the objects view and point and snap information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (snapType, selection1, view1, point1, selection2, view2, point2). snapType is a :py:class:`NXOpen.InferSnapTypeSnapType`.    snap point typeselection1 is a :py:class:`NXOpen.Weld.DatumSurface`.   first selected object view1 is a :py:class:`NXOpen.View`.   first selected object viewpoint1 is a :py:class:`NXOpen.Point3d`.   first selected object pointselection2 is a :py:class:`NXOpen.Weld.DatumSurface`.   second selected object view2 is a :py:class:`NXOpen.View`.   second selected object viewpoint2 is a :py:class:`NXOpen.Point3d`.   second selected object point
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetValue(self) -> tuple:
        """
        The object being selected with CAE set object information.
        
        Signature ``GetValue()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (selection, caeSubType, caeSubId). selection is a :py:class:`NXOpen.Weld.DatumSurface`.   selected object caeSubType is a :py:class:`NXOpen.CaeObjectTypeCaeSubType`.   CAE set object sub typecaeSubId is a int.   CAE set object sub id
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use other versions of :py:meth:`NXOpen.SelectObject.GetValue`.
        
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
    
    Value: DatumSurface = ...
    """
    Returns or sets  the object being selected
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns:  selected object  
    :rtype: :py:class:`NXOpen.Weld.DatumSurface` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Value`` 
    
    :param selection:  selected object  
    :type selection: :py:class:`NXOpen.Weld.DatumSurface` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: SelectDatumSurface = ...  # unknown typename


class EdgePrep(NXOpen.Features.BodyFeature):
    """
    Represents a Weld Edge Prep feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.EdgePrepBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: EdgePrep = ...  # unknown typename


class Transform(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a Weld Transform Feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.TransformBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Transform = ...  # unknown typename


class SurfaceWeldBuilderDestinationTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SurfaceWeldBuilderDestinationTypes():
    """
    The option specifying where the surface weld feature should be created. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WorkPart", " - "
       "NewComponent", " - "
    """
    WorkPart = 0  # SurfaceWeldBuilderDestinationTypesMemberType
    NewComponent = 1  # SurfaceWeldBuilderDestinationTypesMemberType
    
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
    


class SurfaceWeldBuilder(StructureWeldBuilder):
    """
    Use to create or edit a :py:class:`NXOpen.Weld.SurfaceWeld` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateSurfaceWeldBuilder`
    
    Default values.
    
    ================  ===========================================
    Property          Value
    ================  ===========================================
    Thickness.Value   12.2 (millimeters part), 0.5 (inches part) 
    ----------------  -------------------------------------------
    Width.Value       12.2 (millimeters part), 0.5 (inches part) 
    ================  ===========================================
    
    .. versionadded:: NX9.0.0
    """
    
    class DestinationTypes():
        """
        The option specifying where the surface weld feature should be created. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WorkPart", " - "
           "NewComponent", " - "
        """
        WorkPart = 0  # SurfaceWeldBuilderDestinationTypesMemberType
        NewComponent = 1  # SurfaceWeldBuilderDestinationTypesMemberType
        
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
        
    
    Boundary: NXOpen.Section = ...
    """
    Returns  the section defining all the boundaries to use for creating the surface weld.  
    
    The largest boundary will be treated as the primary exterior boundary. 
    
    <hr>
    
    Getter Method
    
    Signature ``Boundary`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics to assign to the object created.  
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Destination: SurfaceWeldBuilderDestinationTypes = ...
    """
    Returns or sets  the option specifying the destination for this surface weld feature.  
    
    Only applicable during create. 
    
    <hr>
    
    Getter Method
    
    Signature ``Destination`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.SurfaceWeldBuilderDestinationTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Destination`` 
    
    :param destination: 
    :type destination: :py:class:`NXOpen.Weld.SurfaceWeldBuilderDestinationTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance for constructing the surface weld.  
    
    Uses the modeling tolerance during creation. 
    
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
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX9.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    LineColorFontWidth: NXOpen.LineColorFontWidthBuilder = ...
    """
    Returns  the color, font, and width of the surface weld output curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``LineColorFontWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.LineColorFontWidthBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    NamePrefix: str = ...
    """
    Returns or sets  the prefix used for the surface weld Design Feature name in Fourth Generation Design mode.  
    
    Only applicable during create. 
    
    <hr>
    
    Getter Method
    
    Signature ``NamePrefix`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NamePrefix`` 
    
    :param prefix:     
    :type prefix: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: structure_weld ("STRUCTURE WELD")
    """
    Panel: NXOpen.ScCollector = ...
    """
    Returns  the collector containing the faces to create the surface weld on.  
    
    <hr>
    
    Getter Method
    
    Signature ``Panel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ProjectionDirection: NXOpen.GeometricUtilities.ProjectionOptions = ...
    """
    Returns  the project direction, which is used to project the boundary curves to the plate mold face.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProjectionDirection`` 
    
    :returns:  Projection Options data.  
    :rtype: :py:class:`NXOpen.GeometricUtilities.ProjectionOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the thickness of the surface weld.  
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the expression containing the value of the width of the surface weld if only the centerline is specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    Null: SurfaceWeldBuilder = ...  # unknown typename


class JointmarkGuideBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[JointmarkGuideBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: JointmarkGuideBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
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
    
    
    def FindIndex(self, obj: JointmarkGuideBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> JointmarkGuideBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
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
    def Erase(self, obj: JointmarkGuideBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: JointmarkGuideBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
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
    
    
    def GetContents(self) -> 'list[JointmarkGuideBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[JointmarkGuideBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
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
    def Swap(self, object1: JointmarkGuideBuilder, object2: JointmarkGuideBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: JointmarkGuideBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Weld.JointmarkGuideBuilder` 
        
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
    Null: JointmarkGuideBuilderList = ...  # unknown typename


class CompoundWeld(NXOpen.Features.Feature):
    """
    Represents a compound weld feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.CompoundWeldBuilder`
    
    .. versionadded:: NX9.0.0
    """
    Null: CompoundWeld = ...  # unknown typename


class EdgePrepBuilder(NXOpen.Builder):
    """
    A builder used to create or edit a :py:class:`NXOpen.Weld.EdgePrep` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateEdgePrepBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetNoResultsInfo(self) -> 'list[NXOpen.Curve]':
        """
        Returns the curves that weld preparation was attempted on, but could not be performed.  
        
        Signature ``GetNoResultsInfo()`` 
        
        :returns:  The welding joint curves that weld preparation failed on.  
        :rtype: list of :py:class:`NXOpen.Curve` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    ErrorCode: int = ...
    """
    Returns  the error code for the first welding joint curve that could not be processed.  
    
    <hr>
    
    Getter Method
    
    Signature ``ErrorCode`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    WeldObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the welding joints to drive edge preparation 
    
    <hr>
    
    Getter Method
    
    Signature ``WeldObjects`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: EdgePrepBuilder = ...  # unknown typename


class Extract(NXOpen.Features.Feature):
    """
    Represents a Linked Feature created in the Weld Assistant.  
    
    This class supports operations on a Weld Extract faces.
    
    .. versionadded:: NX5.0.0
    """
    
    def CompressFace(self) -> None:
        """
        Compresses the size of weld linked face objects.  
        
        This will reduce file size when the
        object is stored. On edit these faces will be automatically recreated. 
        
        Signature ``CompressFace()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    Null: Extract = ...  # unknown typename


class SurfaceWeld(NXOpen.Features.CurveFeature, IFeature):
    """
    Represents a surface weld feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.SurfaceWeldBuilder`
    
    .. versionadded:: NX9.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: SurfaceWeld = ...  # unknown typename


class ConnectionFinderBuilderFilterTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConnectionFinderBuilderFilterTypes():
    """
    Filter values to control "Save All" processing. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", " - "
       "Passed", " - "
       "Warning", " - "
       "Failed", " - "
       "Saved", " - "
       "NotSaved", " - "
       "Deleted", " - "
    """
    All = 0  # ConnectionFinderBuilderFilterTypesMemberType
    Passed = 1  # ConnectionFinderBuilderFilterTypesMemberType
    Warning = 2  # ConnectionFinderBuilderFilterTypesMemberType
    Failed = 3  # ConnectionFinderBuilderFilterTypesMemberType
    Saved = 4  # ConnectionFinderBuilderFilterTypesMemberType
    NotSaved = 5  # ConnectionFinderBuilderFilterTypesMemberType
    Deleted = 6  # ConnectionFinderBuilderFilterTypesMemberType
    
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
    


class ConnectionFinderBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a builder to display, manage, delete, and allow the user to
    reparent face information for the weld objects.  
    
    .. versionadded:: NX9.0.0
    """
    
    class FilterTypes():
        """
        Filter values to control "Save All" processing. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", " - "
           "Passed", " - "
           "Warning", " - "
           "Failed", " - "
           "Saved", " - "
           "NotSaved", " - "
           "Deleted", " - "
        """
        All = 0  # ConnectionFinderBuilderFilterTypesMemberType
        Passed = 1  # ConnectionFinderBuilderFilterTypesMemberType
        Warning = 2  # ConnectionFinderBuilderFilterTypesMemberType
        Failed = 3  # ConnectionFinderBuilderFilterTypesMemberType
        Saved = 4  # ConnectionFinderBuilderFilterTypesMemberType
        NotSaved = 5  # ConnectionFinderBuilderFilterTypesMemberType
        Deleted = 6  # ConnectionFinderBuilderFilterTypesMemberType
        
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
        
    
    
    def ReorderBeforeFaceNode(self, parentTag: NXOpen.NXObject, faceSetIndexToMove: int, faceSetIndexToReoderBefore: int) -> None:
        """
        Reorders a selected face by putting it before the specified face.  
        
        Indices start at 0 for the 1st element. 
        
        Signature ``ReorderBeforeFaceNode(parentTag, faceSetIndexToMove, faceSetIndexToReoderBefore)`` 
        
        :param parentTag:  Parent Weld Feature.  
        :type parentTag: :py:class:`NXOpen.NXObject` 
        :param faceSetIndexToMove:  Index of the face set to reorder  
        :type faceSetIndexToMove: int 
        :param faceSetIndexToReoderBefore:  Index of the face set to reposition before  
        :type faceSetIndexToReoderBefore: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReorderAfterFaceNode(self, parentTag: NXOpen.NXObject, faceSetIndexToMove: int, faceSetIndexToReoderAfter: int) -> None:
        """
        Reorders a selected face by putting it after the specified face.  
        
        Indices start at 0 for the 1st element. 
        
        Signature ``ReorderAfterFaceNode(parentTag, faceSetIndexToMove, faceSetIndexToReoderAfter)`` 
        
        :param parentTag:  Parent Weld Feature.  
        :type parentTag: :py:class:`NXOpen.NXObject` 
        :param faceSetIndexToMove:  Index of the face set to reorder  
        :type faceSetIndexToMove: int 
        :param faceSetIndexToReoderAfter:  Index of the face set to reposition after  
        :type faceSetIndexToReoderAfter: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def CenterNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
        Adjusts the display of the part and fits the selected weld points in the center of the graphics window.  
        
        Signature ``CenterNode(nodeTag)`` 
        
        :param nodeTag:  Weld Feature.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def DeleteNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
        Deletes the connected part information from the results.  
        
        Signature ``DeleteNode(nodeTag)`` 
        
        :param nodeTag:  Weld Feature  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SaveAllTree(self) -> None:
        """
        Identify all the connected part information as "saved" so the commit will save the information.  
        
        Dependent on value of :py:class:`NXOpen.Weld.ConnectionFinderBuilderFilterTypes`. Will not mark nodes identified in failure condition. 
        
        Signature ``SaveAllTree()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ClearAllTree(self) -> None:
        """
        Clears the tree list and allows you to perform another search.  
        
        Signature ``ClearAllTree()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def SaveNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
        Identify the connected part information as "saved" so commit will save the information.  
        
        Signature ``SaveNode(nodeTag)`` 
        
        :param nodeTag:  Weld Feature.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReassignFaceNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.NXObject) -> None:
        """
        Reassign the faces from the Reassign Face collector to the specified node.  
        
        Signature ``ReassignFaceNode(ownerTag, nodeTag)`` 
        
        :param ownerTag:  Weld Feature Set or Feature Point.  
        :type ownerTag: :py:class:`NXOpen.NXObject` 
        :param nodeTag:  Face, or collector, identify which faces to modify in set or point.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ClearMarking(self, nodeTag: NXOpen.NXObject) -> None:
        """
        Unmarks (removes save or delete mark) the weld feature from processing.  
        
        Signature ``ClearMarking(nodeTag)`` 
        
        :param nodeTag:  Weld Feature.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def IsFaceNodeEmpty(self, weldObject: NXOpen.NXObject, faceNodeIndex: int) -> bool:
        """
        Identify if the face collector for a specific weld object and index has faces assigned to it.  
        
        Search will be limited by the list feature set setting. An error will be returned if the face node cannot be found or the collector is missing.  
        
        Signature ``IsFaceNodeEmpty(weldObject, faceNodeIndex)`` 
        
        :param weldObject:  Specific weld feature set or point to search for.  
        :type weldObject: :py:class:`NXOpen.NXObject` 
        :param faceNodeIndex:  Specific position index to look for in the weld object.  
        :type faceNodeIndex: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFaceNodeCollector(self, weldObject: NXOpen.NXObject, faceNodeIndex: int) -> NXOpen.ScCollector:
        """
        Get the face collector for a specific weld object and index.  
        
        This is useful when the face node for the object is empty and you need to populate it. Search will be limited by the list feature set setting.  
        
        Signature ``GetFaceNodeCollector(weldObject, faceNodeIndex)`` 
        
        :param weldObject:  Specific weld feature set or point to search for.  
        :type weldObject: :py:class:`NXOpen.NXObject` 
        :param faceNodeIndex:  Specific position index to look for in the weld object.  
        :type faceNodeIndex: int 
        :returns:  Can return None if not found.  
        :rtype: :py:class:`NXOpen.ScCollector` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ReorderBeforeEdgeNode(self, parentTag: NXOpen.NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderBefore: int) -> None:
        """
        Reorders a selected edge by putting it before the specified edge.  
        
        Indices start at 0 for the 1st element. 
        
        Signature ``ReorderBeforeEdgeNode(parentTag, edgeSetIndexToMove, edgeSetIndexToReoderBefore)`` 
        
        :param parentTag:  Parent Weld Feature.  
        :type parentTag: :py:class:`NXOpen.NXObject` 
        :param edgeSetIndexToMove:  Index of the edge set to reorder  
        :type edgeSetIndexToMove: int 
        :param edgeSetIndexToReoderBefore:  Index of the edge set to reposition before  
        :type edgeSetIndexToReoderBefore: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReorderAfterEdgeNode(self, parentTag: NXOpen.NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderAfter: int) -> None:
        """
        Reorders a selected edge by putting it after the specified edge.  
        
        Indices start at 0 for the 1st element. 
        
        Signature ``ReorderAfterEdgeNode(parentTag, edgeSetIndexToMove, edgeSetIndexToReoderAfter)`` 
        
        :param parentTag:  Parent Weld Feature.  
        :type parentTag: :py:class:`NXOpen.NXObject` 
        :param edgeSetIndexToMove:  Index of the edge set to reorder  
        :type edgeSetIndexToMove: int 
        :param edgeSetIndexToReoderAfter:  Index of the edge set to reposition after  
        :type edgeSetIndexToReoderAfter: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def ReassignEdgeNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.NXObject) -> None:
        """
        Reassign the edges from the Reassign Edge collector to the specified node.  
        
        Signature ``ReassignEdgeNode(ownerTag, nodeTag)`` 
        
        :param ownerTag:  Weld Feature Set or Feature Point.  
        :type ownerTag: :py:class:`NXOpen.NXObject` 
        :param nodeTag:  Edge, or collector, identify which edges to modify in set or point.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def IsEdgeNodeEmpty(self, weldObject: NXOpen.NXObject, edgeNodeIndex: int) -> bool:
        """
        Identify if the edge collector for a specific weld object and index has edges assigned to it.  
        
        Search will be limited by the list feature set setting. An error will be returned if the edge node cannot be found or the collector is missing.  
        
        Signature ``IsEdgeNodeEmpty(weldObject, edgeNodeIndex)`` 
        
        :param weldObject:  Specific weld feature set or point to search for.  
        :type weldObject: :py:class:`NXOpen.NXObject` 
        :param edgeNodeIndex:  Specific position index to look for in the weld object.  
        :type edgeNodeIndex: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetEdgeNodeCollector(self, weldObject: NXOpen.NXObject, edgeNodeIndex: int) -> NXOpen.ScCollector:
        """
        Get the edge collector for a specific weld object and index.  
        
        This is useful when the edge node for the object is empty and you need to populate it. Search will be limited by the list feature set setting.  
        
        Signature ``GetEdgeNodeCollector(weldObject, edgeNodeIndex)`` 
        
        :param weldObject:  Specific weld feature set or point to search for.  
        :type weldObject: :py:class:`NXOpen.NXObject` 
        :param edgeNodeIndex:  Specific position index to look for in the weld object.  
        :type edgeNodeIndex: int 
        :returns:  Can return None if not found.  
        :rtype: :py:class:`NXOpen.ScCollector` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RequiredFaceNode(self, nodeTag: NXOpen.NXObject, isRequired: bool) -> None:
        """
        Identify if the face node is required (true) or optional (false).  
        
        This is used in the case where a weld point has been identified as having faces from only 1 connected part. 
        
        Signature ``RequiredFaceNode(nodeTag, isRequired)`` 
        
        :param nodeTag:  Weld face identifier. Typically, this will be the tag for the collector.  
        :type nodeTag: :py:class:`NXOpen.NXObject` 
        :param isRequired:  Is the face node required (true) or optional (false)?  
        :type isRequired: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetFaces(self, weldObject: NXOpen.NXObject) -> 'list[NXOpen.ScCollector]':
        """
        Get the face collectors for the given feature set or point depending on the :py:meth:`NXOpen.Weld.ConnectionFinderBuilder.ListFeatureSet``.  
        
        Signature ``GetFaces(weldObject)`` 
        
        :param weldObject:  Specific weld feature set or point to search for.  
        :type weldObject: :py:class:`NXOpen.NXObject` 
        :returns:  Face Collectors.  
        :rtype: list of :py:class:`NXOpen.ScCollector` 
        
        .. versionadded:: NX10.0.2
        
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
    
    Filter: ConnectionFinderBuilderFilterTypes = ...
    """
    Returns or sets  the filter values to contol Save All processing.  
    
    <hr>
    
    Getter Method
    
    Signature ``Filter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.ConnectionFinderBuilderFilterTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Filter`` 
    
    :param filter: 
    :type filter: :py:class:`NXOpen.Weld.ConnectionFinderBuilderFilterTypes` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ListFeatureSet: bool = ...
    """
    Returns or sets  the option to list the search results according to the feature sets that the specified weld point belongs to.  
    
    <hr>
    
    Getter Method
    
    Signature ``ListFeatureSet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ListFeatureSet`` 
    
    :param listFeatureSet: 
    :type listFeatureSet: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReassignEdge: NXOpen.ScCollector = ...
    """
    Returns  the edges to use when the reassign button is invoked.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReassignEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    ReassignFace: NXOpen.ScCollector = ...
    """
    Returns  the faces to use when the reassign button is invoked.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReassignFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    UpdateCoordinateSystem: bool = ...
    """
    Returns or sets  the option to update the coordinate system for the node from the obtained reconnection when saved.  
    
    <hr>
    
    Getter Method
    
    Signature ``UpdateCoordinateSystem`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpdateCoordinateSystem`` 
    
    :param updateCoordinateSystem: 
    :type updateCoordinateSystem: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: ConnectionFinderBuilder = ...  # unknown typename


class WeldFeatureOutputMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldFeatureOutput():
    """
    Feature output 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Curves", "Output only curves"
       "Solid", "Output only solids"
       "Both", "Output both curves and solids"
    """
    Curves = 0  # WeldFeatureOutputMemberType
    Solid = 1  # WeldFeatureOutputMemberType
    Both = 2  # WeldFeatureOutputMemberType
    
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
    


class JointmarkGuideBuilderLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkGuideBuilderLocation():
    """
    The type of guide curve 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CenterLine", "Centerline"
       "OffsetFromEdge", "Offset from Edge"
       "ExistingCurve", "Existing Curve"
    """
    CenterLine = 0  # JointmarkGuideBuilderLocationMemberType
    OffsetFromEdge = 1  # JointmarkGuideBuilderLocationMemberType
    ExistingCurve = 2  # JointmarkGuideBuilderLocationMemberType
    
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
    


class JointmarkGuideBuilderSpaceMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkGuideBuilderSpaceMethod():
    """
    Options for Spacing Method 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ArcLength", "Arc Length"
       "ParallelXPlane", "Parallel X Plane"
       "ParallelYPlane", "Parallel Y Plane"
       "ParallelZPlane", "Parallel Z Plane"
    """
    ArcLength = 0  # JointmarkGuideBuilderSpaceMethodMemberType
    ParallelXPlane = 1  # JointmarkGuideBuilderSpaceMethodMemberType
    ParallelYPlane = 2  # JointmarkGuideBuilderSpaceMethodMemberType
    ParallelZPlane = 3  # JointmarkGuideBuilderSpaceMethodMemberType
    
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
    


class JointmarkGuideBuilderSpaceOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JointmarkGuideBuilderSpaceOption():
    """
    Spacing Option 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Distance", "Space points by a fixed distance. Spacing at last point may not be uniform."
       "Number", "Uniformly space a number of points."
       "MinimumDistance", "Uniformly space points using a minimum distance value."
    """
    Distance = 0  # JointmarkGuideBuilderSpaceOptionMemberType
    Number = 1  # JointmarkGuideBuilderSpaceOptionMemberType
    MinimumDistance = 2  # JointmarkGuideBuilderSpaceOptionMemberType
    
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
    


class JointmarkGuideBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Used to create or edit a guide curve for Jointmark.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.JointmarkBuilder.NewGuide`
    
    .. versionadded:: NX9.0.0
    """
    
    class Location():
        """
        The type of guide curve 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CenterLine", "Centerline"
           "OffsetFromEdge", "Offset from Edge"
           "ExistingCurve", "Existing Curve"
        """
        CenterLine = 0  # JointmarkGuideBuilderLocationMemberType
        OffsetFromEdge = 1  # JointmarkGuideBuilderLocationMemberType
        ExistingCurve = 2  # JointmarkGuideBuilderLocationMemberType
        
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
        
    
    
    class SpaceMethod():
        """
        Options for Spacing Method 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ArcLength", "Arc Length"
           "ParallelXPlane", "Parallel X Plane"
           "ParallelYPlane", "Parallel Y Plane"
           "ParallelZPlane", "Parallel Z Plane"
        """
        ArcLength = 0  # JointmarkGuideBuilderSpaceMethodMemberType
        ParallelXPlane = 1  # JointmarkGuideBuilderSpaceMethodMemberType
        ParallelYPlane = 2  # JointmarkGuideBuilderSpaceMethodMemberType
        ParallelZPlane = 3  # JointmarkGuideBuilderSpaceMethodMemberType
        
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
        
    
    
    class SpaceOption():
        """
        Spacing Option 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Distance", "Space points by a fixed distance. Spacing at last point may not be uniform."
           "Number", "Uniformly space a number of points."
           "MinimumDistance", "Uniformly space points using a minimum distance value."
        """
        Distance = 0  # JointmarkGuideBuilderSpaceOptionMemberType
        Number = 1  # JointmarkGuideBuilderSpaceOptionMemberType
        MinimumDistance = 2  # JointmarkGuideBuilderSpaceOptionMemberType
        
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
        
    
    
    def CreateGuideCurves(self) -> None:
        """
        Creates the guide curves.  
        
        Signature ``CreateGuideCurves()`` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def GetGuideCurves(self) -> tuple:
        """
        Gets the created curves curves.  
        
        The guide curves need to exist before calling this, or nothing will be returned. 
        
        Signature ``GetGuideCurves()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (guideCurves, instanceGuideCurves). guideCurves is a list of :py:class:`NXOpen.ICurve`.  The array of curves.instanceGuideCurves is a list of :py:class:`NXOpen.NXObject`.  The array of component curve instances. If there is not an assembly, then this will match the prototype curve. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def RediscoverGuideEnds(self) -> None:
        """
        Use the specified reuse features to set the start and end distance for the guide curve.  
        
        Signature ``RediscoverGuideEnds()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: ugweld ("UG WELD")
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
    
    EndDistance: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the end distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtendOffset: bool = ...
    """
    Returns or sets  the extend offset.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendOffset`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendOffset`` 
    
    :param extendOffset: 
    :type extendOffset: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    GuideCurve: NXOpen.Section = ...
    """
    Returns or sets  the guide curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``GuideCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``GuideCurve`` 
    
    :param guide: 
    :type guide: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    LocationOption: JointmarkGuideBuilderLocation = ...
    """
    Returns or sets  the location option.  
    
    <hr>
    
    Getter Method
    
    Signature ``LocationOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilderLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``LocationOption`` 
    
    :param locationOption: 
    :type locationOption: :py:class:`NXOpen.Weld.JointmarkGuideBuilderLocation` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    NumberOfPoints: int = ...
    """
    Returns or sets  the number to determine the points along the guide curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfPoints`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfPoints`` 
    
    :param number: 
    :type number: int 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    OffsetDistance: NXOpen.Expression = ...
    """
    Returns  the offset distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the reversal status of Guide Curve direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverse: 
    :type reverse: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Section1: NXOpen.Section = ...
    """
    Returns  the first section used in Centerline.  
    
    <hr>
    
    Getter Method
    
    Signature ``Section1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Section2: NXOpen.Section = ...
    """
    Returns  the second section used in Centerline.  
    
    <hr>
    
    Getter Method
    
    Signature ``Section2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Section3: NXOpen.Section = ...
    """
    Returns  the third section used in Offset from Edge.  
    
    <hr>
    
    Getter Method
    
    Signature ``Section3`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Section4: NXOpen.Section = ...
    """
    Returns  the fourth section used in Existing Curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``Section4`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Spacing: NXOpen.Expression = ...
    """
    Returns  the spacing to determine the points along the guide curve.  
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingMethod: JointmarkGuideBuilderSpaceMethod = ...
    """
    Returns or sets  the spacing method.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilderSpaceMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingMethod`` 
    
    :param spacingMethod: 
    :type spacingMethod: :py:class:`NXOpen.Weld.JointmarkGuideBuilderSpaceMethod` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    SpacingOption: JointmarkGuideBuilderSpaceOption = ...
    """
    Returns or sets  the spacing option.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpacingOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.JointmarkGuideBuilderSpaceOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``SpacingOption`` 
    
    :param spacingOption: 
    :type spacingOption: :py:class:`NXOpen.Weld.JointmarkGuideBuilderSpaceOption` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    StartDistance: NXOpen.GeometricUtilities.OnPathDimensionBuilder = ...
    """
    Returns  the start distance.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OnPathDimensionBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: JointmarkGuideBuilder = ...  # unknown typename


class Fillet(NXOpen.Features.BodyFeature, IFeature):
    """
    Represents a Weld Fillet Feature.  
    
    This is the new Fillet Dialog introduced in 8.0 
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.FilletBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: Fillet = ...  # unknown typename


class WeldGrooveShapeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldGrooveShape():
    """
    Groove Weld Section type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SquareButt", "Square butt shape"
       "VGroove", "V groove shape"
       "Bevel", "Bevel shape"
       "UGroove", "U groove shape"
       "JGroove", "J groove shape"
       "FlaredV", "Flared V shape"
       "FlaredBevel", "Flared bevel shape"
       "FillinFlaredV", "Fillin Flared V shape"
       "FillinFlaredBevel", "Fillin Flared Bevel shape"
    """
    SquareButt = 0  # WeldGrooveShapeMemberType
    VGroove = 1  # WeldGrooveShapeMemberType
    Bevel = 2  # WeldGrooveShapeMemberType
    UGroove = 3  # WeldGrooveShapeMemberType
    JGroove = 4  # WeldGrooveShapeMemberType
    FlaredV = 5  # WeldGrooveShapeMemberType
    FlaredBevel = 6  # WeldGrooveShapeMemberType
    FillinFlaredV = 7  # WeldGrooveShapeMemberType
    FillinFlaredBevel = 8  # WeldGrooveShapeMemberType
    
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
    


class WeldPointLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldPointLocation():
    """
    Settings locating spot welds using guide curves/edges 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AlongGuideCurve", "Place spot welds along guide curves"
       "AlongGuideEdge", "Place spot welds by offsetting from an edge(s)."
       "AlongCenterLine", "To sections are needed for this method."
       "SectionPlane", "Place spot welds along a section curve"
    """
    AlongGuideCurve = 0  # WeldPointLocationMemberType
    AlongGuideEdge = 1  # WeldPointLocationMemberType
    AlongCenterLine = 2  # WeldPointLocationMemberType
    SectionPlane = 3  # WeldPointLocationMemberType
    
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
    


class WeldPoint(NXOpen.Features.Feature):
    """
    Represents a WeldPoint feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.WeldPointBuilder`
    
    .. versionadded:: NX6.0.0
    """
    Null: WeldPoint = ...  # unknown typename


class WeldFillBuilderBoundaryMethodTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldFillBuilderBoundaryMethodType():
    """
    Defines whether the initial boundary of the fill pattern is defined
    by a two point rectangle or a curve. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Rectangle", "Boundary defined by a two point rectangle."
       "Curve", "Boundary defined by a curve."
    """
    Rectangle = 0  # WeldFillBuilderBoundaryMethodTypeMemberType
    Curve = 1  # WeldFillBuilderBoundaryMethodTypeMemberType
    
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
    


class WeldFillBuilderWidthAlongTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldFillBuilderWidthAlongType():
    """
    Defines the direction the fill strip's length is aligned 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xc", "The length is aligned along the current WCS X direction."
       "Yc", "The length is aligned along the current WCS Y direction."
    """
    Xc = 0  # WeldFillBuilderWidthAlongTypeMemberType
    Yc = 1  # WeldFillBuilderWidthAlongTypeMemberType
    
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
    


class WeldFillBuilder(NXOpen.Builder):
    """
    A builder used to create or edit a :py:class:`NXOpen.Weld.Fill` feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateFillBuilder`
    
    Default values.
    
    ======================  =============================================
    Property                Value
    ======================  =============================================
    BoundaryMethod          Rectangle 
    ----------------------  ---------------------------------------------
    ChangeViewOrientation   0 
    ----------------------  ---------------------------------------------
    ExtendDistance          -15.0 (millimeters part), -0.5 (inches part) 
    ----------------------  ---------------------------------------------
    ExtrudeHeight           1 
    ----------------------  ---------------------------------------------
    SubdivideRegion         0 
    ----------------------  ---------------------------------------------
    Width                   5 
    ----------------------  ---------------------------------------------
    WidthAlong              Xc 
    ======================  =============================================
    
    .. versionadded:: NX7.5.0
    """
    
    class BoundaryMethodType():
        """
        Defines whether the initial boundary of the fill pattern is defined
        by a two point rectangle or a curve. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Rectangle", "Boundary defined by a two point rectangle."
           "Curve", "Boundary defined by a curve."
        """
        Rectangle = 0  # WeldFillBuilderBoundaryMethodTypeMemberType
        Curve = 1  # WeldFillBuilderBoundaryMethodTypeMemberType
        
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
        
    
    
    class WidthAlongType():
        """
        Defines the direction the fill strip's length is aligned 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xc", "The length is aligned along the current WCS X direction."
           "Yc", "The length is aligned along the current WCS Y direction."
        """
        Xc = 0  # WeldFillBuilderWidthAlongTypeMemberType
        Yc = 1  # WeldFillBuilderWidthAlongTypeMemberType
        
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
        
    
    
    def NewFillStrip(self, center: NXOpen.Point3d, length: float) -> WeldFillStripBuilder:
        """
        Create a new fill strip.  
        
        Signature ``NewFillStrip(center, length)`` 
        
        :param center:  Center of the fill strip  
        :type center: :py:class:`NXOpen.Point3d` 
        :param length:  Length of the fill strip  
        :type length: float 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    
    def DeleteFillStrip(self, fillStrip: WeldFillStripBuilder) -> None:
        """
        Delete a fill strip.  
        
        Signature ``DeleteFillStrip(fillStrip)`` 
        
        :param fillStrip:  Fill strip to delete.  
        :type fillStrip: :py:class:`NXOpen.Weld.WeldFillStripBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: ugweld ("UG WELD")
        """
        ...
    
    Boundary: NXOpen.Section = ...
    """
    Returns  the section defining the boundary if the 
    :py:class:`NXOpen.Weld.WeldFillBuilderBoundaryMethodType.Curve <NXOpen.Weld.WeldFillBuilderBoundaryMethodType>` 
    option is specified for the boundary type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Boundary`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    BoundaryMethod: WeldFillBuilderBoundaryMethodType = ...
    """
    Returns or sets  the type of boundary to create the fill from.  
    
    <hr>
    
    Getter Method
    
    Signature ``BoundaryMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFillBuilderBoundaryMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BoundaryMethod`` 
    
    :param boundaryMethod: 
    :type boundaryMethod: :py:class:`NXOpen.Weld.WeldFillBuilderBoundaryMethodType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ChangeViewOrientation: bool = ...
    """
    Returns or sets  the indication if the view orientation should be changed automatically (true)
    upon initial creation of rectangles, or not (false) 
    
    <hr>
    
    Getter Method
    
    Signature ``ChangeViewOrientation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ChangeViewOrientation`` 
    
    :param changeViewOrientation: 
    :type changeViewOrientation: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Characteristics: CharacteristicsBuilder = ...
    """
    Returns  the characteristics information.  
    
    <hr>
    
    Getter Method
    
    Signature ``Characteristics`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Corner1: NXOpen.Point = ...
    """
    Returns or sets  the first corner of the boundary if the 
    :py:class:`NXOpen.Weld.WeldFillBuilderBoundaryMethodType.Rectangle <NXOpen.Weld.WeldFillBuilderBoundaryMethodType>` 
    option is specified for the boundary type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Corner1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Corner1`` 
    
    :param corner1: 
    :type corner1: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Corner2: NXOpen.Point = ...
    """
    Returns or sets  the second corner of the boundary if the 
    :py:class:`NXOpen.Weld.WeldFillBuilderBoundaryMethodType.Rectangle <NXOpen.Weld.WeldFillBuilderBoundaryMethodType>` 
    option is specified for the boundary type.  
    
    <hr>
    
    Getter Method
    
    Signature ``Corner2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Corner2`` 
    
    :param corner2: 
    :type corner2: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    DistanceTolerance: float = ...
    """
    Returns or sets  the distance tolerance used in processing to determine if two points are coincident.  
    
    <hr>
    
    Getter Method
    
    Signature ``DistanceTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DistanceTolerance`` 
    
    :param distanceTolerance: 
    :type distanceTolerance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtendDistance: float = ...
    """
    Returns or sets  the distance to extend a strip.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendDistance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendDistance`` 
    
    :param distance: 
    :type distance: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    ExtrudeHeight: float = ...
    """
    Returns or sets  the height of the extrusions representing the fill.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtrudeHeight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtrudeHeight`` 
    
    :param extrudeHeight: 
    :type extrudeHeight: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    FillStripList: WeldFillStripBuilderList = ...
    """
    Returns  the fill strip list.  
    
    <hr>
    
    Getter Method
    
    Signature ``FillStripList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFillStripBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    InnerBoundary: NXOpen.Section = ...
    """
    Returns  the section containing edges of interior openings which indicate that these openings should be filled over.  
    
    <hr>
    
    Getter Method
    
    Signature ``InnerBoundary`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Orientation: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system that defines the alignment of the strips and rectangle.  
    
    <hr>
    
    Getter Method
    
    Signature ``Orientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Orientation`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    PlacementFace: NXOpen.ScCollector = ...
    """
    Returns  the collector containing the faces to build the fill on.  
    
    Note that during processing
    additional faces will be obtained by getting adjacent tangent faces (within 45 degrees) so that
    the boundary of the area is covered. At least one face inside of every boundary must be selected. 
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SubdivideRegion: bool = ...
    """
    Returns or sets  the indication if the fill is to be a collection of rectangles (true), or
    simply the enclosed boundary area (false).  
    
    <hr>
    
    Getter Method
    
    Signature ``SubdivideRegion`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SubdivideRegion`` 
    
    :param subdivideRegion: 
    :type subdivideRegion: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    UseSeedFace: bool = ...
    """
    Returns or sets  the indication if the selected faces should be used as seed faces.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseSeedFace`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseSeedFace`` 
    
    :param useSeedFace: 
    :type useSeedFace: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Width: float = ...
    """
    Returns or sets  the width of the rectangles.  
    
    Only used if SubdivideRegion is true. 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Width`` 
    
    :param width: 
    :type width: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    WidthAlong: WeldFillBuilderWidthAlongType = ...
    """
    Returns or sets  the width of the rectangles will be measured along this direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``WidthAlong`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.WeldFillBuilderWidthAlongType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthAlong`` 
    
    :param widthAlong: 
    :type widthAlong: :py:class:`NXOpen.Weld.WeldFillBuilderWidthAlongType` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: ugweld ("UG WELD")
    """
    Null: WeldFillBuilder = ...  # unknown typename


class PointMark(NXOpen.Features.Feature, IFeature):
    """
    Represents a Weld PointMark Feature.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.PointMarkBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetFeatureDiagnostics(self) -> 'list[int]':
        """
        Returns the feature diagnostic information, warning, or error codes.  
        
        Signature ``GetFeatureDiagnostics()`` 
        
        :returns:  the information, warning, or error codes for this feature.  
        :rtype: list of int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureIconName(self) -> str:
        """
        Gets the feature icon name.  
        
        Signature ``GetFeatureIconName()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureLayer(self) -> int:
        """
        Gets the feature layer.  
        
        Signature ``GetFeatureLayer()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureObjectColor(self) -> int:
        """
        Gets the feature color.  
        
        Signature ``GetFeatureObjectColor()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSets(self) -> 'list[NXOpen.ReferenceSet]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSets()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ReferenceSet` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFeatureReferenceSetStrings(self) -> 'list[str]':
        """
        Gets all the reference sets that this feature is a member of.  
        
        Signature ``GetFeatureReferenceSetStrings()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: PointMark = ...  # unknown typename


class WeldContourShapeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class WeldContourShape():
    """
    Top contour shape 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No shape"
       "Convex", "Convex shape"
       "Flush", "Flush shape"
       "Concave", "Concave shape"
    """
    NotSet = 0  # WeldContourShapeMemberType
    Convex = 1  # WeldContourShapeMemberType
    Flush = 2  # WeldContourShapeMemberType
    Concave = 3  # WeldContourShapeMemberType
    
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
    


class CharacteristicsBuilderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CharacteristicsBuilderType():
    """
    The custom type of the datum specified for creation. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "FilletFeature", " - "
       "GrooveFeature", " - "
       "ResistanceSpotFeature", " - "
       "ArcSpotFeature", " - "
       "ClinchFeature", " - "
       "DollopFeature", " - "
       "WeldNutFeature", " - "
       "WeldStudFeature", " - "
       "Custom1PointFeature", " - "
       "Custom2PointFeature", " - "
       "Custom3PointFeature", " - "
       "Custom4PointFeature", " - "
       "Custom5PointFeature", " - "
       "DatumSurfaceFeature", " - "
       "DatumPinFeature", " - "
       "DatumCustom1Feature", " - "
       "DatumCustom2Feature", " - "
       "DatumCustom3Feature", " - "
       "MeasurementSurfaceFeature", " - "
       "MeasurementHoleFeature", " - "
       "MeasurementSlotFeature", " - "
       "MeasurementStudFeature", " - "
       "MeasurementTrimFeature", " - "
       "MeasurementHemFeature", " - "
       "MeasurementCustom1Feature", " - "
       "MeasurementCustom2Feature", " - "
       "MeasurementCustom3Feature", " - "
       "UserDefinedFeature", " - "
       "SealerFillFeature", " - "
       "SealerBeadFeature", " - "
       "JointFeature", " - "
       "PlugSlotFeature", " - "
       "ShipHull", " - "
       "ShipDeck", " - "
       "ShipTransverseBulkhead", " - "
       "ShipLongitudinalBulkhead", " - "
       "ShipGenericPlate", " - "
       "ShipStiffener", " - "
       "ShipEdgeReinforcement", " - "
       "ShipSeam", " - "
       "DatumSurfaceCustom0", " - "
       "DatumSurfaceCustom1", " - "
       "DatumSurfaceCustom2", " - "
       "DatumSurfaceCustom3", " - "
       "DatumSurfaceCustom4", " - "
       "DatumSurfaceCustom5", " - "
       "DatumSurfaceCustom6", " - "
       "DatumSurfaceCustom7", " - "
       "DatumPinCustom0", " - "
       "DatumPinCustom1", " - "
       "DatumPinCustom2", " - "
       "DatumPinCustom3", " - "
       "DatumPinCustom4", " - "
       "DatumPinCustom5", " - "
       "DatumPinCustom6", " - "
       "DatumPinCustom7", " - "
       "SurfaceWeld", " - "
       "ShipProfileCutOut", " - "
       "JointmarkFeature", " - "
       "ShipStandardPart", " - "
       "PointMarkResistanceSpot", " - "
       "PointMarkArcSpot", " - "
       "PointMarkDollop", " - "
       "PointMarkClinch", " - "
       "PointMarkWeldNut", " - "
       "PointMarkWeldStud", " - "
       "PointMarkCustom1", " - "
       "PointMarkCustom2", " - "
       "PointMarkCustom3", " - "
       "PointMarkCustom4", " - "
       "PointMarkCustom5", " - "
       "ShipBracket", " - "
       "ShipCollarPlate", " - "
    """
    NotSet = 0  # CharacteristicsBuilderTypeMemberType
    FilletFeature = 24  # CharacteristicsBuilderTypeMemberType
    GrooveFeature = 25  # CharacteristicsBuilderTypeMemberType
    ResistanceSpotFeature = 26  # CharacteristicsBuilderTypeMemberType
    ArcSpotFeature = 27  # CharacteristicsBuilderTypeMemberType
    ClinchFeature = 28  # CharacteristicsBuilderTypeMemberType
    DollopFeature = 29  # CharacteristicsBuilderTypeMemberType
    WeldNutFeature = 30  # CharacteristicsBuilderTypeMemberType
    WeldStudFeature = 31  # CharacteristicsBuilderTypeMemberType
    Custom1PointFeature = 32  # CharacteristicsBuilderTypeMemberType
    Custom2PointFeature = 33  # CharacteristicsBuilderTypeMemberType
    Custom3PointFeature = 34  # CharacteristicsBuilderTypeMemberType
    Custom4PointFeature = 35  # CharacteristicsBuilderTypeMemberType
    Custom5PointFeature = 36  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceFeature = 37  # CharacteristicsBuilderTypeMemberType
    DatumPinFeature = 38  # CharacteristicsBuilderTypeMemberType
    DatumCustom1Feature = 39  # CharacteristicsBuilderTypeMemberType
    DatumCustom2Feature = 40  # CharacteristicsBuilderTypeMemberType
    DatumCustom3Feature = 41  # CharacteristicsBuilderTypeMemberType
    MeasurementSurfaceFeature = 42  # CharacteristicsBuilderTypeMemberType
    MeasurementHoleFeature = 43  # CharacteristicsBuilderTypeMemberType
    MeasurementSlotFeature = 44  # CharacteristicsBuilderTypeMemberType
    MeasurementStudFeature = 45  # CharacteristicsBuilderTypeMemberType
    MeasurementTrimFeature = 46  # CharacteristicsBuilderTypeMemberType
    MeasurementHemFeature = 47  # CharacteristicsBuilderTypeMemberType
    MeasurementCustom1Feature = 48  # CharacteristicsBuilderTypeMemberType
    MeasurementCustom2Feature = 49  # CharacteristicsBuilderTypeMemberType
    MeasurementCustom3Feature = 50  # CharacteristicsBuilderTypeMemberType
    UserDefinedFeature = 51  # CharacteristicsBuilderTypeMemberType
    SealerFillFeature = 52  # CharacteristicsBuilderTypeMemberType
    SealerBeadFeature = 53  # CharacteristicsBuilderTypeMemberType
    JointFeature = 54  # CharacteristicsBuilderTypeMemberType
    PlugSlotFeature = 55  # CharacteristicsBuilderTypeMemberType
    ShipHull = 57  # CharacteristicsBuilderTypeMemberType
    ShipDeck = 58  # CharacteristicsBuilderTypeMemberType
    ShipTransverseBulkhead = 59  # CharacteristicsBuilderTypeMemberType
    ShipLongitudinalBulkhead = 60  # CharacteristicsBuilderTypeMemberType
    ShipGenericPlate = 61  # CharacteristicsBuilderTypeMemberType
    ShipStiffener = 62  # CharacteristicsBuilderTypeMemberType
    ShipEdgeReinforcement = 63  # CharacteristicsBuilderTypeMemberType
    ShipSeam = 64  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom0 = 65  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom1 = 66  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom2 = 67  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom3 = 68  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom4 = 69  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom5 = 70  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom6 = 71  # CharacteristicsBuilderTypeMemberType
    DatumSurfaceCustom7 = 72  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom0 = 73  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom1 = 74  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom2 = 75  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom3 = 76  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom4 = 77  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom5 = 78  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom6 = 79  # CharacteristicsBuilderTypeMemberType
    DatumPinCustom7 = 80  # CharacteristicsBuilderTypeMemberType
    SurfaceWeld = 81  # CharacteristicsBuilderTypeMemberType
    ShipProfileCutOut = 82  # CharacteristicsBuilderTypeMemberType
    JointmarkFeature = 83  # CharacteristicsBuilderTypeMemberType
    ShipStandardPart = 84  # CharacteristicsBuilderTypeMemberType
    PointMarkResistanceSpot = 85  # CharacteristicsBuilderTypeMemberType
    PointMarkArcSpot = 86  # CharacteristicsBuilderTypeMemberType
    PointMarkDollop = 87  # CharacteristicsBuilderTypeMemberType
    PointMarkClinch = 88  # CharacteristicsBuilderTypeMemberType
    PointMarkWeldNut = 89  # CharacteristicsBuilderTypeMemberType
    PointMarkWeldStud = 90  # CharacteristicsBuilderTypeMemberType
    PointMarkCustom1 = 91  # CharacteristicsBuilderTypeMemberType
    PointMarkCustom2 = 92  # CharacteristicsBuilderTypeMemberType
    PointMarkCustom3 = 93  # CharacteristicsBuilderTypeMemberType
    PointMarkCustom4 = 94  # CharacteristicsBuilderTypeMemberType
    PointMarkCustom5 = 95  # CharacteristicsBuilderTypeMemberType
    ShipBracket = 96  # CharacteristicsBuilderTypeMemberType
    ShipCollarPlate = 97  # CharacteristicsBuilderTypeMemberType
    
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
    


class CharacteristicsBuilder(NXOpen.Builder):
    """
    This builder allows you to define the attribute values to be set on the
    output of the weld feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateCharacteristicsBuilder`
    
    .. versionadded:: NX7.5.0
    """
    
    class Type():
        """
        The custom type of the datum specified for creation. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "FilletFeature", " - "
           "GrooveFeature", " - "
           "ResistanceSpotFeature", " - "
           "ArcSpotFeature", " - "
           "ClinchFeature", " - "
           "DollopFeature", " - "
           "WeldNutFeature", " - "
           "WeldStudFeature", " - "
           "Custom1PointFeature", " - "
           "Custom2PointFeature", " - "
           "Custom3PointFeature", " - "
           "Custom4PointFeature", " - "
           "Custom5PointFeature", " - "
           "DatumSurfaceFeature", " - "
           "DatumPinFeature", " - "
           "DatumCustom1Feature", " - "
           "DatumCustom2Feature", " - "
           "DatumCustom3Feature", " - "
           "MeasurementSurfaceFeature", " - "
           "MeasurementHoleFeature", " - "
           "MeasurementSlotFeature", " - "
           "MeasurementStudFeature", " - "
           "MeasurementTrimFeature", " - "
           "MeasurementHemFeature", " - "
           "MeasurementCustom1Feature", " - "
           "MeasurementCustom2Feature", " - "
           "MeasurementCustom3Feature", " - "
           "UserDefinedFeature", " - "
           "SealerFillFeature", " - "
           "SealerBeadFeature", " - "
           "JointFeature", " - "
           "PlugSlotFeature", " - "
           "ShipHull", " - "
           "ShipDeck", " - "
           "ShipTransverseBulkhead", " - "
           "ShipLongitudinalBulkhead", " - "
           "ShipGenericPlate", " - "
           "ShipStiffener", " - "
           "ShipEdgeReinforcement", " - "
           "ShipSeam", " - "
           "DatumSurfaceCustom0", " - "
           "DatumSurfaceCustom1", " - "
           "DatumSurfaceCustom2", " - "
           "DatumSurfaceCustom3", " - "
           "DatumSurfaceCustom4", " - "
           "DatumSurfaceCustom5", " - "
           "DatumSurfaceCustom6", " - "
           "DatumSurfaceCustom7", " - "
           "DatumPinCustom0", " - "
           "DatumPinCustom1", " - "
           "DatumPinCustom2", " - "
           "DatumPinCustom3", " - "
           "DatumPinCustom4", " - "
           "DatumPinCustom5", " - "
           "DatumPinCustom6", " - "
           "DatumPinCustom7", " - "
           "SurfaceWeld", " - "
           "ShipProfileCutOut", " - "
           "JointmarkFeature", " - "
           "ShipStandardPart", " - "
           "PointMarkResistanceSpot", " - "
           "PointMarkArcSpot", " - "
           "PointMarkDollop", " - "
           "PointMarkClinch", " - "
           "PointMarkWeldNut", " - "
           "PointMarkWeldStud", " - "
           "PointMarkCustom1", " - "
           "PointMarkCustom2", " - "
           "PointMarkCustom3", " - "
           "PointMarkCustom4", " - "
           "PointMarkCustom5", " - "
           "ShipBracket", " - "
           "ShipCollarPlate", " - "
        """
        NotSet = 0  # CharacteristicsBuilderTypeMemberType
        FilletFeature = 24  # CharacteristicsBuilderTypeMemberType
        GrooveFeature = 25  # CharacteristicsBuilderTypeMemberType
        ResistanceSpotFeature = 26  # CharacteristicsBuilderTypeMemberType
        ArcSpotFeature = 27  # CharacteristicsBuilderTypeMemberType
        ClinchFeature = 28  # CharacteristicsBuilderTypeMemberType
        DollopFeature = 29  # CharacteristicsBuilderTypeMemberType
        WeldNutFeature = 30  # CharacteristicsBuilderTypeMemberType
        WeldStudFeature = 31  # CharacteristicsBuilderTypeMemberType
        Custom1PointFeature = 32  # CharacteristicsBuilderTypeMemberType
        Custom2PointFeature = 33  # CharacteristicsBuilderTypeMemberType
        Custom3PointFeature = 34  # CharacteristicsBuilderTypeMemberType
        Custom4PointFeature = 35  # CharacteristicsBuilderTypeMemberType
        Custom5PointFeature = 36  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceFeature = 37  # CharacteristicsBuilderTypeMemberType
        DatumPinFeature = 38  # CharacteristicsBuilderTypeMemberType
        DatumCustom1Feature = 39  # CharacteristicsBuilderTypeMemberType
        DatumCustom2Feature = 40  # CharacteristicsBuilderTypeMemberType
        DatumCustom3Feature = 41  # CharacteristicsBuilderTypeMemberType
        MeasurementSurfaceFeature = 42  # CharacteristicsBuilderTypeMemberType
        MeasurementHoleFeature = 43  # CharacteristicsBuilderTypeMemberType
        MeasurementSlotFeature = 44  # CharacteristicsBuilderTypeMemberType
        MeasurementStudFeature = 45  # CharacteristicsBuilderTypeMemberType
        MeasurementTrimFeature = 46  # CharacteristicsBuilderTypeMemberType
        MeasurementHemFeature = 47  # CharacteristicsBuilderTypeMemberType
        MeasurementCustom1Feature = 48  # CharacteristicsBuilderTypeMemberType
        MeasurementCustom2Feature = 49  # CharacteristicsBuilderTypeMemberType
        MeasurementCustom3Feature = 50  # CharacteristicsBuilderTypeMemberType
        UserDefinedFeature = 51  # CharacteristicsBuilderTypeMemberType
        SealerFillFeature = 52  # CharacteristicsBuilderTypeMemberType
        SealerBeadFeature = 53  # CharacteristicsBuilderTypeMemberType
        JointFeature = 54  # CharacteristicsBuilderTypeMemberType
        PlugSlotFeature = 55  # CharacteristicsBuilderTypeMemberType
        ShipHull = 57  # CharacteristicsBuilderTypeMemberType
        ShipDeck = 58  # CharacteristicsBuilderTypeMemberType
        ShipTransverseBulkhead = 59  # CharacteristicsBuilderTypeMemberType
        ShipLongitudinalBulkhead = 60  # CharacteristicsBuilderTypeMemberType
        ShipGenericPlate = 61  # CharacteristicsBuilderTypeMemberType
        ShipStiffener = 62  # CharacteristicsBuilderTypeMemberType
        ShipEdgeReinforcement = 63  # CharacteristicsBuilderTypeMemberType
        ShipSeam = 64  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom0 = 65  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom1 = 66  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom2 = 67  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom3 = 68  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom4 = 69  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom5 = 70  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom6 = 71  # CharacteristicsBuilderTypeMemberType
        DatumSurfaceCustom7 = 72  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom0 = 73  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom1 = 74  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom2 = 75  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom3 = 76  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom4 = 77  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom5 = 78  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom6 = 79  # CharacteristicsBuilderTypeMemberType
        DatumPinCustom7 = 80  # CharacteristicsBuilderTypeMemberType
        SurfaceWeld = 81  # CharacteristicsBuilderTypeMemberType
        ShipProfileCutOut = 82  # CharacteristicsBuilderTypeMemberType
        JointmarkFeature = 83  # CharacteristicsBuilderTypeMemberType
        ShipStandardPart = 84  # CharacteristicsBuilderTypeMemberType
        PointMarkResistanceSpot = 85  # CharacteristicsBuilderTypeMemberType
        PointMarkArcSpot = 86  # CharacteristicsBuilderTypeMemberType
        PointMarkDollop = 87  # CharacteristicsBuilderTypeMemberType
        PointMarkClinch = 88  # CharacteristicsBuilderTypeMemberType
        PointMarkWeldNut = 89  # CharacteristicsBuilderTypeMemberType
        PointMarkWeldStud = 90  # CharacteristicsBuilderTypeMemberType
        PointMarkCustom1 = 91  # CharacteristicsBuilderTypeMemberType
        PointMarkCustom2 = 92  # CharacteristicsBuilderTypeMemberType
        PointMarkCustom3 = 93  # CharacteristicsBuilderTypeMemberType
        PointMarkCustom4 = 94  # CharacteristicsBuilderTypeMemberType
        PointMarkCustom5 = 95  # CharacteristicsBuilderTypeMemberType
        ShipBracket = 96  # CharacteristicsBuilderTypeMemberType
        ShipCollarPlate = 97  # CharacteristicsBuilderTypeMemberType
        
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
        
    
    
    @typing.overload
    def CreateSelectionSet(self, weldType: int, data: NXOpen.NXObject) -> CharacteristicsSelectionBuilder:
        """
        Create a new selection set and add it to the list.  
        
        Signature ``CreateSelectionSet(weldType, data)`` 
        
        :param weldType:  The type of welding feature being processed, see uf_weld_types.h.  
        :type weldType: int 
        :param data:  An object to retrieve the current attribute settings.  
        :type data: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsSelectionBuilder` 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.0
           Use overloaded function with enum instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def CreateSelectionSet(self, charxType: CharacteristicsBuilderType, data: NXOpen.NXObject) -> CharacteristicsSelectionBuilder:
        """
        Create a new selection set and add it to the list.  
        
        Signature ``CreateSelectionSet(charxType, data)`` 
        
        :param charxType:  The type of characteristics being processed  
        :type charxType: :py:class:`NXOpen.Weld.CharacteristicsBuilderType` 
        :param data:  An object to retrieve the current attribute settings.  
        :type data: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.Weld.CharacteristicsSelectionBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ApplyAttributes(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Apply the selected attributes to the objects.  
        
        Signature ``ApplyAttributes(objects)`` 
        
        :param objects:  The objects to apply the attributes to.  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveInheritedAttributes(self) -> None:
        """
        Remove any attributes that are inherited from other objects (for example, edges).  
        
        These will be attributes that are
        not required and are not in a category. 
        
        Signature ``RemoveInheritedAttributes()`` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllAttributes(self, objects: 'list[NXOpen.NXObject]') -> None:
        """
        Remove all attributes from the objects.  
        
        Signature ``RemoveAllAttributes(objects)`` 
        
        :param objects:  The objects to remove the attributes from.  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ApplyAttributesToSelected(self) -> None:
        """
        Apply the selected attributes to the objects that were selected.  
        
        Signature ``ApplyAttributesToSelected()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def InheritAttributesFromObject(self, object: NXOpen.NXObject) -> None:
        """
        Inherit the attributes that are on the object to the selection.  
        
        Signature ``InheritAttributesFromObject(object)`` 
        
        :param object:  The object from which to inherit the attributes.  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyAttributesFromObject(self, object: NXOpen.NXObject) -> None:
        """
        Copy the attributes that are on the object to the selection.  
        
        Signature ``CopyAttributesFromObject(object)`` 
        
        :param object:  The object from which to copy the attributes.  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyNonActiveAttributesFromObject(self, object: NXOpen.NXObject) -> None:
        """
        Copy the non active attributes that are on the object to the selection.  
        
        Signature ``CopyNonActiveAttributesFromObject(object)`` 
        
        :param object:  The object from which to copy the attributes.  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DoesObjectHaveAttributes(self, object: NXOpen.NXObject) -> bool:
        """
        Copy the attributes that are on the object to the selection and returns a flag indicating whether the object actually has attributes.  
        
        Signature ``DoesObjectHaveAttributes(object)`` 
        
        :param object:  The object from which to copy the attributes.  
        :type object: :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def HasActiveValues(self) -> bool:
        """
        Returns true if the characteristics builder has any active values.  
        
        Signature ``HasActiveValues()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def AreAttributesDefault(self, weldType: int) -> bool:
        """
        Returns true if the characteristics builder contains all attributes with default values.  
        
        Signature ``AreAttributesDefault(weldType)`` 
        
        :param weldType:  The type of welding feature being processed, see uf_weld_types.h.  
        :type weldType: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Use overloaded function with enum instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def AreAttributesDefault(self, charxType: CharacteristicsBuilderType) -> bool:
        """
        Returns true if the characteristics builder contains all attributes with default values.  
        
        Signature ``AreAttributesDefault(charxType)`` 
        
        :param charxType:  The type of characteristics being processed  
        :type charxType: :py:class:`NXOpen.Weld.CharacteristicsBuilderType` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def ChangeFeatureType(self, weldType: int) -> None:
        """
        Change the type of feature defining the attributes. 
        Note after calling this method, the WeldJA::CharacteristicsValueBuilder objects 
        previously retrieved will be invalid. You need to reaccess them if you want to
        make any changes to them. 
        
        Signature ``ChangeFeatureType(weldType)`` 
        
        :param weldType:  The type of welding feature being processed, see uf_weld_types.h.  
        :type weldType: int 
        
        .. versionadded:: NX7.5.0
        
        .. deprecated::  NX9.0.0
           Use overloaded function with enum instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def ChangeFeatureType(self, charxType: CharacteristicsBuilderType) -> None:
        """
        Change the type of feature defining the attributes. 
        Note after calling this method, the WeldJA::CharacteristicsValueBuilder objects 
        previously retrieved will be invalid. You need to reaccess them if you want to
        make any changes to them. 
        
        Signature ``ChangeFeatureType(charxType)`` 
        
        :param charxType:  The type of characteristics being processed  
        :type charxType: :py:class:`NXOpen.Weld.CharacteristicsBuilderType` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetAllAttributesChanged(self) -> None:
        """
        Sets all attributes to be changed. 
        
        Signature ``SetAllAttributesChanged()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAllAttributesChanged(self, status: bool) -> None:
        """
        Sets all attributes changed value to the status value. 
        
        Signature ``SetAllAttributesChanged(status)`` 
        
        :param status:  The value to set changed value. true means attribute has been changed, false means attribute has not been changed  
        :type status: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CopyAttributesFromObjectForPaint(self, objectTag: NXOpen.NXObject) -> None:
        """
        Copies the attributes that are on the object to the selection for paint.  
        
        Signature ``CopyAttributesFromObjectForPaint(objectTag)`` 
        
        :param objectTag:  The object from which to copy the attributes.  
        :type objectTag: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    InheritObject: NXOpen.SelectNXObject = ...
    """
    Returns  the selection object containing data that is used to define the attribute values.  
    
    <hr>
    
    Getter Method
    
    Signature ``InheritObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObject` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Selected: CharacteristicsValueBuilder = ...
    """
    Returns or sets  the selected characteristic value.  
    
    <hr>
    
    Getter Method
    
    Signature ``Selected`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Selected`` 
    
    :param valueBuilder: 
    :type valueBuilder: :py:class:`NXOpen.Weld.CharacteristicsValueBuilder` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectionList: NXOpen.NXObjectList = ...
    """
    Returns  the list of potential attributes and objects selected for this weld feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: CharacteristicsBuilder = ...  # unknown typename


class InformationBuilderAttributeOriginTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InformationBuilderAttributeOriginType():
    """
    the Object Type enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Object", " - "
       "Df", " - "
    """
    Object = 0  # InformationBuilderAttributeOriginTypeMemberType
    Df = 1  # InformationBuilderAttributeOriginTypeMemberType
    
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
    


class InformationBuilder(NXOpen.Builder):
    """
    This class is used by "Fabrication Information" to output fabrication objects information.  
    
    When commit is called, attributes and total weld length and volume of selected objects 
    will be output into a list window. No objects are returned when Commit is called.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Weld.WeldManager.CreateInformationBuilder`
    
    Default values.
    
    ======================  =======
    Property                Value
    ======================  =======
    AttributeOrigin         Object 
    ----------------------  -------
    OutputAttributes        1 
    ----------------------  -------
    OutputLengthAndVolume   0 
    ======================  =======
    
    .. versionadded:: NX9.0.0
    """
    
    class AttributeOriginType():
        """
        the Object Type enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Object", " - "
           "Df", " - "
        """
        Object = 0  # InformationBuilderAttributeOriginTypeMemberType
        Df = 1  # InformationBuilderAttributeOriginTypeMemberType
        
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
        
    
    
    def GetTotalLength(self) -> float:
        """
        Get the total length of the selection weld objects.  
        
        This function may be time intensive and should be used after all weld data has been defined.  
        
        Signature ``GetTotalLength()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    
    def GetTotalVolume(self) -> float:
        """
        Get the total volume of the selection weld objects.  
        
        This function may be time intensive and should be used after all weld data has been defined.  
        
        Signature ``GetTotalVolume()`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
        """
        ...
    
    AttributeOrigin: InformationBuilderAttributeOriginType = ...
    """
    Returns or sets  the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``AttributeOrigin`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Weld.InformationBuilderAttributeOriginType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``AttributeOrigin`` 
    
    :param attributeOrigin: 
    :type attributeOrigin: :py:class:`NXOpen.Weld.InformationBuilderAttributeOriginType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    ConnectedToInformation: bool = ...
    """
    Returns or sets  the option to specify if the connected to information should be displayed in the output.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedToInformation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectedToInformation`` 
    
    :param connectedToInformation: 
    :type connectedToInformation: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    FabricationObjects: NXOpen.SelectNXObjectList = ...
    """
    Returns  the list of weld fabrication objects to create the output.  
    
    <hr>
    
    Getter Method
    
    Signature ``FabricationObjects`` 
    
    :returns:  Selected weld objects list  
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    OutputAttributes: bool = ...
    """
    Returns or sets  the option to specify if the weld attributes should be included in the output.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputAttributes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputAttributes`` 
    
    :param outputAttributes: 
    :type outputAttributes: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    OutputLengthAndVolume: bool = ...
    """
    Returns or sets  the option to specify if the weld length and volume should be calculated for the output.  
    
    <hr>
    
    Getter Method
    
    Signature ``OutputLengthAndVolume`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    
    <hr>
    
    Setter Method
    
    Signature ``OutputLengthAndVolume`` 
    
    :param outputLengthAndVolume: 
    :type outputLengthAndVolume: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD")
    """
    Null: InformationBuilder = ...  # unknown typename


class WeldGroove(NXOpen.Features.BodyFeature):
    """
    Represents a Weld Groove Feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Weld.WeldGrooveBuilder`
    
    .. versionadded:: NX9.0.0
    """
    Null: WeldGroove = ...  # unknown typename


