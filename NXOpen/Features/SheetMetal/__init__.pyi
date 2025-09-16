# module 'NXOpen.Features.SheetMetal'
#
# Automatically generated 2025-06-09T14:38:46.493265
#

import typing

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities



class SheetmetalBaseBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Sheet Metal Feature Builder to be used in the creation and modification of features.  
    
    Feature Builders
    manage the steps needed to correctly create features on a part. 
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX7.5.0
    """
    
    def GetApplicationContext(self) -> ApplicationContext:
        """
        Get the application context.  
        
        This feature is available in more than one application and under different licenses. The enum :py:class:`NXOpen.Features.SheetMetal.ApplicationContext`
        contains a list of all sheet metal related applications and a feature might be available in one or more applications listed there. 
        
        Signature ``GetApplicationContext()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ApplicationContext` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetApplicationContext(self, appContext: ApplicationContext) -> None:
        """
        Set the application context.  
        
        Signature ``SetApplicationContext(appContext)`` 
        
        :param appContext: 
        :type appContext: :py:class:`NXOpen.Features.SheetMetal.ApplicationContext` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    Null: SheetmetalBaseBuilder = ...  # unknown typename


class ResizeBendAngleBuilder(SheetmetalBaseBuilder):
    """
    Represents a :py:class:`NXOpen.Features.ResizeBendAngle` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateResizeBendAngleBuilder`
    
    .. versionadded:: NX5.0.0
    """
    Angle: NXOpen.Expression = ...
    """
    Returns   the bend angle 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendFace: NXOpen.SelectFace = ...
    """
    Returns   the bend face 
    
    <hr>
    
    Getter Method
    
    Signature ``BendFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    KeepRadiusFixed: bool = ...
    """
    Returns or sets  the flag indicationg to keep radius fixed 
    
    <hr>
    
    Getter Method
    
    Signature ``KeepRadiusFixed`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``KeepRadiusFixed`` 
    
    :param keepRadiusFixed: 
    :type keepRadiusFixed: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReferenceEdge: NXOpen.SelectEdge = ...
    """
    Returns   the reference edge
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReferenceFace: NXOpen.SelectFace = ...
    """
    Returns   the reference face
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: ResizeBendAngleBuilder = ...  # unknown typename


class FlatSolidBuilderOrientationTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlatSolidBuilderOrientationType():
    """
    The enum defines how to orient flat solid body.   
    
    .. versionadded:: NX12.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Default", "do not orient flat solid body"
       "Edge", "transform flat solid body as per orientation defined by edge"
       "Csys", "transform flat solid body as per orientation defined by CSYS"
    """
    Default = 0  # FlatSolidBuilderOrientationTypeMemberType
    Edge = 1  # FlatSolidBuilderOrientationTypeMemberType
    Csys = 2  # FlatSolidBuilderOrientationTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlatSolidBuilderTransformComponentsOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlatSolidBuilderTransformComponentsOption():
    """
    The enum defines how to represent PCB components on flat solid.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "do not transform components"
       "Body", "transform components as bodies"
       "Csys", "transform components as CSYS"
    """
    NotSet = 0  # FlatSolidBuilderTransformComponentsOptionMemberType
    Body = 1  # FlatSolidBuilderTransformComponentsOptionMemberType
    Csys = 2  # FlatSolidBuilderTransformComponentsOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlatSolidBuilder(SheetmetalBaseBuilder):
    """
    Represents a Flat As Solid feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateFlatSolidFeatureBuilder`
    
    Default values.
    
    ===================================  ======================================
    Property                             Value
    ===================================  ======================================
    Associative                          true 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.TreatmentType   None 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.UseGlobal       1 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.Value.Value     0 (millimeters part), 0 (inches part) 
    -----------------------------------  --------------------------------------
    TransformComponents                  None 
    -----------------------------------  --------------------------------------
    TransformRestrictionAreas            0 
    ===================================  ======================================
    
    .. versionadded:: NX4.0.0
    """
    
    class OrientationType():
        """
        The enum defines how to orient flat solid body.   
        
        .. versionadded:: NX12.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Default", "do not orient flat solid body"
           "Edge", "transform flat solid body as per orientation defined by edge"
           "Csys", "transform flat solid body as per orientation defined by CSYS"
        """
        Default = 0  # FlatSolidBuilderOrientationTypeMemberType
        Edge = 1  # FlatSolidBuilderOrientationTypeMemberType
        Csys = 2  # FlatSolidBuilderOrientationTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TransformComponentsOption():
        """
        The enum defines how to represent PCB components on flat solid.   
        
        .. versionadded:: NX10.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "do not transform components"
           "Body", "transform components as bodies"
           "Csys", "transform components as CSYS"
        """
        NotSet = 0  # FlatSolidBuilderTransformComponentsOptionMemberType
        Body = 1  # FlatSolidBuilderTransformComponentsOptionMemberType
        Csys = 2  # FlatSolidBuilderTransformComponentsOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ValidateBuilderData(self) -> int:
        """
        Validate the builder data  
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  0 Means no errors.  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    AddedGeometry: NXOpen.Section = ...
    """
    Returns  the added geometry selection 
    
    <hr>
    
    Getter Method
    
    Signature ``AddedGeometry`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Associative: bool = ...
    """
    Returns or sets  the setting which decides whether the flattened solid will be associative to parent body.  
    
    **  This is applicable to flat solid features created in NX12 and later release.
    **  Cannot change during feature edit if the feature was created as non associative.
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns:  True = Feature is associative, False = Feature is not associative.  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative:  True = Feature is associative, False = Feature is not associative.  
    :type associative: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FixAtTimestamp: bool = ...
    """
    Returns or sets  the setting decides whether the flattened solid will be fixed at timestamp.  
    
    **  This is applicable to flat solid features created in NX12 and later release.
    **  Cannot change during feature edit if the feature was created as fixed at timestamp.
    
    <hr>
    
    Getter Method
    
    Signature ``FixAtTimestamp`` 
    
    :returns:  True = Fix at Timestamp, False = Do not Fix at Timestamp.  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FixAtTimestamp`` 
    
    :param fixAtTimestamp:  True = Fix at Timestamp, False = Do not Fix at Timestamp.  
    :type fixAtTimestamp: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    InnerCornerTreatment: CornerTreatmentBuilder = ...
    """
    Returns  the inner corner treatment corner object 
    
    <hr>
    
    Getter Method
    
    Signature ``InnerCornerTreatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Orientation: FlatSolidBuilderOrientationType = ...
    """
    Returns or sets  the option which decides if the flattened solid will be transformed to Absolute CSYS.  
    
    This is applicable to flat solid / flat pattern features created (or renewed) to NX12 and later release.
    
    <hr>
    
    Getter Method
    
    Signature ``Orientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderOrientationType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Orientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderOrientationType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OrientationCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the orientation csys 
    **  This is applicable to flat solid features created (or renewed) in NX12 and later release.  
    
    <hr>
    
    Getter Method
    
    Signature ``OrientationCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrientationCsys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OuterCornerTreatment: CornerTreatmentBuilder = ...
    """
    Returns  the outer corner treatment corner object 
    
    <hr>
    
    Getter Method
    
    Signature ``OuterCornerTreatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ReferenceVertex: NXOpen.Point3d = ...
    """
    Returns or sets  the end of the edge where the tangent will define the x axis for flat as solid.  
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceVertex`` 
    
    :returns:  One of the end points of the reference edge.  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceVertex`` 
    
    :param vertex:  One of the end points of the reference edge.  
    :type vertex: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StationaryFace: NXOpen.SelectFace = ...
    """
    Returns  the stationary face selection 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    TransformComponents: FlatSolidBuilderTransformComponentsOption = ...
    """
    Returns or sets  the setting indicating how to represent transformed components in flat solid.  
    
    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal. 
    
    <hr>
    
    Getter Method
    
    Signature ``TransformComponents`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderTransformComponentsOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransformComponents`` 
    
    :param transformComponents: 
    :type transformComponents: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderTransformComponentsOption` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    TransformRestrictionAreas: bool = ...
    """
    Returns or sets  the setting indicating whether to transform restriction areas in flat solid.  
    
    Only applies to the Flexible Printed Circuit Design application and will have no effect in Sheet Metal. 
    
    <hr>
    
    Getter Method
    
    Signature ``TransformRestrictionAreas`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransformRestrictionAreas`` 
    
    :param transformRestrictionAreas: 
    :type transformRestrictionAreas: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    TransformToAbsoluteCsys: bool = ...
    """
    Returns or sets  the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
    
    This is applicable to flat solid / flat pattern features created before NX12 release and not yet renewed.
    The API can not be deprecated because it is required to edit features created before NX12 release.
    But user should modify automation programs written before NX12 and replace use this option with the orientation option,
    before using the program to create new features in NX12 or later.
    
    <hr>
    
    Getter Method
    
    Signature ``TransformToAbsoluteCsys`` 
    
    :returns:  True = Transform to ABS, False = Do not transform to ABS.  
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TransformToAbsoluteCsys`` 
    
    :param transformFlag:  True = Transform to ABS, False = Do not transform to ABS.  
    :type transformFlag: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    XAxisEdge: NXOpen.SelectEdge = ...
    """
    Returns  the x axis edge selection 
    
    <hr>
    
    Getter Method
    
    Signature ``XAxisEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: FlatSolidBuilder = ...  # unknown typename


class AeroFlatSolidBuilder(FlatSolidBuilder):
    """
    Represents a Flat As Solid feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateFlatSolidBuilder`
    
    Default values.
    
    ==========================  =====
    Property                    Value
    ==========================  =====
    Associative                 true 
    --------------------------  -----
    TransformComponents         None 
    --------------------------  -----
    TransformRestrictionAreas   0 
    ==========================  =====
    
    .. versionadded:: NX6.0.0
    """
    Null: AeroFlatSolidBuilder = ...  # unknown typename


class JoggleSideOptionsBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Sheetmetal Joggle side Options class.  
    
    .. versionadded:: NX11.0.0
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
    
    Clearance: NXOpen.Expression = ...
    """
    Returns  the clearance 
    
    <hr>
    
    Getter Method
    
    Signature ``Clearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    OffsetRadius: NXOpen.Expression = ...
    """
    Returns  the offset radius 
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Runout: NXOpen.Expression = ...
    """
    Returns  the runout 
    
    <hr>
    
    Getter Method
    
    Signature ``Runout`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    StationaryRadius: NXOpen.Expression = ...
    """
    Returns  the stationary radius 
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: JoggleSideOptionsBuilder = ...  # unknown typename


class SheetmetalComponentBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a sheet metal component builder to be used in the creation and modification of features componenets.  
    
    Component builders
    manage the steps needed to correctly create features components on a feature. 
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX12.0.0
    """
    
    def GetApplicationContext(self) -> ApplicationContext:
        """
        Get the application context.  
        
        This component is available in more than one application and under different licenses. The enum :py:class:`NXOpen.Features.SheetMetal.ApplicationContext`
        contains a list of all sheet metal related applications and a component might be available in one or more applications listed there. 
        
        Signature ``GetApplicationContext()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ApplicationContext` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetApplicationContext(self, appContext: ApplicationContext) -> None:
        """
        Set the application context.  
        
        Signature ``SetApplicationContext(appContext)`` 
        
        :param appContext: 
        :type appContext: :py:class:`NXOpen.Features.SheetMetal.ApplicationContext` 
        
        .. versionadded:: NX12.0.0
        
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
    
    Null: SheetmetalComponentBuilder = ...  # unknown typename


class FeatureBendPropertiesListBuilder(SheetmetalComponentBuilder):
    """
    Represents a Sheetmetal Feature properties List builder class.  
    
    This builder is used to
    interrogate the feature properties list.
    
    .. versionadded:: NX12.0.0
    """
    
    def CreateFeatureProperties(self) -> FeatureBendPropertiesBuilder:
        """
        Create a feature properties.  
        
        Signature ``CreateFeatureProperties()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    FeatureBendPropertiesList: FeatureBendPropertiesBuilderList = ...
    """
    Returns  the feature properties list 
    
    <hr>
    
    Getter Method
    
    Signature ``FeatureBendPropertiesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilderList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: FeatureBendPropertiesListBuilder = ...  # unknown typename


class SheetmetalManagerTabSweepDirMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalManagerTabSweepDir():
    """
    This enum is for Tab sweep direction flag. Sweep direction can be along the normal to section or opposite to normal.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Normal", "Tab sweep direction along normal direction"
       "OppositeToNormal", "Tab sweep direction opposite to normal direction"
    """
    Normal = 0  # SheetmetalManagerTabSweepDirMemberType
    OppositeToNormal = 1  # SheetmetalManagerTabSweepDirMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GussetBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GussetBuilderTypes():
    """
    This enum represents the two Gusset Feature types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AutomaticProfile", "Gusset(s) will be created between the planar faces adjacent to the selected bend face."
       "UserDefinedProfile", "Gusset will be created using a profile defined by the user."
    """
    AutomaticProfile = 0  # GussetBuilderTypesMemberType
    UserDefinedProfile = 1  # GussetBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GussetBuilderWidthSidesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GussetBuilderWidthSides():
    """
    This enum represents the different options for thickening the user defined profile Gusset. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Side1", "The Gusset will be created on the side of plane normal of the user defined profile."
       "Side2", "The Gusset will be created on the opposite side of the plane normal of the user defined profile."
       "Symmetric", "The Gusset will be created on both sides of the plane of the user defined profile."
    """
    Side1 = 0  # GussetBuilderWidthSidesMemberType
    Side2 = 1  # GussetBuilderWidthSidesMemberType
    Symmetric = 2  # GussetBuilderWidthSidesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GussetBuilderPlacementTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GussetBuilderPlacementTypes():
    """
    This enum represents the different options for placing an automatic profile Gusset. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Single", "One Gusset will be created at an offset from an edge on the selected bend face."
       "Fit", "Users will specify the number of occurances of Gusset on the selected bend face and software will calculate the spacing."
       "Fill", "Users will specify the spacing of Gussets on the selected bend face and software will calculate the number of occurances."
       "Fixed", "Users will specify the number of occurances and the spacing for Gussets on the selected bend face."
    """
    Single = 0  # GussetBuilderPlacementTypesMemberType
    Fit = 1  # GussetBuilderPlacementTypesMemberType
    Fill = 2  # GussetBuilderPlacementTypesMemberType
    Fixed = 3  # GussetBuilderPlacementTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GussetBuilderShapesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GussetBuilderShapes():
    """
    This enum represents the two different shapes for Gusset. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Square", "Specifies a square shape for the Gusset"
       "Round", "Specifies a round shape for the Gusset"
    """
    Square = 0  # GussetBuilderShapesMemberType
    Round = 1  # GussetBuilderShapesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class GussetBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a NX Sheet Metal :py:class:`NXOpen.Features.Gusset` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateGussetBuilder`
    
    Default values.
    
    ========================  =========================================
    Property                  Value
    ========================  =========================================
    CornerRadius.Value        1 (millimeters part), 0.05 (inches part) 
    ------------------------  -----------------------------------------
    Depth.Value               10 (millimeters part), 1 (inches part) 
    ------------------------  -----------------------------------------
    DieRadius.Value           2 (millimeters part), 0.1 (inches part) 
    ------------------------  -----------------------------------------
    PlacementCount            2 
    ------------------------  -----------------------------------------
    PlacementDistance.Value   10 (millimeters part), 1 (inches part) 
    ------------------------  -----------------------------------------
    PlacementSpacing.Value    20 (millimeters part), 2 (inches part) 
    ------------------------  -----------------------------------------
    PlacementType             Single 
    ------------------------  -----------------------------------------
    PunchRadius.Value         2 (millimeters part), 0.1 (inches part) 
    ------------------------  -----------------------------------------
    Shape                     Square 
    ------------------------  -----------------------------------------
    SideAngle.Value           0 
    ------------------------  -----------------------------------------
    Width.Value               10 (millimeters part), 1 (inches part) 
    ------------------------  -----------------------------------------
    WidthSide                 Side1 
    ========================  =========================================
    
    .. versionadded:: NX7.5.0
    """
    
    class Types():
        """
        This enum represents the two Gusset Feature types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AutomaticProfile", "Gusset(s) will be created between the planar faces adjacent to the selected bend face."
           "UserDefinedProfile", "Gusset will be created using a profile defined by the user."
        """
        AutomaticProfile = 0  # GussetBuilderTypesMemberType
        UserDefinedProfile = 1  # GussetBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class WidthSides():
        """
        This enum represents the different options for thickening the user defined profile Gusset. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Side1", "The Gusset will be created on the side of plane normal of the user defined profile."
           "Side2", "The Gusset will be created on the opposite side of the plane normal of the user defined profile."
           "Symmetric", "The Gusset will be created on both sides of the plane of the user defined profile."
        """
        Side1 = 0  # GussetBuilderWidthSidesMemberType
        Side2 = 1  # GussetBuilderWidthSidesMemberType
        Symmetric = 2  # GussetBuilderWidthSidesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PlacementTypes():
        """
        This enum represents the different options for placing an automatic profile Gusset. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Single", "One Gusset will be created at an offset from an edge on the selected bend face."
           "Fit", "Users will specify the number of occurances of Gusset on the selected bend face and software will calculate the spacing."
           "Fill", "Users will specify the spacing of Gussets on the selected bend face and software will calculate the number of occurances."
           "Fixed", "Users will specify the number of occurances and the spacing for Gussets on the selected bend face."
        """
        Single = 0  # GussetBuilderPlacementTypesMemberType
        Fit = 1  # GussetBuilderPlacementTypesMemberType
        Fill = 2  # GussetBuilderPlacementTypesMemberType
        Fixed = 3  # GussetBuilderPlacementTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Shapes():
        """
        This enum represents the two different shapes for Gusset. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Square", "Specifies a square shape for the Gusset"
           "Round", "Specifies a round shape for the Gusset"
        """
        Square = 0  # GussetBuilderShapesMemberType
        Round = 1  # GussetBuilderShapesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetStartEdgeCandidates(self) -> 'list[NXOpen.Edge]':
        """
        Get the edges on the bend face that can be selected as Start Edge.  
        
        Only use this option to edit gussets created prior to NX10.
        Use :py:meth:`NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane`` to locate automatic profile gussets from NX10 onwards. 
        Get the edges on the bend face that can be selected as Start Edge.
        If there is no Bend Face, then no edges will be returned.
        
        Signature ``GetStartEdgeCandidates()`` 
        
        :returns:  An array of edges that are valid for selection as start edge  
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def GetPlacementOriginAndDirection(self) -> tuple:
        """
        Get the placement origin and direction.  
        
        Only use this option to edit gussets created prior to NX10.
        Use :py:meth:`NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane`` to locate automatic profile gussets from NX10 onwards.  
        Get the point from which the placement distance will be measured and the 
        direction along which the positive distance is defined.
        
        Signature ``GetPlacementOriginAndDirection()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (direction, origin). direction is a :py:class:`NXOpen.Vector3d`.   Direction along which the placement distance is measured. origin is a :py:class:`NXOpen.Point3d`.   Start point from which placement distance is measured. 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def AlternateSolution(self) -> None:
        """
        Cycles the available solutions when a user defined profile intersects the solid body.  
        
        If there is
        only one working solution then it will be automatically selected and this method will not do anything. 
        
        Signature ``AlternateSolution()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetIsPreNx10(self) -> bool:
        """
        Whether this is a pre-NX10 gusset.  
        
        Use this to determine whether the gusset is created prior to NX10.
        
        Signature ``GetIsPreNx10()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    BendFace: NXOpen.SelectFace = ...
    """
    Returns  the bend face 
    
    Selects the bend face along which the gusset is placed.
    
    <hr>
    
    Getter Method
    
    Signature ``BendFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    CornerRadius: NXOpen.Expression = ...
    """
    Returns  the corner radius 
    
    Only use this option to edit gussets created prior to NX10.
    From NX10 onwards, this is going to be automatically determined by adding the material thickness to the :py:meth:`NXOpen.Features.SheetMetal.GussetBuilder.PunchRadius`
    This value is used only for the :py:class:`NXOpen.Features.SheetMetal.GussetBuilderShapes.Square <NXOpen.Features.SheetMetal.GussetBuilderShapes>` shape. The value must be greater than or equal to zero.
    
    <hr>
    
    Getter Method
    
    Signature ``CornerRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DatumPlane: NXOpen.Plane = ...
    """
    Returns or sets  the plane of the gusset profile.  
    
    Returns the datum plane on the bend face that contains the profile of the automatic profile gusset.
    
    <hr>
    
    Getter Method
    
    Signature ``DatumPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DatumPlane`` 
    
    :param dPlane: 
    :type dPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Depth: NXOpen.Expression = ...
    """
    Returns  the depth 
    
    This value is used for the automatic profile Gussets. It represents the distance from the outer
    bend face of the selected bends along the bisector of the planar faces adjacent to the outer bend face.
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the die radius value of the sharp edges of the bottom face.  
    
    The value must be greater than or equal to zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PlacementCount: int = ...
    """
    Returns or sets  the placement count 
    
    Only use this option to edit gussets created prior to NX10.
    Use patterns to create multiple gussets from NX10 onwards. 
    This value is used if the :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` is set 
    to :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fit <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>` or
    :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fixed <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>`. It represents 
    the number of occurances of the automatic profile Gusset to create on the selected bend face. The count
    must be greater than zero for :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fit <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>` and greater than one for
    :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fixed <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>`.
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementCount`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlacementCount`` 
    
    :param placementCount: 
    :type placementCount: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    PlacementDistance: NXOpen.Expression = ...
    """
    Returns  the placement distance 
    
    Only use this option to edit gussets created prior to NX10. 
    Use :py:meth:`NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane`` to locate automatic profile gussets from NX10 onwards. 
    If the :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` is set to :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Single <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>`, then this option
    represents the location of the automatic profile Gusset from one of the ends of the selected bend face. The distance is measured in a direction going from 
    the start end to the other end. Users can specify which end of the selected bend face to use as the start.
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PlacementSpacing: NXOpen.Expression = ...
    """
    Returns  the placement spacing  
    
    Only use this option to edit gussets created prior to NX10.
    Use patterns to create multiple gussets from NX10 onwards. 
    This value is used if the :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` is set 
    to :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fill <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>` or
    :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes.Fixed <NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes>`. It represents 
    the spacing between the automatic profile Gussets to create on the selected bend face.
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementSpacing`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PlacementType: GussetBuilderPlacementTypes = ...
    """
    Returns or sets  the placement type 
    
    Only use this option to edit gussets created prior to NX10.
    Use patterns to create multiple gussets from NX10 onwards. 
    Specify the Gusset placement option. See the description of :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` elements for details.
    
    <hr>
    
    Getter Method
    
    Signature ``PlacementType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlacementType`` 
    
    :param placementType: 
    :type placementType: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderPlacementTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    PunchRadius: NXOpen.Expression = ...
    """
    Returns  the punch radius value 
    
    The application of the punch radius has changed from NX10 onwards, to ensure material thickness is constant in the gusset. 
    See the legend in the gusset dialog for more information. 
    
    <hr>
    
    Getter Method
    
    Signature ``PunchRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Section: NXOpen.Section = ...
    """
    Returns  the section 
    
    This section object contains a planar set of connected curves that will be used to
    create a Gusset of type :py:class:`NXOpen.Features.SheetMetal.GussetBuilderTypes.UserDefinedProfile <NXOpen.Features.SheetMetal.GussetBuilderTypes>`. This
    profile can be closed or open. If it is open, then the end points can touch face(s). The profile must not intersect the
    solid body. If an open profile does not intersect or touch any face, each end will be extended until it touches a face.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Shape: GussetBuilderShapes = ...
    """
    Returns or sets  the shape 
    
    See :py:class:`NXOpen.Features.SheetMetal.GussetBuilderShapes` for details.
    
    <hr>
    
    Getter Method
    
    Signature ``Shape`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderShapes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Shape`` 
    
    :param shape: 
    :type shape: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderShapes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SideAngle: NXOpen.Expression = ...
    """
    Returns  the side angle.  
    
    The value must be greater than or equal to zero. 
    
    <hr>
    
    Getter Method
    
    Signature ``SideAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    StartEdge: NXOpen.SelectEdge = ...
    """
    Returns  the start edge  
    
    Only use this option to edit gussets created prior to NX10.
    Use :py:meth:`NXOpen.Features.SheetMetal.GussetBuilder.DatumPlane`` to locate automatic profile gussets from NX10 onwards.  
    Selects the edge on the bend face to determine the gusset offset direction.
    
    <hr>
    
    Getter Method
    
    Signature ``StartEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Type: GussetBuilderTypes = ...
    """
    Returns or sets  the type of Gusset feature 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width value for the Gusset 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    WidthSide: GussetBuilderWidthSides = ...
    """
    Returns or sets  the width side 
    
    Defines the side of the profile to which material should be added or from which material should be removed to construct 
    the feature. 
    
    The side option is not required when the profile is closed.
    
    <hr>
    
    Getter Method
    
    Signature ``WidthSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderWidthSides` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthSide`` 
    
    :param widthSide: 
    :type widthSide: :py:class:`NXOpen.Features.SheetMetal.GussetBuilderWidthSides` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: GussetBuilder = ...  # unknown typename


class RebendBuilder(SheetmetalBaseBuilder):
    """
    The Rebend feature class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateRebendFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating Rebend or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    FaceCollector: NXOpen.ScCollector = ...
    """
    Returns or sets  the unbent faces to rebend 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``FaceCollector`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReferenceEntity: NXOpen.NXObject = ...
    """
    Returns or sets  the non-thickness planar face or linear edge to remain fixed while part is rebent 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceEntity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceEntity`` 
    
    :param referenceEntity: 
    :type referenceEntity: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: RebendBuilder = ...  # unknown typename


class EditBendBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.EditBend` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateEditBendBuilder`
    
    .. versionadded:: NX7.5.0
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SelectBend: NXOpen.ScCollector = ...
    """
    Returns  the select bend 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectBend`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: EditBendBuilder = ...  # unknown typename


class MultiBendBendPropertiesListBuilder(FeatureBendPropertiesListBuilder):
    """
    Represents a Sheetmetal Multi Bend properties List builder class.  
    
    This builder is used to
    interrogate the properties list of multiple bends.
    
    .. versionadded:: NX12.0.0
    """
    
    def CreateMultiBendBendProperties(self) -> MultiBendBendPropertiesBuilder:
        """
        Create a multi bend properties.  
        
        Signature ``CreateMultiBendBendProperties()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.MultiBendBendPropertiesBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    Null: MultiBendBendPropertiesListBuilder = ...  # unknown typename


class FeatureBendPropertiesBuilder(SheetmetalComponentBuilder):
    """
    Represents a Sheetmetal Feature bend properties builder class.  
    
    This builder is used to
    interrogate the feature properties in the list.
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.FeatureBendPropertiesListBuilder.CreateFeatureProperties`
    
    .. versionadded:: NX12.0.0
    """
    BendOptions: BendOptions = ...
    """
    Returns  the Sheet Metal Bend Options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Value: NXOpen.Expression = ...
    """
    Returns  the offset 
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: FeatureBendPropertiesBuilder = ...  # unknown typename


class MultiBendBendPropertiesBuilderInsetsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MultiBendBendPropertiesBuilderInsets():
    """
    This enum defines the material inset types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", " - "
       "MaterialOutside", " - "
    """
    MaterialInside = 0  # MultiBendBendPropertiesBuilderInsetsMemberType
    MaterialOutside = 1  # MultiBendBendPropertiesBuilderInsetsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MultiBendBendPropertiesBuilder(FeatureBendPropertiesBuilder):
    """
    Represents a Sheetmetal Multi Bend properties builder class.  
    
    This builder is used to
    interrogate the properties of multiple bends in the list.
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.MultiBendBendPropertiesListBuilder.CreateMultiBendBendProperties`
    
    .. versionadded:: NX12.0.0
    """
    
    class Insets():
        """
        This enum defines the material inset types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", " - "
           "MaterialOutside", " - "
        """
        MaterialInside = 0  # MultiBendBendPropertiesBuilderInsetsMemberType
        MaterialOutside = 1  # MultiBendBendPropertiesBuilderInsetsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def DeleteMultiBendBendProperties(self) -> None:
        """
        Deletes a multi bend properties.  
        
        Signature ``DeleteMultiBendBendProperties()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    Inset: MultiBendBendPropertiesBuilderInsets = ...
    """
    Returns or sets  the inset 
    
    <hr>
    
    Getter Method
    
    Signature ``Inset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MultiBendBendPropertiesBuilderInsets` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Inset`` 
    
    :param inset: 
    :type inset: :py:class:`NXOpen.Features.SheetMetal.MultiBendBendPropertiesBuilderInsets` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ParentPlane: NXOpen.Plane = ...
    """
    Returns or sets  the plane 
    
    <hr>
    
    Getter Method
    
    Signature ``ParentPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ParentPlane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    SketchParentPlane: bool = ...
    """
    Returns or sets  the option to set sketch plane as parent 
    
    <hr>
    
    Getter Method
    
    Signature ``SketchParentPlane`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SketchParentPlane`` 
    
    :param isSketchPlaneParent: 
    :type isSketchPlaneParent: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: MultiBendBendPropertiesBuilder = ...  # unknown typename


class DimpleBuilderDepthTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DimpleBuilderDepthTypeOptions():
    """
    This enum represents the depth direction for the dimple. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Dimple punched on the side of the section normal."
       "SectionReverseNormalSide", "Dimple punched on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # DimpleBuilderDepthTypeOptionsMemberType
    SectionReverseNormalSide = 1  # DimpleBuilderDepthTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DimpleBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DimpleBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the dimple punches material. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # DimpleBuilderSectionSideOptionsMemberType
    Right = 1  # DimpleBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DimpleBuilderDimensionTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DimpleBuilderDimensionTypeOptions():
    """
    the Dimension options for dimple. This specifies whether the dimple's depth must be measured from the plane to which the section
    is attached or from the 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Offset", "the actual depth will be depth plus the thickness of sheet."
       "Full", "the actual extent distance will be the value specified as depth."
    """
    Offset = 0  # DimpleBuilderDimensionTypeOptionsMemberType
    Full = 1  # DimpleBuilderDimensionTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DimpleBuilderSidewallTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DimpleBuilderSidewallTypeOptions():
    """
    the side walls material option. This specifies whether the dimple's outerwalls or the innerwalls coincide with the section outline 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Outside", "the innerface of the dimple side walls coincides with the section outline."
       "Inside", "the outerface of the dimple side walls coincides with the section outline."
    """
    Outside = 0  # DimpleBuilderSidewallTypeOptionsMemberType
    Inside = 1  # DimpleBuilderSidewallTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DimpleBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Dimple feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateDimpleFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class DepthTypeOptions():
        """
        This enum represents the depth direction for the dimple. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Dimple punched on the side of the section normal."
           "SectionReverseNormalSide", "Dimple punched on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # DimpleBuilderDepthTypeOptionsMemberType
        SectionReverseNormalSide = 1  # DimpleBuilderDepthTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the dimple punches material. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # DimpleBuilderSectionSideOptionsMemberType
        Right = 1  # DimpleBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DimensionTypeOptions():
        """
        the Dimension options for dimple. This specifies whether the dimple's depth must be measured from the plane to which the section
        is attached or from the 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Offset", "the actual depth will be depth plus the thickness of sheet."
           "Full", "the actual extent distance will be the value specified as depth."
        """
        Offset = 0  # DimpleBuilderDimensionTypeOptionsMemberType
        Full = 1  # DimpleBuilderDimensionTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SidewallTypeOptions():
        """
        the side walls material option. This specifies whether the dimple's outerwalls or the innerwalls coincide with the section outline 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Outside", "the innerface of the dimple side walls coincides with the section outline."
           "Inside", "the outerface of the dimple side walls coincides with the section outline."
        """
        Outside = 0  # DimpleBuilderSidewallTypeOptionsMemberType
        Inside = 1  # DimpleBuilderSidewallTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetDepth(self) -> NXOpen.Expression:
        """
        Depth of the Dimple 
        
        Signature ``GetDepth()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetDepth(self, extent: str) -> None:
        """
        Signature ``SetDepth(extent)`` 
        
        :param extent: 
        :type extent: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.GetDepth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetTaperAngle(self) -> NXOpen.Expression:
        """
        Taper Angle of the Dimple.  
        
        In case of a tapered dimple, the taper angle is applied on the side faces of the above-protruded section.
        The affects of taper angle will always increases the cavity volume of the dimple.
        
        Signature ``GetTaperAngle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetTaperAngle(self, taperAngle: str) -> None:
        """
        Signature ``SetTaperAngle(taperAngle)`` 
        
        :param taperAngle: 
        :type taperAngle: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.GetTaperAngle` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetPunchRadius(self) -> NXOpen.Expression:
        """
        Radius value of the sharp edges on the top face 
        
        Signature ``GetPunchRadius()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetPunchRadius(self, punchRadius: str) -> None:
        """
        Signature ``SetPunchRadius(punchRadius)`` 
        
        :param punchRadius: 
        :type punchRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.GetPunchRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetDieRadius(self) -> NXOpen.Expression:
        """
        Radius value of the sharp edges of the bottom face 
        
        Signature ``GetDieRadius()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetDieRadius(self, dieRadius: str) -> None:
        """
        Signature ``SetDieRadius(dieRadius)`` 
        
        :param dieRadius: 
        :type dieRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.GetDieRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFilletRadius(self) -> NXOpen.Expression:
        """
        Fillet Radius to be applied for rounding the Sharp section Corners
        
        Signature ``GetFilletRadius()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetFilletRadius(self, filletRadius: str) -> None:
        """
        Signature ``SetFilletRadius(filletRadius)`` 
        
        :param filletRadius: 
        :type filletRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.GetFilletRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a dimple or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    DepthType: DimpleBuilderDepthTypeOptions = ...
    """
    Returns or sets  the Direction in which the Dimple is punched.  
    
    This is used to specify the direction in which the punching should happen. If Punching must happen in the
    direction of the Section Normal (specified using the :py:meth:`NXOpen.Features.SheetMetal.DimpleBuilder.Section``) then
    pass the value of :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions.SectionNormalSide <NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions>`
    If punching must happen in the opposite direction to that of Section Normal, set the value to be
    :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions.SectionReverseNormalSide <NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions>`
    
    <hr>
    
    Getter Method
    
    Signature ``DepthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``DepthType`` 
    
    :param depthType: 
    :type depthType: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    DimensionType: DimpleBuilderDimensionTypeOptions = ...
    """
    Returns or sets  the Offset Dimension
    
    The actual extent distance of the Dimple will be determined by the active dimension option.
    In case of :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions.Offset <NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions>` the actual extent distance will be offset dimension distance plus the thickness of sheet.
    In case of :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions.Full <NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions>` the actual extent distance will be the Full dimension distance.
    
    <hr>
    
    Getter Method
    
    Signature ``DimensionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``DimensionType`` 
    
    :param dimensionType: 
    :type dimensionType: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderDimensionTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    FilletSectionCorners: bool = ...
    """
    Returns or sets  the Rounding Option for section Corners which contain Non Fillet Radii
    
    <hr>
    
    Getter Method
    
    Signature ``FilletSectionCorners`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``FilletSectionCorners`` 
    
    :param filletSectionCorners: 
    :type filletSectionCorners: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    IncludeRounding: bool = ...
    """
    Returns or sets  the Rounding type of the Sharp edges of bottom face and top face.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeRounding`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeRounding`` 
    
    :param includeRounding: 
    :type includeRounding: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MinimumToolClearance: NXOpen.Expression = ...
    """
    Returns  
    the minimum tool clearance expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumToolClearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the Section used by the Dimple.  
    
    Section can be Open/Closed.
    
    The section is protruded on the reference face at finite distance of extent and in the direction of
    extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
    Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
    dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
    will be the Full dimension distance.
    In case of open section, the end segments are extended to the nearest flat face edges. If the end
    segments are already crossing the flat face edges, those segments will be trimmed to the edges.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SectionSide: DimpleBuilderSectionSideOptions = ...
    """
    Returns or sets  the section Side for the Dimple section.  
    
    This is used to specify which side of the section should remain stationary during the Dimple operation.
    Dimple's section is a set of connected curves. The material exists on both sides of the section curves.
    section Side specifies - the material on which side of the curve must be punched.The other side shall
    be bent to the specified angle with respect to this fixed side. This is how you calculate Left/Right.
    Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
    vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
    you want the material on the side of Result to be punched, then you have to pass the value of
    :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions.Right <NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions>` If you want the
    other side to be punched, then you have to send :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions.Left <NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``SectionSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SidewallType: DimpleBuilderSidewallTypeOptions = ...
    """
    Returns or sets  the side where the material must be added to the dimple.  
    
    Done with Respect to the section
    
    If :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions.Inside <NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions>` is specified, the material of the dimple sidewalls will be added to the interior of the section.
    If :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions.Outside <NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions>` is specified,the material will be added from the lifted section such that the volume of the dimple cavity is increased.
    
    <hr>
    
    Getter Method
    
    Signature ``SidewallType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``SidewallType`` 
    
    :param sidewallType: 
    :type sidewallType: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilderSidewallTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the Slave Sketch used by the Dimple, If one exists.  
    
    If the Sketch is created internally as part of the Dimple command in the UI, then it shall be consumed by the Dimple and shall not show up as a separate feature in the Part Navigator.
    If such a behaviour is desired, then specify the Sketch here.
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: DimpleBuilder = ...  # unknown typename


class ClosedCornerBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClosedCornerBuilderTypes():
    """
    This enum represents the feature types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CloseAndRelief", " - "
       "Relief", " - "
    """
    CloseAndRelief = 0  # ClosedCornerBuilderTypesMemberType
    Relief = 1  # ClosedCornerBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ClosedCornerBuilderClosureTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClosedCornerBuilderClosureTypeOptions():
    """
    This enum represents Corner Closure type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Close", " - "
       "Overlap", " - "
    """
    Close = 0  # ClosedCornerBuilderClosureTypeOptionsMemberType
    Overlap = 1  # ClosedCornerBuilderClosureTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ClosedCornerBuilderTreatmentTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClosedCornerBuilderTreatmentTypeOptions():
    """
    This enum represents Corner treatment type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Open", "Only Webs will be closed"
       "Closed", "Bend and Webs will be closed"
       "CircularCutout", "Circular shaped relief"
       "UCutout", "U shaped relief"
       "VCutout", "V shaped relief"
       "RectangularCutout", "Rectangular shaped relief"
    """
    Open = 0  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    Closed = 1  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    CircularCutout = 2  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    UCutout = 3  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    VCutout = 4  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    RectangularCutout = 5  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ClosedCornerBuilderOriginTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ClosedCornerBuilderOriginTypes():
    """
    This enum represents Origin type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BendCenter", "The relief origin will be at the intersection of first bend's centerline and bisector of corrner angle."
       "CornerPoint", "The relief origin will be at the corner point."
    """
    BendCenter = 0  # ClosedCornerBuilderOriginTypesMemberType
    CornerPoint = 1  # ClosedCornerBuilderOriginTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ClosedCornerBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Closed corner feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateClosedCornerFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class Types():
        """
        This enum represents the feature types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "CloseAndRelief", " - "
           "Relief", " - "
        """
        CloseAndRelief = 0  # ClosedCornerBuilderTypesMemberType
        Relief = 1  # ClosedCornerBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ClosureTypeOptions():
        """
        This enum represents Corner Closure type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Close", " - "
           "Overlap", " - "
        """
        Close = 0  # ClosedCornerBuilderClosureTypeOptionsMemberType
        Overlap = 1  # ClosedCornerBuilderClosureTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TreatmentTypeOptions():
        """
        This enum represents Corner treatment type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Open", "Only Webs will be closed"
           "Closed", "Bend and Webs will be closed"
           "CircularCutout", "Circular shaped relief"
           "UCutout", "U shaped relief"
           "VCutout", "V shaped relief"
           "RectangularCutout", "Rectangular shaped relief"
        """
        Open = 0  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        Closed = 1  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        CircularCutout = 2  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        UCutout = 3  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        VCutout = 4  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        RectangularCutout = 5  # ClosedCornerBuilderTreatmentTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OriginTypes():
        """
        This enum represents Origin type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BendCenter", "The relief origin will be at the intersection of first bend's centerline and bisector of corrner angle."
           "CornerPoint", "The relief origin will be at the corner point."
        """
        BendCenter = 0  # ClosedCornerBuilderOriginTypesMemberType
        CornerPoint = 1  # ClosedCornerBuilderOriginTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Add a face pair.  
        
        Signature ``AddFacePair(firstFace, secondFace)`` 
        
        :param firstFace:   A bend face from a bend  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:   A bend face from an adjacent bend  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFacePair(self, index: int) -> tuple:
        """
        Return the face pair.  
        
        Signature ``GetFacePair(index)`` 
        
        :param index:  Index of the desired face pair  
        :type index: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (firstFace, secondFace). firstFace is a :py:class:`NXOpen.Face`.   First face of the face pair secondFace is a :py:class:`NXOpen.Face`.   Second face of the face pair 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetNumberOfFacePairs(self) -> int:
        """
        Returns the number of face pairs already identified for the three bend corner feature.  
        
        Signature ``GetNumberOfFacePairs()`` 
        
        :returns:  The number of face pairs currently identified  
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Validates the builder data.  
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Returns 0 if the data in the builder is valid  
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def RemoveFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Removes a face pair (that represents a unique corner) from the list of face pairs already added.  
        
        Signature ``RemoveFacePair(firstFace, secondFace)`` 
        
        :param firstFace:  A face from an already selected face pair  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:  The other face from the face pair  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    BlendMiter: bool = ...
    """
    Returns or sets  the option for smooth transition from miter to cutout edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``BlendMiter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``BlendMiter`` 
    
    :param blendMiter: 
    :type blendMiter: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    ClosureType: ClosedCornerBuilderClosureTypeOptions = ...
    """
    Returns or sets  the closure type
    
    <hr>
    
    Getter Method
    
    Signature ``ClosureType`` 
    
    :returns:  The type of closure specified for the corner  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderClosureTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``ClosureType`` 
    
    :param closureType:  The type of closure specified for the corner 
    :type closureType: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderClosureTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the diameter.  
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns:  The diameter for relief  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Gap: NXOpen.Expression = ...
    """
    Returns  the gap.  
    
    <hr>
    
    Getter Method
    
    Signature ``Gap`` 
    
    :returns:  The gap.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MiterCorner: bool = ...
    """
    Returns or sets  the corner will be closed using the miter algorithm.  
    
    <hr>
    
    Getter Method
    
    Signature ``MiterCorner`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``MiterCorner`` 
    
    :param miterCorner: 
    :type miterCorner: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the value by which relief origin will be offset
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns:  The Offset   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Origin: ClosedCornerBuilderOriginTypes = ...
    """
    Returns or sets  the default origin will be at the corner point instead of the intersection of bend centerlines.  
    
    <hr>
    
    Getter Method
    
    Signature ``Origin`` 
    
    :returns:  The default location of relief origin  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderOriginTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Origin`` 
    
    :param originType:  The default location of relief origin 
    :type originType: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderOriginTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Overlap: NXOpen.Expression = ...
    """
    Returns  the overlap.  
    
    <hr>
    
    Getter Method
    
    Signature ``Overlap`` 
    
    :returns:  The overlap  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    RectangularLength: NXOpen.Expression = ...
    """
    Returns  the length of rectangular relief.  
    
    The length is associated to the first bend selected.
    
    <hr>
    
    Getter Method
    
    Signature ``RectangularLength`` 
    
    :returns:  The Length   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    RectangularWidth: NXOpen.Expression = ...
    """
    Returns  the width of rectangular relief.  
    
    The width is associated to the second bend selected. 
    
    <hr>
    
    Getter Method
    
    Signature ``RectangularWidth`` 
    
    :returns:  The Width   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    TreatmentType: ClosedCornerBuilderTreatmentTypeOptions = ...
    """
    Returns or sets  the treatment type
    
    <hr>
    
    Getter Method
    
    Signature ``TreatmentType`` 
    
    :returns:  The type of treatment specified for the corner  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderTreatmentTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``TreatmentType`` 
    
    :param treatmentType:  The type of treatment specified for the corner 
    :type treatmentType: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderTreatmentTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Type: ClosedCornerBuilderTypes = ...
    """
    Returns or sets  the feature type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilderTypes` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    VAngle1: NXOpen.Expression = ...
    """
    Returns  the angle1 of V relief.  
    
    This is the angle associated with the first bend selected.
    
    <hr>
    
    Getter Method
    
    Signature ``VAngle1`` 
    
    :returns:  The Angle1   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    VAngle2: NXOpen.Expression = ...
    """
    Returns  the angle2 of V relief.  
    
    This is the angle associated to the second bend selected.
    
    <hr>
    
    Getter Method
    
    Signature ``VAngle2`` 
    
    :returns:  The Angle2   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: ClosedCornerBuilder = ...  # unknown typename


class AeroLighteningCutoutBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroLighteningCutoutBuilderTypes():
    """
    Represents the cutout type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hole", " - "
       "UserDefined", " - "
    """
    Hole = 0  # AeroLighteningCutoutBuilderTypesMemberType
    UserDefined = 1  # AeroLighteningCutoutBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroLighteningCutoutBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilder` 
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateAeroLighteningCutoutBuilder`
    
    Default values.
    
    ================  ==========================================
    Property          Value
    ================  ==========================================
    Angle.Value       45 
    ----------------  ------------------------------------------
    CheckClearance    true 
    ----------------  ------------------------------------------
    Clearance.Value   5 (millimeters part), 0.12 (inches part) 
    ----------------  ------------------------------------------
    Diameter.Value    102 (millimeters part), 2.6 (inches part) 
    ----------------  ------------------------------------------
    DieRadius.Value   8 (millimeters part), 0.2 (inches part) 
    ----------------  ------------------------------------------
    Length.Value      8 (millimeters part), 0.2 (inches part) 
    ----------------  ------------------------------------------
    Type              UserDefined 
    ================  ==========================================
    
    .. versionadded:: NX5.0.0
    """
    
    class Types():
        """
        Represents the cutout type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hole", " - "
           "UserDefined", " - "
        """
        Hole = 0  # AeroLighteningCutoutBuilderTypesMemberType
        UserDefined = 1  # AeroLighteningCutoutBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetStandards(self) -> 'list[str]':
        """
        Returns the standard names  
        
        Signature ``GetStandards()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CheckClearance: bool = ...
    """
    Returns or sets  the check clearance 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckClearance`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckClearance`` 
    
    :param checkClearance: 
    :type checkClearance: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Clearance: NXOpen.Expression = ...
    """
    Returns  the clearance 
    
    <hr>
    
    Getter Method
    
    Signature ``Clearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CornerRadius: NXOpen.Expression = ...
    """
    Returns  the corner radius 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    CutoutProfile: NXOpen.Section = ...
    """
    Returns  the cutout profile 
    
    <hr>
    
    Getter Method
    
    Signature ``CutoutProfile`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the die radius 
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    HoleCenter: NXOpen.Point = ...
    """
    Returns or sets  the hole center 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleCenter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HoleCenter`` 
    
    :param holeCenter: 
    :type holeCenter: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    HoleFace: NXOpen.SelectFace = ...
    """
    Returns  the hole face 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ReverseBendDirection: bool = ...
    """
    Returns or sets  the reverse bend direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseBendDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseBendDirection`` 
    
    :param reverseBendDirection: 
    :type reverseBendDirection: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    StandardName: str = ...
    """
    Returns or sets  the standard name 
    
    <hr>
    
    Getter Method
    
    Signature ``StandardName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StandardName`` 
    
    :param standardName: 
    :type standardName: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Type: AeroLighteningCutoutBuilderTypes = ...
    """
    Returns or sets  the feature type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AeroLighteningCutoutBuilder = ...  # unknown typename


class SMBoundaryConditionBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[SMBoundaryConditionBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: SMBoundaryConditionBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
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
    
    
    def FindIndex(self, obj: SMBoundaryConditionBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> SMBoundaryConditionBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
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
    def Erase(self, obj: SMBoundaryConditionBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: SMBoundaryConditionBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
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
    
    
    def GetContents(self) -> 'list[SMBoundaryConditionBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[SMBoundaryConditionBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
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
    def Swap(self, object1: SMBoundaryConditionBuilder, object2: SMBoundaryConditionBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: SMBoundaryConditionBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
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
    Null: SMBoundaryConditionBuilderList = ...  # unknown typename


class UnbendBuilder(SheetmetalBaseBuilder):
    """
    The Unbend feature class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateUnbendFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating Unbend or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    AddedGeometry: NXOpen.Section = ...
    """
    Returns or sets  the added geometry selection 
    
    <hr>
    
    Getter Method
    
    Signature ``AddedGeometry`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddedGeometry`` 
    
    :param addedGeometry: 
    :type addedGeometry: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ExtractGussetCurves: bool = ...
    """
    Returns or sets  the option to extract gusset boundary curves 
    
    <hr>
    
    Getter Method
    
    Signature ``ExtractGussetCurves`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtractGussetCurves`` 
    
    :param extractGussetCurves: 
    :type extractGussetCurves: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FaceCollector: NXOpen.ScCollector = ...
    """
    Returns or sets  the bend faces 
    
    <hr>
    
    Getter Method
    
    Signature ``FaceCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``FaceCollector`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    HideOriginalCurves: bool = ...
    """
    Returns or sets  the option to keep or hide input curves 
    
    <hr>
    
    Getter Method
    
    Signature ``HideOriginalCurves`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideOriginalCurves`` 
    
    :param hideOriginalCurves: 
    :type hideOriginalCurves: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReferenceEntity: NXOpen.NXObject = ...
    """
    Returns or sets  the non-thickness planar face or linear edge to remain fixed while part is unbent 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceEntity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceEntity`` 
    
    :param referenceEntity: 
    :type referenceEntity: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: UnbendBuilder = ...  # unknown typename


class BendListItemBuilder(NXOpen.Builder):
    """
    Represents a Sheetmetal Flat Pattern bend list item builder class.  
    
    This builder is used to
    edit the bend sequence ID and bend name of the bends in the bend list.
    BendListItemBuilder objects will be created and populated in the BendListBuilder when bend information of a flat pattern view is populated.
    User should never need to create or delete BendListItemBuilder object on its own.
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBendListItemBuilder`
    
    .. versionadded:: NX12.0.0
    """
    BendID: int = ...
    """
    Returns or sets  the new bend id 
    
    <hr>
    
    Getter Method
    
    Signature ``BendID`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendID`` 
    
    :param bendId: 
    :type bendId: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendName: str = ...
    """
    Returns or sets  the bend name 
    
    <hr>
    
    Getter Method
    
    Signature ``BendName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendName`` 
    
    :param bendName: 
    :type bendName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: BendListItemBuilder = ...  # unknown typename


class ContourFlangeBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContourFlangeBuilderSectionSideOptions():
    """
    This enum represents the side of the section in which material is created. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", " - "
       "Right", " - "
    """
    Left = 0  # ContourFlangeBuilderSectionSideOptionsMemberType
    Right = 1  # ContourFlangeBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ContourFlangeBuilderSweepSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContourFlangeBuilderSweepSideOptions():
    """
    This enum represents the side in which the contour flange will be swept.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", " - "
       "SectionReverseNormalSide", " - "
    """
    SectionNormalSide = 0  # ContourFlangeBuilderSweepSideOptionsMemberType
    SectionReverseNormalSide = 1  # ContourFlangeBuilderSweepSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ContourFlangeBuilderSweepTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContourFlangeBuilderSweepTypeOptions():
    """
    This enum represents the sweep type of the contour flange 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Finite", " - "
       "Symmetric", " - "
       "ToEnd", " - "
       "Chain", " - "
    """
    Finite = 0  # ContourFlangeBuilderSweepTypeOptionsMemberType
    Symmetric = 1  # ContourFlangeBuilderSweepTypeOptionsMemberType
    ToEnd = 2  # ContourFlangeBuilderSweepTypeOptionsMemberType
    Chain = 3  # ContourFlangeBuilderSweepTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ContourFlangeBuilder(SheetmetalBaseBuilder):
    """
    Represents a Contour Flange feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateContourFlangeFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class SectionSideOptions():
        """
        This enum represents the side of the section in which material is created. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", " - "
           "Right", " - "
        """
        Left = 0  # ContourFlangeBuilderSectionSideOptionsMemberType
        Right = 1  # ContourFlangeBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SweepSideOptions():
        """
        This enum represents the side in which the contour flange will be swept.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", " - "
           "SectionReverseNormalSide", " - "
        """
        SectionNormalSide = 0  # ContourFlangeBuilderSweepSideOptionsMemberType
        SectionReverseNormalSide = 1  # ContourFlangeBuilderSweepSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SweepTypeOptions():
        """
        This enum represents the sweep type of the contour flange 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Finite", " - "
           "Symmetric", " - "
           "ToEnd", " - "
           "Chain", " - "
        """
        Finite = 0  # ContourFlangeBuilderSweepTypeOptionsMemberType
        Symmetric = 1  # ContourFlangeBuilderSweepTypeOptionsMemberType
        ToEnd = 2  # ContourFlangeBuilderSweepTypeOptionsMemberType
        Chain = 3  # ContourFlangeBuilderSweepTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetThickness(self) -> NXOpen.Expression:
        """
        THE thickness of contour flange  
        
        Signature ``GetThickness()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetThickness(self, thickness: str) -> None:
        """
        Signature ``SetThickness(thickness)`` 
        
        :param thickness: 
        :type thickness: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.ContourFlangeBuilder.GetThickness` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetSweepDistance(self) -> NXOpen.Expression:
        """
        THE projection distance of contour flange  
        
        Signature ``GetSweepDistance()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetSweepDistance(self, sweepDistance: str) -> None:
        """
        Signature ``SetSweepDistance(sweepDistance)`` 
        
        :param sweepDistance: 
        :type sweepDistance: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.ContourFlangeBuilder.GetSweepDistance` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a Contour Flange or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendOptions: BendOptions = ...
    """
    Returns  the bend options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EdgeChain: NXOpen.Section = ...
    """
    Returns or sets  the section having chain edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeChain`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``EdgeChain`` 
    
    :param edgeChain: 
    :type edgeChain: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    IsSecondary: bool = ...
    """
    Returns or sets  the contour flange type.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsSecondary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``IsSecondary`` 
    
    :param isSecondary: 
    :type isSecondary: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MiterOptions: MiterOptions = ...
    """
    Returns  the miter options 
    
    <hr>
    
    Getter Method
    
    Signature ``MiterOptions`` 
    
    :returns:  Miter data  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the section of contour flange 
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns:  section of contour flange  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the sketch 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns:  sketch  
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch:  sketch  
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    SweepSide: ContourFlangeBuilderSweepSideOptions = ...
    """
    Returns or sets  the projection direction of contour flange 
    
    <hr>
    
    Getter Method
    
    Signature ``SweepSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSweepSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``SweepSide`` 
    
    :param sweepSide: 
    :type sweepSide: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSweepSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    SweepType: ContourFlangeBuilderSweepTypeOptions = ...
    """
    Returns or sets  the projection side of contour flange
    
    <hr>
    
    Getter Method
    
    Signature ``SweepType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSweepTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``SweepType`` 
    
    :param sweepType: 
    :type sweepType: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSweepTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ThicknessSide: ContourFlangeBuilderSectionSideOptions = ...
    """
    Returns or sets  the thickness side of contour flange 
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ThicknessSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: ContourFlangeBuilder = ...  # unknown typename


class EditCornerBuilderBendClosureTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EditCornerBuilderBendClosureTypeOptions():
    """
    This enum specifies the type of bend closure required at the corner. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Open", " - "
       "Closed", " - "
    """
    Open = 0  # EditCornerBuilderBendClosureTypeOptionsMemberType
    Closed = 1  # EditCornerBuilderBendClosureTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EditCornerBuilderPlateClosureTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EditCornerBuilderPlateClosureTypeOptions():
    """
    This enum specifies the type of plate closure required at the corner. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Closed", " - "
       "Overlapped", " - "
    """
    Closed = 0  # EditCornerBuilderPlateClosureTypeOptionsMemberType
    Overlapped = 1  # EditCornerBuilderPlateClosureTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EditCornerBuilderCornerReliefTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EditCornerBuilderCornerReliefTypeOptions():
    """
    This enum specifies the type of relief required at the corner.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "CircularCutout", " - "
    """
    NotSet = 0  # EditCornerBuilderCornerReliefTypeOptionsMemberType
    CircularCutout = 1  # EditCornerBuilderCornerReliefTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EditCornerBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilder`
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateEditCornerBuilder`
    
    Default values.
    
    ===================  ==========================================
    Property             Value
    ===================  ==========================================
    BendClosureType      Open 
    -------------------  ------------------------------------------
    CornerReliefType     None 
    -------------------  ------------------------------------------
    Diameter.Value       2.5 (millimeters part), 0.1 (inches part) 
    -------------------  ------------------------------------------
    OverlapRatio.Value   1 
    -------------------  ------------------------------------------
    PlateClosureType     Closed 
    -------------------  ------------------------------------------
    PlateGap.Value       0 (millimeters part), 0 (inches part) 
    ===================  ==========================================
    
    .. versionadded:: NX7.5.0
    """
    
    class BendClosureTypeOptions():
        """
        This enum specifies the type of bend closure required at the corner. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Open", " - "
           "Closed", " - "
        """
        Open = 0  # EditCornerBuilderBendClosureTypeOptionsMemberType
        Closed = 1  # EditCornerBuilderBendClosureTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PlateClosureTypeOptions():
        """
        This enum specifies the type of plate closure required at the corner. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Closed", " - "
           "Overlapped", " - "
        """
        Closed = 0  # EditCornerBuilderPlateClosureTypeOptionsMemberType
        Overlapped = 1  # EditCornerBuilderPlateClosureTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CornerReliefTypeOptions():
        """
        This enum specifies the type of relief required at the corner.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "CircularCutout", " - "
        """
        NotSet = 0  # EditCornerBuilderCornerReliefTypeOptionsMemberType
        CircularCutout = 1  # EditCornerBuilderCornerReliefTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Add a face pair.  
        
        Signature ``AddFacePair(firstFace, secondFace)`` 
        
        :param firstFace:   A bend face from a bend  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:   A bend face from an adjacent bend  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFacePair(self, index: int) -> tuple:
        """
        Return the face pair.  
        
        Signature ``GetFacePair(index)`` 
        
        :param index:  Index of the desired face pair  
        :type index: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (firstFace, secondFace). firstFace is a :py:class:`NXOpen.Face`.   First face of the face pair secondFace is a :py:class:`NXOpen.Face`.   Second face of the face pair 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetNumberOfFacePairs(self) -> int:
        """
        Returns the number of face pairs already identified for the three bend corner feature.  
        
        Signature ``GetNumberOfFacePairs()`` 
        
        :returns:  The number of face pairs currently identified  
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def RemoveFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Removes a face pair (that represents a unique corner) from the list of face pairs already added.  
        
        Signature ``RemoveFacePair(firstFace, secondFace)`` 
        
        :param firstFace:  A face from an already selected face pair  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:  The other face from the face pair  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    BendClosureType: EditCornerBuilderBendClosureTypeOptions = ...
    """
    Returns or sets  the bend type 
    
    <hr>
    
    Getter Method
    
    Signature ``BendClosureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderBendClosureTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendClosureType`` 
    
    :param bends: 
    :type bends: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderBendClosureTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    CornerReliefType: EditCornerBuilderCornerReliefTypeOptions = ...
    """
    Returns or sets  the corner relief type 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderCornerReliefTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CornerReliefType`` 
    
    :param cornerRelief: 
    :type cornerRelief: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderCornerReliefTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the diameter for a circular cutout 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    OverlapRatio: NXOpen.Expression = ...
    """
    Returns  the overlap ratio between plates 
    
    <hr>
    
    Getter Method
    
    Signature ``OverlapRatio`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    PlateClosureType: EditCornerBuilderPlateClosureTypeOptions = ...
    """
    Returns or sets  the plate type 
    
    <hr>
    
    Getter Method
    
    Signature ``PlateClosureType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderPlateClosureTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PlateClosureType`` 
    
    :param plates: 
    :type plates: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilderPlateClosureTypeOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    PlateGap: NXOpen.Expression = ...
    """
    Returns  the gap value between plates
    
    <hr>
    
    Getter Method
    
    Signature ``PlateGap`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ReverseOverlap: bool = ...
    """
    Returns or sets  whether the overlap is reversed or not 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseOverlap`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseOverlap`` 
    
    :param reverseOverlap: 
    :type reverseOverlap: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: EditCornerBuilder = ...  # unknown typename


class EdgeRipBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Edge Rip feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateEdgeRipFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    def SetRipEdges(self, ripEdges: 'list[NXOpen.Edge]') -> None:
        """
        Edges to rip 
        
        Signature ``SetRipEdges(ripEdges)`` 
        
        :param ripEdges:  Rip Edges  
        :type ripEdges: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetRipEdges(self) -> 'list[NXOpen.Edge]':
        """
        Edges to rip  
        
        Signature ``GetRipEdges()`` 
        
        :returns:  Rip Edges  
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a Edge Rip or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    Section: NXOpen.Section = ...
    """
    Returns or sets  the section used by Edge Rip 
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the Slave Sketch used by the Edge Rip, If one exists.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: EdgeRipBuilder = ...  # unknown typename


class BreakCornerBuilderTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BreakCornerBuilderTypeOptions():
    """
    This enum represents the break corner type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Fillet", " - "
       "ChamferEqualSetback", " - "
    """
    Fillet = 0  # BreakCornerBuilderTypeOptionsMemberType
    ChamferEqualSetback = 1  # BreakCornerBuilderTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BreakCornerBuilder(SheetmetalBaseBuilder):
    """
    Represents a break corner feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBreakCornerFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class TypeOptions():
        """
        This enum represents the break corner type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Fillet", " - "
           "ChamferEqualSetback", " - "
        """
        Fillet = 0  # BreakCornerBuilderTypeOptionsMemberType
        ChamferEqualSetback = 1  # BreakCornerBuilderTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetValue(self, filletRadiusOrSetback: str) -> None:
        """
        Signature ``SetValue(filletRadiusOrSetback)`` 
        
        :param filletRadiusOrSetback:  Either fillet radius or setback value (depending on the type of break corner) 
        :type filletRadiusOrSetback: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.BreakCornerBuilder.Value` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetEdges(self, edges: 'list[NXOpen.Edge]') -> None:
        """
        The array of input edges for the break corner.  
        
        Signature ``SetEdges(edges)`` 
        
        :param edges:  Edge list  
        :type edges: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetEdges(self) -> 'list[NXOpen.Edge]':
        """
        The array of input edges for the break corner.  
        
        Signature ``GetEdges()`` 
        
        :returns:  Edge list  
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetFaces(self, faces: 'list[NXOpen.Face]') -> None:
        """
        The array of input faces that implicitly include all connected sharp thickness edges as input for the break corner.  
        
        Signature ``SetFaces(faces)`` 
        
        :param faces:  Face list  
        :type faces: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetFaces(self) -> 'list[NXOpen.Face]':
        """
        The array of input faces that implicitly include all connected sharp thickness edges as input for the break corner.  
        
        Signature ``GetFaces()`` 
        
        :returns:  Face list  
        :rtype: list of :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify that the builder data is valid for creating a break corner.  
        
        If the Builder data is valid, return value is 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data validity flag (zero for valid and non-zero for invalid)  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    Type: BreakCornerBuilderTypeOptions = ...
    """
    Returns or sets  the type of the break corner.  
    
    Specify :py:class:`Features.SheetMetal.BreakCornerBuilderTypeOptions.Fillet <Features.SheetMetal.BreakCornerBuilderTypeOptions>` to fillet the edge.
    Specify :py:class:`Features.SheetMetal.BreakCornerBuilderTypeOptions.ChamferEqualSetback <Features.SheetMetal.BreakCornerBuilderTypeOptions>` to chamfer the edge.
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns:  Break corner type  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BreakCornerBuilderTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type:  Break corner type  
    :type type: :py:class:`NXOpen.Features.SheetMetal.BreakCornerBuilderTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Value: NXOpen.Expression = ...
    """
    Returns  the fillet radius or the setback value, depending on the type of the break corner.  
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns:  Either fillet radius or setback value (depending on the type of break corner)  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: BreakCornerBuilder = ...  # unknown typename


class JogBuilderDirectionTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JogBuilderDirectionTypeOptions():
    """
    this enum represents the  direction for the Jog. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "jog created on the side of the section normal."
       "SectionReverseNormalSide", "jog created on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # JogBuilderDirectionTypeOptionsMemberType
    SectionReverseNormalSide = 1  # JogBuilderDirectionTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class JogBuilderFixedSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JogBuilderFixedSideOptions():
    """
    The "left" option represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionSideLeft", "Side pointed to by the inverse of the tangent cross normal vector"
       "SectionSideRight", "Side pointed to by the tangent cross normal vector"
    """
    SectionSideLeft = 0  # JogBuilderFixedSideOptionsMemberType
    SectionSideRight = 1  # JogBuilderFixedSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class JogBuilderDimensionTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JogBuilderDimensionTypeOptions():
    """
    the Dimension options for jog. This specifies whether the Jog's depth must be measured from the plane to which the section
    is attached or from the 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Offset", "the actual depth will be depth plus the thickness of sheet."
       "Full", "the actual extent distance will be the value specified as depth."
    """
    Offset = 0  # JogBuilderDimensionTypeOptionsMemberType
    Full = 1  # JogBuilderDimensionTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class JogBuilderBendLocationOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JogBuilderBendLocationOptions():
    """
    Represents the bend location type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", " - "
       "MaterialOutside", " - "
       "BendOutside", " - "
    """
    MaterialInside = 0  # JogBuilderBendLocationOptionsMemberType
    MaterialOutside = 1  # JogBuilderBendLocationOptionsMemberType
    BendOutside = 2  # JogBuilderBendLocationOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class JogBuilder(SheetmetalBaseBuilder):
    """
    Represents a Jog feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateJogFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class DirectionTypeOptions():
        """
        this enum represents the  direction for the Jog. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "jog created on the side of the section normal."
           "SectionReverseNormalSide", "jog created on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # JogBuilderDirectionTypeOptionsMemberType
        SectionReverseNormalSide = 1  # JogBuilderDirectionTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FixedSideOptions():
        """
        The "left" option represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionSideLeft", "Side pointed to by the inverse of the tangent cross normal vector"
           "SectionSideRight", "Side pointed to by the tangent cross normal vector"
        """
        SectionSideLeft = 0  # JogBuilderFixedSideOptionsMemberType
        SectionSideRight = 1  # JogBuilderFixedSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DimensionTypeOptions():
        """
        the Dimension options for jog. This specifies whether the Jog's depth must be measured from the plane to which the section
        is attached or from the 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Offset", "the actual depth will be depth plus the thickness of sheet."
           "Full", "the actual extent distance will be the value specified as depth."
        """
        Offset = 0  # JogBuilderDimensionTypeOptionsMemberType
        Full = 1  # JogBuilderDimensionTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendLocationOptions():
        """
        Represents the bend location type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", " - "
           "MaterialOutside", " - "
           "BendOutside", " - "
        """
        MaterialInside = 0  # JogBuilderBendLocationOptionsMemberType
        MaterialOutside = 1  # JogBuilderBendLocationOptionsMemberType
        BendOutside = 2  # JogBuilderBendLocationOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetHeight(self) -> NXOpen.Expression:
        """
        Height of the Jog 
        
        Signature ``GetHeight()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetHeight(self, height: str) -> None:
        """
        Signature ``SetHeight(height)`` 
        
        :param height: 
        :type height: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.JogBuilder.GetHeight` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a jog or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendLocation: JogBuilderBendLocationOptions = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``BendLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JogBuilderBendLocationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendLocation`` 
    
    :param bendLocation: 
    :type bendLocation: :py:class:`NXOpen.Features.SheetMetal.JogBuilderBendLocationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options.  
    
    The option :py:class:`Features.SheetMetal.BendOptionsCornerReliefTypeOptions.None <Features.SheetMetal.BendOptionsCornerReliefTypeOptions>` is not valid for the :py:class:`Features.Jog` starting NX11 onwards.
    
    From NX 12 :py:meth:`Features.SheetMetal.BendOptions.ExtendBendRelief`
    has no effect on the Jog feature.
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DimensionType: JogBuilderDimensionTypeOptions = ...
    """
    Returns or sets  the Offset Dimension
    
    The actual extent distance of the Jog will be determined by the active dimension option.
    In case of :py:class:`Features.SheetMetal.JogBuilderDimensionTypeOptions.Offset <Features.SheetMetal.JogBuilderDimensionTypeOptions>` the actual extent distance will be offset dimension distance plus the thickness of sheet.
    In case of :py:class:`Features.SheetMetal.JogBuilderDimensionTypeOptions.Full <Features.SheetMetal.JogBuilderDimensionTypeOptions>` the actual extent distance will be the Full dimension distance.
    
    <hr>
    
    Getter Method
    
    Signature ``DimensionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JogBuilderDimensionTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``DimensionType`` 
    
    :param dimensionType: 
    :type dimensionType: :py:class:`NXOpen.Features.SheetMetal.JogBuilderDimensionTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DirectionType: JogBuilderDirectionTypeOptions = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``DirectionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JogBuilderDirectionTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``DirectionType`` 
    
    :param directionType: 
    :type directionType: :py:class:`NXOpen.Features.SheetMetal.JogBuilderDirectionTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ExtendProfile: bool = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendProfile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendProfile`` 
    
    :param extendOption: 
    :type extendOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FixedSide: JogBuilderFixedSideOptions = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``FixedSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JogBuilderFixedSideOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``FixedSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.JogBuilderFixedSideOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TargetFace: NXOpen.Face = ...
    """
    Returns or sets  the target face on which jog feature applies.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFace`` 
    
    :returns:  Returns the target face on which the jog feature is created.  
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TargetFace`` 
    
    :param targetFace:  A planar non-deform sheet metal face on which the jog feature is to be created.  
    :type targetFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: JogBuilder = ...  # unknown typename


class TabBuilderThicknessSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TabBuilderThicknessSideOptions():
    """
    This enum represents the extent direction for the Tab. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Material created on the side of the section normal."
       "SectionReverseNormalSide", "Material created on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # TabBuilderThicknessSideOptionsMemberType
    SectionReverseNormalSide = 1  # TabBuilderThicknessSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TabBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TabBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the dimple punches material. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # TabBuilderSectionSideOptionsMemberType
    Right = 1  # TabBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TabBuilder(SheetmetalBaseBuilder):
    """
    Represents a Tab feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateTabFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class ThicknessSideOptions():
        """
        This enum represents the extent direction for the Tab. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Material created on the side of the section normal."
           "SectionReverseNormalSide", "Material created on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # TabBuilderThicknessSideOptionsMemberType
        SectionReverseNormalSide = 1  # TabBuilderThicknessSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the dimple punches material. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # TabBuilderSectionSideOptionsMemberType
        Right = 1  # TabBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetThickness(self, thickness: str) -> None:
        """
        Signature ``SetThickness(thickness)`` 
        
        :param thickness:  Tab thickness 
        :type thickness: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.TabBuilder.Thickness` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a Tab or not.  
        
        If the Builder data is valid, returned value shall be 0.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def UpdateReferenceCurves(self) -> NXOpen.Features.Feature:
        """
        This is only applicable for base tab created with bends.  
        
        This extracts boundary curves of the faces
        that are attached to the planes specified by  :py:meth:`NXOpen.Features.SheetMetal.MultiBendBendPropertiesBuilder.Plane``. 
        
        Signature ``UpdateReferenceCurves()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    IsSecondary: bool = ...
    """
    Returns or sets  the tab type 
    
    <hr>
    
    Getter Method
    
    Signature ``IsSecondary`` 
    
    :returns:  tab type  
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``IsSecondary`` 
    
    :param isSecondary:  tab type  
    :type isSecondary: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MaterialSide: TabBuilderSectionSideOptions = ...
    """
    Returns or sets  the material side value of secondary tab 
    
    <hr>
    
    Getter Method
    
    Signature ``MaterialSide`` 
    
    :returns:  material side value  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.TabBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``MaterialSide`` 
    
    :param sectionSide:  material side value  
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.TabBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MultiBendPropertiesList: FeatureBendPropertiesListBuilder = ...
    """
    Returns  the multi bend  properties list 
    
    <hr>
    
    Getter Method
    
    Signature ``MultiBendPropertiesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesListBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the section of tab 
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns:  Section tag  
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section:  section tag  
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the sketch of tab 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns:  Sketch tag  
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch:  sketch tag  
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TargetBody: NXOpen.Body = ...
    """
    Returns or sets  the target body on which the secondary tab is created.  
    
    Use :py:meth:`NXOpen.Features.SheetMetal.TabBuilder.IsSecondary`` to determine whether this is a secondary tab.
    
    <hr>
    
    Getter Method
    
    Signature ``TargetBody`` 
    
    :returns:  Returns the target body on which the secondary tab is created.  
    :rtype: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TargetBody`` 
    
    :param targetBody:  A sheet metal body on which secondary tab is to be created.  
    :type targetBody: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the thickness of tab 
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns:  Tab thickness 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ThicknessSide: TabBuilderThicknessSideOptions = ...
    """
    Returns or sets  the sweep direction flag of tab 
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessSide`` 
    
    :returns:  Sweep Direction Flag 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.TabBuilderThicknessSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ThicknessSide`` 
    
    :param flag:  Sweep Direction Flag  
    :type flag: :py:class:`NXOpen.Features.SheetMetal.TabBuilderThicknessSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: TabBuilder = ...  # unknown typename


class JoggleBuilderLimitTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class JoggleBuilderLimitTypes():
    """
    This enum defines the limit types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Single", " - "
       "Twin", " - "
    """
    Single = 0  # JoggleBuilderLimitTypesMemberType
    Twin = 1  # JoggleBuilderLimitTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class JoggleBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Sheetmetal joggle builder class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateJoggleBuilder`
    
    Default values.
    
    ========================  =======
    Property                  Value
    ========================  =======
    Adjustment.Value          0 
    ------------------------  -------
    FlatPatternCompensation   0 
    ------------------------  -------
    LimitType                 Single 
    ------------------------  -------
    SymmetricSides            1 
    ========================  =======
    
    .. versionadded:: NX11.0.0
    """
    
    class LimitTypes():
        """
        This enum defines the limit types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Single", " - "
           "Twin", " - "
        """
        Single = 0  # JoggleBuilderLimitTypesMemberType
        Twin = 1  # JoggleBuilderLimitTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateJoggleInputListItem(self) -> JoggleInputListItemBuilder:
        """
        Create a input list item.  
        
        Signature ``CreateJoggleInputListItem()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    Adjustment: NXOpen.Expression = ...
    """
    Returns  the adjustment 
    
    <hr>
    
    Getter Method
    
    Signature ``Adjustment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    EndPlane: NXOpen.Plane = ...
    """
    Returns or sets  the end plane 
    
    <hr>
    
    Getter Method
    
    Signature ``EndPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndPlane`` 
    
    :param endPlane: 
    :type endPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    FlatPatternCompensation: bool = ...
    """
    Returns or sets  the flat pattern compensation 
    
    <hr>
    
    Getter Method
    
    Signature ``FlatPatternCompensation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlatPatternCompensation`` 
    
    :param flatPatternCompensation: 
    :type flatPatternCompensation: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    InputList: JoggleInputListItemBuilderList = ...
    """
    Returns  the input list 
    
    <hr>
    
    Getter Method
    
    Signature ``InputList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilderList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    LimitType: JoggleBuilderLimitTypes = ...
    """
    Returns or sets  the limit type 
    
    <hr>
    
    Getter Method
    
    Signature ``LimitType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleBuilderLimitTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LimitType`` 
    
    :param limitType: 
    :type limitType: :py:class:`NXOpen.Features.SheetMetal.JoggleBuilderLimitTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Side1Options: JoggleSideOptionsBuilder = ...
    """
    Returns  the joggle side 1 options 
    
    <hr>
    
    Getter Method
    
    Signature ``Side1Options`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleSideOptionsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Side2Options: JoggleSideOptionsBuilder = ...
    """
    Returns  the joggle side 2 options 
    
    <hr>
    
    Getter Method
    
    Signature ``Side2Options`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleSideOptionsBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    StartPlane: NXOpen.Plane = ...
    """
    Returns or sets  the start plane 
    
    <hr>
    
    Getter Method
    
    Signature ``StartPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartPlane`` 
    
    :param startPlane: 
    :type startPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SymmetricSides: bool = ...
    """
    Returns or sets  the symmetric sides 
    
    <hr>
    
    Getter Method
    
    Signature ``SymmetricSides`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SymmetricSides`` 
    
    :param symmetricSides: 
    :type symmetricSides: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UseMaterialTable: bool = ...
    """
    Returns or sets  the Use Material Table 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMaterialTable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseMaterialTable`` 
    
    :param useMaterialTable: 
    :type useMaterialTable: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: JoggleBuilder = ...  # unknown typename


class JoggleInputListItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[JoggleInputListItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: JoggleInputListItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: JoggleInputListItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> JoggleInputListItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
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
    def Erase(self, obj: JoggleInputListItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: JoggleInputListItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[JoggleInputListItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[JoggleInputListItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
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
    def Swap(self, object1: JoggleInputListItemBuilder, object2: JoggleInputListItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: JoggleInputListItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.SheetMetal.JoggleInputListItemBuilder` 
        
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
    Null: JoggleInputListItemBuilderList = ...  # unknown typename


class FlatPatternBuilder(SheetmetalBaseBuilder):
    """
    Represents a Flat Pattern feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateFlatPatternBuilder`
    
    Default values.
    
    ===================================  ======================================
    Property                             Value
    ===================================  ======================================
    Associative                          true 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.TreatmentType   None 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.UseGlobal       1 
    -----------------------------------  --------------------------------------
    InnerCornerTreatment.Value.Value     0 (millimeters part), 0 (inches part) 
    ===================================  ======================================
    
    .. versionadded:: NX5.0.0
    """
    
    def GenerateMoldLines(self) -> None:
        """
        Set the flag to generate inner and outer mold lines for flat pattern features created before NX11.  
        
        Signature ``GenerateMoldLines()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    AddedGeometry: NXOpen.Section = ...
    """
    Returns  the added geometry selection 
    
    <hr>
    
    Getter Method
    
    Signature ``AddedGeometry`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Associative: bool = ...
    """
    Returns or sets  the setting which decides whether the flattened solid will be associative to parent body.  
    
    **  This is applicable to flat pattern features created in NX12 and later release.
    **  Cannot change during feature edit if the feature was created as non associative.
    
    <hr>
    
    Getter Method
    
    Signature ``Associative`` 
    
    :returns:  True = Feature is associative, False = Feature is not associative.  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Associative`` 
    
    :param associative:  True = Feature is associative, False = Feature is not associative.  
    :type associative: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FixAtTimestamp: bool = ...
    """
    Returns or sets  the setting which decides whether the flattened solid will be fixed at timestamp.  
    
    **  This is applicable to flat pattern features created in NX12 and later release.
    **  Cannot change during feature edit if the feature was created as fixed at timestamp.
    
    <hr>
    
    Getter Method
    
    Signature ``FixAtTimestamp`` 
    
    :returns:  True = Fix at Timestamp, False = Do not Fix at Timestamp.  
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FixAtTimestamp`` 
    
    :param fixAtTimestamp:  True = Fix at Timestamp, False = Do not Fix at Timestamp.  
    :type fixAtTimestamp: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FlatPatternViewName: str = ...
    """
    Returns  the flat pattern view name string 
    
    <hr>
    
    Getter Method
    
    Signature ``FlatPatternViewName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    HoleTreatment: HoleTreatmentBuilder = ...
    """
    Returns  the hole treatment object
    **  This is applicable to flat pattern features created in NX12 and later release.  
    
    <hr>
    
    Getter Method
    
    Signature ``HoleTreatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.HoleTreatmentBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    InnerCornerTreatment: CornerTreatmentBuilder = ...
    """
    Returns  the inner corner treatment corner object 
    
    <hr>
    
    Getter Method
    
    Signature ``InnerCornerTreatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Orientation: FlatSolidBuilderOrientationType = ...
    """
    Returns or sets  the option which decides if the flattened solid will be transformed to Absolute CSYS.  
    
    **  This flag will only be used if the Upward face belongs to a formed sheet metal body.
    **  If a face from a flat solid is selected, this value will be ignored.
    **  This is applicable to flat solid / flat pattern features created (or renewed) to NX12 and later release.
    
    <hr>
    
    Getter Method
    
    Signature ``Orientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderOrientationType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Orientation`` 
    
    :param orientation: 
    :type orientation: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilderOrientationType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OrientationCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the orientation csys 
    **  This is applicable to flat pattern features created (or renewed) in NX12 and later release.  
    
    <hr>
    
    Getter Method
    
    Signature ``OrientationCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OrientationCsys`` 
    
    :param csys: 
    :type csys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OuterCornerTreatment: CornerTreatmentBuilder = ...
    """
    Returns  the outer corner treatment corner object 
    
    <hr>
    
    Getter Method
    
    Signature ``OuterCornerTreatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilder` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ReferenceVertex: NXOpen.Point3d = ...
    """
    Returns or sets  the end of the edge where the tangent will define the x axis for flat as solid.  
    
    This value will only
    **  be used when a face from a formed solid body is picked as Upward face. If a face from a flat solid is selected,
    **  this value will be ignored.
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceVertex`` 
    
    :returns:  One of the end points of the reference edge.  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceVertex`` 
    
    :param vertex:  One of the end points of the reference edge.  
    :type vertex: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ShowInteriorFeatureCurves: bool = ...
    """
    Returns or sets  the show interior feature curves toggle value 
    
    <hr>
    
    Getter Method
    
    Signature ``ShowInteriorFeatureCurves`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ShowInteriorFeatureCurves`` 
    
    :param showInteriorFeatureCurves: 
    :type showInteriorFeatureCurves: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TransformToAbsoluteCsys: bool = ...
    """
    Returns or sets  the flag which decides if the flattened solid will be transformed to Absolute CSYS.  
    
    This flag will only be 
    **  used if the Upward face belongs to a formed sheet metal body. If a face from a flat solid is selected,
    **  this value will be ignored.
    **  This is applicable to flat solid / flat pattern features created before NX12 release and not yet renewed.
    **  The API can not be deprecated because it is required to edit features created before NX12 release.
    **  But user should modify automation programs written before NX12 and replace use this option with the orientation option,
    **  before using the program to create new features in NX12 or later.
    
    <hr>
    
    Getter Method
    
    Signature ``TransformToAbsoluteCsys`` 
    
    :returns:  True = Transform to ABS, False = Do not transform to ABS.  
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TransformToAbsoluteCsys`` 
    
    :param transformFlag:  True = Transform to ABS, False = Do not transform to ABS.  
    :type transformFlag: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    UpwardFace: NXOpen.SelectFace = ...
    """
    Returns  the upward face selection 
    
    <hr>
    
    Getter Method
    
    Signature ``UpwardFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    XAxisEdge: NXOpen.SelectEdge = ...
    """
    Returns  the x axis edge selection.  
    
    This edge selection is necessary when a face from a formed 
    **  solid body is picked as Upward face. If a face from a flat solid is selected,
    **  this value will be ignored. 
    
    <hr>
    
    Getter Method
    
    Signature ``XAxisEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: FlatPatternBuilder = ...  # unknown typename


class AeroFlatPatternBuilder(FlatPatternBuilder):
    """
    Represents a Flat Pattern feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateFlatPatternBuilder`
    
    Default values.
    
    ============  =====
    Property      Value
    ============  =====
    Associative   true 
    ============  =====
    
    .. versionadded:: NX6.0.0
    """
    Null: AeroFlatPatternBuilder = ...  # unknown typename


class ResizeBendRadiusBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ResizeBendRadiusBuilderTypes():
    """
    This enum represents the feature types. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FixedFoldedLength", " - "
       "FixedUnfoldedLength", " - "
    """
    FixedFoldedLength = 0  # ResizeBendRadiusBuilderTypesMemberType
    FixedUnfoldedLength = 1  # ResizeBendRadiusBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ResizeBendRadiusBuilderBendReliefTypeOptions():
    """
    This enum represents the bend relief type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Square", " - "
       "Round", " - "
       "NotSet", " - "
    """
    Square = 0  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
    Round = 1  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
    NotSet = 2  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ResizeBendRadiusBuilder(SheetmetalBaseBuilder):
    """
    Represents a ResizeBendRadius feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateResizeBendRadiusFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class Types():
        """
        This enum represents the feature types. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FixedFoldedLength", " - "
           "FixedUnfoldedLength", " - "
        """
        FixedFoldedLength = 0  # ResizeBendRadiusBuilderTypesMemberType
        FixedUnfoldedLength = 1  # ResizeBendRadiusBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendReliefTypeOptions():
        """
        This enum represents the bend relief type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Square", " - "
           "Round", " - "
           "NotSet", " - "
        """
        Square = 0  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
        Round = 1  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
        NotSet = 2  # ResizeBendRadiusBuilderBendReliefTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetBendReliefType(self, bendReliefType: ResizeBendRadiusBuilderBendReliefTypeOptions) -> None:
        """
        Signature ``SetBendReliefType(bendReliefType)`` 
        
        :param bendReliefType: 
        :type bendReliefType: :py:class:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilderBendReliefTypeOptions` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendFaces: NXOpen.ScCollector = ...
    """
    Returns  the bend faces 
    
    <hr>
    
    Getter Method
    
    Signature ``BendFaces`` 
    
    :returns:  The Bend Face Collection   
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendRadius: NXOpen.Expression = ...
    """
    Returns  the bend radius 
    
    <hr>
    
    Getter Method
    
    Signature ``BendRadius`` 
    
    :returns:  The Bend Radius   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendReliefDepth: NXOpen.Expression = ...
    """
    Returns  the bend relief depth.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendReliefType: ResizeBendRadiusBuilderBendReliefTypeOptions = ...
    """
    Returns  the relief type for the resize bend radius feature.  
    
    The options are in :py:meth:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilder.BendReliefType`. 
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilderBendReliefTypeOptions` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendReliefWidth: NXOpen.Expression = ...
    """
    Returns  the bend relief width.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReferenceEntity: NXOpen.SelectDisplayableObject = ...
    """
    Returns  the non-thickness planar face or linear edge to remain fixed while bend is resized 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceEntity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectDisplayableObject` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    """
    Type: ResizeBendRadiusBuilderTypes = ...
    """
    Returns or sets  the feature type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilderTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilderTypes` 
    
    .. versionadded:: NX7.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: ResizeBendRadiusBuilder = ...  # unknown typename


class ApplicationContextMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ApplicationContext():
    """
    This is the enum representing application context of the feature 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NxSheetMetal", "Sheet Metal application context"
       "FlexiblePrintedCircuitDesign", "Flexible Printed Circuit Design application context"
       "AerospaceSheetMetal", "Aerospace Sheet Metal application context"
    """
    NxSheetMetal = 0  # ApplicationContextMemberType
    FlexiblePrintedCircuitDesign = 1  # ApplicationContextMemberType
    AerospaceSheetMetal = 2  # ApplicationContextMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendBuilderBendDirectionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendBuilderBendDirectionOptions():
    """
    This enum represents the Bend Direction for Bend.   
    
    .. versionadded:: NX5.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Bend is created on the side of the section normal."
       "SectionReverseNormalSide", "Bend is created on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # BendBuilderBendDirectionOptionsMemberType
    SectionReverseNormalSide = 1  # BendBuilderBendDirectionOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendBuilderFixedSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendBuilderFixedSideOptions():
    """
    This enum represents the Fixed Side for Bend.   
    
    .. versionadded:: NX5.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionSideLeft", "Side pointed to by the inverse of the tangent cross normal vector"
       "SectionSideRight", "Side pointed to by the tangent cross normal vector"
    """
    SectionSideLeft = 0  # BendBuilderFixedSideOptionsMemberType
    SectionSideRight = 1  # BendBuilderFixedSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendBuilderBendLocationOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendBuilderBendLocationOptions():
    """
    This enum represents the Bend Location (Material Side) for Bend.   
    
    .. versionadded:: NX5.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "OuterMoldLine", " - "
       "CenterLine", " - "
       "InnerMoldLine", " - "
       "MaterialInside", " - "
       "MaterialOutside", " - "
    """
    OuterMoldLine = 0  # BendBuilderBendLocationOptionsMemberType
    CenterLine = 1  # BendBuilderBendLocationOptionsMemberType
    InnerMoldLine = 2  # BendBuilderBendLocationOptionsMemberType
    MaterialInside = 3  # BendBuilderBendLocationOptionsMemberType
    MaterialOutside = 4  # BendBuilderBendLocationOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendBuilder(SheetmetalBaseBuilder):
    """
    Represents a Bend feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBendFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class BendDirectionOptions():
        """
        This enum represents the Bend Direction for Bend.   
        
        .. versionadded:: NX5.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Bend is created on the side of the section normal."
           "SectionReverseNormalSide", "Bend is created on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # BendBuilderBendDirectionOptionsMemberType
        SectionReverseNormalSide = 1  # BendBuilderBendDirectionOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FixedSideOptions():
        """
        This enum represents the Fixed Side for Bend.   
        
        .. versionadded:: NX5.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionSideLeft", "Side pointed to by the inverse of the tangent cross normal vector"
           "SectionSideRight", "Side pointed to by the tangent cross normal vector"
        """
        SectionSideLeft = 0  # BendBuilderFixedSideOptionsMemberType
        SectionSideRight = 1  # BendBuilderFixedSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendLocationOptions():
        """
        This enum represents the Bend Location (Material Side) for Bend.   
        
        .. versionadded:: NX5.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "OuterMoldLine", " - "
           "CenterLine", " - "
           "InnerMoldLine", " - "
           "MaterialInside", " - "
           "MaterialOutside", " - "
        """
        OuterMoldLine = 0  # BendBuilderBendLocationOptionsMemberType
        CenterLine = 1  # BendBuilderBendLocationOptionsMemberType
        InnerMoldLine = 2  # BendBuilderBendLocationOptionsMemberType
        MaterialInside = 3  # BendBuilderBendLocationOptionsMemberType
        MaterialOutside = 4  # BendBuilderBendLocationOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetBendAngle(self) -> NXOpen.Expression:
        """
        Returns the Bend Angle  
        
        Signature ``GetBendAngle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetBendAngle(self, bendAngle: str) -> None:
        """
        Sets the Bend Angle 
        
        Signature ``SetBendAngle(bendAngle)`` 
        
        :param bendAngle: 
        :type bendAngle: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating bend or not.  
        
        If the Builder data is valid, returned value should be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendLocation: BendBuilderBendLocationOptions = ...
    """
    Returns or sets  the Bend Location (Material Side) 
    
    <hr>
    
    Getter Method
    
    Signature ``BendLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendBuilderBendLocationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendLocation`` 
    
    :param bendLocation: 
    :type bendLocation: :py:class:`NXOpen.Features.SheetMetal.BendBuilderBendLocationOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendOptions: BendOptions = ...
    """
    Returns  the Bend Options.  
    
    The option :py:class:`Features.SheetMetal.BendOptionsCornerReliefTypeOptions.None <Features.SheetMetal.BendOptionsCornerReliefTypeOptions>` is not valid for the :py:class:`Features.Bend` starting NX11 onwards.
    
    From NX 12 :py:meth:`Features.SheetMetal.BendOptions.ExtendBendRelief`
    has no effect on the Bend feature.
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Direction: BendBuilderBendDirectionOptions = ...
    """
    Returns or sets  the Bend Direction
    
    <hr>
    
    Getter Method
    
    Signature ``Direction`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendBuilderBendDirectionOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Direction`` 
    
    :param direction: 
    :type direction: :py:class:`NXOpen.Features.SheetMetal.BendBuilderBendDirectionOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ExtendProfile: bool = ...
    """
    Returns or sets  the Extend Option 
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendProfile`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendProfile`` 
    
    :param extendOption: 
    :type extendOption: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FixedSide: BendBuilderFixedSideOptions = ...
    """
    Returns or sets  the Fixed Side 
    
    <hr>
    
    Getter Method
    
    Signature ``FixedSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendBuilderFixedSideOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``FixedSide`` 
    
    :param fixedSide: 
    :type fixedSide: :py:class:`NXOpen.Features.SheetMetal.BendBuilderFixedSideOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the Section 
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the Sketch 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TargetFace: NXOpen.Face = ...
    """
    Returns or sets  the target face on which bend feature applies.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFace`` 
    
    :returns:  Returns the target face on which the bend feature is created.  
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TargetFace`` 
    
    :param targetFace:  A planar non-deform sheet metal face on which the bend feature is to be created.  
    :type targetFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: BendBuilder = ...  # unknown typename


class BendListItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[BendListItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: BendListItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: BendListItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> BendListItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
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
    def Erase(self, obj: BendListItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: BendListItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[BendListItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[BendListItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
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
    def Swap(self, object1: BendListItemBuilder, object2: BendListItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: BendListItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
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
    Null: BendListItemBuilderList = ...  # unknown typename


class SheetmetalManager():
    """
    Represents an object that manages sheetmetal features   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Features.FeatureCollection`
    
    .. versionadded:: NX4.0.0
    """
    
    def CreateDimpleFeatureBuilder(self, dimple: NXOpen.Features.Feature) -> DimpleBuilder:
        """
        Create a NXSM Dimple feature Builder 
        
        Signature ``CreateDimpleFeatureBuilder(dimple)`` 
        
        :param dimple:  The Dimple for which builder needs to be constructed. NULL for creating a new dimple  
        :type dimple: :py:class:`NXOpen.Features.Feature` 
        :returns:  DimpleBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.DimpleBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateDrawnCutoutFeatureBuilder(self, dCutout: NXOpen.Features.Feature) -> DrawnCutoutBuilder:
        """
        Create a NXSM Drawn Cutout feature Builder 
        
        Signature ``CreateDrawnCutoutFeatureBuilder(dCutout)`` 
        
        :param dCutout:  The Drawn Cutout for which builder needs to be constructed. NULL for creating a new Drawn Cutout  
        :type dCutout: :py:class:`NXOpen.Features.Feature` 
        :returns:  DrawnCutoutBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateLighteningCutoutBuilder(self, lighteningCutout: LighteningCutout) -> LighteningCutoutBuilder:
        """
        Creates a :py:class:`Features.SheetMetal.LighteningCutoutBuilder`  
        
        Signature ``CreateLighteningCutoutBuilder(lighteningCutout)`` 
        
        :param lighteningCutout:  :py:class:`Features.SheetMetal.LighteningCutout` to be edited  
        :type lighteningCutout: :py:class:`NXOpen.Features.SheetMetal.LighteningCutout` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateLouverFeatureBuilder(self, louver: NXOpen.Features.Feature) -> LouverBuilder:
        """
        Create a NXSM Louver feature Builder 
        
        Signature ``CreateLouverFeatureBuilder(louver)`` 
        
        :param louver:  The Louver for which builder needs to be constructed. NULL for creating a new Louver  
        :type louver: :py:class:`NXOpen.Features.Feature` 
        :returns:  LouverBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.LouverBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateBeadFeatureBuilder(self, bead: NXOpen.Features.Feature) -> BeadBuilder:
        """
        Create a NXSM Bead feature Builder 
        
        Signature ``CreateBeadFeatureBuilder(bead)`` 
        
        :param bead:  The Bead for which builder needs to be constructed. NULL for creating a new Bead  
        :type bead: :py:class:`NXOpen.Features.Feature` 
        :returns:  BeadBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BeadBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateFlangeFeatureBuilder(self, dCutout: NXOpen.Features.Feature) -> FlangeBuilder:
        """
        Create a NXSM Flange feature Builder 
        
        Signature ``CreateFlangeFeatureBuilder(dCutout)`` 
        
        :param dCutout:  The Flange for which builder needs to be constructed. NULL for creating a new Flange  
        :type dCutout: :py:class:`NXOpen.Features.Feature` 
        :returns:  FlangeBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateBreakCornerFeatureBuilder(self, brcorner: NXOpen.Features.Feature) -> BreakCornerBuilder:
        """
        Create a NXSM Break Corner feature Builder 
        
        Signature ``CreateBreakCornerFeatureBuilder(brcorner)`` 
        
        :param brcorner:  The Break Corner for which builder needs to be constructed. NULL for creating a new Break Corner  
        :type brcorner: :py:class:`NXOpen.Features.Feature` 
        :returns:  BrcornerBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BreakCornerBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateEdgeRipFeatureBuilder(self, edgeRip: NXOpen.Features.Feature) -> EdgeRipBuilder:
        """
        Create a NXSM Edge Rip feature Builder 
        
        Signature ``CreateEdgeRipFeatureBuilder(edgeRip)`` 
        
        :param edgeRip:  The Edge Rip for which builder needs to be constructed. NULL for creating a new Edge Rip  
        :type edgeRip: :py:class:`NXOpen.Features.Feature` 
        :returns:  Edge Rip Builder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.EdgeRipBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateConvertToSheetmetalFeatureBuilder(self, convertToSheetMetal: NXOpen.Features.Feature) -> ConvertToSheetmetalBuilder:
        """
        Create a NXSM Convert To Sheetmetal feature Builder 
        
        Signature ``CreateConvertToSheetmetalFeatureBuilder(convertToSheetMetal)`` 
        
        :param convertToSheetMetal:  The Convert To Sheetmetal feature for which builder needs to be constructed. NULL for converting a part for the first time 
        :type convertToSheetMetal: :py:class:`NXOpen.Features.Feature` 
        :returns:  Convert To Sheetmetal Builder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ConvertToSheetmetalBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateNormalCutoutFeatureBuilder(self, ncutout: NXOpen.Features.Feature) -> NormalCutoutBuilder:
        """
        Create a NXSM Normal Cutout feature Builder 
        
        Signature ``CreateNormalCutoutFeatureBuilder(ncutout)`` 
        
        :param ncutout:  The Normal Cutout for which builder needs to be constructed. NULL for creating a new Normal Cutout  
        :type ncutout: :py:class:`NXOpen.Features.Feature` 
        :returns:  NormalCutoutBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateTabFeatureBuilder(self, tab: NXOpen.Features.Feature) -> TabBuilder:
        """
        Create a NXSM Tab feature Builder 
        
        Signature ``CreateTabFeatureBuilder(tab)`` 
        
        :param tab:  The Tab for which builder needs to be constructed. NULL for creating a new Tab  
        :type tab: :py:class:`NXOpen.Features.Feature` 
        :returns:  TabBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.TabBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateLoftedFlangeFeatureBuilder(self, lflange: NXOpen.Features.Feature) -> LoftedFlangeBuilder:
        """
        Create a NXSM Lofted Flange feature Builder 
        
        Signature ``CreateLoftedFlangeFeatureBuilder(lflange)`` 
        
        :param lflange:  The Lofted Flange for which builder needs to be constructed. NULL for creating a new LoftedFlange  
        :type lflange: :py:class:`NXOpen.Features.Feature` 
        :returns:  LoftedFlangeBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.LoftedFlangeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateThreeBendCornerFeatureBuilder(self, threeBendCorner: NXOpen.Features.Feature) -> ThreeBendCornerBuilder:
        """
        Create a NXSM Three Bend Corner feature Builder 
        
        Signature ``CreateThreeBendCornerFeatureBuilder(threeBendCorner)`` 
        
        :param threeBendCorner:  The Three Bend Corner for which builder needs to be constructed. NULL for creating a new Three Bend Corner  
        :type threeBendCorner: :py:class:`NXOpen.Features.Feature` 
        :returns:  ThreeBendCornerBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateContourFlangeFeatureBuilder(self, contourFlange: NXOpen.Features.Feature) -> ContourFlangeBuilder:
        """
        Create a NXSM Contour Flange feature Builder 
        
        Signature ``CreateContourFlangeFeatureBuilder(contourFlange)`` 
        
        :param contourFlange: The Contour Flange for which builder needs to be constructed. NULL for creating a new Contour Flange  
        :type contourFlange: :py:class:`NXOpen.Features.Feature` 
        :returns:  ContourFlangeBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ContourFlangeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateFlatSolidFeatureBuilder(self, flatSolid: NXOpen.Features.Feature) -> FlatSolidBuilder:
        """
        Create a NXSM Flat Solid feature Builder 
        
        Signature ``CreateFlatSolidFeatureBuilder(flatSolid)`` 
        
        :param flatSolid: The Contour Flange for which builder needs to be constructed. NULL for creating a new Flat Solid  
        :type flatSolid: :py:class:`NXOpen.Features.Feature` 
        :returns:  Flat Solid object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateFlatPatternBuilder(self, flatPattern: NXOpen.Features.Feature) -> FlatPatternBuilder:
        """
        Create a NXSM Flat Pattern feature Builder 
        
        Signature ``CreateFlatPatternBuilder(flatPattern)`` 
        
        :param flatPattern: The Flat Pattern for which builder needs to be constructed. NULL for creating a new Flat Pattern  
        :type flatPattern: :py:class:`NXOpen.Features.Feature` 
        :returns:  Flat Pattern object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatPatternBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateBendTaperBuilder(self, bendTaper: NXOpen.Features.Feature) -> BendTaperBuilder:
        """
        Create a NXSM Bend taper feature Builder 
        
        Signature ``CreateBendTaperBuilder(bendTaper)`` 
        
        :param bendTaper: The Bend Taper for which builder needs to be constructed. NULL for creating a new Bend Taper  
        :type bendTaper: :py:class:`NXOpen.Features.Feature` 
        :returns:  Bend Taper object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateBendFeatureBuilder(self, bend: NXOpen.Features.Feature) -> BendBuilder:
        """
        Create a NXSM Bend feature Builder 
        
        Signature ``CreateBendFeatureBuilder(bend)`` 
        
        :param bend: The Bend for which builder needs to be constructed. NULL for creating a new Bend  
        :type bend: :py:class:`NXOpen.Features.Feature` 
        :returns:  Bend object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BendBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateClosedCornerFeatureBuilder(self, closedCorner: NXOpen.Features.Feature) -> ClosedCornerBuilder:
        """
        Create a NXSM Closed Corner feature Builder 
        
        Signature ``CreateClosedCornerFeatureBuilder(closedCorner)`` 
        
        :param closedCorner: The Closed Corner for which builder needs to be constructed. NULL for creating a new Closed Corner  
        :type closedCorner: :py:class:`NXOpen.Features.Feature` 
        :returns:  Closed Corner object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ClosedCornerBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateJogFeatureBuilder(self, jog: NXOpen.Features.Feature) -> JogBuilder:
        """
        Create a NXSM Jog feature Builder 
        
        Signature ``CreateJogFeatureBuilder(jog)`` 
        
        :param jog:  The Jog for which builder needs to be constructed. NULL for creating a new Jog  
        :type jog: :py:class:`NXOpen.Features.Feature` 
        :returns:  JogBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.JogBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateUnbendFeatureBuilder(self, unbend: NXOpen.Features.Feature) -> UnbendBuilder:
        """
        Create a NXSM Unbend feature builder 
        
        Signature ``CreateUnbendFeatureBuilder(unbend)`` 
        
        :param unbend: The Unbend for which builder needs to be constructed. NULL for creating a new Unbend  
        :type unbend: :py:class:`NXOpen.Features.Feature` 
        :returns:  Unbend object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.UnbendBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateRebendFeatureBuilder(self, rebend: NXOpen.Features.Feature) -> RebendBuilder:
        """
        Create a NXSM Rebend feature builder 
        
        Signature ``CreateRebendFeatureBuilder(rebend)`` 
        
        :param rebend: The Rebend for which builder needs to be constructed. NULL for creating a new Rebend  
        :type rebend: :py:class:`NXOpen.Features.Feature` 
        :returns:  Rebend object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.RebendBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateMigratedPanelFeatureBuilder(self, migratedPanel: NXOpen.Features.Feature) -> MigratedPanelBuilder:
        """
        Create a NXSM Migrated Panel feature Builder 
        
        Signature ``CreateMigratedPanelFeatureBuilder(migratedPanel)`` 
        
        :param migratedPanel:  The Migrated Panel feature for which builder needs to be constructed. NULL for converting a part for the first time 
        :type migratedPanel: :py:class:`NXOpen.Features.Feature` 
        :returns:  Migrated Panel Builder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.MigratedPanelBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateResizeBendRadiusFeatureBuilder(self, resizeBendRadius: NXOpen.Features.Feature) -> ResizeBendRadiusBuilder:
        """
        Create a Resize Bend Radius Builder 
        
        Signature ``CreateResizeBendRadiusFeatureBuilder(resizeBendRadius)`` 
        
        :param resizeBendRadius:  The ResizeBendRadius feature for which builder needs to be constructed. NULL for creating a new ResizeBendRadius  
        :type resizeBendRadius: :py:class:`NXOpen.Features.Feature` 
        :returns:  ResizeBendRadius Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ResizeBendRadiusBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateResizeBendAngleBuilder(self, resizeBendAngle: NXOpen.Features.Feature) -> ResizeBendAngleBuilder:
        """
        Creates Resize Bend Angle Builder  
        
        Signature ``CreateResizeBendAngleBuilder(resizeBendAngle)`` 
        
        :param resizeBendAngle: The Resize Bend Angle feature for which builder needs to be constructed. NULL for creating a new Resize Bend Angle 
        :type resizeBendAngle: :py:class:`NXOpen.Features.Feature` 
        :returns: Resize Bend Angle Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ResizeBendAngleBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateHemFlangeFeatureBuilder(self, hemFalnge: NXOpen.Features.Feature) -> HemFlangeBuilder:
        """
        Create hem flange feature builder  
        
        Signature ``CreateHemFlangeFeatureBuilder(hemFalnge)`` 
        
        :param hemFalnge:  The Hem Flange feature for which builder needs to be constructed. NULL for creating a new Hem Flange  
        :type hemFalnge: :py:class:`NXOpen.Features.Feature` 
        :returns:  Hem Flange Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateResizeNeutralFactorBuilder(self, resizeNeutralFactor: NXOpen.Features.Feature) -> ResizeNeutralFactorBuilder:
        """
        Creates Resize Neutral Factor Builder  
        
        Signature ``CreateResizeNeutralFactorBuilder(resizeNeutralFactor)`` 
        
        :param resizeNeutralFactor:  The Resize Neutral Factor feature for which builder needs to be constructed. NULL for creating a new Resize Neutral Factor feature  
        :type resizeNeutralFactor: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ResizeNeutralFactorBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateSolidPunchBuilder(self, solidPunch: NXOpen.Features.Feature) -> SolidPunchBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.SolidPunchBuilder`  
        
        Signature ``CreateSolidPunchBuilder(solidPunch)`` 
        
        :param solidPunch:  :py:class:`NXOpen.Features.Feature` to be edited  
        :type solidPunch: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SolidPunchBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateBridgeTransitionBuilder(self, transition: NXOpen.Features.Feature) -> BridgeTransitionBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilder`  
        
        Signature ``CreateBridgeTransitionBuilder(transition)`` 
        
        :param transition: The Bridge Transition feature for which builder needs to be constructed.  
        
        NULL for creating a new Bridge Transition 
        :type transition: :py:class:`NXOpen.Features.Feature` 
        :returns: Bridge Transition Builder 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilder` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def IsSheetmetalBody(self, inputBody: NXOpen.Body) -> bool:
        """
        Is a sheet metal body.  
        
        This function will return True if the body has at least one NX Sheet Metal feature or
        a Flexible Printed Circuit Design feature.  
        
        Signature ``IsSheetmetalBody(inputBody)`` 
        
        :param inputBody: The body to check 
        :type inputBody: :py:class:`NXOpen.Body` 
        :returns: True = Body has NX Sheet Metal features or Flexible Printed Circuit Design features 
        :rtype: bool 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetBodyThickness(self, sheetmetalBody: NXOpen.Body) -> float:
        """
        Thickness of sheet metal body.  
        
        Value is returned in part units.  
        
        Signature ``GetBodyThickness(sheetmetalBody)`` 
        
        :param sheetmetalBody: The face to check 
        :type sheetmetalBody: :py:class:`NXOpen.Body` 
        :returns: Thickness Value 
        :rtype: float 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetInnerBendFaces(self, sheetmetalBody: NXOpen.Body) -> tuple:
        """
        Get inner bend faces.  
        
        For every bend the inner face is the face with smaller radius.
        
        Signature ``GetInnerBendFaces(sheetmetalBody)`` 
        
        :param sheetmetalBody: The body to check 
        :type sheetmetalBody: :py:class:`NXOpen.Body` 
        :returns: a tuple 
        :rtype: A tuple consisting of (innerBendFaces, bendStates). innerBendFaces is a list of :py:class:`NXOpen.Face`.  Inner bend facesbendStates is a list of :py:class:`NXOpen.Features.SheetMetal.SheetmetalBendState`.  Bend Face is flat or bent
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetFaceType(self, inputFace: NXOpen.Face) -> SheetmetalFaceType:
        """
        Sheet metal face type  
        
        Signature ``GetFaceType(inputFace)`` 
        
        :param inputFace: The face to check 
        :type inputFace: :py:class:`NXOpen.Face` 
        :returns: Sheet Metal Face Type 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SheetmetalFaceType` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetFaceLayer(self, inputFace: NXOpen.Face) -> SheetmetalFaceLayer:
        """
        Sheet metal face layer  
        
        Signature ``GetFaceLayer(inputFace)`` 
        
        :param inputFace: The face to check 
        :type inputFace: :py:class:`NXOpen.Face` 
        :returns: Sheet Metal Face Layer 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SheetmetalFaceLayer` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetOppositeFace(self, inputFace: NXOpen.Face) -> NXOpen.Face:
        """
        Opposite face to bend, web or deform face.  
        
        Will raise an exception if the input face is not a valid face. 
        
        Signature ``GetOppositeFace(inputFace)`` 
        
        :param inputFace: The face to check 
        :type inputFace: :py:class:`NXOpen.Face` 
        :returns: Opposite Layer Face 
        :rtype: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def GetBendParameters(self, bendFace: NXOpen.Face) -> SheetmetalBendParameters:
        """
        Bend region parameters.  
        
        The values are calculated from the inner face of bend region. The radius and angle values are returned in part units. This function will raise an exception of the face is not a valid bend face. 
        
        Signature ``GetBendParameters(bendFace)`` 
        
        :param bendFace: The face to query. This can be outer or inner bend face 
        :type bendFace: :py:class:`NXOpen.Face` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SheetmetalBendParameters` 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def IsThicknessEdge(self, inputEdge: NXOpen.Edge) -> bool:
        """
        Check if this edge is a thickness edge  
        
        Signature ``IsThicknessEdge(inputEdge)`` 
        
        :param inputEdge: The edge to check 
        :type inputEdge: :py:class:`NXOpen.Edge` 
        :returns: True = Thickness Edge 
        :rtype: bool 
        
        .. versionadded:: NX5.0.2
        
        License requirements: None.
        """
        ...
    
    
    def CreateSheetMetalFromSolidBuilder(self, sheetMetalFromSolid: NXOpen.Features.Feature) -> SheetMetalFromSolidBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.SheetMetalFromSolidBuilder`  
        
        Signature ``CreateSheetMetalFromSolidBuilder(sheetMetalFromSolid)`` 
        
        :param sheetMetalFromSolid:  :py:class:`NXOpen.Features.SheetMetalFromSolid` to be edited  
        :type sheetMetalFromSolid: :py:class:`NXOpen.Features.Feature` 
        :returns:  Sheet Metal from Solid Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SheetMetalFromSolidBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateFlexibleCableBuilder(self, flexibleCable: NXOpen.Features.Feature) -> FlexibleCableBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilder`  
        
        Signature ``CreateFlexibleCableBuilder(flexibleCable)`` 
        
        :param flexibleCable: The Flexible Cable feature for which builder needs to be constructed.  
        
        NULL for creating a new Flexible Cable.  
        :type flexibleCable: :py:class:`NXOpen.Features.Feature` 
        :returns: Flexible Cable Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreateGussetBuilder(self, gusset: NXOpen.Features.Feature) -> GussetBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.GussetBuilder`  
        
        Signature ``CreateGussetBuilder(gusset)`` 
        
        :param gusset:  :py:class:`NXOpen.Features.Gusset` to be edited  
        :type gusset: :py:class:`NXOpen.Features.Feature` 
        :returns:  Gusset Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.GussetBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateEditBendBuilder(self, editBend: NXOpen.Features.Feature) -> EditBendBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.EditBendBuilder`  
        
        Signature ``CreateEditBendBuilder(editBend)`` 
        
        :param editBend:  :py:class:`NXOpen.Features.EditBend` to be edited  
        :type editBend: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.EditBendBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateCleanUpUtilityBuilder(self) -> CleanUpUtilityBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.CleanUpUtilityBuilder`  
        
        Signature ``CreateCleanUpUtilityBuilder()`` 
        
        :returns:  Clean-Up Utility Builder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.CleanUpUtilityBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateMetaformBuilder(self, metaform: NXOpen.Features.Feature) -> MetaformBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.MetaformBuilder`  
        
        Signature ``CreateMetaformBuilder(metaform)`` 
        
        :param metaform:  :py:class:`NXOpen.Features.Metaform` to be edited  
        :type metaform: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.MetaformBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateEditCornerBuilder(self) -> EditCornerBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilder`  
        
        Signature ``CreateEditCornerBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.EditCornerBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def CreateExportFlatPatternBuilder(self) -> ExportFlatPatternBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilder`  
        
        Signature ``CreateExportFlatPatternBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilder` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreateJoggleBuilder(self, joggle: NXOpen.Features.Feature) -> JoggleBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.JoggleBuilder`  
        
        Signature ``CreateJoggleBuilder(joggle)`` 
        
        :param joggle: 
        :type joggle: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.JoggleBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateAdvancedFlangeBuilder(self, joggle: NXOpen.Features.Feature) -> AdvancedFlangeBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilder`  
        
        Signature ``CreateAdvancedFlangeBuilder(joggle)`` 
        
        :param joggle: 
        :type joggle: :py:class:`NXOpen.Features.Feature` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateBendListBuilder(self) -> BendListBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.BendListBuilder`  
        
        Signature ``CreateBendListBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BendListBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreateBendListItemBuilder(self) -> BendListItemBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        BendListItemBuilder objects will be created and populated in the BendListBuilder when bend information of a flat pattern view is populated.  
        
        User should never need to create or delete BendListItemBuilder object on its own. 
        
        Signature ``CreateBendListItemBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreateMultiFlangeBuilder(self, multiFlange: MultiFlange) -> MultiFlangeBuilder:
        """
        Creates a :py:class:`Features.SheetMetal.MultiFlangeBuilder`  
        
        Signature ``CreateMultiFlangeBuilder(multiFlange)`` 
        
        :param multiFlange:  :py:class:`Features.SheetMetal.MultiFlange` to be edited  
        :type multiFlange: :py:class:`NXOpen.Features.SheetMetal.MultiFlange` 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.MultiFlangeBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    


class ConvertInputListItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Sheetmetal convert to sheet metal corner list item builder class.  
    
    This builder is used to interrogate the corner items in the list.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.ConvertToSheetmetalBuilder.CreateConvertInputListItem`
    
    .. versionadded:: NX12.0.0
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
    
    CornerFaces: NXOpen.ScCollector = ...
    """
    Returns  the corner faces 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: ConvertInputListItemBuilder = ...  # unknown typename


class FlexibleCableSegment(NXOpen.NXObject):
    """
    Represents a Flexible Cable Segment class.  
    
    No creator as of now
    
    .. versionadded:: NX7.5.0
    """
    
    def GetSegmentType(self) -> FlexibleCableBuilderSegmentTypeOptions:
        """
        Returns the type of cable segment.  
        
        It could be of :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderSegmentTypeOptions.Planar <NXOpen.Features.SheetMetal.FlexibleCableBuilderSegmentTypeOptions>`, 
        or :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderSegmentTypeOptions.Bend <NXOpen.Features.SheetMetal.FlexibleCableBuilderSegmentTypeOptions>` 
        
        Signature ``GetSegmentType()`` 
        
        :returns:  Cable segment type.  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderSegmentTypeOptions` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendAngle: NXOpen.Expression = ...
    """
    Returns  the bend angle.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendAngle`` 
    
    :returns:  Bend Angle.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    BendAngleDirection: FlexibleCableBuilderBendAngleDirectionOptions = ...
    """
    Returns or sets  the bend angle direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendAngleDirection`` 
    
    :returns:  Bend angle direction option.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderBendAngleDirectionOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendAngleDirection`` 
    
    :param bendAngleDirectionOption:  Bend angle direction option.  
    :type bendAngleDirectionOption: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderBendAngleDirectionOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    BendRadius: NXOpen.Expression = ...
    """
    Returns  the bend radius.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendRadius`` 
    
    :returns:  Bend Radius.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length.  
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns:  Length.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    PathAdjustmentAngle: NXOpen.Expression = ...
    """
    Returns  the path adjustment angle.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathAdjustmentAngle`` 
    
    :returns:  Path Adjustment Angle.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    PathAdjustmentAngleDirection: FlexibleCableBuilderPathAdjustmentAngleDirectionOptions = ...
    """
    Returns or sets  the path adjustment angle direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathAdjustmentAngleDirection`` 
    
    :returns:  Path adjustment angle direction option.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderPathAdjustmentAngleDirectionOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``PathAdjustmentAngleDirection`` 
    
    :param pathAdjustmentAngleDirectionOption:  Path adjustment angle direction option.  
    :type pathAdjustmentAngleDirectionOption: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderPathAdjustmentAngleDirectionOptions` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: FlexibleCableSegment = ...  # unknown typename


class SheetMetalFromSolidBuilder(SheetmetalBaseBuilder):
    """
    Represents a :py:class:`NXOpen.Features.SheetMetalFromSolid` builder
    (Sheet Metal from Solid).  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateSheetMetalFromSolidBuilder`
    
    Default values.
    
    ===================  ==========================================
    Property             Value
    ===================  ==========================================
    Thickness.Value      3.0 (millimeters part), 0.1 (inches part) 
    -------------------  ------------------------------------------
    UseGlobalThickness   1 
    ===================  ==========================================
    
    .. versionadded:: NX6.0.0
    """
    
    def GetCandidateBendEdges(self) -> 'list[NXOpen.Edge]':
        """
        Get the candidate bend edges  
        
        Signature ``GetCandidateBendEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetAutomaticBendEdges(self) -> 'list[NXOpen.Edge]':
        """
        Get the automatic bend edges  
        
        Signature ``GetAutomaticBendEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendEdges: NXOpen.ScCollector = ...
    """
    Returns  the bend edges 
    
    <hr>
    
    Getter Method
    
    Signature ``BendEdges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the reverse direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UseGlobalThickness: bool = ...
    """
    Returns or sets  the use global thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalThickness`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalThickness`` 
    
    :param useGlobalThickness: 
    :type useGlobalThickness: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    WebFaces: NXOpen.ScCollector = ...
    """
    Returns  the web faces 
    
    <hr>
    
    Getter Method
    
    Signature ``WebFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: SheetMetalFromSolidBuilder = ...  # unknown typename


class AdvancedFlangeBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AdvancedFlangeBuilderTypes():
    """
    This enum defines the  type options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ByValue", " - "
       "ToReference", " - "
    """
    ByValue = 0  # AdvancedFlangeBuilderTypesMemberType
    ToReference = 1  # AdvancedFlangeBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AdvancedFlangeBuilderLengthReferencesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AdvancedFlangeBuilderLengthReferences():
    """
    This enum defines the flange length dimension types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", " - "
       "Outside", " - "
       "Web", " - "
       "Din6935", " - "
    """
    Inside = 0  # AdvancedFlangeBuilderLengthReferencesMemberType
    Outside = 1  # AdvancedFlangeBuilderLengthReferencesMemberType
    Web = 2  # AdvancedFlangeBuilderLengthReferencesMemberType
    Din6935 = 3  # AdvancedFlangeBuilderLengthReferencesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AdvancedFlangeBuilderInsetsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AdvancedFlangeBuilderInsets():
    """
    This enum defines the material types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", " - "
       "MaterialOutside", " - "
       "BendOutside", " - "
    """
    MaterialInside = 0  # AdvancedFlangeBuilderInsetsMemberType
    MaterialOutside = 1  # AdvancedFlangeBuilderInsetsMemberType
    BendOutside = 2  # AdvancedFlangeBuilderInsetsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AdvancedFlangeBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Sheetmetal Advanced Flange builder class.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateAdvancedFlangeBuilder`
    
    Default values.
    
    ===============================  ======================================
    Property                         Value
    ===============================  ======================================
    Angle.Value                      0 
    -------------------------------  --------------------------------------
    EndAdjustment.Value              0 
    -------------------------------  --------------------------------------
    FlatPatternCompensationAtEnd     0 
    -------------------------------  --------------------------------------
    FlatPatternCompensationAtStart   0 
    -------------------------------  --------------------------------------
    InferLength                      0 
    -------------------------------  --------------------------------------
    Inset                            MaterialInside 
    -------------------------------  --------------------------------------
    Length.Value                     0 (millimeters part), 0 (inches part) 
    -------------------------------  --------------------------------------
    LengthReference                  Inside 
    -------------------------------  --------------------------------------
    StartAdjustment.Value            0 
    ===============================  ======================================
    
    .. versionadded:: NX11.0.0
    """
    
    class Types():
        """
        This enum defines the  type options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ByValue", " - "
           "ToReference", " - "
        """
        ByValue = 0  # AdvancedFlangeBuilderTypesMemberType
        ToReference = 1  # AdvancedFlangeBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LengthReferences():
        """
        This enum defines the flange length dimension types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", " - "
           "Outside", " - "
           "Web", " - "
           "Din6935", " - "
        """
        Inside = 0  # AdvancedFlangeBuilderLengthReferencesMemberType
        Outside = 1  # AdvancedFlangeBuilderLengthReferencesMemberType
        Web = 2  # AdvancedFlangeBuilderLengthReferencesMemberType
        Din6935 = 3  # AdvancedFlangeBuilderLengthReferencesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Insets():
        """
        This enum defines the material types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", " - "
           "MaterialOutside", " - "
           "BendOutside", " - "
        """
        MaterialInside = 0  # AdvancedFlangeBuilderInsetsMemberType
        MaterialOutside = 1  # AdvancedFlangeBuilderInsetsMemberType
        BendOutside = 2  # AdvancedFlangeBuilderInsetsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    Returns  the angle 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    BendOptions: BendOptions = ...
    """
    Returns  the  Sheet Metal Bend Options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Edges: NXOpen.ScCollector = ...
    """
    Returns  the base edge for the advanced flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``Edges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    EndAdjustment: NXOpen.Expression = ...
    """
    Returns  the flat pattern compensation adjustment at end of the flange 
    
    <hr>
    
    Getter Method
    
    Signature ``EndAdjustment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Faces: NXOpen.ScCollector = ...
    """
    Returns  the  reference face for advanced flange 
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    FlatPatternCompensationAtEnd: bool = ...
    """
    Returns or sets  the  option to apply flat pattern compensation at end of the flange 
    
    <hr>
    
    Getter Method
    
    Signature ``FlatPatternCompensationAtEnd`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlatPatternCompensationAtEnd`` 
    
    :param flatPatternCompensationAtEnd: 
    :type flatPatternCompensationAtEnd: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    FlatPatternCompensationAtStart: bool = ...
    """
    Returns or sets  the  option to apply flat pattern compensation at start of the flange
    
    <hr>
    
    Getter Method
    
    Signature ``FlatPatternCompensationAtStart`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FlatPatternCompensationAtStart`` 
    
    :param flatPatternCompensationAtStart: 
    :type flatPatternCompensationAtStart: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    InferLength: bool = ...
    """
    Returns or sets  the infer length option 
    
    <hr>
    
    Getter Method
    
    Signature ``InferLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferLength`` 
    
    :param inferLength: 
    :type inferLength: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Inset: AdvancedFlangeBuilderInsets = ...
    """
    Returns or sets  the inset type 
    
    <hr>
    
    Getter Method
    
    Signature ``Inset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderInsets` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Inset`` 
    
    :param inset: 
    :type inset: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderInsets` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    LengthReference: AdvancedFlangeBuilderLengthReferences = ...
    """
    Returns or sets  the length reference 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthReference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderLengthReferences` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LengthReference`` 
    
    :param lengthReference: 
    :type lengthReference: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderLengthReferences` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Plane1: NXOpen.Plane = ...
    """
    Returns or sets  the first plane for the end limits 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane1`` 
    
    :param plane1: 
    :type plane1: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Plane2: NXOpen.Plane = ...
    """
    Returns or sets  the second plane for the end limits 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane2`` 
    
    :param plane2: 
    :type plane2: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the option to reverse length direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReverseTrimSide: bool = ...
    """
    Returns or sets  the option to reverse trim side 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseTrimSide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseTrimSide`` 
    
    :param reverseTrimSide: 
    :type reverseTrimSide: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    StartAdjustment: NXOpen.Expression = ...
    """
    Returns  the flat pattern compensation adjustment at start of the flange 
    
    <hr>
    
    Getter Method
    
    Signature ``StartAdjustment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Type: AdvancedFlangeBuilderTypes = ...
    """
    Returns or sets  the advanced flange type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilderTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AdvancedFlangeBuilder = ...  # unknown typename


class FlangeBuilderInsetTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBuilderInsetTypeOptions():
    """
    This enum represents the inset type for the material of the flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", "The flange is flush with the thickness face on the inside"
       "MaterialOutside", "The flange is flush with the thickness face on the outside"
       "BendOutside", "The bend and flange are outside the thickness face"
    """
    MaterialInside = 0  # FlangeBuilderInsetTypeOptionsMemberType
    MaterialOutside = 1  # FlangeBuilderInsetTypeOptionsMemberType
    BendOutside = 2  # FlangeBuilderInsetTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBuilderLengthTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBuilderLengthTypeOptions():
    """
    This enum indicates the two ways that the flange length can be measured. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "InsideDimension", "The flange length is dimensioned to the Inner Mold line."
       "OutsideDimension", "The flange length is dimensioned to the Outer Mold Line."
       "WebDimension", "The flange length is dimensioned to the Bend Tangent Line."
    """
    InsideDimension = 0  # FlangeBuilderLengthTypeOptionsMemberType
    OutsideDimension = 1  # FlangeBuilderLengthTypeOptionsMemberType
    WebDimension = 2  # FlangeBuilderLengthTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBuilderOffsetTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBuilderOffsetTypeOptions():
    """
    This enum represents the offset type for the flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "The flange is offset to the inside of the face"
       "Outside", "The flange is offset to the outside of the face"
    """
    Inside = 0  # FlangeBuilderOffsetTypeOptionsMemberType
    Outside = 1  # FlangeBuilderOffsetTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBuilderWidthTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBuilderWidthTypeOptions():
    """
    This enum represents the width type for the flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FullEdge", "The flange spans the entire edge."
       "CenterOfEdge", "The flange is centered on the edge."
       "AtEdgeEnd", "The flange starts from the specified end of the edge."
       "FromEdgeEnd", "The flange starts at a specified distance from an end of the edge."
       "FromBothEnds", "The flange starts and ends at specified distances from the ends of the edge."
       "Custom", "The flange sketch has been edited after creation and may or may not conform to any of the above."
    """
    FullEdge = 0  # FlangeBuilderWidthTypeOptionsMemberType
    CenterOfEdge = 1  # FlangeBuilderWidthTypeOptionsMemberType
    AtEdgeEnd = 2  # FlangeBuilderWidthTypeOptionsMemberType
    FromEdgeEnd = 3  # FlangeBuilderWidthTypeOptionsMemberType
    FromBothEnds = 4  # FlangeBuilderWidthTypeOptionsMemberType
    Custom = 5  # FlangeBuilderWidthTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBuilderMatchFaceOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBuilderMatchFaceOptions():
    """
    This enum represents the match face option for the flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "The flange is placed on the selected edge"
       "UntilSelected", "The flange face is extended until the selected plane"
    """
    NotSet = 0  # FlangeBuilderMatchFaceOptionsMemberType
    UntilSelected = 1  # FlangeBuilderMatchFaceOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBuilder(SheetmetalBaseBuilder):
    """
    Represents a Flange feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateFlangeFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class InsetTypeOptions():
        """
        This enum represents the inset type for the material of the flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", "The flange is flush with the thickness face on the inside"
           "MaterialOutside", "The flange is flush with the thickness face on the outside"
           "BendOutside", "The bend and flange are outside the thickness face"
        """
        MaterialInside = 0  # FlangeBuilderInsetTypeOptionsMemberType
        MaterialOutside = 1  # FlangeBuilderInsetTypeOptionsMemberType
        BendOutside = 2  # FlangeBuilderInsetTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LengthTypeOptions():
        """
        This enum indicates the two ways that the flange length can be measured. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "InsideDimension", "The flange length is dimensioned to the Inner Mold line."
           "OutsideDimension", "The flange length is dimensioned to the Outer Mold Line."
           "WebDimension", "The flange length is dimensioned to the Bend Tangent Line."
        """
        InsideDimension = 0  # FlangeBuilderLengthTypeOptionsMemberType
        OutsideDimension = 1  # FlangeBuilderLengthTypeOptionsMemberType
        WebDimension = 2  # FlangeBuilderLengthTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OffsetTypeOptions():
        """
        This enum represents the offset type for the flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "The flange is offset to the inside of the face"
           "Outside", "The flange is offset to the outside of the face"
        """
        Inside = 0  # FlangeBuilderOffsetTypeOptionsMemberType
        Outside = 1  # FlangeBuilderOffsetTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class WidthTypeOptions():
        """
        This enum represents the width type for the flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FullEdge", "The flange spans the entire edge."
           "CenterOfEdge", "The flange is centered on the edge."
           "AtEdgeEnd", "The flange starts from the specified end of the edge."
           "FromEdgeEnd", "The flange starts at a specified distance from an end of the edge."
           "FromBothEnds", "The flange starts and ends at specified distances from the ends of the edge."
           "Custom", "The flange sketch has been edited after creation and may or may not conform to any of the above."
        """
        FullEdge = 0  # FlangeBuilderWidthTypeOptionsMemberType
        CenterOfEdge = 1  # FlangeBuilderWidthTypeOptionsMemberType
        AtEdgeEnd = 2  # FlangeBuilderWidthTypeOptionsMemberType
        FromEdgeEnd = 3  # FlangeBuilderWidthTypeOptionsMemberType
        FromBothEnds = 4  # FlangeBuilderWidthTypeOptionsMemberType
        Custom = 5  # FlangeBuilderWidthTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MatchFaceOptions():
        """
        This enum represents the match face option for the flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "The flange is placed on the selected edge"
           "UntilSelected", "The flange face is extended until the selected plane"
        """
        NotSet = 0  # FlangeBuilderMatchFaceOptionsMemberType
        UntilSelected = 1  # FlangeBuilderMatchFaceOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetOffset(self, offset: str) -> None:
        """
        Signature ``SetOffset(offset)`` 
        
        :param offset:  The flange offset value  
        :type offset: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Offset` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetLength(self, length: str) -> None:
        """
        Signature ``SetLength(length)`` 
        
        :param length: 
        :type length: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Length` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetFirstDistance(self, firstDistance: str) -> None:
        """
        Signature ``SetFirstDistance(firstDistance)`` 
        
        :param firstDistance: 
        :type firstDistance: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetSecondDistance(self, secondDistance: str) -> None:
        """
        Signature ``SetSecondDistance(secondDistance)`` 
        
        :param secondDistance: 
        :type secondDistance: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetBendAngle(self, bendAngle: str) -> None:
        """
        Signature ``SetBendAngle(bendAngle)`` 
        
        :param bendAngle: 
        :type bendAngle: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.BendAngle` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify that the builder data is valid for creating a flange.  
        
        If the builder data is valid, return value is zero.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  A value of zero is returned if the data in the builder is valid.  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def GetSketch(self) -> NXOpen.Sketch:
        """
        Get the flange sketch   
        
        Signature ``GetSketch()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Sketch` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def EditSketch(self) -> None:
        """
        Edit the sketch base on a new edge you need to call SetEdge to set a new edge
        
        Signature ``EditSketch()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def DeleteSketch(self) -> None:
        """
        Delete the flange sketch 
        
        Signature ``DeleteSketch()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    BendAngle: NXOpen.Expression = ...
    """
    Returns  the bend angle for flange.  
    
    It should be set in degrees (??????). 
    
    <hr>
    
    Getter Method
    
    Signature ``BendAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options object.  
    
    The bend options object stores additional parameters for the bend, such as bend radius, bend 
    relief width and depth, corner relief type etc.
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Edge: NXOpen.Edge = ...
    """
    Returns or sets  the edge on which the flange is created.  
    
    The edge should be linear and it should not be a thickness edge.
    
    <hr>
    
    Getter Method
    
    Signature ``Edge`` 
    
    :returns:  The flange is created on this edge.  
    :rtype: :py:class:`NXOpen.Edge` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Edge`` 
    
    :param edge:  The flange is created on this edge.  
    :type edge: :py:class:`NXOpen.Edge` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    FirstDistance: NXOpen.Expression = ...
    """
    Returns  a distance based on :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.WidthType`.  
    
    See :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.WidthType`` for a detailed desctiption of what this distance stands for.
    
    <hr>
    
    Getter Method
    
    Signature ``FirstDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    InsetType: FlangeBuilderInsetTypeOptions = ...
    """
    Returns or sets  the inset type (inside, outside, bendoutside) for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``InsetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderInsetTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``InsetType`` 
    
    :param insetType: 
    :type insetType: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderInsetTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length of the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    LengthType: FlangeBuilderLengthTypeOptions = ...
    """
    Returns or sets  a enum indicating the length type.  
    
    For Features created in NX8 and above:
    The way length is measured for the flange. It can either be measure from the inside edge or the outside edge.
    
    Flange length can be specified starting from the selected edge or from the corresponding edge on the other face 
    (other linear edge on the other side of the thickness face). If the length is specified from the
    selected edge use value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions.InsideDimension <NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions>` or
    if the flange length is specifed from the other edge use value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions.OutsideDimension <NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions>`.
    
    For Features created in NX8 and above:        
    Flange length can be measure from the Inner Mold Line, Outer Mold Line or Bend Tangent Line.
    
    Inner Mold Line: Intersection of inner tab face and inner flange web face
    Outer Mold Line: Intersection of outer tab face and outer flange web face
    Bend  Tangent Line: common edge between flange web face and bend face.
    
    Flange length can be specified starting from the inner mold line or outer mold line or bend tangent line. If the length is specified from the
    inner mold line use value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions.InsideDimension <NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions>` or
    if the flange length is specifed from the outer mold line use value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions.OutsideDimension <NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions>`or
    if the flange length is specifed from the bend tangent line use value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions.WebDimension <NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``LengthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``LengthType`` 
    
    :param lengthType: 
    :type lengthType: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderLengthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    MatchFaceOption: FlangeBuilderMatchFaceOptions = ...
    """
    Returns or sets  the match face selection type.  
    
    None for Regular Flange.
    Until Selected for Match To Face type Flange .
    
    <hr>
    
    Getter Method
    
    Signature ``MatchFaceOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderMatchFaceOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``MatchFaceOption`` 
    
    :param matchFaceOption: 
    :type matchFaceOption: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderMatchFaceOptions` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MatchPlane: NXOpen.Plane = ...
    """
    Returns or sets  the Match Plane.  
    
    <hr>
    
    Getter Method
    
    Signature ``MatchPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``MatchPlane`` 
    
    :param matchPlane: 
    :type matchPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset value for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns:  The flange offset value  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    OffsetType: FlangeBuilderOffsetTypeOptions = ...
    """
    Returns or sets  the offset type for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``OffsetType`` 
    
    :returns:  The flange can be offset inside or outside.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderOffsetTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``OffsetType`` 
    
    :param offsetType:  The flange can be offset inside or outside.  
    :type offsetType: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderOffsetTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    SecondDistance: NXOpen.Expression = ...
    """
    Returns  a distance based on :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.WidthType`.  
    
    See :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.WidthType`` for a detailed desctiption of what this distance stands for.
    
    <hr>
    
    Getter Method
    
    Signature ``SecondDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Vertex: NXOpen.Point3d = ...
    """
    Returns or sets  the vertex on the flange edge, needed to dimension the flange width.  
    
    The vertex needs to be specified ONLY if :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.WidthType` is
    set to one of :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.AtEdgeEnd <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`,  
    :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.FromEdgeEnd <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`. In case of 
    :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.FromBothEnds <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`, the start vertex of the edge
    is assumed to be the start point for :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`.
    
    <hr>
    
    Getter Method
    
    Signature ``Vertex`` 
    
    :returns:  A vertex on the flange edge.  
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Vertex`` 
    
    :param vertex:  A vertex on the flange edge.  
    :type vertex: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    WidthType: FlangeBuilderWidthTypeOptions = ...
    """
    Returns or sets  the width type for flange.  
    
    Use one of the values from :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions`. Depending on which of the 
    values from the enum is used, none, either or both of the distance values from 
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`  and 
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance`
    may be used. Here is a description of the distances:
    
    If the value is :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.FullEdge <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`, 
    then both the :py:meth:`FirstDistance`
    and :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance` values are unused.
    
    If the value is :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.CenterOfEdge <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`, 
    then both the :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`
    and :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance` represent exactly half the width of the flange.
    
    If the value is :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.AtEdgeEnd <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`,
    then :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`
    represents the width of the flange, starting from the end of the edge specified by the 
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Vertex` and 
    the :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance` is not used.
    
    If the value is :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.FromEdgeEnd <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`,
    then :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`
    represents the distance of the start point of the flange from the end of the edge specified by 
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Vertex` 
    and :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance` represents the width of the flange.
    
    If the value is :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.FromBothEnds <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`, 
    then :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`
    represents the distance of the start point of the flange from the from the end of the edge specified by
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Vertex`  
    and :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance`
    represents the distance of the end point of the flange from end of the edge opposite to the end 
    specified by :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.Vertex`.
    
    The value :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions.Custom <NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions>`, cannot be set by the user. It is set internally if the
    sketch for the flange has been edited after creation. In this case, the expressions
    :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.FirstDistance`
    and :py:meth:`NXOpen.Features.SheetMetal.FlangeBuilder.SecondDistance`
    may or may not retain their original meaning when the flange was first created, 
    so the user should not rely on these any more to mean anything specific.
    
    <hr>
    
    Getter Method
    
    Signature ``WidthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``WidthType`` 
    
    :param widthType: 
    :type widthType: :py:class:`NXOpen.Features.SheetMetal.FlangeBuilderWidthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Null: FlangeBuilder = ...  # unknown typename


class FeaturePropertyMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FeatureProperty():
    """
    This is a common enum that comprises of values to be used for various features.
    All Feature builder APIs will enumerate valid values that can be used for that feature parameter.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "IgNullConstant", " - "
       "IgLeft", " - "
       "IgRight", " - "
       "IgSymmetric", " - "
       "IgInside", " - "
       "IgOutside", " - "
       "IgBoth", " - "
       "IgNormalSidedummy", " - "
       "IgReverseNormalSidedummy", " - "
       "IgExtend", " - "
       "IgNoextend", " - "
       "IgThkinprofileplane", " - "
       "IgThkNormalToProfilePlane", " - "
       "IgFinite", " - "
       "IgTonext", " - "
       "IgFromTo", " - "
       "IgThroughAll", " - "
       "IgThreeHundredAndSixty", " - "
       "IgParallelDummy", " - "
       "IgAngularDummy", " - "
       "IgNormal", " - "
       "IgThroughAxis", " - "
       "IgSingleEdge", " - "
       "IgMultipleEdges", " - "
       "IgEdgesByLoop", " - "
       "IgEdgesByVertex", " - "
       "IgAll", " - "
       "IgConcave", " - "
       "IgConvex", " - "
       "IgStart", " - "
       "IgEnd", " - "
       "IgLinear", " - "
       "IgRadial", " - "
       "IgRegularHole", " - "
       "IgCounterBoreHole", " - "
       "IgCounterSinkHole", " - "
       "IgCounterDrillHole", " - "
       "IgTappedHole", " - "
       "IgTaperedHole", " - "
       "IgConstRadiusRound", " - "
       "IgVarRadiusRound", " - "
       "IgChamfer45degSetback", " - "
       "IgChamferAngleSetback", " - "
       "IgChamfer2Serbacks", " - "
       "IgNone", " - "
       "IgTaperByAngle", " - "
       "IgTaperByRatio", " - "
       "IgClosed", " - "
       "IgProfileBasedCrosssection", " - "
       "IgEdgeBasedCrosssection", " - "
       "IgTangent", " - "
       "IgRectangularBendRelief", " - "
       "IgFilletBendRelief", " - "
       "IgRipBendRelief", " - "
       "IgBendOnlyCornerRelief", " - "
       "IgBendAndFaceCornerRelief", " - "
       "IgRipCornerRelief", " - "
       "IgNftype", " - "
       "IgEquationType", " - "
       "IgPatternMirror", " - "
       "IgPatternRectangular", " - "
       "IgPatternCircular", " - "
       "IgPatternUserDefined", " - "
       "IgFromReferenceEnd", " - "
       "IgFromNonreferenceEnd", " - "
       "IgRndRollAcrossTnagentEdgesOn", " - "
       "IgRndRollAcrossTangentEdgesOff", " - "
       "IgRndCapAcrossSharpEdges", " - "
       "IgRndRollAcrossSharpEdges", " - "
       "IgRndRollAlongBlendEdgesOn", " - "
       "IgRndRollAlongBlendEdgesOff", " - "
       "IgToKepPoint", " - "
       "IgFlatten", " - "
       "IgAsConstruction", " - "
       "IgOffset", " - "
       "IgMitreParalletToThickness", " - "
       "IgMitreNormalToThickness", " - "
       "IgMitreByDist", " - "
       "IgMitreByAngle", " - "
       "IgMiterRegularCut", " - "
       "IgMitreManufacturingCut", " - "
       "IgProjectOptionProject", " - "
       "IgProjectOptionWrap", " - "
       "IgLip", " - "
       "IgGroove", " - "
       "IgPartingFromPlane", " - "
       "IgPartingFromSurface", " - "
       "IgPartingFromEdge", " - "
       "IgPartingFromCurve", " - "
       "IgSplitDraft", " - "
       "IgSplitAngle1Right", " - "
       "IgSplitAngle1Left", " - "
       "IgLouverformedendtype", " - "
       "IgLouverlancedendtype", " - "
       "IgLouverround", " - "
       "IgLouverroundnone", " - "
       "IgInsideDimension", " - "
       "IgOutsideDimension", " - "
       "IgFull", " - "
       "IgBend", " - "
       "IgAddRound", " - "
       "IgNoRound", " - "
       "IgCloseFaces", " - "
       "IgOverlapFaces", " - "
       "IgTreatmentOff", " - "
       "IgTreatmentIntersect", " - "
       "IgTreatmentCircleCutout", " - "
       "IgStepDreat", " - "
       "IgShowBoundaries", " - "
       "IgRemoveBoundaries", " - "
       "IgCornerRound", " - "
       "IgNoCornerRound", " - "
       "IgNatural", " - "
       "IgPeriodic", " - "
       "IgRoundAllVertexSetback", " - "
       "IgRoundSingleVertexSetback", " - "
       "IgRoundVertexEdgeSetback", " - "
       "IgRoundSetbackIsAbsolute", " - "
       "IgRoundSetbackIsRelative", " - "
       "IgCircular", " - "
       "IgUshaped", " - "
       "IgVshaped", " - "
       "IgPunchedEnd", " - "
       "IgLancedEnd", " - "
       "IgFormedEnd", " - "
       "IgSweepAlignParallel", " - "
       "IgSweepAlignNormal", " - "
       "IgRoundStartVertexEdgeSetback", " - "
       "IgRoundEndVertexEdgeSetback", " - "
       "IgSubtract", " - "
       "IgUnite", " - "
       "IgIntersect", " - "
       "IgContinuous", " - "
       "IgFlangeFulledge", " - "
       "IgFlangeCenterOfEdge", " - "
       "IgFlangeStartOnEndEdge", " - "
       "IgFlangeEndOnEndEdge", " - "
       "IgFlangeStartFromEndEdge", " - "
       "IgFlangeEndFromEndEdge", " - "
       "IgFlangeFromBothEndsOfEdge", " - "
       "IgFlangeOffset", " - "
       "IgChainedCornerRelief", " - "
       "IgTangentInterior", " - "
       "IgParallelToPlane", " - "
       "IgVbottomDimToFlat", " - "
       "IgVbottomDimToV", " - "
       "IgTaperDimAtTop", " - "
       "IgTaperDimAtBottom", " - "
       "IgCounterBoreProfileIsAtTop", " - "
       "IgCounterBoreProfileIsAtBottom", " - "
       "IgTaperByRlRatio", " - "
       "IgRndmiteratCorner", " - "
       "IgRndRollAroundCorner", " - "
       "IgRndPreserveTopologyon", " - "
       "IgRndPreserveTopologyOff", " - "
       "IgStepDraftPerpendicular", " - "
       "IgExtendBendRelief", " - "
       "IgEqualOffset", " - "
       "IgUnequalOffset", " - "
       "IgThickness", " - "
       "IgFacesTouchingCurvesOnly", " - "
       "IgCurvesetSeperator", " - "
       "IgSideInfosetSeperator", " - "
       "IgRegularThread", " - "
       "IgStraightPipethread", " - "
       "IgTaperedPipethread", " - "
       "IgRemoveInternalBoundaries", " - "
       "IgRemoveExternalBoundaries", " - "
       "IgDeleteFaceheal", " - "
       "IgEndcaps", " - "
       "IgCurvatureContinuous", " - "
       "IgNonsymmetric", " - "
       "IgTreatmentDraft", " - "
       "IgTreatmentCrown", " - "
       "IgCloseCornerNone", " - "
       "IgCloseCornerOpen", " - "
       "IgCloseCornerClosed", " - "
       "IgCloseCornerCircleCutout", " - "
       "IgPatternAlongCurve", " - "
       "IgPatternMountingBoss", " - "
       "IgSmClearanceCutout", " - "
       "IgSmMidplaceCutout", " - "
       "IgCentermark", " - "
    """
    IgNullConstant = 0  # FeaturePropertyMemberType
    IgLeft = 1  # FeaturePropertyMemberType
    IgRight = 2  # FeaturePropertyMemberType
    IgSymmetric = 3  # FeaturePropertyMemberType
    IgInside = 4  # FeaturePropertyMemberType
    IgOutside = 5  # FeaturePropertyMemberType
    IgBoth = 6  # FeaturePropertyMemberType
    IgNormalSidedummy = 7  # FeaturePropertyMemberType
    IgReverseNormalSidedummy = 8  # FeaturePropertyMemberType
    IgExtend = 9  # FeaturePropertyMemberType
    IgNoextend = 10  # FeaturePropertyMemberType
    IgThkinprofileplane = 11  # FeaturePropertyMemberType
    IgThkNormalToProfilePlane = 12  # FeaturePropertyMemberType
    IgFinite = 13  # FeaturePropertyMemberType
    IgTonext = 14  # FeaturePropertyMemberType
    IgFromTo = 15  # FeaturePropertyMemberType
    IgThroughAll = 16  # FeaturePropertyMemberType
    IgThreeHundredAndSixty = 17  # FeaturePropertyMemberType
    IgParallelDummy = 18  # FeaturePropertyMemberType
    IgAngularDummy = 19  # FeaturePropertyMemberType
    IgNormal = 20  # FeaturePropertyMemberType
    IgThroughAxis = 21  # FeaturePropertyMemberType
    IgSingleEdge = 22  # FeaturePropertyMemberType
    IgMultipleEdges = 23  # FeaturePropertyMemberType
    IgEdgesByLoop = 24  # FeaturePropertyMemberType
    IgEdgesByVertex = 25  # FeaturePropertyMemberType
    IgAll = 26  # FeaturePropertyMemberType
    IgConcave = 27  # FeaturePropertyMemberType
    IgConvex = 28  # FeaturePropertyMemberType
    IgStart = 29  # FeaturePropertyMemberType
    IgEnd = 30  # FeaturePropertyMemberType
    IgLinear = 31  # FeaturePropertyMemberType
    IgRadial = 32  # FeaturePropertyMemberType
    IgRegularHole = 33  # FeaturePropertyMemberType
    IgCounterBoreHole = 34  # FeaturePropertyMemberType
    IgCounterSinkHole = 35  # FeaturePropertyMemberType
    IgCounterDrillHole = 36  # FeaturePropertyMemberType
    IgTappedHole = 37  # FeaturePropertyMemberType
    IgTaperedHole = 38  # FeaturePropertyMemberType
    IgConstRadiusRound = 39  # FeaturePropertyMemberType
    IgVarRadiusRound = 40  # FeaturePropertyMemberType
    IgChamfer45degSetback = 41  # FeaturePropertyMemberType
    IgChamferAngleSetback = 42  # FeaturePropertyMemberType
    IgChamfer2Serbacks = 43  # FeaturePropertyMemberType
    IgNone = 44  # FeaturePropertyMemberType
    IgTaperByAngle = 45  # FeaturePropertyMemberType
    IgTaperByRatio = 46  # FeaturePropertyMemberType
    IgClosed = 47  # FeaturePropertyMemberType
    IgProfileBasedCrosssection = 48  # FeaturePropertyMemberType
    IgEdgeBasedCrosssection = 49  # FeaturePropertyMemberType
    IgTangent = 50  # FeaturePropertyMemberType
    IgRectangularBendRelief = 51  # FeaturePropertyMemberType
    IgFilletBendRelief = 52  # FeaturePropertyMemberType
    IgRipBendRelief = 53  # FeaturePropertyMemberType
    IgBendOnlyCornerRelief = 54  # FeaturePropertyMemberType
    IgBendAndFaceCornerRelief = 55  # FeaturePropertyMemberType
    IgRipCornerRelief = 56  # FeaturePropertyMemberType
    IgNftype = 57  # FeaturePropertyMemberType
    IgEquationType = 58  # FeaturePropertyMemberType
    IgPatternMirror = 59  # FeaturePropertyMemberType
    IgPatternRectangular = 60  # FeaturePropertyMemberType
    IgPatternCircular = 61  # FeaturePropertyMemberType
    IgPatternUserDefined = 62  # FeaturePropertyMemberType
    IgFromReferenceEnd = 64  # FeaturePropertyMemberType
    IgFromNonreferenceEnd = 65  # FeaturePropertyMemberType
    IgRndRollAcrossTnagentEdgesOn = 66  # FeaturePropertyMemberType
    IgRndRollAcrossTangentEdgesOff = 67  # FeaturePropertyMemberType
    IgRndCapAcrossSharpEdges = 68  # FeaturePropertyMemberType
    IgRndRollAcrossSharpEdges = 69  # FeaturePropertyMemberType
    IgRndRollAlongBlendEdgesOn = 70  # FeaturePropertyMemberType
    IgRndRollAlongBlendEdgesOff = 71  # FeaturePropertyMemberType
    IgToKepPoint = 72  # FeaturePropertyMemberType
    IgFlatten = 73  # FeaturePropertyMemberType
    IgAsConstruction = 74  # FeaturePropertyMemberType
    IgOffset = 75  # FeaturePropertyMemberType
    IgMitreParalletToThickness = 76  # FeaturePropertyMemberType
    IgMitreNormalToThickness = 77  # FeaturePropertyMemberType
    IgMitreByDist = 78  # FeaturePropertyMemberType
    IgMitreByAngle = 79  # FeaturePropertyMemberType
    IgMiterRegularCut = 80  # FeaturePropertyMemberType
    IgMitreManufacturingCut = 81  # FeaturePropertyMemberType
    IgProjectOptionProject = 82  # FeaturePropertyMemberType
    IgProjectOptionWrap = 83  # FeaturePropertyMemberType
    IgLip = 84  # FeaturePropertyMemberType
    IgGroove = 85  # FeaturePropertyMemberType
    IgPartingFromPlane = 86  # FeaturePropertyMemberType
    IgPartingFromSurface = 87  # FeaturePropertyMemberType
    IgPartingFromEdge = 88  # FeaturePropertyMemberType
    IgPartingFromCurve = 89  # FeaturePropertyMemberType
    IgSplitDraft = 90  # FeaturePropertyMemberType
    IgSplitAngle1Right = 91  # FeaturePropertyMemberType
    IgSplitAngle1Left = 92  # FeaturePropertyMemberType
    IgLouverformedendtype = 93  # FeaturePropertyMemberType
    IgLouverlancedendtype = 94  # FeaturePropertyMemberType
    IgLouverround = 95  # FeaturePropertyMemberType
    IgLouverroundnone = 96  # FeaturePropertyMemberType
    IgInsideDimension = 97  # FeaturePropertyMemberType
    IgOutsideDimension = 98  # FeaturePropertyMemberType
    IgFull = 99  # FeaturePropertyMemberType
    IgBend = 100  # FeaturePropertyMemberType
    IgAddRound = 101  # FeaturePropertyMemberType
    IgNoRound = 102  # FeaturePropertyMemberType
    IgCloseFaces = 103  # FeaturePropertyMemberType
    IgOverlapFaces = 104  # FeaturePropertyMemberType
    IgTreatmentOff = 105  # FeaturePropertyMemberType
    IgTreatmentIntersect = 106  # FeaturePropertyMemberType
    IgTreatmentCircleCutout = 107  # FeaturePropertyMemberType
    IgStepDreat = 108  # FeaturePropertyMemberType
    IgShowBoundaries = 109  # FeaturePropertyMemberType
    IgRemoveBoundaries = 110  # FeaturePropertyMemberType
    IgCornerRound = 111  # FeaturePropertyMemberType
    IgNoCornerRound = 112  # FeaturePropertyMemberType
    IgNatural = 113  # FeaturePropertyMemberType
    IgPeriodic = 114  # FeaturePropertyMemberType
    IgRoundAllVertexSetback = 115  # FeaturePropertyMemberType
    IgRoundSingleVertexSetback = 116  # FeaturePropertyMemberType
    IgRoundVertexEdgeSetback = 117  # FeaturePropertyMemberType
    IgRoundSetbackIsAbsolute = 118  # FeaturePropertyMemberType
    IgRoundSetbackIsRelative = 119  # FeaturePropertyMemberType
    IgCircular = 120  # FeaturePropertyMemberType
    IgUshaped = 121  # FeaturePropertyMemberType
    IgVshaped = 122  # FeaturePropertyMemberType
    IgPunchedEnd = 123  # FeaturePropertyMemberType
    IgLancedEnd = 124  # FeaturePropertyMemberType
    IgFormedEnd = 125  # FeaturePropertyMemberType
    IgSweepAlignParallel = 126  # FeaturePropertyMemberType
    IgSweepAlignNormal = 127  # FeaturePropertyMemberType
    IgRoundStartVertexEdgeSetback = 128  # FeaturePropertyMemberType
    IgRoundEndVertexEdgeSetback = 129  # FeaturePropertyMemberType
    IgSubtract = 130  # FeaturePropertyMemberType
    IgUnite = 131  # FeaturePropertyMemberType
    IgIntersect = 132  # FeaturePropertyMemberType
    IgContinuous = 133  # FeaturePropertyMemberType
    IgFlangeFulledge = 134  # FeaturePropertyMemberType
    IgFlangeCenterOfEdge = 135  # FeaturePropertyMemberType
    IgFlangeStartOnEndEdge = 136  # FeaturePropertyMemberType
    IgFlangeEndOnEndEdge = 137  # FeaturePropertyMemberType
    IgFlangeStartFromEndEdge = 138  # FeaturePropertyMemberType
    IgFlangeEndFromEndEdge = 139  # FeaturePropertyMemberType
    IgFlangeFromBothEndsOfEdge = 140  # FeaturePropertyMemberType
    IgFlangeOffset = 141  # FeaturePropertyMemberType
    IgChainedCornerRelief = 142  # FeaturePropertyMemberType
    IgTangentInterior = 143  # FeaturePropertyMemberType
    IgParallelToPlane = 144  # FeaturePropertyMemberType
    IgVbottomDimToFlat = 145  # FeaturePropertyMemberType
    IgVbottomDimToV = 146  # FeaturePropertyMemberType
    IgTaperDimAtTop = 147  # FeaturePropertyMemberType
    IgTaperDimAtBottom = 148  # FeaturePropertyMemberType
    IgCounterBoreProfileIsAtTop = 149  # FeaturePropertyMemberType
    IgCounterBoreProfileIsAtBottom = 150  # FeaturePropertyMemberType
    IgTaperByRlRatio = 151  # FeaturePropertyMemberType
    IgRndmiteratCorner = 152  # FeaturePropertyMemberType
    IgRndRollAroundCorner = 153  # FeaturePropertyMemberType
    IgRndPreserveTopologyon = 154  # FeaturePropertyMemberType
    IgRndPreserveTopologyOff = 155  # FeaturePropertyMemberType
    IgStepDraftPerpendicular = 156  # FeaturePropertyMemberType
    IgExtendBendRelief = 157  # FeaturePropertyMemberType
    IgEqualOffset = 158  # FeaturePropertyMemberType
    IgUnequalOffset = 159  # FeaturePropertyMemberType
    IgThickness = 160  # FeaturePropertyMemberType
    IgFacesTouchingCurvesOnly = 161  # FeaturePropertyMemberType
    IgCurvesetSeperator = 162  # FeaturePropertyMemberType
    IgSideInfosetSeperator = 163  # FeaturePropertyMemberType
    IgRegularThread = 164  # FeaturePropertyMemberType
    IgStraightPipethread = 165  # FeaturePropertyMemberType
    IgTaperedPipethread = 166  # FeaturePropertyMemberType
    IgRemoveInternalBoundaries = 167  # FeaturePropertyMemberType
    IgRemoveExternalBoundaries = 168  # FeaturePropertyMemberType
    IgDeleteFaceheal = 169  # FeaturePropertyMemberType
    IgEndcaps = 170  # FeaturePropertyMemberType
    IgCurvatureContinuous = 171  # FeaturePropertyMemberType
    IgNonsymmetric = 172  # FeaturePropertyMemberType
    IgTreatmentDraft = 173  # FeaturePropertyMemberType
    IgTreatmentCrown = 174  # FeaturePropertyMemberType
    IgCloseCornerNone = 175  # FeaturePropertyMemberType
    IgCloseCornerOpen = 176  # FeaturePropertyMemberType
    IgCloseCornerClosed = 177  # FeaturePropertyMemberType
    IgCloseCornerCircleCutout = 178  # FeaturePropertyMemberType
    IgPatternAlongCurve = 179  # FeaturePropertyMemberType
    IgPatternMountingBoss = 180  # FeaturePropertyMemberType
    IgSmClearanceCutout = 181  # FeaturePropertyMemberType
    IgSmMidplaceCutout = 182  # FeaturePropertyMemberType
    IgCentermark = 183  # FeaturePropertyMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SolidPunchBuilderTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SolidPunchBuilderTypes():
    """
    Represents the punch type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PunchType", " - "
       "DieType", " - "
    """
    PunchType = 0  # SolidPunchBuilderTypesMemberType
    DieType = 1  # SolidPunchBuilderTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SolidPunchBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.SheetMetal.SolidPunchBuilder` 
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateSolidPunchBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class Types():
        """
        Represents the punch type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PunchType", " - "
           "DieType", " - "
        """
        PunchType = 0  # SolidPunchBuilderTypesMemberType
        DieType = 1  # SolidPunchBuilderTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AutoCentroid: bool = ...
    """
    Returns or sets  the option to create centroid automatically.  
    
    <hr>
    
    Getter Method
    
    Signature ``AutoCentroid`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AutoCentroid`` 
    
    :param autoCentroid: 
    :type autoCentroid: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    ConstantThickness: bool = ...
    """
    Returns or sets  the option to maintain constant thickness during thickening.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConstantThickness`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstantThickness`` 
    
    :param constantThickness: 
    :type constantThickness: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the Radius value of the sharp edges of the bottom face 
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FromCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys that defines the start of transformation of the tool body.  
    
    <hr>
    
    Getter Method
    
    Signature ``FromCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FromCsys`` 
    
    :param fromCsys: 
    :type fromCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    HideTool: bool = ...
    """
    Returns or sets  the option to hide the tool body after creating the punch.  
    
    <hr>
    
    Getter Method
    
    Signature ``HideTool`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideTool`` 
    
    :param hideTool: 
    :type hideTool: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    IncludeRounding: bool = ...
    """
    Returns or sets  the option to round the sharp edges of bottom face and top face.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeRounding`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeRounding`` 
    
    :param includeRounding: 
    :type includeRounding: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    InferThickness: bool = ...
    """
    Returns or sets  the option to infer the thickness from the target body.  
    
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
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    PierceFaces: NXOpen.SelectFaceList = ...
    """
    Returns  the pierce faces of the tool body.  
    
    <hr>
    
    Getter Method
    
    Signature ``PierceFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFaceList` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    PunchRadius: NXOpen.Expression = ...
    """
    Returns  the Radius value of the sharp edges on the top face 
    
    <hr>
    
    Getter Method
    
    Signature ``PunchRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    TargetFace: NXOpen.SelectFace = ...
    """
    Returns  the target face 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectFace` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the thickness expression to use when the option to infer thickness is turned off.  
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ToCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the csys that defines the end of transformation of the tool body.  
    
    <hr>
    
    Getter Method
    
    Signature ``ToCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ToCsys`` 
    
    :param toCsys: 
    :type toCsys: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    ToolBody: NXOpen.SelectBody = ...
    """
    Returns  the tool body 
    
    <hr>
    
    Getter Method
    
    Signature ``ToolBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectBody` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Type: SolidPunchBuilderTypes = ...
    """
    Returns or sets  the type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.SolidPunchBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.SolidPunchBuilderTypes` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR sheet_metal_design ("SHEET METAL DESIGN")
    """
    Null: SolidPunchBuilder = ...  # unknown typename


class JoggleInputListItemBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Sheetmetal joggle input list item builder class.  
    
    This builder is used to
    interrogate the joggle inputitems in the list.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.JoggleBuilder.CreateJoggleInputListItem`
    
    .. versionadded:: NX11.0.0
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
    
    Depth: NXOpen.Expression = ...
    """
    Returns  the depth 
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Faces: NXOpen.ScCollector = ...
    """
    Returns  the faces 
    
    <hr>
    
    Getter Method
    
    Signature ``Faces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReverseDirection: bool = ...
    """
    Returns or sets  the reverse direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirection`` 
    
    :param reverseDirection: 
    :type reverseDirection: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: JoggleInputListItemBuilder = ...  # unknown typename


class FlexibleCableBuilderBendAngleDirectionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlexibleCableBuilderBendAngleDirectionOptions():
    """
    This enum represents the bend angle direction for the bend segment. First member of the cable is
    always a planar segment. For this, the normal direction for bend angle is opposite to the
    thickness direction. This convention continues untill a fold (bend type having nonzero
    path adjustment angle) is placed. After this, the convention reverses, meaning the normal
    direction for the bend angle is along the thickness direction. For each member, the thickness
    direction signifies the material addition direction. This is an input for the entire cable at the
    start.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ReverseNormalDirection", "Bend angle reverse normal direction."
       "NormalDirection", "Bend angle normal direction."
    """
    ReverseNormalDirection = 0  # FlexibleCableBuilderBendAngleDirectionOptionsMemberType
    NormalDirection = 1  # FlexibleCableBuilderBendAngleDirectionOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlexibleCableBuilderPathAdjustmentAngleDirectionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlexibleCableBuilderPathAdjustmentAngleDirectionOptions():
    """
    This enum represents the path adjustment angle direction for the bend segment. The cross
    product of the cable direction and the bend angle direction determined using above
    convention gives the right direction for the path adjustment angle. The left direction is
    opposite to that. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "LeftDirection", "Path adjustment angle left direction."
       "RightDirection", "Path adjustment angle right direction."
    """
    LeftDirection = 0  # FlexibleCableBuilderPathAdjustmentAngleDirectionOptionsMemberType
    RightDirection = 1  # FlexibleCableBuilderPathAdjustmentAngleDirectionOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlexibleCableBuilderSegmentTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlexibleCableBuilderSegmentTypeOptions():
    """
    Represents the Flexible Cable segment options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Planar", "Planar cable segment."
       "Bend", "Bend cable segment."
    """
    Planar = 0  # FlexibleCableBuilderSegmentTypeOptionsMemberType
    Bend = 1  # FlexibleCableBuilderSegmentTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlexibleCableBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Flexible Cable feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateFlexibleCableBuilder`
    
    Default values.
    
    ========================  =========================================
    Property                  Value
    ========================  =========================================
    ConductorCount            5 
    ------------------------  -----------------------------------------
    ConductorSpacing.Value    1 (millimeters part), 0.1 (inches part) 
    ------------------------  -----------------------------------------
    ConductorWidth.Value      2 (millimeters part), 0.2 (inches part) 
    ------------------------  -----------------------------------------
    CrossSectionWidth.Value   20 (millimeters part), 1 (inches part) 
    ------------------------  -----------------------------------------
    StrippingLength.Value     3 (millimeters part), 0.3 (inches part) 
    ------------------------  -----------------------------------------
    Thickness.Value           1 (millimeters part), 0.04 (inches part) 
    ========================  =========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class BendAngleDirectionOptions():
        """
        This enum represents the bend angle direction for the bend segment. First member of the cable is
        always a planar segment. For this, the normal direction for bend angle is opposite to the
        thickness direction. This convention continues untill a fold (bend type having nonzero
        path adjustment angle) is placed. After this, the convention reverses, meaning the normal
        direction for the bend angle is along the thickness direction. For each member, the thickness
        direction signifies the material addition direction. This is an input for the entire cable at the
        start.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ReverseNormalDirection", "Bend angle reverse normal direction."
           "NormalDirection", "Bend angle normal direction."
        """
        ReverseNormalDirection = 0  # FlexibleCableBuilderBendAngleDirectionOptionsMemberType
        NormalDirection = 1  # FlexibleCableBuilderBendAngleDirectionOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PathAdjustmentAngleDirectionOptions():
        """
        This enum represents the path adjustment angle direction for the bend segment. The cross
        product of the cable direction and the bend angle direction determined using above
        convention gives the right direction for the path adjustment angle. The left direction is
        opposite to that. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "LeftDirection", "Path adjustment angle left direction."
           "RightDirection", "Path adjustment angle right direction."
        """
        LeftDirection = 0  # FlexibleCableBuilderPathAdjustmentAngleDirectionOptionsMemberType
        RightDirection = 1  # FlexibleCableBuilderPathAdjustmentAngleDirectionOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SegmentTypeOptions():
        """
        Represents the Flexible Cable segment options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Planar", "Planar cable segment."
           "Bend", "Bend cable segment."
        """
        Planar = 0  # FlexibleCableBuilderSegmentTypeOptionsMemberType
        Bend = 1  # FlexibleCableBuilderSegmentTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetIndexOfSegment(self, flexibleCableSegment: FlexibleCableSegment) -> int:
        """
        Returns the index of cable segment.  
        
        Signature ``GetIndexOfSegment(flexibleCableSegment)`` 
        
        :param flexibleCableSegment:  :py:class:`Features.SheetMetal.FlexibleCableSegment`.  
        :type flexibleCableSegment: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableSegment` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetSegment(self, index: int) -> FlexibleCableSegment:
        """
        Returns the cable segment at given index.  
        
        Signature ``GetSegment(index)`` 
        
        :param index:  Index of the required :py:class:`Features.SheetMetal.FlexibleCableSegment`.  
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableSegment` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def DeleteSegment(self, index: int) -> None:
        """
        Deletes a cable segment at given index.  
        
        Signature ``DeleteSegment(index)`` 
        
        :param index:  Index of the :py:class:`Features.SheetMetal.FlexibleCableSegment` which needs to be deleted.  
        :type index: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def DeleteAllSegments(self) -> None:
        """
        Deletes all cable segments.  
        
        Signature ``DeleteAllSegments()`` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreatePlanarSegment(self, length: str, segmentIndex: int) -> FlexibleCableSegment:
        """
        Creates a new :py:class:`Features.SheetMetal.FlexibleCableSegment` planar segment.  
        
        This
        can be either appended at the end, or inserted in between the list. This is decided by
        the input index.  
        
        Signature ``CreatePlanarSegment(length, segmentIndex)`` 
        
        :param length:  Length.  
        :type length: str 
        :param segmentIndex:  Index.  
        :type segmentIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableSegment` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def CreateBendSegment(self, bendAngle: str, bendRadius: str, pathAdjustmentAngle: str, bendAngleDirection: FlexibleCableBuilderBendAngleDirectionOptions, pathAdjustmentAngleDirection: FlexibleCableBuilderPathAdjustmentAngleDirectionOptions, segmentIndex: int) -> FlexibleCableSegment:
        """
        Creates a new :py:class:`Features.SheetMetal.FlexibleCableSegment` bend segment.  
        
        This
        can be either appended at the end, or inserted in between the list. This is decided by
        the input index.  
        
        Signature ``CreateBendSegment(bendAngle, bendRadius, pathAdjustmentAngle, bendAngleDirection, pathAdjustmentAngleDirection, segmentIndex)`` 
        
        :param bendAngle:  Bend angle.  
        :type bendAngle: str 
        :param bendRadius:  Bend radius.  
        :type bendRadius: str 
        :param pathAdjustmentAngle:  Path adjustment angle.  
        :type pathAdjustmentAngle: str 
        :param bendAngleDirection:  :py:class:`Features.SheetMetal.FlexibleCableBuilderBendAngleDirectionOptions`  
        :type bendAngleDirection: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderBendAngleDirectionOptions` 
        :param pathAdjustmentAngleDirection:  :py:class:`Features.SheetMetal.FlexibleCableBuilderPathAdjustmentAngleDirectionOptions`  
        :type pathAdjustmentAngleDirection: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableBuilderPathAdjustmentAngleDirectionOptions` 
        :param segmentIndex:  Index.  
        :type segmentIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlexibleCableSegment` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def GetSegmentCount(self) -> int:
        """
        Get the count of :py:class:`Features.SheetMetal.FlexibleCableSegment`.  
        
        Signature ``GetSegmentCount()`` 
        
        :returns:  Segment count.  
        :rtype: int 
        
        .. versionadded:: NX7.5.0
        
        License requirements: nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    CableDirection: NXOpen.Direction = ...
    """
    Returns or sets  the cable direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``CableDirection`` 
    
    :returns:  Cable direction.  
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``CableDirection`` 
    
    :param cableDirection: 
    :type cableDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    ConductorCount: int = ...
    """
    Returns or sets  the count of conductors.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConductorCount`` 
    
    :returns:  Number of conductors of cable.  
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ConductorCount`` 
    
    :param noOfConductors:  Number of conductors of cable.  
    :type noOfConductors: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    ConductorSpacing: NXOpen.Expression = ...
    """
    Returns  the conductor spacing.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConductorSpacing`` 
    
    :returns:  Conductor spacing.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    ConductorWidth: NXOpen.Expression = ...
    """
    Returns  the conductor width.  
    
    <hr>
    
    Getter Method
    
    Signature ``ConductorWidth`` 
    
    :returns:  Conductor width of the cable.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    CrossSectionWidth: NXOpen.Expression = ...
    """
    Returns  the cross section width.  
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionWidth`` 
    
    :returns:  Cable width.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    SegmentList: NXOpen.TaggedObjectList = ...
    """
    Returns  the cable segment list.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentList`` 
    
    :returns:  Cable segment list.  
    :rtype: :py:class:`NXOpen.TaggedObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    StartPoint: NXOpen.Point = ...
    """
    Returns or sets  the start point.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartPoint`` 
    
    :returns:  Start point.  
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartPoint`` 
    
    :param startPoint: 
    :type startPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    StrippingLength: NXOpen.Expression = ...
    """
    Returns  the stripping length.  
    
    <hr>
    
    Getter Method
    
    Signature ``StrippingLength`` 
    
    :returns:  Stripping length of the cable.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the thickness.  
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns:  Cable thickness.  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    ThicknessDirection: NXOpen.Direction = ...
    """
    Returns or sets  the thickness direction.  
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessDirection`` 
    
    :returns:  Cable thickness direction.  
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ThicknessDirection`` 
    
    :param thicknessDirection: 
    :type thicknessDirection: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: FlexibleCableBuilder = ...  # unknown typename


class BendListBuilder(NXOpen.Builder):
    """
    Represents a Sheetmetal Flat Pattern bend list builder class.  
    
    This builder is used to
    edit the bend sequence ID and bend name of the bends in the bend list.
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBendListBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def PopulateBendListFromView(self, flatPatternView: NXOpen.View) -> None:
        """
        This will populate the bend list from given flat pattern modeling view
        
        Signature ``PopulateBendListFromView(flatPatternView)`` 
        
        :param flatPatternView: 
        :type flatPatternView: :py:class:`NXOpen.View` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def EditBendItem(self, existingBendId: int, newBendId: int, newBendName: str) -> None:
        """
        This will edit a bend item in the list which has existing bend Id same as input id
        and assign new bend Id and bend name
        
        Signature ``EditBendItem(existingBendId, newBendId, newBendName)`` 
        
        :param existingBendId: Existing Bend Id to search 
        :type existingBendId: int 
        :param newBendId: Bend Id to be assigned 
        :type newBendId: int 
        :param newBendName: Bend name to be assigned 
        :type newBendName: str 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendList: BendListItemBuilderList = ...
    """
    Returns  the bend list 
    
    <hr>
    
    Getter Method
    
    Signature ``BendList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendListItemBuilderList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Null: BendListBuilder = ...  # unknown typename


class AeroReformBuilder(SheetmetalBaseBuilder):
    """
    Represents a Aerospace Sheet Metal REFORM Builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateReformBuilder`
    
    .. versionadded:: NX4.0.0
    """
    UnformFaceCollector: NXOpen.ScCollector = ...
    """
    Returns or sets  the unformed faces smart collector object.  
    
    <hr>
    
    Getter Method
    
    Signature ``UnformFaceCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``UnformFaceCollector`` 
    
    :param unformFaceCollector: 
    :type unformFaceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AeroReformBuilder = ...  # unknown typename


class BeadBuilderCrossSectionTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BeadBuilderCrossSectionTypeOptions():
    """
    This enum represents the cross section type options for the Bead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Circular", " - "
       "Ushaped", " - "
       "Vshaped", " - "
    """
    Circular = 0  # BeadBuilderCrossSectionTypeOptionsMemberType
    Ushaped = 1  # BeadBuilderCrossSectionTypeOptionsMemberType
    Vshaped = 2  # BeadBuilderCrossSectionTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BeadBuilderEndTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BeadBuilderEndTypeOptions():
    """
    This enum represents the end type options for the Bead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Punched", " - "
       "Lanced", " - "
       "Formed", " - "
       "Tapered", " - "
    """
    Punched = 0  # BeadBuilderEndTypeOptionsMemberType
    Lanced = 1  # BeadBuilderEndTypeOptionsMemberType
    Formed = 2  # BeadBuilderEndTypeOptionsMemberType
    Tapered = 3  # BeadBuilderEndTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BeadBuilderHeightSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BeadBuilderHeightSideOptions():
    """
    This enum represents the depth direction for the Bead. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Material removed on the side of the section normal."
       "SectionReverseNormalSide", "Material removed on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # BeadBuilderHeightSideOptionsMemberType
    SectionReverseNormalSide = 1  # BeadBuilderHeightSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BeadBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Bead feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBeadFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class CrossSectionTypeOptions():
        """
        This enum represents the cross section type options for the Bead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Circular", " - "
           "Ushaped", " - "
           "Vshaped", " - "
        """
        Circular = 0  # BeadBuilderCrossSectionTypeOptionsMemberType
        Ushaped = 1  # BeadBuilderCrossSectionTypeOptionsMemberType
        Vshaped = 2  # BeadBuilderCrossSectionTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EndTypeOptions():
        """
        This enum represents the end type options for the Bead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Punched", " - "
           "Lanced", " - "
           "Formed", " - "
           "Tapered", " - "
        """
        Punched = 0  # BeadBuilderEndTypeOptionsMemberType
        Lanced = 1  # BeadBuilderEndTypeOptionsMemberType
        Formed = 2  # BeadBuilderEndTypeOptionsMemberType
        Tapered = 3  # BeadBuilderEndTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class HeightSideOptions():
        """
        This enum represents the depth direction for the Bead. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Material removed on the side of the section normal."
           "SectionReverseNormalSide", "Material removed on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # BeadBuilderHeightSideOptionsMemberType
        SectionReverseNormalSide = 1  # BeadBuilderHeightSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetHeight(self, beadHeight: str) -> None:
        """
        Signature ``SetHeight(beadHeight)`` 
        
        :param beadHeight: 
        :type beadHeight: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.Height` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetWidth(self, beadWidth: str) -> None:
        """
        Signature ``SetWidth(beadWidth)`` 
        
        :param beadWidth: 
        :type beadWidth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.Width` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetAngle(self, beadAngle: str) -> None:
        """
        Signature ``SetAngle(beadAngle)`` 
        
        :param beadAngle: 
        :type beadAngle: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.Angle` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetRadius(self, beadRadius: str) -> None:
        """
        Signature ``SetRadius(beadRadius)`` 
        
        :param beadRadius: 
        :type beadRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.Radius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetPunchedWidth(self, punchedWidth: str) -> None:
        """
        Signature ``SetPunchedWidth(punchedWidth)`` 
        
        :param punchedWidth: 
        :type punchedWidth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.PunchedWidth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetPunchRadius(self, punchRadius: str) -> None:
        """
        Signature ``SetPunchRadius(punchRadius)`` 
        
        :param punchRadius: 
        :type punchRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.PunchRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetDieRadius(self, beadDieRadius: str) -> None:
        """
        Signature ``SetDieRadius(beadDieRadius)`` 
        
        :param beadDieRadius: 
        :type beadDieRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.DieRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a Bead or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    CrossSectionType: BeadBuilderCrossSectionTypeOptions = ...
    """
    Returns or sets  the bead profile type .  
    
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions.Circular <NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions>` to have profile of half circle.
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions.Ushaped <NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions>` to have profile of U shape.
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions.Vshaped <NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions>` to have profile of V shape.
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``CrossSectionType`` 
    
    :param crossSectionOption: 
    :type crossSectionOption: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderCrossSectionTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the bead die radius.  
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    EndType: BeadBuilderEndTypeOptions = ...
    """
    Returns or sets  the bead end type .  
    
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions.Formed  <NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions>` to have ends of bead feature be formed.
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions.Lanced  <NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions>` to have ends of bead feature be Lanced.
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions.Punched <NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions>` to have ends of bead feature be Punched.
    Specify :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions.Tapered <NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions>` to have ends of bead feature be Tapered.
    
    <hr>
    
    Getter Method
    
    Signature ``EndType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``EndType`` 
    
    :param beadEndOptions: 
    :type beadEndOptions: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderEndTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Height: NXOpen.Expression = ...
    """
    Returns  the height of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``Height`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    HeightSide: BeadBuilderHeightSideOptions = ...
    """
    Returns or sets  the Height side for the bead.  
    
    This is used to specify the direction in which the Bead is created. If Bead creation must happen in the
    direction of the Section Normal (specified using the :py:meth:`NXOpen.Features.SheetMetal.BeadBuilder.Section``) then
    pass the value of :py:class:`NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions.SectionNormalSide <NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions>`
    If Bead creation must happen in the opposite direction to that of Section Normal, set the value to be
    :py:class:`NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions.SectionReverseNormalSide <NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions>`
    
    <hr>
    
    Getter Method
    
    Signature ``HeightSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``HeightSide`` 
    
    :param heightSide: 
    :type heightSide: :py:class:`NXOpen.Features.SheetMetal.BeadBuilderHeightSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    IncludeRounding: bool = ...
    """
    Returns or sets  the rounding type .  
    
    Specify true to Round the Sharp edges.
    Specify false to avoid rounding.
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeRounding`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeRounding`` 
    
    :param rounding: 
    :type rounding: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MinimumToolClearance: NXOpen.Expression = ...
    """
    Returns  
    the Minimum tool clearance expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumToolClearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    PunchRadius: NXOpen.Expression = ...
    """
    Returns  the bead punch radius.  
    
    <hr>
    
    Getter Method
    
    Signature ``PunchRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    PunchedWidth: NXOpen.Expression = ...
    """
    Returns  the Punched width of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``PunchedWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Radius: NXOpen.Expression = ...
    """
    Returns  the radius of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``Radius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the Section used by the bead.  
    
    section should be open.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the Slave Sketch used by the Bead, If one exists.  
    
    If the Sketch is created internally as part of the Bead command in the UI, then it shall be consumed by the Bead and shall not show up as a separate feature in the Part Navigator.
    If such a behaviour is deired, then specify the Sketch here.
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    TaperDistance: NXOpen.Expression = ...
    """
    Returns  the taper distance of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``TaperDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width of the bead.  
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: BeadBuilder = ...  # unknown typename


class MetaformBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.Metaform` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateMetaformBuilder`
    
    Default values.
    
    ============================  ===========================================
    Property                      Value
    ============================  ===========================================
    AngularTolerance.Value        90 
    ----------------------------  -------------------------------------------
    ChordalTolerance.Value        0.75 (millimeters part), 0 (inches part) 
    ----------------------------  -------------------------------------------
    ElasticModulus.Value          210000000 
    ----------------------------  -------------------------------------------
    HoleRemovalMinModulus.Value   6.9e-008 
    ----------------------------  -------------------------------------------
    InferThickness                0 
    ----------------------------  -------------------------------------------
    LinearTolerance.Value         25 (millimeters part), 0 (inches part) 
    ----------------------------  -------------------------------------------
    NeutralFactor.Value           0.33 
    ----------------------------  -------------------------------------------
    OutputLayer                   1 
    ----------------------------  -------------------------------------------
    PoissonsRatio.Value           0.3 
    ----------------------------  -------------------------------------------
    RValue.Value                  1 
    ----------------------------  -------------------------------------------
    RemoveHoles                   0 
    ----------------------------  -------------------------------------------
    TangentModulus.Value          6900 
    ----------------------------  -------------------------------------------
    Thickness.Value               3 (millimeters part), 0 (inches part) 
    ----------------------------  -------------------------------------------
    YieldStress.Value             190000 (millimeters part), 0 (inches part) 
    ============================  ===========================================
    
    .. versionadded:: NX7.5.0
    """
    
    def CreateSMBoundaryCondition(self) -> SMBoundaryConditionBuilder:
        """
        Create a new boundary condition.  
        
        Signature ``CreateSMBoundaryCondition()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilder` 
        
        .. versionadded:: NX7.5.0
        
        License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    AngularTolerance: NXOpen.Expression = ...
    """
    Returns  the angular tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``AngularTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ChordalTolerance: NXOpen.Expression = ...
    """
    Returns  the chordal tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``ChordalTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    ElasticModulus: NXOpen.Expression = ...
    """
    Returns  the elastic modulus 
    
    <hr>
    
    Getter Method
    
    Signature ``ElasticModulus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    EndRegion: NXOpen.ScCollector = ...
    """
    Returns  the end region Metaform feature will map geometry "From" surfaces "To" surfaces.  
    
    The End
    Region defines the "To" surface. 
    
    <hr>
    
    Getter Method
    
    Signature ``EndRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    HoleRemovalMinModulus: NXOpen.Expression = ...
    """
    Returns  the hole removal min modulus 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleRemovalMinModulus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    InferThickness: bool = ...
    """
    Returns or sets  the option to infer thickness from the Start Region.  
    
    <hr>
    
    Getter Method
    
    Signature ``InferThickness`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferThickness`` 
    
    :param inferThickness: 
    :type inferThickness: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    LinearTolerance: NXOpen.Expression = ...
    """
    Returns  the linear tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``LinearTolerance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    NeutralFactor: NXOpen.Expression = ...
    """
    Returns  the neutral factor 
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    OutputLayer: int = ...
    """
    Returns or sets  the output layer.  
    
    Layer on which the Transform Geometry will be created. 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputLayer`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputLayer`` 
    
    :param outputLayer: 
    :type outputLayer: int 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    PoissonsRatio: NXOpen.Expression = ...
    """
    Returns  the Poisson's ratio 
    
    <hr>
    
    Getter Method
    
    Signature ``PoissonsRatio`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    RValue: NXOpen.Expression = ...
    """
    Returns  the r value 
    
    <hr>
    
    Getter Method
    
    Signature ``RValue`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    RemoveHoles: bool = ...
    """
    Returns or sets  the remove holes 
    
    <hr>
    
    Getter Method
    
    Signature ``RemoveHoles`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RemoveHoles`` 
    
    :param removeHoles: 
    :type removeHoles: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ReverseThicknessDirection: bool = ...
    """
    Returns or sets  the thickness direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseThicknessDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseThicknessDirection`` 
    
    :param reverseThicknessDirection: 
    :type reverseThicknessDirection: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SMBoundaryConditions: SMBoundaryConditionBuilderList = ...
    """
    Returns  the boundary conditions 
    
    <hr>
    
    Getter Method
    
    Signature ``SMBoundaryConditions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilderList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    StartRegion: NXOpen.ScCollector = ...
    """
    Returns  the start region.  
    
    Metaform feature will map geometry "From" surfaces "To" surfaces. The Start
    Region defines the "From" surface. 
    
    <hr>
    
    Getter Method
    
    Signature ``StartRegion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TangentModulus: NXOpen.Expression = ...
    """
    Returns  the tangent modulus 
    
    <hr>
    
    Getter Method
    
    Signature ``TangentModulus`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Thickness: NXOpen.Expression = ...
    """
    Returns  the thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``Thickness`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    TransformGeometry: NXOpen.SelectNXObjectList = ...
    """
    Returns  the transform geometry Metaform feature will map geometry "From" surfaces "To" surfaces.  
    
    The Start
    Region defines the "From" surface and the End Region defines the "To" surface. Transform Geometry 
    is the actual geometry on the "From" surfaces that will be produced as output geometry.
    
    <hr>
    
    Getter Method
    
    Signature ``TransformGeometry`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    YieldStress: NXOpen.Expression = ...
    """
    Returns  the yield stress 
    
    <hr>
    
    Getter Method
    
    Signature ``YieldStress`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    Null: MetaformBuilder = ...  # unknown typename


class BendOptionsBendReliefTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendOptionsBendReliefTypeOptions():
    """
    This enum represents the bend relief type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "igRipBendRelief"
       "Square", "igRectangularBendRelief"
       "Round", "igFilletBendRelief"
    """
    NotSet = 0  # BendOptionsBendReliefTypeOptionsMemberType
    Square = 1  # BendOptionsBendReliefTypeOptionsMemberType
    Round = 2  # BendOptionsBendReliefTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendOptionsCornerReliefTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendOptionsCornerReliefTypeOptions():
    """
    This enum represents the corner relief type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "BendOnly", "igBendOnlyCornerRelief"
       "BendAndFace", "igBendAndFaceCornerRelief"
       "BendAndFaceChain", "igChainedCornerRelief"
    """
    NotSet = 0  # BendOptionsCornerReliefTypeOptionsMemberType
    BendOnly = 1  # BendOptionsCornerReliefTypeOptionsMemberType
    BendAndFace = 2  # BendOptionsCornerReliefTypeOptionsMemberType
    BendAndFaceChain = 3  # BendOptionsCornerReliefTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendOptions(NXOpen.TaggedObject):
    """
    Represents a Sheetmetal Bend Options class.  
    
    .. versionadded:: NX4.0.0
    """
    
    class BendReliefTypeOptions():
        """
        This enum represents the bend relief type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "igRipBendRelief"
           "Square", "igRectangularBendRelief"
           "Round", "igFilletBendRelief"
        """
        NotSet = 0  # BendOptionsBendReliefTypeOptionsMemberType
        Square = 1  # BendOptionsBendReliefTypeOptionsMemberType
        Round = 2  # BendOptionsBendReliefTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CornerReliefTypeOptions():
        """
        This enum represents the corner relief type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "BendOnly", "igBendOnlyCornerRelief"
           "BendAndFace", "igBendAndFaceCornerRelief"
           "BendAndFaceChain", "igChainedCornerRelief"
        """
        NotSet = 0  # BendOptionsCornerReliefTypeOptionsMemberType
        BendOnly = 1  # BendOptionsCornerReliefTypeOptionsMemberType
        BendAndFace = 2  # BendOptionsCornerReliefTypeOptionsMemberType
        BendAndFaceChain = 3  # BendOptionsCornerReliefTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetBendRadius(self, radius: str) -> None:
        """
        Sets the bend radius.  
        
        Signature ``SetBendRadius(radius)`` 
        
        :param radius: 
        :type radius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.BendRadius` instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetBendReliefDepth(self, depth: str) -> None:
        """
        Sets the bend relief depth.  
        
        Applicable only if :py:meth:`NXOpen.Features.SheetMetal.BendOptions.BendReliefTypeOptions` is 
        set to a value other than :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>`.
        
        Signature ``SetBendReliefDepth(depth)`` 
        
        :param depth: 
        :type depth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.BendReliefDepth` instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetBendReliefWidth(self, width: str) -> None:
        """
        Sets the bend relief width.  
        
        Applicable only if :py:meth:`NXOpen.Features.SheetMetal.BendOptions.BendReliefTypeOptions` is 
        set to a value other than :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>`.
        
        Signature ``SetBendReliefWidth(width)`` 
        
        :param width: 
        :type width: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.BendReliefWidth` instead.
        
        License requirements: None.
        """
        ...
    
    
    def SetNeutralFactor(self, neutralFactor: str) -> None:
        """
        Sets the neutral factor.  
        
        Signature ``SetNeutralFactor(neutralFactor)`` 
        
        :param neutralFactor: 
        :type neutralFactor: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.NeutralFactor` instead.
        
        License requirements: None.
        """
        ...
    
    BendRadius: NXOpen.Expression = ...
    """
    Returns  the bend radius.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    BendReliefDepth: NXOpen.Expression = ...
    """
    Returns  the bend relief depth.  
    
    Applicable only if :py:meth:`NXOpen.Features.SheetMetal.BendOptions.BendReliefTypeOptions` is 
    set to a value other than :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    BendReliefType: BendOptionsBendReliefTypeOptions = ...
    """
    Returns or sets  the bend relief type.  
    
    Specify :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>` if you do not want a bend relief.
    Specify :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.Square <Features.SheetMetal.BendOptionsBendReliefTypeOptions>` for a square/rectangular bend relief.
    Specify :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.Round <Features.SheetMetal.BendOptionsBendReliefTypeOptions>` for a rounded bend relief.
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptionsBendReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendReliefType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.BendOptionsBendReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    BendReliefWidth: NXOpen.Expression = ...
    """
    Returns  the bend relief width.  
    
    Applicable only if :py:meth:`NXOpen.Features.SheetMetal.BendOptions.BendReliefTypeOptions` is 
    set to a value other than :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    CornerReliefType: BendOptionsCornerReliefTypeOptions = ...
    """
    Returns or sets  the corner relief type.  
    
    Use one of the values from :py:class:`NXOpen.Features.SheetMetal.BendOptionsCornerReliefTypeOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``CornerReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptionsCornerReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CornerReliefType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.BendOptionsCornerReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    DieToolId: int = ...
    """
    Returns or sets  the die tool id selected 
    
    <hr>
    
    Getter Method
    
    Signature ``DieToolId`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DieToolId`` 
    
    :param dieToolId: 
    :type dieToolId: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    DieToolIdName: str = ...
    """
    Returns or sets  the die tool id string selected 
    
    <hr>
    
    Getter Method
    
    Signature ``DieToolIdName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DieToolIdName`` 
    
    :param dieToolId: 
    :type dieToolId: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ExtendBendRelief: bool = ...
    """
    Returns or sets  the option to extend the bend relief if required.  
    
    This only applies if the bend relief type
    is set to a value other than :py:class:`Features.SheetMetal.BendOptionsBendReliefTypeOptions.None <Features.SheetMetal.BendOptionsBendReliefTypeOptions>`.    
    
    <hr>
    
    Getter Method
    
    Signature ``ExtendBendRelief`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExtendBendRelief`` 
    
    :param extend: 
    :type extend: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    NeutralFactor: NXOpen.Expression = ...
    """
    Returns  the neutral factor.  
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    OverrideToolSet: bool = ...
    """
    Returns or sets  the override tool set toggle value.  
    
    <hr>
    
    Getter Method
    
    Signature ``OverrideToolSet`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverrideToolSet`` 
    
    :param overrideToolSet: 
    :type overrideToolSet: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    PunchToolId: int = ...
    """
    Returns or sets  the punch tool id selected 
    
    <hr>
    
    Getter Method
    
    Signature ``PunchToolId`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PunchToolId`` 
    
    :param punchToolId: 
    :type punchToolId: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    PunchToolIdName: str = ...
    """
    Returns or sets  the punch tool id string selected 
    
    <hr>
    
    Getter Method
    
    Signature ``PunchToolIdName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``PunchToolIdName`` 
    
    :param punchToolId: 
    :type punchToolId: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UseGlobalBendRadius: bool = ...
    """
    Returns or sets  the Use Global Bend Radius toggle.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalBendRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalBendRadius`` 
    
    :param useGlobalBendRadius: 
    :type useGlobalBendRadius: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UseGlobalNeutralFactor: bool = ...
    """
    Returns or sets  the Use Global Neutral Factor toggle.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalNeutralFactor`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalNeutralFactor`` 
    
    :param useGlobalNeutralFactor: 
    :type useGlobalNeutralFactor: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UseGlobalReliefDepth: bool = ...
    """
    Returns or sets  the Use Global Relief Depth toggle.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalReliefDepth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalReliefDepth`` 
    
    :param useGlobalReliefDepth: 
    :type useGlobalReliefDepth: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    UseGlobalReliefWidth: bool = ...
    """
    Returns or sets  the Use Global Relief Width toggle.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobalReliefWidth`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobalReliefWidth`` 
    
    :param useGlobalReliefWidth: 
    :type useGlobalReliefWidth: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: BendOptions = ...  # unknown typename


class LouverBuilderDepthSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LouverBuilderDepthSideOptions():
    """
    This enum represents the depth side for the louver. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Material added on the side of the section normal."
       "SectionReverseNormalSide", "Material added on the side opposite to that of the section normal."
    """
    SectionNormalSide = 0  # LouverBuilderDepthSideOptionsMemberType
    SectionReverseNormalSide = 1  # LouverBuilderDepthSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LouverBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LouverBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the louver width is measured. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves 
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    The "right" side at any point along the section can also be represented by the vector resulting from 
    the cross product of the curve tangent (of the section curve at that point) and the section normal. 
    The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # LouverBuilderSectionSideOptionsMemberType
    Right = 1  # LouverBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LouverBuilderEndTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LouverBuilderEndTypeOptions():
    """
    This enum represents the end type for the louver. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Formed", " - "
       "Lanced", " - "
    """
    Formed = 0  # LouverBuilderEndTypeOptionsMemberType
    Lanced = 1  # LouverBuilderEndTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LouverBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a louver feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateLouverFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class DepthSideOptions():
        """
        This enum represents the depth side for the louver. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Material added on the side of the section normal."
           "SectionReverseNormalSide", "Material added on the side opposite to that of the section normal."
        """
        SectionNormalSide = 0  # LouverBuilderDepthSideOptionsMemberType
        SectionReverseNormalSide = 1  # LouverBuilderDepthSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the louver width is measured. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves 
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        The "right" side at any point along the section can also be represented by the vector resulting from 
        the cross product of the curve tangent (of the section curve at that point) and the section normal. 
        The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # LouverBuilderSectionSideOptionsMemberType
        Right = 1  # LouverBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EndTypeOptions():
        """
        This enum represents the end type for the louver. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Formed", " - "
           "Lanced", " - "
        """
        Formed = 0  # LouverBuilderEndTypeOptionsMemberType
        Lanced = 1  # LouverBuilderEndTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetDepth(self, depth: str) -> None:
        """
        Signature ``SetDepth(depth)`` 
        
        :param depth: 
        :type depth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.Depth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetWidth(self, width: str) -> None:
        """
        Signature ``SetWidth(width)`` 
        
        :param width: 
        :type width: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.Width` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetDieRadius(self, dieRadius: str) -> None:
        """
        Signature ``SetDieRadius(dieRadius)`` 
        
        :param dieRadius: 
        :type dieRadius: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.DieRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        This method verifies that the builder data is valid for louver creation.  
        
        If the builder data is valid, it returns a value of 0.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  data validity flag  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    Depth: NXOpen.Expression = ...
    """
    Returns  the depth of the louver 
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns:  The depth of the louver  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    DepthSide: LouverBuilderDepthSideOptions = ...
    """
    Returns or sets  the depth side for the louver.  
    
    <hr>
    
    Getter Method
    
    Signature ``DepthSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderDepthSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``DepthSide`` 
    
    :param depthSide: 
    :type depthSide: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderDepthSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the die radius.  
    
    Not used if :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.IncludeRounding` is false. 
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    EndType: LouverBuilderEndTypeOptions = ...
    """
    Returns or sets  the end type for the louver.  
    
    Select lanced end or formed end from :py:class:`NXOpen.Features.SheetMetal.LouverBuilderEndTypeOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``EndType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderEndTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``EndType`` 
    
    :param endType: 
    :type endType: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderEndTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    IncludeRounding: bool = ...
    """
    Returns or sets  the option to round the edges of the louver using the die radius.  
    
    If this is false, then the value 
    of :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.DieRadius` is not used.
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeRounding`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeRounding`` 
    
    :param includeRounding: 
    :type includeRounding: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MinimumToolClearance: NXOpen.Expression = ...
    """
    Returns 
    the minimum tool clearance expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumToolClearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the section used by the louver.  
    
    The section should be open.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SectionSide: LouverBuilderSectionSideOptions = ...
    """
    Returns or sets  the side of the section on which the louver is created and width is measure.  
    
    <hr>
    
    Getter Method
    
    Signature ``SectionSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.LouverBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the internal sketch used by the louver's section.  
    
    If the sketch is created internally as part of the louver command in the UI, then it 
    is consumed by the louver and does not show up as a separate feature in the part navigator.
    By setting the sketch object here, you will be making it internal to the louver feature. 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width of the louver.  
    
    The side of the section that the width is measured from depends on the 
    value of the section side (see :py:meth:`NXOpen.Features.SheetMetal.LouverBuilder.SectionSide`). 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns:  The width of the louver  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: LouverBuilder = ...  # unknown typename


class SheetmetalManagerFlangeWidthOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalManagerFlangeWidthOption():
    """
    Flange width option
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "CustomizeWidth", "customize width"
       "FullWidth", "full width"
       "Centred", "centred"
       "AtEnd", "at end"
       "FromBothEnds", "from both ends"
       "FromEnd", "from end"
    """
    CustomizeWidth = -1  # SheetmetalManagerFlangeWidthOptionMemberType
    FullWidth = 0  # SheetmetalManagerFlangeWidthOptionMemberType
    Centred = 1  # SheetmetalManagerFlangeWidthOptionMemberType
    AtEnd = 2  # SheetmetalManagerFlangeWidthOptionMemberType
    FromBothEnds = 3  # SheetmetalManagerFlangeWidthOptionMemberType
    FromEnd = 4  # SheetmetalManagerFlangeWidthOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilderWidthOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeTransitionBuilderWidthOptions():
    """
    Enum representing width option types for Bridge Transition feature. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Finite", "Bridge Transition starts at specified point on start edge and extends on one side by the specified distance."
       "Symmetric", "Bridge Transition starts at specified point on start edge and extends on either side by half the specified distance."
       "FullStartEdge", "Bridge Transition spans the full length of start edge."
       "FullEndEdge", "Bridge Transition spans the full length of end edge."
       "FullBothEdges", "Bridge Transition spans the full length of both the edges."
    """
    Finite = 0  # BridgeTransitionBuilderWidthOptionsMemberType
    Symmetric = 1  # BridgeTransitionBuilderWidthOptionsMemberType
    FullStartEdge = 2  # BridgeTransitionBuilderWidthOptionsMemberType
    FullEndEdge = 3  # BridgeTransitionBuilderWidthOptionsMemberType
    FullBothEdges = 4  # BridgeTransitionBuilderWidthOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilderTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeTransitionBuilderTypeOptions():
    """
    Enum representing types for Bridge Transition feature.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Zu", "Bridge Transition type consisting of Bend-Planar-Bend regions."
       "Fold", "Bridge Transition type consisting of Planar-Bend-Planar regions."
    """
    Zu = 0  # BridgeTransitionBuilderTypeOptionsMemberType
    Fold = 1  # BridgeTransitionBuilderTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilderWidthDirectionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeTransitionBuilderWidthDirectionOptions():
    """
    Enum representing the width direction for the Bridge Transition. 
    This enum applies only when the width type is :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthOptions.Finite <Features.SheetMetal.BridgeTransitionBuilderWidthOptions>`. 
    The :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions.Right <Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions>` option indicates that 
    the width is in the counter clockwise direction of flow of the start edge in the 
    non-thickness face adjacent to it. The :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions.Left <Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions>` 
    option indicates the width is in the opposite direction.        
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "It means Bridge Transition width direction at point specified and fin direction are in opposite direction."
       "Right", "It means Bridge Transition width direction at point specified and fin direction are in same direction."
    """
    Left = 0  # BridgeTransitionBuilderWidthDirectionOptionsMemberType
    Right = 1  # BridgeTransitionBuilderWidthDirectionOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilderInsetOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeTransitionBuilderInsetOptions():
    """
    Enum representing the side of the Bridge Transition material with respect to 
    the specified tangent plane. If it is :py:class:`Features.SheetMetal.BridgeTransitionBuilderInsetOptions.MaterialInside <Features.SheetMetal.BridgeTransitionBuilderInsetOptions>` 
    then the transtion and start edge flow will be on the same logical side 
    of the plane. If they are on opposite sides then use :py:class:`Features.SheetMetal.BridgeTransitionBuilderInsetOptions.MaterialOutside <Features.SheetMetal.BridgeTransitionBuilderInsetOptions>`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", "Bridge Transition body near tangential plane and start will be on same side of the tangential plane selected."
       "MaterialOutside", "Bridge Transition body near tangential plane and start will be on opposite sides of the tangential plane selected."
    """
    MaterialInside = 0  # BridgeTransitionBuilderInsetOptionsMemberType
    MaterialOutside = 1  # BridgeTransitionBuilderInsetOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilderFoldTransitionTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BridgeTransitionBuilderFoldTransitionTypeOptions():
    """
    Enum representing the type of :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>`. 
    :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>` can be defined by Length or Bend.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Length", "Fold Transition type is Length."
       "Bend", "Fold Transition type is Bend."
    """
    Length = 0  # BridgeTransitionBuilderFoldTransitionTypeOptionsMemberType
    Bend = 1  # BridgeTransitionBuilderFoldTransitionTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BridgeTransitionBuilder(SheetmetalBaseBuilder):
    """
    Represents a Bridge Transition builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBridgeTransitionBuilder`
    
    .. versionadded:: NX5.0.2
    """
    
    class WidthOptions():
        """
        Enum representing width option types for Bridge Transition feature. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Finite", "Bridge Transition starts at specified point on start edge and extends on one side by the specified distance."
           "Symmetric", "Bridge Transition starts at specified point on start edge and extends on either side by half the specified distance."
           "FullStartEdge", "Bridge Transition spans the full length of start edge."
           "FullEndEdge", "Bridge Transition spans the full length of end edge."
           "FullBothEdges", "Bridge Transition spans the full length of both the edges."
        """
        Finite = 0  # BridgeTransitionBuilderWidthOptionsMemberType
        Symmetric = 1  # BridgeTransitionBuilderWidthOptionsMemberType
        FullStartEdge = 2  # BridgeTransitionBuilderWidthOptionsMemberType
        FullEndEdge = 3  # BridgeTransitionBuilderWidthOptionsMemberType
        FullBothEdges = 4  # BridgeTransitionBuilderWidthOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TypeOptions():
        """
        Enum representing types for Bridge Transition feature.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Zu", "Bridge Transition type consisting of Bend-Planar-Bend regions."
           "Fold", "Bridge Transition type consisting of Planar-Bend-Planar regions."
        """
        Zu = 0  # BridgeTransitionBuilderTypeOptionsMemberType
        Fold = 1  # BridgeTransitionBuilderTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class WidthDirectionOptions():
        """
        Enum representing the width direction for the Bridge Transition. 
        This enum applies only when the width type is :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthOptions.Finite <Features.SheetMetal.BridgeTransitionBuilderWidthOptions>`. 
        The :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions.Right <Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions>` option indicates that 
        the width is in the counter clockwise direction of flow of the start edge in the 
        non-thickness face adjacent to it. The :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions.Left <Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions>` 
        option indicates the width is in the opposite direction.        
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "It means Bridge Transition width direction at point specified and fin direction are in opposite direction."
           "Right", "It means Bridge Transition width direction at point specified and fin direction are in same direction."
        """
        Left = 0  # BridgeTransitionBuilderWidthDirectionOptionsMemberType
        Right = 1  # BridgeTransitionBuilderWidthDirectionOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class InsetOptions():
        """
        Enum representing the side of the Bridge Transition material with respect to 
        the specified tangent plane. If it is :py:class:`Features.SheetMetal.BridgeTransitionBuilderInsetOptions.MaterialInside <Features.SheetMetal.BridgeTransitionBuilderInsetOptions>` 
        then the transtion and start edge flow will be on the same logical side 
        of the plane. If they are on opposite sides then use :py:class:`Features.SheetMetal.BridgeTransitionBuilderInsetOptions.MaterialOutside <Features.SheetMetal.BridgeTransitionBuilderInsetOptions>`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", "Bridge Transition body near tangential plane and start will be on same side of the tangential plane selected."
           "MaterialOutside", "Bridge Transition body near tangential plane and start will be on opposite sides of the tangential plane selected."
        """
        MaterialInside = 0  # BridgeTransitionBuilderInsetOptionsMemberType
        MaterialOutside = 1  # BridgeTransitionBuilderInsetOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FoldTransitionTypeOptions():
        """
        Enum representing the type of :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>`. 
        :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>` can be defined by Length or Bend.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Length", "Fold Transition type is Length."
           "Bend", "Fold Transition type is Bend."
        """
        Length = 0  # BridgeTransitionBuilderFoldTransitionTypeOptionsMemberType
        Bend = 1  # BridgeTransitionBuilderFoldTransitionTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AlternateSolution: bool = ...
    """
    Returns or sets  the option to get an alternate solution for the :py:class:`Features.SheetMetal.BridgeTransitionBuilderFoldTransitionTypeOptions.Bend <Features.SheetMetal.BridgeTransitionBuilderFoldTransitionTypeOptions>`
    when the width option is finite or symmetric.  
    
    If there is only one working solution possible then this method will not do anything. 
    
    <hr>
    
    Getter Method
    
    Signature ``AlternateSolution`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``AlternateSolution`` 
    
    :param isAlternateSolution: 
    :type isAlternateSolution: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    EndEdge: NXOpen.SelectEdge = ...
    """
    Returns  the end edge 
    
    <hr>
    
    Getter Method
    
    Signature ``EndEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    EndRadius: NXOpen.Expression = ...
    """
    Returns  the inner bend radius of bend region near end edge.  
    
    End radius required to be specified for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Zu <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>`. 
    
    <hr>
    
    Getter Method
    
    Signature ``EndRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.2
    
    .. deprecated::  NX10.0.2
       Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.BendRadius` instead.
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    FoldBendOptions: BendOptions = ...
    """
    Returns  the bend options for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>` bridge bend
    
    The bend options object stores additional parameters for the bend, such as bend radius, neutral factor, bend 
    relief width and depth.
    
    <hr>
    
    Getter Method
    
    Signature ``FoldBendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    FoldTransitionType: int = ...
    """
    Returns or sets  the option to get fold transition type.  
    
    <hr>
    
    Getter Method
    
    Signature ``FoldTransitionType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``FoldTransitionType`` 
    
    :param foldTransitionType: 
    :type foldTransitionType: int 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    InsetType: BridgeTransitionBuilderInsetOptions = ...
    """
    Returns or sets  the inset type
    
    <hr>
    
    Getter Method
    
    Signature ``InsetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderInsetOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``InsetType`` 
    
    :param insetType: 
    :type insetType: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderInsetOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length of the planar region near start edge.  
    
    Length is required to be specified for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Fold <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Plane: NXOpen.SelectISurface = ...
    """
    Returns  the tangential plane
    
    Only use this option to edit feature created prior to NX12. 
    Use :py:meth:`NXOpen.Features.SheetMetal.BridgeTransitionBuilder.ReferenceGeometryPlane`` to locate tangential plane.
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectISurface` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the point with respect to which the finite or symmetric width is specified.  
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    ReferenceGeometryPlane: NXOpen.Plane = ...
    """
    Returns or sets  the reference geometry plane 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceGeometryPlane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceGeometryPlane`` 
    
    :param refGeometryPlane: 
    :type refGeometryPlane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    StartAndEndParametersEqual: bool = ...
    """
    Returns or sets  the option to find whether the start and end parameters are equal.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartAndEndParametersEqual`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``StartAndEndParametersEqual`` 
    
    :param areBendParametersEqual: 
    :type areBendParametersEqual: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    StartEdge: NXOpen.SelectEdge = ...
    """
    Returns  the start edge 
    
    <hr>
    
    Getter Method
    
    Signature ``StartEdge`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectEdge` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    StartRadius: NXOpen.Expression = ...
    """
    Returns  the inner bend radius of the bend region near start edge.  
    
    Start radius required to be specified for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Zu <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``StartRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.2
    
    .. deprecated::  NX10.0.2
       Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.BendOptions.BendRadius` instead.
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    TrimOrExtendToBend: bool = ...
    """
    Returns or sets  the option to trim or extend faces to bend face.  
    
    <hr>
    
    Getter Method
    
    Signature ``TrimOrExtendToBend`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``TrimOrExtendToBend`` 
    
    :param trimOrExtend: 
    :type trimOrExtend: bool 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Type: BridgeTransitionBuilderTypeOptions = ...
    """
    Returns or sets  the transition type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderTypeOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderTypeOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    WidthDirection: BridgeTransitionBuilderWidthDirectionOptions = ...
    """
    Returns or sets  the width direction.  
    
    Only applies if the width type is :py:class:`Features.SheetMetal.BridgeTransitionBuilderWidthOptions.Finite <Features.SheetMetal.BridgeTransitionBuilderWidthOptions>` 
    
    <hr>
    
    Getter Method
    
    Signature ``WidthDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``WidthDirection`` 
    
    :param widthDirection: 
    :type widthDirection: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderWidthDirectionOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    WidthType: BridgeTransitionBuilderWidthOptions = ...
    """
    Returns or sets  the width type
    
    <hr>
    
    Getter Method
    
    Signature ``WidthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderWidthOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``WidthType`` 
    
    :param widthType: 
    :type widthType: :py:class:`NXOpen.Features.SheetMetal.BridgeTransitionBuilderWidthOptions` 
    
    .. versionadded:: NX5.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    ZuEndEdgeBendOptions: BendOptions = ...
    """
    Returns  the bend options at end edge for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Zu <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>` bridge bend.  
    
    The bend options object stores additional parameters for the bend, such as bend radius and neutral factor.
    
    <hr>
    
    Getter Method
    
    Signature ``ZuEndEdgeBendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    ZuStartEdgeBendOptions: BendOptions = ...
    """
    Returns  the bend options at start edge for :py:class:`Features.SheetMetal.BridgeTransitionBuilderTypeOptions.Zu <Features.SheetMetal.BridgeTransitionBuilderTypeOptions>` bridge bend.  
    
    The bend options object stores additional parameters for the bend, such as bend radius and neutral factor.
    
    <hr>
    
    Getter Method
    
    Signature ``ZuStartEdgeBendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX10.0.2
    
    License requirements: nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal")
    """
    Null: BridgeTransitionBuilder = ...  # unknown typename


class SMBoundaryConditionBuilderConstraintTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SMBoundaryConditionBuilderConstraintTypes():
    """
    Types of Boundary condition constraints 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "PointToPoint", " - "
       "PointAlongCurve", " - "
       "CurveToCurve", " - "
       "CurveAlongCurve", " - "
    """
    PointToPoint = 0  # SMBoundaryConditionBuilderConstraintTypesMemberType
    PointAlongCurve = 1  # SMBoundaryConditionBuilderConstraintTypesMemberType
    CurveToCurve = 2  # SMBoundaryConditionBuilderConstraintTypesMemberType
    CurveAlongCurve = 3  # SMBoundaryConditionBuilderConstraintTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SMBoundaryConditionBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Represents a Boundary condition object for Metaform.  
    
    A Metaform feature can have one or more boundary
    conditions and each condition determines how the mapped geometry will be locked. 
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.MetaformBuilder.CreateSMBoundaryCondition`
    
    .. versionadded:: NX7.5.0
    """
    
    class ConstraintTypes():
        """
        Types of Boundary condition constraints 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "PointToPoint", " - "
           "PointAlongCurve", " - "
           "CurveToCurve", " - "
           "CurveAlongCurve", " - "
        """
        PointToPoint = 0  # SMBoundaryConditionBuilderConstraintTypesMemberType
        PointAlongCurve = 1  # SMBoundaryConditionBuilderConstraintTypesMemberType
        CurveToCurve = 2  # SMBoundaryConditionBuilderConstraintTypesMemberType
        CurveAlongCurve = 3  # SMBoundaryConditionBuilderConstraintTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    ConstraintName: str = ...
    """
    Returns or sets  the constraint name.  
    
    If a constraint is added interactively, an automatic name will be generated for the
    users which can be edited. Each of the constraint name must be unique. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintName`` 
    
    :param constraintName: 
    :type constraintName: str 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    ConstraintType: SMBoundaryConditionBuilderConstraintTypes = ...
    """
    Returns or sets  the constraint type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstraintType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConstraintType`` 
    
    :param constraintType: 
    :type constraintType: :py:class:`NXOpen.Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    EndRegionCurve: NXOpen.ScCollector = ...
    """
    Returns  the end region curve This input is required if the Constraint Type is NOT :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.PointToPoint <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndRegionCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    EndRegionPoint: NXOpen.Point = ...
    """
    Returns or sets  the end region point This input is required only if the Constraint Type is :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.PointToPoint <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndRegionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndRegionPoint`` 
    
    :param endRegionPoint: 
    :type endRegionPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    StartRegionCurve: NXOpen.ScCollector = ...
    """
    Returns  the start region curve This input is required only if the Constraint Type is :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.CurveToCurve <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>` or 
    :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.CurveAlongCurve <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartRegionCurve`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    StartRegionPoint: NXOpen.Point = ...
    """
    Returns or sets  the start region point.  
    
    This input is required only if the Constraint Type is :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.PointToPoint <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>` or 
    :py:class:`Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes.PointAlongCurve <Features.SheetMetal.SMBoundaryConditionBuilderConstraintTypes>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartRegionPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartRegionPoint`` 
    
    :param startRegionPoint: 
    :type startRegionPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: SMBoundaryConditionBuilder = ...  # unknown typename


class HemFlangeBuilderInsetTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HemFlangeBuilderInsetTypeOptions():
    """
    This enum represents the inset type for the material of the hem flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", "The hem flange is flush with the thickness face on the inside"
       "MaterialOutside", "The hem flange is flush with the thickness face on the outside"
       "BendOutside", "The bend and hem flange are outside the thickness face"
    """
    MaterialInside = 0  # HemFlangeBuilderInsetTypeOptionsMemberType
    MaterialOutside = 1  # HemFlangeBuilderInsetTypeOptionsMemberType
    BendOutside = 2  # HemFlangeBuilderInsetTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HemFlangeBuilderBendReliefOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HemFlangeBuilderBendReliefOptions():
    """
    This enum represents the Bend relief type of the hem flange. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Square", " - "
       "Round", " - "
       "NotSet", " - "
    """
    Square = 0  # HemFlangeBuilderBendReliefOptionsMemberType
    Round = 1  # HemFlangeBuilderBendReliefOptionsMemberType
    NotSet = 2  # HemFlangeBuilderBendReliefOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HemFlangeBuilderTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HemFlangeBuilderTypeOptions():
    """
    Represents the Hem Flange type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ClosedHemType", " - "
       "OpenHemType", " - "
       "SFlangeHemType", " - "
       "CurlHemType", " - "
       "OpenLoopHemType", " - "
       "ClosedLoopHemType", " - "
       "CenteredLoopHemType", " - "
    """
    ClosedHemType = 0  # HemFlangeBuilderTypeOptionsMemberType
    OpenHemType = 1  # HemFlangeBuilderTypeOptionsMemberType
    SFlangeHemType = 2  # HemFlangeBuilderTypeOptionsMemberType
    CurlHemType = 3  # HemFlangeBuilderTypeOptionsMemberType
    OpenLoopHemType = 4  # HemFlangeBuilderTypeOptionsMemberType
    ClosedLoopHemType = 5  # HemFlangeBuilderTypeOptionsMemberType
    CenteredLoopHemType = 6  # HemFlangeBuilderTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HemFlangeBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`NXOpen.Features.HemFlange` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateHemFlangeFeatureBuilder`
    
    .. versionadded:: NX5.0.0
    """
    
    class InsetTypeOptions():
        """
        This enum represents the inset type for the material of the hem flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", "The hem flange is flush with the thickness face on the inside"
           "MaterialOutside", "The hem flange is flush with the thickness face on the outside"
           "BendOutside", "The bend and hem flange are outside the thickness face"
        """
        MaterialInside = 0  # HemFlangeBuilderInsetTypeOptionsMemberType
        MaterialOutside = 1  # HemFlangeBuilderInsetTypeOptionsMemberType
        BendOutside = 2  # HemFlangeBuilderInsetTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendReliefOptions():
        """
        This enum represents the Bend relief type of the hem flange. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Square", " - "
           "Round", " - "
           "NotSet", " - "
        """
        Square = 0  # HemFlangeBuilderBendReliefOptionsMemberType
        Round = 1  # HemFlangeBuilderBendReliefOptionsMemberType
        NotSet = 2  # HemFlangeBuilderBendReliefOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TypeOptions():
        """
        Represents the Hem Flange type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ClosedHemType", " - "
           "OpenHemType", " - "
           "SFlangeHemType", " - "
           "CurlHemType", " - "
           "OpenLoopHemType", " - "
           "ClosedLoopHemType", " - "
           "CenteredLoopHemType", " - "
        """
        ClosedHemType = 0  # HemFlangeBuilderTypeOptionsMemberType
        OpenHemType = 1  # HemFlangeBuilderTypeOptionsMemberType
        SFlangeHemType = 2  # HemFlangeBuilderTypeOptionsMemberType
        CurlHemType = 3  # HemFlangeBuilderTypeOptionsMemberType
        OpenLoopHemType = 4  # HemFlangeBuilderTypeOptionsMemberType
        ClosedLoopHemType = 5  # HemFlangeBuilderTypeOptionsMemberType
        CenteredLoopHemType = 6  # HemFlangeBuilderTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    BendReliefDepth: NXOpen.Expression = ...
    """
    Returns  the bend relief depth 
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BendReliefType: HemFlangeBuilderBendReliefOptions = ...
    """
    Returns or sets  the bend relief type 
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderBendReliefOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``BendReliefType`` 
    
    :param bendReliefType: 
    :type bendReliefType: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderBendReliefOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BendReliefWidth: NXOpen.Expression = ...
    """
    Returns  the bend relief width 
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    EdgeChain: NXOpen.ScCollector = ...
    """
    Returns  the edge chain 
    
    <hr>
    
    Getter Method
    
    Signature ``EdgeChain`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    FirstBendRadius: NXOpen.Expression = ...
    """
    Returns  the first bend radius 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstBendRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    FirstFlangeLength: NXOpen.Expression = ...
    """
    Returns  the first flange length 
    
    <hr>
    
    Getter Method
    
    Signature ``FirstFlangeLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    InsetType: HemFlangeBuilderInsetTypeOptions = ...
    """
    Returns or sets  the inset type options 
    
    <hr>
    
    Getter Method
    
    Signature ``InsetType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderInsetTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``InsetType`` 
    
    :param insetType: 
    :type insetType: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderInsetTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MiterAngle: NXOpen.Expression = ...
    """
    Returns  the miter angle 
    
    <hr>
    
    Getter Method
    
    Signature ``MiterAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    NeutralFactor: NXOpen.Expression = ...
    """
    Returns  the neutral factor 
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SecondBendRadius: NXOpen.Expression = ...
    """
    Returns  the second bend radius 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondBendRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SecondFlangeLength: NXOpen.Expression = ...
    """
    Returns  the second flange length 
    
    <hr>
    
    Getter Method
    
    Signature ``SecondFlangeLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SweepAngle: NXOpen.Expression = ...
    """
    Returns  the sweep 
    
    <hr>
    
    Getter Method
    
    Signature ``SweepAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Type: HemFlangeBuilderTypeOptions = ...
    """
    Returns or sets  the hem type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.HemFlangeBuilderTypeOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    UseMiter: bool = ...
    """
    Returns or sets  the use miter hem 
    
    <hr>
    
    Getter Method
    
    Signature ``UseMiter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``UseMiter`` 
    
    :param useMiterHem: 
    :type useMiterHem: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: HemFlangeBuilder = ...  # unknown typename


class AeroUnformBuilder(SheetmetalBaseBuilder):
    """
    Represents a Aerospace Sheet Metal UNFORM Builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateUnformBuilder`
    
    .. versionadded:: NX4.0.0
    """
    BaseFace: NXOpen.Face = ...
    """
    Returns or sets  the Base Face for the UNFORM.  
    
    <hr>
    
    Getter Method
    
    Signature ``BaseFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``BaseFace`` 
    
    :param baseFace: 
    :type baseFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    FormFaces: NXOpen.ScCollector = ...
    """
    Returns or sets  the formed faces smart collector object
    
    <hr>
    
    Getter Method
    
    Signature ``FormFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``FormFaces`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AeroUnformBuilder = ...  # unknown typename


class MultiFlangeBuilderMatchFaceOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MultiFlangeBuilderMatchFaceOptions():
    """
    This enum defines the mathc face options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "UntilSelected", " - "
    """
    NotSet = 0  # MultiFlangeBuilderMatchFaceOptionsMemberType
    UntilSelected = 1  # MultiFlangeBuilderMatchFaceOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MultiFlangeBuilder(SheetmetalBaseBuilder):
    """
    Represents a :py:class:`Features.SheetMetal.MultiFlange` builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateMultiFlangeBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    class MatchFaceOptions():
        """
        This enum defines the mathc face options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "UntilSelected", " - "
        """
        NotSet = 0  # MultiFlangeBuilderMatchFaceOptionsMemberType
        UntilSelected = 1  # MultiFlangeBuilderMatchFaceOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    FlangePropertiesList: FeatureBendPropertiesListBuilder = ...
    """
    Returns  the flange properties list 
    
    <hr>
    
    Getter Method
    
    Signature ``FlangePropertiesList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesListBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    MatchFace: MultiFlangeBuilderMatchFaceOptions = ...
    """
    Returns or sets  the match face 
    
    <hr>
    
    Getter Method
    
    Signature ``MatchFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MultiFlangeBuilderMatchFaceOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MatchFace`` 
    
    :param matchFace: 
    :type matchFace: :py:class:`NXOpen.Features.SheetMetal.MultiFlangeBuilderMatchFaceOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Null: MultiFlangeBuilder = ...  # unknown typename


class CornerTreatmentBuilderCornerTreatmentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CornerTreatmentBuilderCornerTreatmentType():
    """
    Corner Treatment Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Chamfer", " - "
       "Radius", " - "
    """
    NotSet = 0  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
    Chamfer = 1  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
    Radius = 2  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CornerTreatmentBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The CornerTreatmentBuilder class is used to manage a builder object for
    a corner treatment in the flat solid and flat pattern dialogs.  
    
    It includes
    properties and an enumeration type for a flag that indicates whether the
    global (flat pattern preferences) value is to be used, an enumeration type
    that indicates what type of corner treatment to apply, and an expression
    to indicate the value associated with treatment types chamfer and radius.
    
    .. versionadded:: NX6.0.0
    """
    
    class CornerTreatmentType():
        """
        Corner Treatment Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Chamfer", " - "
           "Radius", " - "
        """
        NotSet = 0  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
        Chamfer = 1  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
        Radius = 2  # CornerTreatmentBuilderCornerTreatmentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    TreatmentType: CornerTreatmentBuilderCornerTreatmentType = ...
    """
    Returns or sets  the treatment type option menu value 
    
    <hr>
    
    Getter Method
    
    Signature ``TreatmentType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilderCornerTreatmentType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TreatmentType`` 
    
    :param treatmentType: 
    :type treatmentType: :py:class:`NXOpen.Features.SheetMetal.CornerTreatmentBuilderCornerTreatmentType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    UseGlobal: bool = ...
    """
    Returns or sets  the use global toggle value 
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobal`` 
    
    :param useGlobal: 
    :type useGlobal: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Value: NXOpen.Expression = ...
    """
    Returns  the value associated with the chamfer and radius treatment types 
    
    <hr>
    
    Getter Method
    
    Signature ``Value`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: CornerTreatmentBuilder = ...  # unknown typename


class CleanUpUtilityBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Clean-Up Utility builder builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateCleanUpUtilityBuilder`
    
    Default values.
    
    =====================  ======================================
    Property               Value
    =====================  ======================================
    SliverTol              0.009 
    ---------------------  --------------------------------------
    ThicknessValue.Value   0 (millimeters part), 0 (inches part) 
    ---------------------  --------------------------------------
    UseGlobal              1 
    =====================  ======================================
    
    .. versionadded:: NX7.5.0
    """
    HideOriginal: bool = ...
    """
    Returns or sets  the hide original 
    
    <hr>
    
    Getter Method
    
    Signature ``HideOriginal`` 
    
    :returns:  The option to hide original value 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HideOriginal`` 
    
    :param hideOriginal:  The option to hide original value 
    :type hideOriginal: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    InferThickness: bool = ...
    """
    Returns or sets  the infer thickness 
    
    <hr>
    
    Getter Method
    
    Signature ``InferThickness`` 
    
    :returns:  The option to infer thickness value 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InferThickness`` 
    
    :param inferThickness:  The option to infer thickness value 
    :type inferThickness: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SelectBaseFace: NXOpen.ScCollector = ...
    """
    Returns  the select base face for clean-up utility 
    
    <hr>
    
    Getter Method
    
    Signature ``SelectBaseFace`` 
    
    :returns:  This face will specify top layer in processing the body.  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    SliverTol: float = ...
    """
    Returns or sets  the sliver tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``SliverTol`` 
    
    :returns:  The sliver tolerance value 
    :rtype: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SliverTol`` 
    
    :param sliverTol:  The sliver tolerance value 
    :type sliverTol: float 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    ThicknessValue: NXOpen.Expression = ...
    """
    Returns  the thickness value 
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessValue`` 
    
    :returns:  The thickness value 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    """
    UseGlobal: bool = ...
    """
    Returns or sets  the use global, if it equals to true - use global thickness value 
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobal`` 
    
    :returns:  The option for global value 
    :rtype: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobal`` 
    
    :param useGlobal:  The option for global value 
    :type useGlobal: bool 
    
    .. versionadded:: NX7.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: CleanUpUtilityBuilder = ...  # unknown typename


class SheetmetalFaceLayerMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalFaceLayer():
    """
    Face Layer 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", " - "
       "Top", " - "
       "Bottom", " - "
    """
    Unknown = 0  # SheetmetalFaceLayerMemberType
    Top = 1  # SheetmetalFaceLayerMemberType
    Bottom = 2  # SheetmetalFaceLayerMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Joggle(NXOpen.Features.Feature):
    """
    Represents a joggle feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Features.SheetMetal.JoggleBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Null: Joggle = ...  # unknown typename


class LighteningCutoutBuilderCutoutTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LighteningCutoutBuilderCutoutType():
    """
    Represents the type of Lightening Cutout 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Hole", " - "
       "UserDefined", " - "
    """
    Hole = 0  # LighteningCutoutBuilderCutoutTypeMemberType
    UserDefined = 1  # LighteningCutoutBuilderCutoutTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LighteningCutoutBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a :py:class:`Features.SheetMetal.LighteningCutout` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateLighteningCutoutBuilder`
    
    Default values.
    
    =================================  ==========================================
    Property                           Value
    =================================  ==========================================
    Angle.Value                        45 
    ---------------------------------  ------------------------------------------
    CheckClearance                     1 
    ---------------------------------  ------------------------------------------
    Clearance.Value                    5 (millimeters part), 0.12 (inches part) 
    ---------------------------------  ------------------------------------------
    Diameter.Value                     102 (millimeters part), 2.6 (inches part) 
    ---------------------------------  ------------------------------------------
    DieRadius.Value                    8 (millimeters part), 0.2 (inches part) 
    ---------------------------------  ------------------------------------------
    Length.Value                       6 (millimeters part), 0.125 (inches part) 
    ---------------------------------  ------------------------------------------
    NeutralFactor.Value (deprecated)   0.33 
    ---------------------------------  ------------------------------------------
    SectionCornerRadius.Value          8 (millimeters part), 0.2 (inches part) 
    ---------------------------------  ------------------------------------------
    Type                               UserDefined 
    =================================  ==========================================
    
    .. versionadded:: NX11.0.0
    """
    
    class CutoutType():
        """
        Represents the type of Lightening Cutout 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Hole", " - "
           "UserDefined", " - "
        """
        Hole = 0  # LighteningCutoutBuilderCutoutTypeMemberType
        UserDefined = 1  # LighteningCutoutBuilderCutoutTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetStandards(self) -> 'list[str]':
        """
        Returns the standard names available for the material selected  
        
        Signature ``GetStandards()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options 
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    CheckClearance: bool = ...
    """
    Returns or sets  whether to check the clearance 
    
    <hr>
    
    Getter Method
    
    Signature ``CheckClearance`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckClearance`` 
    
    :param checkClearance: 
    :type checkClearance: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Clearance: NXOpen.Expression = ...
    """
    Returns  the clearance 
    
    <hr>
    
    Getter Method
    
    Signature ``Clearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the diameter when the type is :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType.Hole <NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    DieRadius: NXOpen.Expression = ...
    """
    Returns  the die radius 
    
    <hr>
    
    Getter Method
    
    Signature ``DieRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    HoleCenter: NXOpen.Section = ...
    """
    Returns  the hole center when the type is :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType.Hole <NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``HoleCenter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    NeutralFactor: NXOpen.Expression = ...
    """
    Returns  the neutral factor 
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX12.0.0
       Obtain the bend options object using :py:meth:`NXOpen.Features.SheetMetal.LighteningCutoutBuilder.BendOptions` and from bend options, get Neutral Factor using :py:meth:`NXOpen.Features.SheetMetal.BendOptions.NeutralFactor`
    
    License requirements: None.
    """
    ReverseBendDirection: bool = ...
    """
    Returns or sets  whether the bend direction is reversed 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseBendDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseBendDirection`` 
    
    :param reverseBendDirection: 
    :type reverseBendDirection: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    SectionCornerRadius: NXOpen.Expression = ...
    """
    Returns  the section corner radius 
    
    <hr>
    
    Getter Method
    
    Signature ``SectionCornerRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns  the Sketch used by Lightening Cutout 
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    StandardName: str = ...
    """
    Returns or sets  the standard name selected 
    
    <hr>
    
    Getter Method
    
    Signature ``StandardName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StandardName`` 
    
    :param standardName: 
    :type standardName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Type: LighteningCutoutBuilderCutoutType = ...
    """
    Returns or sets  the type 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    UserDefinedSection: NXOpen.Section = ...
    """
    Returns  the section when the type is :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType.UserDefined <NXOpen.Features.SheetMetal.LighteningCutoutBuilderCutoutType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Null: LighteningCutoutBuilder = ...  # unknown typename


class SheetmetalFaceTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalFaceType():
    """
    Face Type 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", " - "
       "Web", " - "
       "Bend", " - "
       "Deform", " - "
       "Thickness", " - "
    """
    Unknown = 0  # SheetmetalFaceTypeMemberType
    Web = 1  # SheetmetalFaceTypeMemberType
    Bend = 2  # SheetmetalFaceTypeMemberType
    Deform = 3  # SheetmetalFaceTypeMemberType
    Thickness = 4  # SheetmetalFaceTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HoleTreatmentBuilderTreatmentTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HoleTreatmentBuilderTreatmentType():
    """
    Hole Treatment Type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Centermark", " - "
    """
    NotSet = 0  # HoleTreatmentBuilderTreatmentTypeMemberType
    Centermark = 1  # HoleTreatmentBuilderTreatmentTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class HoleTreatmentBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    The HoleTreatmentBuilder class is used to manage a builder object for
    a hole treatment in the flat pattern dialogs.  
    
    It includes
    properties and an enumeration type for a flag that indicates whether the
    global (flat pattern preferences) value is to be used, an enumeration type
    that indicates what type of hole treatment to apply, and an expression
    to indicate the diameter value associated with treatment type.
    
    .. versionadded:: NX12.0.0
    """
    
    class TreatmentType():
        """
        Hole Treatment Type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Centermark", " - "
        """
        NotSet = 0  # HoleTreatmentBuilderTreatmentTypeMemberType
        Centermark = 1  # HoleTreatmentBuilderTreatmentTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    Diameter: NXOpen.Expression = ...
    """
    Returns  the hole diameter value associated with the treatment type 
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Treatment: HoleTreatmentBuilderTreatmentType = ...
    """
    Returns or sets  the treatment type option menu value 
    
    <hr>
    
    Getter Method
    
    Signature ``Treatment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.HoleTreatmentBuilderTreatmentType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Treatment`` 
    
    :param treatmentType: 
    :type treatmentType: :py:class:`NXOpen.Features.SheetMetal.HoleTreatmentBuilderTreatmentType` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    UseGlobal: bool = ...
    """
    Returns or sets  the use global toggle value 
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobal`` 
    
    :param useGlobal: 
    :type useGlobal: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: HoleTreatmentBuilder = ...  # unknown typename


class LighteningCutout(NXOpen.Features.BodyFeature):
    """
    Represents a lightening cutout feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Features.SheetMetal.LighteningCutoutBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Null: LighteningCutout = ...  # unknown typename


class AeroJoggleBuilderSideTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroJoggleBuilderSideType():
    """
    This enum defines the side of a twin joggle
    only side1 is used for a single joggle 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Side1", "Side 1 (only side of single)"
       "Side2", "Side 2"
    """
    Side1 = 0  # AeroJoggleBuilderSideTypeMemberType
    Side2 = 1  # AeroJoggleBuilderSideTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroJoggleBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Aerospace Sheet Metal Joggle Builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateJoggleBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class SideType():
        """
        This enum defines the side of a twin joggle
        only side1 is used for a single joggle 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Side1", "Side 1 (only side of single)"
           "Side2", "Side 2"
        """
        Side1 = 0  # AeroJoggleBuilderSideTypeMemberType
        Side2 = 1  # AeroJoggleBuilderSideTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetStartPlane(self, startPlane: NXOpen.Plane) -> None:
        """
        Set the start plane 
        
        Signature ``SetStartPlane(startPlane)`` 
        
        :param startPlane:  datum plane feature  
        :type startPlane: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetStartPlane(self) -> NXOpen.Plane:
        """
        The start plane 
        
        Signature ``GetStartPlane()`` 
        
        :returns:  datum plane feature  
        :rtype: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetEndPlane(self, endPlane: NXOpen.Plane) -> None:
        """
        Set the end plane 
        
        Signature ``SetEndPlane(endPlane)`` 
        
        :param endPlane:  datum plane feature  
        :type endPlane: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetEndPlane(self) -> NXOpen.Plane:
        """
        The end plane 
        
        Signature ``GetEndPlane()`` 
        
        :returns:  datum plane feature  
        :rtype: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetDepth(self, depthStr: str) -> None:
        """
        Set the depth expression.  
        
        Signature ``SetDepth(depthStr)`` 
        
        :param depthStr:  value of depth expression  
        :type depthStr: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetClearance(self, sideType: AeroJoggleBuilderSideType, clearanceStr: str) -> None:
        """
        Set the clearance expression.  
        
        Signature ``SetClearance(sideType, clearanceStr)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param clearanceStr:  value of clearance expression  
        :type clearanceStr: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetClearance(self, sideType: AeroJoggleBuilderSideType) -> NXOpen.Expression:
        """
        The clearance expression.  
        
        Signature ``GetClearance(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  clearance expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetRunout(self, sideType: AeroJoggleBuilderSideType, runoutStr: str) -> None:
        """
        Set the runout expression.  
        
        Signature ``SetRunout(sideType, runoutStr)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param runoutStr:  value of runout expression  
        :type runoutStr: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetRunout(self, sideType: AeroJoggleBuilderSideType) -> NXOpen.Expression:
        """
        The runout expression.  
        
        Signature ``GetRunout(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  runout expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetStationaryRadius(self, sideType: AeroJoggleBuilderSideType, radiusStr: str) -> None:
        """
        Set the stationary radius expression.  
        
        Signature ``SetStationaryRadius(sideType, radiusStr)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param radiusStr:  value of stationary radius expression  
        :type radiusStr: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetStationaryRadius(self, sideType: AeroJoggleBuilderSideType) -> NXOpen.Expression:
        """
        The stationary radius expression.  
        
        Signature ``GetStationaryRadius(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  stationary radius expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetOffsetRadius(self, sideType: AeroJoggleBuilderSideType, radiusStr: str) -> None:
        """
        Set the offset radius expression.  
        
        Signature ``SetOffsetRadius(sideType, radiusStr)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param radiusStr:  value of offset radius expression  
        :type radiusStr: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetOffsetRadius(self, sideType: AeroJoggleBuilderSideType) -> NXOpen.Expression:
        """
        The offset radius expression.  
        
        Signature ``GetOffsetRadius(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  offset radius expression  
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetStandardRunout(self, sideType: AeroJoggleBuilderSideType, standardRunout: bool) -> None:
        """
        Set the Global flag for runout
        
        Signature ``SetStandardRunout(sideType, standardRunout)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param standardRunout:  If true use standard runout  
        :type standardRunout: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetStandardRunout(self, sideType: AeroJoggleBuilderSideType) -> bool:
        """
        The global flag for runout
        
        Signature ``GetStandardRunout(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  If true use standard runout  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetGlobalStationaryRadius(self, sideType: AeroJoggleBuilderSideType, globalRadius: bool) -> None:
        """
        Set the Global flag for stationary radius
        
        Signature ``SetGlobalStationaryRadius(sideType, globalRadius)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param globalRadius:  If true use global radius  
        :type globalRadius: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetGlobalStationaryRadius(self, sideType: AeroJoggleBuilderSideType) -> bool:
        """
        The Global flag for stationary radius 
        
        Signature ``GetGlobalStationaryRadius(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  If true use global radius  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetGlobalOffsetRadius(self, sideType: AeroJoggleBuilderSideType, globalRadius: bool) -> None:
        """
        Set the Global flag for offset radius
        
        Signature ``SetGlobalOffsetRadius(sideType, globalRadius)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :param globalRadius:  If true use global radius  
        :type globalRadius: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetGlobalOffsetRadius(self, sideType: AeroJoggleBuilderSideType) -> bool:
        """
        The Global flag for offset radius
        
        Signature ``GetGlobalOffsetRadius(sideType)`` 
        
        :param sideType:  side1/side2  
        :type sideType: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilderSideType` 
        :returns:  If true use global radius  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    BendFaces: NXOpen.ScCollector = ...
    """
    Returns or sets  the flange 
    
    <hr>
    
    Getter Method
    
    Signature ``BendFaces`` 
    
    :returns:  bend faces  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``BendFaces`` 
    
    :param bendFaces:  bend faces  
    :type bendFaces: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Depth: NXOpen.Expression = ...
    """
    Returns  the depth expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns:  depth expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    FlipJoggleSide: bool = ...
    """
    Returns or sets  the joggle direction flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``FlipJoggleSide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``FlipJoggleSide`` 
    
    :param flipJoggleSide: 
    :type flipJoggleSide: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    IsSymmetric: bool = ...
    """
    Returns or sets  the symmetric flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsSymmetric`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``IsSymmetric`` 
    
    :param isSymmetric: 
    :type isSymmetric: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    IsTwin: bool = ...
    """
    Returns or sets  the is_twin flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``IsTwin`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``IsTwin`` 
    
    :param isTwin: 
    :type isTwin: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    JoggleCompensation: bool = ...
    """
    Returns or sets  the joggle compensation.  
    
    <hr>
    
    Getter Method
    
    Signature ``JoggleCompensation`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``JoggleCompensation`` 
    
    :param joggleComp:  If true use joggle compensation  
    :type joggleComp: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    JoggleIn: bool = ...
    """
    Returns or sets  the joggle in flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``JoggleIn`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``JoggleIn`` 
    
    :param joggleIn: 
    :type joggleIn: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AeroJoggleBuilder = ...  # unknown typename


class SheetmetalBendParameters():
    """
    This structure contains the bend parameters for a Sheet Metal bend area.  
    
    .
    Constructor: 
    NXOpen.Features.SheetMetal.SheetmetalBendParameters()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    InnerRadius: float = ...
    """
    Inner Bend Radius.  
    
    This works only for cylidrical bend faces. Other faces return 0.0 
    <hr>
    
    Field Value
    Type:float
    """
    NeutralFactor: float = ...
    """
    Neutral factor value.  
    
    If the flange is controlled by bend tables, then this is table value converted to neutral factor.
    <hr>
    
    Field Value
    Type:float
    """
    BendAngle: float = ...
    """
    Bend Angle
    <hr>
    
    Field Value
    Type:float
    """
    BendState: SheetmetalBendState = ...
    """
    Bend Face is flat or bent
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Features.SheetMetal.SheetmetalBendState`
    """


class LoftedFlangeBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LoftedFlangeBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the lofted flange creates thickness. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # LoftedFlangeBuilderSectionSideOptionsMemberType
    Right = 1  # LoftedFlangeBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LoftedFlangeBuilder(SheetmetalBaseBuilder):
    """
    Represents a Lofted Flange feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateLoftedFlangeFeatureBuilder`
    
    Default values.
    
    ======================  ========================================
    Property                Value
    ======================  ========================================
    IndexMarkLength.Value   5 (millimeters part), 0.5 (inches part) 
    ----------------------  ----------------------------------------
    NumberOfBendSegments    0 
    ----------------------  ----------------------------------------
    UseSegmentedBends       0 
    ======================  ========================================
    
    .. versionadded:: NX4.0.0
    """
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the lofted flange creates thickness. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # LoftedFlangeBuilderSectionSideOptionsMemberType
        Right = 1  # LoftedFlangeBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetThickness(self) -> NXOpen.Expression:
        """
        The thickness  of base lofted flange.  
        
        Applicable only for Base lofted flange. Ignored for a Secondary Lofted Flange. 
        
        Signature ``GetThickness()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def SetThickness(self, thickness: str) -> None:
        """
        The thickness  of base lofted flange.  
        
        Applicable only for Base lofted flange. Ignored for a Secondary Lofted Flange.
        
        Signature ``SetThickness(thickness)`` 
        
        :param thickness: 
        :type thickness: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.LoftedFlangeBuilder.GetThickness` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify user data validity.  
        
        If the data is valid, returned value should be 0.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    BendOptions: BendOptions = ...
    """
    Returns  the bend options object.  
    
    Get the bend options object which is created while creating builder. Then set values to parameters of
    bend options object(like bend radius, bend relief type etc.) using set methods of bend options object.
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndSection: NXOpen.Section = ...
    """
    Returns or sets  the end section of the lofted flange.  
    
    The section profile should be open looped.
    
    <hr>
    
    Getter Method
    
    Signature ``EndSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``EndSection`` 
    
    :param endSection: 
    :type endSection: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndSectionPoint: NXOpen.Point3d = ...
    """
    Returns or sets  the start/end point of the end section.  
    
    It can be start/end point of the section profile.
    
    <hr>
    
    Getter Method
    
    Signature ``EndSectionPoint`` 
    
    :returns:  point 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``EndSectionPoint`` 
    
    :param point:  point 
    :type point: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndSketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the end section sketch as slave.  
    
    Set the sketch which is used to create end section.
    This is only used when the section is created from sketch. If the section is created
    from edges or if the end sketch is not required to be slave, set the value as None .
    
    <hr>
    
    Getter Method
    
    Signature ``EndSketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``EndSketch`` 
    
    :param slaveEndSketch: 
    :type slaveEndSketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    IndexMarkLength: NXOpen.Expression = ...
    """
    Returns  the index mark length 
    Get the index mark length expression 
    If use segmented bends is set to true the only the index mark length value 
    is used for dividing the bend even though a value is set 
    Index mark length value only gets reflected in flat pattern view
    
    <hr>
    
    Getter Method
    
    Signature ``IndexMarkLength`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsSecondary: bool = ...
    """
    Returns or sets  the type of lofted flange feature - base lofted flange/secondary lofted flange.  
    
    Specify false for base lofted flanges and true for secondary lofted flanges.
    
    <hr>
    
    Getter Method
    
    Signature ``IsSecondary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``IsSecondary`` 
    
    :param isSecondary: 
    :type isSecondary: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    NumberOfBendSegments: int = ...
    """
    Returns or sets  the number of bend segments 
    Get and set the number of bend segments
    If use segmented bends is set to true then only the number of bend segments value is used for dividing the bend even though a value is set
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfBendSegments`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NumberOfBendSegments`` 
    
    :param numberOfBendSegments: 
    :type numberOfBendSegments: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    StartSection: NXOpen.Section = ...
    """
    Returns or sets  the start section of the lofted flange.  
    
    The section profile should be open looped.
    
    <hr>
    
    Getter Method
    
    Signature ``StartSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartSection`` 
    
    :param startSection: 
    :type startSection: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartSectionPoint: NXOpen.Point3d = ...
    """
    Returns or sets  the start/end point of the start section.  
    
    It can be start/end point of the section profile.
    
    <hr>
    
    Getter Method
    
    Signature ``StartSectionPoint`` 
    
    :returns:  point 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartSectionPoint`` 
    
    :param point:  point 
    :type point: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartSketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the start section sketch as slave.  
    
    Set the sketch which is used to create start section.
    This is only used when the section is created from sketch. If the section is created
    from edges or start sketch is not required to be slave, set slave sketch as None.
    
    <hr>
    
    Getter Method
    
    Signature ``StartSketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartSketch`` 
    
    :param slaveStartSketch: 
    :type slaveStartSketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ThicknessSide: LoftedFlangeBuilderSectionSideOptions = ...
    """
    Returns or sets  the thickness side of base lofted flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``ThicknessSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.LoftedFlangeBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ThicknessSide`` 
    
    :param thickSide: 
    :type thickSide: :py:class:`NXOpen.Features.SheetMetal.LoftedFlangeBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    UseSegmentedBends: bool = ...
    """
    Returns or sets   the use multi segment bends 
    Set use_segmented_bends to true or false and get the same 
    If use multi segment bends is set to true then lofted flange bend face is gets divided as per the number bend segments mentioned by the user
    
    <hr>
    
    Getter Method
    
    Signature ``UseSegmentedBends`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseSegmentedBends`` 
    
    :param useMultiSegmentBends: 
    :type useMultiSegmentBends: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: LoftedFlangeBuilder = ...  # unknown typename


class MiterOptionsPositionOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MiterOptionsPositionOptions():
    """
    the miter positions options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "no miter"
       "Start", "miter is done at the beginning"
       "End", "miter is done at the ending"
       "Both", "miter is done both at beginning and ending"
    """
    NotSet = 0  # MiterOptionsPositionOptionsMemberType
    Start = 1  # MiterOptionsPositionOptionsMemberType
    End = 2  # MiterOptionsPositionOptionsMemberType
    Both = 3  # MiterOptionsPositionOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MiterOptionsTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MiterOptionsTypeOptions():
    """
    the miter type options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NormalToSourceFace", "mitering is done along the normal to source face"
       "NormalToThicknessFace", "mitering is done along the normal to thickness face"
    """
    NormalToSourceFace = 0  # MiterOptionsTypeOptionsMemberType
    NormalToThicknessFace = 1  # MiterOptionsTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MiterOptionsClosedCornerTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MiterOptionsClosedCornerTypeOptions():
    """
    the closed corner type options.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Corner is not closed"
       "Open", "corner is open"
       "Closed", "corner is closed completely"
       "CircularCutout", "corner has a circular cutout in it"
       "UCutout", "corner has a U shaped cutout in it"
       "VCutout", "corner has a V shaped cutout in it"
    """
    NotSet = 0  # MiterOptionsClosedCornerTypeOptionsMemberType
    Open = 1  # MiterOptionsClosedCornerTypeOptionsMemberType
    Closed = 2  # MiterOptionsClosedCornerTypeOptionsMemberType
    CircularCutout = 3  # MiterOptionsClosedCornerTypeOptionsMemberType
    UCutout = 4  # MiterOptionsClosedCornerTypeOptionsMemberType
    VCutout = 5  # MiterOptionsClosedCornerTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MiterOptionsCornerTreatmentOriginTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MiterOptionsCornerTreatmentOriginTypeOptions():
    """
    This enum represents corner treatment cutout origin type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BendCenter", "The cutout origin will be at the intersection of first bend's centerline and bisector of corner angle."
       "CornerPoint", "The cutout origin will be at the corner point."
    """
    BendCenter = 0  # MiterOptionsCornerTreatmentOriginTypeOptionsMemberType
    CornerPoint = 1  # MiterOptionsCornerTreatmentOriginTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MiterOptions(NXOpen.TaggedObject):
    """
    Represents a Miter Data Options builder.  
    
    Mitre cut is essentially an end treatment to the contour flange feature,
    which shall prevent merging/interference with the existing or newly placed features in sheet metal.
    
    .. versionadded:: NX4.0.0
    """
    
    class PositionOptions():
        """
        the miter positions options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "no miter"
           "Start", "miter is done at the beginning"
           "End", "miter is done at the ending"
           "Both", "miter is done both at beginning and ending"
        """
        NotSet = 0  # MiterOptionsPositionOptionsMemberType
        Start = 1  # MiterOptionsPositionOptionsMemberType
        End = 2  # MiterOptionsPositionOptionsMemberType
        Both = 3  # MiterOptionsPositionOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TypeOptions():
        """
        the miter type options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NormalToSourceFace", "mitering is done along the normal to source face"
           "NormalToThicknessFace", "mitering is done along the normal to thickness face"
        """
        NormalToSourceFace = 0  # MiterOptionsTypeOptionsMemberType
        NormalToThicknessFace = 1  # MiterOptionsTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ClosedCornerTypeOptions():
        """
        the closed corner type options.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Corner is not closed"
           "Open", "corner is open"
           "Closed", "corner is closed completely"
           "CircularCutout", "corner has a circular cutout in it"
           "UCutout", "corner has a U shaped cutout in it"
           "VCutout", "corner has a V shaped cutout in it"
        """
        NotSet = 0  # MiterOptionsClosedCornerTypeOptionsMemberType
        Open = 1  # MiterOptionsClosedCornerTypeOptionsMemberType
        Closed = 2  # MiterOptionsClosedCornerTypeOptionsMemberType
        CircularCutout = 3  # MiterOptionsClosedCornerTypeOptionsMemberType
        UCutout = 4  # MiterOptionsClosedCornerTypeOptionsMemberType
        VCutout = 5  # MiterOptionsClosedCornerTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CornerTreatmentOriginTypeOptions():
        """
        This enum represents corner treatment cutout origin type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BendCenter", "The cutout origin will be at the intersection of first bend's centerline and bisector of corner angle."
           "CornerPoint", "The cutout origin will be at the corner point."
        """
        BendCenter = 0  # MiterOptionsCornerTreatmentOriginTypeOptionsMemberType
        CornerPoint = 1  # MiterOptionsCornerTreatmentOriginTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetStartValue(self) -> NXOpen.Expression:
        """
        THE miter start value expression.  
        
        Positive value adds material and negative v 
        
        Signature ``GetStartValue()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetStartValue(self, startValue: str) -> None:
        """
        Signature ``SetStartValue(startValue)`` 
        
        :param startValue: 
        :type startValue: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.MiterOptions.GetStartValue` instead.
        
        License requirements: None.
        """
        ...
    
    
    def GetEndValue(self) -> NXOpen.Expression:
        """
        THE miter end value expression.  
        
        Signature ``GetEndValue()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetEndValue(self, endValue: str) -> None:
        """
        Signature ``SetEndValue(endValue)`` 
        
        :param endValue: 
        :type endValue: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`Features.SheetMetal.MiterOptions.GetEndValue` instead.
        
        License requirements: None.
        """
        ...
    
    
    def GetClosedCornerDiameter(self) -> NXOpen.Expression:
        """
        The diameter expression of the closed corner.  
        
        Applicable only when :py:meth:`NXOpen.Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions`
        is :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.CircularCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
        :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.UCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
        :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`. 
        
        Signature ``GetClosedCornerDiameter()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Expression` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetClosedCornerDiameter(self, endValue: str) -> None:
        """
        Signature ``SetClosedCornerDiameter(endValue)`` 
        
        :param endValue: 
        :type endValue: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    BlendMiter: bool = ...
    """
    Returns or sets  the option that specifies whether to blend the sharp edges created by the miter 
    
    <hr>
    
    Getter Method
    
    Signature ``BlendMiter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BlendMiter`` 
    
    :param blendMiter: 
    :type blendMiter: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ClosedCornerGap: NXOpen.Expression = ...
    """
    Returns  the corner gap used for a contour flange corner in case of a closed corner condition.  
    
    This applies for all treatment types in :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions`
    
    <hr>
    
    Getter Method
    
    Signature ``ClosedCornerGap`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    ClosedCornerType: MiterOptionsClosedCornerTypeOptions = ...
    """
    Returns or sets  the closed corner option type.  
    
    <hr>
    
    Getter Method
    
    Signature ``ClosedCornerType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsClosedCornerTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ClosedCornerType`` 
    
    :param cutType: 
    :type cutType: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsClosedCornerTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    ClosedCornerVAngle1: NXOpen.Expression = ...
    """
    Returns  the v cutout angle1 expression of the closed corner.  
    
    Applicable only when :py:meth:`NXOpen.Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions`
    is :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``ClosedCornerVAngle1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ClosedCornerVAngle2: NXOpen.Expression = ...
    """
    Returns  the v cutout angle2 expression of the closed corner.  
    
    Applicable only when :py:meth:`NXOpen.Features.SheetMetal.MiterOptions.ClosedCornerTypeOptions`
    is :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``ClosedCornerVAngle2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    CornerTreatmentOffset: NXOpen.Expression = ...
    """
    Returns  the offset used for circular, u and v cutout corner treatments.  
    
    This only applies when the treatment type is set to 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.CircularCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.UCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``CornerTreatmentOffset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    CornerTreatmentOriginType: MiterOptionsCornerTreatmentOriginTypeOptions = ...
    """
    Returns or sets  the origin used for circular, u and v cutout corner treatments.  
    
    This only applies when the treatment type is set to 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.CircularCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.UCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``CornerTreatmentOriginType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsCornerTreatmentOriginTypeOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CornerTreatmentOriginType`` 
    
    :param originType: 
    :type originType: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsCornerTreatmentOriginTypeOptions` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndType: MiterOptionsTypeOptions = ...
    """
    Returns or sets  the miter end type.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``EndType`` 
    
    :param endType: 
    :type endType: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    MiterCorner: bool = ...
    """
    Returns or sets  the miter toggle value that specifies whether to miter the corner.  
    
    This only applies when the treatment type is set to 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.Closed <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.CircularCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.UCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``MiterCorner`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MiterCorner`` 
    
    :param miterCorner: 
    :type miterCorner: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MiterInteriorCornersIfNecessary: bool = ...
    """
    Returns or sets  the miter_corners option.  
    
    If set to true, it miter bend edges that are larger than default bend radius.
    
    <hr>
    
    Getter Method
    
    Signature ``MiterInteriorCornersIfNecessary`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MiterInteriorCornersIfNecessary`` 
    
    :param miterCorners: 
    :type miterCorners: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    MiterRootRadius: NXOpen.Expression = ...
    """
    Returns  the root radius used when mitering the corner.  
    
    This only applies when the treatment type is set to 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.Closed <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.CircularCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.UCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>` or 
    :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions.VCutout <Features.SheetMetal.MiterOptionsClosedCornerTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``MiterRootRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    Position: MiterOptionsPositionOptions = ...
    """
    Returns or sets  the position of miter.  
    
    <hr>
    
    Getter Method
    
    Signature ``Position`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsPositionOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Position`` 
    
    :param miterPosition: 
    :type miterPosition: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsPositionOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    StartType: MiterOptionsTypeOptions = ...
    """
    Returns or sets  the miter start type.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StartType`` 
    
    :param startType: 
    :type startType: :py:class:`NXOpen.Features.SheetMetal.MiterOptionsTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    ThreeBendCornerFlangeClearance: NXOpen.Expression = ...
    """
    Returns  the flange clearance used for a contour flange corner in case of a three bend corner condition.  
    
    This applies for all treatment types in :py:class:`Features.SheetMetal.MiterOptionsClosedCornerTypeOptions` 
    
    <hr>
    
    Getter Method
    
    Signature ``ThreeBendCornerFlangeClearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    """
    UseNormalCutoutMethod: bool = ...
    """
    Returns or sets  the cut type of the sheet.  
    
    If set to true, mitering is done using the normal cutout method and aims
    to reduce the small segements that result as part of miter computation, and is carried out on an unbent sheet.
    Normally, the cut runs through from one bend centre to another.  The sheet is later bent to achieve the desired result.
    
    <hr>
    
    Getter Method
    
    Signature ``UseNormalCutoutMethod`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseNormalCutoutMethod`` 
    
    :param cutType: 
    :type cutType: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    Null: MiterOptions = ...  # unknown typename


class ResizeNeutralFactorBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Resize Neutral Factor Builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateResizeNeutralFactorBuilder`
    
    .. versionadded:: NX5.0.0
    """
    BendFaces: NXOpen.ScCollector = ...
    """
    Returns  the bend face list provided by user 
    
    <hr>
    
    Getter Method
    
    Signature ``BendFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    NeutralFactor: NXOpen.Expression = ...
    """
    Returns  the neutral factor 
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralFactor`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    UseGlobal: bool = ...
    """
    Returns or sets  the Use Global Neutral Factor toggle.  
    
    <hr>
    
    Getter Method
    
    Signature ``UseGlobal`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseGlobal`` 
    
    :param useGlobal: 
    :type useGlobal: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: ResizeNeutralFactorBuilder = ...  # unknown typename


class ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ConvertToSheetmetalBuilderBendReliefTypeOptions():
    """
    This enum represents the bend relief type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Square", " - "
       "Round", " - "
    """
    NotSet = 0  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
    Square = 1  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
    Round = 2  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ConvertToSheetmetalBuilder(SheetmetalBaseBuilder):
    """
    This is the feature builder for the convert to sheetmetal feature.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateConvertToSheetmetalFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class BendReliefTypeOptions():
        """
        This enum represents the bend relief type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Square", " - "
           "Round", " - "
        """
        NotSet = 0  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
        Square = 1  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
        Round = 2  # ConvertToSheetmetalBuilderBendReliefTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetRipEdges(self) -> 'list[NXOpen.Edge]':
        """
        Gets the array of edges selected for ripping while converting to sheetmetal.  
        
        Signature ``GetRipEdges()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetRipEdges(self, ripEdges: 'list[NXOpen.Edge]') -> None:
        """
        Sets the array of edges that need to be ripped while converting to sheetmetal.  
        
        Signature ``SetRipEdges(ripEdges)`` 
        
        :param ripEdges: 
        :type ripEdges: list of :py:class:`NXOpen.Edge` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetBendReliefWidth(self, bendReliefWidth: str) -> None:
        """
        Signature ``SetBendReliefWidth(bendReliefWidth)`` 
        
        :param bendReliefWidth: 
        :type bendReliefWidth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.ConvertToSheetmetalBuilder.BendReliefWidth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def SetBendReliefDepth(self, bendReliefDepth: str) -> None:
        """
        Signature ``SetBendReliefDepth(bendReliefDepth)`` 
        
        :param bendReliefDepth: 
        :type bendReliefDepth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`Expression.RightHandSide` on the :py:class:`Expression` object returned from :py:meth:`Features.SheetMetal.ConvertToSheetmetalBuilder.BendReliefDepth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify that the builder data is valid for feature creation.  
        
        If the builder data is valid, it returns a value of 0.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  data validity flag (0 - valid, 1 - invalid)  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def CreateConvertInputListItem(self) -> ConvertInputListItemBuilder:
        """
        Create a corner list item.  
        
        Signature ``CreateConvertInputListItem()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    AdditionalFacesToConvert: NXOpen.ScCollector = ...
    """
    Returns  the additional faces to convert 
    
    <hr>
    
    Getter Method
    
    Signature ``AdditionalFacesToConvert`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BaseFace: NXOpen.Face = ...
    """
    Returns or sets  the base face from which the thickness of the part is determined.  
    
    <hr>
    
    Getter Method
    
    Signature ``BaseFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``BaseFace`` 
    
    :param baseFace: 
    :type baseFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    BendReliefDepth: NXOpen.Expression = ...
    """
    Returns  the bend relief depth.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    BendReliefType: ConvertToSheetmetalBuilderBendReliefTypeOptions = ...
    """
    Returns or sets  the bend relief type.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ConvertToSheetmetalBuilderBendReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``BendReliefType`` 
    
    :param bendReliefType: 
    :type bendReliefType: :py:class:`NXOpen.Features.SheetMetal.ConvertToSheetmetalBuilderBendReliefTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    BendReliefWidth: NXOpen.Expression = ...
    """
    Returns  the bend relief width.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendReliefWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    CornerList: ConvertInputListItemBuilderList = ...
    """
    Returns  the corner list 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilderList` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    LocalBaseFace: NXOpen.Face = ...
    """
    Returns or sets  the base face of local convert from which the thickness of the part is determined.  
    
    <hr>
    
    Getter Method
    
    Signature ``LocalBaseFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``LocalBaseFace`` 
    
    :param localBaseFace: 
    :type localBaseFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    LocalRegionFaces: NXOpen.ScCollector = ...
    """
    Returns  the faces for local convert 
    
    <hr>
    
    Getter Method
    
    Signature ``LocalRegionFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    MaintainZeroBendRadius: bool = ...
    """
    Returns or sets  the option for Maintain zero bend radius.  
    
    If the option is set to true,
    a tiny 0.02 mm radius bend will be created on inside sharp edge (for the 
    features created in NX8 or later releases); else the radius value from 
    NXSM Preferences will be used.
    
    <hr>
    
    Getter Method
    
    Signature ``MaintainZeroBendRadius`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``MaintainZeroBendRadius`` 
    
    :param maintainZeroBendRadius: 
    :type maintainZeroBendRadius: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    RipSection: NXOpen.Section = ...
    """
    Returns or sets  the section containing curves that need to be ripped while converting to sheetmetal.  
    
    <hr>
    
    Getter Method
    
    Signature ``RipSection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``RipSection`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the internal sketch (used to specify rip curves), if it exists.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Null: ConvertToSheetmetalBuilder = ...  # unknown typename


class DrawnCutoutBuilderDepthTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DrawnCutoutBuilderDepthTypeOptions():
    """
    This enum represents the depth direction for the drawn cutout. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Drawn Cutout punched on the side of the section normal."
       "SectionReverseNormalSide", "Drawn Cutout punched on the side opposite to that of the section normal"
    """
    SectionNormalSide = 0  # DrawnCutoutBuilderDepthTypeOptionsMemberType
    SectionReverseNormalSide = 1  # DrawnCutoutBuilderDepthTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DrawnCutoutBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DrawnCutoutBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the drawn cutout punches material. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
    along the section can also be represented by the vector resulting from the cross product of the curve tangent
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # DrawnCutoutBuilderSectionSideOptionsMemberType
    Right = 1  # DrawnCutoutBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DrawnCutoutBuilderSidewallTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DrawnCutoutBuilderSidewallTypeOptions():
    """
    The side walls material option. This specifies whether the drawn cutout's outerwalls or the innerwalls coincide with the section outline 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Outside", "the innerface of the drawn cutout side walls coincides with the section outline."
       "Inside", "the outerface of the drawn cutout side walls coincides with the section outline."
    """
    Outside = 0  # DrawnCutoutBuilderSidewallTypeOptionsMemberType
    Inside = 1  # DrawnCutoutBuilderSidewallTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DrawnCutoutBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents a Drawn Cutout feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateDrawnCutoutFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class DepthTypeOptions():
        """
        This enum represents the depth direction for the drawn cutout. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Drawn Cutout punched on the side of the section normal."
           "SectionReverseNormalSide", "Drawn Cutout punched on the side opposite to that of the section normal"
        """
        SectionNormalSide = 0  # DrawnCutoutBuilderDepthTypeOptionsMemberType
        SectionReverseNormalSide = 1  # DrawnCutoutBuilderDepthTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the drawn cutout punches material. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point
        along the section can also be represented by the vector resulting from the cross product of the curve tangent
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # DrawnCutoutBuilderSectionSideOptionsMemberType
        Right = 1  # DrawnCutoutBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SidewallTypeOptions():
        """
        The side walls material option. This specifies whether the drawn cutout's outerwalls or the innerwalls coincide with the section outline 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Outside", "the innerface of the drawn cutout side walls coincides with the section outline."
           "Inside", "the outerface of the drawn cutout side walls coincides with the section outline."
        """
        Outside = 0  # DrawnCutoutBuilderSidewallTypeOptionsMemberType
        Inside = 1  # DrawnCutoutBuilderSidewallTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetCutoutDepth(self, depth: str) -> None:
        """
        Signature ``SetCutoutDepth(depth)`` 
        
        :param depth: 
        :type depth: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder.CutoutDepth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetSideAngle(self, sideAngle: str) -> None:
        """
        Signature ``SetSideAngle(sideAngle)`` 
        
        :param sideAngle: 
        :type sideAngle: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder.SideAngle` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetRadiusOfDie(self, dieRadius: str) -> None:
        """
        Signature ``SetRadiusOfDie(dieRadius)`` 
        
        :param dieRadius: 
        :type dieRadius: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder.RadiusOfDie` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetCornerRadius(self, cornerRadius: str) -> None:
        """
        Signature ``SetCornerRadius(cornerRadius)`` 
        
        :param cornerRadius: 
        :type cornerRadius: str 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder.CornerRadius` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify whether the builder data is valid for creating a Drawn Cutout or not.  
        
        If the Builder data is valid, returned value shall be 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Data Validity Flag. 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    CornerRadius: NXOpen.Expression = ...
    """
    Returns  the Radius to be applied for rounding the sharp section corners
    
    <hr>
    
    Getter Method
    
    Signature ``CornerRadius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    CutoutDepth: NXOpen.Expression = ...
    """
    Returns  the depth of the Drawn Cutout
    
    <hr>
    
    Getter Method
    
    Signature ``CutoutDepth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    DepthType: DrawnCutoutBuilderDepthTypeOptions = ...
    """
    Returns or sets  the Direction in which the Drawn Cutout is punched.  
    
    This is used to specify the direction in which the punching should happen. If Punching must happen in the
    direction of the Section Normal (see :py:meth:`NXOpen.Features.SheetMetal.DrawnCutoutBuilder.Section`) then
    pass the value of :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions.SectionNormalSide <NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions>`
    If punching must happen in the opposite direction to that of Section Normal, set the value to be
    :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions.SectionReverseNormalSide <NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions>`
    
    <hr>
    
    Getter Method
    
    Signature ``DepthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``DepthType`` 
    
    :param depthType: 
    :type depthType: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    FilletSectionCorners: bool = ...
    """
    Returns or sets  the Rounding Option for section Corners which contain Non Fillet Radii
    
    <hr>
    
    Getter Method
    
    Signature ``FilletSectionCorners`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``FilletSectionCorners`` 
    
    :param filletSectionCorners: 
    :type filletSectionCorners: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    IncludeRounding: bool = ...
    """
    Returns or sets  the Rounding type of the Sharp edges of bottom face and top face.  
    
    <hr>
    
    Getter Method
    
    Signature ``IncludeRounding`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``IncludeRounding`` 
    
    :param roundType: 
    :type roundType: bool 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MinimumToolClearance: NXOpen.Expression = ...
    """
    Returns  
    the minimum tool clearance expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``MinimumToolClearance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    RadiusOfDie: NXOpen.Expression = ...
    """
    Returns  the Radius value of the sharp edges of the bottom face
    
    <hr>
    
    Getter Method
    
    Signature ``RadiusOfDie`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the Section used by the Drawn Cutout.  
    
    Section can be Open/Closed.
    
    The section is protruded on the reference face at finite distance of extent and in the direction of
    extent side. The actual extent distance will be determined by the active dimension option i.e. Offset
    Dimension or Full Dimension. In case of Offset Dimension the actual extent distance will be offset
    dimension distance plus the thickness of sheet. In case of Full Dimension the actual extent distance
    will be the Full dimension distance.
    In case of open section, the end segments are extended to the nearest flat face edges. If the end
    segments are already crossing the flat face edges, those segments will be trimmed to the edges.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SectionSide: DrawnCutoutBuilderSectionSideOptions = ...
    """
    Returns or sets  the section side for the Drawn Cutout.  
    
    This is used to specify which side of the section should remain stationary during the drawn cutout operation.
    drawn cutout's section is a set of connected curves. The material exists on both sides of the section curves.
    section Side specifies - the material on which side of the curve must be punched.The other side shall
    be bent to the specified angle with respect to this fixed side. This is how you calculate Left/Right.
    Get the Section Normal (N)Get the Tangent of the section.(T) Result =  CrossProduct(N, T). The resultant
    vector is called RIGHT. This vector shall be in the direction of one if the two sides of the material.If
    you want the material on the side of Result to be punched, then you have to pass the value of
    :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions.Right <NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions>` If you want the
    other side to be punched, then you have to send :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions.Left <NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``SectionSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SideAngle: NXOpen.Expression = ...
    """
    Returns  the Side Angle used by the Drawn Cutout.  
    
    In case of a tapered drawn cutout, the side angle is applied on the side faces of the above-protruded section.
    The affects of side angle will always increases the cavity volume of the drawn cutout.
    
    <hr>
    
    Getter Method
    
    Signature ``SideAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    SidewallType: DrawnCutoutBuilderSidewallTypeOptions = ...
    """
    Returns or sets  the side where the material must be added to the Drawn Cutout.  
    
    Done with Respect to the section
    
    If :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions.Inside <NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions>` is specified, the material of the drawn cutout sidewalls will be added to the interior of the section.
    If :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions.Outside <NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions>` is specified,the material will be added from the lifted section such that the volume of the drawn cutout cavity is increased.
    
    <hr>
    
    Getter Method
    
    Signature ``SidewallType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``SidewallType`` 
    
    :param sidewallType: 
    :type sidewallType: :py:class:`NXOpen.Features.SheetMetal.DrawnCutoutBuilderSidewallTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the Slave Sketch used by the Drawn Cutout, If one exists.  
    
    If the Sketch is created internally as part of the Drawn Cutout command in the UI, then it shall be consumed by the Drawn Cutout and shall not show up as a separate feature in the Part Navigator.
    If such a behaviour is deired, then specify the Sketch here.
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: DrawnCutoutBuilder = ...  # unknown typename


class BendTaperBuilderBendTaperSidesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderBendTaperSides():
    """
    This enum represents the taper sides options for the bend taper. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Both", "Both Sides"
       "Side1", "Side 1 only"
       "Side2", "Side 2 only"
       "Symmetric", "Symmetric. Side 1 = Side 2"
    """
    Both = 0  # BendTaperBuilderBendTaperSidesMemberType
    Side1 = 1  # BendTaperBuilderBendTaperSidesMemberType
    Side2 = 2  # BendTaperBuilderBendTaperSidesMemberType
    Symmetric = 3  # BendTaperBuilderBendTaperSidesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilderChainingTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderChainingType():
    """
    This enum represents the chaining options for the bend taper.   
    
    .. deprecated::  NX8.5.0
       Use WebTaperType instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BendOnly", "Bend Only"
       "BendFace", "Bend and Face"
       "BendFaceChain", "Bend and Face Chain"
    """
    BendOnly = 0  # BendTaperBuilderChainingTypeMemberType
    BendFace = 1  # BendTaperBuilderChainingTypeMemberType
    BendFaceChain = 2  # BendTaperBuilderChainingTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilderBendTaperTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderBendTaperType():
    """
    This enum represents the bend taper types for the bend taper. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Linear", "Linear"
       "Tangent", "Tangent"
       "Square", "Square"
    """
    Linear = 0  # BendTaperBuilderBendTaperTypeMemberType
    Tangent = 1  # BendTaperBuilderBendTaperTypeMemberType
    Square = 2  # BendTaperBuilderBendTaperTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilderBendTaperInputMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderBendTaperInputMethod():
    """
    This enum represents the input methods for the bend taper. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Angle", "Angle"
       "Distance", "Distance"
       "ToEnd", "To End"
    """
    Angle = 0  # BendTaperBuilderBendTaperInputMethodMemberType
    Distance = 1  # BendTaperBuilderBendTaperInputMethodMemberType
    ToEnd = 2  # BendTaperBuilderBendTaperInputMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilderWebTaperTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderWebTaperType():
    """
    This enum represents the web taper types for the bend taper. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None"
       "Face", "Face"
       "FaceChain", "Face Chain"
    """
    NotSet = 0  # BendTaperBuilderWebTaperTypeMemberType
    Face = 1  # BendTaperBuilderWebTaperTypeMemberType
    FaceChain = 2  # BendTaperBuilderWebTaperTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilderStartTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendTaperBuilderStartType():
    """
    This enum represents the start types for the bend taper.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TaperFromBend", "Taper from Bend"
       "TaperFromWeb", "Taper from Web"
    """
    TaperFromBend = 0  # BendTaperBuilderStartTypeMemberType
    TaperFromWeb = 1  # BendTaperBuilderStartTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendTaperBuilder(SheetmetalBaseBuilder):
    """
    Represents a Bend Taper feature builder
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateBendTaperBuilder`
    
    Default values.
    
    ======================  ==========================================
    Property                Value
    ======================  ==========================================
    BendTaperAngle1.Value   10 
    ----------------------  ------------------------------------------
    BendTaperAngle2.Value   10 
    ----------------------  ------------------------------------------
    BendTaperInputMethod1   Angle 
    ----------------------  ------------------------------------------
    BendTaperInputMethod2   Angle 
    ----------------------  ------------------------------------------
    BendTaperType1          Linear 
    ----------------------  ------------------------------------------
    BendTaperType2          Linear 
    ----------------------  ------------------------------------------
    Chaining (deprecated)   BendOnly 
    ----------------------  ------------------------------------------
    EndRadius1.Value        2 (millimeters part), 0.1 (inches part) 
    ----------------------  ------------------------------------------
    EndRadius2.Value        2 (millimeters part), 0.1 (inches part) 
    ----------------------  ------------------------------------------
    InferRadius1            1 
    ----------------------  ------------------------------------------
    InferRadius2            1 
    ----------------------  ------------------------------------------
    StartRadius1.Value      2 (millimeters part), 0.1 (inches part) 
    ----------------------  ------------------------------------------
    StartRadius2.Value      2 (millimeters part), 0.1 (inches part) 
    ----------------------  ------------------------------------------
    StartType1              TaperFromBend 
    ----------------------  ------------------------------------------
    StartType2              TaperFromBend 
    ----------------------  ------------------------------------------
    TaperDistance1.Value    5.0 (millimeters part), 0.3 (inches part) 
    ----------------------  ------------------------------------------
    TaperDistance2.Value    5.0 (millimeters part), 0.3 (inches part) 
    ----------------------  ------------------------------------------
    TaperSides              Both 
    ----------------------  ------------------------------------------
    WebTaperAngle1.Value    0 
    ----------------------  ------------------------------------------
    WebTaperAngle2.Value    0 
    ----------------------  ------------------------------------------
    WebTaperType1           None 
    ----------------------  ------------------------------------------
    WebTaperType2           None 
    ======================  ==========================================
    
    .. versionadded:: NX6.0.0
    """
    
    class BendTaperSides():
        """
        This enum represents the taper sides options for the bend taper. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Both", "Both Sides"
           "Side1", "Side 1 only"
           "Side2", "Side 2 only"
           "Symmetric", "Symmetric. Side 1 = Side 2"
        """
        Both = 0  # BendTaperBuilderBendTaperSidesMemberType
        Side1 = 1  # BendTaperBuilderBendTaperSidesMemberType
        Side2 = 2  # BendTaperBuilderBendTaperSidesMemberType
        Symmetric = 3  # BendTaperBuilderBendTaperSidesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ChainingType():
        """
        This enum represents the chaining options for the bend taper.   
        
        .. deprecated::  NX8.5.0
           Use WebTaperType instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BendOnly", "Bend Only"
           "BendFace", "Bend and Face"
           "BendFaceChain", "Bend and Face Chain"
        """
        BendOnly = 0  # BendTaperBuilderChainingTypeMemberType
        BendFace = 1  # BendTaperBuilderChainingTypeMemberType
        BendFaceChain = 2  # BendTaperBuilderChainingTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendTaperType():
        """
        This enum represents the bend taper types for the bend taper. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Linear", "Linear"
           "Tangent", "Tangent"
           "Square", "Square"
        """
        Linear = 0  # BendTaperBuilderBendTaperTypeMemberType
        Tangent = 1  # BendTaperBuilderBendTaperTypeMemberType
        Square = 2  # BendTaperBuilderBendTaperTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class BendTaperInputMethod():
        """
        This enum represents the input methods for the bend taper. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Angle", "Angle"
           "Distance", "Distance"
           "ToEnd", "To End"
        """
        Angle = 0  # BendTaperBuilderBendTaperInputMethodMemberType
        Distance = 1  # BendTaperBuilderBendTaperInputMethodMemberType
        ToEnd = 2  # BendTaperBuilderBendTaperInputMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class WebTaperType():
        """
        This enum represents the web taper types for the bend taper. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None"
           "Face", "Face"
           "FaceChain", "Face Chain"
        """
        NotSet = 0  # BendTaperBuilderWebTaperTypeMemberType
        Face = 1  # BendTaperBuilderWebTaperTypeMemberType
        FaceChain = 2  # BendTaperBuilderWebTaperTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StartType():
        """
        This enum represents the start types for the bend taper.   
        
        .. versionadded:: NX10.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "TaperFromBend", "Taper from Bend"
           "TaperFromWeb", "Taper from Web"
        """
        TaperFromBend = 0  # BendTaperBuilderStartTypeMemberType
        TaperFromWeb = 1  # BendTaperBuilderStartTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    BendTaperAngle1: NXOpen.Expression = ...
    """
    Returns  the bend taper angle1 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperAngle1`` 
    
    :returns:  The bend taper angle for side 1 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperAngle2: NXOpen.Expression = ...
    """
    Returns  the bend taper angle2 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperAngle2`` 
    
    :returns:  The bend taper angle for side 2 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperInputMethod1: BendTaperBuilderBendTaperInputMethod = ...
    """
    Returns or sets  the input method for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperInputMethod1`` 
    
    :returns:  The input method can be Angle,  Distance and To End 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperInputMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendTaperInputMethod1`` 
    
    :param bendTaperInputMethod1:  The input method can be Angle, Distance and To End 
    :type bendTaperInputMethod1: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperInputMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperInputMethod2: BendTaperBuilderBendTaperInputMethod = ...
    """
    Returns or sets  the input method for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperInputMethod2`` 
    
    :returns:  The input method can be Angle, Distance and To End 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperInputMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendTaperInputMethod2`` 
    
    :param bendTaperInputMethod2:  The input method can be Angle, Distance and To End 
    :type bendTaperInputMethod2: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperInputMethod` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperSelectBendFace: NXOpen.ScCollector = ...
    """
    Returns  the bend taper select bend face.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperSelectBendFace`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperType1: BendTaperBuilderBendTaperType = ...
    """
    Returns or sets  the bend taper type for Side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperType1`` 
    
    :returns:  The bend taper type can be Linear, Tangent and Square.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendTaperType1`` 
    
    :param bendTaperType1:  The bend taper type can be Linear, Tangent and Square.  
    :type bendTaperType1: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTaperType2: BendTaperBuilderBendTaperType = ...
    """
    Returns or sets  the bend taper type for Side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTaperType2`` 
    
    :returns:  The bend taper type can be Linear, Tangent and Square.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``BendTaperType2`` 
    
    :param bendTaperType2:  The bend taper type can be Linear, Tangent and Square.  
    :type bendTaperType2: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Chaining: BendTaperBuilderChainingType = ...
    """
    Returns or sets  the chaining 
    
    <hr>
    
    Getter Method
    
    Signature ``Chaining`` 
    
    :returns:  The chaining can be Bend Only, Bend and Face, and Bend and Face Chain.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderChainingType` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:meth:`WebTaperType1`` and :py:meth:`WebTaperType2`` instead.
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Chaining`` 
    
    :param chaining:  The chaining can be Bend Only, Bend and Face, and Bend and Face Chain.  
    :type chaining: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderChainingType` 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX8.5.0
       Use :py:meth:`WebTaperType1`` and :py:meth:`WebTaperType2`` instead.
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndRadius1: NXOpen.Expression = ...
    """
    Returns  the end radius for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``EndRadius1`` 
    
    :returns:  the end radius for side 1  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    EndRadius2: NXOpen.Expression = ...
    """
    Returns  the end radius for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``EndRadius2`` 
    
    :returns:  the end radius for side 2  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    InferRadius1: bool = ...
    """
    Returns or sets  the infer radius flag for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``InferRadius1`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``InferRadius1`` 
    
    :param inferRadius1: 
    :type inferRadius1: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    InferRadius2: bool = ...
    """
    Returns or sets  the infer radius flag for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``InferRadius2`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``InferRadius2`` 
    
    :param inferRadius2: 
    :type inferRadius2: bool 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    ReverseTaperDirection: bool = ...
    """
    Returns or sets  the flag indication the reverse taper direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseTaperDirection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`StationaryEntity`` instead.
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseTaperDirection`` 
    
    :param reverseTaperDirection: 
    :type reverseTaperDirection: bool 
    
    .. versionadded:: NX6.0.0
    
    .. deprecated::  NX10.0.0
       Use :py:meth:`StationaryEntity`` instead.
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartRadius1: NXOpen.Expression = ...
    """
    Returns  the start radius for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``StartRadius1`` 
    
    :returns:  the start radius for side 1  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartRadius2: NXOpen.Expression = ...
    """
    Returns  the start radius for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``StartRadius2`` 
    
    :returns:  the start radius for side 2  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartType1: BendTaperBuilderStartType = ...
    """
    Returns or sets  the start type for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``StartType1`` 
    
    :returns:  the start type can be Taper from Bend or Taper from Web 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderStartType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartType1`` 
    
    :param startType1:  the start type can be Taper from Bend or Taper from Web 
    :type startType1: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderStartType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StartType2: BendTaperBuilderStartType = ...
    """
    Returns or sets  the start type for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``StartType2`` 
    
    :returns:  the start type can be Taper from Bend and Taper from Web 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderStartType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StartType2`` 
    
    :param startType2:  the start type can be Taper from Bend and Taper from Web 
    :type startType2: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderStartType` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    StationaryEntity: NXOpen.NXObject = ...
    """
    Returns or sets  the stationary entity, can be an edge or a face.  
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryEntity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryEntity`` 
    
    :param bendTaperStationaryEntity: 
    :type bendTaperStationaryEntity: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TaperDistance1: NXOpen.Expression = ...
    """
    Returns  the taper distance for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperDistance1`` 
    
    :returns:  the taper distance for side 1  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TaperDistance2: NXOpen.Expression = ...
    """
    Returns  the taper distance for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperDistance2`` 
    
    :returns:  the taper distance for side 2  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TaperSides: BendTaperBuilderBendTaperSides = ...
    """
    Returns or sets  the taper sides 
    
    <hr>
    
    Getter Method
    
    Signature ``TaperSides`` 
    
    :returns:  The taperSides can be Both, Side 1, Side 2, and Symmetric.  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperSides` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TaperSides`` 
    
    :param taperSides:  The taperSides can be Both, Side 1, Side 2, and Symmetric.  
    :type taperSides: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderBendTaperSides` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    WebTaperAngle1: NXOpen.Expression = ...
    """
    Returns  the web taper angle1 
    
    <hr>
    
    Getter Method
    
    Signature ``WebTaperAngle1`` 
    
    :returns:  The web taper angle for side 1 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    WebTaperAngle2: NXOpen.Expression = ...
    """
    Returns  the web taper angle2 
    
    <hr>
    
    Getter Method
    
    Signature ``WebTaperAngle2`` 
    
    :returns:  The web taper angle for side 2 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    WebTaperType1: BendTaperBuilderWebTaperType = ...
    """
    Returns or sets  the web taper type for side 1 
    
    <hr>
    
    Getter Method
    
    Signature ``WebTaperType1`` 
    
    :returns:  the web taper type can be  None, Face and Face Chain 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderWebTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``WebTaperType1`` 
    
    :param webTaperType1:  the web taper type can be  None, Face and Face Chain 
    :type webTaperType1: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderWebTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    WebTaperType2: BendTaperBuilderWebTaperType = ...
    """
    Returns or sets  the web taper type for side 2 
    
    <hr>
    
    Getter Method
    
    Signature ``WebTaperType2`` 
    
    :returns:  the web taper type can be  None, Face and Face Chain 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderWebTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``WebTaperType2`` 
    
    :param webTaperType2:  the web taper type can be  None, Face and Face Chain 
    :type webTaperType2: :py:class:`NXOpen.Features.SheetMetal.BendTaperBuilderWebTaperType` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: BendTaperBuilder = ...  # unknown typename


class MigratedPanelBuilder(NXOpen.Features.FeatureBuilder):
    """
    Represents an I-DEAS Migrated Panel feature builder
    
    This builder cannot be instantiated separately.
    
    .. versionadded:: NX5.0.0
    """
    AlongFaceNormal: bool = ...
    """
    Returns or sets 
    the along face normal flag.  
    
    This value only has meaning
    for the ground panel.
    
    The edge that defines an end condition must be linear and must be on the
    stationary face for the Ground Panel and the moving face for other panels.
    The index indicates the position of the End Condition that will be
    modified.  The first End Condition has an index of zero.
    
    <hr>
    
    Getter Method
    
    Signature ``AlongFaceNormal`` 
    
    :returns:  Along Face Normal flag  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``AlongFaceNormal`` 
    
    :param alongFaceNormal:  Along Face Normal flag  
    :type alongFaceNormal: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BendFace: NXOpen.Face = ...
    """
    Returns or sets 
    the parent bend face.  
    
    This face will usually be NULL.  It will
    be non-NULL if this Migrated Panel was defined using the BFCS
    (Bend From Cylindrical Surface) method.
    
    The set method is only available inside the I-DEAS to NX Content Migration Manager.
    
    <hr>
    
    Getter Method
    
    Signature ``BendFace`` 
    
    :returns:  The bend face  
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``BendFace`` 
    
    :param bendFace:  The bend face  
    :type bendFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BendOptions: BendOptions = ...
    """
    Returns  the bend options for the panel feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns:  Bend Options  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BendRadius: str = ...
    """
    Returns or sets 
    the bend radius expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendRadius`` 
    
    :returns:  Gap tolerance  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``BendRadius`` 
    
    :param bendRadius:  Gap tolerance  
    :type bendRadius: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    CutoffAngle: str = ...
    """
    Returns or sets 
    the cutoff angle expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``CutoffAngle`` 
    
    :returns:  Cutoff angle  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``CutoffAngle`` 
    
    :param cutoffAngle:  Cutoff angle  
    :type cutoffAngle: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    EndConditions: NXOpen.ExpressionCollectorSet = ...
    """
    Returns  the end conditions 
    
    <hr>
    
    Getter Method
    
    Signature ``EndConditions`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ExpressionCollectorSet` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    GapTolerance: str = ...
    """
    Returns or sets 
    the gap tolerance expression.  
    
    This is the size of the gap introduced
    between this panel and neighboring features.
    
    <hr>
    
    Getter Method
    
    Signature ``GapTolerance`` 
    
    :returns:  Gap tolerance  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``GapTolerance`` 
    
    :param gapTolerance:  Gap tolerance  
    :type gapTolerance: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MovingFace: NXOpen.Face = ...
    """
    Returns or sets 
    the parent moving face.  
    
    This face will be NULL for the ground panel.
    If non-NULL, the face must be planar.
    
    The set method is only available inside the I-DEAS to NX Content Migration Manager.
    
    <hr>
    
    Getter Method
    
    Signature ``MovingFace`` 
    
    :returns:  The moving face  
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``MovingFace`` 
    
    :param moveFace:  The moving face  
    :type moveFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    NeutralOffset: str = ...
    """
    Returns or sets 
    the neutral offset (i.  
    
    e., K Factor) expression.
    
    <hr>
    
    Getter Method
    
    Signature ``NeutralOffset`` 
    
    :returns:  Gap tolerance  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``NeutralOffset`` 
    
    :param gapTolerance:  Gap tolerance  
    :type gapTolerance: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    ParentSmBody: NXOpen.Body = ...
    """
    Returns or sets 
    the parent sheet metal body.  
    
    The Migrated Panel is applied to this
    body.  The body must be made up of other Migrated Panel features. This
    body will be NULL for the ground panel.
    
    The set method is only available inside the I-DEAS to NX Content Migration Manager.
    
    <hr>
    
    Getter Method
    
    Signature ``ParentSmBody`` 
    
    :returns:  Parent Sheet Metal Body  
    :rtype: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``ParentSmBody`` 
    
    :param sheetMetalBody:  Parent Sheet Metal Body  
    :type sheetMetalBody: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    StationaryFace: NXOpen.Face = ...
    """
    Returns or sets 
    the parent stationary face.  
    
    This face cannot be NULL.
    
    The set method is only available inside the I-DEAS to NX Content Migration Manager.
    
    <hr>
    
    Getter Method
    
    Signature ``StationaryFace`` 
    
    :returns:  The stationary face  
    :rtype: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``StationaryFace`` 
    
    :param stationaryFace:  The stationary face  
    :type stationaryFace: :py:class:`NXOpen.Face` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: MigratedPanelBuilder = ...  # unknown typename


class ThreeBendCornerBuilderTreatmentTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ThreeBendCornerBuilderTreatmentTypeOptions():
    """
    This enum represents the corner treatment type. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Open", " - "
       "Closed", " - "
       "CircularCutout", " - "
       "UCutout", " - "
       "VCutout", " - "
    """
    Open = 0  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
    Closed = 1  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
    CircularCutout = 2  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
    UCutout = 3  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
    VCutout = 4  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ThreeBendCornerBuilderOriginTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ThreeBendCornerBuilderOriginTypes():
    """
    This enum represents Origin type
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "BendCenter", "The relief origin will be at the intersection of first bend's centerline and bisector of corner angle."
       "CornerPoint", "The relief origin will be at the corner point."
    """
    BendCenter = 0  # ThreeBendCornerBuilderOriginTypesMemberType
    CornerPoint = 1  # ThreeBendCornerBuilderOriginTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ThreeBendCornerBuilder(NXOpen.Features.FeatureBuilder):
    """
    The Three Bend Corner feature class.  
    
    Users can identify multiple input face pairs for each three bend 
    corner feature. Each pair is made up of one face each from adjacent bends. The bends must both have the 
    same radius and sweep angle, and they must also be connected via another adjoining bend.
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateThreeBendCornerFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class TreatmentTypeOptions():
        """
        This enum represents the corner treatment type. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Open", " - "
           "Closed", " - "
           "CircularCutout", " - "
           "UCutout", " - "
           "VCutout", " - "
        """
        Open = 0  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
        Closed = 1  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
        CircularCutout = 2  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
        UCutout = 3  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
        VCutout = 4  # ThreeBendCornerBuilderTreatmentTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OriginTypes():
        """
        This enum represents Origin type
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "BendCenter", "The relief origin will be at the intersection of first bend's centerline and bisector of corner angle."
           "CornerPoint", "The relief origin will be at the corner point."
        """
        BendCenter = 0  # ThreeBendCornerBuilderOriginTypesMemberType
        CornerPoint = 1  # ThreeBendCornerBuilderOriginTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Input a bend face pair for the three bend corner feature.  
        
        This method can be called multiple  
        times for a feature, with each bend face pair representing a unique corner.
        
        Signature ``AddFacePair(firstFace, secondFace)`` 
        
        :param firstFace:   A bend face from a bend  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:   A bend face from an adjacent bend  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def RemoveFacePair(self, firstFace: NXOpen.Face, secondFace: NXOpen.Face) -> None:
        """
        Removes a face pair (that represents a unique corner) from the list of face pairs already added.  
        
        Signature ``RemoveFacePair(firstFace, secondFace)`` 
        
        :param firstFace:  A face from an already selected face pair  
        :type firstFace: :py:class:`NXOpen.Face` 
        :param secondFace:  The other face from the face pair  
        :type secondFace: :py:class:`NXOpen.Face` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def GetFacePair(self, index: int) -> tuple:
        """
        Gets the bend face pair at the given index.  
        
        The index can vary between zero and one less than the 
        value returned by :py:meth:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.NumberOfFacePairs`.
        
        Signature ``GetFacePair(index)`` 
        
        :param index:  Index of the desired face pair  
        :type index: int 
        :returns: a tuple 
        :rtype: A tuple consisting of (firstFace, secondFace). firstFace is a :py:class:`NXOpen.Face`.   First face of the face pair secondFace is a :py:class:`NXOpen.Face`.   Second face of the face pair 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def SetDiameter(self, diameter: str) -> None:
        """
        The diameter used for the circular cutout corner treatment.  
        
        This only applies when the treatment type is set to 
        :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or 
        :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
        :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.            .
        
        Signature ``SetDiameter(diameter)`` 
        
        :param diameter:  The diameter for the circular cutout corner treatment  
        :type diameter: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.Diameter` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify that the builder data is valid for creation of a three bend corner.  
        
        If the data in the builder is valid, the return value is 0
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  Returns 0 if the data in the builder is valid  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal")
        """
        ...
    
    BlendMiter: bool = ...
    """
    Returns or sets  the option for smooth transition from miter to cutout edges.  
    
    <hr>
    
    Getter Method
    
    Signature ``BlendMiter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``BlendMiter`` 
    
    :param blendMiter: 
    :type blendMiter: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    BlendMiterRadius: NXOpen.Expression = ...
    """
    Returns  the blend miter radius used for three bend corner miter treatment.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.Closed <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``BlendMiterRadius`` 
    
    :returns:  The blend miter radius for the three bend corner miter treatment  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns  the diameter used for circular, u and v cutout corner treatments.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns:  The diameter for the circular cutout corner treatment  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    FlangeClearance: NXOpen.Expression = ...
    """
    Returns  the flange clearance used for three bend corner miter treatment.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.Open <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.Closed <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FlangeClearance`` 
    
    :returns:  The flange clearance for the three bend corner miter treatment  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MiterCorner: bool = ...
    """
    Returns or sets  whether the corner will be closed using miter.  
    
    <hr>
    
    Getter Method
    
    Signature ``MiterCorner`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``MiterCorner`` 
    
    :param miterCorner: 
    :type miterCorner: bool 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    MiterRootRadius: NXOpen.Expression = ...
    """
    Returns  the miter root radius used for three bend corner miter treatment.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.Closed <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``MiterRootRadius`` 
    
    :returns:  The miter root radius for the three bend corner miter treatment  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    NumberOfFacePairs: int = ...
    """
    Returns  the number of face pairs already identified for the three bend corner feature.  
    
    <hr>
    
    Getter Method
    
    Signature ``NumberOfFacePairs`` 
    
    :returns:  The number of face pairs currently identified  
    :rtype: int 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset used for circular, u and v cutout corner treatments.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns:  The offset for the circular/u/v cutout corner treatment  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    OriginType: ThreeBendCornerBuilderOriginTypes = ...
    """
    Returns or sets  the relief origin used for circular, u and v cutout corner treatments.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.CircularCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.UCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>` or
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``OriginType`` 
    
    :returns:  The relief origin type 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderOriginTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``OriginType`` 
    
    :param originType:  The relief origin type 
    :type originType: :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderOriginTypes` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    TreatmentType: ThreeBendCornerBuilderTreatmentTypeOptions = ...
    """
    Returns or sets  the corner treatment type.  
    
    The :py:meth:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilder.TreatmentType``) specifies how the 
    corner should be treated. Valid options are in :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions`. 
    
    <hr>
    
    Getter Method
    
    Signature ``TreatmentType`` 
    
    :returns:  The type of treatment specified for the corner  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    
    <hr>
    
    Setter Method
    
    Signature ``TreatmentType`` 
    
    :param treatmentType:  The type of treatment specified for the corner 
    :type treatmentType: :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    VCutoutAngle1: NXOpen.Expression = ...
    """
    Returns  the angle 1 used for the v cutout treatment.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``VCutoutAngle1`` 
    
    :returns:  The Angle 1 for the v cutout corner treatment   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    VCutoutAngle2: NXOpen.Expression = ...
    """
    Returns  the angle 2 used for the v cutout treatment.  
    
    This only applies when the treatment type is set to 
    :py:class:`NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions.VCutout <NXOpen.Features.SheetMetal.ThreeBendCornerBuilderTreatmentTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``VCutoutAngle2`` 
    
    :returns:  The Angle 2 for the v cutout corner treatment   
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX8.5.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal")
    """
    Null: ThreeBendCornerBuilder = ...  # unknown typename


class ConvertInputListItemBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[ConvertInputListItemBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: ConvertInputListItemBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
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
    
    
    def FindIndex(self, obj: ConvertInputListItemBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> ConvertInputListItemBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
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
    def Erase(self, obj: ConvertInputListItemBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: ConvertInputListItemBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
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
    
    
    def GetContents(self) -> 'list[ConvertInputListItemBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[ConvertInputListItemBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
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
    def Swap(self, object1: ConvertInputListItemBuilder, object2: ConvertInputListItemBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: ConvertInputListItemBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.SheetMetal.ConvertInputListItemBuilder` 
        
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
    Null: ConvertInputListItemBuilderList = ...  # unknown typename


class AeroFlangeBuilderLengthTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderLengthType():
    """
    This enum defines the length type options. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Value", "Value"
       "Infer", "Infer from face"
    """
    Value = 0  # AeroFlangeBuilderLengthTypeMemberType
    Infer = 1  # AeroFlangeBuilderLengthTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilderEndTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderEndType():
    """
    This enum defines the ends of a bend edge 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "End1", "Start of section"
       "End2", "End of section"
       "Closed", "Periodic Bend Edge"
    """
    End1 = 0  # AeroFlangeBuilderEndTypeMemberType
    End2 = 1  # AeroFlangeBuilderEndTypeMemberType
    Closed = 2  # AeroFlangeBuilderEndTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilderDirTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderDirType():
    """
    This enum defines the type of direction vector 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Bend", "Bend Direction Type"
       "Discard", "Discard Direction Type"
    """
    Bend = 0  # AeroFlangeBuilderDirTypeMemberType
    Discard = 1  # AeroFlangeBuilderDirTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilderCompTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderCompType():
    """
    This method defines the types of Flange Compensation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Automatic", "Automatic"
       "Angle", "Angle"
       "Distance", "Distance"
       "NotSet", "None"
    """
    Automatic = 0  # AeroFlangeBuilderCompTypeMemberType
    Angle = 1  # AeroFlangeBuilderCompTypeMemberType
    Distance = 2  # AeroFlangeBuilderCompTypeMemberType
    NotSet = 3  # AeroFlangeBuilderCompTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilderMatTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderMatType():
    """
    This enum defines the material types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", "Material Inside"
       "MaterialOutside", "Material Outside"
       "BendOutside", "Bend Outside"
    """
    MaterialInside = 0  # AeroFlangeBuilderMatTypeMemberType
    MaterialOutside = 1  # AeroFlangeBuilderMatTypeMemberType
    BendOutside = 2  # AeroFlangeBuilderMatTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilderDimTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AeroFlangeBuilderDimType():
    """
    This enum defines the flange length dimension types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", "Inside Dimension"
       "Outside", "Outside Dimension"
    """
    Inside = 0  # AeroFlangeBuilderDimTypeMemberType
    Outside = 1  # AeroFlangeBuilderDimTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroFlangeBuilder(SheetmetalBaseBuilder):
    """
    Represents a Aerospace Sheet Metal Flange Builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.AeroSheetmetalManager.CreateFlangeBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class LengthType():
        """
        This enum defines the length type options. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Value", "Value"
           "Infer", "Infer from face"
        """
        Value = 0  # AeroFlangeBuilderLengthTypeMemberType
        Infer = 1  # AeroFlangeBuilderLengthTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class EndType():
        """
        This enum defines the ends of a bend edge 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "End1", "Start of section"
           "End2", "End of section"
           "Closed", "Periodic Bend Edge"
        """
        End1 = 0  # AeroFlangeBuilderEndTypeMemberType
        End2 = 1  # AeroFlangeBuilderEndTypeMemberType
        Closed = 2  # AeroFlangeBuilderEndTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DirType():
        """
        This enum defines the type of direction vector 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Bend", "Bend Direction Type"
           "Discard", "Discard Direction Type"
        """
        Bend = 0  # AeroFlangeBuilderDirTypeMemberType
        Discard = 1  # AeroFlangeBuilderDirTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CompType():
        """
        This method defines the types of Flange Compensation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Automatic", "Automatic"
           "Angle", "Angle"
           "Distance", "Distance"
           "NotSet", "None"
        """
        Automatic = 0  # AeroFlangeBuilderCompTypeMemberType
        Angle = 1  # AeroFlangeBuilderCompTypeMemberType
        Distance = 2  # AeroFlangeBuilderCompTypeMemberType
        NotSet = 3  # AeroFlangeBuilderCompTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class MatType():
        """
        This enum defines the material types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", "Material Inside"
           "MaterialOutside", "Material Outside"
           "BendOutside", "Bend Outside"
        """
        MaterialInside = 0  # AeroFlangeBuilderMatTypeMemberType
        MaterialOutside = 1  # AeroFlangeBuilderMatTypeMemberType
        BendOutside = 2  # AeroFlangeBuilderMatTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DimType():
        """
        This enum defines the flange length dimension types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", "Inside Dimension"
           "Outside", "Outside Dimension"
        """
        Inside = 0  # AeroFlangeBuilderDimTypeMemberType
        Outside = 1  # AeroFlangeBuilderDimTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetAngle(self, angleExpression: str) -> None:
        """
        Set the angle expression.  
        
        This method should be called only when there is no ref_face selection.
        
        Signature ``SetAngle(angleExpression)`` 
        
        :param angleExpression:  value of angle expression  
        :type angleExpression: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetLength(self, type: AeroFlangeBuilderLengthType, valueExpression: str) -> None:
        """
        Set the type of length and the length expression.  
        
        If there are no ref_face's then the only length type 
        possible is "Value". If there are selected ref_face's 
        and the length type is "Infer", then the length 
        expression should be NULL.
        
        Signature ``SetLength(type, valueExpression)`` 
        
        :param type:  length type input Value/Infer  
        :type type: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderLengthType` 
        :param valueExpression:  value of length expression  
        :type valueExpression: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetLength(self) -> tuple:
        """
        Get the type of length and the length expression.  
        
        Signature ``GetLength()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (lengthExpression, type). lengthExpression is a :py:class:`NXOpen.Expression`.   length expression type is a :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderLengthType`.   length type Value/Infer 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetFlipDirection(self, type: AeroFlangeBuilderDirType, flipFlag: bool) -> None:
        """
        Set flip direction.  
        
        This method is called if either the bend direction or the
        material direction needs to be flipped. 
        
        Signature ``SetFlipDirection(type, flipFlag)`` 
        
        :param type:  direction type bend/discard  
        :type type: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderDirType` 
        :param flipFlag:  flip_flag => false = do not flip, true = flip  
        :type flipFlag: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetFlipDirection(self, type: AeroFlangeBuilderDirType) -> bool:
        """
        Get flip direction.  
        
        Signature ``GetFlipDirection(type)`` 
        
        :param type:  direction type bend/discard  
        :type type: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderDirType` 
        :returns:  flip_flag => false = do not flip, true = flip  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetEndCompensation(self, endType: AeroFlangeBuilderEndType, compType: AeroFlangeBuilderCompType, valueExpression: str) -> None:
        """
        Set end compensation.  
        
        This method sets the flange compensation for one end of a non-periodic
        Base Edge section. The end_type input parameter denotes if the end is
        the start of section(end1) or the end of section(end2). If the compensation
        type( comp_type) is either Angle or Distance, an expression for the
        value of compensation must be provided. This expression input can be NULL
        for Automatic and None type of compensations.
        
        Signature ``SetEndCompensation(endType, compType, valueExpression)`` 
        
        :param endType:  end1/end2  
        :type endType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderEndType` 
        :param compType:  Automatic/Angle/Distance/None  
        :type compType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderCompType` 
        :param valueExpression:  value of compensation expression  
        :type valueExpression: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetEndCompensation(self, endType: AeroFlangeBuilderEndType) -> tuple:
        """
        Get end compensation.  
        
        Signature ``GetEndCompensation(endType)`` 
        
        :param endType:  end1/end2  
        :type endType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderEndType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (valueExpression, compType). valueExpression is a :py:class:`NXOpen.Expression`.   compensation expression compType is a :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderCompType`.   Automatic/Angle/Distance/None 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetEndPlane(self, endType: AeroFlangeBuilderEndType, endPlane: NXOpen.Plane) -> None:
        """
        Set the end plane 
        
        Signature ``SetEndPlane(endType, endPlane)`` 
        
        :param endType:  end1/end2  
        :type endType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderEndType` 
        :param endPlane:  smart plane entity  
        :type endPlane: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetEndPlane(self, endType: AeroFlangeBuilderEndType) -> NXOpen.Plane:
        """
        Get the end plane 
        
        Signature ``GetEndPlane(endType)`` 
        
        :param endType:  end1/end2  
        :type endType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderEndType` 
        :returns:  smart plane entity  
        :rtype: :py:class:`NXOpen.Plane` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetContourFlag(self, showContour: bool) -> None:
        """
        Set the flag that turns on/off the visibility of Contour Curve 
        
        Signature ``SetContourFlag(showContour)`` 
        
        :param showContour:  false = Hide contour curve, true = Show contour curve  
        :type showContour: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetContourFlag(self) -> bool:
        """
        Get the flag that turns on/off the visibility of Contour Curve 
        
        Signature ``GetContourFlag()`` 
        
        :returns:  false = Hide contour curve, true = Show contour curve  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetMaterialType(self, matType: AeroFlangeBuilderMatType) -> None:
        """
        Set the material type of the flange 
        
        Signature ``SetMaterialType(matType)`` 
        
        :param matType:  material inside/material outside/bend outside  
        :type matType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderMatType` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetMaterialType(self) -> AeroFlangeBuilderMatType:
        """
        Get the material type of the flange 
        
        Signature ``GetMaterialType()`` 
        
        :returns:  material inside/material outside/bend outside  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderMatType` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def SetDimensionType(self, dimType: AeroFlangeBuilderDimType) -> None:
        """
        Set the length dimension type of the flange 
        
        Signature ``SetDimensionType(dimType)`` 
        
        :param dimType:  inside/outside  
        :type dimType: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderDimType` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def GetDimensionType(self) -> AeroFlangeBuilderDimType:
        """
        Get the length dimension type of the flange 
        
        Signature ``GetDimensionType()`` 
        
        :returns:  inside/outside  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilderDimType` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle expression.  
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns:   angle expression  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    BaseEdges: NXOpen.ScCollector = ...
    """
    Returns or sets  the base edge section object for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``BaseEdges`` 
    
    :returns:  Base Edges  
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``BaseEdges`` 
    
    :param baseEdges:  Base Edges  
    :type baseEdges: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    BendOptions: BendOptions = ...
    """
    Returns  the base edge section object for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendOptions`` 
    
    :returns:  Bend Options  
    :rtype: :py:class:`NXOpen.Features.SheetMetal.BendOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    RefFaces: NXOpen.ScCollector = ...
    """
    Returns or sets  the ref face smart collector object
    
    <hr>
    
    Getter Method
    
    Signature ``RefFaces`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    
    <hr>
    
    Setter Method
    
    Signature ``RefFaces`` 
    
    :param faceCollector: 
    :type faceCollector: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    """
    Null: AeroFlangeBuilder = ...  # unknown typename


class MultiFlange(NXOpen.Features.Feature):
    """
    Represents a multi flange feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Features.SheetMetal.MultiFlangeBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: MultiFlange = ...  # unknown typename


class ExportFlatPatternBuilderFileTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExportFlatPatternBuilderFileType():
    """
    Specifies the flat pattern export type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Dxf", "DXF Export"
       "TrumpfGeo", "Trumpf Geo Export"
    """
    Dxf = 0  # ExportFlatPatternBuilderFileTypeMemberType
    TrumpfGeo = 1  # ExportFlatPatternBuilderFileTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExportFlatPatternBuilderDxfRevisionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ExportFlatPatternBuilderDxfRevisionType():
    """
    Specifies the DXF Revisions for flat pattern export  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "R2005", " - "
       "R2004", " - "
       "R2000", " - "
       "R14", " - "
       "R2007", " - "
       "R20102012", " - "
       "R20132016", " - "
       "R12", " - "
       "R13", " - "
    """
    R2005 = 0  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R2004 = 1  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R2000 = 2  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R14 = 3  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R2007 = 4  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R20102012 = 5  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R20132016 = 6  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R12 = 7  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    R13 = 8  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ExportFlatPatternBuilder(NXOpen.Builder):
    """
    Represents a Export flat pattern builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateExportFlatPatternBuilder`
    
    Default values.
    
    ================  ======
    Property          Value
    ================  ======
    AddedBottom       false 
    ----------------  ------
    AddedTop          false 
    ----------------  ------
    BendDown          true 
    ----------------  ------
    BendTangent       false 
    ----------------  ------
    BendUp            true 
    ----------------  ------
    InteriorCutout    true 
    ----------------  ------
    InteriorFeature   false 
    ================  ======
    
    .. versionadded:: NX8.0.0
    """
    
    class FileType():
        """
        Specifies the flat pattern export type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Dxf", "DXF Export"
           "TrumpfGeo", "Trumpf Geo Export"
        """
        Dxf = 0  # ExportFlatPatternBuilderFileTypeMemberType
        TrumpfGeo = 1  # ExportFlatPatternBuilderFileTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DxfRevisionType():
        """
        Specifies the DXF Revisions for flat pattern export  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "R2005", " - "
           "R2004", " - "
           "R2000", " - "
           "R14", " - "
           "R2007", " - "
           "R20102012", " - "
           "R20132016", " - "
           "R12", " - "
           "R13", " - "
        """
        R2005 = 0  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R2004 = 1  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R2000 = 2  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R14 = 3  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R2007 = 4  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R20102012 = 5  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R20132016 = 6  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R12 = 7  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        R13 = 8  # ExportFlatPatternBuilderDxfRevisionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AddedBottom: bool = ...
    """
    Returns or sets  the option to export the added bottom geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``AddedBottom`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddedBottom`` 
    
    :param addedBottom: 
    :type addedBottom: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    AddedTop: bool = ...
    """
    Returns or sets  the option to export the added top geometry 
    
    <hr>
    
    Getter Method
    
    Signature ``AddedTop`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AddedTop`` 
    
    :param addedTop: 
    :type addedTop: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendDown: bool = ...
    """
    Returns or sets  the option to export the bend down center line 
    
    <hr>
    
    Getter Method
    
    Signature ``BendDown`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendDown`` 
    
    :param bendDown: 
    :type bendDown: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendTangent: bool = ...
    """
    Returns or sets  the option to export the bend tangent line 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTangent`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendTangent`` 
    
    :param bendTangent: 
    :type bendTangent: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    BendUp: bool = ...
    """
    Returns or sets  the option to export the bend up center line 
    
    <hr>
    
    Getter Method
    
    Signature ``BendUp`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BendUp`` 
    
    :param bendUp: 
    :type bendUp: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DeviationalTolerance: float = ...
    """
    Returns or sets  the deviational tolerance 
    
    <hr>
    
    Getter Method
    
    Signature ``DeviationalTolerance`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DeviationalTolerance`` 
    
    :param deviationalTolerance: 
    :type deviationalTolerance: float 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DxfRevision: ExportFlatPatternBuilderDxfRevisionType = ...
    """
    Returns or sets  the dxf revision.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilderDxfRevisionType`.
    
    <hr>
    
    Getter Method
    
    Signature ``DxfRevision`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilderDxfRevisionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``DxfRevision`` 
    
    :param dxfRevision: 
    :type dxfRevision: :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilderDxfRevisionType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    FlatPattern: NXOpen.Features.SelectFlatPattern = ...
    """
    Returns  the flat pattern feature 
    
    <hr>
    
    Getter Method
    
    Signature ``FlatPattern`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFlatPattern` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    """
    InnerMold: bool = ...
    """
    Returns or sets  the option to export the inner mold 
    
    Use this option only for the DXF type.
    
    <hr>
    
    Getter Method
    
    Signature ``InnerMold`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InnerMold`` 
    
    :param innerMold: 
    :type innerMold: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    InteriorCutout: bool = ...
    """
    Returns or sets  the option to export the interior cutout 
    
    <hr>
    
    Getter Method
    
    Signature ``InteriorCutout`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InteriorCutout`` 
    
    :param interiorCutout: 
    :type interiorCutout: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    InteriorFeature: bool = ...
    """
    Returns or sets  the option to export the interior feature 
    
    <hr>
    
    Getter Method
    
    Signature ``InteriorFeature`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InteriorFeature`` 
    
    :param interiorFeature: 
    :type interiorFeature: bool 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OuterMold: bool = ...
    """
    Returns or sets  the option to export the outer mold 
    
    Use this option only for the DXF type.
    
    <hr>
    
    Getter Method
    
    Signature ``OuterMold`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OuterMold`` 
    
    :param outerMold: 
    :type outerMold: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    OutputFile: str = ...
    """
    Returns or sets  the output file used to export flat pattern curves 
    
    <hr>
    
    Getter Method
    
    Signature ``OutputFile`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OutputFile`` 
    
    :param filename: 
    :type filename: str 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Type: ExportFlatPatternBuilderFileType = ...
    """
    Returns or sets  the type for the flat pattern export.  
    
    The options are in :py:meth:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilder.Type`. 
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilderFileType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.ExportFlatPatternBuilderFileType` 
    
    .. versionadded:: NX8.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: ExportFlatPatternBuilder = ...  # unknown typename


class FlangeBendPropertiesBuilderWidthOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBendPropertiesBuilderWidthOptions():
    """
    This enum defines the flange width options 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Full", " - "
       "AtCenter", " - "
       "AtEnd", " - "
       "FromEnd", " - "
       "FromBothEnds", " - "
    """
    Full = 0  # FlangeBendPropertiesBuilderWidthOptionsMemberType
    AtCenter = 1  # FlangeBendPropertiesBuilderWidthOptionsMemberType
    AtEnd = 2  # FlangeBendPropertiesBuilderWidthOptionsMemberType
    FromEnd = 3  # FlangeBendPropertiesBuilderWidthOptionsMemberType
    FromBothEnds = 4  # FlangeBendPropertiesBuilderWidthOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBendPropertiesBuilderLengthReferencesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBendPropertiesBuilderLengthReferences():
    """
    This enum defines the flange length dimension types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Inside", " - "
       "Outside", " - "
       "Web", " - "
    """
    Inside = 0  # FlangeBendPropertiesBuilderLengthReferencesMemberType
    Outside = 1  # FlangeBendPropertiesBuilderLengthReferencesMemberType
    Web = 2  # FlangeBendPropertiesBuilderLengthReferencesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBendPropertiesBuilderInsetsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FlangeBendPropertiesBuilderInsets():
    """
    This enum defines the material inset types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MaterialInside", " - "
       "MaterialOutside", " - "
       "BendOutside", " - "
    """
    MaterialInside = 0  # FlangeBendPropertiesBuilderInsetsMemberType
    MaterialOutside = 1  # FlangeBendPropertiesBuilderInsetsMemberType
    BendOutside = 2  # FlangeBendPropertiesBuilderInsetsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FlangeBendPropertiesBuilder(FeatureBendPropertiesBuilder):
    """
    Represents a Sheetmetal Flange Bend Properties builder class.  
    
    This builder is used to
    interrogate the flange bend properties in the list.
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.FlangeBendPropertiesListBuilder.CreateFlangeBendProperties`
    
    .. versionadded:: NX12.0.0
    """
    
    class WidthOptions():
        """
        This enum defines the flange width options 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Full", " - "
           "AtCenter", " - "
           "AtEnd", " - "
           "FromEnd", " - "
           "FromBothEnds", " - "
        """
        Full = 0  # FlangeBendPropertiesBuilderWidthOptionsMemberType
        AtCenter = 1  # FlangeBendPropertiesBuilderWidthOptionsMemberType
        AtEnd = 2  # FlangeBendPropertiesBuilderWidthOptionsMemberType
        FromEnd = 3  # FlangeBendPropertiesBuilderWidthOptionsMemberType
        FromBothEnds = 4  # FlangeBendPropertiesBuilderWidthOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LengthReferences():
        """
        This enum defines the flange length dimension types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Inside", " - "
           "Outside", " - "
           "Web", " - "
        """
        Inside = 0  # FlangeBendPropertiesBuilderLengthReferencesMemberType
        Outside = 1  # FlangeBendPropertiesBuilderLengthReferencesMemberType
        Web = 2  # FlangeBendPropertiesBuilderLengthReferencesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Insets():
        """
        This enum defines the material inset types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MaterialInside", " - "
           "MaterialOutside", " - "
           "BendOutside", " - "
        """
        MaterialInside = 0  # FlangeBendPropertiesBuilderInsetsMemberType
        MaterialOutside = 1  # FlangeBendPropertiesBuilderInsetsMemberType
        BendOutside = 2  # FlangeBendPropertiesBuilderInsetsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def DeleteFlangeBendProperties(self) -> None:
        """
        Create a flange properties.  
        
        Signature ``DeleteFlangeBendProperties()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    Angle: NXOpen.Expression = ...
    """
    Returns  the angle 
    
    <hr>
    
    Getter Method
    
    Signature ``Angle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Distance1: NXOpen.Expression = ...
    """
    Returns  the distance1 
    
    <hr>
    
    Getter Method
    
    Signature ``Distance1`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Distance2: NXOpen.Expression = ...
    """
    Returns  the distance2 
    
    <hr>
    
    Getter Method
    
    Signature ``Distance2`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Edges: NXOpen.ScCollector = ...
    """
    Returns  the base edge for the flange.  
    
    <hr>
    
    Getter Method
    
    Signature ``Edges`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ScCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Inset: FlangeBendPropertiesBuilderInsets = ...
    """
    Returns or sets  the inset 
    
    <hr>
    
    Getter Method
    
    Signature ``Inset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderInsets` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Inset`` 
    
    :param inset: 
    :type inset: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderInsets` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Length: NXOpen.Expression = ...
    """
    Returns  the length 
    
    <hr>
    
    Getter Method
    
    Signature ``Length`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    LengthReference: FlangeBendPropertiesBuilderLengthReferences = ...
    """
    Returns or sets  the length reference 
    
    <hr>
    
    Getter Method
    
    Signature ``LengthReference`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderLengthReferences` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LengthReference`` 
    
    :param lengthReference: 
    :type lengthReference: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderLengthReferences` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Miter: bool = ...
    """
    Returns or sets  the  option to specify behaviour of mirror/pattern of the flange
    
    <hr>
    
    Getter Method
    
    Signature ``Miter`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Miter`` 
    
    :param bMiter: 
    :type bMiter: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Offset: NXOpen.Expression = ...
    """
    Returns  the offset 
    
    <hr>
    
    Getter Method
    
    Signature ``Offset`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    Point: NXOpen.Point = ...
    """
    Returns or sets  the point 
    
    <hr>
    
    Getter Method
    
    Signature ``Point`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Point`` 
    
    :param point: 
    :type point: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    ReverseDirectionLength: bool = ...
    """
    Returns or sets  the reverse direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirectionLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirectionLength`` 
    
    :param reverseDirectionLength: 
    :type reverseDirectionLength: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    ReverseDirectionOffset: bool = ...
    """
    Returns or sets  the reverse direction 
    
    <hr>
    
    Getter Method
    
    Signature ``ReverseDirectionOffset`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ReverseDirectionOffset`` 
    
    :param reverseDirectionOffset: 
    :type reverseDirectionOffset: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    UseRecipe: bool = ...
    """
    Returns or sets  the  option to specify behaviour of mirror/pattern of the flange
    
    <hr>
    
    Getter Method
    
    Signature ``UseRecipe`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseRecipe`` 
    
    :param bUseRecipe: 
    :type bUseRecipe: bool 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Width: NXOpen.Expression = ...
    """
    Returns  the width 
    
    <hr>
    
    Getter Method
    
    Signature ``Width`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    """
    WidthOption: FlangeBendPropertiesBuilderWidthOptions = ...
    """
    Returns or sets  the width option 
    
    <hr>
    
    Getter Method
    
    Signature ``WidthOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderWidthOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WidthOption`` 
    
    :param widthOption: 
    :type widthOption: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilderWidthOptions` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
    """
    Null: FlangeBendPropertiesBuilder = ...  # unknown typename


class NormalCutoutBuilderDepthTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NormalCutoutBuilderDepthTypeOptions():
    """
    This enum represents the depth type for the normal cutout. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Finite", "Finite"
       "FromTo", "From To"
       "ThroughNext", "Though Next"
       "ThroughAll", "Through All"
    """
    Finite = 0  # NormalCutoutBuilderDepthTypeOptionsMemberType
    FromTo = 1  # NormalCutoutBuilderDepthTypeOptionsMemberType
    ThroughNext = 2  # NormalCutoutBuilderDepthTypeOptionsMemberType
    ThroughAll = 3  # NormalCutoutBuilderDepthTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalCutoutBuilderCutTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NormalCutoutBuilderCutTypeOptions():
    """
    This enum represents the cut type for the normal cutout. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "ThicknessCut", " - "
       "MidPlaneCut", " - "
       "NearestFaceCut", " - "
    """
    ThicknessCut = 0  # NormalCutoutBuilderCutTypeOptionsMemberType
    MidPlaneCut = 1  # NormalCutoutBuilderCutTypeOptionsMemberType
    NearestFaceCut = 2  # NormalCutoutBuilderCutTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalCutoutBuilderDepthSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NormalCutoutBuilderDepthSideOptions():
    """
    This enum represents the depth direction for the normal cutout. Not used if the normal cutout is from-to. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SectionNormalSide", "Material removed on the side of the section normal."
       "SectionReverseNormalSide", "Material removed on the side opposite to that of the section normal"
       "Symmetric", "Material removed in both directions equally. Only applies when the depth type is :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions.Finite <NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions>`."
    """
    SectionNormalSide = 0  # NormalCutoutBuilderDepthSideOptionsMemberType
    SectionReverseNormalSide = 1  # NormalCutoutBuilderDepthSideOptionsMemberType
    Symmetric = 2  # NormalCutoutBuilderDepthSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalCutoutBuilderSectionSideOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NormalCutoutBuilderSectionSideOptions():
    """
    This enum represents the side of the section that the normal cutout removes material. The "left" option
    represents the side to the left of a person who is walking along the section in the direction of its curves 
    when the section normal is pointing up. The "right" option represents the person's right hand side.
    This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point 
    along the section can also be represented by the vector resulting from the cross product of the curve tangent 
    (of the section curve at that point) and the section normal. The "left" side is the opposite. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Left", "Side pointed to by the inverse of the tangent cross normal vector"
       "Right", "Side pointed to by the tangent cross normal vector"
    """
    Left = 0  # NormalCutoutBuilderSectionSideOptionsMemberType
    Right = 1  # NormalCutoutBuilderSectionSideOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalCutoutBuilderTypeOptionsMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class NormalCutoutBuilderTypeOptions():
    """
    Represents the type of the normal cutout - sketch type OR 3D-curve type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SketchType", "Sketch type normal cutout"
       "NonPlanarCurveType", "3D curves type normal cutout"
    """
    SketchType = 0  # NormalCutoutBuilderTypeOptionsMemberType
    NonPlanarCurveType = 1  # NormalCutoutBuilderTypeOptionsMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class NormalCutoutBuilder(SheetmetalBaseBuilder):
    """
    Represents a NormalCutout feature builder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Features.SheetMetal.SheetmetalManager.CreateNormalCutoutFeatureBuilder`
    
    .. versionadded:: NX4.0.0
    """
    
    class DepthTypeOptions():
        """
        This enum represents the depth type for the normal cutout. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Finite", "Finite"
           "FromTo", "From To"
           "ThroughNext", "Though Next"
           "ThroughAll", "Through All"
        """
        Finite = 0  # NormalCutoutBuilderDepthTypeOptionsMemberType
        FromTo = 1  # NormalCutoutBuilderDepthTypeOptionsMemberType
        ThroughNext = 2  # NormalCutoutBuilderDepthTypeOptionsMemberType
        ThroughAll = 3  # NormalCutoutBuilderDepthTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class CutTypeOptions():
        """
        This enum represents the cut type for the normal cutout. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "ThicknessCut", " - "
           "MidPlaneCut", " - "
           "NearestFaceCut", " - "
        """
        ThicknessCut = 0  # NormalCutoutBuilderCutTypeOptionsMemberType
        MidPlaneCut = 1  # NormalCutoutBuilderCutTypeOptionsMemberType
        NearestFaceCut = 2  # NormalCutoutBuilderCutTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DepthSideOptions():
        """
        This enum represents the depth direction for the normal cutout. Not used if the normal cutout is from-to. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SectionNormalSide", "Material removed on the side of the section normal."
           "SectionReverseNormalSide", "Material removed on the side opposite to that of the section normal"
           "Symmetric", "Material removed in both directions equally. Only applies when the depth type is :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions.Finite <NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions>`."
        """
        SectionNormalSide = 0  # NormalCutoutBuilderDepthSideOptionsMemberType
        SectionReverseNormalSide = 1  # NormalCutoutBuilderDepthSideOptionsMemberType
        Symmetric = 2  # NormalCutoutBuilderDepthSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SectionSideOptions():
        """
        This enum represents the side of the section that the normal cutout removes material. The "left" option
        represents the side to the left of a person who is walking along the section in the direction of its curves 
        when the section normal is pointing up. The "right" option represents the person's right hand side.
        This interpretation is the same regardless of whether the section is open or closed. The "right" side at any point 
        along the section can also be represented by the vector resulting from the cross product of the curve tangent 
        (of the section curve at that point) and the section normal. The "left" side is the opposite. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Left", "Side pointed to by the inverse of the tangent cross normal vector"
           "Right", "Side pointed to by the tangent cross normal vector"
        """
        Left = 0  # NormalCutoutBuilderSectionSideOptionsMemberType
        Right = 1  # NormalCutoutBuilderSectionSideOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TypeOptions():
        """
        Represents the type of the normal cutout - sketch type OR 3D-curve type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SketchType", "Sketch type normal cutout"
           "NonPlanarCurveType", "3D curves type normal cutout"
        """
        SketchType = 0  # NormalCutoutBuilderTypeOptionsMemberType
        NonPlanarCurveType = 1  # NormalCutoutBuilderTypeOptionsMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetDepth(self, depth: str) -> None:
        """
        Signature ``SetDepth(depth)`` 
        
        :param depth: 
        :type depth: str 
        
        .. versionadded:: NX4.0.0
        
        .. deprecated::  NX10.0.0
           Use :py:meth:`NXOpen.Expression.RightHandSide` on the :py:class:`NXOpen.Expression` object returned from :py:meth:`NXOpen.Features.SheetMetal.NormalCutoutBuilder.Depth` instead.
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    
    def ValidateBuilderData(self) -> int:
        """
        Verify that the builder data is valid for creating a normal cutout.  
        
        If the builder data is valid, a value of 0 is returned.
        
        Signature ``ValidateBuilderData()`` 
        
        :returns:  data validity flag (zero is valid, non-zero is invalid). 
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
        """
        ...
    
    CutType: NormalCutoutBuilderCutTypeOptions = ...
    """
    Returns or sets  the cut type for the normal cutout.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderCutTypeOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``CutType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderCutTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``CutType`` 
    
    :param cutType: 
    :type cutType: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderCutTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Depth: NXOpen.Expression = ...
    """
    Returns  the depth of the cutout.  
    
    Only applies when the depth type is :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions.Finite <NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions>`.
    
    <hr>
    
    Getter Method
    
    Signature ``Depth`` 
    
    :returns:  The depth of the normal cutout  
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DepthSide: NormalCutoutBuilderDepthSideOptions = ...
    """
    Returns or sets  the depth side for the normal cutout.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthSideOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``DepthSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``DepthSide`` 
    
    :param depthSide: 
    :type depthSide: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    DepthType: NormalCutoutBuilderDepthTypeOptions = ...
    """
    Returns or sets  the depth type for the normal cutout.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``DepthType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``DepthType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    From: NXOpen.ISurface = ...
    """
    Returns or sets  the face or datum plane from which the cutout begins.  
    
    This is only applicable if the depth type
    is :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions.FromTo <NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions>` 
    
    <hr>
    
    Getter Method
    
    Signature ``From`` 
    
    :returns:  From face or datum plane  
    :rtype: :py:class:`NXOpen.ISurface` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``From`` 
    
    :param ffrom:  From face or datum plane  
    :type ffrom: :py:class:`NXOpen.ISurface` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Section: NXOpen.Section = ...
    """
    Returns or sets  the section used by the normal cutout.  
    
    It can be open or closed.
    
    <hr>
    
    Getter Method
    
    Signature ``Section`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Section`` 
    
    :param section: 
    :type section: :py:class:`NXOpen.Section` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    SectionSide: NormalCutoutBuilderSectionSideOptions = ...
    """
    Returns or sets  the side of the section that the normal cutout removes material.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderSectionSideOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``SectionSide`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``SectionSide`` 
    
    :param sectionSide: 
    :type sectionSide: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderSectionSideOptions` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Sketch: NXOpen.Features.SketchFeature = ...
    """
    Returns or sets  the internal sketch used by the normal cutout, if it exists.  
    
    <hr>
    
    Getter Method
    
    Signature ``Sketch`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Sketch`` 
    
    :param sketch: 
    :type sketch: :py:class:`NXOpen.Features.SketchFeature` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    TargetBody: NXOpen.Body = ...
    """
    Returns or sets  the target body on which the normal cutout is created.  
    
    <hr>
    
    Getter Method
    
    Signature ``TargetBody`` 
    
    :returns:  Returns the target body on which the normal cutout feature is created.  
    :rtype: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``TargetBody`` 
    
    :param targetBody:  A sheetmetal body on which normal cutout is to be created.  
    :type targetBody: :py:class:`NXOpen.Body` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    To: NXOpen.ISurface = ...
    """
    Returns or sets  the face or datum plane at which the cutout ends.  
    
    This is only applicable if the depth type
    is :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions.FromTo <NXOpen.Features.SheetMetal.NormalCutoutBuilderDepthTypeOptions>` 
    
    <hr>
    
    Getter Method
    
    Signature ``To`` 
    
    :returns:  To face or datum plane  
    :rtype: :py:class:`NXOpen.ISurface` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``To`` 
    
    :param to:  To face or datum plane  
    :type to: :py:class:`NXOpen.ISurface` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Type: NormalCutoutBuilderTypeOptions = ...
    """
    Returns or sets  the type for the normal cutout.  
    
    The options are in :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderTypeOptions`.
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderTypeOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.Features.SheetMetal.NormalCutoutBuilderTypeOptions` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB")
    """
    Null: NormalCutoutBuilder = ...  # unknown typename


class SheetmetalBendStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalBendState():
    """
    Bend State 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", " - "
       "Bent", " - "
       "Flat", " - "
    """
    Unknown = 0  # SheetmetalBendStateMemberType
    Bent = 1  # SheetmetalBendStateMemberType
    Flat = 2  # SheetmetalBendStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AdvancedFlange(NXOpen.Features.Feature):
    """
    Represents an advanced flange feature   
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Features.SheetMetal.AdvancedFlangeBuilder`
    
    .. versionadded:: NX11.0.0
    """
    Null: AdvancedFlange = ...  # unknown typename


class SheetmetalManagerTabTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SheetmetalManagerTabType():
    """
    This is the enum for Tab type i.e. base tab and secondary tab.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Base", "base tab"
       "Secondary", "secondary tab"
    """
    Base = 0  # SheetmetalManagerTabTypeMemberType
    Secondary = 1  # SheetmetalManagerTabTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AeroSheetmetalManager():
    """
    Provides methods for manipulating the Knowledge Fusion rules in a part   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Features.FeatureCollection`
    
    .. versionadded:: NX4.0.0
    """
    
    def CreateFlangeBuilder(self, aerosmFlange: NXOpen.Features.Feature) -> AeroFlangeBuilder:
        """
        Create flange builder 
        
        Signature ``CreateFlangeBuilder(aerosmFlange)`` 
        
        :param aerosmFlange:  :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilder`                                                  to be edited, if None  then create a new one  
        :type aerosmFlange: :py:class:`NXOpen.Features.Feature` 
        :returns:  AeroFlangeBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroFlangeBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateJoggleBuilder(self, aerosmJoggle: NXOpen.Features.Feature) -> AeroJoggleBuilder:
        """
        Create joggle builder 
        
        Signature ``CreateJoggleBuilder(aerosmJoggle)`` 
        
        :param aerosmJoggle:  :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilder`                                                  to be edited, if None  then create a new one  
        :type aerosmJoggle: :py:class:`NXOpen.Features.Feature` 
        :returns:  AeroJoggleBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroJoggleBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateUnformBuilder(self, aerosmUnform: NXOpen.Features.Feature) -> AeroUnformBuilder:
        """
        Create unform builder 
        
        Signature ``CreateUnformBuilder(aerosmUnform)`` 
        
        :param aerosmUnform:  :py:class:`NXOpen.Features.SheetMetal.AeroUnformBuilder`                                                  to be edited, if None  then create a new one  
        :type aerosmUnform: :py:class:`NXOpen.Features.Feature` 
        :returns:  AeroUnformBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroUnformBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateReformBuilder(self, aerosmReform: NXOpen.Features.Feature) -> AeroReformBuilder:
        """
        Create reform builder 
        
        Signature ``CreateReformBuilder(aerosmReform)`` 
        
        :param aerosmReform:  :py:class:`NXOpen.Features.SheetMetal.AeroReformBuilder`                                                  to be edited, if None  then create a new one  
        :type aerosmReform: :py:class:`NXOpen.Features.Feature` 
        :returns:  AeroReformBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroReformBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateFlatSolidBuilder(self, aerosmUnform: NXOpen.Features.Feature) -> FlatSolidBuilder:
        """
        Create flat solid builder 
        
        Signature ``CreateFlatSolidBuilder(aerosmUnform)`` 
        
        :param aerosmUnform:  :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilder`                                                  to be edited, if None  then create a new one  
        :type aerosmUnform: :py:class:`NXOpen.Features.Feature` 
        :returns:  FlatSolidBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatSolidBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateAeroLighteningCutoutBuilder(self, aeroLighteningCutout: NXOpen.Features.Feature) -> AeroLighteningCutoutBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilder`  
        
        Signature ``CreateAeroLighteningCutoutBuilder(aeroLighteningCutout)`` 
        
        :param aeroLighteningCutout:  :py:class:`NXOpen.Features.Feature` to be edited  
        :type aeroLighteningCutout: :py:class:`NXOpen.Features.Feature` 
        :returns:  AeroLighteningCutoutBuilder object 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.AeroLighteningCutoutBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    
    
    def CreateFlatPatternBuilder(self, aerosmUnform: NXOpen.Features.Feature) -> FlatPatternBuilder:
        """
        Creates a :py:class:`NXOpen.Features.SheetMetal.FlatPatternBuilder`  
        
        Signature ``CreateFlatPatternBuilder(aerosmUnform)`` 
        
        :param aerosmUnform:  :py:class:`NXOpen.Features.Feature`                                                                            to be edited, if None  then create a new one  
        :type aerosmUnform: :py:class:`NXOpen.Features.Feature` 
        :returns:  FlatPatternBuilder object  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlatPatternBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
        """
        ...
    


class FlangeBendPropertiesListBuilder(FeatureBendPropertiesListBuilder):
    """
    Represents a Sheetmetal Feature properties List builder class.  
    
    This builder is used to
    interrogate the feature properties list.
    
    .. versionadded:: NX12.0.0
    """
    
    def CreateFlangeBendProperties(self) -> FlangeBendPropertiesBuilder:
        """
        Create a flange properties.  
        
        Signature ``CreateFlangeBendProperties()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FlangeBendPropertiesBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    Null: FlangeBendPropertiesListBuilder = ...  # unknown typename


class FeatureBendPropertiesBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[FeatureBendPropertiesBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: FeatureBendPropertiesBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
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
    
    
    def FindIndex(self, obj: FeatureBendPropertiesBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> FeatureBendPropertiesBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
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
    def Erase(self, obj: FeatureBendPropertiesBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: FeatureBendPropertiesBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
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
    
    
    def GetContents(self) -> 'list[FeatureBendPropertiesBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[FeatureBendPropertiesBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
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
    def Swap(self, object1: FeatureBendPropertiesBuilder, object2: FeatureBendPropertiesBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: FeatureBendPropertiesBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.Features.SheetMetal.FeatureBendPropertiesBuilder` 
        
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
    Null: FeatureBendPropertiesBuilderList = ...  # unknown typename


