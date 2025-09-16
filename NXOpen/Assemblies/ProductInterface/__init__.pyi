# module 'NXOpen.Assemblies.ProductInterface'
#
# Automatically generated 2025-06-09T14:38:43.636750
#

import typing

import NXOpen
import NXOpen.Features



class ObjectBuilderBuilderVersionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ObjectBuilderBuilderVersion():
    """
    Version number of product interface builder 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Original", "linked feature cannot select the product interface item"
       "One", "linked feature can directly select the product interface item"
       "Two", "product interface builder supports composite curve, composite face and body collector options"
       "Three", "Enables product interface types but used along with the 'Enable Product Interface Type' customer default"
    """
    Original = 0  # ObjectBuilderBuilderVersionMemberType
    One = 1  # ObjectBuilderBuilderVersionMemberType
    Two = 2  # ObjectBuilderBuilderVersionMemberType
    Three = 3  # ObjectBuilderBuilderVersionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ObjectBuilderWaveMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ObjectBuilderWave():
    """
    An enum representing settings available for rule checking during creation of WAVE geomtery and interpart expressions  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoCheck", "no checking for product interface objects"
       "Warn", "warn user while using non product interface objects"
       "Prevent", "restrict user from using non product interface objects"
    """
    NoCheck = 0  # ObjectBuilderWaveMemberType
    Warn = 1  # ObjectBuilderWaveMemberType
    Prevent = 2  # ObjectBuilderWaveMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ObjectBuilderMateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ObjectBuilderMate():
    """
    An enum representing the settings available for rule checking during creation of mating conditions  
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoCheck", "no checking for product interface objects"
       "Warn", "warn user while using non product interface objects"
       "Prevent", "restrict user from using non product interface objects"
    """
    NoCheck = 0  # ObjectBuilderMateMemberType
    Warn = 1  # ObjectBuilderMateMemberType
    Prevent = 2  # ObjectBuilderMateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ObjectBuilder(NXOpen.Builder):
    """
    Represents a Product Interface Object Builder.  
    
    It creates a set of product interface objects 
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ProductInterface.Collection.CreateObjectBuilderWithVersion`
    
    Default values.
    
    ============================  ==============
    Property                      Value
    ============================  ==============
    PartGeometryCopy.ObjectType   BodyCollector 
    ============================  ==============
    
    .. versionadded:: NX5.0.0
    """
    
    class BuilderVersion():
        """
        Version number of product interface builder 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Original", "linked feature cannot select the product interface item"
           "One", "linked feature can directly select the product interface item"
           "Two", "product interface builder supports composite curve, composite face and body collector options"
           "Three", "Enables product interface types but used along with the 'Enable Product Interface Type' customer default"
        """
        Original = 0  # ObjectBuilderBuilderVersionMemberType
        One = 1  # ObjectBuilderBuilderVersionMemberType
        Two = 2  # ObjectBuilderBuilderVersionMemberType
        Three = 3  # ObjectBuilderBuilderVersionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Wave():
        """
        An enum representing settings available for rule checking during creation of WAVE geomtery and interpart expressions  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoCheck", "no checking for product interface objects"
           "Warn", "warn user while using non product interface objects"
           "Prevent", "restrict user from using non product interface objects"
        """
        NoCheck = 0  # ObjectBuilderWaveMemberType
        Warn = 1  # ObjectBuilderWaveMemberType
        Prevent = 2  # ObjectBuilderWaveMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Mate():
        """
        An enum representing the settings available for rule checking during creation of mating conditions  
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoCheck", "no checking for product interface objects"
           "Warn", "warn user while using non product interface objects"
           "Prevent", "restrict user from using non product interface objects"
        """
        NoCheck = 0  # ObjectBuilderMateMemberType
        Warn = 1  # ObjectBuilderMateMemberType
        Prevent = 2  # ObjectBuilderMateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def AddProductInterfaceObject1(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> InterfaceObject:
        """
        Adds an object to the product interface; currently supported types are expressions and geometry   
        
        Signature ``AddProductInterfaceObject1(nxObject, name, description, reverseDirection)`` 
        
        :param nxObject:  Selected object to add  
        :type nxObject: :py:class:`NXOpen.NXObject` 
        :param name:  User defined name of selected object  
        :type name: str 
        :param description:  User comments of selected object  
        :type description: str 
        :param reverseDirection:  Flag to specify whether to reverse the direction of the source object  
        :type reverseDirection: bool 
        :returns:  the product interface object created  
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddProductInterfaceObject2(self, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObjectInterfaceUsageType) -> InterfaceObject:
        """
        Adds an object to the product interface; currently supported types are expressions and geometry.  
        
        Interface Usage type can be set using this API.   
        
        Signature ``AddProductInterfaceObject2(nxObject, name, description, reverseDirection, interfaceUsageType)`` 
        
        :param nxObject:  Selected object to add  
        :type nxObject: :py:class:`NXOpen.NXObject` 
        :param name:  User defined name of selected object  
        :type name: str 
        :param description:  User comments of selected object  
        :type description: str 
        :param reverseDirection:  Flag to specify whether to reverse the direction of the source object  
        :type reverseDirection: bool 
        :param interfaceUsageType:  Usage type of product interface object  
        :type interfaceUsageType: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType` 
        :returns:  the product interface object created  
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditProductInterfaceObject(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool) -> None:
        """
        Edits a product interface object  
        
        Signature ``EditProductInterfaceObject(productInterface, nxObject, name, description, reverseDirection)`` 
        
        :param productInterface:  Product interface object to be edited  
        :type productInterface: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        :param nxObject:  Selected object to add  
        :type nxObject: :py:class:`NXOpen.NXObject` 
        :param name:  User defined name of selected object  
        :type name: str 
        :param description:  User comments of selected object  
        :type description: str 
        :param reverseDirection:  Flag to specify whether to reverse the direction of the source object  
        :type reverseDirection: bool 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def EditProductInterfaceObject1(self, productInterface: InterfaceObject, nxObject: NXOpen.NXObject, name: str, description: str, reverseDirection: bool, interfaceUsageType: InterfaceObjectInterfaceUsageType) -> None:
        """
        Edits a product interface object with interface object type .  
        
        Interface Usage type can be set using this API. 
        
        Signature ``EditProductInterfaceObject1(productInterface, nxObject, name, description, reverseDirection, interfaceUsageType)`` 
        
        :param productInterface:  Product interface object to be edited  
        :type productInterface: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        :param nxObject:  Selected object to add  
        :type nxObject: :py:class:`NXOpen.NXObject` 
        :param name:  User defined name of selected object  
        :type name: str 
        :param description:  User comments of selected object  
        :type description: str 
        :param reverseDirection:  Flag to specify whether to reverse the direction of the source object  
        :type reverseDirection: bool 
        :param interfaceUsageType:  Usage type of product interface object  
        :type interfaceUsageType: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetBuilderVersion(self) -> ObjectBuilderBuilderVersion:
        """
        Gets the version of this builder.  
        
        Signature ``GetBuilderVersion()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderBuilderVersion` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetBuilderVersion(self, version: ObjectBuilderBuilderVersion) -> None:
        """
        Sets the version of this builder.  
        
        Signature ``SetBuilderVersion(version)`` 
        
        :param version: 
        :type version: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderBuilderVersion` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddProductInterfaceObject(self, nxItem: NXOpen.NXObject) -> InterfaceObject:
        """
        Adds an object to the product interface; currently supported types are expressions and geometry   
        
        Signature ``AddProductInterfaceObject(nxItem)`` 
        
        :param nxItem:  nx item to be added to the product interface  
        :type nxItem: :py:class:`NXOpen.NXObject` 
        :returns:  the product interface object created  
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddProductInterface(self, nxItem: NXOpen.NXObject) -> tuple:
        """
        Adds an object to the product interface; currently supported types are expressions and geometry.  
        
        If the object already exists, it becomes active.   
        
        Signature ``AddProductInterface(nxItem)`` 
        
        :param nxItem:  nx item to be added to the product interface  
        :type nxItem: :py:class:`NXOpen.NXObject` 
        :returns: a tuple 
        :rtype: A tuple consisting of (prodIntItem, alreadyExisted). prodIntItem is a :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject`.   the product interface object created or modified alreadyExisted is a bool. 
        
        .. versionadded:: NX8.5.1
        
        License requirements: None.
        """
        ...
    
    
    def RemoveProductInterfaceObject(self, prodIntItem: InterfaceObject) -> None:
        """
        Removes an object from the product interface; currently supported types are expressions and geometry  
        
        Signature ``RemoveProductInterfaceObject(prodIntItem)`` 
        
        :param prodIntItem:  product interface object to be removed from the product interface set 
        :type prodIntItem: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def QueryProductInterfaceObjects(self, part: NXOpen.NXObject) -> 'list[InterfaceObject]':
        """
        Returns a list of product interface objects in the part  
        
        Signature ``QueryProductInterfaceObjects(part)`` 
        
        :param part:  part whose product interface objects have to be queried  
        :type part: :py:class:`NXOpen.NXObject` 
        :returns:  objects in the product interface  
        :rtype: list of :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserComments(self, prodIntItem: InterfaceObject, userComments: str) -> None:
        """
        Sets the user comments on the product interface item passed in  
        
        Signature ``SetUserComments(prodIntItem, userComments)`` 
        
        :param prodIntItem:  product interface item on which the user comments have to set  
        :type prodIntItem: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        :param userComments:  user comments to be set on specified product interface item  
        :type userComments: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UpdateAttributesFromPart(self, part: NXOpen.NXObject) -> None:
        """
        Updates the attributes of the product interface items in the part  
        
        Signature ``UpdateAttributesFromPart(part)`` 
        
        :param part:  part, product interface objects of which need to have their  attributes updated  
        :type part: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    MateSetting: ObjectBuilderMate = ...
    """
    Returns or sets  the current rule setting for use during creation of mating conditions 
    
    <hr>
    
    Getter Method
    
    Signature ``MateSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderMate` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MateSetting`` 
    
    :param mateSetting: 
    :type mateSetting: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderMate` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    PartGeometryCopy: NXOpen.Features.PartGeometryCopyBuilder = ...
    """
    Returns  the part geometry copy 
    
    <hr>
    
    Getter Method
    
    Signature ``PartGeometryCopy`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Features.PartGeometryCopyBuilder` 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    """
    WaveSetting: ObjectBuilderWave = ...
    """
    Returns or sets  the current rule setting for use during creation of WAVE geomtery and interpart expressions 
    
    <hr>
    
    Getter Method
    
    Signature ``WaveSetting`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderWave` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WaveSetting`` 
    
    :param waveSetting: 
    :type waveSetting: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilderWave` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: ObjectBuilder = ...  # unknown typename


class InterfaceObjectInvalidStateMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InterfaceObjectInvalidState():
    """
    Invalid state of problematic product interface object 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Valid", "product interface has no issue"
       "Sleeping", "product interface is sleep"
       "IncorrectOrphan", "product interface is in an incorrect orphan state"
       "SelfReferenced", "product interface references itself"
    """
    Valid = 0  # InterfaceObjectInvalidStateMemberType
    Sleeping = 1  # InterfaceObjectInvalidStateMemberType
    IncorrectOrphan = 2  # InterfaceObjectInvalidStateMemberType
    SelfReferenced = 3  # InterfaceObjectInvalidStateMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InterfaceObjectInterfaceUsageTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class InterfaceObjectInterfaceUsageType():
    """
    An enum representing product interface usage types 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Unknown", "usage type as unknown"
       "Output", "usage type as output"
       "Input", "usage type as input"
       "KeyPerformanceInterface", "usage type as key performance interface"
    """
    Unknown = 0  # InterfaceObjectInterfaceUsageTypeMemberType
    Output = 1  # InterfaceObjectInterfaceUsageTypeMemberType
    Input = 2  # InterfaceObjectInterfaceUsageTypeMemberType
    KeyPerformanceInterface = 3  # InterfaceObjectInterfaceUsageTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class InterfaceObject(NXOpen.NXObject):
    """
    Represents a Product Interface Object Builder.  
    
    It creates a product interface object 
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ProductInterface.ObjectBuilder.AddProductInterfaceObject`
    
    .. versionadded:: NX5.0.0
    """
    
    class InvalidState():
        """
        Invalid state of problematic product interface object 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Valid", "product interface has no issue"
           "Sleeping", "product interface is sleep"
           "IncorrectOrphan", "product interface is in an incorrect orphan state"
           "SelfReferenced", "product interface references itself"
        """
        Valid = 0  # InterfaceObjectInvalidStateMemberType
        Sleeping = 1  # InterfaceObjectInvalidStateMemberType
        IncorrectOrphan = 2  # InterfaceObjectInvalidStateMemberType
        SelfReferenced = 3  # InterfaceObjectInvalidStateMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class InterfaceUsageType():
        """
        An enum representing product interface usage types 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Unknown", "usage type as unknown"
           "Output", "usage type as output"
           "Input", "usage type as input"
           "KeyPerformanceInterface", "usage type as key performance interface"
        """
        Unknown = 0  # InterfaceObjectInterfaceUsageTypeMemberType
        Output = 1  # InterfaceObjectInterfaceUsageTypeMemberType
        Input = 2  # InterfaceObjectInterfaceUsageTypeMemberType
        KeyPerformanceInterface = 3  # InterfaceObjectInterfaceUsageTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetProductInterfaceObjectType(self) -> str:
        """
        Returns the type of the input product interface object   
        
        Signature ``GetProductInterfaceObjectType()`` 
        
        :returns:  type of the product interface object  
        :rtype: str 
        
        .. versionadded:: NX5.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetProductInterfaceDefiningEntity(self) -> NXOpen.NXObject:
        """
        Returns the underlying NX object referenced by the input product interface object   
        
        Signature ``GetProductInterfaceDefiningEntity()`` 
        
        :returns:  nx item referenced by the product interface  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX5.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetProductInterfaceObjectStatus(self) -> str:
        """
        Returns the status of the input product interface object   
        
        Signature ``GetProductInterfaceObjectStatus()`` 
        
        :returns:  status of the product interface object  
        :rtype: str 
        
        .. versionadded:: NX5.0.1
        
        License requirements: None.
        """
        ...
    
    
    def SetUserComments(self, userComments: str) -> None:
        """
        Sets the user comments on the input product interface object 
        
        Signature ``SetUserComments(userComments)`` 
        
        :param userComments:  user comments to be set on the product interface object  
        :type userComments: str 
        
        .. versionadded:: NX5.0.1
        
        License requirements: None.
        """
        ...
    
    
    def GetUserComments(self) -> str:
        """
        Returns the user comments on the input product interface object  
        
        Signature ``GetUserComments()`` 
        
        :returns:  user comments on the product interface object  
        :rtype: str 
        
        .. versionadded:: NX5.0.1
        
        License requirements: None.
        """
        ...
    
    
    def RemoveProductInterfaceObject(self) -> None:
        """
        Removes an object from the product interface set; currently supported types are expressions and geometry  
        
        Signature ``RemoveProductInterfaceObject()`` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RenameProductInterfaceObject(self, name: str) -> None:
        """
        Renames an object from the product interface set 
        
        Signature ``RenameProductInterfaceObject(name)`` 
        
        :param name:  user defined name to be set on the product interface object, if it is empty reset it to default name  
        :type name: str 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CheckProductInterfaceObject(self) -> InterfaceObjectInvalidState:
        """
        Check the invalid state of product interface object  
        
        Signature ``CheckProductInterfaceObject()`` 
        
        :returns:  The state of product interface object  
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInvalidState` 
        
        .. versionadded:: NX10.0.1
        
        License requirements: None.
        """
        ...
    
    
    def FixInvalidProductInterfaceObject(self) -> bool:
        """
        Fix the invalid state of product interface object  
        
        Signature ``FixInvalidProductInterfaceObject()`` 
        
        :returns:  if true the product interface has an issue and is fixed  
        :rtype: bool 
        
        .. versionadded:: NX10.0.1
        
        License requirements: None.
        """
        ...
    
    
    def InsertRelatedExpressions(self, relatedExps: 'list[NXOpen.NXObject]') -> None:
        """
        Relate expressions to the product interface 
        
        Signature ``InsertRelatedExpressions(relatedExps)`` 
        
        :param relatedExps:  Expressions to relate to the product interface  
        :type relatedExps: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveRelatedExpression(self, relatedExp: NXOpen.NXObject) -> None:
        """
        Removes related expression from the product interface object 
        
        Signature ``RemoveRelatedExpression(relatedExp)`` 
        
        :param relatedExp:  the expression to have a relation to product inerface  
        :type relatedExp: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllRelatedExpressions(self) -> int:
        """
        Removes all related expressions from the product interface object  
        
        Signature ``RemoveAllRelatedExpressions()`` 
        
        :returns:  number of expressions removed  
        :rtype: int 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRelatedExpressions(self) -> 'list[NXOpen.NXObject]':
        """
        Returns all expressions related to the product interface object  
        
        Signature ``GetRelatedExpressions()`` 
        
        :returns:  expressions related to the product interface  
        :rtype: list of :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetInterfaceUsageType(self) -> InterfaceObjectInterfaceUsageType:
        """
        Returns the usage type of the product interface object  
        
        Signature ``GetInterfaceUsageType()`` 
        
        :returns:  usage type of the product interface object  
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetInterfaceUsageType(self, usageType: InterfaceObjectInterfaceUsageType) -> None:
        """
        Sets the usage type on the product interface object 
        
        Signature ``SetInterfaceUsageType(usageType)`` 
        
        :param usageType:  usage type to be set on the product interface object  
        :type usageType: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BreakPIReferencingLinks(self, usageType: InterfaceObjectInterfaceUsageType) -> None:
        """
        Breaks referencing link of PI when usage type changes.  
        
        When the product interface type changed to input or key performance interface. Break link feature and inter part expression referring to the product interface. 
        
        Signature ``BreakPIReferencingLinks(usageType)`` 
        
        :param usageType:  usage type to be set on the product interface object  
        :type usageType: :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObjectInterfaceUsageType` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    
    Null: InterfaceObject = ...  # unknown typename


class PropertyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Assemblies.ProductInterface.PropertyBuilder` builder   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Assemblies.ProductInterface.Collection.CreatePropertyBuilder`
    
    .. versionadded:: NX9.0.0
    """
    Description: str = ...
    """
    Returns or sets  the description of a product interface provided by users 
    
    <hr>
    
    Getter Method
    
    Signature ``Description`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Description`` 
    
    :param description: 
    :type description: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    InterfaceUsageType: int = ...
    """
    Returns or sets  the interface type of a product interface provided by users 
    
    <hr>
    
    Getter Method
    
    Signature ``InterfaceUsageType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InterfaceUsageType`` 
    
    :param interfaceUsageType:  usage type to be set on the product interface object  
    :type interfaceUsageType: int 
    
    .. versionadded:: NX12.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    Name: str = ...
    """
    Returns or sets  the name of a product interface provided by users 
    
    <hr>
    
    Getter Method
    
    Signature ``Name`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Name`` 
    
    :param name: 
    :type name: str 
    
    .. versionadded:: NX9.0.0
    
    License requirements: gateway ("UG GATEWAY")
    """
    Null: PropertyBuilder = ...  # unknown typename


class Collection():
    """
    This class represents the collection of product interface objects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Part`
    
    .. versionadded:: NX5.0.0
    """
    
    def CreateObjectBuilder(self) -> ObjectBuilder:
        """
        Create Product Interface Object Builder  
        
        Signature ``CreateObjectBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilder` 
        
        .. versionadded:: NX5.0.0
        
        .. deprecated::  NX11.0.1
           Please use :py:class:`NXOpen.Assemblies.ProductInterface.Collection.CreateObjectBuilderWithVersion` instead.
        
        License requirements: None.
        """
        ...
    
    
    def CreateObjectBuilderWithVersion(self, version: int) -> ObjectBuilder:
        """
        Create Product Interface Object Builder  
        
        Signature ``CreateObjectBuilderWithVersion(version)`` 
        
        :param version: 
        :type version: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.ObjectBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def CreatePropertyBuilder(self) -> PropertyBuilder:
        """
        Create Product Interface Property Builder  
        
        Signature ``CreatePropertyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Assemblies.ProductInterface.PropertyBuilder` 
        
        .. versionadded:: NX9.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> NXOpen.NXObject:
        """
        Find the Product Interface Object with input name  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier of the product interface object you want  
        :type journalIdentifier: str 
        :returns:  Product Interface Object with this identifier  
        :rtype: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetProductInterfaces(self) -> 'list[InterfaceObject]':
        """
        Returns all the product interface objects in the part  
        
        Signature ``GetProductInterfaces()`` 
        
        :returns:  product interface objects in the part  
        :rtype: list of :py:class:`NXOpen.Assemblies.ProductInterface.InterfaceObject` 
        
        .. versionadded:: NX10.0.2
        
        License requirements: None.
        """
        ...
    


