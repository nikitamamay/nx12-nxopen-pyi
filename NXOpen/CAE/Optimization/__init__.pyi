# module 'NXOpen.CAE.Optimization'
#
# Automatically generated 2025-06-09T14:38:44.558629
#

import typing

import NXOpen
import NXOpen.CAE



class TBSSmoothBuilderFormatMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderFormat():
    """
    Defines the output file format of surface representation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Bdf", "Represents surfaces in .bdf file"
       "Stl", "Represents surfaces in .stl file"
       "Iges", "Represents surfaces in .igs file"
    """
    Bdf = 0  # TBSSmoothBuilderFormatMemberType
    Stl = 1  # TBSSmoothBuilderFormatMemberType
    Iges = 2  # TBSSmoothBuilderFormatMemberType
    
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
    


class TBSSmoothBuilderResultFilteringMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderResultFiltering():
    """
    Defines if the element material values are to be filtered before the isocut
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "Don't filter the element material values"
       "Moderate", "Filters the element material values partially"
       "Full", "Filters the element material values fully"
    """
    Off = 0  # TBSSmoothBuilderResultFilteringMemberType
    Moderate = 1  # TBSSmoothBuilderResultFilteringMemberType
    Full = 2  # TBSSmoothBuilderResultFilteringMemberType
    
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
    


class TBSSmoothBuilderIsoTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderIsoType():
    """
    Specifies the content saved to the output files 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Original", "Saves the original surface"
       "New", "Saves the surface gererated by Isocut"
       "Both", "Saves the complete surface"
    """
    Original = 0  # TBSSmoothBuilderIsoTypeMemberType
    New = 1  # TBSSmoothBuilderIsoTypeMemberType
    Both = 2  # TBSSmoothBuilderIsoTypeMemberType
    
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
    


class TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderOriginalSurfaceSmoothingOption():
    """
    Defines if the original surface is to be smoothed or remain unchanged 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "No changes to the original surface"
       "Shrink", "Allows the nodes on original surface to be moved towards the inside only"
       "Full", "Allows any modifications to the original surface"
    """
    Off = 0  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
    Shrink = 1  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
    Full = 2  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
    
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
    


class TBSSmoothBuilderSliceFormatOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderSliceFormatOption():
    """
    Defines how to save slices 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "IgsPolygon", "Saves slices as polygons using cubic parametric splines for each segment"
       "IgsCurves", "Saves slices as curves obtained by interpolation using uniform cubic splines"
       "Cli", "Saves slices as polygons saved in common layer interface format"
       "All", "Save slices in all formats mentioned above"
    """
    IgsPolygon = 0  # TBSSmoothBuilderSliceFormatOptionMemberType
    IgsCurves = 1  # TBSSmoothBuilderSliceFormatOptionMemberType
    Cli = 2  # TBSSmoothBuilderSliceFormatOptionMemberType
    All = 3  # TBSSmoothBuilderSliceFormatOptionMemberType
    
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
    


class TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSSmoothBuilderSelfIntersectionCheckingOption():
    """
    Defines if the self-itersection checks are to be performed during the isocut, smoothing and data reduction
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "No checks"
       "Check", "Check once"
       "Runtime", "Check always"
       "Iterative", "First run without check, then rerun if self-intersections are found"
    """
    Off = 0  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
    Check = 1  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
    Runtime = 2  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
    Iterative = 3  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
    
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
    


class TBSSmoothBuilder(NXOpen.Builder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSSmooth`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateSmoothBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class Format():
        """
        Defines the output file format of surface representation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Bdf", "Represents surfaces in .bdf file"
           "Stl", "Represents surfaces in .stl file"
           "Iges", "Represents surfaces in .igs file"
        """
        Bdf = 0  # TBSSmoothBuilderFormatMemberType
        Stl = 1  # TBSSmoothBuilderFormatMemberType
        Iges = 2  # TBSSmoothBuilderFormatMemberType
        
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
        
    
    
    class ResultFiltering():
        """
        Defines if the element material values are to be filtered before the isocut
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "Don't filter the element material values"
           "Moderate", "Filters the element material values partially"
           "Full", "Filters the element material values fully"
        """
        Off = 0  # TBSSmoothBuilderResultFilteringMemberType
        Moderate = 1  # TBSSmoothBuilderResultFilteringMemberType
        Full = 2  # TBSSmoothBuilderResultFilteringMemberType
        
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
        
    
    
    class IsoType():
        """
        Specifies the content saved to the output files 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Original", "Saves the original surface"
           "New", "Saves the surface gererated by Isocut"
           "Both", "Saves the complete surface"
        """
        Original = 0  # TBSSmoothBuilderIsoTypeMemberType
        New = 1  # TBSSmoothBuilderIsoTypeMemberType
        Both = 2  # TBSSmoothBuilderIsoTypeMemberType
        
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
        
    
    
    class OriginalSurfaceSmoothingOption():
        """
        Defines if the original surface is to be smoothed or remain unchanged 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "No changes to the original surface"
           "Shrink", "Allows the nodes on original surface to be moved towards the inside only"
           "Full", "Allows any modifications to the original surface"
        """
        Off = 0  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
        Shrink = 1  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
        Full = 2  # TBSSmoothBuilderOriginalSurfaceSmoothingOptionMemberType
        
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
        
    
    
    class SliceFormatOption():
        """
        Defines how to save slices 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "IgsPolygon", "Saves slices as polygons using cubic parametric splines for each segment"
           "IgsCurves", "Saves slices as curves obtained by interpolation using uniform cubic splines"
           "Cli", "Saves slices as polygons saved in common layer interface format"
           "All", "Save slices in all formats mentioned above"
        """
        IgsPolygon = 0  # TBSSmoothBuilderSliceFormatOptionMemberType
        IgsCurves = 1  # TBSSmoothBuilderSliceFormatOptionMemberType
        Cli = 2  # TBSSmoothBuilderSliceFormatOptionMemberType
        All = 3  # TBSSmoothBuilderSliceFormatOptionMemberType
        
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
        
    
    
    class SelfIntersectionCheckingOption():
        """
        Defines if the self-itersection checks are to be performed during the isocut, smoothing and data reduction
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "No checks"
           "Check", "Check once"
           "Runtime", "Check always"
           "Iterative", "First run without check, then rerun if self-intersections are found"
        """
        Off = 0  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
        Check = 1  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
        Runtime = 2  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
        Iterative = 3  # TBSSmoothBuilderSelfIntersectionCheckingOptionMemberType
        
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
        
    
    
    def GetFormatOption(self) -> 'list[TBSSmoothBuilderFormat]':
        """
        The output result format accessor  
        
        Signature ``GetFormatOption()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderFormat` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFormatOption(self, formatOption: 'list[TBSSmoothBuilderFormat]') -> None:
        """
        The output result format mutator 
        
        Signature ``SetFormatOption(formatOption)`` 
        
        :param formatOption: 
        :type formatOption: list of :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderFormat` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    Border: bool = ...
    """
    Returns or sets  the option to save border.  
    
    If yes, the border of the shell element model will saved 
    
    <hr>
    
    Getter Method
    
    Signature ``Border`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Border`` 
    
    :param border: 
    :type border: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ComponentLimitingSize: NXOpen.Expression = ...
    """
    Returns  the limiting size that defines the minimal allowed relative size of a connected component.  
    
    All components with the relative size below this value are removed 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentLimitingSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    IsoTypeOption: TBSSmoothBuilderIsoType = ...
    """
    Returns or sets  the option that specifies what should be saved to the output files 
    
    <hr>
    
    Getter Method
    
    Signature ``IsoTypeOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderIsoType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsoTypeOption`` 
    
    :param isoTypeOption: 
    :type isoTypeOption: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderIsoType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    IsoValue: float = ...
    """
    Returns or sets  the iso value that is used to determine the positions on the element edges where the new nodes are created.  
    
    Larger value lead to models with smaller volume. Value is between 0 and 1 
    
    <hr>
    
    Getter Method
    
    Signature ``IsoValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsoValue`` 
    
    :param isoValue: 
    :type isoValue: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    MinimumAngle: NXOpen.Expression = ...
    """
    Returns  the minimum angle that defines the minimal angle of the triangles that result from the smoothing
    and data reduction.  
    
    Too large value may prevent the smoothing, and too small value may lead to degenerated triangles 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MixedMesh: bool = ...
    """
    Returns or sets  the choice whether to form quardrilaterals from adjacent triangles 
    
    <hr>
    
    Getter Method
    
    Signature ``MixedMesh`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MixedMesh`` 
    
    :param mixedMesh: 
    :type mixedMesh: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    NameDescription: NameDescription = ...
    """
    Returns  the name description 
    
    <hr>
    
    Getter Method
    
    Signature ``NameDescription`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.NameDescription` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    OriginalSurfaceSmooth: TBSSmoothBuilderOriginalSurfaceSmoothingOption = ...
    """
    Returns or sets  the option of how to smooth the original surface 
    
    <hr>
    
    Getter Method
    
    Signature ``OriginalSurfaceSmooth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderOriginalSurfaceSmoothingOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OriginalSurfaceSmooth`` 
    
    :param originalSurfaceSmooth: 
    :type originalSurfaceSmooth: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderOriginalSurfaceSmoothingOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ReductionAngle: NXOpen.Expression = ...
    """
    Returns  the reduction angle that defines the maximal angle between adjacent faces at a node such
    that the node may be removed during the data reduction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReductionAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReductionRate: float = ...
    """
    Returns or sets  the reduction rate that defines the percent of faces that should be removed during the data reduction.  
    
    if set to 0, no data reduction occurs. If set to 100, the data reduction sopts when no faces could be removed 
    
    <hr>
    
    Getter Method
    
    Signature ``ReductionRate`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReductionRate`` 
    
    :param reductionRate: 
    :type reductionRate: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ResultFilteringOption: TBSSmoothBuilderResultFiltering = ...
    """
    Returns or sets  the result filtering option 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultFilteringOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderResultFiltering` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResultFilteringOption`` 
    
    :param resultFilteringOption: 
    :type resultFilteringOption: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderResultFiltering` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SelfIntersectionChecking: TBSSmoothBuilderSelfIntersectionCheckingOption = ...
    """
    Returns or sets  the option of self-intersection checking 
    
    <hr>
    
    Getter Method
    
    Signature ``SelfIntersectionChecking`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderSelfIntersectionCheckingOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelfIntersectionChecking`` 
    
    :param selfIntersectionChecking: 
    :type selfIntersectionChecking: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderSelfIntersectionCheckingOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SliceFormat: TBSSmoothBuilderSliceFormatOption = ...
    """
    Returns or sets  the slice format 
    
    <hr>
    
    Getter Method
    
    Signature ``SliceFormat`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderSliceFormatOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SliceFormat`` 
    
    :param sliceFormat: 
    :type sliceFormat: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilderSliceFormatOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SliceNormalVector: NXOpen.Direction = ...
    """
    Returns or sets  the slice normal vector 
    
    <hr>
    
    Getter Method
    
    Signature ``SliceNormalVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SliceNormalVector`` 
    
    :param sliceNormalVector: 
    :type sliceNormalVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SliceNumber: int = ...
    """
    Returns or sets  the slice number 
    
    <hr>
    
    Getter Method
    
    Signature ``SliceNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SliceNumber`` 
    
    :param sliceNumber: 
    :type sliceNumber: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SmoothArea: TBSGroupDefinition = ...
    """
    Returns  the area to be smoothed 
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothArea`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    SmoothCycles: int = ...
    """
    Returns or sets  the number of smoothing cycles.  
    
    If set to 0, no smoothing is performed. Larger value
    leads to smoother models, but may cause the narrowing of thin components 
    
    <hr>
    
    Getter Method
    
    Signature ``SmoothCycles`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SmoothCycles`` 
    
    :param smoothCycles: 
    :type smoothCycles: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TargetVolume: float = ...
    """
    Returns or sets  the target volume that is to be achieved iteratively by varying the isovalue.  
    
    If set to 0,
    the given :py:meth:`NXOpen.CAE.Optimization.TBSSmoothBuilder.IsoValue`` is usedfor the generation of the isosurface 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetVolume`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetVolume`` 
    
    :param targetVolume: 
    :type targetVolume: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    UseAdditionalParameters: bool = ...
    """
    Returns or sets  the option to use additional parameter.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseAdditionalParameters`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseAdditionalParameters`` 
    
    :param useAdditionalParameters: 
    :type useAdditionalParameters: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSSmoothBuilder = ...  # unknown typename


class TBSSmoothCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.CAE.Optimization.TBSSmooth`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, smoothName: str) -> TBSSmooth:
        """
        Finds a smooth object with specified name within an optimization solution  
        
        Signature ``FindObject(smoothName)`` 
        
        :param smoothName: 
        :type smoothName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmooth` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    


class TBSRestrictArea(NXOpen.NXObject):
    """
    Represents the restrictions for the design variable in an optimization   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSRestrictAreaBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSRestrictArea = ...  # unknown typename


class TBSMeshSmoothStrategyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSMeshSmoothStrategy():
    """
    Specify the strategy of mesh smooth 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ConstrainedLaplacian", "Constrained Laplacian Strategy"
       "LocalGradient", "Local Gradient Strategy"
    """
    ConstrainedLaplacian = 0  # TBSMeshSmoothStrategyMemberType
    LocalGradient = 1  # TBSMeshSmoothStrategyMemberType
    
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
    


class TBSMeshSmooth(NXOpen.NXObject):
    """
    Represents the mesh smooth   
    
    .. versionadded:: NX8.5.0
    """
    
    class Strategy():
        """
        Specify the strategy of mesh smooth 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ConstrainedLaplacian", "Constrained Laplacian Strategy"
           "LocalGradient", "Local Gradient Strategy"
        """
        ConstrainedLaplacian = 0  # TBSMeshSmoothStrategyMemberType
        LocalGradient = 1  # TBSMeshSmoothStrategyMemberType
        
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
        
    
    FixSurfaceNodes: bool = ...
    """
    Returns or sets  a value indicating whether to fix surface nodes outside design area 
    
    <hr>
    
    Getter Method
    
    Signature ``FixSurfaceNodes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FixSurfaceNodes`` 
    
    :param fixedSurfaceNodes: 
    :type fixedSurfaceNodes: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    MeshSmoothElements: TBSGroupDefinition = ...
    """
    Returns  the elements of mesh smooth 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSmoothElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MeshSmoothStrategy: TBSMeshSmoothStrategy = ...
    """
    Returns or sets  the strategy of mesh smooth 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSmoothStrategy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSMeshSmoothStrategy` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshSmoothStrategy`` 
    
    :param strategy: 
    :type strategy: :py:class:`NXOpen.CAE.Optimization.TBSMeshSmoothStrategy` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    UseHighestQuality: bool = ...
    """
    Returns or sets  a value indicating whether to use highest mesh quality 
    
    <hr>
    
    Getter Method
    
    Signature ``UseHighestQuality`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseHighestQuality`` 
    
    :param highestQuality: 
    :type highestQuality: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSMeshSmooth = ...  # unknown typename


class TBSSingleObjective(NXOpen.TaggedObject):
    """
    Represents a single objective   
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateSingleObjective`
    
    .. versionadded:: NX8.0.0
    """
    DesignResponse: TBSDesignResponse = ...
    """
    Returns or sets  the design response 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignResponse`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DesignResponse`` 
    
    :param designResponse: 
    :type designResponse: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ReferenceValue: float = ...
    """
    Returns or sets  the reference value 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceValue`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceValue`` 
    
    :param referenceValue: 
    :type referenceValue: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Weight: float = ...
    """
    Returns or sets  the weight of the design variable 
    
    <hr>
    
    Getter Method
    
    Signature ``Weight`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Weight`` 
    
    :param weight: 
    :type weight: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSSingleObjective = ...  # unknown typename


class TBSOptimizationSolutionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.TBSOptimizationManager`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, solutionName: str) -> TBSOptimizationSolution:
        """
        Finds an optimization solution with specified name  
        
        Signature ``FindObject(solutionName)`` 
        
        :param solutionName: 
        :type solutionName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CloneSolution(self, sourceSolution: TBSOptimizationSolution, cloneResult: bool) -> TBSOptimizationSolution:
        """
        Clones an optimization solution and the associated result file optional  
        
        Signature ``CloneSolution(sourceSolution, cloneResult)`` 
        
        :param sourceSolution: 
        :type sourceSolution: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution` 
        :param cloneResult:   true if you want associated result files to be cloned as well  
        :type cloneResult: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    


class TBSOptimizationSolutionBuilderStrategyTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSOptimizationSolutionBuilderStrategyType():
    """
    Defines the optimization strategy
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Sensitivity", "Uses sensitivity strategy to run optimization"
       "Controller", "uses controller strategy to run optimization"
    """
    Sensitivity = 0  # TBSOptimizationSolutionBuilderStrategyTypeMemberType
    Controller = 1  # TBSOptimizationSolutionBuilderStrategyTypeMemberType
    
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
    


class TBSOptimizationSolutionBuilder(NXOpen.Builder):
    """
    Represents the abstract builder of :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`.  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX8.0.0
    """
    
    class StrategyType():
        """
        Defines the optimization strategy
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Sensitivity", "Uses sensitivity strategy to run optimization"
           "Controller", "uses controller strategy to run optimization"
        """
        Sensitivity = 0  # TBSOptimizationSolutionBuilderStrategyTypeMemberType
        Controller = 1  # TBSOptimizationSolutionBuilderStrategyTypeMemberType
        
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
        
    
    NameDescription: NameDescription = ...
    """
    Returns  the name description 
    
    <hr>
    
    Getter Method
    
    Signature ``NameDescription`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.NameDescription` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReferencedSolution: NXOpen.CAE.SimSolution = ...
    """
    Returns or sets  the referenced solution 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencedSolution`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencedSolution`` 
    
    :param referencedSolution: 
    :type referencedSolution: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Strategy: TBSOptimizationSolutionBuilderStrategyType = ...
    """
    Returns or sets  the optimization strategy 
    
    <hr>
    
    Getter Method
    
    Signature ``Strategy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolutionBuilderStrategyType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Strategy`` 
    
    :param strategy: 
    :type strategy: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolutionBuilderStrategyType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSOptimizationSolutionBuilder = ...  # unknown typename


class TBSShapeOptimizationSolutionBuilder(TBSOptimizationSolutionBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationSolution`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateShapeOptimizationSolutionBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: TBSShapeOptimizationSolutionBuilder = ...  # unknown typename


class TBSObjectivesObjectiveTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSObjectivesObjectiveType():
    """
    Defines the target type of the design objective 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Minimum", "Target is to minimize the list of design response"
       "Maximum", "Target is to maximize the list of design response"
       "MaxMin", "Target is the MINMAX formulation of the list of design responses"
    """
    Minimum = 0  # TBSObjectivesObjectiveTypeMemberType
    Maximum = 1  # TBSObjectivesObjectiveTypeMemberType
    MaxMin = 2  # TBSObjectivesObjectiveTypeMemberType
    
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
    


class TBSObjectives(NXOpen.TaggedObject):
    """
    Represents the objective functions of an optimization   
    
    .. versionadded:: NX8.0.0
    """
    
    class ObjectiveType():
        """
        Defines the target type of the design objective 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Minimum", "Target is to minimize the list of design response"
           "Maximum", "Target is to maximize the list of design response"
           "MaxMin", "Target is the MINMAX formulation of the list of design responses"
        """
        Minimum = 0  # TBSObjectivesObjectiveTypeMemberType
        Maximum = 1  # TBSObjectivesObjectiveTypeMemberType
        MaxMin = 2  # TBSObjectivesObjectiveTypeMemberType
        
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
        
    
    
    def GetObjectives(self) -> 'list[TBSSingleObjective]':
        """
        Returns the design response  
        
        Signature ``GetObjectives()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetObjectives(self, objectives: 'list[TBSSingleObjective]') -> None:
        """
        Sets the design response 
        
        Signature ``SetObjectives(objectives)`` 
        
        :param objectives: 
        :type objectives: list of :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def AddObjectives(self, objectives: 'list[TBSSingleObjective]') -> None:
        """
        Add objectives 
        
        Signature ``AddObjectives(objectives)`` 
        
        :param objectives: 
        :type objectives: list of :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def RemoveObjectives(self, objectives: 'list[TBSSingleObjective]', deleteObject: bool) -> None:
        """
        Remove objectives 
        
        Signature ``RemoveObjectives(objectives, deleteObject)`` 
        
        :param objectives: 
        :type objectives: list of :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective` 
        :param deleteObject: 
        :type deleteObject: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    TargetObjective: TBSObjectivesObjectiveType = ...
    """
    Returns or sets  the target objective type 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetObjective`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSObjectivesObjectiveType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetObjective`` 
    
    :param target: 
    :type target: :py:class:`NXOpen.CAE.Optimization.TBSObjectivesObjectiveType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSObjectives = ...  # unknown typename


class TBSOptimizationParameters(NXOpen.TaggedObject):
    """
    Represents the parameters to control an optimization   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSOptimizationParameters = ...  # unknown typename


class TBSShapeOptimizationParametersDisplacementStepsizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSShapeOptimizationParametersDisplacementStepsize():
    """
    the step size option for incrementing the displacement during the optimization operation  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Minimum", "Minimum displacement stepsize"
       "Average", "Average displacement stepsize"
    """
    Minimum = 0  # TBSShapeOptimizationParametersDisplacementStepsizeMemberType
    Average = 1  # TBSShapeOptimizationParametersDisplacementStepsizeMemberType
    
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
    


class TBSShapeOptimizationParameters(TBSOptimizationParameters):
    """
    Represents the control parameters of shape optimization   
    
    .. versionadded:: NX8.5.0
    """
    
    class DisplacementStepsize():
        """
        the step size option for incrementing the displacement during the optimization operation  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Minimum", "Minimum displacement stepsize"
           "Average", "Average displacement stepsize"
        """
        Minimum = 0  # TBSShapeOptimizationParametersDisplacementStepsizeMemberType
        Average = 1  # TBSShapeOptimizationParametersDisplacementStepsizeMemberType
        
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
        
    
    DisplacementStepSize: TBSShapeOptimizationParametersDisplacementStepsize = ...
    """
    Returns or sets  the step size option for modifying the displacement during the optimization operation 
    
    <hr>
    
    Getter Method
    
    Signature ``DisplacementStepSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationParametersDisplacementStepsize` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DisplacementStepSize`` 
    
    :param stepSizeOption: 
    :type stepSizeOption: :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationParametersDisplacementStepsize` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Scale: float = ...
    """
    Returns or sets  the scale factor 
    
    <hr>
    
    Getter Method
    
    Signature ``Scale`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Scale`` 
    
    :param scale: 
    :type scale: float 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSShapeOptimizationParameters = ...  # unknown typename


class TBSConstraint(NXOpen.NXObject):
    """
    Represents the design constraint, which is defined with :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable`   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSConstraint = ...  # unknown typename


class DAODesignVariable(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAODesignVariable`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetResults(self) -> 'list[float]':
        """
        Gets the design variable results  
        
        Signature ``GetResults()`` 
        
        :returns:  Design variable optimization results  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    Null: DAODesignVariable = ...  # unknown typename


class TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologySensitivityOptimizationParametersDensityUpdate():
    """
    the method defines how the densities are updated in the method of moving asymptotes 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Normal", "Normal strategy"
       "Conservative", "Conservative strategy"
       "Agressive", "Agressive strategy"
    """
    Normal = 0  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
    Conservative = 1  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
    Agressive = 2  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
    
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
    


class TBSTopologySensitivityOptimizationParametersMaterialInterpolationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologySensitivityOptimizationParametersMaterialInterpolation():
    """
    the relationshp between relative density and relative element stiffness 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Simp", "Solid Isotropic material with penalization"
       "Ramp", "Rational approximation of material properties"
    """
    Simp = 0  # TBSTopologySensitivityOptimizationParametersMaterialInterpolationMemberType
    Ramp = 1  # TBSTopologySensitivityOptimizationParametersMaterialInterpolationMemberType
    
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
    


class TBSTopologySensitivityOptimizationParameters(TBSOptimizationParameters):
    """
    Represents the parameters to control an optimization in sensitivity strategy   
    
    .. versionadded:: NX8.0.0
    """
    
    class DensityUpdate():
        """
        the method defines how the densities are updated in the method of moving asymptotes 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Normal", "Normal strategy"
           "Conservative", "Conservative strategy"
           "Agressive", "Agressive strategy"
        """
        Normal = 0  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
        Conservative = 1  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
        Agressive = 2  # TBSTopologySensitivityOptimizationParametersDensityUpdateMemberType
        
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
        
    
    
    class MaterialInterpolation():
        """
        the relationshp between relative density and relative element stiffness 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Simp", "Solid Isotropic material with penalization"
           "Ramp", "Rational approximation of material properties"
        """
        Simp = 0  # TBSTopologySensitivityOptimizationParametersMaterialInterpolationMemberType
        Ramp = 1  # TBSTopologySensitivityOptimizationParametersMaterialInterpolationMemberType
        
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
        
    
    DensityMove: float = ...
    """
    Returns or sets  the move limit on design variables 
    
    <hr>
    
    Getter Method
    
    Signature ``DensityMove`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DensityMove`` 
    
    :param densityMove: 
    :type densityMove: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    DensityUpdateOption: TBSTopologySensitivityOptimizationParametersDensityUpdate = ...
    """
    Returns or sets  the parameter for how the densities are updated 
    
    <hr>
    
    Getter Method
    
    Signature ``DensityUpdateOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologySensitivityOptimizationParametersDensityUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DensityUpdateOption`` 
    
    :param densityUpdateOption: 
    :type densityUpdateOption: :py:class:`NXOpen.CAE.Optimization.TBSTopologySensitivityOptimizationParametersDensityUpdate` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    EigenvalueParameters: TBSEigenvalueOptimizationParameters = ...
    """
    Returns  the eigenvalue optimization control parameters 
    
    <hr>
    
    Getter Method
    
    Signature ``EigenvalueParameters`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSEigenvalueOptimizationParameters` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    FilterRadius: NXOpen.Expression = ...
    """
    Returns  the filter for mesh independence and minimum size 
    
    <hr>
    
    Getter Method
    
    Signature ``FilterRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MaterialInterpolationOption: TBSTopologySensitivityOptimizationParametersMaterialInterpolation = ...
    """
    Returns or sets  the material interpolation scheme 
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialInterpolationOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologySensitivityOptimizationParametersMaterialInterpolation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialInterpolationOption`` 
    
    :param materialInterpolationOption: 
    :type materialInterpolationOption: :py:class:`NXOpen.CAE.Optimization.TBSTopologySensitivityOptimizationParametersMaterialInterpolation` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSTopologySensitivityOptimizationParameters = ...  # unknown typename


class TBSRestrictAreaBuilder(NXOpen.Builder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSRestrictArea`  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX8.0.0
    """
    NameDescription: NameDescription = ...
    """
    Returns  the name description 
    
    <hr>
    
    Getter Method
    
    Signature ``NameDescription`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.NameDescription` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSRestrictAreaBuilder = ...  # unknown typename


class TBSShapeRestrictAreaBuilder(TBSRestrictAreaBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSShapeRestrictArea`  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateShapeRestrictAreaBuilder`
    
    .. versionadded:: NX8.5.0
    """
    ActLinkConditionButton: TBSShapeLinkCondition = ...
    """
    Returns  the link condition 
    
    <hr>
    
    Getter Method
    
    Signature ``ActLinkConditionButton`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSShapeLinkCondition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    CheckBoundaryCondition: bool = ...
    """
    Returns or sets  a value indicating whether to accept nodes of boundary condition as constraint 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckBoundaryCondition`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckBoundaryCondition`` 
    
    :param boundaryCondition: 
    :type boundaryCondition: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckDof: bool = ...
    """
    Returns or sets  a value indicating whether to restrict the dispacement in the coordinate direction of the referenced coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckDof`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckDof`` 
    
    :param checkDof: 
    :type checkDof: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckElementGroup: bool = ...
    """
    Returns or sets  a value indicating whether to check elements for penetration  
    
    <hr>
    
    Getter Method
    
    Signature ``CheckElementGroup`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckElementGroup`` 
    
    :param checkElements: 
    :type checkElements: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckLinkCondition: bool = ...
    """
    Returns or sets  a value indicating whether to check link condition 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckLinkCondition`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckLinkCondition`` 
    
    :param checkLinkCondition: 
    :type checkLinkCondition: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckMaximumGrowValue: bool = ...
    """
    Returns or sets  a value indicating whether to check maximum grow value 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckMaximumGrowValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckMaximumGrowValue`` 
    
    :param isMaxGrowValue: 
    :type isMaxGrowValue: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckMaximumShrinkValue: bool = ...
    """
    Returns or sets  a value indicating whether to check maximum shrink value 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckMaximumShrinkValue`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckMaximumShrinkValue`` 
    
    :param isMaxShrinkValue: 
    :type isMaxShrinkValue: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    CheckedElements: TBSGroupDefinition = ...
    """
    Returns  the elements checked for penetration  
    
    <hr>
    
    Getter Method
    
    Signature ``CheckedElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DofSettings: TBSCheckDOF = ...
    """
    Returns  the DOF settings 
    
    <hr>
    
    Getter Method
    
    Signature ``DofSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSCheckDOF` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumGrowValue: NXOpen.Expression = ...
    """
    Returns  the maximum grow value 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumGrowValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    MaximumShrinkValue: NXOpen.Expression = ...
    """
    Returns  the maximum shrink value 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumShrinkValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    RestrictedNodes: TBSGroupDefinition = ...
    """
    Returns  the nodes to react on the restrictions 
    
    <hr>
    
    Getter Method
    
    Signature ``RestrictedNodes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: TBSShapeRestrictAreaBuilder = ...  # unknown typename


class DAOConstraint(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOConstraint`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.DAOConstraintBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetNumberResultGroup(self) -> int:
        """
        Gets the constraint result group number  
        
        Signature ``GetNumberResultGroup()`` 
        
        :returns:  Result group number  
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResults(self, resultGroupIndex: int) -> 'list[float]':
        """
        Gets the constraint results  
        
        Signature ``GetResults(resultGroupIndex)`` 
        
        :param resultGroupIndex:  Result group index  
        :type resultGroupIndex: int 
        :returns:  Constraint optimization results  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    Null: DAOConstraint = ...  # unknown typename


class TBSDesignVariable(NXOpen.NXObject):
    """
    Represents the design variable referenced by :py:class:`NXOpen.CAE.Optimization.TBSConstraint` and 
    :py:class:`NXOpen.CAE.Optimization.TBSObjectives`  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSDesignVariableBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSDesignVariable = ...  # unknown typename


class TBSOptimizationManager():
    """
    Represents the optimization manager to contain the optimization solutions and take charge of 
    creating optimization objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.SimSimulation`
    
    .. versionadded:: NX8.0.0
    """
    
    def CreateTopologyOptimizationSolutionBuilder(self, topoSolution: TBSTopologyOptimizationSolution) -> TBSTopologyOptimizationSolutionBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSTopologyOptimizationSolution`  
        
        Signature ``CreateTopologyOptimizationSolutionBuilder(topoSolution)`` 
        
        :param topoSolution: 
        :type topoSolution: :py:class:`NXOpen.CAE.Optimization.TBSTopologyOptimizationSolution` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyOptimizationSolutionBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization")
        """
        ...
    
    
    def CreateShapeOptimizationSolutionBuilder(self, shapeSolution: TBSShapeOptimizationSolution) -> TBSShapeOptimizationSolutionBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationSolution`  
        
        Signature ``CreateShapeOptimizationSolutionBuilder(shapeSolution)`` 
        
        :param shapeSolution: 
        :type shapeSolution: :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationSolution` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationSolutionBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateDesignVariableBuilder(self, designVariable: TBSDesignVariable) -> TBSDesignVariableBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable`  
        
        Signature ``CreateDesignVariableBuilder(designVariable)`` 
        
        :param designVariable: 
        :type designVariable: :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignVariableBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateDesignResponseBuilder(self, designResponse: TBSDesignResponse) -> TBSDesignResponseBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse`  
        
        Signature ``CreateDesignResponseBuilder(designResponse)`` 
        
        :param designResponse: 
        :type designResponse: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponseBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateResponseConstraintBuilder(self, responseConstraint: TBSConstraint) -> TBSConstraintBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSConstraint`  
        
        Signature ``CreateResponseConstraintBuilder(responseConstraint)`` 
        
        :param responseConstraint: 
        :type responseConstraint: :py:class:`NXOpen.CAE.Optimization.TBSConstraint` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateTopologyRestrictAreaBuilder(self, restrictArea: TBSTopologyRestrictArea) -> TBSTopologyRestrictAreaBuilder:
        """
        Create the builder of :py:class:`NXOpen.CAE.Optimization.TBSRestrictAreaBuilder`  
        
        Signature ``CreateTopologyRestrictAreaBuilder(restrictArea)`` 
        
        :param restrictArea: 
        :type restrictArea: :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictArea` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictAreaBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization")
        """
        ...
    
    
    def CreateShapeRestrictAreaBuilder(self, restrictArea: TBSShapeRestrictArea) -> TBSShapeRestrictAreaBuilder:
        """
        Create the builder of :py:class:`NXOpen.CAE.Optimization.TBSRestrictAreaBuilder`  
        
        Signature ``CreateShapeRestrictAreaBuilder(restrictArea)`` 
        
        :param restrictArea: 
        :type restrictArea: :py:class:`NXOpen.CAE.Optimization.TBSShapeRestrictArea` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSShapeRestrictAreaBuilder` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateSmoothBuilder(self, smooth: TBSSmooth) -> TBSSmoothBuilder:
        """
        Creates the builder of :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilder`  
        
        Signature ``CreateSmoothBuilder(smooth)`` 
        
        :param smooth: 
        :type smooth: :py:class:`NXOpen.CAE.Optimization.TBSSmooth` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateSingleObjective(self, designResponse: TBSDesignResponse, weight: float, referenceValue: float) -> TBSSingleObjective:
        """
        Creates an object of :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective`  
        
        Signature ``CreateSingleObjective(designResponse, weight, referenceValue)`` 
        
        :param designResponse: 
        :type designResponse: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
        :param weight: 
        :type weight: float 
        :param referenceValue: 
        :type referenceValue: float 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSingleObjective` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def CreateLoadCase(self) -> TBSLoadCase:
        """
        Create a :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` object  
        
        Signature ``CreateLoadCase()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    OptimizationSolutions: TBSOptimizationSolutionCollection = ...
    """
    Represents the optimization solution collection belonging to this simulation 
    
    Signature ``OptimizationSolutions`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolutionCollection`
    """


class TBSIOptimizationTest():
    """
    Represents an interface to perform optimization test   
    
    .. versionadded:: NX8.5.0
    """
    Null = ...  # unknown typename: InterfaceIdentifier


class TBSOutputControlOptionsOp2OptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSOutputControlOptionsOp2Option():
    """
    Defines the op2 output option 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Donot output op2 result"
       "FirstLast", "Output op2 results of first and last iteration"
       "All", "Output op2 results of all iterations"
    """
    NotSet = 0  # TBSOutputControlOptionsOp2OptionMemberType
    FirstLast = 1  # TBSOutputControlOptionsOp2OptionMemberType
    All = 2  # TBSOutputControlOptionsOp2OptionMemberType
    
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
    


class TBSOutputControlOptions(NXOpen.TaggedObject):
    """
    Represents the output result control options of the optimization   
    
    .. versionadded:: NX8.0.0
    """
    
    class Op2Option():
        """
        Defines the op2 output option 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Donot output op2 result"
           "FirstLast", "Output op2 results of first and last iteration"
           "All", "Output op2 results of all iterations"
        """
        NotSet = 0  # TBSOutputControlOptionsOp2OptionMemberType
        FirstLast = 1  # TBSOutputControlOptionsOp2OptionMemberType
        All = 2  # TBSOutputControlOptionsOp2OptionMemberType
        
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
        
    
    CustomScratchDirectory: str = ...
    """
    Returns or sets  the custom cratch directory for solving 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomScratchDirectory`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CustomScratchDirectory`` 
    
    :param customScrathDir: 
    :type customScrathDir: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    HasCustomScratchDirectory: bool = ...
    """
    Returns or sets  whether to use a custom cratch directory or not when solving 
    
    <hr>
    
    Getter Method
    
    Signature ``HasCustomScratchDirectory`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HasCustomScratchDirectory`` 
    
    :param hasCustomScrathDir: 
    :type hasCustomScrathDir: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    IsJobRunInForeground: bool = ...
    """
    Returns or sets  whether to run optimization job in foreground or not when solving 
    
    <hr>
    
    Getter Method
    
    Signature ``IsJobRunInForeground`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsJobRunInForeground`` 
    
    :param isJobRunInForeground: 
    :type isJobRunInForeground: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Op2OutputOption: TBSOutputControlOptionsOp2Option = ...
    """
    Returns or sets  the op2 output control option 
    
    <hr>
    
    Getter Method
    
    Signature ``Op2OutputOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOutputControlOptionsOp2Option` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Op2OutputOption`` 
    
    :param op2Option: 
    :type op2Option: :py:class:`NXOpen.CAE.Optimization.TBSOutputControlOptionsOp2Option` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSOutputControlOptions = ...  # unknown typename


class HookesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Hookes():
    """
    Represents the Hooke's location   
    
    .. deprecated::  NX10.0.0
       Use the ShellSection property on one of the following classes - :py:class:`NXOpen.CAE.ResultMeasureResultSectionOptions`, :py:class:`NXOpen.CAE.ResultMeasureResultDirectionSectionOptions`, or :py:class:`NXOpen.CAE.ResultMeasureResultAllOptions`
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Top", "Top"
       "Bottom", "Bottom"
       "Middle", "Middle"
       "Minimum", "Minimum"
       "Maximum", "Maximum"
    """
    Top = 0  # HookesMemberType
    Bottom = 1  # HookesMemberType
    Middle = 2  # HookesMemberType
    Minimum = 3  # HookesMemberType
    Maximum = 4  # HookesMemberType
    
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
    


class TBSTopologyLinkConditionSymmetryOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyLinkConditionSymmetryOption():
    """
    Defines the type of link condition 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PlaneSymmetry", "Plane symmetry referring to the plane which lies perpendicular to the given axis of the coordinate system"
       "CyclicSymmetry", "Cyclic symmetry definition"
    """
    PlaneSymmetry = 0  # TBSTopologyLinkConditionSymmetryOptionMemberType
    CyclicSymmetry = 1  # TBSTopologyLinkConditionSymmetryOptionMemberType
    
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
    


class TBSTopologyLinkConditionAxisTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyLinkConditionAxisType():
    """
    Represents the axis of the symmetry coordinate system
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "X", "Represents X axis"
       "Y", "Represents Y axis"
       "Z", "Represents Z axis"
    """
    X = 0  # TBSTopologyLinkConditionAxisTypeMemberType
    Y = 1  # TBSTopologyLinkConditionAxisTypeMemberType
    Z = 2  # TBSTopologyLinkConditionAxisTypeMemberType
    
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
    


class TBSTopologyLinkCondition(NXOpen.TaggedObject):
    """
    Represents the definition of symmetry and link conditions for topology optimization   
    
    .. versionadded:: NX8.0.0
    """
    
    class SymmetryOption():
        """
        Defines the type of link condition 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PlaneSymmetry", "Plane symmetry referring to the plane which lies perpendicular to the given axis of the coordinate system"
           "CyclicSymmetry", "Cyclic symmetry definition"
        """
        PlaneSymmetry = 0  # TBSTopologyLinkConditionSymmetryOptionMemberType
        CyclicSymmetry = 1  # TBSTopologyLinkConditionSymmetryOptionMemberType
        
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
        
    
    
    class AxisType():
        """
        Represents the axis of the symmetry coordinate system
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "X", "Represents X axis"
           "Y", "Represents Y axis"
           "Z", "Represents Z axis"
        """
        X = 0  # TBSTopologyLinkConditionAxisTypeMemberType
        Y = 1  # TBSTopologyLinkConditionAxisTypeMemberType
        Z = 2  # TBSTopologyLinkConditionAxisTypeMemberType
        
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
        
    
    Axis: TBSTopologyLinkConditionAxisType = ...
    """
    Returns or sets  the axis of symmetry coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``Axis`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyLinkConditionAxisType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Axis`` 
    
    :param axis: 
    :type axis: :py:class:`NXOpen.CAE.Optimization.TBSTopologyLinkConditionAxisType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    IgnoreFrozen: bool = ...
    """
    Returns or sets  the choice whether the frozen elements should be excluded from the link definitions 
    
    <hr>
    
    Getter Method
    
    Signature ``IgnoreFrozen`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IgnoreFrozen`` 
    
    :param ignoreFrozen: 
    :type ignoreFrozen: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ReferenceCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the referenced coordinate system used for the link condition 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :param refCsys: 
    :type refCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SymmetryType: TBSTopologyLinkConditionSymmetryOption = ...
    """
    Returns or sets  the symmetry link condition type 
    
    <hr>
    
    Getter Method
    
    Signature ``SymmetryType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyLinkConditionSymmetryOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SymmetryType`` 
    
    :param symmetryType: 
    :type symmetryType: :py:class:`NXOpen.CAE.Optimization.TBSTopologyLinkConditionSymmetryOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TranslationAmount: int = ...
    """
    Returns or sets  the translation amount for the segments, only available when :py:meth:`CAE.Optimization.TBSTopologyLinkCondition.SymmetryType` is 
    :py:class:`CAE.Optimization.TBSTopologyLinkConditionSymmetryOption.CyclicSymmetry <CAE.Optimization.TBSTopologyLinkConditionSymmetryOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``TranslationAmount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TranslationAmount`` 
    
    :param translationAmount: 
    :type translationAmount: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSTopologyLinkCondition = ...  # unknown typename


class TBSOptimizationSolutionResultStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSOptimizationSolutionResultStatus():
    """
    Define the status of optimization result 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Valid", "The result is valid"
       "OutOfDate", "The result is out-of-date"
       "Invalid", "The result is invalid"
    """
    Valid = 0  # TBSOptimizationSolutionResultStatusMemberType
    OutOfDate = 1  # TBSOptimizationSolutionResultStatusMemberType
    Invalid = 2  # TBSOptimizationSolutionResultStatusMemberType
    
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
    


class TBSOptimizationSolution(NXOpen.NXObject):
    """
    Represents the solution to contain optimization setting   
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX8.0.0
    """
    
    class ResultStatus():
        """
        Define the status of optimization result 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Valid", "The result is valid"
           "OutOfDate", "The result is out-of-date"
           "Invalid", "The result is invalid"
        """
        Valid = 0  # TBSOptimizationSolutionResultStatusMemberType
        OutOfDate = 1  # TBSOptimizationSolutionResultStatusMemberType
        Invalid = 2  # TBSOptimizationSolutionResultStatusMemberType
        
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
        
    
    
    def Solve(self) -> None:
        """
        Solves the optimization solution 
        
        Signature ``Solve()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def GetIterationNumber(self) -> int:
        """
        Returns the iteration number during the optimization  
        
        Signature ``GetIterationNumber()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPostResult(self, iterationID: int) -> tuple:
        """
        Returns the post result file name and status  
        
        Signature ``GetPostResult(iterationID)`` 
        
        :param iterationID: 
        :type iterationID: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, postResultName). status is a :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolutionResultStatus`. postResultName is a str. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetSmoothResult(self, smooth: TBSSmooth) -> tuple:
        """
        Returns the result file name and status for a specified smoothing setting  
        
        Signature ``GetSmoothResult(smooth)`` 
        
        :param smooth: 
        :type smooth: :py:class:`NXOpen.CAE.Optimization.TBSSmooth` 
        :returns: a tuple 
        :rtype: A tuple consisting of (status, smoothResultName). status is a :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolutionResultStatus`. smoothResultName is a str. 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX8.5.0
           Use :py:meth:`NXOpen.CAE.Optimization.TBSSmooth.GetResults` instead.
        
        License requirements: None.
        """
        ...
    
    
    def Find(self, journalIdentifier: str) -> NXOpen.TaggedObject:
        """
        Finds the :py:class:`NXOpen.TaggedObject` with the given identifier as recorded in a journal.  
        
        In general, this method should not be used in handwritten code and exists to support record 
        and playback of journals. An exception will be thrown if no object can be found with the given journal identifier.  
        
        Signature ``Find(journalIdentifier)`` 
        
        :param journalIdentifier:  Journal identifier of the object  
        :type journalIdentifier: str 
        :returns: 
        :rtype: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Rename(self, name: str, renameResults: bool) -> None:
        """
        Rename Solution and optionally rename associated results files 
        
        Signature ``Rename(name, renameResults)`` 
        
        :param name:  new solution name  
        :type name: str 
        :param renameResults:  true if you what associated results files to be renamed as well   
        :type renameResults: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Destroy(self, deleteResult: bool) -> None:
        """
        Deletes an optimization solution and the associated result file optional 
        
        Signature ``Destroy(deleteResult)`` 
        
        :param deleteResult:   true if you want associated result files to be deleted as well  
        :type deleteResult: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    ControlParameters: TBSOptimizationParameters = ...
    """
    Returns  the parameters to control optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``ControlParameters`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOptimizationParameters` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DesignArea: TBSDesignArea = ...
    """
    Returns  the design area that will be modified during optimization
    
    <hr>
    
    Getter Method
    
    Signature ``DesignArea`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignArea` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Objectives: TBSObjectives = ...
    """
    Returns  the objective function of the optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``Objectives`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSObjectives` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    OutputControlOptions: TBSOutputControlOptions = ...
    """
    Returns  the output control options of the optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputControlOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSOutputControlOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    StopCondition: TBSStopCondition = ...
    """
    Returns  the stop condition to end the optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``StopCondition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSStopCondition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    RestrictAreas: TBSRestrictAreaCollection = ...
    """
    Represents the restrict area collection belonging to this optimization solution 
    
    Signature ``RestrictAreas`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSRestrictAreaCollection`
    """
    Constraints: TBSConstraintCollection = ...
    """
    Represents the response constrain collection belonging to this optimization solution 
    
    Signature ``Constraints`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSConstraintCollection`
    """
    DesignVariables: TBSDesignVariableCollection = ...
    """
    Represents the design variable collection belonging to this optimization solution 
    
    Signature ``DesignVariables`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignVariableCollection`
    """
    Smoothings: TBSSmoothCollection = ...
    """
    Represents the smooth collection belonging to this optimization solution 
    
    Signature ``Smoothings`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSSmoothCollection`
    """
    Null: TBSOptimizationSolution = ...  # unknown typename


class DAOSolutionBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOSolutionBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.DAOSolutionCollection.CreateOptimizationBuilder`
    
    .. versionadded:: NX8.0.0
    """
    AnalysisSolution: NXOpen.CAE.SimSolution = ...
    """
    Returns or sets  the optimization solution analysis solution 
    
    <hr>
    
    Getter Method
    
    Signature ``AnalysisSolution`` 
    
    :returns:  Analysis solution of optimization solution  
    :rtype: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnalysisSolution`` 
    
    :param analysisSolution:  Analysis solution of optimization solution  
    :type analysisSolution: :py:class:`NXOpen.CAE.SimSolution` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Name: str = ...
    """
    Returns or sets  the optimization solution name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  Optimization solution name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param solutionName:  Optimization solution name  
    :type solutionName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SolverType: Solver = ...
    """
    Returns or sets  the optimization solution solver type 
    
    <hr>
    
    Getter Method
    
    Signature ``SolverType`` 
    
    :returns:  Optimization solution solver type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Solver` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverType`` 
    
    :param solverType:  Optimization solution solver type  
    :type solverType: :py:class:`NXOpen.CAE.Optimization.Solver` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: DAOSolutionBuilder = ...  # unknown typename


class TBSShapeRestrictArea(TBSRestrictArea):
    """
    Represents the restrictions of the design variable in Shape optimization   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSShapeRestrictAreaBuilder`
    
    .. versionadded:: NX8.5.0
    """
    Null: TBSShapeRestrictArea = ...  # unknown typename


class DAOOptimizationManager():
    """
    Represents the Design and Analysis optimization manager that contains all optimization objects.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.SimSimulation`
    
    .. versionadded:: NX8.0.0
    """
    OptimizationSolution: DAOSolutionCollection = ...
    """
    Returns the optimization solution collection belonging to this sim part.  
    
    Signature ``OptimizationSolution`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.DAOSolutionCollection`
    """


class TBSDesignArea(NXOpen.NXObject):
    """
    Represents the design area   
    
    .. versionadded:: NX8.0.0
    """
    DesignElements: TBSGroupDefinition = ...
    """
    Returns  the design elements for optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSDesignArea = ...  # unknown typename


class TBSCheckDOFCheckDofOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSCheckDOFCheckDofOption():
    """
    Represents the status of displacement restriction 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fix", "Displacement is constrainted"
       "Free", "Displacement is allowed"
    """
    Fix = 0  # TBSCheckDOFCheckDofOptionMemberType
    Free = 1  # TBSCheckDOFCheckDofOptionMemberType
    
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
    


class TBSCheckDOFDofSettings_Struct():
    """
    the displacement restriction settings on three axial directions of referenced coordinate system  .  
    
    Constructor: 
    NXOpen.CAE.Optimization.TBSCheckDOF.DofSettings()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    Dof1: TBSCheckDOFCheckDofOption = ...
    """
    Represents displacement in the X axial direction 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
    """
    Dof2: TBSCheckDOFCheckDofOption = ...
    """
    Represents displacement in the Y axial direction 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
    """
    Dof3: TBSCheckDOFCheckDofOption = ...
    """
    Represents displacement in the Z axial direction 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
    """


class TBSCheckDOF(NXOpen.NXObject):
    """
    Represents the restriction of dispacement in the coordinate direction of the referenced coordinate system     
    
    .. versionadded:: NX8.5.0
    """
    
    class CheckDofOption():
        """
        Represents the status of displacement restriction 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fix", "Displacement is constrainted"
           "Free", "Displacement is allowed"
        """
        Fix = 0  # TBSCheckDOFCheckDofOptionMemberType
        Free = 1  # TBSCheckDOFCheckDofOptionMemberType
        
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
        
    
    
    class DofSettings():
        """
        the displacement restriction settings on three axial directions of referenced coordinate system  .  
        
        Constructor: 
        NXOpen.CAE.Optimization.TBSCheckDOF.DofSettings()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        Dof1: TBSCheckDOFCheckDofOption = ...
        """
        Represents displacement in the X axial direction 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
        """
        Dof2: TBSCheckDOFCheckDofOption = ...
        """
        Represents displacement in the Y axial direction 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
        """
        Dof3: TBSCheckDOFCheckDofOption = ...
        """
        Represents displacement in the Z axial direction 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.CAE.Optimization.TBSCheckDOFCheckDofOption`
        """
    
    Dofs: TBSCheckDOFDofSettings_Struct = ...
    """
    Returns or sets  the displacement restriction settings on referenced coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``Dofs`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSCheckDOFDofSettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Dofs`` 
    
    :param dofs: 
    :type dofs: :py:class:`NXOpen.CAE.Optimization.TBSCheckDOFDofSettings_Struct` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    ReferencedCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the referenced coordinate system for displacement restriction  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferencedCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferencedCoordinateSystem`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSCheckDOF = ...  # unknown typename


class TBSRestrictAreaCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.CAE.Optimization.TBSRestrictArea`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, name: str) -> TBSRestrictArea:
        """
        Finds a restrict area with the specified name within an optimization solution  
        
        Signature ``FindObject(name)`` 
        
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSRestrictArea` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    


class TBSBaseDesignVariableBuilderGroupOperatorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSBaseDesignVariableBuilderGroupOperator():
    """
    Defines the operator type to determine the design variable that used within the selection area 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Max", "Maximum value fo the selection area"
       "Min", "Minimum value of the selection area"
       "Sum", "Sum of all values of the selection area"
       "Count", "Determines the number of values of the selection area"
       "Deviation", "Deviation from the maximum value of the reference value"
    """
    Max = 0  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
    Min = 1  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
    Sum = 2  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
    Count = 3  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
    Deviation = 4  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
    
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
    


class TBSBaseDesignVariableBuilder(NXOpen.Builder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable`  
    
    This is an abstract class, and cannot be created.
    
    .. versionadded:: NX8.0.0
    """
    
    class GroupOperator():
        """
        Defines the operator type to determine the design variable that used within the selection area 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Max", "Maximum value fo the selection area"
           "Min", "Minimum value of the selection area"
           "Sum", "Sum of all values of the selection area"
           "Count", "Determines the number of values of the selection area"
           "Deviation", "Deviation from the maximum value of the reference value"
        """
        Max = 0  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
        Min = 1  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
        Sum = 2  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
        Count = 3  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
        Deviation = 4  # TBSBaseDesignVariableBuilderGroupOperatorMemberType
        
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
        
    
    DesignElements: TBSGroupDefinition = ...
    """
    Returns  the element group in which the value of the design variable is to be determined 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignElements`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DesignNodes: TBSGroupDefinition = ...
    """
    Returns  the node group in which the value of the design variable is to be determined 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignNodes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    GroupOperatorOption: TBSBaseDesignVariableBuilderGroupOperator = ...
    """
    Returns or sets  the group operator option 
    
    <hr>
    
    Getter Method
    
    Signature ``GroupOperatorOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSBaseDesignVariableBuilderGroupOperator` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GroupOperatorOption`` 
    
    :param groupOperatorOption: 
    :type groupOperatorOption: :py:class:`NXOpen.CAE.Optimization.TBSBaseDesignVariableBuilderGroupOperator` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    LoadCases: TBSLoadCaseManager = ...
    """
    Returns  the load cases 
    
    <hr>
    
    Getter Method
    
    Signature ``LoadCases`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSLoadCaseManager` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    NameDescription: NameDescription = ...
    """
    Returns  the name description 
    
    <hr>
    
    Getter Method
    
    Signature ``NameDescription`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.NameDescription` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    ReferenceCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the referenced coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceCoordinateSystem`` 
    
    :param referenceCsys: 
    :type referenceCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SelectionAreaType: TBSGroupDefinitionGroupElementType = ...
    """
    Returns or sets  the type of selection location on which design variable is applied 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionAreaType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinitionGroupElementType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionAreaType`` 
    
    :param areaType: 
    :type areaType: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinitionGroupElementType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSBaseDesignVariableBuilder = ...  # unknown typename


class TBSTopologyRestrictArea(TBSRestrictArea):
    """
    Represents the restrictions of the design variable in topology optimization   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictAreaBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSTopologyRestrictArea = ...  # unknown typename


class TBSTopologyOptimizationSolutionBuilder(TBSOptimizationSolutionBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSTopologyOptimizationSolution`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateTopologyOptimizationSolutionBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSTopologyOptimizationSolutionBuilder = ...  # unknown typename


class LimitMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Limit():
    """
    Represents the limit type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Upper", "Upper"
       "Lower", "Lower"
    """
    Upper = 0  # LimitMemberType
    Lower = 1  # LimitMemberType
    
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
    


class TBSDesignResponseBuilderResponseMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSDesignResponseBuilderResponse():
    """
    Defines the design response type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "DynamicFrequency", "Eigenfrequency from modal analysis"
       "DynamicFrequencyKressissel", "Eigenfrequency calculated with Kreisselmaier-Steinhauser formula"
       "Volume", "Volume of element"
       "VolumeFill", "Volume of element"
       "Weight", "Weight of element"
       "DisplacementAbsolute", "Absolute nodal displacement"
       "DisplacementX", "Nodal displacement in X-direction"
       "DisplacementY", "Nodal displacement in Y-direction"
       "DisplacementZ", "Nodal displacement in Z-direction"
       "DisplacementXAbsolute", "Absolute nodal displacement in X-direction"
       "DisplacementYAbsolute", "Absolute nodal displacement in Y-direction"
       "DisplacementZAbsolute", "Absolute nodal displacement in Z-directionm"
       "RotationAbsolute", "Absolute rotation"
       "RotationX", "Nodal rotation around X-axis"
       "RotationY", "Nodal rotation around Y-axis"
       "RotationZ", "Nodal rotation around Z-axis"
       "RotationXAbsolute", "Absolute nodal rotation around X-axis"
       "RotationYAbsolute", "Absolute nodal rotation around Y-axis"
       "RotationZAbsolute", "Absolute nodal rotation around Z-axis"
       "StrainEnergy", "Strain energy"
       "CenterGravityX", "Center of gravity for the X-direction"
       "CenterGravityY", "Center of gravity for the Y-direction"
       "CenterGravityZ", "Center of gravity for the Z-direction"
       "InertiaXx", "Moment of inertia around X-X-direction"
       "InertiaXy", "Moment of inertia around X-Y-direction"
       "InertiaXz", "Moment of inertia around X-Z-direction"
       "InertiaYy", "Moment of inertia around Y-Y-direction"
       "InertiaYz", "Moment of inertia around Y-Z-direction"
       "InertiaZz", "Moment of inertia around Z-Z-direction"
       "ReactionForceAbsolute", "Absolute nodal reaction force"
       "ReactionForceX", "Nodal reaction force in X-direction"
       "ReactionForceY", "Nodal reaction force in Y-direction"
       "ReactionForceZ", "Nodal reaction force in Z-direction"
       "ReactionForceXAbsolute", "Absolute nodal reaction force in X-direction"
       "ReactionForceYAbsolute", "Absolute nodal reaction force in Y-direction"
       "ReactionForceZAbsolute", "Absolute nodal reaction force in Z-direction"
       "ReactionForceRotationAbsolute", "Absolute nodal reaction moment"
       "ReactionForceRotationX", "Nodal reaction moment around X-axis"
       "ReactionForceRotationY", "Nodal reaction moment around Y-axis"
       "ReactionForceRotationZ", "Nodal reaction moment around Z-axis"
       "ReactionForceRotationXAbsolute", "Absolute nodal reaction moment around X-axis"
       "ReactionForceRotationYAbsolute", "Absolute nodal reaction moment around Y-axis"
       "ReactionForceRotationZAbsolute", "Absolute nodal reaction moment around Z-axis"
       "InternalForceAbsolute", "Absolute nodal internal force"
       "InternalForceX", "Nodal internal force in X-direction"
       "InternalForceY", "Nodal internal force in Y-direction"
       "InternalForceZ", "Nodal internal force in Z-direction"
       "InternalForceXAbsolute", "Absolute nodal internal force in X-direction"
       "InternalForceYAbsolute", "Absolute nodal internal force in Y-direction"
       "InternalForceZAbsolute", "Absolute nodal internal force in Z-direction"
       "InternalForceRotationAbsolute", "Absolute nodal internal moment"
       "InternalForceRotationX", "Nodal internal moment around X-axis"
       "InternalForceRotationY", "Nodal internal moment around Y-axis"
       "InternalForceRotationZ", "Nodal internal moment around Z-axis"
       "InternalForceRotationXAbsolute", "Absolute nodal internal moment around X-axis"
       "InternalForceRotationYAbsolute", "Absolute nodal internal moment around Y-axis"
       "InternalForceRotationZAbsolute", "Absolute nodal internal moment around Z-axis"
       "FrequencyResponseAccelerationX", "Acceleration in X-direction for frequency response"
       "FrequencyResponseAccelerationY", "Acceleration in Y-direction for frequency response"
       "FrequencyResponseAccelerationZ", "Acceleration in Z-direction for frequency response"
       "FrequencyResponseCompliance", "Dynamic compliance for frequency response"
       "FrequencyResponseDbaPressure", "Sound pressure level (dBA)"
       "FrequencyResponseDbPressure", "Sound pressure level (dB)"
       "FrequencyResponseDisplacementAbsolute", "Absolute amplitude for frequency response"
       "FrequencyResponseDisplacementXAbsolute", "Amplitude in X-direction for frequency response"
       "FrequencyResponseDisplacementYAbsolute", "Amplitude in Y-direction for frequency respons"
       "FrequencyResponseDisplacementZAbsolute", "Amplitude in Z-direction for frequency respons"
       "FrequencyResponsePhaseXAbsolute", "Phase in X-direction for frequency response"
       "FrequencyResponsePhaseYAbsolute", "Phase in Y-direction for frequency response"
       "FrequencyResponsePhaseZAbsolute", "Phase in Z-direction for frequency response"
       "FrequencyResponsePressure", "Instantaneous sound pressure"
       "FrequencyResponseRmsPressure", "Effective sound pressure"
       "FrequencyResponseVelocityXAbsolute", "Velocity in X-direction for frequecy response"
       "FrequencyResponseVelocityYAbsolute", "Velocity in Y-direction for frequecy response"
       "FrequencyResponseVelocityZAbsolute", "Velocity in Z-direction for frequecy response"
       "FrequencyResponseNvhSolid", "Surface normal velocity equivalent. Referenced node group, must be on solid elements"
       "FrequencyResponseNvhShell", "Surface normal velocity equivalent. Referenced node group, must be on plate or shell elements"
       "MisesStressHypothesis", "Mises Stress hypothesis"
       "MaximumPrincipalStress", "Maximum principal Stress"
       "MinimumAbsolutePrincipalStress", "Absolute value of the minimum principal Stress"
       "MaximumAbsolutePrincipalStress", "Maximum of absolute value of the principal stress"
    """
    DynamicFrequency = 0  # TBSDesignResponseBuilderResponseMemberType
    DynamicFrequencyKressissel = 1  # TBSDesignResponseBuilderResponseMemberType
    Volume = 2  # TBSDesignResponseBuilderResponseMemberType
    VolumeFill = 3  # TBSDesignResponseBuilderResponseMemberType
    Weight = 4  # TBSDesignResponseBuilderResponseMemberType
    DisplacementAbsolute = 5  # TBSDesignResponseBuilderResponseMemberType
    DisplacementX = 6  # TBSDesignResponseBuilderResponseMemberType
    DisplacementY = 7  # TBSDesignResponseBuilderResponseMemberType
    DisplacementZ = 8  # TBSDesignResponseBuilderResponseMemberType
    DisplacementXAbsolute = 9  # TBSDesignResponseBuilderResponseMemberType
    DisplacementYAbsolute = 10  # TBSDesignResponseBuilderResponseMemberType
    DisplacementZAbsolute = 11  # TBSDesignResponseBuilderResponseMemberType
    RotationAbsolute = 12  # TBSDesignResponseBuilderResponseMemberType
    RotationX = 13  # TBSDesignResponseBuilderResponseMemberType
    RotationY = 14  # TBSDesignResponseBuilderResponseMemberType
    RotationZ = 15  # TBSDesignResponseBuilderResponseMemberType
    RotationXAbsolute = 16  # TBSDesignResponseBuilderResponseMemberType
    RotationYAbsolute = 17  # TBSDesignResponseBuilderResponseMemberType
    RotationZAbsolute = 18  # TBSDesignResponseBuilderResponseMemberType
    StrainEnergy = 19  # TBSDesignResponseBuilderResponseMemberType
    CenterGravityX = 20  # TBSDesignResponseBuilderResponseMemberType
    CenterGravityY = 21  # TBSDesignResponseBuilderResponseMemberType
    CenterGravityZ = 22  # TBSDesignResponseBuilderResponseMemberType
    InertiaXx = 23  # TBSDesignResponseBuilderResponseMemberType
    InertiaXy = 24  # TBSDesignResponseBuilderResponseMemberType
    InertiaXz = 25  # TBSDesignResponseBuilderResponseMemberType
    InertiaYy = 26  # TBSDesignResponseBuilderResponseMemberType
    InertiaYz = 27  # TBSDesignResponseBuilderResponseMemberType
    InertiaZz = 28  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceAbsolute = 29  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceX = 30  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceY = 31  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceZ = 32  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceXAbsolute = 33  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceYAbsolute = 34  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceZAbsolute = 35  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationAbsolute = 36  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationX = 37  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationY = 38  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationZ = 39  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationXAbsolute = 40  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationYAbsolute = 41  # TBSDesignResponseBuilderResponseMemberType
    ReactionForceRotationZAbsolute = 42  # TBSDesignResponseBuilderResponseMemberType
    InternalForceAbsolute = 43  # TBSDesignResponseBuilderResponseMemberType
    InternalForceX = 44  # TBSDesignResponseBuilderResponseMemberType
    InternalForceY = 45  # TBSDesignResponseBuilderResponseMemberType
    InternalForceZ = 46  # TBSDesignResponseBuilderResponseMemberType
    InternalForceXAbsolute = 47  # TBSDesignResponseBuilderResponseMemberType
    InternalForceYAbsolute = 48  # TBSDesignResponseBuilderResponseMemberType
    InternalForceZAbsolute = 49  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationAbsolute = 50  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationX = 51  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationY = 52  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationZ = 53  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationXAbsolute = 54  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationYAbsolute = 55  # TBSDesignResponseBuilderResponseMemberType
    InternalForceRotationZAbsolute = 56  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseAccelerationX = 57  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseAccelerationY = 58  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseAccelerationZ = 59  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseCompliance = 60  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDbaPressure = 61  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDbPressure = 62  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDisplacementAbsolute = 63  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDisplacementXAbsolute = 64  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDisplacementYAbsolute = 65  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseDisplacementZAbsolute = 66  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponsePhaseXAbsolute = 67  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponsePhaseYAbsolute = 68  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponsePhaseZAbsolute = 69  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponsePressure = 70  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseRmsPressure = 71  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseVelocityXAbsolute = 72  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseVelocityYAbsolute = 73  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseVelocityZAbsolute = 74  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseNvhSolid = 75  # TBSDesignResponseBuilderResponseMemberType
    FrequencyResponseNvhShell = 76  # TBSDesignResponseBuilderResponseMemberType
    MisesStressHypothesis = 77  # TBSDesignResponseBuilderResponseMemberType
    MaximumPrincipalStress = 78  # TBSDesignResponseBuilderResponseMemberType
    MinimumAbsolutePrincipalStress = 79  # TBSDesignResponseBuilderResponseMemberType
    MaximumAbsolutePrincipalStress = 80  # TBSDesignResponseBuilderResponseMemberType
    
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
    


class TBSDesignResponseBuilder(TBSBaseDesignVariableBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse`  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateDesignResponseBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class Response():
        """
        Defines the design response type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "DynamicFrequency", "Eigenfrequency from modal analysis"
           "DynamicFrequencyKressissel", "Eigenfrequency calculated with Kreisselmaier-Steinhauser formula"
           "Volume", "Volume of element"
           "VolumeFill", "Volume of element"
           "Weight", "Weight of element"
           "DisplacementAbsolute", "Absolute nodal displacement"
           "DisplacementX", "Nodal displacement in X-direction"
           "DisplacementY", "Nodal displacement in Y-direction"
           "DisplacementZ", "Nodal displacement in Z-direction"
           "DisplacementXAbsolute", "Absolute nodal displacement in X-direction"
           "DisplacementYAbsolute", "Absolute nodal displacement in Y-direction"
           "DisplacementZAbsolute", "Absolute nodal displacement in Z-directionm"
           "RotationAbsolute", "Absolute rotation"
           "RotationX", "Nodal rotation around X-axis"
           "RotationY", "Nodal rotation around Y-axis"
           "RotationZ", "Nodal rotation around Z-axis"
           "RotationXAbsolute", "Absolute nodal rotation around X-axis"
           "RotationYAbsolute", "Absolute nodal rotation around Y-axis"
           "RotationZAbsolute", "Absolute nodal rotation around Z-axis"
           "StrainEnergy", "Strain energy"
           "CenterGravityX", "Center of gravity for the X-direction"
           "CenterGravityY", "Center of gravity for the Y-direction"
           "CenterGravityZ", "Center of gravity for the Z-direction"
           "InertiaXx", "Moment of inertia around X-X-direction"
           "InertiaXy", "Moment of inertia around X-Y-direction"
           "InertiaXz", "Moment of inertia around X-Z-direction"
           "InertiaYy", "Moment of inertia around Y-Y-direction"
           "InertiaYz", "Moment of inertia around Y-Z-direction"
           "InertiaZz", "Moment of inertia around Z-Z-direction"
           "ReactionForceAbsolute", "Absolute nodal reaction force"
           "ReactionForceX", "Nodal reaction force in X-direction"
           "ReactionForceY", "Nodal reaction force in Y-direction"
           "ReactionForceZ", "Nodal reaction force in Z-direction"
           "ReactionForceXAbsolute", "Absolute nodal reaction force in X-direction"
           "ReactionForceYAbsolute", "Absolute nodal reaction force in Y-direction"
           "ReactionForceZAbsolute", "Absolute nodal reaction force in Z-direction"
           "ReactionForceRotationAbsolute", "Absolute nodal reaction moment"
           "ReactionForceRotationX", "Nodal reaction moment around X-axis"
           "ReactionForceRotationY", "Nodal reaction moment around Y-axis"
           "ReactionForceRotationZ", "Nodal reaction moment around Z-axis"
           "ReactionForceRotationXAbsolute", "Absolute nodal reaction moment around X-axis"
           "ReactionForceRotationYAbsolute", "Absolute nodal reaction moment around Y-axis"
           "ReactionForceRotationZAbsolute", "Absolute nodal reaction moment around Z-axis"
           "InternalForceAbsolute", "Absolute nodal internal force"
           "InternalForceX", "Nodal internal force in X-direction"
           "InternalForceY", "Nodal internal force in Y-direction"
           "InternalForceZ", "Nodal internal force in Z-direction"
           "InternalForceXAbsolute", "Absolute nodal internal force in X-direction"
           "InternalForceYAbsolute", "Absolute nodal internal force in Y-direction"
           "InternalForceZAbsolute", "Absolute nodal internal force in Z-direction"
           "InternalForceRotationAbsolute", "Absolute nodal internal moment"
           "InternalForceRotationX", "Nodal internal moment around X-axis"
           "InternalForceRotationY", "Nodal internal moment around Y-axis"
           "InternalForceRotationZ", "Nodal internal moment around Z-axis"
           "InternalForceRotationXAbsolute", "Absolute nodal internal moment around X-axis"
           "InternalForceRotationYAbsolute", "Absolute nodal internal moment around Y-axis"
           "InternalForceRotationZAbsolute", "Absolute nodal internal moment around Z-axis"
           "FrequencyResponseAccelerationX", "Acceleration in X-direction for frequency response"
           "FrequencyResponseAccelerationY", "Acceleration in Y-direction for frequency response"
           "FrequencyResponseAccelerationZ", "Acceleration in Z-direction for frequency response"
           "FrequencyResponseCompliance", "Dynamic compliance for frequency response"
           "FrequencyResponseDbaPressure", "Sound pressure level (dBA)"
           "FrequencyResponseDbPressure", "Sound pressure level (dB)"
           "FrequencyResponseDisplacementAbsolute", "Absolute amplitude for frequency response"
           "FrequencyResponseDisplacementXAbsolute", "Amplitude in X-direction for frequency response"
           "FrequencyResponseDisplacementYAbsolute", "Amplitude in Y-direction for frequency respons"
           "FrequencyResponseDisplacementZAbsolute", "Amplitude in Z-direction for frequency respons"
           "FrequencyResponsePhaseXAbsolute", "Phase in X-direction for frequency response"
           "FrequencyResponsePhaseYAbsolute", "Phase in Y-direction for frequency response"
           "FrequencyResponsePhaseZAbsolute", "Phase in Z-direction for frequency response"
           "FrequencyResponsePressure", "Instantaneous sound pressure"
           "FrequencyResponseRmsPressure", "Effective sound pressure"
           "FrequencyResponseVelocityXAbsolute", "Velocity in X-direction for frequecy response"
           "FrequencyResponseVelocityYAbsolute", "Velocity in Y-direction for frequecy response"
           "FrequencyResponseVelocityZAbsolute", "Velocity in Z-direction for frequecy response"
           "FrequencyResponseNvhSolid", "Surface normal velocity equivalent. Referenced node group, must be on solid elements"
           "FrequencyResponseNvhShell", "Surface normal velocity equivalent. Referenced node group, must be on plate or shell elements"
           "MisesStressHypothesis", "Mises Stress hypothesis"
           "MaximumPrincipalStress", "Maximum principal Stress"
           "MinimumAbsolutePrincipalStress", "Absolute value of the minimum principal Stress"
           "MaximumAbsolutePrincipalStress", "Maximum of absolute value of the principal stress"
        """
        DynamicFrequency = 0  # TBSDesignResponseBuilderResponseMemberType
        DynamicFrequencyKressissel = 1  # TBSDesignResponseBuilderResponseMemberType
        Volume = 2  # TBSDesignResponseBuilderResponseMemberType
        VolumeFill = 3  # TBSDesignResponseBuilderResponseMemberType
        Weight = 4  # TBSDesignResponseBuilderResponseMemberType
        DisplacementAbsolute = 5  # TBSDesignResponseBuilderResponseMemberType
        DisplacementX = 6  # TBSDesignResponseBuilderResponseMemberType
        DisplacementY = 7  # TBSDesignResponseBuilderResponseMemberType
        DisplacementZ = 8  # TBSDesignResponseBuilderResponseMemberType
        DisplacementXAbsolute = 9  # TBSDesignResponseBuilderResponseMemberType
        DisplacementYAbsolute = 10  # TBSDesignResponseBuilderResponseMemberType
        DisplacementZAbsolute = 11  # TBSDesignResponseBuilderResponseMemberType
        RotationAbsolute = 12  # TBSDesignResponseBuilderResponseMemberType
        RotationX = 13  # TBSDesignResponseBuilderResponseMemberType
        RotationY = 14  # TBSDesignResponseBuilderResponseMemberType
        RotationZ = 15  # TBSDesignResponseBuilderResponseMemberType
        RotationXAbsolute = 16  # TBSDesignResponseBuilderResponseMemberType
        RotationYAbsolute = 17  # TBSDesignResponseBuilderResponseMemberType
        RotationZAbsolute = 18  # TBSDesignResponseBuilderResponseMemberType
        StrainEnergy = 19  # TBSDesignResponseBuilderResponseMemberType
        CenterGravityX = 20  # TBSDesignResponseBuilderResponseMemberType
        CenterGravityY = 21  # TBSDesignResponseBuilderResponseMemberType
        CenterGravityZ = 22  # TBSDesignResponseBuilderResponseMemberType
        InertiaXx = 23  # TBSDesignResponseBuilderResponseMemberType
        InertiaXy = 24  # TBSDesignResponseBuilderResponseMemberType
        InertiaXz = 25  # TBSDesignResponseBuilderResponseMemberType
        InertiaYy = 26  # TBSDesignResponseBuilderResponseMemberType
        InertiaYz = 27  # TBSDesignResponseBuilderResponseMemberType
        InertiaZz = 28  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceAbsolute = 29  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceX = 30  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceY = 31  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceZ = 32  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceXAbsolute = 33  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceYAbsolute = 34  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceZAbsolute = 35  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationAbsolute = 36  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationX = 37  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationY = 38  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationZ = 39  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationXAbsolute = 40  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationYAbsolute = 41  # TBSDesignResponseBuilderResponseMemberType
        ReactionForceRotationZAbsolute = 42  # TBSDesignResponseBuilderResponseMemberType
        InternalForceAbsolute = 43  # TBSDesignResponseBuilderResponseMemberType
        InternalForceX = 44  # TBSDesignResponseBuilderResponseMemberType
        InternalForceY = 45  # TBSDesignResponseBuilderResponseMemberType
        InternalForceZ = 46  # TBSDesignResponseBuilderResponseMemberType
        InternalForceXAbsolute = 47  # TBSDesignResponseBuilderResponseMemberType
        InternalForceYAbsolute = 48  # TBSDesignResponseBuilderResponseMemberType
        InternalForceZAbsolute = 49  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationAbsolute = 50  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationX = 51  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationY = 52  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationZ = 53  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationXAbsolute = 54  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationYAbsolute = 55  # TBSDesignResponseBuilderResponseMemberType
        InternalForceRotationZAbsolute = 56  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseAccelerationX = 57  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseAccelerationY = 58  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseAccelerationZ = 59  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseCompliance = 60  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDbaPressure = 61  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDbPressure = 62  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDisplacementAbsolute = 63  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDisplacementXAbsolute = 64  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDisplacementYAbsolute = 65  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseDisplacementZAbsolute = 66  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponsePhaseXAbsolute = 67  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponsePhaseYAbsolute = 68  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponsePhaseZAbsolute = 69  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponsePressure = 70  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseRmsPressure = 71  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseVelocityXAbsolute = 72  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseVelocityYAbsolute = 73  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseVelocityZAbsolute = 74  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseNvhSolid = 75  # TBSDesignResponseBuilderResponseMemberType
        FrequencyResponseNvhShell = 76  # TBSDesignResponseBuilderResponseMemberType
        MisesStressHypothesis = 77  # TBSDesignResponseBuilderResponseMemberType
        MaximumPrincipalStress = 78  # TBSDesignResponseBuilderResponseMemberType
        MinimumAbsolutePrincipalStress = 79  # TBSDesignResponseBuilderResponseMemberType
        MaximumAbsolutePrincipalStress = 80  # TBSDesignResponseBuilderResponseMemberType
        
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
        
    
    VariableType: TBSDesignResponseBuilderResponse = ...
    """
    Returns or sets  the varialbe type 
    
    <hr>
    
    Getter Method
    
    Signature ``VariableType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponseBuilderResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VariableType`` 
    
    :param categoryOption: 
    :type categoryOption: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponseBuilderResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSDesignResponseBuilder = ...  # unknown typename


class ResponseMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Response():
    """
    Represents the specific variable 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Weight", " - "
       "Volume", " - "
       "Frequency", " - "
       "Temperature", " - "
       "StressVonMises", " - "
       "StrainVonMises", " - "
       "TranslationX", " - "
       "TranslationY", " - "
       "TranslationZ", " - "
       "RotationX", " - "
       "RotationY", " - "
       "RotationZ", " - "
       "Stress2DMaximumShear", " - "
       "Stress2DMajorPrincipal", " - "
       "Stress2DMinorPrincipal", " - "
       "Stress2DVonMises", " - "
       "Stress2DMaximumShearBottom", " - "
       "Stress2DMajorPrincipalBottom", " - "
       "Stress2DMinorPrincipalBottom", " - "
       "Stress2DVonMisesBottom", " - "
       "Strain2DMaximumShear", " - "
       "Strain2DMajorPrincipal", " - "
       "Strain2DMinorPrincipal", " - "
       "Strain2DVonMises", " - "
       "Strain2DMaximumShearBottom", " - "
       "Strain2DMajorPrincipalBottom", " - "
       "Strain2DMinorPrincipalBottom", " - "
       "Strain2DVonMisesBottom", " - "
       "Stress1DVonMisesStressRecoveryPointC", " - "
       "Stress1DVonMisesStressRecoveryPointD", " - "
       "Stress1DVonMisesStressRecoveryPointE", " - "
       "Stress1DVonMisesStressRecoveryPointF", " - "
       "Stress1DVonMisesMaximum", " - "
       "Stress1DVonMisesMinimum", " - "
       "Strain1DVonMisesStressRecoveryPointC", " - "
       "Strain1DVonMisesStressRecoveryPointD", " - "
       "Strain1DVonMisesStressRecoveryPointE", " - "
       "Strain1DVonMisesStressRecoveryPointF", " - "
       "Strain1DVonMisesMaximum", " - "
       "Strain1DVonMisesMinimum", " - "
       "Stress3DFirstPrincipal", " - "
       "Stress3DSecondPrincipal", " - "
       "Stress3DThirdPrincipal", " - "
       "Stress3DVonMises", " - "
       "Strain3DFirstPrincipal", " - "
       "Strain3DSecondPrincipal", " - "
       "Strain3DThirdPrincipal", " - "
       "Strain3DVonMises", " - "
       "ResultMeasure", "Response type is a result measure"
    """
    NotSet = 0  # ResponseMemberType
    Weight = 1  # ResponseMemberType
    Volume = 2  # ResponseMemberType
    Frequency = 3  # ResponseMemberType
    Temperature = 4  # ResponseMemberType
    StressVonMises = 5  # ResponseMemberType
    StrainVonMises = 6  # ResponseMemberType
    TranslationX = 7  # ResponseMemberType
    TranslationY = 8  # ResponseMemberType
    TranslationZ = 9  # ResponseMemberType
    RotationX = 10  # ResponseMemberType
    RotationY = 11  # ResponseMemberType
    RotationZ = 12  # ResponseMemberType
    Stress2DMaximumShear = 13  # ResponseMemberType
    Stress2DMajorPrincipal = 14  # ResponseMemberType
    Stress2DMinorPrincipal = 15  # ResponseMemberType
    Stress2DVonMises = 16  # ResponseMemberType
    Stress2DMaximumShearBottom = 17  # ResponseMemberType
    Stress2DMajorPrincipalBottom = 18  # ResponseMemberType
    Stress2DMinorPrincipalBottom = 19  # ResponseMemberType
    Stress2DVonMisesBottom = 20  # ResponseMemberType
    Strain2DMaximumShear = 21  # ResponseMemberType
    Strain2DMajorPrincipal = 22  # ResponseMemberType
    Strain2DMinorPrincipal = 23  # ResponseMemberType
    Strain2DVonMises = 24  # ResponseMemberType
    Strain2DMaximumShearBottom = 25  # ResponseMemberType
    Strain2DMajorPrincipalBottom = 26  # ResponseMemberType
    Strain2DMinorPrincipalBottom = 27  # ResponseMemberType
    Strain2DVonMisesBottom = 28  # ResponseMemberType
    Stress1DVonMisesStressRecoveryPointC = 29  # ResponseMemberType
    Stress1DVonMisesStressRecoveryPointD = 30  # ResponseMemberType
    Stress1DVonMisesStressRecoveryPointE = 31  # ResponseMemberType
    Stress1DVonMisesStressRecoveryPointF = 32  # ResponseMemberType
    Stress1DVonMisesMaximum = 33  # ResponseMemberType
    Stress1DVonMisesMinimum = 34  # ResponseMemberType
    Strain1DVonMisesStressRecoveryPointC = 35  # ResponseMemberType
    Strain1DVonMisesStressRecoveryPointD = 36  # ResponseMemberType
    Strain1DVonMisesStressRecoveryPointE = 37  # ResponseMemberType
    Strain1DVonMisesStressRecoveryPointF = 38  # ResponseMemberType
    Strain1DVonMisesMaximum = 39  # ResponseMemberType
    Strain1DVonMisesMinimum = 40  # ResponseMemberType
    Stress3DFirstPrincipal = 41  # ResponseMemberType
    Stress3DSecondPrincipal = 42  # ResponseMemberType
    Stress3DThirdPrincipal = 43  # ResponseMemberType
    Stress3DVonMises = 44  # ResponseMemberType
    Strain3DFirstPrincipal = 45  # ResponseMemberType
    Strain3DSecondPrincipal = 46  # ResponseMemberType
    Strain3DThirdPrincipal = 47  # ResponseMemberType
    Strain3DVonMises = 48  # ResponseMemberType
    ResultMeasure = 49  # ResponseMemberType
    
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
    


class TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyRestrictAreaBuilderCheckTypeOption():
    """
    Defines the type of restriction 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Frozen", "All elements of the element group which do not undergo any changes during optimization"
       "LinkTopo", "Definition of symmetry and link condtions"
       "MaximumsSize", "Defition of the maximum structural diameter"
       "MinimumSize", "Definition of minimum structural diameter"
       "Cast", "Manufacturing restrictions to guarantee the manufacturing of the elements"
    """
    Frozen = 0  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
    LinkTopo = 1  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
    MaximumsSize = 2  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
    MinimumSize = 3  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
    Cast = 4  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
    
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
    


class TBSTopologyRestrictAreaBuilder(TBSRestrictAreaBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictArea`  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateTopologyRestrictAreaBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class CheckTypeOption():
        """
        Defines the type of restriction 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Frozen", "All elements of the element group which do not undergo any changes during optimization"
           "LinkTopo", "Definition of symmetry and link condtions"
           "MaximumsSize", "Defition of the maximum structural diameter"
           "MinimumSize", "Definition of minimum structural diameter"
           "Cast", "Manufacturing restrictions to guarantee the manufacturing of the elements"
        """
        Frozen = 0  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
        LinkTopo = 1  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
        MaximumsSize = 2  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
        MinimumSize = 3  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
        Cast = 4  # TBSTopologyRestrictAreaBuilderCheckTypeOptionMemberType
        
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
        
    
    CastCondition: TBSCastCondition = ...
    """
    Returns  the cast condition 
    
    <hr>
    
    Getter Method
    
    Signature ``CastCondition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSCastCondition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    CheckingElementGroup: TBSGroupDefinition = ...
    """
    Returns  the elements to react on the restrictions 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckingElementGroup`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    CheckingType: TBSTopologyRestrictAreaBuilderCheckTypeOption = ...
    """
    Returns or sets  the checking type 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictAreaBuilderCheckTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckingType`` 
    
    :param checkType: 
    :type checkType: :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictAreaBuilderCheckTypeOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Distance: NXOpen.Expression = ...
    """
    Returns  the distance value 
    
    <hr>
    
    Getter Method
    
    Signature ``Distance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    LinkCondition: TBSTopologyLinkCondition = ...
    """
    Returns  the link condition 
    
    <hr>
    
    Getter Method
    
    Signature ``LinkCondition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyLinkCondition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MinimumThickness: NXOpen.Expression = ...
    """
    Returns  the minimum thickness of the structure 
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumThickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Radius: NXOpen.Expression = ...
    """
    Returns  the radius 
    
    <hr>
    
    Getter Method
    
    Signature ``Radius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the maximum thickness of the structure
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSTopologyRestrictAreaBuilder = ...  # unknown typename


class GeometryMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Geometry():
    """
    Represents the geometry type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Body", "Body"
       "Face", "Face"
       "Edge", "Edge"
       "Point", "Point"
       "Curve", "Curve"
    """
    Body = 0  # GeometryMemberType
    Face = 1  # GeometryMemberType
    Edge = 2  # GeometryMemberType
    Point = 3  # GeometryMemberType
    Curve = 4  # GeometryMemberType
    
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
    


class TBSLoadCaseLayerOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSLoadCaseLayerOption():
    """
    Defines the location for calcuating shell stresses 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No calculation"
       "Maximum", "the maximum value among Top, Middle and Bottom"
       "Minimum", "the minimum value among Top, Middle and Bottom"
       "Top", "Top-layer of shell"
       "Middle", "Mid-layer of shell"
       "Bottom", "Bottom layer of shell"
    """
    NotSet = 0  # TBSLoadCaseLayerOptionMemberType
    Maximum = 1  # TBSLoadCaseLayerOptionMemberType
    Minimum = 2  # TBSLoadCaseLayerOptionMemberType
    Top = 3  # TBSLoadCaseLayerOptionMemberType
    Middle = 4  # TBSLoadCaseLayerOptionMemberType
    Bottom = 5  # TBSLoadCaseLayerOptionMemberType
    
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
    


class TBSLoadCase(NXOpen.TaggedObject):
    """
    Represents the load case   
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateLoadCase`
    
    .. versionadded:: NX8.0.0
    """
    
    class LayerOption():
        """
        Defines the location for calcuating shell stresses 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No calculation"
           "Maximum", "the maximum value among Top, Middle and Bottom"
           "Minimum", "the minimum value among Top, Middle and Bottom"
           "Top", "Top-layer of shell"
           "Middle", "Mid-layer of shell"
           "Bottom", "Bottom layer of shell"
        """
        NotSet = 0  # TBSLoadCaseLayerOptionMemberType
        Maximum = 1  # TBSLoadCaseLayerOptionMemberType
        Minimum = 2  # TBSLoadCaseLayerOptionMemberType
        Top = 3  # TBSLoadCaseLayerOptionMemberType
        Middle = 4  # TBSLoadCaseLayerOptionMemberType
        Bottom = 5  # TBSLoadCaseLayerOptionMemberType
        
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
        
    
    
    def GetSubcase(self) -> tuple:
        """
        Returns the load cases  
        
        Signature ``GetSubcase()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (allSubcase, subcaseId). allSubcase is a bool. subcaseId is a int. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSubcase(self, allSubcases: bool, subcaseId: int) -> None:
        """
        Sets the load cases 
        
        Signature ``SetSubcase(allSubcases, subcaseId)`` 
        
        :param allSubcases: 
        :type allSubcases: bool 
        :param subcaseId: 
        :type subcaseId: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def GetSubstep(self) -> tuple:
        """
        Returns the substeps  
        
        Signature ``GetSubstep()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (allSubSteps, subSteps). allSubSteps is a bool. subSteps is a list of int. 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetSubstep(self, allSubSteps: bool, subSteps: 'list[int]') -> None:
        """
        Sets the sub steps 
        
        Signature ``SetSubstep(allSubSteps, subSteps)`` 
        
        :param allSubSteps: 
        :type allSubSteps: bool 
        :param subSteps: 
        :type subSteps: list of int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    ShellLayer: TBSLoadCaseLayerOption = ...
    """
    Returns or sets  the shell layer 
    
    <hr>
    
    Getter Method
    
    Signature ``ShellLayer`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSLoadCaseLayerOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShellLayer`` 
    
    :param layer: 
    :type layer: :py:class:`NXOpen.CAE.Optimization.TBSLoadCaseLayerOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSLoadCase = ...  # unknown typename


class TBSDesignResponse(TBSDesignVariable):
    """
    Represents the design response referenced by :py:class:`NXOpen.CAE.Optimization.TBSConstraint` and 
    :py:class:`NXOpen.CAE.Optimization.TBSObjectives`  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSDesignResponseBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSDesignResponse = ...  # unknown typename


class TBSDesignVariableBuilder(TBSBaseDesignVariableBuilder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable`  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateDesignVariableBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSDesignVariableBuilder = ...  # unknown typename


class DAOConstraintBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOConstraintBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.DAOSolutionCollection.CreateConstraintBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetGeometry(self) -> 'list[NXOpen.DisplayableObject]':
        """
        Gets the target geometry  
        
        Signature ``GetGeometry()`` 
        
        :returns:  Target geometry  
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGeometry(self, geometry: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Sets the target geometry 
        
        Signature ``SetGeometry(geometry)`` 
        
        :param geometry:  Target geometry  
        :type geometry: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    CategoryType: Category = ...
    """
    Returns or sets  the category type 
    
    <hr>
    
    Getter Method
    
    Signature ``CategoryType`` 
    
    :returns:  Category type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Category` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CategoryType`` 
    
    :param categoryType:  Category type  
    :type categoryType: :py:class:`NXOpen.CAE.Optimization.Category` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    GeometryType: Geometry = ...
    """
    Returns or sets  the geometry type 
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryType`` 
    
    :returns:  Geometry type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Geometry` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryType`` 
    
    :param geometryType:  Geometry type  
    :type geometryType: :py:class:`NXOpen.CAE.Optimization.Geometry` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LimitType: Limit = ...
    """
    Returns or sets  the limit type 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitType`` 
    
    :returns:  Limit type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Limit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitType`` 
    
    :param limitType:  Limit type  
    :type limitType: :py:class:`NXOpen.CAE.Optimization.Limit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LimitUnit: NXOpen.Unit = ...
    """
    Returns or sets  the limit unit 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitUnit`` 
    
    :returns:  Limit unit  
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitUnit`` 
    
    :param targetUnit:  Limit unit  
    :type targetUnit: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LimitValue: float = ...
    """
    Returns or sets  the limit value 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitValue`` 
    
    :returns:  Limit value  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitValue`` 
    
    :param limitValue:  Limit value  
    :type limitValue: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LoadCase: int = ...
    """
    Returns or sets  the frequency load case index 
    
    <hr>
    
    Getter Method
    
    Signature ``LoadCase`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LoadCase`` 
    
    :param loadcase: 
    :type loadcase: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ModeNumber: int = ...
    """
    Returns or sets  the frequency mode number 
    
    <hr>
    
    Getter Method
    
    Signature ``ModeNumber`` 
    
    :returns:  Mode number  
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModeNumber`` 
    
    :param modeNumber:  Mode number  
    :type modeNumber: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Response: Response = ...
    """
    Returns or sets  the constraint response 
    
    <hr>
    
    Getter Method
    
    Signature ``Response`` 
    
    :returns:  Constraint response  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Response` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Response`` 
    
    :param constraintResponse:  Constraint response  
    :type constraintResponse: :py:class:`NXOpen.CAE.Optimization.Response` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ResultMeasure: NXOpen.CAE.ResultMeasure = ...
    """
    Returns or sets  the result measure 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultMeasure`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResultMeasure` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResultMeasure`` 
    
    :param resMeas: 
    :type resMeas: :py:class:`NXOpen.CAE.ResultMeasure` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: DAOConstraintBuilder = ...  # unknown typename


class DAODesignVariableCollection(NXOpen.TaggedObjectCollection):
    """
    Represents the collection of optimization solution design variable   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.DAOSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, designVariableName: str) -> DAODesignVariable:
        """
        Finds an optimization solution design variable with a specified name  
        
        Signature ``FindObject(designVariableName)`` 
        
        :param designVariableName:  Design variable name  
        :type designVariableName: str 
        :returns:  Design variable  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class DAOSolution(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOSolution`.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.DAOSolutionBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def GetDesignObjective(self) -> DAOObjective:
        """
        Gets the optimization solution design objective  
        
        Signature ``GetDesignObjective()`` 
        
        :returns:  Design objective  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOObjective` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDesignConstraints(self) -> 'list[DAOConstraint]':
        """
        Gets the optimization solution design constraints  
        
        Signature ``GetDesignConstraints()`` 
        
        :returns:  Design constraints  
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDesignConstraints(self, designConstraints: 'list[DAOConstraint]') -> None:
        """
        Sets the optimization solution design constraints 
        
        Signature ``SetDesignConstraints(designConstraints)`` 
        
        :param designConstraints:  Design constraints  
        :type designConstraints: list of :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Not a valid method. Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.CreateConstraintBuilder` instead.
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetOptimizationDesignVariables(self) -> 'list[DAODesignVariable]':
        """
        Gets the optimization solution design variables for general optimization type  
        
        Signature ``GetOptimizationDesignVariables()`` 
        
        :returns:  Design variables  
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOptimizationDesignVariables(self, designVariables: 'list[DAOConstraint]') -> None:
        """
        Sets the optimization solution design variables for general optimization type 
        
        Signature ``SetOptimizationDesignVariables(designVariables)`` 
        
        :param designVariables:  Design variables  
        :type designVariables: list of :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Not a valid method. Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.CreateDesignVariableBuilder` instead.
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetGlobalSensitivityDesignVariables(self) -> 'list[DAODesignVariable]':
        """
        Gets the optimization solution design variables for global sensitivity optimization type  
        
        Signature ``GetGlobalSensitivityDesignVariables()`` 
        
        :returns:  Design variables  
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGlobalSensitivityDesignVariables(self, designVariables: 'list[DAODesignVariable]') -> None:
        """
        Sets the optimization solution design variables for global sensitivity optimization type 
        
        Signature ``SetGlobalSensitivityDesignVariables(designVariables)`` 
        
        :param designVariables:  Design variables  
        :type designVariables: list of :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetSolutionControls(self) -> DAOStopCondition:
        """
        Gets the optimization solution optimizer control  
        
        Signature ``GetSolutionControls()`` 
        
        :returns:  Optimizer control  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOStopCondition` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Solve(self) -> None:
        """
        Solves the optimization solution 
        
        Signature ``Solve()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def DeleteSolution(self) -> None:
        """
        Deletes the optimization solution 
        
        Signature ``DeleteSolution()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def ActivateSolution(self) -> None:
        """
        Activates the optimization solution setup 
        
        Signature ``ActivateSolution()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateConstraintBuilder(self, optimizationConstraint: DAOConstraint) -> DAOConstraintBuilder:
        """
        Creates the builder object of optimization solution design constraint  
        
        Signature ``CreateConstraintBuilder(optimizationConstraint)`` 
        
        :param optimizationConstraint:  Design constraint  
        :type optimizationConstraint: :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        :returns:  Design constraint builder  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOConstraintBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateDesignVariableBuilder(self, optimizationDesvar: DAODesignVariable) -> DAODesignVariableBuilder:
        """
        Creates the builder object of optimization solution design variable  
        
        Signature ``CreateDesignVariableBuilder(optimizationDesvar)`` 
        
        :param optimizationDesvar:  Design variable  
        :type optimizationDesvar: :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        :returns:  Design variable builder  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    Name: str = ...
    """
    Returns or sets  the optimization solution name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  Solution name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param solutionName:  Solution name  
    :type solutionName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    OptimizerControl: DAOStopCondition = ...
    """
    Returns or sets  the optimization solution optimizer control 
    
    <hr>
    
    Getter Method
    
    Signature ``OptimizerControl`` 
    
    :returns:  Optimizer control  
    :rtype: :py:class:`NXOpen.CAE.Optimization.DAOStopCondition` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Not a valid method. Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.GetSolutionControls` instead.
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OptimizerControl`` 
    
    :param optimizerControl:  Optimizer control  
    :type optimizerControl: :py:class:`NXOpen.CAE.Optimization.DAOStopCondition` 
    
    .. versionadded:: NX8.0.0
    
    .. deprecated::  NX9.0.0
       Not a valid method. Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.GetSolutionControls` instead.
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SolverType: Solver = ...
    """
    Returns or sets  the optimization solution solver type 
    
    <hr>
    
    Getter Method
    
    Signature ``SolverType`` 
    
    :returns:  Optimization solution solver type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Solver` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverType`` 
    
    :param solverType:  Optimization solution solver type  
    :type solverType: :py:class:`NXOpen.CAE.Optimization.Solver` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    DesignConstraint: DAOConstraintCollection = ...
    """
    Returns the optimization design constraint collection.  
    
    Signature ``DesignConstraint`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.DAOConstraintCollection`
    """
    DesignVariable: DAODesignVariableCollection = ...
    """
    Returns the optimization design variable collection.  
    
    Signature ``DesignVariable`` 
    
    .. versionadded:: NX8.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.DAODesignVariableCollection`
    """
    Null: DAOSolution = ...  # unknown typename


class TBSGroupDefinitionDefinitionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSGroupDefinitionDefinitionType():
    """
    Represents the definition method of a group 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "All", "Defines a group with all nodes or elements"
       "Selected", "Defines a group by selection"
       "DesignArea", "Defines a group refer to design area"
       "MeshSmoothingArea", "Defines a group refer to mesh smoothing area"
    """
    All = 0  # TBSGroupDefinitionDefinitionTypeMemberType
    Selected = 1  # TBSGroupDefinitionDefinitionTypeMemberType
    DesignArea = 2  # TBSGroupDefinitionDefinitionTypeMemberType
    MeshSmoothingArea = 3  # TBSGroupDefinitionDefinitionTypeMemberType
    
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
    


class TBSGroupDefinitionGroupElementTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSGroupDefinitionGroupElementType():
    """
    Represents the type of group elements 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Element", "The group contains element"
       "Node", "The group contains node"
    """
    Element = 0  # TBSGroupDefinitionGroupElementTypeMemberType
    Node = 1  # TBSGroupDefinitionGroupElementTypeMemberType
    
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
    


class TBSGroupDefinition(NXOpen.TaggedObject):
    """
    Represents a group of nodes or elements   
    
    .. versionadded:: NX8.0.0
    """
    
    class DefinitionType():
        """
        Represents the definition method of a group 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "All", "Defines a group with all nodes or elements"
           "Selected", "Defines a group by selection"
           "DesignArea", "Defines a group refer to design area"
           "MeshSmoothingArea", "Defines a group refer to mesh smoothing area"
        """
        All = 0  # TBSGroupDefinitionDefinitionTypeMemberType
        Selected = 1  # TBSGroupDefinitionDefinitionTypeMemberType
        DesignArea = 2  # TBSGroupDefinitionDefinitionTypeMemberType
        MeshSmoothingArea = 3  # TBSGroupDefinitionDefinitionTypeMemberType
        
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
        
    
    
    class GroupElementType():
        """
        Represents the type of group elements 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Element", "The group contains element"
           "Node", "The group contains node"
        """
        Element = 0  # TBSGroupDefinitionGroupElementTypeMemberType
        Node = 1  # TBSGroupDefinitionGroupElementTypeMemberType
        
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
        
    
    
    def GetElementType(self) -> TBSGroupDefinitionGroupElementType:
        """
        Returns the group element type  
        
        Signature ``GetElementType()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinitionGroupElementType` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    Definition: TBSGroupDefinitionDefinitionType = ...
    """
    Returns or sets  the definition type 
    
    <hr>
    
    Getter Method
    
    Signature ``Definition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinitionDefinitionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Definition`` 
    
    :param definition: 
    :type definition: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinitionDefinitionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TargetSet: NXOpen.CAE.SetManager = ...
    """
    Returns  the target set 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetSet`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.SetManager` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSGroupDefinition = ...  # unknown typename


class TBSLoadCaseManagerSelectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSLoadCaseManagerSelectionType():
    """
    Defines the selection of the loadcase 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Maximum", "Maximum value of the selected load cases"
       "Minimum", "Minimum value of the selected load cases"
       "Sum", "Sum of the selected load cases"
    """
    Maximum = 0  # TBSLoadCaseManagerSelectionTypeMemberType
    Minimum = 1  # TBSLoadCaseManagerSelectionTypeMemberType
    Sum = 2  # TBSLoadCaseManagerSelectionTypeMemberType
    
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
    


class TBSLoadCaseManager(NXOpen.TaggedObject):
    """
    Managers load cases  
    
    .. versionadded:: NX8.0.0
    """
    
    class SelectionType():
        """
        Defines the selection of the loadcase 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Maximum", "Maximum value of the selected load cases"
           "Minimum", "Minimum value of the selected load cases"
           "Sum", "Sum of the selected load cases"
        """
        Maximum = 0  # TBSLoadCaseManagerSelectionTypeMemberType
        Minimum = 1  # TBSLoadCaseManagerSelectionTypeMemberType
        Sum = 2  # TBSLoadCaseManagerSelectionTypeMemberType
        
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
        
    
    
    def GetLoadCases(self) -> 'list[TBSLoadCase]':
        """
        Returns the load cases  
        
        Signature ``GetLoadCases()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetLoadCases(self, loadCases: 'list[TBSLoadCase]') -> None:
        """
        Sets the load cases 
        
        Signature ``SetLoadCases(loadCases)`` 
        
        :param loadCases: 
        :type loadCases: list of :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def AddLoadCases(self, loadCases: 'list[TBSLoadCase]') -> None:
        """
        Adds the load cases 
        
        Signature ``AddLoadCases(loadCases)`` 
        
        :param loadCases: 
        :type loadCases: list of :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def RemoveLoadCases(self, loadCases: 'list[TBSLoadCase]', deleteLoadCase: bool) -> None:
        """
        Removes the load cases 
        
        Signature ``RemoveLoadCases(loadCases, deleteLoadCase)`` 
        
        :param loadCases: 
        :type loadCases: list of :py:class:`NXOpen.CAE.Optimization.TBSLoadCase` 
        :param deleteLoadCase: 
        :type deleteLoadCase: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    SelectionOption: TBSLoadCaseManagerSelectionType = ...
    """
    Returns or sets  the selection option 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSLoadCaseManagerSelectionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SelectionOption`` 
    
    :param selectionOption: 
    :type selectionOption: :py:class:`NXOpen.CAE.Optimization.TBSLoadCaseManagerSelectionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSLoadCaseManager = ...  # unknown typename


class TBSConstraintCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`NXOpen.CAE.Optimization.TBSConstraint`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, constraintName: str) -> TBSConstraint:
        """
        Finds a response constraint with the specified name within an optimization solution  
        
        Signature ``FindObject(constraintName)`` 
        
        :param constraintName: 
        :type constraintName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSConstraint` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    


class TBSDesignVariableCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of :py:class:`CAE.Optimization.TBSDesignVariable`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.TBSOptimizationSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, variableName: str) -> TBSDesignVariable:
        """
        Finds a design variable object with specified name in an optimization solution  
        
        Signature ``FindObject(variableName)`` 
        
        :param variableName: 
        :type variableName: str 
        :returns: 
        :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignVariable` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    


class DAOConstraintCollection(NXOpen.TaggedObjectCollection):
    """
    Represents the collection of optimization solution design constraint   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.DAOSolution`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def FindObject(self, designConstraintName: str) -> DAOConstraint:
        """
        Finds an optimization solution design constraint with a specified name  
        
        Signature ``FindObject(designConstraintName)`` 
        
        :param designConstraintName:  Design constraint name  
        :type designConstraintName: str 
        :returns:  Design constraint  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class SolverMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Solver():
    """
    Represents the optimization solution solver type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Optimization", "Optimization"
       "GlobalSensitivity", "Global sensitivity"
       "AltairHyperOpt", "Altair HyperOpt: Deprecated in NX10"
    """
    Optimization = 0  # SolverMemberType
    GlobalSensitivity = 1  # SolverMemberType
    AltairHyperOpt = 2  # SolverMemberType
    
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
    


class GoalMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Goal():
    """
    Represents the goal type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Minimum", "Minimum value"
       "Maximum", "Maximum value"
       "Target", "Target value"
    """
    Minimum = 0  # GoalMemberType
    Maximum = 1  # GoalMemberType
    Target = 2  # GoalMemberType
    
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
    


class DAODesignVariableBuilderVariableMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DAODesignVariableBuilderVariable():
    """
    Represents the design variable type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionProperty", "Section property variables"
       "ShellProperty", "Shell property variables"
       "FeatureDimension", "Feature dimension variables"
       "SketchDimension", "Sketch dimension variables"
       "AllExpressions", "Variables from FEM, SIM and master part"
       "Count", "Variable type count"
    """
    SectionProperty = 0  # DAODesignVariableBuilderVariableMemberType
    ShellProperty = 1  # DAODesignVariableBuilderVariableMemberType
    FeatureDimension = 2  # DAODesignVariableBuilderVariableMemberType
    SketchDimension = 3  # DAODesignVariableBuilderVariableMemberType
    AllExpressions = 4  # DAODesignVariableBuilderVariableMemberType
    Count = 5  # DAODesignVariableBuilderVariableMemberType
    
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
    


class DAODesignVariableBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.DAOSolutionCollection.CreateDesignVariableBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class Variable():
        """
        Represents the design variable type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionProperty", "Section property variables"
           "ShellProperty", "Shell property variables"
           "FeatureDimension", "Feature dimension variables"
           "SketchDimension", "Sketch dimension variables"
           "AllExpressions", "Variables from FEM, SIM and master part"
           "Count", "Variable type count"
        """
        SectionProperty = 0  # DAODesignVariableBuilderVariableMemberType
        ShellProperty = 1  # DAODesignVariableBuilderVariableMemberType
        FeatureDimension = 2  # DAODesignVariableBuilderVariableMemberType
        SketchDimension = 3  # DAODesignVariableBuilderVariableMemberType
        AllExpressions = 4  # DAODesignVariableBuilderVariableMemberType
        Count = 5  # DAODesignVariableBuilderVariableMemberType
        
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
        
    
    
    def GetVariable(self) -> tuple:
        """
        Gets the design variable 
        
        Signature ``GetVariable()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (variableType, variableExpression). variableType is a :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilderVariable`.   Variable type variableExpression is a :py:class:`NXOpen.Expression`.   Variable expression 
        
        .. versionadded:: NX8.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetVariable(self, variableType: DAODesignVariableBuilderVariable, variableExpression: NXOpen.Expression) -> None:
        """
        Sets the design variable 
        
        Signature ``SetVariable(variableType, variableExpression)`` 
        
        :param variableType:  Variable type  
        :type variableType: :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilderVariable` 
        :param variableExpression:  Variable Expression  
        :type variableExpression: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX8.0.1
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    GlobalSensitivityFlag: bool = ...
    """
    Returns or sets  the flag if mark current design variable as global sensitivity design variable, only effective for global sensitivity optimization type 
    
    <hr>
    
    Getter Method
    
    Signature ``GlobalSensitivityFlag`` 
    
    :returns:  Global sensitivity design variable flag  
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GlobalSensitivityFlag`` 
    
    :param globalSensitivityFlag:  Global sensitivity design variable flag  
    :type globalSensitivityFlag: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LowerLimit: float = ...
    """
    Returns or sets  the lower limit value 
    
    <hr>
    
    Getter Method
    
    Signature ``LowerLimit`` 
    
    :returns:  Lower limit value  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LowerLimit`` 
    
    :param lowerLimit:  Lower limit value  
    :type lowerLimit: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Name: str = ...
    """
    Returns or sets  the design variable name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns:  Design variable name  
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param designVariableName:  Design variable name  
    :type designVariableName: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    UpperLimit: float = ...
    """
    Returns or sets  the upper limit value 
    
    <hr>
    
    Getter Method
    
    Signature ``UpperLimit`` 
    
    :returns:  Upper limit value  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UpperLimit`` 
    
    :param upperLimit:  Upper limit value  
    :type upperLimit: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: DAODesignVariableBuilder = ...  # unknown typename


class NameDescription(NXOpen.TaggedObject):
    """.. versionadded:: NX8.0.0"""
    
    def GetDescription(self) -> 'list[str]':
        """
        Returns the description  
        
        Signature ``GetDescription()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDescription(self, description: 'list[str]') -> None:
        """
        Sets the description 
        
        Signature ``SetDescription(description)`` 
        
        :param description: 
        :type description: list of str 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    Name: str = ...
    """
    Returns or sets  the name 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: NameDescription = ...  # unknown typename


class TBSShapeOptimizationSolution(TBSOptimizationSolution, TBSIOptimizationTest):
    """
    Represents a shape optimization solution   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSShapeOptimizationSolutionBuilder`
    
    .. versionadded:: NX8.5.0
    """
    
    def SolveTest(self) -> None:
        """
        Solves optimization test 
        
        Signature ``SolveTest()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def GetTestResultFile(self) -> str:
        """
        Returns the file name of test result  
        
        Signature ``GetTestResultFile()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    MeshSmooth: TBSMeshSmooth = ...
    """
    Returns  the mesh smooth definition 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSmooth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSMeshSmooth` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    TestFunction: TBSTestFunction = ...
    """
    Returns  the test function 
    
    <hr>
    
    Getter Method
    
    Signature ``TestFunction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTestFunction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Null: TBSShapeOptimizationSolution = ...  # unknown typename


class TBSTopologyControllerOptimizationParametersSpeedMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyControllerOptimizationParametersSpeed():
    """
    Specifies the step size of increment 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "VerySlow", "Very small stepsize"
       "Slow", "Small stepsize"
       "Moderate", "Moderate stepsize"
       "Medium", "Medium stepsize"
       "Fast", "Fast large step size"
       "Iteration", "Step size is modified dynamically so the optimization end after the given number of iterations"
    """
    VerySlow = 0  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    Slow = 1  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    Moderate = 2  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    Medium = 3  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    Fast = 4  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    Iteration = 5  # TBSTopologyControllerOptimizationParametersSpeedMemberType
    
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
    


class TBSTopologyControllerOptimizationParametersVolumeDefinitionMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyControllerOptimizationParametersVolumeDefinitionMethod():
    """
    Represents the definition of volume that can be removed immediatedly in the first design cycle 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Percent", "Specifying the volume in percentage"
       "Absolute", "Specifying the absolute volume"
    """
    Percent = 0  # TBSTopologyControllerOptimizationParametersVolumeDefinitionMethodMemberType
    Absolute = 1  # TBSTopologyControllerOptimizationParametersVolumeDefinitionMethodMemberType
    
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
    


class TBSTopologyControllerOptimizationParametersAutoFrozenMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTopologyControllerOptimizationParametersAutoFrozen():
    """
    Defines the automatic fromzen strategy 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Load", "All loaded elements and nodes are excluded from the optimization"
       "Off", "Loaded elements are optimizable"
       "Spc", "Elements with boundary conditions are excluded from the optimization"
       "Both", "All loaded elements, elements with load nodes with boundary conditions are excluded from the optimization"
    """
    Load = 0  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
    Off = 1  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
    Spc = 2  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
    Both = 3  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
    
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
    


class TBSTopologyControllerOptimizationParameters(TBSOptimizationParameters):
    """
    Represents the parameters to control an optimization in controller strategy   
    
    .. versionadded:: NX8.0.0
    """
    
    class Speed():
        """
        Specifies the step size of increment 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "VerySlow", "Very small stepsize"
           "Slow", "Small stepsize"
           "Moderate", "Moderate stepsize"
           "Medium", "Medium stepsize"
           "Fast", "Fast large step size"
           "Iteration", "Step size is modified dynamically so the optimization end after the given number of iterations"
        """
        VerySlow = 0  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        Slow = 1  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        Moderate = 2  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        Medium = 3  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        Fast = 4  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        Iteration = 5  # TBSTopologyControllerOptimizationParametersSpeedMemberType
        
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
        
    
    
    class VolumeDefinitionMethod():
        """
        Represents the definition of volume that can be removed immediatedly in the first design cycle 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Percent", "Specifying the volume in percentage"
           "Absolute", "Specifying the absolute volume"
        """
        Percent = 0  # TBSTopologyControllerOptimizationParametersVolumeDefinitionMethodMemberType
        Absolute = 1  # TBSTopologyControllerOptimizationParametersVolumeDefinitionMethodMemberType
        
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
        
    
    
    class AutoFrozen():
        """
        Defines the automatic fromzen strategy 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Load", "All loaded elements and nodes are excluded from the optimization"
           "Off", "Loaded elements are optimizable"
           "Spc", "Elements with boundary conditions are excluded from the optimization"
           "Both", "All loaded elements, elements with load nodes with boundary conditions are excluded from the optimization"
        """
        Load = 0  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
        Off = 1  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
        Spc = 2  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
        Both = 3  # TBSTopologyControllerOptimizationParametersAutoFrozenMemberType
        
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
        
    
    AutomaticFrozenOption: TBSTopologyControllerOptimizationParametersAutoFrozen = ...
    """
    Returns or sets  the automatic frozen option 
    
    <hr>
    
    Getter Method
    
    Signature ``AutomaticFrozenOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersAutoFrozen` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutomaticFrozenOption`` 
    
    :param autoFrozen: 
    :type autoFrozen: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersAutoFrozen` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    IterationNumbers: int = ...
    """
    Returns or sets  the number of iterations.  
    
    Only available when :py:meth:`CAE.Optimization.TBSTopologyControllerOptimizationParameters.SpeedOption` is
    :py:class:`CAE.Optimization.TBSTopologyControllerOptimizationParametersSpeed.Iteration <CAE.Optimization.TBSTopologyControllerOptimizationParametersSpeed>` 
    
    <hr>
    
    Getter Method
    
    Signature ``IterationNumbers`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IterationNumbers`` 
    
    :param numIterations: 
    :type numIterations: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    SpeedOption: TBSTopologyControllerOptimizationParametersSpeed = ...
    """
    Returns or sets  the speed size of increment 
    
    <hr>
    
    Getter Method
    
    Signature ``SpeedOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersSpeed` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SpeedOption`` 
    
    :param speedOption: 
    :type speedOption: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersSpeed` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    StartDeleteVolume: float = ...
    """
    Returns or sets  the volume that is deleted in the first design cycle 
    
    <hr>
    
    Getter Method
    
    Signature ``StartDeleteVolume`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartDeleteVolume`` 
    
    :param startDeleteVolume: 
    :type startDeleteVolume: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    VolumeDefinitionOption: TBSTopologyControllerOptimizationParametersVolumeDefinitionMethod = ...
    """
    Returns or sets  the volume definition option 
    
    <hr>
    
    Getter Method
    
    Signature ``VolumeDefinitionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersVolumeDefinitionMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``VolumeDefinitionOption`` 
    
    :param volumeDefinitionOption: 
    :type volumeDefinitionOption: :py:class:`NXOpen.CAE.Optimization.TBSTopologyControllerOptimizationParametersVolumeDefinitionMethod` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSTopologyControllerOptimizationParameters = ...  # unknown typename


class CategoryMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class Category():
    """
    Represents the category type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OneDimension", "1D constraints"
       "TwoDimension", "2D constraints"
       "ThreeDimension", "3D constraints"
       "All", "Model constraints"
    """
    OneDimension = 0  # CategoryMemberType
    TwoDimension = 1  # CategoryMemberType
    ThreeDimension = 2  # CategoryMemberType
    All = 3  # CategoryMemberType
    
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
    


class DAOSolutionCollection(NXOpen.TaggedObjectCollection):
    """
    Represents the collection of optimization solution   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.CAE.Optimization.DAOOptimizationManager`
    
    .. versionadded:: NX8.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateOptimizationBuilder(self, optimizationSolution: DAOSolution) -> DAOSolutionBuilder:
        """
        Creates the builder object of optimization solution  
        
        Signature ``CreateOptimizationBuilder(optimizationSolution)`` 
        
        :param optimizationSolution:  Optimization solution  
        :type optimizationSolution: :py:class:`NXOpen.CAE.Optimization.DAOSolution` 
        :returns:  Optimization solution builder  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOSolutionBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def FindObject(self, solutionName: str) -> DAOSolution:
        """
        Finds an optimization solution with a specified name  
        
        Signature ``FindObject(solutionName)`` 
        
        :param solutionName:  Optimization solution name  
        :type solutionName: str 
        :returns:  Optimization solution  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOSolution` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateConstraintBuilder(self, designConstraint: DAOConstraint) -> DAOConstraintBuilder:
        """
        Creates the builder object of optimization solution design constraint  
        
        Signature ``CreateConstraintBuilder(designConstraint)`` 
        
        :param designConstraint:  Design constraint  
        :type designConstraint: :py:class:`NXOpen.CAE.Optimization.DAOConstraint` 
        :returns:  Design constraint builder  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAOConstraintBuilder` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.CreateConstraintBuilder` instead.
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def CreateDesignVariableBuilder(self, designVariable: DAODesignVariable) -> DAODesignVariableBuilder:
        """
        Creates the builder object of optimization solution design variable  
        
        Signature ``CreateDesignVariableBuilder(designVariable)`` 
        
        :param designVariable:  Design variable  
        :type designVariable: :py:class:`NXOpen.CAE.Optimization.DAODesignVariable` 
        :returns:  Design variable builder  
        :rtype: :py:class:`NXOpen.CAE.Optimization.DAODesignVariableBuilder` 
        
        .. versionadded:: NX8.0.0
        
        .. deprecated::  NX9.0.0
           Use :py:meth:`NXOpen.CAE.Optimization.DAOSolution.CreateDesignVariableBuilder` instead.
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    


class TBSShapeLinkConditionManufacturingOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSShapeLinkConditionManufacturingOption():
    """
    Defines the type of link condition 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PlaneSymmetry", "Plane symmetry referring to the plane which lies perpendicular to the given axis of the coordinate system"
       "RotationSymmetry", "Rotation symmetry definition"
       "SurfaceStamp", "Stampable surface definition"
       "SurfaceTurn", "Turnable surface definition"
       "SurfaceDrill", "Drillable surface definition"
       "SurfaceDemold", "Demold surface definition"
    """
    PlaneSymmetry = 0  # TBSShapeLinkConditionManufacturingOptionMemberType
    RotationSymmetry = 1  # TBSShapeLinkConditionManufacturingOptionMemberType
    SurfaceStamp = 2  # TBSShapeLinkConditionManufacturingOptionMemberType
    SurfaceTurn = 3  # TBSShapeLinkConditionManufacturingOptionMemberType
    SurfaceDrill = 4  # TBSShapeLinkConditionManufacturingOptionMemberType
    SurfaceDemold = 5  # TBSShapeLinkConditionManufacturingOptionMemberType
    
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
    


class TBSShapeLinkCondition(NXOpen.TaggedObject):
    """
    Represents the definition of link condition for shape restriction   
    
    .. versionadded:: NX8.5.0
    """
    
    class ManufacturingOption():
        """
        Defines the type of link condition 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PlaneSymmetry", "Plane symmetry referring to the plane which lies perpendicular to the given axis of the coordinate system"
           "RotationSymmetry", "Rotation symmetry definition"
           "SurfaceStamp", "Stampable surface definition"
           "SurfaceTurn", "Turnable surface definition"
           "SurfaceDrill", "Drillable surface definition"
           "SurfaceDemold", "Demold surface definition"
        """
        PlaneSymmetry = 0  # TBSShapeLinkConditionManufacturingOptionMemberType
        RotationSymmetry = 1  # TBSShapeLinkConditionManufacturingOptionMemberType
        SurfaceStamp = 2  # TBSShapeLinkConditionManufacturingOptionMemberType
        SurfaceTurn = 3  # TBSShapeLinkConditionManufacturingOptionMemberType
        SurfaceDrill = 4  # TBSShapeLinkConditionManufacturingOptionMemberType
        SurfaceDemold = 5  # TBSShapeLinkConditionManufacturingOptionMemberType
        
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
        
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle for repeating segments or demold restrictions 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    DemoldGroup: TBSGroupDefinition = ...
    """
    Returns  the surface nodes of demolding area 
    
    <hr>
    
    Getter Method
    
    Signature ``DemoldGroup`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    Direction: NXOpen.Direction = ...
    """
    Returns or sets  the direction or the axis, which is avaliable when :py:meth:`CAE.Optimization.TBSShapeLinkCondition.ManufacturingType`` is set to 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceStamp <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`, or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceDemold <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`, or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.RotationSymmetry <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`,or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceTurn <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`, or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceDrill <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    ManufacturingType: TBSShapeLinkConditionManufacturingOption = ...
    """
    Returns or sets  the manufacturing type 
    
    <hr>
    
    Getter Method
    
    Signature ``ManufacturingType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSShapeLinkConditionManufacturingOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ManufacturingType`` 
    
    :param manufacturingType: 
    :type manufacturingType: :py:class:`NXOpen.CAE.Optimization.TBSShapeLinkConditionManufacturingOption` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    SymmetryPlane: NXOpen.Plane = ...
    """
    Returns or sets  the symmetry plane, which is only available when :py:meth:`CAE.Optimization.TBSShapeLinkCondition.ManufacturingType`` is set to
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.PlaneSymmetry <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``SymmetryPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SymmetryPlane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Tolerance: NXOpen.Expression = ...
    """
    Returns  the tolerance of symmetrical recognitions 
    
    <hr>
    
    Getter Method
    
    Signature ``Tolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    UndercutTolerance: NXOpen.Expression = ...
    """
    Returns  the undercut tolerance in the demolding area 
    
    <hr>
    
    Getter Method
    
    Signature ``UndercutTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    UseCylindricalCsys: bool = ...
    """
    Returns or sets  the option whether to use cylindrical coordinate system, which is avaliable when:py:meth:`CAE.Optimization.TBSShapeLinkCondition.ManufacturingType`` is set to 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceStamp <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>` 
    
    <hr>
    
    Getter Method
    
    Signature ``UseCylindricalCsys`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseCylindricalCsys`` 
    
    :param useCylindricalCSYS: 
    :type useCylindricalCSYS: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    UseSplineToDefineSurface: bool = ...
    """
    Returns or sets  the option whether to use surface parameters, which is avaliable when:py:meth:`CAE.Optimization.TBSShapeLinkCondition.ManufacturingType`` is set to 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceStamp <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`, or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceTurn <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`, or 
    :py:class:`CAE.Optimization.TBSShapeLinkConditionManufacturingOption.SurfaceDrill <CAE.Optimization.TBSShapeLinkConditionManufacturingOption>`
    
    <hr>
    
    Getter Method
    
    Signature ``UseSplineToDefineSurface`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseSplineToDefineSurface`` 
    
    :param useSurfParam: 
    :type useSurfParam: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSShapeLinkCondition = ...  # unknown typename


class DAOStopCondition(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOStopCondition`.  
    
    .. versionadded:: NX8.0.0
    """
    AbsoluteConvergence: float = ...
    """
    Returns or sets  the absolute convergence 
    
    <hr>
    
    Getter Method
    
    Signature ``AbsoluteConvergence`` 
    
    :returns:  Absolute convergence  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AbsoluteConvergence`` 
    
    :param absoluteConvergence:  Absolute convergence  
    :type absoluteConvergence: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ConstraintChecking: bool = ...
    """
    Returns or sets  the constraint checking flag, only effective for global sensitivity optimization type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintChecking`` 
    
    :returns:  Constraint checking flag  
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintChecking`` 
    
    :param constraintChecking:  Constraint checking flag  
    :type constraintChecking: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    MaxConstraintViolation: float = ...
    """
    Returns or sets  the maximum constraint violation 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxConstraintViolation`` 
    
    :returns:  Maximum constraint violation  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxConstraintViolation`` 
    
    :param constraintViolation:  Maximum constraint violation  
    :type constraintViolation: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    MaxIterations: int = ...
    """
    Returns or sets  the maximum iteration number 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxIterations`` 
    
    :returns:  Step number  
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxIterations`` 
    
    :param stepNumber:  Step number  
    :type stepNumber: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    PerturbationFraction: float = ...
    """
    Returns or sets  the perturbation fraction 
    
    <hr>
    
    Getter Method
    
    Signature ``PerturbationFraction`` 
    
    :returns:  Perturbation fraction  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PerturbationFraction`` 
    
    :param perturbationFraction:  Perturbation fraction  
    :type perturbationFraction: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    RelativeConvergence: float = ...
    """
    Returns or sets  the relative convergence 
    
    <hr>
    
    Getter Method
    
    Signature ``RelativeConvergence`` 
    
    :returns:  Relative convergence  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelativeConvergence`` 
    
    :param relativeConvergence:  Relative convergence  
    :type relativeConvergence: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    SaveAllIterationResults: bool = ...
    """
    Returns or sets  the save all interation results flag 
    
    <hr>
    
    Getter Method
    
    Signature ``SaveAllIterationResults`` 
    
    :returns:  Save all iteration results flag  
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SaveAllIterationResults`` 
    
    :param saveResults:  Save all iteration results flag  
    :type saveResults: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: DAOStopCondition = ...  # unknown typename


class DAOObjective(NXOpen.NXObject):
    """
    Represents a :py:class:`NXOpen.CAE.Optimization.DAOObjective`.  
    
    .. versionadded:: NX8.0.0
    """
    
    def GetGeometry(self) -> 'list[NXOpen.DisplayableObject]':
        """
        Gets the target geometry  
        
        Signature ``GetGeometry()`` 
        
        :returns:  Target geometry  
        :rtype: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetGeometry(self, geometry: 'list[NXOpen.DisplayableObject]') -> None:
        """
        Sets the target geometry 
        
        Signature ``SetGeometry(geometry)`` 
        
        :param geometry:  Target geometry  
        :type geometry: list of :py:class:`NXOpen.DisplayableObject` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
        """
        ...
    
    
    def GetNumberResultGroup(self) -> int:
        """
        Gets the objective result group number  
        
        Signature ``GetNumberResultGroup()`` 
        
        :returns:  Result group number  
        :rtype: int 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResults(self, resultGroupIndex: int) -> 'list[float]':
        """
        Gets the objective results  
        
        Signature ``GetResults(resultGroupIndex)`` 
        
        :param resultGroupIndex:  Result group index  
        :type resultGroupIndex: int 
        :returns:  Objective optimization results  
        :rtype: list of float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    CategoryType: Category = ...
    """
    Returns or sets  the category type 
    
    <hr>
    
    Getter Method
    
    Signature ``CategoryType`` 
    
    :returns:  Category type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Category` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CategoryType`` 
    
    :param categoryType:  Category type  
    :type categoryType: :py:class:`NXOpen.CAE.Optimization.Category` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    GeometryType: Geometry = ...
    """
    Returns or sets  the geometry type 
    
    <hr>
    
    Getter Method
    
    Signature ``GeometryType`` 
    
    :returns:  Geometry type  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Geometry` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``GeometryType`` 
    
    :param geometryType:  Geometry type  
    :type geometryType: :py:class:`NXOpen.CAE.Optimization.Geometry` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    LoadCase: int = ...
    """
    Returns or sets  the frequency load case index 
    
    <hr>
    
    Getter Method
    
    Signature ``LoadCase`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LoadCase`` 
    
    :param loadcase: 
    :type loadcase: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ModeNumber: int = ...
    """
    Returns or sets  the frequency mode number 
    
    <hr>
    
    Getter Method
    
    Signature ``ModeNumber`` 
    
    :returns:  Mode number  
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModeNumber`` 
    
    :param modeNumber:  Mode number  
    :type modeNumber: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ObjectiveGoal: Goal = ...
    """
    Returns or sets  the objective goal 
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectiveGoal`` 
    
    :returns:  Objective goal  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Goal` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ObjectiveGoal`` 
    
    :param objectiveGoal:  Objective goal  
    :type objectiveGoal: :py:class:`NXOpen.CAE.Optimization.Goal` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Response: Response = ...
    """
    Returns or sets  the objective response 
    
    <hr>
    
    Getter Method
    
    Signature ``Response`` 
    
    :returns:  Objective response  
    :rtype: :py:class:`NXOpen.CAE.Optimization.Response` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Response`` 
    
    :param objectiveResponse:  Objective response  
    :type objectiveResponse: :py:class:`NXOpen.CAE.Optimization.Response` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    ResultMeasure: NXOpen.CAE.ResultMeasure = ...
    """
    Returns or sets  the result measure 
    
    <hr>
    
    Getter Method
    
    Signature ``ResultMeasure`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.ResultMeasure` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ResultMeasure`` 
    
    :param resMeas: 
    :type resMeas: :py:class:`NXOpen.CAE.ResultMeasure` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    TargetUnit: NXOpen.Unit = ...
    """
    Returns or sets  the target unit 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetUnit`` 
    
    :returns:  Target unit  
    :rtype: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetUnit`` 
    
    :param targetUnit:  Target unit  
    :type targetUnit: :py:class:`NXOpen.Unit` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    TargetValue: float = ...
    """
    Returns or sets  the target value 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetValue`` 
    
    :returns:  Target value  
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TargetValue`` 
    
    :param targetValue:  Target value  
    :type targetValue: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    """
    Null: DAOObjective = ...  # unknown typename


class TBSStopCondition(NXOpen.TaggedObject):
    """
    Represents the condtion to end an optimization   
    
    .. versionadded:: NX8.0.0
    """
    MaximumIterationNumber: int = ...
    """
    Returns or sets  the maximum number of iteration during the optimization 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumIterationNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumIterationNumber`` 
    
    :param iterationNumber: 
    :type iterationNumber: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSStopCondition = ...  # unknown typename


class TBSTopologyOptimizationSolution(TBSOptimizationSolution):
    """
    Represents the topology optimization solution   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSTopologyOptimizationSolutionBuilder`
    
    .. versionadded:: NX8.0.0
    """
    Null: TBSTopologyOptimizationSolution = ...  # unknown typename


class TBSCastConditionMiddlePlaneTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSCastConditionMiddlePlaneType():
    """
    Defines the middle plane type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No definition of a central plane"
       "Automatic", "Automatica determinaton of the central plane"
       "AutomaticTight", "No holes are generated in the central plane"
       "Point", "A point within the central plane from which the deformation vector is positioned perpendicular to"
       "Surface", "The elements are demolded at the actual surface of the restrict area"
       "Stamp", "The element group is demolded keeping a stampable structure"
    """
    NotSet = 0  # TBSCastConditionMiddlePlaneTypeMemberType
    Automatic = 1  # TBSCastConditionMiddlePlaneTypeMemberType
    AutomaticTight = 2  # TBSCastConditionMiddlePlaneTypeMemberType
    Point = 3  # TBSCastConditionMiddlePlaneTypeMemberType
    Surface = 4  # TBSCastConditionMiddlePlaneTypeMemberType
    Stamp = 5  # TBSCastConditionMiddlePlaneTypeMemberType
    
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
    


class TBSCastCondition(NXOpen.TaggedObject):
    """
    Represents the manufacturing restrictions of :py:class:`NXOpen.CAE.Optimization.TBSTopologyRestrictArea`  
    
    .. versionadded:: NX8.0.0
    """
    
    class MiddlePlaneType():
        """
        Defines the middle plane type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No definition of a central plane"
           "Automatic", "Automatica determinaton of the central plane"
           "AutomaticTight", "No holes are generated in the central plane"
           "Point", "A point within the central plane from which the deformation vector is positioned perpendicular to"
           "Surface", "The elements are demolded at the actual surface of the restrict area"
           "Stamp", "The element group is demolded keeping a stampable structure"
        """
        NotSet = 0  # TBSCastConditionMiddlePlaneTypeMemberType
        Automatic = 1  # TBSCastConditionMiddlePlaneTypeMemberType
        AutomaticTight = 2  # TBSCastConditionMiddlePlaneTypeMemberType
        Point = 3  # TBSCastConditionMiddlePlaneTypeMemberType
        Surface = 4  # TBSCastConditionMiddlePlaneTypeMemberType
        Stamp = 5  # TBSCastConditionMiddlePlaneTypeMemberType
        
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
        
    
    CheckingGroup: TBSGroupDefinition = ...
    """
    Returns  the element group that is used for checking collision of the removed elements 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckingGroup`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DraftAngle: NXOpen.Expression = ...
    """
    Returns  the draft angle 
    
    <hr>
    
    Getter Method
    
    Signature ``DraftAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    MiddlePlane: TBSCastConditionMiddlePlaneType = ...
    """
    Returns or sets  the middle plane 
    
    <hr>
    
    Getter Method
    
    Signature ``MiddlePlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSCastConditionMiddlePlaneType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MiddlePlane`` 
    
    :param middlePlane: 
    :type middlePlane: :py:class:`NXOpen.CAE.Optimization.TBSCastConditionMiddlePlaneType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    MiddlePlanePoint: NXOpen.Point = ...
    """
    Returns or sets  the point within the central plane, only available when :py:meth:`NXOpen.CAE.Optimization.TBSCastCondition.MiddlePlaneType` is 
    :py:class:`CAE.Optimization.TBSCastConditionMiddlePlaneType.Point <CAE.Optimization.TBSCastConditionMiddlePlaneType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``MiddlePlanePoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MiddlePlanePoint`` 
    
    :param middlePlanePoint: 
    :type middlePlanePoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    PullCoordinateSystem: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the coordinate system for the definition of the pull direction 
    
    <hr>
    
    Getter Method
    
    Signature ``PullCoordinateSystem`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PullCoordinateSystem`` 
    
    :param pullCsys: 
    :type pullCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    PullDirection: NXOpen.Direction = ...
    """
    Returns or sets  the pull direction for the element groups in the form of a vector with global coordinate system 
    
    <hr>
    
    Getter Method
    
    Signature ``PullDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PullDirection`` 
    
    :param pullDirection: 
    :type pullDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Radius: NXOpen.Expression = ...
    """
    Returns  the radius value that is used internaly for the collision check during the removal of the elements 
    
    <hr>
    
    Getter Method
    
    Signature ``Radius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSCastCondition = ...  # unknown typename


class TBSTestFunctionDirectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSTestFunctionDirection():
    """
    the direction of test displacements 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Grow", "Standard growth"
       "Shrink", "Standard Shrinkage"
       "Random", "Non-standard nodal random displacement"
    """
    Grow = 0  # TBSTestFunctionDirectionMemberType
    Shrink = 1  # TBSTestFunctionDirectionMemberType
    Random = 2  # TBSTestFunctionDirectionMemberType
    
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
    


class TBSTestFunction(NXOpen.NXObject):
    """
    Represents a test displacement for shape optimization or bead optimization    
    
    .. versionadded:: NX8.5.0
    """
    
    class Direction():
        """
        the direction of test displacements 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Grow", "Standard growth"
           "Shrink", "Standard Shrinkage"
           "Random", "Non-standard nodal random displacement"
        """
        Grow = 0  # TBSTestFunctionDirectionMemberType
        Shrink = 1  # TBSTestFunctionDirectionMemberType
        Random = 2  # TBSTestFunctionDirectionMemberType
        
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
        
    
    MaximumDisplacement: NXOpen.Expression = ...
    """
    Returns  the maximum value of test displacements 
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumDisplacement`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    """
    NumberOfIncrements: int = ...
    """
    Returns or sets  the number of increments 
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfIncrements`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfIncrements`` 
    
    :param incrementsNum: 
    :type incrementsNum: int 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    RunTest: bool = ...
    """
    Returns or sets  the option whether to run test solving 
    
    <hr>
    
    Getter Method
    
    Signature ``RunTest`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RunTest`` 
    
    :param useTestFunction: 
    :type useTestFunction: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TestDirectionOption: TBSTestFunctionDirection = ...
    """
    Returns or sets  the direction of test displacements 
    
    <hr>
    
    Getter Method
    
    Signature ``TestDirectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSTestFunctionDirection` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TestDirectionOption`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.CAE.Optimization.TBSTestFunctionDirection` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Null: TBSTestFunction = ...  # unknown typename


class TBSConstraintBuilderMagnitudeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSConstraintBuilderMagnitudeType():
    """
    Defines the type of constraint value 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Relative", "Constraints could be given in relative values"
       "Absolute", "Constraints could be given in absolute values"
    """
    Relative = 0  # TBSConstraintBuilderMagnitudeTypeMemberType
    Absolute = 1  # TBSConstraintBuilderMagnitudeTypeMemberType
    
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
    


class TBSConstraintBuilderConstraintOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TBSConstraintBuilderConstraintOption():
    """
    Defines the constraint type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Eq", "Value of equality constraint"
       "Lt", "Value of greater or equal constraint"
       "Gt", "Value of less or equal constraint"
    """
    Eq = 0  # TBSConstraintBuilderConstraintOptionMemberType
    Lt = 1  # TBSConstraintBuilderConstraintOptionMemberType
    Gt = 2  # TBSConstraintBuilderConstraintOptionMemberType
    
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
    


class TBSConstraintBuilder(NXOpen.Builder):
    """
    Represents the builder of :py:class:`NXOpen.CAE.Optimization.TBSConstraint`  
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAE.Optimization.TBSOptimizationManager.CreateResponseConstraintBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    class MagnitudeType():
        """
        Defines the type of constraint value 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Relative", "Constraints could be given in relative values"
           "Absolute", "Constraints could be given in absolute values"
        """
        Relative = 0  # TBSConstraintBuilderMagnitudeTypeMemberType
        Absolute = 1  # TBSConstraintBuilderMagnitudeTypeMemberType
        
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
        
    
    
    class ConstraintOption():
        """
        Defines the constraint type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Eq", "Value of equality constraint"
           "Lt", "Value of greater or equal constraint"
           "Gt", "Value of less or equal constraint"
        """
        Eq = 0  # TBSConstraintBuilderConstraintOptionMemberType
        Lt = 1  # TBSConstraintBuilderConstraintOptionMemberType
        Gt = 2  # TBSConstraintBuilderConstraintOptionMemberType
        
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
        
    
    ConstraintType: TBSConstraintBuilderConstraintOption = ...
    """
    Returns or sets  the constraint type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilderConstraintOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintType`` 
    
    :param constraintType: 
    :type constraintType: :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilderConstraintOption` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    ConstraintValue: NXOpen.Expression = ...
    """
    Returns  the constrain value 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    DesignResponse: TBSDesignResponse = ...
    """
    Returns or sets  the design response 
    
    <hr>
    
    Getter Method
    
    Signature ``DesignResponse`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DesignResponse`` 
    
    :param designResponse: 
    :type designResponse: :py:class:`NXOpen.CAE.Optimization.TBSDesignResponse` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    Magnitude: TBSConstraintBuilderMagnitudeType = ...
    """
    Returns or sets  the magnitude type of the constraint 
    
    <hr>
    
    Getter Method
    
    Signature ``Magnitude`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilderMagnitudeType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Magnitude`` 
    
    :param magnitude: 
    :type magnitude: :py:class:`NXOpen.CAE.Optimization.TBSConstraintBuilderMagnitudeType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    NameDescription: NameDescription = ...
    """
    Returns  the name description 
    
    <hr>
    
    Getter Method
    
    Signature ``NameDescription`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.NameDescription` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSConstraintBuilder = ...  # unknown typename


class TBSEigenvalueOptimizationParameters(NXOpen.TaggedObject):
    """
    Represents the parameters to control an eigenvalue optimization   
    
    .. versionadded:: NX8.0.0
    """
    ModeNumber: int = ...
    """
    Returns or sets  the number of modes included in the mode tracking 
    
    <hr>
    
    Getter Method
    
    Signature ``ModeNumber`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ModeNumber`` 
    
    :param modeNumber: 
    :type modeNumber: int 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TrackingMode: bool = ...
    """
    Returns or sets  the switch for mode tracking 
    
    <hr>
    
    Getter Method
    
    Signature ``TrackingMode`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrackingMode`` 
    
    :param trackingMode: 
    :type trackingMode: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
    """
    TrackingNodes: TBSGroupDefinition = ...
    """
    Returns  the tracking nodes, only available when :py:meth:`CAE.Optimization.TBSEigenvalueOptimizationParameters.TrackingMode`` is True 
    
    <hr>
    
    Getter Method
    
    Signature ``TrackingNodes`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CAE.Optimization.TBSGroupDefinition` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    Null: TBSEigenvalueOptimizationParameters = ...  # unknown typename


class TBSSmooth(NXOpen.NXObject):
    """
    Represents the parameters that control the generation of surfaces by optimization   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.CAE.Optimization.TBSSmoothBuilder`
    
    .. versionadded:: NX8.0.0
    """
    
    def Execute(self) -> None:
        """
        Executes the surface generation 
        
        Signature ``Execute()`` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    
    def Rename(self, name: str, renameResults: bool) -> None:
        """
        Rename smooth and optionally rename associated results files 
        
        Signature ``Rename(name, renameResults)`` 
        
        :param name:  new solution name  
        :type name: str 
        :param renameResults:  true if you what associated results files to be renamed as well   
        :type renameResults: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetResults(self) -> 'list[str]':
        """
        Returns the result file name and status for the smoothing setting  
        
        Signature ``GetResults()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def Destroy(self, deleteResult: bool) -> None:
        """
        Deletes a smooth and the associated result file optional 
        
        Signature ``Destroy(deleteResult)`` 
        
        :param deleteResult:   true if you want associated result files to be deleted as well  
        :type deleteResult: bool 
        
        .. versionadded:: NX8.0.0
        
        License requirements: cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization")
        """
        ...
    
    Null: TBSSmooth = ...  # unknown typename


