# module 'NXOpen.CAM.FBM'
#
# Automatically generated 2025-06-09T14:38:44.839879
#

import typing

import NXOpen
import NXOpen.CAM



class FeatureGeometrySortOrderMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FeatureGeometrySortOrder():
    """
    the optimization types   
    
    .. versionadded:: NX9.0.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Closest", "Sort order: Closet"
       "ShortestPath", "Sort order: Shortest Path"
       "PrimaryDirection", "Sort order: Primary Direction"
    """
    Closest = 0  # FeatureGeometrySortOrderMemberType
    ShortestPath = 1  # FeatureGeometrySortOrderMemberType
    PrimaryDirection = 2  # FeatureGeometrySortOrderMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FeatureGeometrySequenceDirectionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FeatureGeometrySequenceDirectionType():
    """
    the direction types   
    
    .. versionadded:: NX9.0.2
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Xm", "Direction: XM"
       "Ym", "Direction: YM"
       "Zm", "Direction: ZM"
       "Vector", "Direction: Vector"
    """
    Xm = 0  # FeatureGeometrySequenceDirectionTypeMemberType
    Ym = 1  # FeatureGeometrySequenceDirectionTypeMemberType
    Zm = 2  # FeatureGeometrySequenceDirectionTypeMemberType
    Vector = 3  # FeatureGeometrySequenceDirectionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FeatureGeometrySequencePatternTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class FeatureGeometrySequencePatternType():
    """
    the pattern types   
    
    .. versionadded:: NX9.0.2
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Zig", "Pattern: Zig"
       "ZigZag", "Pattern: Zig Zag"
    """
    Zig = 0  # FeatureGeometrySequencePatternTypeMemberType
    ZigZag = 1  # FeatureGeometrySequencePatternTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class FeatureGeometry(NXOpen.CAM.Geometry):
    """
    Represents a feature geometry builder   
    
    This is an abstract class and cannot be instantiated.
    
    .. versionadded:: NX9.0.1
    """
    
    class SortOrder():
        """
        the optimization types   
        
        .. versionadded:: NX9.0.1
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Closest", "Sort order: Closet"
           "ShortestPath", "Sort order: Shortest Path"
           "PrimaryDirection", "Sort order: Primary Direction"
        """
        Closest = 0  # FeatureGeometrySortOrderMemberType
        ShortestPath = 1  # FeatureGeometrySortOrderMemberType
        PrimaryDirection = 2  # FeatureGeometrySortOrderMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SequenceDirectionType():
        """
        the direction types   
        
        .. versionadded:: NX9.0.2
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Xm", "Direction: XM"
           "Ym", "Direction: YM"
           "Zm", "Direction: ZM"
           "Vector", "Direction: Vector"
        """
        Xm = 0  # FeatureGeometrySequenceDirectionTypeMemberType
        Ym = 1  # FeatureGeometrySequenceDirectionTypeMemberType
        Zm = 2  # FeatureGeometrySequenceDirectionTypeMemberType
        Vector = 3  # FeatureGeometrySequenceDirectionTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class SequencePatternType():
        """
        the pattern types   
        
        .. versionadded:: NX9.0.2
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Zig", "Pattern: Zig"
           "ZigZag", "Pattern: Zig Zag"
        """
        Zig = 0  # FeatureGeometrySequencePatternTypeMemberType
        ZigZag = 1  # FeatureGeometrySequencePatternTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def CreateFeatureSet(self) -> FeatureSet:
        """
        Create a new empty feature editor 
        
        Signature ``CreateFeatureSet()`` 
        
        :returns:  the new in process feature set  
        :rtype: :py:class:`NXOpen.CAM.FBM.FeatureSet` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def AddFeatureSet(self, tagMachiningFeature: NXOpen.CAM.CAMFeature, featureType: str) -> FeatureSet:
        """
        Creates a feature geometry set  
        
        Signature ``AddFeatureSet(tagMachiningFeature, featureType)`` 
        
        :param tagMachiningFeature:  the machining feature  
        :type tagMachiningFeature: :py:class:`NXOpen.CAM.CAMFeature` 
        :param featureType:  the in process feature type  
        :type featureType: str 
        :returns:  the new in process feature set  
        :rtype: :py:class:`NXOpen.CAM.FBM.FeatureSet` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def GetFeatureSet(self, nIndex: int) -> FeatureSet:
        """
        Get the in process feature editor at the specified index  
        
        Signature ``GetFeatureSet(nIndex)`` 
        
        :param nIndex:  the index of the feature set editor  
        :type nIndex: int 
        :returns:  the in process feature set  
        :rtype: :py:class:`NXOpen.CAM.FBM.FeatureSet` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    @typing.overload
    def SetDefaultAttribute(self, attributeName: str, dValue: float) -> None:
        """
        Sets a default attribute value 
        
        Signature ``SetDefaultAttribute(attributeName, dValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param dValue:  the attribute value  
        :type dValue: float 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetDefaultAttribute(self, attributeName: str, strValue: str) -> None:
        """
        Sets a default attribute value 
        
        Signature ``SetDefaultAttribute(attributeName, strValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param strValue:  the attribute value  
        :type strValue: str 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetDefaultAttribute(self, attributeName: str, nValue: int) -> None:
        """
        Sets a default attribute value 
        
        Signature ``SetDefaultAttribute(attributeName, nValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param nValue:  the attribute value  
        :type nValue: int 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetDefaultAttribute(self, attributeName: str, bValue: bool) -> None:
        """
        Sets a default attribute value 
        
        Signature ``SetDefaultAttribute(attributeName, bValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param bValue:  the attribute value  
        :type bValue: bool 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def ReorderFeatures(self, sortType: FeatureGeometrySortOrder) -> None:
        """
        Reorders the features according to a predefined algorithm 
        
        Signature ``ReorderFeatures(sortType)`` 
        
        :param sortType: 
        :type sortType: :py:class:`NXOpen.CAM.FBM.FeatureGeometrySortOrder` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    @typing.overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometrySequenceDirectionType, pattern: FeatureGeometrySequencePatternType, vecValue: NXOpen.Vector3d) -> None:
        """
        Reorders the features according to primary direction 
        
        Signature ``ReorderFeaturesByDirection(direction, pattern, vecValue)`` 
        
        :param direction: 
        :type direction: :py:class:`NXOpen.CAM.FBM.FeatureGeometrySequenceDirectionType` 
        :param pattern: 
        :type pattern: :py:class:`NXOpen.CAM.FBM.FeatureGeometrySequencePatternType` 
        :param vecValue: 
        :type vecValue: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def ReorderFeaturesByDirection(self, direction: FeatureGeometrySequenceDirectionType, pattern: FeatureGeometrySequencePatternType, vecValue: NXOpen.Vector3d, bandWidth: float) -> None:
        """
        Reorders the features according to primary direction with band width 
        
        Signature ``ReorderFeaturesByDirection(direction, pattern, vecValue, bandWidth)`` 
        
        :param direction: 
        :type direction: :py:class:`NXOpen.CAM.FBM.FeatureGeometrySequenceDirectionType` 
        :param pattern: 
        :type pattern: :py:class:`NXOpen.CAM.FBM.FeatureGeometrySequencePatternType` 
        :param vecValue: 
        :type vecValue: :py:class:`NXOpen.Vector3d` 
        :param bandWidth: 
        :type bandWidth: float 
        
        .. versionadded:: NX9.0.3
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def ReverseFeatures(self) -> None:
        """
        Reverse the features 
        
        Signature ``ReverseFeatures()`` 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def ReloadList(self) -> None:
        """
        Reload list from parent 
        
        Signature ``ReloadList()`` 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def SetMachiningArea(self, machiningArea: str) -> None:
        """
        Change machining area 
        
        Signature ``SetMachiningArea(machiningArea)`` 
        
        :param machiningArea:  the machining area  
        :type machiningArea: str 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def GetMachiningArea(self) -> str:
        """
        Returns the machining area  
        
        Signature ``GetMachiningArea()`` 
        
        :returns:  the machining area  
        :rtype: str 
        
        .. versionadded:: NX9.0.2
        
        License requirements: None.
        """
        ...
    
    
    def CreateFeatures(self, objects: 'list[NXOpen.NXObject]', featureType: str) -> 'list[Feature]':
        """
        Create a series of (in process) features.  
        
        Depending on the input objects feature recognition is performed. When
        no known features can be recognized, tagged features are created of type featureType  
        
        Signature ``CreateFeatures(objects, featureType)`` 
        
        :param objects:  the geometry objects, can also be machining features  
        :type objects: list of :py:class:`NXOpen.NXObject` 
        :param featureType:  the machining feature type of the implictly created features when feature recognition fails  
        :type featureType: str 
        :returns: 
        :rtype: list of :py:class:`NXOpen.CAM.FBM.Feature` 
        
        .. versionadded:: NX10.0.3
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    UseModelDepth: bool = ...
    """
    Returns or sets  the use model depth flag 
    
    <hr>
    
    Getter Method
    
    Signature ``UseModelDepth`` 
    
    :returns:  the use model depth flag  
    :rtype: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UseModelDepth`` 
    
    :param flag: 
    :type flag: bool 
    
    .. versionadded:: NX11.0.2
    
    License requirements: cam_base ("CAM BASE")
    """
    Null: FeatureGeometry = ...  # unknown typename
    
    def __repr__(self) -> None:
        """Return repr(self)."""
        ...
    
    
    def __hash__(self) -> None:
        """Return hash(self)."""
        ...
    
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    
    def __getattribute__(self) -> None:
        """Return getattr(self, name)."""
        ...
    
    
    def __setattr__(self) -> None:
        """Implement setattr(self, name, value)."""
        ...
    
    
    def __delattr__(self) -> None:
        """Implement delattr(self, name)."""
        ...
    
    
    def __lt__(self) -> None:
        """Return self<value."""
        ...
    
    
    def __le__(self) -> None:
        """Return self<=value."""
        ...
    
    
    def __eq__(self) -> None:
        """Return self==value."""
        ...
    
    
    def __ne__(self) -> None:
        """Return self!=value."""
        ...
    
    
    def __gt__(self) -> None:
        """Return self>value."""
        ...
    
    
    def __ge__(self) -> None:
        """Return self>=value."""
        ...
    


class ThreadFeatureGeometryThreadDataSourceMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ThreadFeatureGeometryThreadDataSource():
    """
    thread data source types   
    
    .. versionadded:: NX9.0.1
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "FromModel", "From Model"
       "FromTable", "From Table"
    """
    FromModel = 0  # ThreadFeatureGeometryThreadDataSourceMemberType
    FromTable = 1  # ThreadFeatureGeometryThreadDataSourceMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ThreadFeatureGeometryFormMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ThreadFeatureGeometryForm():
    """
    Thread form standards   
    
    .. versionadded:: NX9.0.2
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unified", "Form: Unified"
       "Acme", "Form: Acme"
       "StubAcme", "Form: Stub Acme"
       "Buttress", "Form: Buttress"
       "Metric", "Form: Metric"
       "Trapezoidal", "Form: Trapezoidal"
       "Lowernherz", "Form: Lowenherz"
       "SparkPlug", "Form: Spark Plug"
       "Npt", "Form: NPT"
       "HoseCoupling", "Form: Hose Coupling"
       "FireHose", "Form: Fire Hose"
       "Unj", "Form: UNJ"
       "Nps", "Form: NPS"
       "Bsp", "Form: BSP"
       "Bstp", "Form: BSTP"
       "Helicoil", "Form: Helicoil"
       "Ns", "Form: NS"
       "UserDefined", "Form: User defined"
    """
    Unified = 0  # ThreadFeatureGeometryFormMemberType
    Acme = 1  # ThreadFeatureGeometryFormMemberType
    StubAcme = 2  # ThreadFeatureGeometryFormMemberType
    Buttress = 4  # ThreadFeatureGeometryFormMemberType
    Metric = 5  # ThreadFeatureGeometryFormMemberType
    Trapezoidal = 8  # ThreadFeatureGeometryFormMemberType
    Lowernherz = 9  # ThreadFeatureGeometryFormMemberType
    SparkPlug = 10  # ThreadFeatureGeometryFormMemberType
    Npt = 11  # ThreadFeatureGeometryFormMemberType
    HoseCoupling = 12  # ThreadFeatureGeometryFormMemberType
    FireHose = 13  # ThreadFeatureGeometryFormMemberType
    Unj = 14  # ThreadFeatureGeometryFormMemberType
    Nps = 15  # ThreadFeatureGeometryFormMemberType
    Bsp = 16  # ThreadFeatureGeometryFormMemberType
    Bstp = 17  # ThreadFeatureGeometryFormMemberType
    Helicoil = 18  # ThreadFeatureGeometryFormMemberType
    Ns = 19  # ThreadFeatureGeometryFormMemberType
    UserDefined = 20  # ThreadFeatureGeometryFormMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ThreadFeatureGeometryRotationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ThreadFeatureGeometryRotation():
    """
    the rotation types   
    
    .. versionadded:: NX9.0.2
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "RightHand", "Rotation: Right-hand"
       "LeftHand", "Rotation: Left-hand"
    """
    RightHand = 0  # ThreadFeatureGeometryRotationMemberType
    LeftHand = 1  # ThreadFeatureGeometryRotationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ThreadFeatureGeometry(FeatureGeometry):
    """
    Represents a feature geometry builder   
    
    This is an abstract class and cannot be instantiated.
    
    .. versionadded:: NX9.0.1
    """
    
    class ThreadDataSource():
        """
        thread data source types   
        
        .. versionadded:: NX9.0.1
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "FromModel", "From Model"
           "FromTable", "From Table"
        """
        FromModel = 0  # ThreadFeatureGeometryThreadDataSourceMemberType
        FromTable = 1  # ThreadFeatureGeometryThreadDataSourceMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Form():
        """
        Thread form standards   
        
        .. versionadded:: NX9.0.2
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unified", "Form: Unified"
           "Acme", "Form: Acme"
           "StubAcme", "Form: Stub Acme"
           "Buttress", "Form: Buttress"
           "Metric", "Form: Metric"
           "Trapezoidal", "Form: Trapezoidal"
           "Lowernherz", "Form: Lowenherz"
           "SparkPlug", "Form: Spark Plug"
           "Npt", "Form: NPT"
           "HoseCoupling", "Form: Hose Coupling"
           "FireHose", "Form: Fire Hose"
           "Unj", "Form: UNJ"
           "Nps", "Form: NPS"
           "Bsp", "Form: BSP"
           "Bstp", "Form: BSTP"
           "Helicoil", "Form: Helicoil"
           "Ns", "Form: NS"
           "UserDefined", "Form: User defined"
        """
        Unified = 0  # ThreadFeatureGeometryFormMemberType
        Acme = 1  # ThreadFeatureGeometryFormMemberType
        StubAcme = 2  # ThreadFeatureGeometryFormMemberType
        Buttress = 4  # ThreadFeatureGeometryFormMemberType
        Metric = 5  # ThreadFeatureGeometryFormMemberType
        Trapezoidal = 8  # ThreadFeatureGeometryFormMemberType
        Lowernherz = 9  # ThreadFeatureGeometryFormMemberType
        SparkPlug = 10  # ThreadFeatureGeometryFormMemberType
        Npt = 11  # ThreadFeatureGeometryFormMemberType
        HoseCoupling = 12  # ThreadFeatureGeometryFormMemberType
        FireHose = 13  # ThreadFeatureGeometryFormMemberType
        Unj = 14  # ThreadFeatureGeometryFormMemberType
        Nps = 15  # ThreadFeatureGeometryFormMemberType
        Bsp = 16  # ThreadFeatureGeometryFormMemberType
        Bstp = 17  # ThreadFeatureGeometryFormMemberType
        Helicoil = 18  # ThreadFeatureGeometryFormMemberType
        Ns = 19  # ThreadFeatureGeometryFormMemberType
        UserDefined = 20  # ThreadFeatureGeometryFormMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Rotation():
        """
        the rotation types   
        
        .. versionadded:: NX9.0.2
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "RightHand", "Rotation: Right-hand"
           "LeftHand", "Rotation: Left-hand"
        """
        RightHand = 0  # ThreadFeatureGeometryRotationMemberType
        LeftHand = 1  # ThreadFeatureGeometryRotationMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def SetThreadDataSource(self, source: ThreadFeatureGeometryThreadDataSource) -> None:
        """
        Sets the source type for retrieving thread data 
        
        Signature ``SetThreadDataSource(source)`` 
        
        :param source:  thread data source type  
        :type source: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryThreadDataSource` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def GetThreadDataSource(self) -> ThreadFeatureGeometryThreadDataSource:
        """
        Gets the source type for retrieving thread data  
        
        Signature ``GetThreadDataSource()`` 
        
        :returns:  thread data source type  
        :rtype: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryThreadDataSource` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetFormUserDefined(self) -> str:
        """
        Get the user defined form standard  
        
        Signature ``GetFormUserDefined()`` 
        
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.2
        
        License requirements: None.
        """
        ...
    
    
    def SetFormUserDefined(self, userDefinedForm: str) -> None:
        """
        Set the user defined form standard 
        
        Signature ``SetFormUserDefined(userDefinedForm)`` 
        
        :param userDefinedForm: 
        :type userDefinedForm: str 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def UpdateThreadParameters(self, tagFeature: Feature) -> None:
        """
        Update the feature thread parameters 
        
        Signature ``UpdateThreadParameters(tagFeature)`` 
        
        :param tagFeature: 
        :type tagFeature: :py:class:`NXOpen.CAM.FBM.Feature` 
        
        .. versionadded:: NX9.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    FormStandard: ThreadFeatureGeometryForm = ...
    """
    Returns or sets  the form standard 
    
    <hr>
    
    Getter Method
    
    Signature ``FormStandard`` 
    
    :returns:  form standard  
    :rtype: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryForm` 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FormStandard`` 
    
    :param standard:  form standard  
    :type standard: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryForm` 
    
    .. versionadded:: NX9.0.2
    
    License requirements: cam_base ("CAM BASE")
    """
    ThreadRotation: ThreadFeatureGeometryRotation = ...
    """
    Returns or sets  the thread rotation 
    
    <hr>
    
    Getter Method
    
    Signature ``ThreadRotation`` 
    
    :returns:  thread rotation  
    :rtype: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryRotation` 
    
    .. versionadded:: NX9.0.2
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ThreadRotation`` 
    
    :param rotation:  thread rotation  
    :type rotation: :py:class:`NXOpen.CAM.FBM.ThreadFeatureGeometryRotation` 
    
    .. versionadded:: NX9.0.2
    
    License requirements: cam_base ("CAM BASE")
    """
    Null: ThreadFeatureGeometry = ...  # unknown typename


class Feature(NXOpen.NXObject, NXOpen.IFitTo):
    """
    Interface for CAM Feature objects   
    
    This is an abstract class, and cannot be instantiated.
    
    .. versionadded:: NX9.0.0
    """
    
    def GetAttribute(self, attributeName: str) -> NXOpen.CAM.CAMAttribute:
        """
        Gets and attribute  
        
        Signature ``GetAttribute(attributeName)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :returns:  the attribute  
        :rtype: :py:class:`NXOpen.CAM.CAMAttribute` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
        Sets the attribute value 
        
        Signature ``SetAttributeValue(attributeName, dValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param dValue:  the attribute value  
        :type dValue: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
        Sets the attribute value 
        
        Signature ``SetAttributeValue(attributeName, strValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param strValue:  the attribute value  
        :type strValue: str 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
        Sets the attribute value 
        
        Signature ``SetAttributeValue(attributeName, nValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param nValue:  the attribute value  
        :type nValue: int 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
        Sets the attribute value 
        
        Signature ``SetAttributeValue(attributeName, bValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param bValue:  the attribute value  
        :type bValue: bool 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    @typing.overload
    def SetAttribute(self, tagAttribute: NXOpen.CAM.CAMAttribute) -> None:
        """
        Sets the attribute value(s) to the same value(s) as another attribute 
        
        Signature ``SetAttribute(tagAttribute)`` 
        
        :param tagAttribute:  the attribute  
        :type tagAttribute: :py:class:`NXOpen.CAM.CAMAttribute` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: int) -> None:
        """
        Creates or modifies an integer attribute.  This method performs an immediate update
        except when the object is a :py:class:`NXOpen.Features.Feature`. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: int 
        
        .. versionadded:: NX3.0.0
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: int, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies an integer attribute with the option to update or not. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value, option)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: int 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX5.0.1
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: float) -> None:
        """
        Creates or modifies a real attribute.  This method performs an immediate update
        except when the object is a :py:class:`NXOpen.Features.Feature`. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: float 
        
        .. versionadded:: NX3.0.0
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: float, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a real attribute with the option to update or not. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value, option)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: float 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX5.0.1
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: str) -> None:
        """
        Creates or modifies a string attribute.  This method performs an immediate update
        except when the object is a :py:class:`NXOpen.Features.Feature`. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: str 
        
        .. versionadded:: NX3.0.0
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, value: str, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a string attribute with the option to update or not. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, value, option)`` 
        
        :param title: 
        :type title: str 
        :param value: 
        :type value: str 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX5.0.1
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str) -> None:
        """
        Creates or modifies a null attribute which is an attribute with a title and no value.
        This method performs an immediate update except when the object is a 
        :py:class:`NXOpen.Features.Feature`. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title)`` 
        
        :param title: 
        :type title: str 
        
        .. versionadded:: NX3.0.0
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAttribute(self, title: str, option: NXOpen.UpdateOption) -> None:
        """
        Creates or modifies a null attribute with the option to update or not. 
        This method does not support array attributes.
        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
        If it is, the changes will be overridden when the part is updated. 
        
        Signature ``SetAttribute(title, option)`` 
        
        :param title: 
        :type title: str 
        :param option: 
        :type option: :py:class:`NXOpen.UpdateOption` 
        
        .. versionadded:: NX5.0.1
        
        .. deprecated::  NX8.0.0
           Use :py:meth:`SetUserAttribute` instead.
        
        License requirements: None.
        """
        ...
    
    
    def GetAttributeDoubleValue(self, attributeName: str) -> float:
        """
        Returns the actual attribute value  
        
        Signature ``GetAttributeDoubleValue(attributeName)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :returns:  the attribute value  
        :rtype: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, dValue: float) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, dValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param dValue:  the attribute value  
        :type dValue: float 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, nValue: int) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, nValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param nValue:  the attribute value  
        :type nValue: int 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, bValue: bool) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, bValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param bValue:  the attribute value  
        :type bValue: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, strValue: str) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, strValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param strValue:  the attribute value  
        :type strValue: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, ptValue: NXOpen.Point3d) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, ptValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param ptValue:  the attribute value  
        :type ptValue: :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    @typing.overload
    def OverrideAttributeValue(self, attributeName: str, vecValue: NXOpen.Vector3d) -> None:
        """
        Overrides the attribute value 
        
        Signature ``OverrideAttributeValue(attributeName, vecValue)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :param vecValue:  the attribute value  
        :type vecValue: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def IsAttributeOverridden(self, attributeName: str) -> bool:
        """
        Returns true if attribute is overridden  
        
        Signature ``IsAttributeOverridden(attributeName)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        :returns:  the override flag   
        :rtype: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ResetAttributeValue(self, attributeName: str) -> None:
        """
        Resets an attribute to its original value 
        
        Signature ``ResetAttributeValue(attributeName)`` 
        
        :param attributeName:  the attribute name  
        :type attributeName: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def ResetAttributes(self) -> None:
        """
        Resets all attributes to their original value 
        
        Signature ``ResetAttributes()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def FlipDirection(self) -> None:
        """
        Flip feature direction
        
        Signature ``FlipDirection()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def SetCoordinateSystem(self, ptValue: NXOpen.Point3d, xAxis: NXOpen.Vector3d, yAxis: NXOpen.Vector3d) -> None:
        """
        Change the feature coordinate system
        
        Signature ``SetCoordinateSystem(ptValue, xAxis, yAxis)`` 
        
        :param ptValue:  the new feature origin  
        :type ptValue: :py:class:`NXOpen.Point3d` 
        :param xAxis:  the new feature x axis  
        :type xAxis: :py:class:`NXOpen.Vector3d` 
        :param yAxis:  the new feature y axis  
        :type yAxis: :py:class:`NXOpen.Vector3d` 
        
        .. versionadded:: NX9.0.1
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    
    def GetMachiningArea(self, tagEntit: NXOpen.DisplayableObject) -> str:
        """
        Returns the machining area the input entity is part of.  
        
        If the input entity is not part of the feature 
        the return string is empty 
        
        Signature ``GetMachiningArea(tagEntit)`` 
        
        :param tagEntit:  input geometry  
        :type tagEntit: :py:class:`NXOpen.DisplayableObject` 
        :returns: 
        :rtype: str 
        
        .. versionadded:: NX9.0.3
        
        License requirements: None.
        """
        ...
    
    
    def Unlock(self) -> None:
        """
        Unlock Feature
        
        Signature ``Unlock()`` 
        
        .. versionadded:: NX11.0.2
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    Null: Feature = ...  # unknown typename


class MachiningFeatureGeometry(FeatureGeometry):
    """
    Represents a feature geometry builder   
    
    An instance of this class can be obtained from :py:meth:`CAM.HoleBossGeom.GetCenterHoleGeometry` or :py:meth:`CAM.HoleBossGeom.GetChamferHoleGeometry`
    
    .. versionadded:: NX9.0.0
    """
    Null: MachiningFeatureGeometry = ...  # unknown typename


class FeatureSet(NXOpen.CAM.GeometrySet):
    """
    Interface for feature set   
    
    To create a new instance of this class, use :py:meth:`NXOpen.CAM.FBM.FeatureGeometry.CreateFeatureSet`
    
    .. versionadded:: NX9.0.0
    """
    
    def GetFeature(self) -> Feature:
        """
        Returns the feature  
        
        Signature ``GetFeature()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.CAM.FBM.Feature` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateFeature(self, entities: 'list[NXOpen.NXObject]') -> Feature:
        """
        Creates the feature using the specified tags 
        
        Signature ``CreateFeature(entities)`` 
        
        :param entities:  the input entities  
        :type entities: list of :py:class:`NXOpen.NXObject` 
        :returns: 
        :rtype: :py:class:`NXOpen.CAM.FBM.Feature` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: cam_base ("CAM BASE")
        """
        ...
    
    Null: FeatureSet = ...  # unknown typename


