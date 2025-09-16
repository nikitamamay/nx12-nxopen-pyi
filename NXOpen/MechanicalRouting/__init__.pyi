# module 'NXOpen.MechanicalRouting'
#
# Automatically generated 2025-06-09T14:38:46.887653
#
"""Default documentation for NXOpen.MechanicalRouting."""

import typing

import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
import NXOpen.PDM
import NXOpen.Placement
import NXOpen.Routing



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class BaseCornerTypeBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Builder class for Base Corner Types   
    
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
    
    Null: BaseCornerTypeBuilder = ...  # unknown typename


class DynamicCutElbowBehaviorBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.DynamicCutElbowBehaviorBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateDynamicCutElbowBehaviorBuilder`
    
    .. versionadded:: NX12.0.0
    """
    
    def SetModelElementRevision(self, modelElementRevision: NXOpen.PDM.ModelElementRevision) -> None:
        """
        Sets :py:class:`NXOpen.PDM.ModelElementRevision` of Routing Reuse type.  
        
        Raise an error if passed
        other type of object. 
        
        Signature ``SetModelElementRevision(modelElementRevision)`` 
        
        :param modelElementRevision: 
        :type modelElementRevision: :py:class:`NXOpen.PDM.ModelElementRevision` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetLockedCutElbow(self, lockState: bool) -> None:
        """
        Sets true to  define the locked state for dynamic behavior.  
        
        If set false this will have the dynamic behavior.
        If the current model design element is not a cut elbow this will will be ignored. 
        
        Signature ``SetLockedCutElbow(lockState)`` 
        
        :param lockState: 
        :type lockState: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def IsLockedCutElbow(self) -> bool:
        """
        Returns true if the current model element is Cut Elbow and is Locked State for Dynamic behavior for Cut Elbow.  
        
        Signature ``IsLockedCutElbow()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    Null: DynamicCutElbowBehaviorBuilder = ...  # unknown typename


class EditPointBuilderMotiontypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EditPointBuilderMotiontype():
    """
    Specifies the options available for motion. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "MovePoint", "Move Point Motion"
       "EditSegment", "Edit Segment Motion"
    """
    MovePoint = 0  # EditPointBuilderMotiontypeMemberType
    EditSegment = 1  # EditPointBuilderMotiontypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EditPointBuilderEditsegmenttypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class EditPointBuilderEditsegmenttype():
    """
    Specifies the options available for Edit Segment motion. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "Move Point Motion"
       "Length", "Edit length type in Edit Segment Motion"
       "Angle", "Edit angle type in Edit Segment Motion"
    """
    NotSet = 0  # EditPointBuilderEditsegmenttypeMemberType
    Length = 1  # EditPointBuilderEditsegmenttypeMemberType
    Angle = 2  # EditPointBuilderEditsegmenttypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class EditPointBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.EditPointBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateEditPointBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class Motiontype():
        """
        Specifies the options available for motion. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "MovePoint", "Move Point Motion"
           "EditSegment", "Edit Segment Motion"
        """
        MovePoint = 0  # EditPointBuilderMotiontypeMemberType
        EditSegment = 1  # EditPointBuilderMotiontypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Editsegmenttype():
        """
        Specifies the options available for Edit Segment motion. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "Move Point Motion"
           "Length", "Edit length type in Edit Segment Motion"
           "Angle", "Edit angle type in Edit Segment Motion"
        """
        NotSet = 0  # EditPointBuilderEditsegmenttypeMemberType
        Length = 1  # EditPointBuilderEditsegmenttypeMemberType
        Angle = 2  # EditPointBuilderEditsegmenttypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def StartDrag(self) -> None:
        """
        Begin a drag operation.  
        
        Creates a constraint network of routing objects connected to the routing object that is being edited.
        
        Signature ``StartDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def DragObjects(self) -> None:
        """
        Perform a drag operation.  
        
        Solves the constraint network applying the transform required to move the routing object to a new position.
        
        Signature ``DragObjects()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def StopDrag(self) -> None:
        """
        End a drag operation 
        
        Applies the transforms obtained from solving the constraint network on routing objects.  
        
        Signature ``StopDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ResetDrag(self) -> None:
        """
        Reset a drag operation 
        
        Resets the position of routing objects in constraint network back to their initial position.  
        
        Signature ``ResetDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    ActiveEditSegmentType: EditPointBuilderEditsegmenttype = ...
    """
    Returns or sets  the edit segment type setting             
    Allows you to specify the type of edit in edit segment motion.  
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveEditSegmentType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.EditPointBuilderEditsegmenttype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveEditSegmentType`` 
    
    :param editSegmentType: 
    :type editSegmentType: :py:class:`NXOpen.MechanicalRouting.EditPointBuilderEditsegmenttype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    ActiveMotionType: EditPointBuilderMotiontype = ...
    """
    Returns or sets  the motion type setting.  
    
    Allows you to specify the type of edit point motion to be applied. 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveMotionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.EditPointBuilderMotiontype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveMotionType`` 
    
    :param motionType: 
    :type motionType: :py:class:`NXOpen.MechanicalRouting.EditPointBuilderMotiontype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    BendAngle: float = ...
    """
    Returns or sets  the bend angle setting.  
    
    Allows you to specify new angle for a segment connected at the RCP or Port being edited. Reference
    for angle measurement is the other segment connected at the RCP or Port being edited.
    
    Is applicable only when there are two segments connected at RCP or Port being edited. 
    
    <hr>
    
    Getter Method
    
    Signature ``BendAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``BendAngle`` 
    
    :param bendAngle: 
    :type bendAngle: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    IsDetachObject: bool = ...
    """
    Returns or sets  the detach setting.  
    
    Allows you to specify if the selected object has to be detached from the segment during transformation. 
    
    <hr>
    
    Getter Method
    
    Signature ``IsDetachObject`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``IsDetachObject`` 
    
    :param isDetachObject: 
    :type isDetachObject: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    MaintainAngle: bool = ...
    """
    Returns or sets  the maintain angle setting.  
    
    Allows you to specify if the angles between segments connected at the RCP or Port being edited must be fixed
    during transformation. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaintainAngle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MaintainAngle`` 
    
    :param maintainAngle: 
    :type maintainAngle: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    MaintainLength: bool = ...
    """
    Returns or sets  the maintain length setting.  
    
    Allows you to specify if the lengths of segments connected at the RCP or Port being edited must be fixed
    during transformation. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaintainLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MaintainLength`` 
    
    :param maintainLength: 
    :type maintainLength: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    PointSelection: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing objects that are being edited.  
    
    The object can be a Routing Control Point 
    or routing port or one of their occurences. 
    
    <hr>
    
    Getter Method
    
    Signature ``PointSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Segment: NXOpen.Line = ...
    """
    Returns or sets  the segment setting.  
    
    Allows you to specify a segment connected at the RCP or Port being edited.
    
    <hr>
    
    Getter Method
    
    Signature ``Segment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Line` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Segment`` 
    
    :param segment: 
    :type segment: :py:class:`NXOpen.Line` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SegmentLength: float = ...
    """
    Returns or sets  the segment length setting.  
    
    Allows you to specify new length for a segment connected at the RCP or Port being edited. 
    
    New length is applied on the segment by moving the RCP or Port being edited. 
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentLength`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SegmentLength`` 
    
    :param segmentLength: 
    :type segmentLength: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    TransformTool: TransformBlockBuilder = ...
    """
    Returns  the transform tool.  
    
    Allows you to access the transform block object.
    
    <hr>
    
    Getter Method
    
    Signature ``TransformTool`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: EditPointBuilder = ...  # unknown typename


class MergeBuilder(NXOpen.Builder):
    """
    the Builder to Merge Component   
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateMergeBuilder`
    
    .. versionadded:: NX11.0.1
    """
    CandidateStockComponentCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing component collector that collects candidate stock component to merge with target component 
    
    <hr>
    
    Getter Method
    
    Signature ``CandidateStockComponentCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    SimplifyPath: bool = ...
    """
    Returns or sets  the simplify path setting 
    
    <hr>
    
    Getter Method
    
    Signature ``SimplifyPath`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SimplifyPath`` 
    
    :param simplifyPath: 
    :type simplifyPath: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    TargetStockComponentCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing component collector that collects target stock component 
    
    <hr>
    
    Getter Method
    
    Signature ``TargetStockComponentCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: MergeBuilder = ...  # unknown typename


class CornerBuilderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class CornerBuilderType():
    """
    Corner Types available. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "None, no corner created"
       "Bend", "allows corner creation with the specified bend type"
       "Miter", "allows miter corner creation"
    """
    NotSet = 0  # CornerBuilderTypeMemberType
    Bend = 1  # CornerBuilderTypeMemberType
    Miter = 2  # CornerBuilderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CornerBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Builder class for Corner Block   
    
    .. versionadded:: NX11.0.1
    """
    
    class Type():
        """
        Corner Types available. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "None, no corner created"
           "Bend", "allows corner creation with the specified bend type"
           "Miter", "allows miter corner creation"
        """
        NotSet = 0  # CornerBuilderTypeMemberType
        Bend = 1  # CornerBuilderTypeMemberType
        Miter = 2  # CornerBuilderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
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
    
    BendCornerSettings: BendCornerTypeBuilder = ...
    """
    Returns  the bend corner block 
    
    <hr>
    
    Getter Method
    
    Signature ``BendCornerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.BendCornerTypeBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    CornerType: CornerBuilderType = ...
    """
    Returns or sets  the corner types 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.CornerBuilderType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CornerType`` 
    
    :param cornerType: 
    :type cornerType: :py:class:`NXOpen.MechanicalRouting.CornerBuilderType` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: CornerBuilder = ...  # unknown typename


class SplitBuilder(NXOpen.Builder):
    """
    the Builder to Assign Discontinuity for the stocks   
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateSplitBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def GetCreatedComponents(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Components created during Split operation.  
        
        Signature ``GetCreatedComponents()`` 
        
        :returns:  Components created during Split operation.  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def PreCommit(self) -> None:
        """
        Performs the operations needed prior to a commit.  
        
        This method has to be called before invoking commit. 
        
        Signature ``PreCommit()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject`s that represent content that will be created by this builder.  
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    ControlPointCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the Rcp type of the selected object  
    
    <hr>
    
    Getter Method
    
    Signature ``ControlPointCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: SplitBuilder = ...  # unknown typename


class PipingComponentFileBuilder(NXOpen.Builder):
    """
    the Builder for PipingComponentFile data  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreatePipingComponentFileBuilder`
    
    .. versionadded:: NX12.0.0
    """
    ComponentsCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the selected components  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: routing_pipetube ("Routing Piping and Tubing")
    """
    PcfFileName: str = ...
    """
    Returns or sets  the pcf file name.  
    
    <hr>
    
    Getter Method
    
    Signature ``PcfFileName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: routing_pipetube ("Routing Piping and Tubing")
    
    <hr>
    
    Setter Method
    
    Signature ``PcfFileName`` 
    
    :param fileName: 
    :type fileName: str 
    
    .. versionadded:: NX12.0.0
    
    License requirements: routing_pipetube ("Routing Piping and Tubing")
    """
    Null: PipingComponentFileBuilder = ...  # unknown typename


class PathTransitionListManagerBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.PathTransitionListManagerBuilder`.  
    
    Allows the user to create a routing path defined by path points and transitions.
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.CreatePathBuilder.CreatePathTransitionManagerBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def CreatePathTransitionBuilder(self, part: NXOpen.Part) -> PathTransitionBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` object.  
        
        Signature ``CreatePathTransitionBuilder(part)`` 
        
        :param part: 
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    PathTransitionBuilderList: PathTransitionBuilderList = ...
    """
    Returns  the list of path transition builders that describe the path.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathTransitionBuilderList`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: PathTransitionListManagerBuilder = ...  # unknown typename


class LogicalDesignServiceMappingStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LogicalDesignServiceMappingStatus():
    """
    The status returned from checking the logical design mapping to physical design. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Pass", " - "
       "OutOfDate", " - "
       "Unloaded", " - "
       "Fail", " - "
       "Unknown", " - "
    """
    Pass = 0  # LogicalDesignServiceMappingStatusMemberType
    OutOfDate = 1  # LogicalDesignServiceMappingStatusMemberType
    Unloaded = 2  # LogicalDesignServiceMappingStatusMemberType
    Fail = 3  # LogicalDesignServiceMappingStatusMemberType
    Unknown = 4  # LogicalDesignServiceMappingStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LogicalDesignService():
    """
    Represents a :py:class:`NXOpen.MechanicalRouting.LogicalDesignService` object.  
    
    Uses the :py:meth:`MechanicalRouting.RoutingManager.LogicalDesignService` to obtain
    an instance of this class.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.MechanicalRouting.RoutingManager`
    
    .. versionadded:: NX11.0.0
    """
    
    class MappingStatus():
        """
        The status returned from checking the logical design mapping to physical design. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Pass", " - "
           "OutOfDate", " - "
           "Unloaded", " - "
           "Fail", " - "
           "Unknown", " - "
        """
        Pass = 0  # LogicalDesignServiceMappingStatusMemberType
        OutOfDate = 1  # LogicalDesignServiceMappingStatusMemberType
        Unloaded = 2  # LogicalDesignServiceMappingStatusMemberType
        Fail = 3  # LogicalDesignServiceMappingStatusMemberType
        Unknown = 4  # LogicalDesignServiceMappingStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Assign3DPortToLogicalPort(self, logicalPort: NXOpen.NXObject, physicalPort: NXOpen.Routing.Port) -> None:
        """
        Assigns a 3D :py:class:`Routing.Port` mapping to a logical port object.  
        
        Signature ``Assign3DPortToLogicalPort(logicalPort, physicalPort)`` 
        
        :param logicalPort:  The logical port. 
        :type logicalPort: :py:class:`NXOpen.NXObject` 
        :param physicalPort:  The 3D port.  
        :type physicalPort: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def Unassign3DPortsFromLogicalPort(self, container: NXOpen.Assemblies.Component, logicalPort: NXOpen.NXObject) -> None:
        """
        Unassigns the 3D ports from the logical port object.  
        
        Signature ``Unassign3DPortsFromLogicalPort(container, logicalPort)`` 
        
        :param container:  The component of the subset in the workset.  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param logicalPort:  The logical port. 
        :type logicalPort: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetMappingStatus(self, routingObject: NXOpen.NXObject, container: NXOpen.Assemblies.Component) -> LogicalDesignServiceMappingStatus:
        """
        Returns the mapping status from the logical design to physical design.  
        
        Signature ``GetMappingStatus(routingObject, container)`` 
        
        :param routingObject: 
        :type routingObject: :py:class:`NXOpen.NXObject` 
        :param container: 
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.LogicalDesignServiceMappingStatus` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetMappingStatusMessage(self, routingObject: NXOpen.NXObject, container: NXOpen.Assemblies.Component) -> str:
        """
        Returns the mapping status message from logical design to physical design.  
        
        Signature ``GetMappingStatusMessage(routingObject, container)`` 
        
        :param routingObject: 
        :type routingObject: :py:class:`NXOpen.NXObject` 
        :param container: 
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def AssignComponentsToLogicalConnection(self, components: 'list[NXOpen.Assemblies.Component]', logicalConnection: NXOpen.NXObject) -> None:
        """
        Assigns a list of :py:class:`Assemblies.Component` mapping to a logical connection object.  
        
        Signature ``AssignComponentsToLogicalConnection(components, logicalConnection)`` 
        
        :param components:  A list of Components to assign to the logical connection.  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param logicalConnection:  The logical connection object.  
        :type logicalConnection: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def UnassignComponentsToLogicalConnection(self, container: NXOpen.Assemblies.Component, logicalConnection: NXOpen.NXObject) -> None:
        """
        Unassigns all the components currently assigned to this logical connection object.  
        
        Signature ``UnassignComponentsToLogicalConnection(container, logicalConnection)`` 
        
        :param container:  A component that represents the container that holds the Routing design. E.g, a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param logicalConnection:  The logical connection object. 
        :type logicalConnection: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def AssignComponentToLogicalEquipment(self, logicalEquipment: NXOpen.NXObject, component: NXOpen.Assemblies.Component) -> None:
        """
        Assigns a component :py:class:`Assemblies.Component` to a logical equipment object.  
        
        Signature ``AssignComponentToLogicalEquipment(logicalEquipment, component)`` 
        
        :param logicalEquipment:  The logical equipment object. 
        :type logicalEquipment: :py:class:`NXOpen.NXObject` 
        :param component:  The :py:class:`Assemblies.Component` represents a 3D routing equipment.  
        :type component: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def UnassignComponentToLogicalEquipment(self, container: NXOpen.Assemblies.Component, logicalEquipment: NXOpen.NXObject) -> None:
        """
        Unassigns all the components that are currently assigned to the given logical equipment object.  
        
        Signature ``UnassignComponentToLogicalEquipment(container, logicalEquipment)`` 
        
        :param container:  A component that represents the container that holds the Routing design  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param logicalEquipment:  The logical equipment object. 
        :type logicalEquipment: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetRunsInContainer(self, container: NXOpen.Assemblies.Component) -> 'list[NXOpen.NXObject]':
        """
        Gets the :py:class:`NXOpen.PLAS.Run`s that are included in a given :py:class:`Assemblies.Component` that represents a container for the Routing design, such as a subset in a workset  
        
        Signature ``GetRunsInContainer(container)`` 
        
        :param container:  A component that represents the container that holds the Routing design, such as a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The Runs included in the container  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def MakeRunActive(self, container: NXOpen.Assemblies.Component, run: NXOpen.NXObject) -> None:
        """
        Makes a :py:class:`NXOpen.PLAS.Run` active in given :py:class:`Assemblies.Component` that represents a container for the Routing design, such as a subset in Workset 
        
        Signature ``MakeRunActive(container, run)`` 
        
        :param container:  A component that represents the container that holds the Routing design, such as a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param run:  The Run that needs to be made active  
        :type run: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetActiveRun(self, container: NXOpen.Assemblies.Component) -> NXOpen.NXObject:
        """
        Gets a :py:class:`NXOpen.PLAS.Run` that is currently active in given :py:class:`Assemblies.Component` that represents a container for the Routing design, such as a subset in a workset  
        
        Signature ``GetActiveRun(container)`` 
        
        :param container:  A component that represents the container that holds the Routing design such as a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :returns:  The currently active Run.  
        
        Can be null if no active Run is present  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def EnsureLogicalModelIsLoaded(self, container: NXOpen.Assemblies.Component) -> None:
        """
        Ensures that the logical model is loaded for all the Runs included in the given :py:class:`Assemblies.Component` that represents a container for the Routing design, such as a subset in a workset 
        
        Signature ``EnsureLogicalModelIsLoaded(container)`` 
        
        :param container:  A component that represents the container that holds the Routing design such as a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ReassignComponentsFromLogicalConnection(self, container: NXOpen.Assemblies.Component, sourceLogicalConnection: NXOpen.NXObject, destinationObject: NXOpen.NXObject) -> None:
        """
        Reassigns all the components from a source logical connection object to a destination logical connection object or run object.  
        
        Signature ``ReassignComponentsFromLogicalConnection(container, sourceLogicalConnection, destinationObject)`` 
        
        :param container:  The component of the subset in the workset.  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param sourceLogicalConnection:  The source logical connection object. 
        :type sourceLogicalConnection: :py:class:`NXOpen.NXObject` 
        :param destinationObject:  The destination logical connection object or run object. 
        :type destinationObject: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ReassignComponentsToRun(self, components: 'list[NXOpen.Assemblies.Component]', run: NXOpen.NXObject) -> None:
        """
        Reassigns a list of :py:class:`Assemblies.Component` mapping to a destination run object.  
        
        Signature ``ReassignComponentsToRun(components, run)`` 
        
        :param components:  A list of Components to reassign to the run.  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :param run:  The run object.  
        :type run: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def DeleteRuns(self, runs: 'list[NXOpen.NXObject]') -> None:
        """
        Deletes run objects.  
        
        NOTE: only the empty run object can be deleted.
        
        Signature ``DeleteRuns(runs)`` 
        
        :param runs:  The run objects.  
        :type runs: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def LoadAllComponents(self, run: NXOpen.NXObject) -> None:
        """
        Adds a :py:class:`NXOpen.PLAS.Run` in :py:class:`Assemblies.Subset` which is currently set as work part.  
        
        Signature ``LoadAllComponents(run)`` 
        
        :param run:  The Run that needs to be added in subset  
        :type run: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def IsRunIncludedInSubset(self, container: NXOpen.Assemblies.Component, run: NXOpen.NXObject) -> bool:
        """
        Returns true if the supplied :py:class:`NXOpen.PLAS.Run` is included in given :py:class:`Assemblies.Component` that represents a container for the Routing design, such as a subset in Workset  
        
        Signature ``IsRunIncludedInSubset(container, run)`` 
        
        :param container:  A component that represents the container that holds the Routing design, such as a subset in a workset  
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :param run:  The Run that needs to be check whether it is in subset or not  
        :type run: :py:class:`NXOpen.NXObject` 
        :returns:  The logical will be true if supplied run is fully loaded in subset  
        :rtype: bool 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    


class BulkReplacementBuilder(NXOpen.Routing.BulkReplacementBuilder):
    """
    Builder class for Bulk Replacement which manages replacement operations on design elements   
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateBulkReplacementBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: BulkReplacementBuilder = ...  # unknown typename


class BuilderFactory():
    """
    Represents an :py:class:`NXOpen.MechanicalRouting.BuilderFactory` object.  
    
    Use this object 
    to create specific routing mechanical builders.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.MechanicalRouting.RoutingManager`
    
    .. versionadded:: NX11.0.0
    """
    
    def CreateEditPointBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EditPointBuilder:
        """
        Create a :py:class:`NXOpen.MechanicalRouting.EditPointBuilder` object.  
        
        Signature ``CreateEditPointBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which edit point is being performed. It can be passed as null tag when not working in context.  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.EditPointBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreatePartPlacementBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> PartPlacementBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilder` object.  
        
        Signature ``CreatePartPlacementBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which placement is being performed. It can be passed as null tag when not working in context.  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateEditPlacementBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EditPlacementBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.EditPlacementBuilder` object.  
        
        Signature ``CreateEditPlacementBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which edit is being performed. It can be passed as null tag when not working in context.  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.EditPlacementBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateManageInlineBehaviorBuilder(self, part: NXOpen.Part) -> ManageInlineBehaviorBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.ManageInlineBehaviorBuilder` object.  
        
        Signature ``CreateManageInlineBehaviorBuilder(part)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.ManageInlineBehaviorBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateMovePathBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> MovePathBuilder:
        """
        Create a :py:class:`NXOpen.MechanicalRouting.MovePathBuilder` object.  
        
        Signature ``CreateMovePathBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which move is performed. Can be None when work part is same as displayed part  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.MovePathBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateCreatePathBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> CreatePathBuilder:
        """
        Create a :py:class:`NXOpen.MechanicalRouting.CreatePathBuilder` object.  
        
        Signature ``CreateCreatePathBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which stock is being created  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.CreatePathBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateStockBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, segmentsOrStocks: 'list[NXOpen.NXObject]') -> StockBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.StockBuilder` object.  
        
        Signature ``CreateStockBuilder(part, workOcc, segmentsOrStocks)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which stock is being created  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :param segmentsOrStocks:  Occurrences of Routing segments to assign                                                                                                    stock to or stock to be edited  
        :type segmentsOrStocks: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.StockBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateSplitBuilder(self, part: NXOpen.Part, controlPoints: 'list[NXOpen.Routing.ControlPoint]') -> SplitBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.SplitBuilder` object.  
        
        Signature ``CreateSplitBuilder(part, controlPoints)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param controlPoints:  selected Control Points for split stock components  
        :type controlPoints: list of :py:class:`NXOpen.Routing.ControlPoint` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.SplitBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateTransformBlockBuilder(self, part: NXOpen.Part) -> TransformBlockBuilder:
        """
        Create a :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilder` object.  
        
        Signature ``CreateTransformBlockBuilder(part)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateInsulationBuilder(self, part: NXOpen.Part, insulationPartOccurrence: NXOpen.Assemblies.Component) -> InsulationBuilder:
        """
        Create a :py:class:`NXOpen.MechanicalRouting.InsulationBuilder` object.  
        
        Signature ``CreateInsulationBuilder(part, insulationPartOccurrence)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param insulationPartOccurrence: 
        :type insulationPartOccurrence: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.InsulationBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_advanced ("Routing Advanced")
        """
        ...
    
    
    def CreateAssignCornerBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> AssignCornerBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.AssignCornerBuilder` object.  
        
        Signature ``CreateAssignCornerBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which bend is being created. It can be passed as null tag when not working in context.  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.AssignCornerBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateMergeBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> MergeBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.MergeBuilder` object.  
        
        Signature ``CreateMergeBuilder(part, workOcc)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which merge stock is being performed. It can be passed as null tag when not working in context.  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.MergeBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateConnectBuilder(self, part: NXOpen.Part, components: 'list[NXOpen.Assemblies.Component]') -> ConnectBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.ConnectBuilder` object.  
        
        Signature ``CreateConnectBuilder(part, components)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param components:  selected Components for Connect Path  
        :type components: list of :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.ConnectBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreateDynamicCutElbowBehaviorBuilder(self, part: NXOpen.Part) -> DynamicCutElbowBehaviorBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.DynamicCutElbowBehaviorBuilder` object.  
        
        Signature ``CreateDynamicCutElbowBehaviorBuilder(part)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.DynamicCutElbowBehaviorBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreatePipingComponentFileBuilder(self, part: NXOpen.Part) -> PipingComponentFileBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.PipingComponentFileBuilder` object.  
        
        Signature ``CreatePipingComponentFileBuilder(part)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.PipingComponentFileBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_pipetube ("Routing Piping and Tubing")
        """
        ...
    
    
    def CreateBulkReplacementBuilder(self, part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, segmentsOrStocks: 'list[NXOpen.NXObject]') -> BulkReplacementBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.BulkReplacementBuilder` object.  
        
        Signature ``CreateBulkReplacementBuilder(part, workOcc, segmentsOrStocks)`` 
        
        :param part:  the part associated with the builder. Cannot be None.  
        :type part: :py:class:`NXOpen.Part` 
        :param workOcc:  the container component within which stock is being created  
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :param segmentsOrStocks:  Occurrences of Routing segments to assign                                                                                                    stock to or stock to be edited  
        :type segmentsOrStocks: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.BulkReplacementBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    


class CreatePathBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.CreatePathBuilder`.  
    
    Allows the user to create 
    routing path.
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateCreatePathBuilder`
    
    Default values.
    
    ======================================================  ======================================
    Property                                                Value
    ======================================================  ======================================
    BendCornerSettings.Method (deprecated)                  Radius 
    ------------------------------------------------------  --------------------------------------
    BendCornerSettings.Radius.Value (deprecated)            0 (millimeters part), 0 (inches part) 
    ------------------------------------------------------  --------------------------------------
    BendCornerSettings.RatioToDiameter.Value (deprecated)   0 (millimeters part), 0 (inches part) 
    ------------------------------------------------------  --------------------------------------
    CornerSettings.CornerType                               None 
    ======================================================  ======================================
    
    .. versionadded:: NX11.0.0
    """
    
    def CreatePathTransitionManagerBuilder(self, workPart: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, displayPart: NXOpen.Part) -> PathTransitionListManagerBuilder:
        """
        Creates a :py:class:`NXOpen.MechanicalRouting.PathTransitionListManagerBuilder` object.  
        
        Signature ``CreatePathTransitionManagerBuilder(workPart, workOcc, displayPart)`` 
        
        :param workPart: 
        :type workPart: :py:class:`NXOpen.Part` 
        :param workOcc: 
        :type workOcc: :py:class:`NXOpen.Assemblies.Component` 
        :param displayPart: 
        :type displayPart: :py:class:`NXOpen.Part` 
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionListManagerBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def PreCommit(self) -> None:
        """
        Performs the operations needed prior to a commit.  
        
        This method has to be called before invoking commit. 
        
        Signature ``PreCommit()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject`s that represent the content that will be created by this builder.  
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    BendCornerSettings: BendCornerTypeBuilder = ...
    """
    Returns  the builder to assign corners to the routing path.  
    
    <hr>
    
    Getter Method
    
    Signature ``BendCornerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.BendCornerTypeBuilder` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.CreatePathBuilder.CornerSettings` instead.
    
    License requirements: routing_base ("Routing Basic")
    """
    CornerSettings: CornerBuilder = ...
    """
    Returns  the builder to assign corners to the routing path.  
    
    <hr>
    
    Getter Method
    
    Signature ``CornerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.CornerBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    PathTransitionListManagerBuilder: PathTransitionListManagerBuilder = ...
    """
    Returns  the builder for managing path transitions that make up the path.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathTransitionListManagerBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionListManagerBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    PlaceDefaultElbow: bool = ...
    """
    Returns or sets  the setting to determine whether to assign the default elbow to new segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``PlaceDefaultElbow`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PlaceDefaultElbow`` 
    
    :param placeDefaultElbow: 
    :type placeDefaultElbow: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SimplifyPath: bool = ...
    """
    Returns or sets  the setting to determine whether to simplify the path by removing collinear extension Routing Control Points.  
    
    <hr>
    
    Getter Method
    
    Signature ``SimplifyPath`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SimplifyPath`` 
    
    :param simplifyPath: 
    :type simplifyPath: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SnapAngle: float = ...
    """
    Returns or sets  the angle tolerance to snap to a location that allows a valid placement of an elbow.  
    
    <hr>
    
    Getter Method
    
    Signature ``SnapAngle`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SnapAngle`` 
    
    :param snapAngle: 
    :type snapAngle: float 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SnapToElbowAngles: bool = ...
    """
    Returns or sets  the setting to determine whether to force the new control point to automatically snap to a location 
    that allows a valid placement of an elbow.  
    
    <hr>
    
    Getter Method
    
    Signature ``SnapToElbowAngles`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SnapToElbowAngles`` 
    
    :param snapToElbowAngles: 
    :type snapToElbowAngles: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockSettings: PathStockPreferenceBuilder = ...
    """
    Returns  the builder for assigning stock to the new path.  
    
    <hr>
    
    Getter Method
    
    Signature ``StockSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: CreatePathBuilder = ...  # unknown typename


class StockBuilder(NXOpen.Builder):
    """
    Builder for creating/editing stocks.  
    
    Create Stock: Takes a set of segments and assign the selected the stock
    to the segments. The stock style and orientation settings are optional.
    Edit Stock: Takes in the selected stock to edit as input and redefines
    the stock with the new settings.
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateStockBuilder`
    
    Default values.
    
    =======================  =====
    Property                 Value
    =======================  =====
    OrientationAngle.Value   0 
    =======================  =====
    
    .. versionadded:: NX11.0.0
    """
    
    def PreCommit(self) -> None:
        """
        Performs the operations needed prior to a commit.  
        
        This method has to be called before invoking commit. 
        
        Signature ``PreCommit()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject`s that represent content that will be created by this builder.  
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    CrossSectionDirection: NXOpen.Direction = ...
    """
    Returns or sets  the orientation vector.  
    
    cross section direction of the stock. 
    
    <hr>
    
    Getter Method
    
    Signature ``CrossSectionDirection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``CrossSectionDirection`` 
    
    :param orientationVector: 
    :type orientationVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    MirrorCrossSection: bool = ...
    """
    Returns or sets  the mirror cross section value.  
    
    <hr>
    
    Getter Method
    
    Signature ``MirrorCrossSection`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MirrorCrossSection`` 
    
    :param flag: 
    :type flag: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    OrientationAngle: NXOpen.Expression = ...
    """
    Returns  the angle.  
    
    Determines the rotation angle of the stock. 
    
    <hr>
    
    Getter Method
    
    Signature ``OrientationAngle`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SegmentCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing object collector that collects segments to assign stock to.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockAnchor: str = ...
    """
    Returns or sets   
    
    <hr>
    
    Getter Method
    
    Signature ``StockAnchor`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``StockAnchor`` 
    
    :param anchorName: 
    :type anchorName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockSettings: PathStockPreferenceBuilder = ...
    """
    Returns  the path stock settings required to assign stock 
    
    <hr>
    
    Getter Method
    
    Signature ``StockSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: StockBuilder = ...  # unknown typename


class MovePathBuilderDetachTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class MovePathBuilderDetachTypes():
    """
    Specifies the options that will allow the user to enforce the transformation by detaching 
    the routing objects (if necessary) from objects that stop the selected object from moving.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "AlwaysMaintainConnections", " - "
       "AllowDetachOnConflict", " - "
       "DetachSelectedObjects", " - "
    """
    AlwaysMaintainConnections = 0  # MovePathBuilderDetachTypesMemberType
    AllowDetachOnConflict = 1  # MovePathBuilderDetachTypesMemberType
    DetachSelectedObjects = 2  # MovePathBuilderDetachTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class MovePathBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.MovePathBuilder`.  
    
    Allows the user to perform 
    transform of routing objects.  If run from a non-interactive session it will return None.
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateMovePathBuilder`
    
    Default values.
    
    =====================  =====================
    Property               Value
    =====================  =====================
    Motion.DeltaEnum       ReferenceWcsWorkPart 
    ---------------------  ---------------------
    Motion.DeltaXc.Value   0.0 
    ---------------------  ---------------------
    Motion.DeltaYc.Value   0.0 
    ---------------------  ---------------------
    Motion.DeltaZc.Value   0.0 
    =====================  =====================
    
    .. versionadded:: NX11.0.0
    """
    
    class DetachTypes():
        """
        Specifies the options that will allow the user to enforce the transformation by detaching 
        the routing objects (if necessary) from objects that stop the selected object from moving.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "AlwaysMaintainConnections", " - "
           "AllowDetachOnConflict", " - "
           "DetachSelectedObjects", " - "
        """
        AlwaysMaintainConnections = 0  # MovePathBuilderDetachTypesMemberType
        AllowDetachOnConflict = 1  # MovePathBuilderDetachTypesMemberType
        DetachSelectedObjects = 2  # MovePathBuilderDetachTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def StartDrag(self) -> None:
        """
        Begin a drag operation.  
        
        Signature ``StartDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def DragObjects(self) -> None:
        """
        Perform a drag operation.  
        
        Signature ``DragObjects()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def StopDrag(self) -> None:
        """
        End a drag operation 
        
        Signature ``StopDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ResetDrag(self) -> None:
        """
        Reset a drag operation 
        
        Signature ``ResetDrag()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    DetachType: MovePathBuilderDetachTypes = ...
    """
    Returns or sets  the detach type setting.  
    
    Allows the user to specify acceptable detach types for objects that prevent the transformation of the 
    selected objects.
    
    <hr>
    
    Getter Method
    
    Signature ``DetachType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.MovePathBuilderDetachTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``DetachType`` 
    
    :param detachType: 
    :type detachType: :py:class:`NXOpen.MechanicalRouting.MovePathBuilderDetachTypes` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    MaintainLength: bool = ...
    """
    Returns or sets  the maintain length setting.  
    
    This keeps the length of the selected segments constant through the transform operation. The adjacent 
    segments will be modified and reconnected to the end of the moving segments as required. 
    If this option is turned off, the segments that are moved may extend or trim back to connect to adjacent segments. 
    
    <hr>
    
    Getter Method
    
    Signature ``MaintainLength`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``MaintainLength`` 
    
    :param maintainLength: 
    :type maintainLength: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Motion: NXOpen.GeometricUtilities.ModlMotion = ...
    """
    Returns  the transformation to apply to the selected routing objects.  
    
    <hr>
    
    Getter Method
    
    Signature ``Motion`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.ModlMotion` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    PathSelection: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the objects that make up the path that needs to be transformed.  
    
    The objects can be segments, routing control points and routing components that have properties that 
    make them suitable to be moved by the routing application.
    
    <hr>
    
    Getter Method
    
    Signature ``PathSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Preview: bool = ...
    """
    Returns or sets  the preview setting 
    
    <hr>
    
    Getter Method
    
    Signature ``Preview`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Preview`` 
    
    :param preview: 
    :type preview: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: MovePathBuilder = ...  # unknown typename


class InsulationService():
    """
    Represents a :py:class:`NXOpen.MechanicalRouting.InsulationService` object.  
    
    Uses the :py:meth:`MechanicalRouting.RoutingManager.InsulationService` to obtain
    an instance of this class.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.MechanicalRouting.RoutingManager`
    
    .. versionadded:: NX12.0.0
    """
    
    def GetAllInsulatedObjectsInContainer(self, container: NXOpen.Assemblies.Component) -> 'list[NXOpen.NXObject]':
        """
        Get all insulation occurences in current container  
        
        Signature ``GetAllInsulatedObjectsInContainer(container)`` 
        
        :param container: 
        :type container: :py:class:`NXOpen.Assemblies.Component` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_pipetube ("Routing Piping and Tubing")
        """
        ...
    


class EditPlacementBuilder(NXOpen.Builder):
    """
    the Builder to Edit Placement   
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateEditPlacementBuilder`
    
    .. versionadded:: NX12.0.0
    """
    PartPlacementBuilder: PartPlacementBuilder = ...
    """
    Returns  the :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilder` 
    
    <hr>
    
    Getter Method
    
    Signature ``PartPlacementBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilder` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: EditPlacementBuilder = ...  # unknown typename


class AssignCornerBuilderCornerTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AssignCornerBuilderCornerType():
    """
    Defines the corner types. None, Miter and Bend.   
    
    .. deprecated::  NX11.0.1
       Use :py:class:`NXOpen.MechanicalRouting.CornerBuilderType` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "Bend", " - "
       "Miter", " - "
    """
    NotSet = 0  # AssignCornerBuilderCornerTypeMemberType
    Bend = 1  # AssignCornerBuilderCornerTypeMemberType
    Miter = 2  # AssignCornerBuilderCornerTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class AssignCornerBuilder(NXOpen.Builder):
    """
    Builder class for Assign Corner which creates corner  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateAssignCornerBuilder`
    
    Default values.
    
    ======================================================  ======================================
    Property                                                Value
    ======================================================  ======================================
    BendCornerSettings.Method (deprecated)                  Radius 
    ------------------------------------------------------  --------------------------------------
    BendCornerSettings.Radius.Value (deprecated)            0 (millimeters part), 0 (inches part) 
    ------------------------------------------------------  --------------------------------------
    BendCornerSettings.RatioToDiameter.Value (deprecated)   0 (millimeters part), 0 (inches part) 
    ------------------------------------------------------  --------------------------------------
    CornerSettings.CornerType                               None 
    ======================================================  ======================================
    
    .. versionadded:: NX11.0.0
    """
    
    class CornerType():
        """
        Defines the corner types. None, Miter and Bend.   
        
        .. deprecated::  NX11.0.1
           Use :py:class:`NXOpen.MechanicalRouting.CornerBuilderType` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "Bend", " - "
           "Miter", " - "
        """
        NotSet = 0  # AssignCornerBuilderCornerTypeMemberType
        Bend = 1  # AssignCornerBuilderCornerTypeMemberType
        Miter = 2  # AssignCornerBuilderCornerTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetCreatedComponents(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Components created during Assign Corner operation.  
        
        Signature ``GetCreatedComponents()`` 
        
        :returns:  Components created during Assign Corner operation.  
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def PreCommit(self) -> None:
        """
        Performs the operations needed prior to a commit.  
        
        This method has to be called before invoking commit. 
        
        Signature ``PreCommit()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject` that represent the content that will be created by this builder.  
        
        logical objects will be created only for miter corner case. 
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    BendCornerSettings: BendCornerTypeBuilder = ...
    """
    Returns  the bend corner block 
    
    <hr>
    
    Getter Method
    
    Signature ``BendCornerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.BendCornerTypeBuilder` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.AssignCornerBuilder.CornerSettings` instead.
    
    License requirements: routing_base ("Routing Basic")
    """
    ControlPointSelection: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing control points collector 
    
    <hr>
    
    Getter Method
    
    Signature ``ControlPointSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    CornerSettings: CornerBuilder = ...
    """
    Returns  the corner block 
    
    <hr>
    
    Getter Method
    
    Signature ``CornerSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.CornerBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    Type: AssignCornerBuilderCornerType = ...
    """
    Returns or sets  the assign corner type
    
    <hr>
    
    Getter Method
    
    Signature ``Type`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.AssignCornerBuilderCornerType` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.CornerBuilder.CornerType` instead.
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Type`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.MechanicalRouting.AssignCornerBuilderCornerType` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.CornerBuilder.CornerType` instead.
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: AssignCornerBuilder = ...  # unknown typename


class RoutingManager():
    """
    Represents an :py:class:`NXOpen.MechanicalRouting.RoutingManager` object.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX11.0.0
    """
    
    @staticmethod
    def GetRoutingManager():
        ...
    
    BuilderFactory: BuilderFactory = ...
    """
    Returns a :py:class:`NXOpen.MechanicalRouting.BuilderFactory` object.  
    
    Use this object
    to create specific routing mechanical builders.
    
    Signature ``BuilderFactory`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.BuilderFactory`
    """
    ConnectivityService: ConnectivityService = ...
    """
    Returns a :py:class:`NXOpen.MechanicalRouting.ConnectivityService` object.  
    
    Use this object
    for specific Routing Mechanical Connectivity Service.
    
    Signature ``ConnectivityService`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.ConnectivityService`
    """
    LogicalDesignService: LogicalDesignService = ...
    """
    Returns a :py:class:`NXOpen.MechanicalRouting.LogicalDesignService` object.  
    
    Use this object
    for specific Routing Mechanical Logical Design to Physical Design Service.
    
    Signature ``LogicalDesignService`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.LogicalDesignService`
    """
    InsulationService: InsulationService = ...
    """
    Returns a :py:class:`NXOpen.MechanicalRouting.InsulationService` object.  
    
    Use this object
    for specific Routing Mechanical Insulation service
    
    Signature ``InsulationService`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.InsulationService`
    """


class PathStockPreferenceBuilderAssignStockTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathStockPreferenceBuilderAssignStockType():
    """
    Determines the type of stock being assigned. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Stock", "Default stock type."
       "Overstock", "Overstock stock type."
    """
    Stock = 0  # PathStockPreferenceBuilderAssignStockTypeMemberType
    Overstock = 1  # PathStockPreferenceBuilderAssignStockTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathStockPreferenceBuilderAssignStockSubTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathStockPreferenceBuilderAssignStockSubType():
    """
    Determines the type of sub stock being assigned. This is only valid when Stock type is 'Stock' 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Stock", "Default stock subtype."
       "SpaceReservation", "Space Reservation stock subtype."
    """
    Stock = 0  # PathStockPreferenceBuilderAssignStockSubTypeMemberType
    SpaceReservation = 1  # PathStockPreferenceBuilderAssignStockSubTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathStockPreferenceBuilderAssignMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathStockPreferenceBuilderAssignMethod():
    """
    Determines how to choose which stock to assign.   
    
    .. deprecated::  NX11.0.1
       Use :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderStockMethods` instead.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Stock."
       "FromStartObject", "Finds a stock based off of the default stock and the object selected by the user."
       "Circular", "User specified diameter, creates round space reservation stock."
       "Rectangular", "User specified values, creates rectangular space reservation stock."
       "FlatOval", "User specified values, creates flat_oval space reservation stock."
       "SpecifiedStock", "Stock selected from Specify Item dialog"
    """
    NotSet = 0  # PathStockPreferenceBuilderAssignMethodMemberType
    FromStartObject = 1  # PathStockPreferenceBuilderAssignMethodMemberType
    Circular = 2  # PathStockPreferenceBuilderAssignMethodMemberType
    Rectangular = 3  # PathStockPreferenceBuilderAssignMethodMemberType
    FlatOval = 4  # PathStockPreferenceBuilderAssignMethodMemberType
    SpecifiedStock = 5  # PathStockPreferenceBuilderAssignMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathStockPreferenceBuilderStockMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathStockPreferenceBuilderStockMethod():
    """
    Determines how to choose which stock to assign. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Stock."
       "SpecifiedStock", "Stock selected from Specify Item dialog"
    """
    NotSet = 0  # PathStockPreferenceBuilderStockMethodMemberType
    SpecifiedStock = 1  # PathStockPreferenceBuilderStockMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathStockPreferenceBuilderSpaceReservationMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathStockPreferenceBuilderSpaceReservationMethod():
    """
    Determines how to choose which space reservation to assign. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "No Stock."
       "FromStartObject", "Finds a stock based off of the default stock and the object selected by the user."
       "Circular", "User specified diameter, creates round space reservation stock."
       "Rectangular", "User specified values, creates rectangular space reservation stock."
       "FlatOval", "User specified values, creates flat_oval space reservation stock."
       "SpecifiedSpaceReservation", "sp selected from Specify Item dialog"
    """
    NotSet = 0  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    FromStartObject = 1  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    Circular = 2  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    Rectangular = 3  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    FlatOval = 4  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    SpecifiedSpaceReservation = 5  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathStockPreferenceBuilder(NXOpen.TaggedObject, NXOpen.GeometricUtilities.IComponentBuilder):
    """
    Assigns stocks to segments based on user's criteria and the current default stock.  
    
    .. versionadded:: NX11.0.0
    """
    
    class AssignStockType():
        """
        Determines the type of stock being assigned. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Stock", "Default stock type."
           "Overstock", "Overstock stock type."
        """
        Stock = 0  # PathStockPreferenceBuilderAssignStockTypeMemberType
        Overstock = 1  # PathStockPreferenceBuilderAssignStockTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AssignStockSubType():
        """
        Determines the type of sub stock being assigned. This is only valid when Stock type is 'Stock' 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Stock", "Default stock subtype."
           "SpaceReservation", "Space Reservation stock subtype."
        """
        Stock = 0  # PathStockPreferenceBuilderAssignStockSubTypeMemberType
        SpaceReservation = 1  # PathStockPreferenceBuilderAssignStockSubTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AssignMethod():
        """
        Determines how to choose which stock to assign.   
        
        .. deprecated::  NX11.0.1
           Use :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderStockMethods` instead.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No Stock."
           "FromStartObject", "Finds a stock based off of the default stock and the object selected by the user."
           "Circular", "User specified diameter, creates round space reservation stock."
           "Rectangular", "User specified values, creates rectangular space reservation stock."
           "FlatOval", "User specified values, creates flat_oval space reservation stock."
           "SpecifiedStock", "Stock selected from Specify Item dialog"
        """
        NotSet = 0  # PathStockPreferenceBuilderAssignMethodMemberType
        FromStartObject = 1  # PathStockPreferenceBuilderAssignMethodMemberType
        Circular = 2  # PathStockPreferenceBuilderAssignMethodMemberType
        Rectangular = 3  # PathStockPreferenceBuilderAssignMethodMemberType
        FlatOval = 4  # PathStockPreferenceBuilderAssignMethodMemberType
        SpecifiedStock = 5  # PathStockPreferenceBuilderAssignMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StockMethod():
        """
        Determines how to choose which stock to assign. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No Stock."
           "SpecifiedStock", "Stock selected from Specify Item dialog"
        """
        NotSet = 0  # PathStockPreferenceBuilderStockMethodMemberType
        SpecifiedStock = 1  # PathStockPreferenceBuilderStockMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SpaceReservationMethod():
        """
        Determines how to choose which space reservation to assign. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "No Stock."
           "FromStartObject", "Finds a stock based off of the default stock and the object selected by the user."
           "Circular", "User specified diameter, creates round space reservation stock."
           "Rectangular", "User specified values, creates rectangular space reservation stock."
           "FlatOval", "User specified values, creates flat_oval space reservation stock."
           "SpecifiedSpaceReservation", "sp selected from Specify Item dialog"
        """
        NotSet = 0  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        FromStartObject = 1  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        Circular = 2  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        Rectangular = 3  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        FlatOval = 4  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        SpecifiedSpaceReservation = 5  # PathStockPreferenceBuilderSpaceReservationMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetClassificationObjectIdentifier(self, classificationObjectId: str) -> None:
        """
        Sets the identifier of the classification object associated with the part to place 
        
        Signature ``SetClassificationObjectIdentifier(classificationObjectId)`` 
        
        :param classificationObjectId: 
        :type classificationObjectId: str 
        
        .. versionadded:: NX11.0.0
        
        .. deprecated::  NX11.0.1
           Use :py:meth:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder.SetClassificationObjectIdentifierForStock` instead.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetClassificationObjectIdentifierForStock(self) -> str:
        """
        Get the identifier of the classification object associated with the stock part to place 
        NOTE: Client should NOT free the returned string  
        
        Signature ``GetClassificationObjectIdentifierForStock()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetClassificationObjectIdentifierForStock(self, classificationObjectId: str) -> None:
        """
        Sets the identifier of the classification object associated with the stock part to place 
        
        Signature ``SetClassificationObjectIdentifierForStock(classificationObjectId)`` 
        
        :param classificationObjectId: 
        :type classificationObjectId: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetFileSpecificationOfStockToPlace(self) -> str:
        """
        Get the file specification of the stock part to place 
        NOTE: Client should NOT free the returned string  
        
        Signature ``GetFileSpecificationOfStockToPlace()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetFileSpecificationOfStockToPlace(self, filename: str) -> None:
        """
        Sets the file specification of the stock part to place 
        
        Signature ``SetFileSpecificationOfStockToPlace(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetClassificationObjectIdentifierForSpaceReservation(self) -> str:
        """
        Get the identifier of the classification object associated with the space reservation part to place 
        NOTE: Client should NOT free the returned string  
        
        Signature ``GetClassificationObjectIdentifierForSpaceReservation()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetClassificationObjectIdentifierForSpaceReservation(self, classificationObjectId: str) -> None:
        """
        Sets the identifier of the classification object associated with the space reservation part to place 
        
        Signature ``SetClassificationObjectIdentifierForSpaceReservation(classificationObjectId)`` 
        
        :param classificationObjectId: 
        :type classificationObjectId: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetFileSpecificationOfSpaceReservationToPlace(self) -> str:
        """
        Get the file specification of the space reservation part to place 
        NOTE: Client should NOT free the returned string  
        
        Signature ``GetFileSpecificationOfSpaceReservationToPlace()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetFileSpecificationOfSpaceReservationToPlace(self, filename: str) -> None:
        """
        Sets the file specification of the space reservation part to place 
        
        Signature ``SetFileSpecificationOfSpaceReservationToPlace(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
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
    
    AssignStockMethod: PathStockPreferenceBuilderAssignMethod = ...
    """
    Returns or sets  the method to determine which stock to assign.  
    
    <hr>
    
    Getter Method
    
    Signature ``AssignStockMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignMethod` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder.StockMethodType` instead.
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``AssignStockMethod`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignMethod` 
    
    .. versionadded:: NX11.0.0
    
    .. deprecated::  NX11.0.1
       Use :py:meth:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder.StockMethodType` instead.
    
    License requirements: routing_base ("Routing Basic")
    """
    Diameter: NXOpen.Expression = ...
    """
    Returns or sets  the diameter value to use for the 
    :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.Circular <NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``Diameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Diameter`` 
    
    :param diameter: 
    :type diameter: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    FlatOvalHeight: NXOpen.Expression = ...
    """
    Returns  the height value to use for the  :py:class:`
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.FlatOval <
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``FlatOvalHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    FlatOvalWidth: NXOpen.Expression = ...
    """
    Returns  the Width value to use for the  :py:class:`
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.FlatOval <
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment    
    
    <hr>
    
    Getter Method
    
    Signature ``FlatOvalWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    RectangularHeight: NXOpen.Expression = ...
    """
    Returns  the height value to use for the  :py:class:`
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.Rectangular <
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``RectangularHeight`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    RectangularWidth: NXOpen.Expression = ...
    """
    Returns  the Width value to use for the  :py:class:`
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.Rectangular <
    NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment    
    
    <hr>
    
    Getter Method
    
    Signature ``RectangularWidth`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SpaceReservationMethodType: PathStockPreferenceBuilderSpaceReservationMethod = ...
    """
    Returns or sets  the method to determine which space reservation to assign.  
    
    <hr>
    
    Getter Method
    
    Signature ``SpaceReservationMethodType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``SpaceReservationMethodType`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    StartObject: NXOpen.NXObject = ...
    """
    Returns or sets  the start object to use for the 
    :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod.FromStartObject <NXOpen.MechanicalRouting.PathStockPreferenceBuilderSpaceReservationMethod>` 
    method of stock assignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``StartObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``StartObject`` 
    
    :param startObject: 
    :type startObject: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockMethodType: PathStockPreferenceBuilderStockMethod = ...
    """
    Returns or sets  the method to determine which stock to assign.  
    
    <hr>
    
    Getter Method
    
    Signature ``StockMethodType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderStockMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``StockMethodType`` 
    
    :param method: 
    :type method: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderStockMethod` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: routing_base ("Routing Basic")
    """
    StockSubType: PathStockPreferenceBuilderAssignStockSubType = ...
    """
    Returns or sets  the type of stock being assigned.  
    
    <hr>
    
    Getter Method
    
    Signature ``StockSubType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignStockSubType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``StockSubType`` 
    
    :param stockType: 
    :type stockType: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignStockSubType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockType: PathStockPreferenceBuilderAssignStockType = ...
    """
    Returns or sets  the type of stock being assigned.  
    
    <hr>
    
    Getter Method
    
    Signature ``StockType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignStockType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``StockType`` 
    
    :param stockType: 
    :type stockType: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilderAssignStockType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: PathStockPreferenceBuilder = ...  # unknown typename


class PathTransitionBuilderList(NXOpen.TaggedObject):
    """
    Represents a list of objects.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Part.CreateObjectList`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def Append(self, objects: 'list[PathTransitionBuilder]') -> None:
        """
        Appends a set of objects to the list
        
        Signature ``Append(objects)`` 
        
        :param objects:  items to append  
        :type objects: list of :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Append(self, object: PathTransitionBuilder) -> None:
        """
        Appends an object to the list
        
        Signature ``Append(object)`` 
        
        :param object:  item to append  
        :type object: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
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
    
    
    def FindIndex(self, obj: PathTransitionBuilder) -> int:
        """
        Finds the index where the input object appears.  
        
        If it does not appear,
        *   -1 is returned.
        
        Signature ``FindIndex(obj)`` 
        
        :param obj:  Object to find index for  
        :type obj: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        :returns:  index of input object, -1 if not on list  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindItem(self, index: int) -> PathTransitionBuilder:
        """
        Returns the object at the input index.  
        
        May be NULL.
        
        Signature ``FindItem(index)`` 
        
        :param index:  index of object to return  
        :type index: int 
        :returns:  object found at input index  
        :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
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
    def Erase(self, obj: PathTransitionBuilder) -> None:
        """
        Erases the object from the list, but does not delete the object.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def Erase(self, obj: PathTransitionBuilder, deleteOption: NXOpen.ObjectListDeleteOption) -> None:
        """
        Erases the object from the list.
        The list is shifted so that there isn't a null where the object used to exist. 
        
        Signature ``Erase(obj, deleteOption)`` 
        
        :param obj:  object to be removed from the list  
        :type obj: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
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
    
    
    def GetContents(self) -> 'list[PathTransitionBuilder]':
        """
        Gets the contents of the entire list  
        
        Signature ``GetContents()`` 
        
        :returns:  The list contents  
        :rtype: list of :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContents(self, objects: 'list[PathTransitionBuilder]') -> None:
        """
        Sets the contents of the entire list.  
        
        This overwrites the previous contents of this list, 
        but does not delete any objects that were originally on the list.
        
        Signature ``SetContents(objects)`` 
        
        :param objects:  The list contents  
        :type objects: list of :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
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
    def Swap(self, object1: PathTransitionBuilder, object2: PathTransitionBuilder) -> None:
        """
        Exchanges the position of two objects inside the list.
        The first object is placed where the second used to be,
        and second object where the first used to be. 
        
        Signature ``Swap(object1, object2)`` 
        
        :param object1:  first item  
        :type object1: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        :param object2:  second item  
        :type object2: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Insert(self, location: int, object: PathTransitionBuilder) -> None:
        """
        Inserts an object at the specified location 
        
        Signature ``Insert(location, object)`` 
        
        :param location:  location at which to insert the object  
        :type location: int 
        :param object:  object to be inserted  
        :type object: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder` 
        
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
    Null: PathTransitionBuilderList = ...  # unknown typename


class InsulationBuilderWrapTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InsulationBuilderWrapType():
    """
    The application type for wrapped Insulation 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoWarp", "No wrapping"
       "OverlapSpiral", "Overlap Spiral"
       "StripedSpiral", "Striped Spiral"
    """
    NoWarp = 0  # InsulationBuilderWrapTypeMemberType
    OverlapSpiral = 1  # InsulationBuilderWrapTypeMemberType
    StripedSpiral = 2  # InsulationBuilderWrapTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InsulationBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.InsulationBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateInsulationBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class WrapType():
        """
        The application type for wrapped Insulation 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoWarp", "No wrapping"
           "OverlapSpiral", "Overlap Spiral"
           "StripedSpiral", "Striped Spiral"
        """
        NoWarp = 0  # InsulationBuilderWrapTypeMemberType
        OverlapSpiral = 1  # InsulationBuilderWrapTypeMemberType
        StripedSpiral = 2  # InsulationBuilderWrapTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def PreCommit(self) -> None:
        """
        Performs the operations needed prior to a commit.  
        
        This method has to be called before invoking commit. 
        
        Signature ``PreCommit()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObject(self) -> NXOpen.PDM.LogicalObject:
        """
        Returns the :py:class:`PDM.LogicalObject`s that represent the content that will be created by this builder.  
        
        Signature ``GetLogicalObject()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SuggestWrapMethodBasedOnStockSettings(self) -> InsulationBuilderWrapType:
        """
        Returns the suggestion for :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType` based on
        :py:class:`MechanicalRouting.PathStockPreferenceBuilder`  
        
        Signature ``SuggestWrapMethodBasedOnStockSettings()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    AddInsulationOnFittings: bool = ...
    """
    Returns or sets  the value for whether insulation be added on fitting parts or not 
    
    <hr>
    
    Getter Method
    
    Signature ``AddInsulationOnFittings`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``AddInsulationOnFittings`` 
    
    :param addInsulationOnFittings: 
    :type addInsulationOnFittings: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    GapDistance: NXOpen.Expression = ...
    """
    Returns  the gap distance if the :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType`
    is :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType.StripedSpiral <NXOpen.MechanicalRouting.InsulationBuilderWrapType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``GapDistance`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    InsulationPartOccurrenceSelection: NXOpen.Assemblies.SelectComponent = ...
    """
    Returns  the insulation component to edit.  
    
    <hr>
    
    Getter Method
    
    Signature ``InsulationPartOccurrenceSelection`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponent` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    OverlapPercentage: NXOpen.Expression = ...
    """
    Returns  the percentage overlap if the :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType`
    is :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType.OverlapSpiral <NXOpen.MechanicalRouting.InsulationBuilderWrapType>` 
    
    <hr>
    
    Getter Method
    
    Signature ``OverlapPercentage`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    SegmentCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the routing object collector to collect the segments to assign Insulation to.  
    
    <hr>
    
    Getter Method
    
    Signature ``SegmentCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    StockSettings: PathStockPreferenceBuilder = ...
    """
    Returns  the stock settings for Insulation assignment.  
    
    <hr>
    
    Getter Method
    
    Signature ``StockSettings`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathStockPreferenceBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    WrapMethod: InsulationBuilderWrapType = ...
    """
    Returns or sets  the :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType` for Wrapped Insulation.  
    
    <hr>
    
    Getter Method
    
    Signature ``WrapMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``WrapMethod`` 
    
    :param wrapMethod: 
    :type wrapMethod: :py:class:`NXOpen.MechanicalRouting.InsulationBuilderWrapType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: InsulationBuilder = ...  # unknown typename


class TransformBlockBuilderTransformtypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TransformBlockBuilderTransformtype():
    """
    Specifies the options available for transform. The available opitons are Manipulator, OrientXpress, View, Plane, Vector.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", " - "
       "OrientXpress", "OrientXpress allows you to move a point constrained to a coordinate axis or plane in wcs."
       "Vector", "Vector allows you to move a point constrained to a specified direction."
       "View", "View allows you to move a point constrained to a plane, normal to the view."
       "Manipulator", "Manipulator allows you to move a point dynamically to any location in wcs."
       "Plane", "Plane allows you to move a point constrained to a specified plane."
    """
    NotSet = -1  # TransformBlockBuilderTransformtypeMemberType
    OrientXpress = 0  # TransformBlockBuilderTransformtypeMemberType
    Vector = 1  # TransformBlockBuilderTransformtypeMemberType
    View = 2  # TransformBlockBuilderTransformtypeMemberType
    Manipulator = 3  # TransformBlockBuilderTransformtypeMemberType
    Plane = 4  # TransformBlockBuilderTransformtypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TransformBlockBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateTransformBlockBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class Transformtype():
        """
        Specifies the options available for transform. The available opitons are Manipulator, OrientXpress, View, Plane, Vector.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", " - "
           "OrientXpress", "OrientXpress allows you to move a point constrained to a coordinate axis or plane in wcs."
           "Vector", "Vector allows you to move a point constrained to a specified direction."
           "View", "View allows you to move a point constrained to a plane, normal to the view."
           "Manipulator", "Manipulator allows you to move a point dynamically to any location in wcs."
           "Plane", "Plane allows you to move a point constrained to a specified plane."
        """
        NotSet = -1  # TransformBlockBuilderTransformtypeMemberType
        OrientXpress = 0  # TransformBlockBuilderTransformtypeMemberType
        Vector = 1  # TransformBlockBuilderTransformtypeMemberType
        View = 2  # TransformBlockBuilderTransformtypeMemberType
        Manipulator = 3  # TransformBlockBuilderTransformtypeMemberType
        Plane = 4  # TransformBlockBuilderTransformtypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ActiveTransformType: TransformBlockBuilderTransformtype = ...
    """
    Returns or sets  the transform type setting.  
    
    Allows you to specify the type of tool to be used for transform. 
    
    <hr>
    
    Getter Method
    
    Signature ``ActiveTransformType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilderTransformtype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ActiveTransformType`` 
    
    :param transformType: 
    :type transformType: :py:class:`NXOpen.MechanicalRouting.TransformBlockBuilderTransformtype` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    ConstrainedPoint: NXOpen.Point = ...
    """
    Returns or sets  the constrained point setting.  
    
    Allows you to specify the constrained point. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConstrainedPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ConstrainedPoint`` 
    
    :param constrainedPoint: 
    :type constrainedPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    InitialOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the initial orientation setting.  
    
    Allows you to specify initial orientation for the transform tools. 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialOrientation`` 
    
    :param initialOrientation: 
    :type initialOrientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    InitialPosition: NXOpen.Point3d = ...
    """
    Returns or sets  the initial position setting.  
    
    Allows you to specify start point for the transform tool. 
    
    <hr>
    
    Getter Method
    
    Signature ``InitialPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``InitialPosition`` 
    
    :param initialPosition: 
    :type initialPosition: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    OrientExpress: NXOpen.GeometricUtilities.OrientXpressBuilder = ...
    """
    Returns  the orient express setting.  
    
    Allows you to access the orient express object. 
    
    <hr>
    
    Getter Method
    
    Signature ``OrientExpress`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.GeometricUtilities.OrientXpressBuilder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Plane: NXOpen.Plane = ...
    """
    Returns or sets  the plane setting.  
    
    Allows you to specify the constraint plane. 
    
    <hr>
    
    Getter Method
    
    Signature ``Plane`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Plane`` 
    
    :param plane: 
    :type plane: :py:class:`NXOpen.Plane` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    TempOrientation: NXOpen.Matrix3x3 = ...
    """
    Returns or sets  the temp orientation setting.  
    
    Allows you to specify final orientation for the transform tools. 
    
    <hr>
    
    Getter Method
    
    Signature ``TempOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``TempOrientation`` 
    
    :param tempOrientation: 
    :type tempOrientation: :py:class:`NXOpen.Matrix3x3` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    TempPosition: NXOpen.Point3d = ...
    """
    Returns or sets  the temp position setting.  
    
    Allows you to specify final position for the transform tool. 
    
    <hr>
    
    Getter Method
    
    Signature ``TempPosition`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``TempPosition`` 
    
    :param tmepPosition: 
    :type tmepPosition: :py:class:`NXOpen.Point3d` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Vector: NXOpen.Direction = ...
    """
    Returns or sets  the vector setting.  
    
    Allows you to specify the constraint direction. 
    
    <hr>
    
    Getter Method
    
    Signature ``Vector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Vector`` 
    
    :param vector: 
    :type vector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: TransformBlockBuilder = ...  # unknown typename


class PartPlacementBuilderPositionAsTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartPlacementBuilderPositionAsType():
    """
    The positioning types   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Routing", "position as inline routing fitting"
       "Equipment", "position as equipment"
    """
    Routing = 0  # PartPlacementBuilderPositionAsTypeMemberType
    Equipment = 1  # PartPlacementBuilderPositionAsTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartPlacementBuilderPlacementValidationStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PartPlacementBuilderPlacementValidationStatus():
    """
    The placement validation status   
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Success", "part placement is successful as expected"
       "PartNotConnectedToRout", "after placement connection should have been built with routing system but it was not"
    """
    Success = 0  # PartPlacementBuilderPlacementValidationStatusMemberType
    PartNotConnectedToRout = 1  # PartPlacementBuilderPlacementValidationStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PartPlacementBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreatePartPlacementBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class PositionAsType():
        """
        The positioning types   
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Routing", "position as inline routing fitting"
           "Equipment", "position as equipment"
        """
        Routing = 0  # PartPlacementBuilderPositionAsTypeMemberType
        Equipment = 1  # PartPlacementBuilderPositionAsTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class PlacementValidationStatus():
        """
        The placement validation status   
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Success", "part placement is successful as expected"
           "PartNotConnectedToRout", "after placement connection should have been built with routing system but it was not"
        """
        Success = 0  # PartPlacementBuilderPlacementValidationStatusMemberType
        PartNotConnectedToRout = 1  # PartPlacementBuilderPlacementValidationStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetFileSpecificationOfPartToPlace(self, filename: str) -> None:
        """
        Sets the file specification of the part to place 
        
        Signature ``SetFileSpecificationOfPartToPlace(filename)`` 
        
        :param filename: 
        :type filename: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetClassificationObjectIdentifier(self, classificationObjectId: str) -> None:
        """
        Sets the identifier of the classification object associated with the part to place 
        
        Signature ``SetClassificationObjectIdentifier(classificationObjectId)`` 
        
        :param classificationObjectId: 
        :type classificationObjectId: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetReferenceObjectForPlacement(self, referenceObject: NXOpen.TaggedObject, referencePositionPoint: NXOpen.Point3d) -> None:
        """
        Sets the reference object and reference location for placement.  
        
        Signature ``SetReferenceObjectForPlacement(referenceObject, referencePositionPoint)`` 
        
        :param referenceObject:  New object to attach to. Can be NULL.  
        :type referenceObject: :py:class:`NXOpen.TaggedObject` 
        :param referencePositionPoint:  The new location for the part.  
        :type referencePositionPoint: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def LoadPart(self) -> NXOpen.BasePart:
        """
        Loads the :py:class:`BasePart` to place.   
        
        Signature ``LoadPart()`` 
        
        :returns:  loaded part  
        :rtype: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CreatePartOccurrenceToPlace(self, referenceSet: str, layer: int) -> NXOpen.Assemblies.Component:
        """
        Creates the :py:class:`Assemblies.Component` for part to place with given reference set and layer.  
        
        The created component will be used to generate placement solutions. Error will be raised if part to place is not loaded.  
        
        Signature ``CreatePartOccurrenceToPlace(referenceSet, layer)`` 
        
        :param referenceSet:  reference set to apply on part occurrence  
        :type referenceSet: str 
        :param layer:  layer  
        :type layer: int 
        :returns:  created part occurrence  
        :rtype: :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ProcessComponentsForEdit(self) -> None:
        """
        Processes the :py:class:`Assemblies.Component`s to edit their placement 
        
        Signature ``ProcessComponentsForEdit()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def InitializePlacementEngineBuilder(self) -> NXOpen.Placement.PlacementEngineBuilder:
        """
        Initializes the Placement Engine builder with input already present in the Part Placement Builder.  
        
        Signature ``InitializePlacementEngineBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Placement.PlacementEngineBuilder` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def PreCommitThisPlacement(self) -> None:
        """
        Pre commits the current placement operation to prepare data (ex.  
        
        split stock, post placement, etc) for final commit. This method must be followed 
        by a call to final commit method :py:meth:`MechanicalRouting.PartPlacementBuilder.CommitThisPlacement` to complete the placement operation
        
        Signature ``PreCommitThisPlacement()`` 
        
        .. versionadded:: NX11.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`MechanicalRouting.PartPlacementBuilder.ProcessPlacedPart` followed by :py:meth:`MechanicalRouting.PartPlacementBuilder.PrepareDataForConnectivity`.
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ProcessPlacedPart(self) -> None:
        """
        Processes the placed part.  
        
        This might split the target stock geometry. 
        This method will also prepare data needed to build connectivity (connectivity will be built in final commit).
        
        Signature ``ProcessPlacedPart()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ProcessPostPlaceParts(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Process the post placement parts (ex.  
        
        placement of flange after the valve and do geoemtry operations like split stock, etc).
        This method will also prepare data needed to build connectivity (connectivity will be built in final commit). 
        
        Signature ``ProcessPostPlaceParts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetCoincidentPortForCompatibility(self, portFromPlacedPart: NXOpen.Routing.Port) -> NXOpen.Routing.Port:
        """
        Get compatibility  port from port of placed part (ex in case of Valve-Flange get corresponding coincident Flange port from  Valve port)  
        
        Signature ``GetCoincidentPortForCompatibility(portFromPlacedPart)`` 
        
        :param portFromPlacedPart: 
        :type portFromPlacedPart: :py:class:`NXOpen.Routing.Port` 
        :returns:  Other port at the intersection where compatible part needs to be placed.   
        :rtype: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def ProcessCompatibilityPostPlaceParts(self) -> 'list[NXOpen.Assemblies.Component]':
        """
        Process the compatibility post placement parts (ex.  
        
        placement of gasket flange after the post placement of flange and do geoemtry operations like split stock, etc).
        This method will also prepare data needed to build connectivity (connectivity will be built in final commit). 
        
        Signature ``ProcessCompatibilityPostPlaceParts()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Assemblies.Component` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def PrepareDataForConnectivity(self) -> None:
        """
        Prepare data to build connectivity for all placed parts.  
        
        Things like computation of new stock DE (resultant of splitting) will happen here. 
        This method must be followed by a call to final commit method :py:meth:`MechanicalRouting.PartPlacementBuilder.CommitThisPlacement` to complete the placement operation 
        
        Signature ``PrepareDataForConnectivity()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def CommitThisPlacement(self) -> PartPlacementBuilderPlacementValidationStatus:
        """
        Commits the current placement operation.  
        
        This method must be called after calling method
        :py:meth:`MechanicalRouting.PartPlacementBuilder.PreCommitThisPlacement`. 
        This method returns :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilderPlacementValidationStatus` value 
        
        Signature ``CommitThisPlacement()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilderPlacementValidationStatus` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetPrimarySolutionsFlag(self, showPrimarySolutions: bool) -> None:
        """
        Sets the primary solutions flag on builder.  
        
        Signature ``SetPrimarySolutionsFlag(showPrimarySolutions)`` 
        
        :param showPrimarySolutions: 
        :type showPrimarySolutions: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetFilteredPlacementSolutions(self) -> 'list[NXOpen.Placement.PlacementSolution]':
        """
        Filters placement solutions based existing filtration flags in builder ex.  
        
        primary.  
        
        Signature ``GetFilteredPlacementSolutions()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Placement.PlacementSolution` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetPortOfPlaceableObject(self, sourcePortObject: NXOpen.TaggedObject) -> None:
        """
        Sets the port for filtration from the part being placed.  
        
        Signature ``SetPortOfPlaceableObject(sourcePortObject)`` 
        
        :param sourcePortObject: 
        :type sourcePortObject: :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetPositionAsOption(self, positioningType: PartPlacementBuilderPositionAsType) -> None:
        """
        Sets the positioning option :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilderPositionAsType` on the builder.  
        
        Signature ``SetPositionAsOption(positioningType)`` 
        
        :param positioningType: 
        :type positioningType: :py:class:`NXOpen.MechanicalRouting.PartPlacementBuilderPositionAsType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def RotatePlaceableObjectByAngle(self, rotationAngle: float) -> None:
        """
        Rotates the fitting by the specified angle along the plane perpendicular to the vector defined by the engaged port.  
        
        Signature ``RotatePlaceableObjectByAngle(rotationAngle)`` 
        
        :param rotationAngle: 
        :type rotationAngle: float 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetClassificationObjectIdentifierOfPartToPostPlace(self, classificationObjectId: str) -> None:
        """
        Sets the identifier of the classification object associated with the part to be post placed.  
        
        Signature ``SetClassificationObjectIdentifierOfPartToPostPlace(classificationObjectId)`` 
        
        :param classificationObjectId: 
        :type classificationObjectId: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetClassificationObjectIdentifierOfCompatibilityPart(self, ccType: NXOpen.Routing.ReuseLibraryPartType, classificationObjectId: str, portOne: NXOpen.Routing.Port, portTwo: NXOpen.Routing.Port) -> None:
        """
        Sets the identifier of the classification object associated with the compatibility part to post place 
        
        Signature ``SetClassificationObjectIdentifierOfCompatibilityPart(ccType, classificationObjectId, portOne, portTwo)`` 
        
        :param ccType: 
        :type ccType: :py:class:`NXOpen.Routing.ReuseLibraryPartType` 
        :param classificationObjectId: 
        :type classificationObjectId: str 
        :param portOne:  One of the ports at the intersection where compatible part needs to be placed.   
        :type portOne: :py:class:`NXOpen.Routing.Port` 
        :param portTwo:  Other port at the intersection where compatible part needs to be placed.   
        :type portTwo: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def UpdateReferenceSet(self, referenseSetName: str) -> None:
        """
        Updates the reference set for the Design Elements created during part placement operation.  
        
        Signature ``UpdateReferenceSet(referenseSetName)`` 
        
        :param referenseSetName: 
        :type referenseSetName: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def UpdateLayer(self, layerNumber: int) -> None:
        """
        Updates the layer for the Design Elements created during part placement operation.  
        
        Signature ``UpdateLayer(layerNumber)`` 
        
        :param layerNumber: 
        :type layerNumber: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def AutoAssignAttributes(self) -> None:
        """
        Auto assign the auto assignable attributes of all :py:class:`PDM.LogicalObject`s that were created during part placement operation.  
        
        Signature ``AutoAssignAttributes()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject`s having unassigned non-auto-assignable required attributes.  
        
        Signature ``GetLogicalObjectsHavingUnassignedRequiredAttributes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetLogicalObjects(self) -> 'list[NXOpen.PDM.LogicalObject]':
        """
        Returns the :py:class:`PDM.LogicalObject`s that were created during part placement operation.  
        
        Signature ``GetLogicalObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.PDM.LogicalObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetErrorCodeForPlacementSolution(self, placementSolution: NXOpen.Placement.PlacementSolution) -> int:
        """
        Returns the error code for a placement solution.  
        
        A non-zero error code may suggest whether there
        will be any design rule validation due to the given placement solution.  
        
        Signature ``GetErrorCodeForPlacementSolution(placementSolution)`` 
        
        :param placementSolution: 
        :type placementSolution: :py:class:`NXOpen.Placement.PlacementSolution` 
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetAddUnconnectedEquipmentToActiveRunOption(self, canAddEquipmentToActiveRun: bool) -> None:
        """
        Sets the option that determines whether a part positioned as Equipment should be added to the active Run  
        
        Signature ``SetAddUnconnectedEquipmentToActiveRunOption(canAddEquipmentToActiveRun)`` 
        
        :param canAddEquipmentToActiveRun:  Flag when true will result in parts positioned as Equipment to be added to the active Run.  
        :type canAddEquipmentToActiveRun: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetPortAtCutSideOfElbow(self) -> NXOpen.Routing.Port:
        """
        Get the port from cut side of cut elbow  
        
        Signature ``GetPortAtCutSideOfElbow()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Routing.Port` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    ComponentsToEditCollector: NXOpen.Routing.RouteObjectCollector = ...
    """
    Returns  the :py:class:`NXOpen.Routing.RouteObjectCollector` that collects components to edit 
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsToEditCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Routing.RouteObjectCollector` 
    
    .. versionadded:: NX12.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    LogicalDesignObject: NXOpen.NXObject = ...
    """
    Returns or sets  the mapping logical design object 
    
    <hr>
    
    Getter Method
    
    Signature ``LogicalDesignObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``LogicalDesignObject`` 
    
    :param logicalDesignObject: 
    :type logicalDesignObject: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: PartPlacementBuilder = ...  # unknown typename


class BendCornerTypeBuilderBendMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class BendCornerTypeBuilderBendMethod():
    """
    Methods available for bend creation. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Radius", "Radius method allows corner creation with the specified radius value"
       "RatioToDiameter", "Ratio to diameter method"
       "BendRadiusTable", "Bend table method creates bend from specified bend table"
       "InnerRadius", "Inner Radius method allows corner creation with the specified inner radius value"
    """
    Radius = 0  # BendCornerTypeBuilderBendMethodMemberType
    RatioToDiameter = 1  # BendCornerTypeBuilderBendMethodMemberType
    BendRadiusTable = 2  # BendCornerTypeBuilderBendMethodMemberType
    InnerRadius = 3  # BendCornerTypeBuilderBendMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class BendCornerTypeBuilder(BaseCornerTypeBuilder):
    """
    Contains setting for corner creation.  
    
    Type of bend to be created and the method to
    create the corner. 
    
    .. versionadded:: NX11.0.0
    """
    
    class BendMethod():
        """
        Methods available for bend creation. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Radius", "Radius method allows corner creation with the specified radius value"
           "RatioToDiameter", "Ratio to diameter method"
           "BendRadiusTable", "Bend table method creates bend from specified bend table"
           "InnerRadius", "Inner Radius method allows corner creation with the specified inner radius value"
        """
        Radius = 0  # BendCornerTypeBuilderBendMethodMemberType
        RatioToDiameter = 1  # BendCornerTypeBuilderBendMethodMemberType
        BendRadiusTable = 2  # BendCornerTypeBuilderBendMethodMemberType
        InnerRadius = 3  # BendCornerTypeBuilderBendMethodMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def ImportBendRadiusTable(self, bendTableFilename: str) -> None:
        """
        Imports bend radius table 
        
        Signature ``ImportBendRadiusTable(bendTableFilename)`` 
        
        :param bendTableFilename: 
        :type bendTableFilename: str 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    BendTable: str = ...
    """
    Returns or sets  the name of bend radius table 
    
    <hr>
    
    Getter Method
    
    Signature ``BendTable`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``BendTable`` 
    
    :param bendTableName: 
    :type bendTableName: str 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Method: BendCornerTypeBuilderBendMethod = ...
    """
    Returns or sets  the bend corner methods 
    
    <hr>
    
    Getter Method
    
    Signature ``Method`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.BendCornerTypeBuilderBendMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``Method`` 
    
    :param routeCornerBendMethods: 
    :type routeCornerBendMethods: :py:class:`NXOpen.MechanicalRouting.BendCornerTypeBuilderBendMethod` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Radius: NXOpen.Expression = ...
    """
    Returns  the bend corner radius 
    
    <hr>
    
    Getter Method
    
    Signature ``Radius`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    RatioToDiameter: NXOpen.Expression = ...
    """
    Returns  the bend corner ratio to diameter 
    
    <hr>
    
    Getter Method
    
    Signature ``RatioToDiameter`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: BendCornerTypeBuilder = ...  # unknown typename


class PathTransitionBuilderTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathTransitionBuilderType():
    """
    The type of transition the path takes to reach the transition end point. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Direct", " - "
       "Heal", " - "
       "Intersect", " - "
    """
    Direct = 0  # PathTransitionBuilderTypeMemberType
    Heal = 1  # PathTransitionBuilderTypeMemberType
    Intersect = 2  # PathTransitionBuilderTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathTransitionBuilderTraversalOrderMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathTransitionBuilderTraversalOrder():
    """
    The heal transition traversal order the path takes to reach the transition end point. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xyz", " - "
       "Xzy", " - "
       "Yzx", " - "
       "Yxz", " - "
       "Zxy", " - "
       "Zyx", " - "
       "Invalid", " - "
    """
    Xyz = 0  # PathTransitionBuilderTraversalOrderMemberType
    Xzy = 1  # PathTransitionBuilderTraversalOrderMemberType
    Yzx = 2  # PathTransitionBuilderTraversalOrderMemberType
    Yxz = 3  # PathTransitionBuilderTraversalOrderMemberType
    Zxy = 4  # PathTransitionBuilderTraversalOrderMemberType
    Zyx = 5  # PathTransitionBuilderTraversalOrderMemberType
    Invalid = 6  # PathTransitionBuilderTraversalOrderMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathTransitionBuilderHealOrientationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class PathTransitionBuilderHealOrientation():
    """
    The box orientation for heal transition traversal order. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Wcs", " - "
       "Absolute", " - "
       "Start", " - "
       "End", " - "
       "NewCsys", " - "
    """
    Wcs = 0  # PathTransitionBuilderHealOrientationMemberType
    Absolute = 1  # PathTransitionBuilderHealOrientationMemberType
    Start = 2  # PathTransitionBuilderHealOrientationMemberType
    End = 3  # PathTransitionBuilderHealOrientationMemberType
    NewCsys = 4  # PathTransitionBuilderHealOrientationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class PathTransitionBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilder`.  
    
    Allows the user to create 
    a routing path transition.
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.PathTransitionListManagerBuilder.CreatePathTransitionBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    class Type():
        """
        The type of transition the path takes to reach the transition end point. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Direct", " - "
           "Heal", " - "
           "Intersect", " - "
        """
        Direct = 0  # PathTransitionBuilderTypeMemberType
        Heal = 1  # PathTransitionBuilderTypeMemberType
        Intersect = 2  # PathTransitionBuilderTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TraversalOrder():
        """
        The heal transition traversal order the path takes to reach the transition end point. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xyz", " - "
           "Xzy", " - "
           "Yzx", " - "
           "Yxz", " - "
           "Zxy", " - "
           "Zyx", " - "
           "Invalid", " - "
        """
        Xyz = 0  # PathTransitionBuilderTraversalOrderMemberType
        Xzy = 1  # PathTransitionBuilderTraversalOrderMemberType
        Yzx = 2  # PathTransitionBuilderTraversalOrderMemberType
        Yxz = 3  # PathTransitionBuilderTraversalOrderMemberType
        Zxy = 4  # PathTransitionBuilderTraversalOrderMemberType
        Zyx = 5  # PathTransitionBuilderTraversalOrderMemberType
        Invalid = 6  # PathTransitionBuilderTraversalOrderMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class HealOrientation():
        """
        The box orientation for heal transition traversal order. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Wcs", " - "
           "Absolute", " - "
           "Start", " - "
           "End", " - "
           "NewCsys", " - "
        """
        Wcs = 0  # PathTransitionBuilderHealOrientationMemberType
        Absolute = 1  # PathTransitionBuilderHealOrientationMemberType
        Start = 2  # PathTransitionBuilderHealOrientationMemberType
        End = 3  # PathTransitionBuilderHealOrientationMemberType
        NewCsys = 4  # PathTransitionBuilderHealOrientationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    AddExtensionToggle: bool = ...
    """
    Returns or sets  the toggle to set forward/backward extensions for this transition.  
    
    <hr>
    
    Getter Method
    
    Signature ``AddExtensionToggle`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``AddExtensionToggle`` 
    
    :param extensionToggle: 
    :type extensionToggle: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    BackwardExtension: NXOpen.Expression = ...
    """
    Returns or sets  the backward extension length for this transition.  
    
    <hr>
    
    Getter Method
    
    Signature ``BackwardExtension`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``BackwardExtension`` 
    
    :param backwardExtension: 
    :type backwardExtension: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    BoxOrientation: PathTransitionBuilderHealOrientation = ...
    """
    Returns or sets  the box orientation for heal transition traversal order.  
    
    <hr>
    
    Getter Method
    
    Signature ``BoxOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderHealOrientation` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``BoxOrientation`` 
    
    :param boxOrientation: 
    :type boxOrientation: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderHealOrientation` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    ConnectedObject: NXOpen.NXObject = ...
    """
    Returns or sets  the object that the end point of this path transition connects to.  
    
    If the transition
    connects to a port or a routing control point, it is required to set that object as the connected object to
    build connectivity. 
    
    <hr>
    
    Getter Method
    
    Signature ``ConnectedObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ConnectedObject`` 
    
    :param connectedObject: 
    :type connectedObject: :py:class:`NXOpen.NXObject` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    EndPoint: NXOpen.Point = ...
    """
    Returns or sets  the end point that defines the end of the path transition.  
    
    <hr>
    
    Getter Method
    
    Signature ``EndPoint`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``EndPoint`` 
    
    :param endPoint: 
    :type endPoint: :py:class:`NXOpen.Point` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    ExtensionVector: NXOpen.Direction = ...
    """
    Returns or sets  the direction for extension segments.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExtensionVector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ExtensionVector`` 
    
    :param extensionVector: 
    :type extensionVector: :py:class:`NXOpen.Direction` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    ForwardExtension: NXOpen.Expression = ...
    """
    Returns or sets  the forward extension length for this transition.  
    
    <hr>
    
    Getter Method
    
    Signature ``ForwardExtension`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``ForwardExtension`` 
    
    :param forwardExtension: 
    :type forwardExtension: :py:class:`NXOpen.Expression` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    HealSolutionCsys: NXOpen.CoordinateSystem = ...
    """
    Returns or sets  the user-defined coordinate system for the :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderHealOrientation.NewCsys <NXOpen.MechanicalRouting.PathTransitionBuilderHealOrientation>` heal box orientation.  
    
    <hr>
    
    Getter Method
    
    Signature ``HealSolutionCsys`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``HealSolutionCsys`` 
    
    :param coordinateSystem: 
    :type coordinateSystem: :py:class:`NXOpen.CoordinateSystem` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    HealTraversalOrder: PathTransitionBuilderTraversalOrder = ...
    """
    Returns or sets  the heal transition traversal order the path takes to reach the transition end point.  
    
    <hr>
    
    Getter Method
    
    Signature ``HealTraversalOrder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderTraversalOrder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``HealTraversalOrder`` 
    
    :param healTraversalOrder: 
    :type healTraversalOrder: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderTraversalOrder` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    PathForwardThroughExtensionVector: bool = ...
    """
    Returns or sets  the toggle setting to define whether the path passes forward through the extension vector, or backward.  
    
    <hr>
    
    Getter Method
    
    Signature ``PathForwardThroughExtensionVector`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``PathForwardThroughExtensionVector`` 
    
    :param isPathForwardThroughExtensionVector: 
    :type isPathForwardThroughExtensionVector: bool 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    TransitionType: PathTransitionBuilderType = ...
    """
    Returns or sets  the type of transition the path takes to reach the transition end point.  
    
    <hr>
    
    Getter Method
    
    Signature ``TransitionType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    
    <hr>
    
    Setter Method
    
    Signature ``TransitionType`` 
    
    :param transitionType: 
    :type transitionType: :py:class:`NXOpen.MechanicalRouting.PathTransitionBuilderType` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: PathTransitionBuilder = ...  # unknown typename


class ConnectBuilder(NXOpen.Builder):
    """
    the Builder for Connect Path   
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateConnectBuilder`
    
    .. versionadded:: NX11.0.0
    """
    ComponentsCollector: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the selected components  
    
    <hr>
    
    Getter Method
    
    Signature ``ComponentsCollector`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX11.0.0
    
    License requirements: routing_base ("Routing Basic")
    """
    Null: ConnectBuilder = ...  # unknown typename


class ConnectivityService():
    """
    Represents a :py:class:`NXOpen.MechanicalRouting.ConnectivityService` object.  
    
    Use the :py:meth:`MechanicalRouting.RoutingManager.ConnectivityService` to obtain
    an instance of this class.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.MechanicalRouting.RoutingManager`
    
    .. versionadded:: NX11.0.0
    """
    
    def GetConnectedPorts(self, part: NXOpen.Part) -> tuple:
        """
        Returns the pairs of connected ports in the subset.  
        
        Signature ``GetConnectedPorts(part)`` 
        
        :param part:  The subset part.  
        :type part: :py:class:`NXOpen.Part` 
        :returns: a tuple 
        :rtype: A tuple consisting of (connectedPorts1, connectedPorts2). connectedPorts1 is a list of :py:class:`NXOpen.Routing.Port`. connectedPorts2 is a list of :py:class:`NXOpen.Routing.Port`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetPortsConnectedToDesignElement(self, part: NXOpen.Assemblies.Component) -> tuple:
        """
        Returns the pairs of ports connected to the given Design Element.  
        
        Signature ``GetPortsConnectedToDesignElement(part)`` 
        
        :param part:  The component of the Design Element.  
        :type part: :py:class:`NXOpen.Assemblies.Component` 
        :returns: a tuple 
        :rtype: A tuple consisting of (connectedPorts1, connectedPorts2). connectedPorts1 is a list of :py:class:`NXOpen.Routing.Port`. connectedPorts2 is a list of :py:class:`NXOpen.Routing.Port`. 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    


class ManageInlineBehaviorBuilder(NXOpen.Builder):
    """
    Represents :py:class:`NXOpen.MechanicalRouting.ManageInlineBehaviorBuilder`.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.MechanicalRouting.BuilderFactory.CreateManageInlineBehaviorBuilder`
    
    .. versionadded:: NX11.0.0
    """
    
    def SetModelElementRevision(self, modelElementRevision: NXOpen.PDM.ModelElementRevision) -> None:
        """
        Sets :py:class:`NXOpen.PDM.ModelElementRevision` of Routing Reuse type.  
        
        Raise an error if passed
        other type of object. 
        
        Signature ``SetModelElementRevision(modelElementRevision)`` 
        
        :param modelElementRevision: 
        :type modelElementRevision: :py:class:`NXOpen.PDM.ModelElementRevision` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def SetInlineBehavior(self, isInline: bool) -> None:
        """
        Sets true to mark current model element revision as inline design element(which moves along with connected
        routing design elements), false for non-inline design element (which has its own position and drives connected
        routing design elements.  
        
        Its position is never driven by inline design elements). 
        Client should call update after this as model element revision has been logged to change. 
        
        Signature ``SetInlineBehavior(isInline)`` 
        
        :param isInline: 
        :type isInline: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    
    def GetInlineBehavior(self) -> bool:
        """
        Returns true if current model element revision as inline design element.  
        
        Signature ``GetInlineBehavior()`` 
        
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.0
        
        License requirements: routing_base ("Routing Basic")
        """
        ...
    
    Null: ManageInlineBehaviorBuilder = ...  # unknown typename


