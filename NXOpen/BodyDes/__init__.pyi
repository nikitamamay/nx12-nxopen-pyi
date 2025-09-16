# module 'NXOpen.BodyDes'
#
# Automatically generated 2025-06-09T14:38:43.683629
#
"""Default documentation for NXOpen.BodyDes."""

import typing

import NXOpen
import NXOpen.Features



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class OnestepUnformBuilderProcessMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderProcess():
    """
    The process types of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "EntireUnform", "entire"
       "IntermediateUnform", "intermediate"
       "AdvancedUnform", "spring back"
       "TrimLine", "trim line"
    """
    EntireUnform = 0  # OnestepUnformBuilderProcessMemberType
    IntermediateUnform = 1  # OnestepUnformBuilderProcessMemberType
    AdvancedUnform = 2  # OnestepUnformBuilderProcessMemberType
    TrimLine = 3  # OnestepUnformBuilderProcessMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderObjectMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderObject():
    """
    The object types of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Solid", "solid"
       "Face", "face"
    """
    Solid = 0  # OnestepUnformBuilderObjectMemberType
    Face = 1  # OnestepUnformBuilderObjectMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderConstraintMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderConstraint():
    """
    The constraints of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CurveToCurve", "Curve to Curve Constraint, used for intermediate unform only"
       "PointToPoint", "Point to Point Constraint, used for complete unform only"
       "CurveAlongCurve", "Curve along Curve Constraint, used for complete unform only"
    """
    CurveToCurve = 0  # OnestepUnformBuilderConstraintMemberType
    PointToPoint = 1  # OnestepUnformBuilderConstraintMemberType
    CurveAlongCurve = 2  # OnestepUnformBuilderConstraintMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderPartMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderPart():
    """
    The part types of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "WithAddendum", "part with addendum"
       "WithoutAddendum", "part without addendum"
    """
    WithAddendum = 0  # OnestepUnformBuilderPartMemberType
    WithoutAddendum = 1  # OnestepUnformBuilderPartMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderSurfaceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderSurface():
    """
    The surface types of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inner", "Onestep solver will offset inner surface and enlarge it"
       "Middle", "Onestep solver will not offset middle surface"
       "Outer", "Onestep solver will offset outer surface and shrink it"
    """
    Inner = 0  # OnestepUnformBuilderSurfaceMemberType
    Middle = 1  # OnestepUnformBuilderSurfaceMemberType
    Outer = 2  # OnestepUnformBuilderSurfaceMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderMeshElementMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderMeshElement():
    """
    The 2-D mesh element type of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Triangle", "Generate 2D triangle mesh element"
       "Quadrate", "Generate 2D quadrate mesh element"
    """
    Triangle = 0  # OnestepUnformBuilderMeshElementMemberType
    Quadrate = 1  # OnestepUnformBuilderMeshElementMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderConvergencyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderConvergency():
    """
    The solver convergency level of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Low", "Onestep solver convergency level is low"
       "Medium", "Onestep solver convergency level is medium"
       "High", "Onestep solver convergency level is high"
    """
    Low = 0  # OnestepUnformBuilderConvergencyMemberType
    Medium = 1  # OnestepUnformBuilderConvergencyMemberType
    High = 2  # OnestepUnformBuilderConvergencyMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderDisplaySpringbackModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderDisplaySpringbackMode():
    """
    The mode of display springback. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Displacement", "Onestep display springback mode is displacement"
       "Alongx", "Onestep display springback mode is along X"
       "Alongy", "Onestep display springback mode is along Y"
       "Alongz", "Onestep display springback mode is along Z"
    """
    Displacement = 0  # OnestepUnformBuilderDisplaySpringbackModeMemberType
    Alongx = 1  # OnestepUnformBuilderDisplaySpringbackModeMemberType
    Alongy = 2  # OnestepUnformBuilderDisplaySpringbackModeMemberType
    Alongz = 3  # OnestepUnformBuilderDisplaySpringbackModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilderUnfoldModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OnestepUnformBuilderUnfoldMode():
    """
    The Onesetp unfold mode of onestep unform. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Complete", "Onestep unfold mode is complete"
       "Intermediate", "Onestep unfold mode is intermediate"
       "Trimline", "Onestep unfold mode is trimline"
       "Unknown", "Onestep unfold mode is unknown"
    """
    Complete = 0  # OnestepUnformBuilderUnfoldModeMemberType
    Intermediate = 1  # OnestepUnformBuilderUnfoldModeMemberType
    Trimline = 2  # OnestepUnformBuilderUnfoldModeMemberType
    Unknown = 3  # OnestepUnformBuilderUnfoldModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OnestepUnformBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.BodyDes.OnestepUnformBuilder`.  
    
    This allows the creation of an Onestep Unform.
    
    To create a new instance of this class, use :py:meth:`NXOpen.BodyDes.OnestepUnformCollection.CreateOnestepBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class Process():
        """
        The process types of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "EntireUnform", "entire"
           "IntermediateUnform", "intermediate"
           "AdvancedUnform", "spring back"
           "TrimLine", "trim line"
        """
        EntireUnform = 0  # OnestepUnformBuilderProcessMemberType
        IntermediateUnform = 1  # OnestepUnformBuilderProcessMemberType
        AdvancedUnform = 2  # OnestepUnformBuilderProcessMemberType
        TrimLine = 3  # OnestepUnformBuilderProcessMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Object():
        """
        The object types of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Solid", "solid"
           "Face", "face"
        """
        Solid = 0  # OnestepUnformBuilderObjectMemberType
        Face = 1  # OnestepUnformBuilderObjectMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Constraint():
        """
        The constraints of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CurveToCurve", "Curve to Curve Constraint, used for intermediate unform only"
           "PointToPoint", "Point to Point Constraint, used for complete unform only"
           "CurveAlongCurve", "Curve along Curve Constraint, used for complete unform only"
        """
        CurveToCurve = 0  # OnestepUnformBuilderConstraintMemberType
        PointToPoint = 1  # OnestepUnformBuilderConstraintMemberType
        CurveAlongCurve = 2  # OnestepUnformBuilderConstraintMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Part():
        """
        The part types of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "WithAddendum", "part with addendum"
           "WithoutAddendum", "part without addendum"
        """
        WithAddendum = 0  # OnestepUnformBuilderPartMemberType
        WithoutAddendum = 1  # OnestepUnformBuilderPartMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Surface():
        """
        The surface types of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inner", "Onestep solver will offset inner surface and enlarge it"
           "Middle", "Onestep solver will not offset middle surface"
           "Outer", "Onestep solver will offset outer surface and shrink it"
        """
        Inner = 0  # OnestepUnformBuilderSurfaceMemberType
        Middle = 1  # OnestepUnformBuilderSurfaceMemberType
        Outer = 2  # OnestepUnformBuilderSurfaceMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MeshElement():
        """
        The 2-D mesh element type of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Triangle", "Generate 2D triangle mesh element"
           "Quadrate", "Generate 2D quadrate mesh element"
        """
        Triangle = 0  # OnestepUnformBuilderMeshElementMemberType
        Quadrate = 1  # OnestepUnformBuilderMeshElementMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Convergency():
        """
        The solver convergency level of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Low", "Onestep solver convergency level is low"
           "Medium", "Onestep solver convergency level is medium"
           "High", "Onestep solver convergency level is high"
        """
        Low = 0  # OnestepUnformBuilderConvergencyMemberType
        Medium = 1  # OnestepUnformBuilderConvergencyMemberType
        High = 2  # OnestepUnformBuilderConvergencyMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DisplaySpringbackMode():
        """
        The mode of display springback. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Displacement", "Onestep display springback mode is displacement"
           "Alongx", "Onestep display springback mode is along X"
           "Alongy", "Onestep display springback mode is along Y"
           "Alongz", "Onestep display springback mode is along Z"
        """
        Displacement = 0  # OnestepUnformBuilderDisplaySpringbackModeMemberType
        Alongx = 1  # OnestepUnformBuilderDisplaySpringbackModeMemberType
        Alongy = 2  # OnestepUnformBuilderDisplaySpringbackModeMemberType
        Alongz = 3  # OnestepUnformBuilderDisplaySpringbackModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class UnfoldMode():
        """
        The Onesetp unfold mode of onestep unform. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Complete", "Onestep unfold mode is complete"
           "Intermediate", "Onestep unfold mode is intermediate"
           "Trimline", "Onestep unfold mode is trimline"
           "Unknown", "Onestep unfold mode is unknown"
        """
        Complete = 0  # OnestepUnformBuilderUnfoldModeMemberType
        Intermediate = 1  # OnestepUnformBuilderUnfoldModeMemberType
        Trimline = 2  # OnestepUnformBuilderUnfoldModeMemberType
        Unknown = 3  # OnestepUnformBuilderUnfoldModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    def SetDrawDirection(self) -> None:
        """Returns or sets  the draw direction used to define the normal of unform base plane."""
        ...
    
    @typing.overload
    def SetDrawDirection(self, drawDirection: NXOpen.Direction) -> None:
        """
        Getter Method
        
        Signature ``DrawDirection`` 
        
        :param drawDirection: 
        :type drawDirection: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    @typing.overload
    def SetDrawDirection(self, drawDirection: NXOpen.Direction) -> None:
        """
        Setter Method
        
        Signature ``DrawDirection`` 
        
        :param drawDirection: 
        :type drawDirection: :py:class:`NXOpen.Direction` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    @typing.overload
    def SetDrawDirection(self, tdx: int, tdy: int, tdz: int) -> None:
        """
        Sets the unform draw direction. 
        
        Signature ``SetDrawDirection(tdx, tdy, tdz)`` 
        
        :param tdx: 
        :type tdx: int 
        :param tdy: 
        :type tdy: int 
        :param tdz: 
        :type tdz: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    @typing.overload
    def SetSurfaceType(self) -> None:
        """Returns or sets  the surface type used to determine offset direction."""
        ...
    
    @typing.overload
    def SetSurfaceType(self, surfaceType: OnestepUnformBuilderSurface) -> None:
        """
        Getter Method
        
        Signature ``SurfaceType`` 
        
        :param surfaceType: 
        :type surfaceType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    @typing.overload
    def SetSurfaceType(self, surfaceType: OnestepUnformBuilderSurface) -> None:
        """
        Setter Method
        
        Signature ``SurfaceType`` 
        
        :param surfaceType: 
        :type surfaceType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderSurface` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    @typing.overload
    def SetSurfaceType(self, tOnestepSolverSurfaceType: int) -> None:
        """
        Sets the unform surface type. 
        
        Signature ``SetSurfaceType(tOnestepSolverSurfaceType)`` 
        
        :param tOnestepSolverSurfaceType: 
        :type tOnestepSolverSurfaceType: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    @typing.overload
    def GetThickness(self) -> None:
        """Returns or sets  the thickness of sheet metal model."""
        ...
    
    @typing.overload
    def GetThickness(self) -> float:
        """
        Getter Method
        
        Signature ``Thickness`` 
        
        :returns: 
        :rtype: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetThickness(self, thickness: float) -> None:
        """
        Setter Method
        
        Signature ``Thickness`` 
        
        :param thickness: 
        :type thickness: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    @typing.overload
    def GetThickness(self) -> 'list[float]':
        """
        Gets Thickness. 
        
        Signature ``GetThickness()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def Mesh(self) -> None:
        """
        Create FEM 2-D meshes based on the unform region surfaces and the target region surfaces.  
        
        Signature ``Mesh()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def Calculation(self) -> None:
        """
        Starts solver to calculate.  
        
        Signature ``Calculation()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def Constructor(self, tOnestepSolverType: int) -> None:
        """
        Constructs solver to prepare the data.  
        
        Signature ``Constructor(tOnestepSolverType)`` 
        
        :param tOnestepSolverType: 
        :type tOnestepSolverType: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def Destructor(self) -> None:
        """
        Destructs solver to release the data.  
        
        Signature ``Destructor()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetSolverType(self) -> int:
        """
        Gets the solver calculation type.  
        
        Signature ``GetSolverType()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetBlankThickness(self, thickness: float) -> None:
        """
        Sets the blank thickness.  
        
        Signature ``SetBlankThickness(thickness)`` 
        
        :param thickness: 
        :type thickness: float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetRefNode(self) -> int:
        """
        Gets the reference node ID.  
        
        Signature ``GetRefNode()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetMinNodeID(self) -> int:
        """
        Gets the minimum node ID.  
        
        Signature ``GetMinNodeID()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetNodeIDsOnFreeEdge(self, index: 'list[int]', nids: 'list[int]') -> None:
        """
        Sets the node IDs on the free edges (non-constrainted boundary edges).  
        
        Signature ``SetNodeIDsOnFreeEdge(index, nids)`` 
        
        :param index: 
        :type index: list of int 
        :param nids: 
        :type nids: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetNodeIdsOnFreeEdge(self) -> tuple:
        """
        Gets the node IDs on the free edges (non-constrainted boundary edges).  
        
        Signature ``GetNodeIdsOnFreeEdge()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (index, nodeIdentifications). index is a list of int. nodeIdentifications is a list of int. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetMeshes(self) -> tuple:
        """
        Gets the mesh element data.  
        
        Signature ``GetMeshes()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (vnode, constraintId, element). vnode is a list of float. constraintId is a list of int. element is a list of int. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetBlankShape(self) -> 'list[float]':
        """
        Gets the blank result nodes.  
        
        Signature ``GetBlankShape()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetStrain(self) -> 'list[float]':
        """
        Gets the strain result.  
        
        Signature ``GetStrain()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetStress(self) -> 'list[float]':
        """
        Gets the stress result.  
        
        Signature ``GetStress()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetSpringbackShape(self) -> 'list[float]':
        """
        Gets the springbrack result.  
        
        Signature ``GetSpringbackShape()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetTopSurfaceStress(self) -> 'list[float]':
        """
        Gets the top surface stress result.  
        
        Signature ``GetTopSurfaceStress()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetTopSurfaceStrain(self) -> 'list[float]':
        """
        Gets the top surface strain result.  
        
        Signature ``GetTopSurfaceStrain()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetBottomSurfaceStress(self) -> 'list[float]':
        """
        Gets the bottom surface stress result.  
        
        Signature ``GetBottomSurfaceStress()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetBottomSurfaceStrain(self) -> 'list[float]':
        """
        Gets the bottom surface strain result.  
        
        Signature ``GetBottomSurfaceStrain()`` 
        
        :returns: 
        :rtype: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def IsResultExist(self) -> None:
        """
        Checks whether the result is available or not.  
        
        Signature ``IsResultExist()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetBorderInfo(self, edgeTags: 'list[NXOpen.TaggedObject]', nids: 'list[int]', groupInfo: 'list[int]') -> None:
        """
        Sets the boundary condition information.  
        
        Signature ``SetBorderInfo(edgeTags, nids, groupInfo)`` 
        
        :param edgeTags:  Objects to be checked 
        :type edgeTags: list of :py:class:`NXOpen.TaggedObject` 
        :param nids: 
        :type nids: list of int 
        :param groupInfo: 
        :type groupInfo: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def UpdateInputMeshDataToSolver(self) -> None:
        """
        Updates the mesh elements to solver.  
        
        Signature ``UpdateInputMeshDataToSolver()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetBorderLoops(self) -> tuple:
        """
        Gets the boundary loop IDs.  
        
        Signature ``GetBorderLoops()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (index, nodeIdentifications). index is a list of int. nodeIdentifications is a list of int. 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def OnestepUnformRegisterProjectCallback(self) -> None:
        """
        Register the callback to solver.  
        
        Signature ``OnestepUnformRegisterProjectCallback()`` 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def DisplayProfile(self, readResultFromFeature: bool) -> None:
        """
        Displays profile result.  
        
        Signature ``DisplayProfile(readResultFromFeature)`` 
        
        :param readResultFromFeature: 
        :type readResultFromFeature: bool 
        
        .. versionadded:: NX8.5.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateSheetBody(self, readResultFromFeature: bool) -> None:
        """
        Creates unform sheet body result.  
        
        Signature ``CreateSheetBody(readResultFromFeature)`` 
        
        :param readResultFromFeature: 
        :type readResultFromFeature: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetResultThickness(self, thickness: 'list[float]') -> None:
        """
        Sets thickness result.  
        
        Signature ``SetResultThickness(thickness)`` 
        
        :param thickness: 
        :type thickness: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultStrain(self, strain: 'list[float]') -> None:
        """
        Sets strain result.  
        
        Signature ``SetResultStrain(strain)`` 
        
        :param strain: 
        :type strain: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultStress(self, stress: 'list[float]') -> None:
        """
        Sets stress result.  
        
        Signature ``SetResultStress(stress)`` 
        
        :param stress: 
        :type stress: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultSpringBack(self, springback: 'list[float]') -> None:
        """
        Sets springback result.  
        
        Signature ``SetResultSpringBack(springback)`` 
        
        :param springback: 
        :type springback: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultBlankShape(self, blankshape: 'list[float]') -> None:
        """
        Sets blank shape result.  
        
        Signature ``SetResultBlankShape(blankshape)`` 
        
        :param blankshape: 
        :type blankshape: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultNodesIdsOnProfile(self, nids: 'list[int]') -> None:
        """
        Sets profile node ID result.  
        
        Signature ``SetResultNodesIdsOnProfile(nids)`` 
        
        :param nids: 
        :type nids: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultNodesNumEachProfileCurve(self, indexs: 'list[int]') -> None:
        """
        Sets total number of node on each profile.  
        
        Signature ``SetResultNodesNumEachProfileCurve(indexs)`` 
        
        :param indexs: 
        :type indexs: list of int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetResultRefNodeId(self, resultRefNodeId: int) -> None:
        """
        Sets reference node ID.  
        
        Signature ``SetResultRefNodeId(resultRefNodeId)`` 
        
        :param resultRefNodeId: 
        :type resultRefNodeId: int 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetConstraintInformation(self, noCommonEdges: bool, revisedDirU: 'list[int]', revisedDirT: 'list[int]', index: 'list[int]', constraintType: 'list[int]', cacNumsUnform: 'list[int]', cacNumsTarget: 'list[int]', consCurveFromUnform: 'list[NXOpen.TaggedObject]', consCurveFromTarget: 'list[NXOpen.TaggedObject]', consPointFromUnform: 'list[NXOpen.Point]', consPointFromTarget: 'list[NXOpen.Point]', startPtOfConsCrvsUnform: 'list[float]', startPtOfConsCrvsTarget: 'list[float]') -> None:
        """
        Set constraint information.  
        
        Signature ``SetConstraintInformation(noCommonEdges, revisedDirU, revisedDirT, index, constraintType, cacNumsUnform, cacNumsTarget, consCurveFromUnform, consCurveFromTarget, consPointFromUnform, consPointFromTarget, startPtOfConsCrvsUnform, startPtOfConsCrvsTarget)`` 
        
        :param noCommonEdges: 
        :type noCommonEdges: bool 
        :param revisedDirU: 
        :type revisedDirU: list of int 
        :param revisedDirT: 
        :type revisedDirT: list of int 
        :param index: 
        :type index: list of int 
        :param constraintType: 
        :type constraintType: list of int 
        :param cacNumsUnform: 
        :type cacNumsUnform: list of int 
        :param cacNumsTarget: 
        :type cacNumsTarget: list of int 
        :param consCurveFromUnform:  Objects to be checked 
        :type consCurveFromUnform: list of :py:class:`NXOpen.TaggedObject` 
        :param consCurveFromTarget:  Objects to be checked 
        :type consCurveFromTarget: list of :py:class:`NXOpen.TaggedObject` 
        :param consPointFromUnform:  Objects to be checked 
        :type consPointFromUnform: list of :py:class:`NXOpen.Point` 
        :param consPointFromTarget:  Objects to be checked 
        :type consPointFromTarget: list of :py:class:`NXOpen.Point` 
        :param startPtOfConsCrvsUnform: 
        :type startPtOfConsCrvsUnform: list of float 
        :param startPtOfConsCrvsTarget: 
        :type startPtOfConsCrvsTarget: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetAdvancedConstraintInformation(self, advancedConstraintPartType: int, blankHolderWithAddendumBinderRegion: 'list[NXOpen.TaggedObject]', blankHolderWithoutAddendumBoundaryOfPart: 'list[NXOpen.TaggedObject]', blankHolderWithAddendumPressure: float, blankHolderWithAddendumForce: float, blankHolderWithoutAddendumTension: float, blankHolderWithoutAddendumForce: float, blankHolderWithoutAddendumForceStrength: float, drawbeadTag: 'list[NXOpen.TaggedObject]', drawbeadTtension: 'list[float]', drawbeadNtension: 'list[float]', drawbeadForceStrength: 'list[float]') -> None:
        """
        Set advanced constraint information.  
        
        Signature ``SetAdvancedConstraintInformation(advancedConstraintPartType, blankHolderWithAddendumBinderRegion, blankHolderWithoutAddendumBoundaryOfPart, blankHolderWithAddendumPressure, blankHolderWithAddendumForce, blankHolderWithoutAddendumTension, blankHolderWithoutAddendumForce, blankHolderWithoutAddendumForceStrength, drawbeadTag, drawbeadTtension, drawbeadNtension, drawbeadForceStrength)`` 
        
        :param advancedConstraintPartType: 
        :type advancedConstraintPartType: int 
        :param blankHolderWithAddendumBinderRegion:  Objects to be checked 
        :type blankHolderWithAddendumBinderRegion: list of :py:class:`NXOpen.TaggedObject` 
        :param blankHolderWithoutAddendumBoundaryOfPart:  Objects to be checked 
        :type blankHolderWithoutAddendumBoundaryOfPart: list of :py:class:`NXOpen.TaggedObject` 
        :param blankHolderWithAddendumPressure: 
        :type blankHolderWithAddendumPressure: float 
        :param blankHolderWithAddendumForce: 
        :type blankHolderWithAddendumForce: float 
        :param blankHolderWithoutAddendumTension: 
        :type blankHolderWithoutAddendumTension: float 
        :param blankHolderWithoutAddendumForce: 
        :type blankHolderWithoutAddendumForce: float 
        :param blankHolderWithoutAddendumForceStrength: 
        :type blankHolderWithoutAddendumForceStrength: float 
        :param drawbeadTag:  Objects to be checked 
        :type drawbeadTag: list of :py:class:`NXOpen.TaggedObject` 
        :param drawbeadTtension: 
        :type drawbeadTtension: list of float 
        :param drawbeadNtension: 
        :type drawbeadNtension: list of float 
        :param drawbeadForceStrength: 
        :type drawbeadForceStrength: list of float 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContactNodeIds(self) -> 'list[int]':
        """
        Gets the element node IDs where the product face meshes and addendum faces mesh are contacting within the given tolerance.  
        
        Signature ``GetContactNodeIds()`` 
        
        :returns: 
        :rtype: list of int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetFacesOnOffsetSheet(self, unfoldBody: NXOpen.Body) -> bool:
        """
        Sets the offset faces when the object type is body.  
        
        Signature ``SetFacesOnOffsetSheet(unfoldBody)`` 
        
        :param unfoldBody: 
        :type unfoldBody: :py:class:`NXOpen.Body` 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    BinderRegion: NXOpen.ScCollector = ...
    """
    Returns  the binder region which is a group of faces user chooses as holder.  
    
    <hr>
    
    Getter Method
    
    Signature ``BinderRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ConstraintType: OnestepUnformBuilderConstraint = ...
    """
    Returns or sets  the constraint type for intermediate unform or complete unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderConstraint` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintType`` 
    
    :param constraintType: 
    :type constraintType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderConstraint` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ContactPointsTolerance: float = ...
    """
    Returns or sets  the tolerance to find contact points.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContactPointsTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContactPointsTolerance`` 
    
    :param tolerance: 
    :type tolerance: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    DrawDirection: NXOpen.Direction = ...
    """
    Returns or sets  the draw direction used to define the normal of unform base plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``DrawDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DrawDirection`` 
    
    :param drawDirection: 
    :type drawDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Force: float = ...
    """
    Returns or sets  the force on blank holder.  
    
    <hr>
    
    Getter Method
    
    Signature ``Force`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Force`` 
    
    :param force: 
    :type force: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ForceStrength: float = ...
    """
    Returns or sets  the force strength on blank holder.  
    
    <hr>
    
    Getter Method
    
    Signature ``ForceStrength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ForceStrength`` 
    
    :param forceStrength: 
    :type forceStrength: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal")
    """
    InferElementSize: bool = ...
    """
    Returns or sets  the option to infer 2-D element size.  
    
    If it is true, the element size will be auto-detected. If it is false, the element size will be required as input. 
    
    <hr>
    
    Getter Method
    
    Signature ``InferElementSize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferElementSize`` 
    
    :param inforElementSize: 
    :type inforElementSize: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    InferThickness: bool = ...
    """
    Returns or sets  the option to infer thickness.  
    
    If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.
    
    <hr>
    
    Getter Method
    
    Signature ``InferThickness`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferThickness`` 
    
    :param inferThickness: 
    :type inferThickness: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MatchPointOne: NXOpen.Point = ...
    """
    Returns or sets  the first match point for spring back calculation.  
    
    <hr>
    
    Getter Method
    
    Signature ``MatchPointOne`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MatchPointOne`` 
    
    :param matchPointOne: 
    :type matchPointOne: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MatchPointThree: NXOpen.Point = ...
    """
    Returns or sets  the third match point for spring back calculation.  
    
    <hr>
    
    Getter Method
    
    Signature ``MatchPointThree`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MatchPointThree`` 
    
    :param matchPointThree: 
    :type matchPointThree: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MatchPointTwo: NXOpen.Point = ...
    """
    Returns or sets  the second match point for spring back calculation.  
    
    <hr>
    
    Getter Method
    
    Signature ``MatchPointTwo`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MatchPointTwo`` 
    
    :param matchPointTwo: 
    :type matchPointTwo: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyDensity: float = ...
    """
    Returns or sets  the density of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyDensity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyDensity`` 
    
    :param materialPropertyDensity: 
    :type materialPropertyDensity: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyE: float = ...
    """
    Returns or sets  the material property elasticity(E) which enables a material to return to its original shape and dimension.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyE`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyE`` 
    
    :param materialPropertyE: 
    :type materialPropertyE: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyF: float = ...
    """
    Returns or sets  the friction of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyF`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyF`` 
    
    :param materialPropertyF: 
    :type materialPropertyF: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyInitialStrain: float = ...
    """
    Returns or sets  the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyInitialStrain`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyInitialStrain`` 
    
    :param materialPropertyInitialStrain: 
    :type materialPropertyInitialStrain: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyK: float = ...
    """
    Returns or sets  the K(Strength Coefficient) of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyK`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyK`` 
    
    :param materialPropertyK: 
    :type materialPropertyK: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyN: float = ...
    """
    Returns or sets  the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyN`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyN`` 
    
    :param materialPropertyN: 
    :type materialPropertyN: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyPoisson: float = ...
    """
    Returns or sets  the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyPoisson`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyPoisson`` 
    
    :param materialPropertyPoisson: 
    :type materialPropertyPoisson: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyR0: float = ...
    """
    Returns or sets  the r0(Anisotropy Coefficient) of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyR0`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyR0`` 
    
    :param materialPropertyR0: 
    :type materialPropertyR0: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyR45: float = ...
    """
    Returns or sets  the r45(Anisotropy Coefficient) of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyR45`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyR45`` 
    
    :param materialPropertyR45: 
    :type materialPropertyR45: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyR90: float = ...
    """
    Returns or sets  the r90(Anisotropy Coefficient) of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyR90`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyR90`` 
    
    :param materialPropertyR90: 
    :type materialPropertyR90: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MaterialPropertyYieldStress: float = ...
    """
    Returns or sets  the yield stress of material.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialPropertyYieldStress`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialPropertyYieldStress`` 
    
    :param materialPropertyYieldStress: 
    :type materialPropertyYieldStress: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshAttemptMapping: bool = ...
    """
    Returns or sets  the option to attemp mapping for mesh elements.  
    
    If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping. 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshAttemptMapping`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshAttemptMapping`` 
    
    :param meshAttemptMapping: 
    :type meshAttemptMapping: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshElementSize: float = ...
    """
    Returns or sets  the 2-D element size for mesh.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshElementSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshElementSize`` 
    
    :param meshElementSize: 
    :type meshElementSize: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshElementType: OnestepUnformBuilderMeshElement = ...
    """
    Returns or sets  the 2-D mesh element type, either triangle or quadrate element.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshElementType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderMeshElement` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshElementType`` 
    
    :param meshElementType: 
    :type meshElementType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderMeshElement` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshMaxJacobian: float = ...
    """
    Returns or sets  the maximum Jacobian for mesh elements.  
    
    It is used to control the element shape and quality. 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshMaxJacobian`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshMaxJacobian`` 
    
    :param meshMaxJacobian: 
    :type meshMaxJacobian: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshMaxWarp: float = ...
    """
    Returns or sets  the maximum warp for meshing.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshMaxWarp`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshMaxWarp`` 
    
    :param meshMaxWarp: 
    :type meshMaxWarp: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshProcessFillet: bool = ...
    """
    Returns or sets  the option to process fillet for mesh element.  
    
    If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed. 
    
    <hr>
    
    Getter Method
    
    Signature ``MeshProcessFillet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshProcessFillet`` 
    
    :param meshProcessFillet: 
    :type meshProcessFillet: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshSizeVariation: int = ...
    """
    Returns or sets  the variation of mesh element size.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSizeVariation`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshSizeVariation`` 
    
    :param meshSizeVariation: 
    :type meshSizeVariation: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshSmallFeature: float = ...
    """
    Returns or sets  the value of small feature for mesh setting
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSmallFeature`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshSmallFeature`` 
    
    :param meshSmallFeature: 
    :type meshSmallFeature: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    MeshSplitQuad: bool = ...
    """
    Returns or sets  the option to split quadrate element to triangle element when creating meshes.  
    
    <hr>
    
    Getter Method
    
    Signature ``MeshSplitQuad`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MeshSplitQuad`` 
    
    :param meshSplitQuad: 
    :type meshSplitQuad: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ObjectType: OnestepUnformBuilderObject = ...
    """
    Returns or sets  the object type for onestep unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``ObjectType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ObjectType`` 
    
    :param objectType: 
    :type objectType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderObject` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    PartBoundary: NXOpen.ScCollector = ...
    """
    Returns  the boundary which is a group of edges user chooses to apply on equivalent force.  
    
    <hr>
    
    Getter Method
    
    Signature ``PartBoundary`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PartType: OnestepUnformBuilderPart = ...
    """
    Returns or sets  the part type for onestep unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``PartType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderPart` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PartType`` 
    
    :param partType: 
    :type partType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderPart` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Pressure: float = ...
    """
    Returns or sets  the pressure on blank holder.  
    
    <hr>
    
    Getter Method
    
    Signature ``Pressure`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Pressure`` 
    
    :param pressure: 
    :type pressure: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ProcessType: OnestepUnformBuilderProcess = ...
    """
    Returns or sets  the process type for onestep unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProcessType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderProcess` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProcessType`` 
    
    :param processType: 
    :type processType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderProcess` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplayFlattenShape: bool = ...
    """
    Returns or sets  the option to display result flatten shape in report.  
    
    If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplayFlattenShape`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplayFlattenShape`` 
    
    :param reportDisplayFlattenShape: 
    :type reportDisplayFlattenShape: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplaySpringback: bool = ...
    """
    Returns or sets  the option to display springback result in report.  
    
    If it is true, the report will display springback result. If it is false, the springback will not be displayed.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplaySpringback`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplaySpringback`` 
    
    :param reportDisplaySpringback: 
    :type reportDisplaySpringback: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplayStrain: bool = ...
    """
    Returns or sets  the option to display strain in report.  
    
    If it is true, the report will display strain information. If it is false, the report will not display strain information.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplayStrain`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplayStrain`` 
    
    :param reportDisplayStrain: 
    :type reportDisplayStrain: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplayStress: bool = ...
    """
    Returns or sets  the option to display stress in report.  
    
    If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplayStress`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplayStress`` 
    
    :param reportDisplayStress: 
    :type reportDisplayStress: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplayThickness: bool = ...
    """
    Returns or sets  the option to display thickness information in report.  
    
    If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplayThickness`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplayThickness`` 
    
    :param reportDisplayThickness: 
    :type reportDisplayThickness: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReportDisplayViewControl: bool = ...
    """
    Returns or sets  the option to control view while creating screen image in report.  
    
    If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.
    
    <hr>
    
    Getter Method
    
    Signature ``ReportDisplayViewControl`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReportDisplayViewControl`` 
    
    :param reportDisplayViewControl: 
    :type reportDisplayViewControl: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReverseSide: bool = ...
    """
    Returns or sets  the option to indicate whether or not to unform the profile to the other side on the target body.  
    
    This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseSide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseSide`` 
    
    :param reverseSide: 
    :type reverseSide: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverConvergencyLevel: OnestepUnformBuilderConvergency = ...
    """
    Returns or sets  the convergency level of onestep solver.  
    
    <hr>
    
    Getter Method
    
    Signature ``SolverConvergencyLevel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderConvergency` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverConvergencyLevel`` 
    
    :param solverConvergencyLevel: 
    :type solverConvergencyLevel: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderConvergency` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverDisplaySpringbackMode: OnestepUnformBuilderDisplaySpringbackMode = ...
    """
    Returns or sets  the option for springback display.  
    
    If it is true, it will display springback in absolution 3D distance, or projecte in x/y/z directions.
    
    <hr>
    
    Getter Method
    
    Signature ``SolverDisplaySpringbackMode`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderDisplaySpringbackMode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverDisplaySpringbackMode`` 
    
    :param solverDisplaySpringbackMode: 
    :type solverDisplaySpringbackMode: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderDisplaySpringbackMode` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverDoSpringbackCalculation: bool = ...
    """
    Returns or sets  the option to do springback calculation in onestep solver.  
    
    If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.
    
    <hr>
    
    Getter Method
    
    Signature ``SolverDoSpringbackCalculation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverDoSpringbackCalculation`` 
    
    :param solverDoSpringbackCalculation: 
    :type solverDoSpringbackCalculation: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverJoinOutputCurves: bool = ...
    """
    Returns or sets  the option to join output curves.  
    
    If it is true, join output curves. If it is false, do not join output curves
    
    <hr>
    
    Getter Method
    
    Signature ``SolverJoinOutputCurves`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverJoinOutputCurves`` 
    
    :param solverJoinOutputCurves: 
    :type solverJoinOutputCurves: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverMaxIterationSteps: int = ...
    """
    Returns or sets the maximum number of iteration steps in onestep solver.  
    
    <hr>
    
    Getter Method
    
    Signature ``SolverMaxIterationSteps`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverMaxIterationSteps`` 
    
    :param solverMaxIterationSteps: 
    :type solverMaxIterationSteps: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SolverSaveAnalysisResultsIntoFeature: bool = ...
    """
    Returns or sets  the option to save analysis result into feature.  
    
    If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.
    
    <hr>
    
    Getter Method
    
    Signature ``SolverSaveAnalysisResultsIntoFeature`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SolverSaveAnalysisResultsIntoFeature`` 
    
    :param solverSaveAnalysisResultsIntoFeature: 
    :type solverSaveAnalysisResultsIntoFeature: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SurfaceType: OnestepUnformBuilderSurface = ...
    """
    Returns or sets  the surface type used to determine offset direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``SurfaceType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderSurface` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SurfaceType`` 
    
    :param surfaceType: 
    :type surfaceType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderSurface` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    TargetRegion: NXOpen.ScCollector = ...
    """
    Returns  the target region which is a group of faces user chooses to unfrom to.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Thickness: float = ...
    """
    Returns or sets  the thickness of sheet metal model.  
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Thickness`` 
    
    :param thickness: 
    :type thickness: float 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ThicknessDirection: NXOpen.Direction = ...
    """
    Returns or sets  the thickness direction used to define the direction of product thickness at the specific point in trimline.  
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ThicknessDirection`` 
    
    :param thicknessDirection: 
    :type thicknessDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.2
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    TrimlinePoint: NXOpen.Point = ...
    """
    Returns or sets  the point where the thickness direction is defined for trimline.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrimlinePoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TrimlinePoint`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.2
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UnfoldModeType: OnestepUnformBuilderUnfoldMode = ...
    """
    Returns or sets  the onestep unfold mode.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnfoldModeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderUnfoldMode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnfoldModeType`` 
    
    :param unfoldModeType: 
    :type unfoldModeType: :py:class:`NXOpen.BodyDes.OnestepUnformBuilderUnfoldMode` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UnfoldSolid: NXOpen.Body = ...
    """
    Returns or sets  the solid body to unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnfoldSolid`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnfoldSolid`` 
    
    :param unfoldSolidTag: 
    :type unfoldSolidTag: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UnfoldSolidRegion: NXOpen.SelectBodyList = ...
    """
    Returns  the unfold solid regions which are a group of faces user chooses to unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnfoldSolidRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectBodyList` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    UnformRegion: NXOpen.ScCollector = ...
    """
    Returns  the unform region which is a group of faces user chooses to unform.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnformRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UnformSection: NXOpen.Section = ...
    """
    Returns or sets  the unform section which includes a group of user selected points or curves.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnformSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UnformSection`` 
    
    :param unformsection: 
    :type unformsection: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: OnestepUnformBuilder = ...  # unknown typename


class OnestepUnformCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of OnestepUnform   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX5.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateOnestepBuilder(self, onestepunform: NXOpen.Features.Feature) -> OnestepUnformBuilder:
        """
        Creates an Onestep Unform builder.  
        
        Signature ``CreateOnestepBuilder(onestepunform)`` 
        
        :param onestepunform:  :py:class:`Features.Feature` to be edited  
        :type onestepunform: :py:class:`NXOpen.Features.Feature` 
        :returns:  :py:class:`OnestepUnformBuilder` object object  
        :rtype: :py:class:`NXOpen.BodyDes.OnestepUnformBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    


class OnestepUnform(NXOpen.Features.Feature):
    """
    Represents a onestep unform feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.BodyDes.OnestepUnformBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Null: OnestepUnform = ...  # unknown typename


