# module 'NXOpen.ShipDesign'
#
# Automatically generated 2025-06-09T14:38:47.470641
#
"""Default documentation for NXOpen.ShipDesign."""

import typing

import NXOpen
import NXOpen.Assemblies
import NXOpen.Features



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class ApplicationUtils():
    """
    Represents Generator which wrap the ship api for china   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.ShipDesign.ShipSession`
    
    .. versionadded:: NX11.0.0
    """
    
    def RegisterButtonApplication(self, appId: int, buttonName: str) -> None:
        """
        Register button in other application 
        
        Signature ``RegisterButtonApplication(appId, buttonName)`` 
        
        :param appId:  The id of the application.  
        :type appId: int 
        :param buttonName:  The name of the button.  
        :type buttonName: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def RegisterApplicationForModlFeatureEdit(self, appName: str) -> None:
        """
        Register button in other application 
        
        Signature ``RegisterApplicationForModlFeatureEdit(appName)`` 
        
        :param appName:  The name of the application.  
        :type appName: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    


class ShipNavigatorNodeBuilderNodeTypesMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShipNavigatorNodeBuilderNodeTypes():
    """
    Settings to indicate the type of ship navigator node.  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Object", "The object node type."
       "Part", "The part node type."
       "Container", "The container node type."
    """
    Object = 0  # ShipNavigatorNodeBuilderNodeTypesMemberType
    Part = 1  # ShipNavigatorNodeBuilderNodeTypesMemberType
    Container = 2  # ShipNavigatorNodeBuilderNodeTypesMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShipNavigatorNodeBuilder(NXOpen.Builder):
    """
    Represents the ship navigator node builder to add or edit ship navigator node.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.ShipDesign.NavigatorCollection.CreateShipNavigatorNodeBuilder`
    
    .. versionadded:: NX11.0.1
    """
    
    class NodeTypes():
        """
        Settings to indicate the type of ship navigator node.  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Object", "The object node type."
           "Part", "The part node type."
           "Container", "The container node type."
        """
        Object = 0  # ShipNavigatorNodeBuilderNodeTypesMemberType
        Part = 1  # ShipNavigatorNodeBuilderNodeTypesMemberType
        Container = 2  # ShipNavigatorNodeBuilderNodeTypesMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    ExpandChildNodes: bool = ...
    """
    Returns or sets  the setting indicates if the node we create or edit will expand its children in ship navigator.  
    
    <hr>
    
    Getter Method
    
    Signature ``ExpandChildNodes`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ExpandChildNodes`` 
    
    :param expandNode: 
    :type expandNode: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    NodeName: str = ...
    """
    Returns or sets  the ship navigator node name.  
    
    <hr>
    
    Getter Method
    
    Signature ``NodeName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NodeName`` 
    
    :param nodeName: 
    :type nodeName: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    NodeType: ShipNavigatorNodeBuilderNodeTypes = ...
    """
    Returns or sets  the ship navigator node type, which can be object, part or container.  
    
    <hr>
    
    Getter Method
    
    Signature ``NodeType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShipDesign.ShipNavigatorNodeBuilderNodeTypes` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``NodeType`` 
    
    :param type: 
    :type type: :py:class:`NXOpen.ShipDesign.ShipNavigatorNodeBuilderNodeTypes` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_ship_detail ("Ship Detail Design") OR nx_ship_basic ("Ship Basic Design")
    """
    SourceFeatures: NXOpen.Features.SelectFeatureList = ...
    """
    Returns  the list of features used to create ship navigator object node.  
    
    <hr>
    
    Getter Method
    
    Signature ``SourceFeatures`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.SelectFeatureList` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    SourceParts: NXOpen.Assemblies.SelectComponentList = ...
    """
    Returns  the list of parts used to create ship navigator part nodes.  
    
    <hr>
    
    Getter Method
    
    Signature ``SourceParts`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.SelectComponentList` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    Null: ShipNavigatorNodeBuilder = ...  # unknown typename


class GeneralArrangementManager():
    """
    Represents the interface for General Arrangement classes   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.ShipDesign.ShipSession`
    
    .. versionadded:: NX12.0.0
    """
    
    def GASketchEnd(self) -> None:
        """
        Exits the Sketch environment under General Arrangement application.  
        
        Signature ``GASketchEnd()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def ResizeGrid(self) -> None:
        """
        Resizes the ship grid datum.  
        
        Signature ``ResizeGrid()`` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def MakeContainerPart(self, part: NXOpen.Part) -> None:
        """
        Makes the part to be Ship Container.  
        
        Signature ``MakeContainerPart(part)`` 
        
        :param part:  the container part  
        :type part: :py:class:`NXOpen.Part` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def CreateSkecthRectangle(self, sketch: NXOpen.Sketch) -> None:
        """
        Creates the rectangle for Deck Plan sketch.  
        
        Signature ``CreateSkecthRectangle(sketch)`` 
        
        :param sketch:  the sketch  
        :type sketch: :py:class:`NXOpen.Sketch` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_ship_gen_arrange ("Ship General Arrangement") OR nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    


class GeneratorClashTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class GeneratorClashType():
    """
    Clash status to indicate to show space position relation between two bodies
    1.Clashes in entities of the same dimension
    Clash_interfere        Two solid bodies interfere if they share a common volume
    Two faces interfere if they share a common area, or they intersect.
    Two edges interfere if they share a common length, or they intersect.
    
    Clash_abut_no_class    Two solid bodies abut when they touch, but do not share a common volume.
    Two faces abut when they share a common curve or point in space which lies on the bounding topology of at least one of the faces.
    Two edges abut when they share a common point in space which lies on the bounding topology of at least one of the edges.
    
    Clash_a_in_b
    Clash_b_in_a           For solids, faces, and edges, one entity is contained when it lies entirely inside the other entity, 
    and their bounding topologies do not touch.
    2.Clashes in bodies of different dimensions 
    Clash_interfere        If there is a common point in space that lies within the bounding topology of the two bodies,
    then the bodies are said to interfere.
    Clash_abut_no_class    If no common point exists, but the bounding topologies of the two bodies touch,
    then the bodies are said to abut.
    Clash_a_in_b           
    Clash_b_in_a           If one body lies entirely within the bounding topology of the other, and the bounding topology 
    of the two bodies do not touch then the entity is contained.
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSet", "There is no clash between two bodies."
       "AInB", "Body a is completly in body b, without abut."
       "BInA", "Body b is completly in body a, without abut."
       "Exists", "Clash exists; only this is requested."
       "AbutNoClass", "Bounding topologies abut, in/outside unknown."
       "AbutBInA", "Bounding b topology abuts bounding a topology on the inside."
       "AbutBOutA", "Bounding b topology abuts bounding a topology on the outside."
       "Interfere", "Bounding topologies interfere."
    """
    NotSet = 0  # GeneratorClashTypeMemberType
    AInB = 1  # GeneratorClashTypeMemberType
    BInA = 2  # GeneratorClashTypeMemberType
    Exists = 3  # GeneratorClashTypeMemberType
    AbutNoClass = 4  # GeneratorClashTypeMemberType
    AbutBInA = 5  # GeneratorClashTypeMemberType
    AbutBOutA = 6  # GeneratorClashTypeMemberType
    Interfere = 7  # GeneratorClashTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class Generator():
    """
    Represents Generator which wrap the ship api for china   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.ShipDesign.ShipSession`
    
    .. versionadded:: NX11.0.0
    """
    
    class ClashType():
        """
        Clash status to indicate to show space position relation between two bodies
        1.Clashes in entities of the same dimension
        Clash_interfere        Two solid bodies interfere if they share a common volume
        Two faces interfere if they share a common area, or they intersect.
        Two edges interfere if they share a common length, or they intersect.
        
        Clash_abut_no_class    Two solid bodies abut when they touch, but do not share a common volume.
        Two faces abut when they share a common curve or point in space which lies on the bounding topology of at least one of the faces.
        Two edges abut when they share a common point in space which lies on the bounding topology of at least one of the edges.
        
        Clash_a_in_b
        Clash_b_in_a           For solids, faces, and edges, one entity is contained when it lies entirely inside the other entity, 
        and their bounding topologies do not touch.
        2.Clashes in bodies of different dimensions 
        Clash_interfere        If there is a common point in space that lies within the bounding topology of the two bodies,
        then the bodies are said to interfere.
        Clash_abut_no_class    If no common point exists, but the bounding topologies of the two bodies touch,
        then the bodies are said to abut.
        Clash_a_in_b           
        Clash_b_in_a           If one body lies entirely within the bounding topology of the other, and the bounding topology 
        of the two bodies do not touch then the entity is contained.
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSet", "There is no clash between two bodies."
           "AInB", "Body a is completly in body b, without abut."
           "BInA", "Body b is completly in body a, without abut."
           "Exists", "Clash exists; only this is requested."
           "AbutNoClass", "Bounding topologies abut, in/outside unknown."
           "AbutBInA", "Bounding b topology abuts bounding a topology on the inside."
           "AbutBOutA", "Bounding b topology abuts bounding a topology on the outside."
           "Interfere", "Bounding topologies interfere."
        """
        NotSet = 0  # GeneratorClashTypeMemberType
        AInB = 1  # GeneratorClashTypeMemberType
        BInA = 2  # GeneratorClashTypeMemberType
        Exists = 3  # GeneratorClashTypeMemberType
        AbutNoClass = 4  # GeneratorClashTypeMemberType
        AbutBInA = 5  # GeneratorClashTypeMemberType
        AbutBOutA = 6  # GeneratorClashTypeMemberType
        Interfere = 7  # GeneratorClashTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CheckBodyClash(self, bodyA: NXOpen.DisplayableObject, bodyB: NXOpen.DisplayableObject) -> GeneratorClashType:
        """
        Check the clash between two bodys.  
        
        Signature ``CheckBodyClash(bodyA, bodyB)`` 
        
        :param bodyA: 
        :type bodyA: :py:class:`NXOpen.DisplayableObject` 
        :param bodyB: 
        :type bodyB: :py:class:`NXOpen.DisplayableObject` 
        :returns:  O: clash status for body a and body b  
        :rtype: :py:class:`NXOpen.ShipDesign.GeneratorClashType` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def GetOutlineSheetbody(self, bodies: 'list[NXOpen.Body]', datumPlane: NXOpen.DatumPlane) -> NXOpen.Body:
        """
        Get the outline sheet body of input bodies.  
        
        Signature ``GetOutlineSheetbody(bodies, datumPlane)`` 
        
        :param bodies: 
        :type bodies: list of :py:class:`NXOpen.Body` 
        :param datumPlane: 
        :type datumPlane: :py:class:`NXOpen.DatumPlane` 
        :returns:  O: output outline sheet body  
        :rtype: :py:class:`NXOpen.Body` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def AskPlatesSpatialRelations(self, hull: NXOpen.TaggedObject, inSheets: 'list[NXOpen.TaggedObject]', tolerence: float) -> tuple:
        """
        Gets the spatial relations of the plates based on its positions.  
        
        Signature ``AskPlatesSpatialRelations(hull, inSheets, tolerence)`` 
        
        :param hull: 
        :type hull: :py:class:`NXOpen.TaggedObject` 
        :param inSheets: 
        :type inSheets: list of :py:class:`NXOpen.TaggedObject` 
        :param tolerence: 
        :type tolerence: float 
        :returns: a tuple 
        :rtype: A tuple consisting of (elementIndex, outElements). elementIndex is a list of int. outElements is a list of :py:class:`NXOpen.TaggedObject`. 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def AskIntersectionPlates(self, plate: NXOpen.TaggedObject, inSheets: 'list[NXOpen.TaggedObject]', tolerence: float) -> 'list[NXOpen.TaggedObject]':
        """
        Gets all intersected plates with the given plates.  
        
        Signature ``AskIntersectionPlates(plate, inSheets, tolerence)`` 
        
        :param plate: 
        :type plate: :py:class:`NXOpen.TaggedObject` 
        :param inSheets: 
        :type inSheets: list of :py:class:`NXOpen.TaggedObject` 
        :param tolerence: 
        :type tolerence: float 
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def RegisterApplicationCallback(self, name: str, enterCallback: typing.Callable, exitCallback: typing.Callable) -> None:
        """
        Register application callback when application is entered or exited.  
        
        It is specific for ship customers. 
        
        Signature ``RegisterApplicationCallback(name, enterCallback, exitCallback)`` 
        
        :param name:  The name of the application.  
        :type name: str 
        :param enterCallback:  The method called when entering the application  
        :type enterCallback: CallableObject 
        :param exitCallback:  The method called when exiting the application  
        :type exitCallback: CallableObject 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def CreateCargo(self, inSheets: 'list[NXOpen.TaggedObject]', tolerence: float) -> 'list[NXOpen.TaggedObject]':
        """
        Creates the ship cargo body based on the input boundary sheets.  
        
        Signature ``CreateCargo(inSheets, tolerence)`` 
        
        :param inSheets: 
        :type inSheets: list of :py:class:`NXOpen.TaggedObject` 
        :param tolerence: 
        :type tolerence: float 
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def GetSheetsEdgesLaidOnTargetSheet(self, outSheet: NXOpen.TaggedObject, inSheets: 'list[NXOpen.TaggedObject]', tolerence: float) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the edges of tool sheet bodies which are laid on a target sheet body 
        
        Signature ``GetSheetsEdgesLaidOnTargetSheet(outSheet, inSheets, tolerence)`` 
        
        :param outSheet: 
        :type outSheet: :py:class:`NXOpen.TaggedObject` 
        :param inSheets: 
        :type inSheets: list of :py:class:`NXOpen.TaggedObject` 
        :param tolerence: 
        :type tolerence: float 
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def CreateProgress(self, numSteps: int, operationName: str) -> None:
        """
        Creates a progress bar with given title and number of total steps.  
        
        Signature ``CreateProgress(numSteps, operationName)`` 
        
        :param numSteps: 
        :type numSteps: int 
        :param operationName: 
        :type operationName: str 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def DeleteProgress(self) -> None:
        """
        Deletes the progress bar.  
        
        Signature ``DeleteProgress()`` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    
    
    def AdvanceProgress(self, stepNumber: int) -> None:
        """
        Advances the progress bar.  
        
        Signature ``AdvanceProgress(stepNumber)`` 
        
        :param stepNumber: 
        :type stepNumber: int 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design")
        """
        ...
    


class ShipSession():
    """
    Represents Ship session   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX11.0.0
    """
    Navigators: NavigatorCollection = ...
    """
    Returns the :py:class:`NXOpen.ShipDesign.NavigatorCollection` belonging to this session 
    
    Signature ``Navigators`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShipDesign.NavigatorCollection`
    """
    Generator: Generator = ...
    """
    Returns the :py:class:`NXOpen.ShipDesign.Generator` belonging to this session 
    
    Signature ``Generator`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShipDesign.Generator`
    """
    GeneralArrangement: GeneralArrangementManager = ...
    """
    Returns the :py:class:`NXOpen.ShipDesign.GeneralArrangementManager` belonging to this session 
    
    Signature ``GeneralArrangement`` 
    
    .. versionadded:: NX12.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShipDesign.GeneralArrangementManager`
    """
    ApplicationUtils: ApplicationUtils = ...
    """
    Returns the :py:class:`NXOpen.ShipDesign.ApplicationUtils` belonging to this session 
    
    Signature ``ApplicationUtils`` 
    
    .. versionadded:: NX11.0.0
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShipDesign.ApplicationUtils`
    """


class Navigator(NXOpen.NXObject):
    """
    Represents the interface for navigator action classes  
    
    Use the :py:class:`NXOpen.ShipDesign.NavigatorCollection` class to get a navigator
    
    .. versionadded:: NX11.0.1
    """
    
    @typing.overload
    def Hide(self) -> None:
        """
        Hides a navigator. 
        
        Signature ``Hide()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    @typing.overload
    def Hide(self, hideNavigator: bool) -> None:
        """
        Hides a navigator. 
        
        Signature ``Hide(hideNavigator)`` 
        
        :param hideNavigator: 
        :type hideNavigator: bool 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def ShowView(self, viewIndex: int) -> None:
        """
        Shows a navigator view.  
        
        Signature ``ShowView(viewIndex)`` 
        
        :param viewIndex: 
        :type viewIndex: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def HideView(self, viewIndex: int) -> None:
        """
        Hides a navigator view.  
        
        Signature ``HideView(viewIndex)`` 
        
        :param viewIndex: 
        :type viewIndex: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetViewCount(self) -> int:
        """
        Gets navigator view count.  
        
        Signature ``GetViewCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetView(self, viewIndex: int) -> NavigatorView:
        """
        Gets navigator view.  
        
        Signature ``GetView(viewIndex)`` 
        
        :param viewIndex: 
        :type viewIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorView` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RegisterNodeContextMenuItem(self, title: str, icon: str, actionCB: typing.Callable, visibilityCB: typing.Callable, isDefaultCB: typing.Callable) -> None:
        """
        Registers node context menu.  
        
        Signature ``RegisterNodeContextMenuItem(title, icon, actionCB, visibilityCB, isDefaultCB)`` 
        
        :param title: 
        :type title: str 
        :param icon: 
        :type icon: str 
        :param actionCB: 
        :type actionCB: CallableObject 
        :param visibilityCB: 
        :type visibilityCB: CallableObject 
        :param isDefaultCB: 
        :type isDefaultCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RegisterViewContextMenuItem(self, title: str, icon: str, actionCB: typing.Callable, visibilityCB: typing.Callable) -> None:
        """
        Registers view context menu.  
        
        Signature ``RegisterViewContextMenuItem(title, icon, actionCB, visibilityCB)`` 
        
        :param title: 
        :type title: str 
        :param icon: 
        :type icon: str 
        :param actionCB: 
        :type actionCB: CallableObject 
        :param visibilityCB: 
        :type visibilityCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetNodeSelectedCallback(self, selectedCB: typing.Callable) -> None:
        """
        Sets node selected callback.  
        
        Signature ``SetNodeSelectedCallback(selectedCB)`` 
        
        :param selectedCB: 
        :type selectedCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetNodeDeselectedCallback(self, deselectedCB: typing.Callable) -> None:
        """
        Sets node deselected callback.  
        
        Signature ``SetNodeDeselectedCallback(deselectedCB)`` 
        
        :param deselectedCB: 
        :type deselectedCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetNodeCheckCallback(self, checkCB: typing.Callable) -> None:
        """
        Sets node check callback.  
        
        Signature ``SetNodeCheckCallback(checkCB)`` 
        
        :param checkCB: 
        :type checkCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetRootPart(self, rootPart: NXOpen.BasePart) -> None:
        """
        Sets root part to load navigator model.  
        
        Signature ``SetRootPart(rootPart)`` 
        
        :param rootPart: 
        :type rootPart: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetRootPart(self) -> NXOpen.BasePart:
        """
        Gets root part to load navigator model.  
        
        Signature ``GetRootPart()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RegisterNodesContextMenuItem(self, title: str, icon: str, actionCB: typing.Callable, visibilityCB: typing.Callable, isDefaultCB: typing.Callable) -> None:
        """
        Registers multiple nodes context menu.  
        
        Signature ``RegisterNodesContextMenuItem(title, icon, actionCB, visibilityCB, isDefaultCB)`` 
        
        :param title: 
        :type title: str 
        :param icon: 
        :type icon: str 
        :param actionCB: 
        :type actionCB: CallableObject 
        :param visibilityCB: 
        :type visibilityCB: CallableObject 
        :param isDefaultCB: 
        :type isDefaultCB: CallableObject 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    Null: Navigator = ...  # unknown typename


class NavigatorView(NXOpen.NXObject):
    """
    Represents the interface for navigator view classes  
    
    Use the :py:class:`NXOpen.ShipDesign.Navigator` class to get a navigator view
    
    .. versionadded:: NX11.0.0
    """
    
    def AddRootNode(self, name: str, nodeObjects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Adds a root object to the navigator to represent the object.  
        
        Signature ``AddRootNode(name, nodeObjects)`` 
        
        :param name: 
        :type name: str 
        :param nodeObjects: 
        :type nodeObjects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetRootNode(self) -> NavigatorNode:
        """
        Gets root node.  
        
        Signature ``GetRootNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RemoveRootNode(self) -> None:
        """
        Removes root node.  
        
        Signature ``RemoveRootNode()`` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetSelectedNodes(self) -> 'list[NavigatorNode]':
        """
        Gets selected nodes.  
        
        Signature ``GetSelectedNodes()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetSelectedNodes(self, selectedNodes: 'list[NavigatorNode]') -> None:
        """
        Sets selected nodes.  
        
        Signature ``SetSelectedNodes(selectedNodes)`` 
        
        :param selectedNodes: 
        :type selectedNodes: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetLastSelectedNode(self, selectedNode: NavigatorNode) -> None:
        """
        Sets last selected node.  
        
        Signature ``SetLastSelectedNode(selectedNode)`` 
        
        :param selectedNode: 
        :type selectedNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetLastSelectedNode(self) -> NavigatorNode:
        """
        Gets last selected node.  
        
        Signature ``GetLastSelectedNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    Null: NavigatorView = ...  # unknown typename


class ShipNavigatorRoot(NXOpen.NXObject):
    """
    Represents the interface for ship navigator root classes.  
    
    An instance of this class can be obtained from :py:meth:`NXOpen.ShipDesign.NavigatorCollection.GetShipNavigatorRoot`
    
    .. versionadded:: NX11.0.1
    """
    Null: ShipNavigatorRoot = ...  # unknown typename


class NavigatorCollection():
    """
    Represents the interface for navigator action classes  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.ShipDesign.ShipSession`
    
    .. versionadded:: NX11.0.1
    """
    
    def ShowNavigator(self, index: int, bitmap: str, tooltip: str, name: str) -> Navigator:
        """
        Shows the navigator.  
        
        Signature ``ShowNavigator(index, bitmap, tooltip, name)`` 
        
        :param index: 
        :type index: int 
        :param bitmap: 
        :type bitmap: str 
        :param tooltip: 
        :type tooltip: str 
        :param name: 
        :type name: str 
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.Navigator` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RegisterNavigator(self, index: int, bitmap: str, tooltip: str, name: str) -> None:
        """
        Registers the navigator.  
        
        Signature ``RegisterNavigator(index, bitmap, tooltip, name)`` 
        
        :param index: 
        :type index: int 
        :param bitmap: 
        :type bitmap: str 
        :param tooltip: 
        :type tooltip: str 
        :param name: 
        :type name: str 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def UnregisterNavigator(self, index: int) -> None:
        """
        Unregisters the navigator.  
        
        Signature ``UnregisterNavigator(index)`` 
        
        :param index: 
        :type index: int 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def IsNavigatorRegistered(self, index: int) -> bool:
        """
        Checks if ship navigator is registered.  
        
        Signature ``IsNavigatorRegistered(index)`` 
        
        :param index: 
        :type index: int 
        :returns: 
        :rtype: bool 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetNavigatorCount(self) -> int:
        """
        Gets navigator count.  
        
        Signature ``GetNavigatorCount()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def ActiveNavigator(self, index: int) -> None:
        """
        Actives ship navigator.  
        
        Signature ``ActiveNavigator(index)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetNavigator(self, index: int) -> Navigator:
        """
        Gets ship navigator.  
        
        Signature ``GetNavigator(index)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.Navigator` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RefreshNavigator(self, index: int) -> None:
        """
        Loads navigator models.  
        
        Signature ``RefreshNavigator(index)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetShipNavigatorRoot(self) -> ShipNavigatorRoot:
        """
        Establish ship navigator root  
        
        Signature ``GetShipNavigatorRoot()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.ShipNavigatorRoot` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def UnloadPartAndItsChildren(self, partTag: NXOpen.BasePart) -> None:
        """
        Unloads part and its children.  
        
        Signature ``UnloadPartAndItsChildren(partTag)`` 
        
        :param partTag: 
        :type partTag: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SaveConfigureFile(self, index: int) -> None:
        """
        Saves the configure file.  
        
        Signature ``SaveConfigureFile(index)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def ChangeNodeState(self, tgTargetNode: NavigatorNode, status: int) -> None:
        """
        Change node state.  
        
        Signature ``ChangeNodeState(tgTargetNode, status)`` 
        
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        :param status: 
        :type status: int 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RemoveNodes(self, index: int, tgNodes: 'list[NavigatorNode]') -> None:
        """
        Remove navigator nodes.  
        
        Signature ``RemoveNodes(index, tgNodes)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgNodes: 
        :type tgNodes: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def CopyNode(self, index: int, tgNodes: 'list[NavigatorNode]') -> None:
        """
        Copy navigator node.  
        
        Signature ``CopyNode(index, tgNodes)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgNodes: 
        :type tgNodes: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def CutNode(self, index: int, tgNodes: 'list[NavigatorNode]') -> None:
        """
        Cut navigator node.  
        
        Signature ``CutNode(index, tgNodes)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgNodes: 
        :type tgNodes: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def PasteNode(self, index: int, tgTargetNode: NavigatorNode) -> None:
        """
        Paste navigator node.  
        
        Signature ``PasteNode(index, tgTargetNode)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def ReparentNode(self, index: int, tgTargetNode: NavigatorNode, tgSourceNode: NavigatorNode) -> None:
        """
        Reparent navigator node.  
        
        Signature ``ReparentNode(index, tgTargetNode, tgSourceNode)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        :param tgSourceNode: 
        :type tgSourceNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def ReparentNodes(self, index: int, tgTargetNode: NavigatorNode, tgNodes: 'list[NavigatorNode]') -> None:
        """
        Reparent navigator nodes.  
        
        Signature ``ReparentNodes(index, tgTargetNode, tgNodes)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        :param tgNodes: 
        :type tgNodes: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetNodeName(self, tgTargetNode: NavigatorNode, name: str) -> None:
        """
        Set node name.  
        
        Signature ``SetNodeName(tgTargetNode, name)`` 
        
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        :param name: 
        :type name: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetActiveNode(self, index: int, tgTargetNode: NavigatorNode) -> None:
        """
        Set selected node as active node.  
        
        Signature ``SetActiveNode(index, tgTargetNode)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SendToSubView(self, index: int, tgTargetNode: NavigatorNode) -> None:
        """
        Send node to sub view.  
        
        Signature ``SendToSubView(index, tgTargetNode)`` 
        
        :param index:  ship navigator id  
        :type index: int 
        :param tgTargetNode: 
        :type tgTargetNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def CreateShipNavigatorNodeBuilder(self, isEdit: bool, tgNode: NavigatorNode) -> ShipNavigatorNodeBuilder:
        """
        Creates a :py:class:`NXOpen.ShipDesign.ShipNavigatorNodeBuilder`.  
        
        Signature ``CreateShipNavigatorNodeBuilder(isEdit, tgNode)`` 
        
        :param isEdit: 
        :type isEdit: bool 
        :param tgNode: 
        :type tgNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.ShipNavigatorNodeBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def EditFeature(self, tgFeat: NXOpen.Features.Feature) -> None:
        """
        Edit feature.  
        
        Signature ``EditFeature(tgFeat)`` 
        
        :param tgFeat:  :py:class:`NXOpen.Features.Feature` to be edited  
        :type tgFeat: :py:class:`NXOpen.Features.Feature` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetReferencingNodes(self, tgReferencedObject: NXOpen.TaggedObject) -> 'list[NavigatorNode]':
        """
        Gets all referencing navigator nodes.  
        
        Signature ``GetReferencingNodes(tgReferencedObject)`` 
        
        :param tgReferencedObject: 
        :type tgReferencedObject: :py:class:`NXOpen.TaggedObject` 
        :returns: 
        :rtype: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def PopulateAndPrintShipNavigator(self, displayPart: NXOpen.BasePart) -> None:
        """
        Populates and prints data for each navigator found.  
        
        Signature ``PopulateAndPrintShipNavigator(displayPart)`` 
        
        :param displayPart:  part being validated  
        :type displayPart: :py:class:`NXOpen.BasePart` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: None.
        """
        ...
    


class NavigatorNode(NXOpen.NXObject):
    """
    Represents the interface for navigator view classes  
    
    Use the :py:class:`NXOpen.ShipDesign.NavigatorView` class to create a navigator node
    
    .. versionadded:: NX11.0.1
    """
    
    def GetNodeObjects(self) -> 'list[NXOpen.TaggedObject]':
        """
        Gets the objects represented by the node.  
        
        Signature ``GetNodeObjects()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetNodeObjects(self, nodeObjects: 'list[NXOpen.TaggedObject]') -> None:
        """
        Sets the objects represented by the node.  
        
        Signature ``SetNodeObjects(nodeObjects)`` 
        
        :param nodeObjects: 
        :type nodeObjects: list of :py:class:`NXOpen.TaggedObject` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def AddChild(self, name: str, nodeObjects: 'list[NXOpen.TaggedObject]', createPersistentData: bool) -> NavigatorNode:
        """
        Adds a child node.  
        
        Signature ``AddChild(name, nodeObjects, createPersistentData)`` 
        
        :param name: 
        :type name: str 
        :param nodeObjects: 
        :type nodeObjects: list of :py:class:`NXOpen.TaggedObject` 
        :param createPersistentData: 
        :type createPersistentData: bool 
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def RemoveChild(self, childNode: NavigatorNode) -> None:
        """
        Removes a child node.  
        
        Signature ``RemoveChild(childNode)`` 
        
        :param childNode: 
        :type childNode: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetParent(self) -> NavigatorNode:
        """
        Gets parent node.  
        
        Signature ``GetParent()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetChildren(self) -> 'list[NavigatorNode]':
        """
        Gets children nodes.  
        
        Signature ``GetChildren()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetNextNode(self) -> NavigatorNode:
        """
        Get next node.  
        
        If this node has some child nodes, the next node is the first child.
        Otherwise return next sibling of this node, or its parent node, or its grandparent node...   
        
        Signature ``GetNextNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetPreviousNode(self) -> NavigatorNode:
        """
        Get previous node.  
        
        If this node has no prior siblings, the previous node is its parent node if it has. 
        If this node has a prior sibling, the previous node is the last descendant node of this previous sibling.  
        
        Signature ``GetPreviousNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetNextSiblingNode(self) -> NavigatorNode:
        """
        Gets next sibling node.  
        
        Signature ``GetNextSiblingNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetPreviousSiblingNode(self) -> NavigatorNode:
        """
        Gets previous sibling node.  
        
        Signature ``GetPreviousSiblingNode()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.ShipDesign.NavigatorNode` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetIcon(self, icon: str) -> None:
        """
        Sets the node icon.  
        
        Signature ``SetIcon(icon)`` 
        
        :param icon: 
        :type icon: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def SetDraggable(self, draggable: bool) -> None:
        """
        Sets the node draggable attribute.  
        
        Signature ``SetDraggable(draggable)`` 
        
        :param draggable: 
        :type draggable: bool 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def UpdateProperty(self, propertyName: str, propertyValue: str) -> None:
        """
        Sets the node property.  
        
        Signature ``UpdateProperty(propertyName, propertyValue)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :param propertyValue: 
        :type propertyValue: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    
    def GetProperty(self, propertyName: str) -> str:
        """
        Gets the node property.  
        
        Signature ``GetProperty(propertyName)`` 
        
        :param propertyName: 
        :type propertyName: str 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX11.0.1
        
        License requirements: nx_ship_basic ("Ship Basic Design")
        """
        ...
    
    CheckStatus: bool = ...
    """
    Returns or sets  the node check status.  
    
    <hr>
    
    Getter Method
    
    Signature ``CheckStatus`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CheckStatus`` 
    
    :param checkStatus: 
    :type checkStatus: bool 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_ship_basic ("Ship Basic Design")
    """
    Modifiable: bool = ...
    """
    Returns or sets  the node modifiable property.  
    
    <hr>
    
    Getter Method
    
    Signature ``Modifiable`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Modifiable`` 
    
    :param modifiable: 
    :type modifiable: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: nx_ship_basic ("Ship Basic Design")
    """
    Title: str = ...
    """
    Returns or sets  the node title.  
    
    <hr>
    
    Getter Method
    
    Signature ``Title`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Title`` 
    
    :param title: 
    :type title: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: nx_ship_basic ("Ship Basic Design")
    """
    Null: NavigatorNode = ...  # unknown typename


