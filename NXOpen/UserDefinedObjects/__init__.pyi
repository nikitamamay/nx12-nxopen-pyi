# module 'NXOpen.UserDefinedObjects'
#
# Automatically generated 2025-06-09T14:38:48.488462
#
"""Default documentation for NXOpen.UserDefinedObjects."""

import typing

import NXOpen
import NXOpen.Features



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class UserDefinedClassManager():
    """
    JA interface for the UserDefinedClassManager object   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX5.0.0
    """
    
    def NewUserDefinedClass(self) -> UserDefinedClass:
        """
        Creats a new UserDefinedClass object  
        
        Signature ``NewUserDefinedClass()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateUserDefinedObjectClass(self, className: str, friendlyName: str) -> UserDefinedClass:
        """
        Constructs a new :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` object.  
        
        Signature ``CreateUserDefinedObjectClass(className, friendlyName)`` 
        
        :param className:  The  class name of the new UserDefinedClass  
        :type className: str 
        :param friendlyName:  The  friendly name of the new UserDefinedClass (this is the class name displayed in the UI)  
        :type friendlyName: str 
        :returns:  The new UserDefinedClass instance  
        :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserDefinedClassFromClassName(self, className: str) -> UserDefinedClass:
        """
        Get the :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` object associated with the given class name.  
        
        Signature ``GetUserDefinedClassFromClassName(className)`` 
        
        :param className:  name of class to find  
        :type className: str 
        :returns:  The UserDefinedClass instance it may be None if you do not have permission to query this object  
        :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectManagerLinkedUdoDefinition_Struct():
    """
    Used to define a link to a UserDefinedObject .  
    
    Constructor: 
    NXOpen.UserDefinedObjects.UserDefinedObjectManager.LinkedUdoDefinition()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    LinkType: UserDefinedObjectLinkType = ...
    """
    Field Value
    Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType`
    """
    AssociatedUdo: UserDefinedObject = ...
    """
    Field Value
    Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`
    """
    Status: UserDefinedObjectLinkStatus = ...
    """
    Field Value
    Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkStatus`
    """


class UserDefinedObjectManager():
    """
    This class creates and manages UserDefinedObjects   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX5.0.0
    """
    
    class LinkedUdoDefinition():
        """
        Used to define a link to a UserDefinedObject .  
        
        Constructor: 
        NXOpen.UserDefinedObjects.UserDefinedObjectManager.LinkedUdoDefinition()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        LinkType: UserDefinedObjectLinkType = ...
        """
        Field Value
        Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType`
        """
        AssociatedUdo: UserDefinedObject = ...
        """
        Field Value
        Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`
        """
        Status: UserDefinedObjectLinkStatus = ...
        """
        Field Value
        Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkStatus`
        """
    
    
    def CreateUserDefinedObject(self, udoClass: UserDefinedClass) -> UserDefinedObject:
        """
        Constructs a new :py:class:`NXOpen.Features.UserDefinedObjectFeature`.  
        
        Signature ``CreateUserDefinedObject(udoClass)`` 
        
        :param udoClass:  The UserDefinedClass used to define the new UserDefinedObject   
        :type udoClass: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
        :returns:  The new UserDefinedObject instance  
        :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUdosOfClass(self, udoClass: UserDefinedClass) -> 'list[UserDefinedObject]':
        """
        Finds all :py:class:`UserDefinedObjects.UserDefinedObject` instances that use the given :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass`.  
        
        Signature ``GetUdosOfClass(udoClass)`` 
        
        :param udoClass:  The UserDefinedClass we want to find  
        :type udoClass: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
        :returns:  User Defined Objects of the given class  
        :rtype: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsObjectLinkable(self, linkObject: NXOpen.TaggedObject, linkType: UserDefinedObjectLinkType) -> bool:
        """
        Queries an NX Object to see if it can be linked to a :py:class:`UserDefinedObjects.UserDefinedObject` via the given link type  
        
        Signature ``IsObjectLinkable(linkObject, linkType)`` 
        
        :param linkObject:  NXObject to query for linkability  
        :type linkObject: :py:class:`NXOpen.TaggedObject` 
        :param linkType:  The link type used to link this object to a UDO  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :returns:  TRUE - This object can be linked to a UDO with the given link type, FALSE - this object can not be NOT linked to a UDO with the given link type  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsObjectLinkedToUserDefinedObject(self, linkObject: NXOpen.TaggedObject) -> bool:
        """
        Queries an NX Object to see if it is linked to a :py:class:`UserDefinedObjects.UserDefinedObject` (note this will not
        tell you if the object is owned by a UDO with an owning link)  
        
        Signature ``IsObjectLinkedToUserDefinedObject(linkObject)`` 
        
        :param linkObject:  NXObject to query for links  
        :type linkObject: :py:class:`NXOpen.TaggedObject` 
        :returns:  TRUE - This object is linked to a UDO, FALSE - this object is NOT linked to a UDO  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetLinksToObject(self, linkObject: NXOpen.TaggedObject) -> 'list[UserDefinedObjectManagerLinkedUdoDefinition_Struct]':
        """
        Queries an NX Object to find all :py:class:`UserDefinedObjects.UserDefinedObject`'s that are linked to the given NXObject (note this will not find owning udos)  
        
        Signature ``GetLinksToObject(linkObject)`` 
        
        :param linkObject:  NXObject to query for links  
        :type linkObject: :py:class:`NXOpen.TaggedObject` 
        :returns:  The link definitions from UDO's to the NXObject  
        :rtype: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectManagerLinkedUdoDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsObjectOwnedByUserDefinedObject(self, linkObject: NXOpen.TaggedObject) -> bool:
        """
        Queries an NX Object to see if it is owned by a :py:class:`UserDefinedObjects.UserDefinedObject`  
        
        Signature ``IsObjectOwnedByUserDefinedObject(linkObject)`` 
        
        :param linkObject:  NXObject to query for an owning UDO  
        :type linkObject: :py:class:`NXOpen.TaggedObject` 
        :returns:  TRUE - This object is owned by a UDO, FALSE - this object is NOT owned by a UDO  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOwningUserDefinedObject(self, linkObject: NXOpen.TaggedObject) -> UserDefinedObject:
        """
        Queries an NX Object to find the :py:class:`UserDefinedObjects.UserDefinedObject` that owns the given NXObject (note this will return null for the owning udo if the object is not owned)  
        
        Signature ``GetOwningUserDefinedObject(linkObject)`` 
        
        :param linkObject:  NXObject to query for an owning UDO  
        :type linkObject: :py:class:`NXOpen.TaggedObject` 
        :returns:  The UDO which owns the NXObject  
        :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectLinkStatusMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectLinkStatus():
    """
    Status of the object linked to a :py:class:`NXOpen.Features.UserDefinedObjectFeature` 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "UpToDate", "The associated object is up to date."
       "OutOfDate", "The associated object is out of date."
    """
    UpToDate = 0  # UserDefinedObjectLinkStatusMemberType
    OutOfDate = 1  # UserDefinedObjectLinkStatusMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectLinkTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectLinkType():
    """
    Available link types for a :py:class:`NXOpen.Features.UserDefinedObjectFeature`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Owning", "The object is owned by the UDO"
       "Type1", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the UDO is also deleted. If the associated object is updated the UDO is updated."
       "Type2", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is deleted. If the UDO is updated the associated NX object is unaffected. If the associated object is deleted, it is left in the data model in a condemned state and remains attached to the UDO. If the associated object is updated the UDO is unaffected."
       "Type3", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the UDO is removed and the UDO is updated. If the associated object is updated the UDO is updated"
       "Type4", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the UDO is removed and the UDO is unaffected. If the associated object is updated the UDO is unaffected."
    """
    Owning = 0  # UserDefinedObjectLinkTypeMemberType
    Type1 = 1  # UserDefinedObjectLinkTypeMemberType
    Type2 = 2  # UserDefinedObjectLinkTypeMemberType
    Type3 = 3  # UserDefinedObjectLinkTypeMemberType
    Type4 = 4  # UserDefinedObjectLinkTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectLinkDefinition_Struct():
    """
    Contains the linked object and it's status along with the type of link.  
    
    .
    Constructor: 
    NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AssociatedObject: NXOpen.TaggedObject = ...
    """
    linked object 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.TaggedObject`
    """
    Status: UserDefinedObjectLinkStatus = ...
    """
    status of the linked object 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkStatus`
    """


class UserDefinedObject(NXOpen.DisplayableObject):
    """
    JA interface for the UserDefinedObject object   
    
    .. versionadded:: NX5.0.0
    """
    
    class LinkStatus():
        """
        Status of the object linked to a :py:class:`NXOpen.Features.UserDefinedObjectFeature` 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "UpToDate", "The associated object is up to date."
           "OutOfDate", "The associated object is out of date."
        """
        UpToDate = 0  # UserDefinedObjectLinkStatusMemberType
        OutOfDate = 1  # UserDefinedObjectLinkStatusMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LinkType():
        """
        Available link types for a :py:class:`NXOpen.Features.UserDefinedObjectFeature`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Owning", "The object is owned by the UDO"
           "Type1", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the UDO is also deleted. If the associated object is updated the UDO is updated."
           "Type2", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is deleted. If the UDO is updated the associated NX object is unaffected. If the associated object is deleted, it is left in the data model in a condemned state and remains attached to the UDO. If the associated object is updated the UDO is unaffected."
           "Type3", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the UDO is removed and the UDO is updated. If the associated object is updated the UDO is updated"
           "Type4", "If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the UDO is removed and the UDO is unaffected. If the associated object is updated the UDO is unaffected."
        """
        Owning = 0  # UserDefinedObjectLinkTypeMemberType
        Type1 = 1  # UserDefinedObjectLinkTypeMemberType
        Type2 = 2  # UserDefinedObjectLinkTypeMemberType
        Type3 = 3  # UserDefinedObjectLinkTypeMemberType
        Type4 = 4  # UserDefinedObjectLinkTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class LinkDefinition():
        """
        Contains the linked object and it's status along with the type of link.  
        
        .
        Constructor: 
        NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AssociatedObject: NXOpen.TaggedObject = ...
        """
        linked object 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.TaggedObject`
        """
        Status: UserDefinedObjectLinkStatus = ...
        """
        status of the linked object 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkStatus`
        """
    
    
    def GetUserDefinedObjectStatus(self) -> int:
        """
        Gets the out of date indicator (status) of this UDO  
        
        Signature ``GetUserDefinedObjectStatus()`` 
        
        :returns:  The status of this UDO 
        0 - The UDO is up to date
        1 - Out of date due to addition or deletion of links to the UDO
        2 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method
        3 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method 
        4 - Out of date due to deletion of associated (linked) objects in the absence of a UDO method 
        5 - Out of date due to addition or deletion of links to the UDO AND deletion of associated (linked) objects in the absence of a UDO method 
        6 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method 
        7 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method  
        :rtype: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def ClearUserDefinedObjectStatus(self) -> None:
        """
        Clears the out of data indicator (status) of this UDO 
        
        Signature ``ClearUserDefinedObjectStatus()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserDefinedObjectFeature(self) -> NXOpen.Features.UserDefinedObjectFeature:
        """
        Gets the :py:class:`NXOpen.Features.UserDefinedObjectFeature` associated with this UDO, if there isn't an associated feature, None is returned  
        
        Signature ``GetUserDefinedObjectFeature()`` 
        
        :returns:  The UserDefinedObjectFeature associated this UDO  
        :rtype: :py:class:`NXOpen.Features.UserDefinedObjectFeature` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetIntegers(self) -> 'list[int]':
        """
        Gets all of the integers stored with this UDO  
        
        Signature ``GetIntegers()`` 
        
        :returns:  Array of integers stored with this UDO  
        :rtype: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetIntegers(self, offset: int, length: int) -> 'list[int]':
        """
        Gets the integers stored in the specified range with this UDO  
        
        Signature ``GetIntegers(offset, length)`` 
        
        :param offset:  Index into the array of integers at the start of the                                                 returned range.                                                Valid values are 0 through (number of integers in the udo - 1)                                                and -(number of integers in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the integer array.                                                  Therefore using -1 or (number of integers in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of integers you wish to get  
        :type length: int 
        :returns:  Array of integers stored within the specified  
        range of the integer array for this UDO  
        :rtype: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetIntegers(self, integers: 'list[int]') -> None:
        """
        Sets all of the integers stored with this UDO 
        
        Signature ``SetIntegers(integers)`` 
        
        :param integers:  New Array of integers stored with this UDO  
        :type integers: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetIntegers(self, offset: int, length: int, integers: 'list[int]') -> None:
        """
        Replaces the integers stored with this UDO in the specified range with a new array of integers 
        
        Signature ``SetIntegers(offset, length, integers)`` 
        
        :param offset:  Index into the array of integers at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of integers in the udo - 1)                                                and -(number of integers in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the integer array.                                                  Therefore using -1 or (number of integers in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of integers in the range you wish to cut  
        :type length: int 
        :param integers:  Array of integers to paste in place of the specified range.  
        :type integers: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopIntegers(self, numIntegers: int) -> 'list[int]':
        """
        Removes the integers stored at the end of the integer array for this UDO, 
        and returns them in an array  
        
        Signature ``PopIntegers(numIntegers)`` 
        
        :param numIntegers: 
        :type numIntegers: int 
        :returns:  Array of integers that have been 
        removed from this UDO  
        :rtype: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushIntegers(self, integers: 'list[int]') -> None:
        """
        Add the specified integers to the end of the integer array for this UDO 
        
        Signature ``PushIntegers(integers)`` 
        
        :param integers:  Array of new integers to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any integers already stored with the UDO.                                                         It simply adds these new integers to the end of                                                         the existing integer array and increases                                                          the total number of integers stored with the UDO  
        :type integers: list of int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetDoubles(self) -> 'list[float]':
        """
        Gets all of the doubles stored with this UDO  
        
        Signature ``GetDoubles()`` 
        
        :returns:  Array of doubles stored with this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetDoubles(self, offset: int, length: int) -> 'list[float]':
        """
        Gets the doubles stored in the specified range with this UDO  
        
        Signature ``GetDoubles(offset, length)`` 
        
        :param offset:  Index into the array of doubles at the start of the                                                 returned range.                                                Valid values are 0 through (number of doubles in the udo - 1)                                                and -(number of doubles in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the double array.                                                  Therefore using -1 or (number of doubles in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of doubles you wish to get  
        :type length: int 
        :returns:  Array of doubles stored within the specified  
        range of the double array for this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetDoubles(self, doubles: 'list[float]') -> None:
        """
        Sets all of the doubles stored with this UDO 
        
        Signature ``SetDoubles(doubles)`` 
        
        :param doubles:  New Array of doubles stored with this UDO  
        :type doubles: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetDoubles(self, offset: int, length: int, doubles: 'list[float]') -> None:
        """
        Replaces the doubles stored with this UDO in the specified range with a new array of doubles 
        
        Signature ``SetDoubles(offset, length, doubles)`` 
        
        :param offset:  Index into the array of doubles at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of doubles in the udo - 1)                                                and -(number of doubles in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the double array.                                                  Therefore using -1 or (number of doubles in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of doubles in the range you wish to cut  
        :type length: int 
        :param doubles:  Array of doubles to paste in place of the specified range.  
        :type doubles: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopDoubles(self, numDoubles: int) -> 'list[float]':
        """
        Removes the doubles stored at the end of the double array for this UDO, 
        and returns them in an array  
        
        Signature ``PopDoubles(numDoubles)`` 
        
        :param numDoubles: 
        :type numDoubles: int 
        :returns:  Array of doubles that have been 
        removed from this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushDoubles(self, doubles: 'list[float]') -> None:
        """
        Add the specified doubles to the end of the double array for this UDO 
        
        Signature ``PushDoubles(doubles)`` 
        
        :param doubles:  Array of new doubles to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any doubles already stored with the UDO.                                                         It simply adds these new doubles to the end of                                                         the existing double array and increases                                                          the total number of doubles stored with the UDO  
        :type doubles: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetStrings(self) -> 'list[str]':
        """
        Gets all of the strings stored with this UDO  
        
        Signature ``GetStrings()`` 
        
        :returns:  Array of strings stored with this UDO  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetStrings(self, offset: int, length: int) -> 'list[str]':
        """
        Gets the strings stored in the specified range with this UDO  
        
        Signature ``GetStrings(offset, length)`` 
        
        :param offset:  Index into the array of strings at the start of the                                                 returned range.                                                Valid values are 0 through (number of strings in the udo - 1)                                                and -(number of strings in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the string array.                                                  Therefore using -1 or (number of strings in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of strings you wish to get  
        :type length: int 
        :returns:  Array of strings stored within the specified  
        range of the string array for this UDO  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetStrings(self, strings: 'list[str]') -> None:
        """
        Sets all of the strings stored with this UDO 
        
        Signature ``SetStrings(strings)`` 
        
        :param strings:  New Array of strings stored with this UDO  
        :type strings: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetStrings(self, offset: int, length: int, strings: 'list[str]') -> None:
        """
        Replaces the strings stored with this UDO in the specified range with a new array of strings 
        
        Signature ``SetStrings(offset, length, strings)`` 
        
        :param offset:  Index into the array of strings at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of strings in the udo - 1)                                                and -(number of strings in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the string array.                                                  Therefore using -1 or (number of strings in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of strings in the range you wish to cut  
        :type length: int 
        :param strings:  Array of strings to paste in place of the specified range.  
        :type strings: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopStrings(self, numStrings: int) -> 'list[str]':
        """
        Removes the strings stored at the end of the string array for this UDO, 
        and returns them in an array  
        
        Signature ``PopStrings(numStrings)`` 
        
        :param numStrings: 
        :type numStrings: int 
        :returns:  Array of strings that have been 
        removed from this UDO  
        :rtype: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushStrings(self, strings: 'list[str]') -> None:
        """
        Add the specified strings to the end of the string array for this UDO 
        
        Signature ``PushStrings(strings)`` 
        
        :param strings:  Array of new strings to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any strings already stored with the UDO.                                                         It simply adds these new strings to the end of                                                         the existing string array and increases                                                          the total number of strings stored with the UDO  
        :type strings: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetLengths(self) -> 'list[float]':
        """
        Gets all of the lengths stored with this UDO  
        
        Signature ``GetLengths()`` 
        
        :returns:  Array of lengths stored with this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetLengths(self, offset: int, length: int) -> 'list[float]':
        """
        Gets the lengths stored in the specified range with this UDO  
        
        Signature ``GetLengths(offset, length)`` 
        
        :param offset:  Index into the array of lengths at the start of the                                                 returned range.                                                Valid values are 0 through (number of lengths in the udo - 1)                                                and -(number of lengths in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the length array.                                                  Therefore using -1 or (number of lengths in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of lengths you wish to get  
        :type length: int 
        :returns:  Array of lengths stored within the specified  
        range of the length array for this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetLengths(self, lengths: 'list[float]') -> None:
        """
        Sets all of the lengths stored with this UDO 
        
        Signature ``SetLengths(lengths)`` 
        
        :param lengths:  New Array of lengths stored with this UDO  
        :type lengths: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetLengths(self, offset: int, length: int, lengths: 'list[float]') -> None:
        """
        Replaces the lengths stored with this UDO in the specified range with a new array of lengths 
        
        Signature ``SetLengths(offset, length, lengths)`` 
        
        :param offset:  Index into the array of lengths at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of lengths in the udo - 1)                                                and -(number of lengths in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the length array.                                                  Therefore using -1 or (number of lengths in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of lengths in the range you wish to cut  
        :type length: int 
        :param lengths:  Array of lengths to paste in place of the specified range.  
        :type lengths: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopLengths(self, numLengths: int) -> 'list[float]':
        """
        Removes the lengths stored at the end of the length array for this UDO, 
        and returns them in an array  
        
        Signature ``PopLengths(numLengths)`` 
        
        :param numLengths: 
        :type numLengths: int 
        :returns:  Array of lengths that have been 
        removed from this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushLengths(self, lengths: 'list[float]') -> None:
        """
        Add the specified lengths to the end of the length array for this UDO 
        
        Signature ``PushLengths(lengths)`` 
        
        :param lengths:  Array of new lengths to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any lengths already stored with the UDO.                                                         It simply adds these new lengths to the end of                                                         the existing length array and increases                                                          the total number of lengths stored with the UDO  
        :type lengths: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetAreas(self) -> 'list[float]':
        """
        Gets all of the areas stored with this UDO  
        
        Signature ``GetAreas()`` 
        
        :returns:  Array of areas stored with this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetAreas(self, offset: int, length: int) -> 'list[float]':
        """
        Gets the areas stored in the specified range with this UDO  
        
        Signature ``GetAreas(offset, length)`` 
        
        :param offset:  Index into the array of areas at the start of the                                                 returned range.                                                Valid values are 0 through (number of areas in the udo - 1)                                                and -(number of areas in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the area array.                                                  Therefore using -1 or (number of areas in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of areas you wish to get  
        :type length: int 
        :returns:  Array of areas stored within the specified  
        range of the area array for this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetAreas(self, areas: 'list[float]') -> None:
        """
        Sets all of the areas stored with this UDO 
        
        Signature ``SetAreas(areas)`` 
        
        :param areas:  New Array of areas stored with this UDO  
        :type areas: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetAreas(self, offset: int, length: int, areas: 'list[float]') -> None:
        """
        Replaces the areas stored with this UDO in the specified range with a new array of areas 
        
        Signature ``SetAreas(offset, length, areas)`` 
        
        :param offset:  Index into the array of areas at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of areas in the udo - 1)                                                and -(number of areas in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the area array.                                                  Therefore using -1 or (number of areas in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of areas in the range you wish to cut  
        :type length: int 
        :param areas:  Array of areas to paste in place of the specified range.  
        :type areas: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopAreas(self, numAreas: int) -> 'list[float]':
        """
        Removes the areas stored at the end of the area array for this UDO, 
        and returns them in an array  
        
        Signature ``PopAreas(numAreas)`` 
        
        :param numAreas: 
        :type numAreas: int 
        :returns:  Array of areas that have been 
        removed from this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushAreas(self, areas: 'list[float]') -> None:
        """
        Add the specified areas to the end of the area array for this UDO 
        
        Signature ``PushAreas(areas)`` 
        
        :param areas:  Array of new areas to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any areas already stored with the UDO.                                                         It simply adds these new areas to the end of                                                         the existing area array and increases                                                          the total number of areas stored with the UDO  
        :type areas: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetVolumes(self) -> 'list[float]':
        """
        Gets all of the volumes stored with this UDO  
        
        Signature ``GetVolumes()`` 
        
        :returns:  Array of volumes stored with this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetVolumes(self, offset: int, length: int) -> 'list[float]':
        """
        Gets the volumes stored in the specified range with this UDO  
        
        Signature ``GetVolumes(offset, length)`` 
        
        :param offset:  Index into the array of volumes at the start of the                                                 returned range.                                                Valid values are 0 through (number of volumes in the udo - 1)                                                and -(number of volumes in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the volume array.                                                  Therefore using -1 or (number of volumes in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of volumes you wish to get  
        :type length: int 
        :returns:  Array of volumes stored within the specified  
        range of the volume array for this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetVolumes(self, volumes: 'list[float]') -> None:
        """
        Sets all of the volumes stored with this UDO 
        
        Signature ``SetVolumes(volumes)`` 
        
        :param volumes:  New Array of volumes stored with this UDO  
        :type volumes: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetVolumes(self, offset: int, length: int, volumes: 'list[float]') -> None:
        """
        Replaces the volumes stored with this UDO in the specified range with a new array of volumes 
        
        Signature ``SetVolumes(offset, length, volumes)`` 
        
        :param offset:  Index into the array of volumes at the start of the                                                 range you wish to cut and replace.                                                Valid values are 0 through (number of volumes in the udo - 1)                                                and -(number of volumes in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the volume array.                                                  Therefore using -1 or (number of volumes in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of volumes in the range you wish to cut  
        :type length: int 
        :param volumes:  Array of volumes to paste in place of the specified range.  
        :type volumes: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopVolumes(self, numVolumes: int) -> 'list[float]':
        """
        Removes the volumes stored at the end of the volume array for this UDO, 
        and returns them in an array  
        
        Signature ``PopVolumes(numVolumes)`` 
        
        :param numVolumes: 
        :type numVolumes: int 
        :returns:  Array of volumes that have been 
        removed from this UDO  
        :rtype: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushVolumes(self, volumes: 'list[float]') -> None:
        """
        Add the specified volumes to the end of the volume array for this UDO 
        
        Signature ``PushVolumes(volumes)`` 
        
        :param volumes:  Array of new volumes to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any volumes already stored with the UDO.                                                         It simply adds these new volumes to the end of                                                         the existing volume array and increases                                                          the total number of volumes stored with the UDO  
        :type volumes: list of float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetLinks(self, linkType: UserDefinedObjectLinkType) -> 'list[UserDefinedObjectLinkDefinition_Struct]':
        """
        Gets all links with the given link type that are stored with this UDO  
        
        Signature ``GetLinks(linkType)`` 
        
        :param linkType:  The type of links you wish to get  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :returns:  Array of links (with the given link type) stored with this UDO  
        :rtype: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetLinks(self, linkType: UserDefinedObjectLinkType, offset: int, length: int) -> 'list[UserDefinedObjectLinkDefinition_Struct]':
        """
        Gets the links with the given link type that are stored in the specified range with this UDO  
        
        Signature ``GetLinks(linkType, offset, length)`` 
        
        :param linkType:  The type of links you wish to get  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :param offset:  Index into the array of links (with the given link type)                                                at the start of the returned range.                                                Valid values are 0 through (number of links of the given type in the udo - 1)                                                and -(number of links of the given type in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the link array.                                                  Therefore using -1 or (number of links of the given link type in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of links (with the given link type) you wish to get  
        :type length: int 
        :returns:  Array of links stored within the specified  
        range of the link type's link array for this UDO  
        :rtype: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetLinks(self, linkType: UserDefinedObjectLinkType, links: 'list[UserDefinedObjectLinkDefinition_Struct]') -> None:
        """
        Sets all of the links with the given link type stored with this UDO.
        If you already had objects linked to the UDO via the specified link type,
        this operation will over-write them with the newly specified links. 
        
        Signature ``SetLinks(linkType, links)`` 
        
        :param linkType:  The type of links you wish to set  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :param links:  New Array of links (with the given link type) stored with this UDO  
        :type links: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetLinks(self, linkType: UserDefinedObjectLinkType, offset: int, length: int, links: 'list[UserDefinedObjectLinkDefinition_Struct]') -> None:
        """
        Replaces the links of the given link type stored with this UDO in the specified range with a new array of links 
        
        Signature ``SetLinks(linkType, offset, length, links)`` 
        
        :param linkType:  The type of links you wish to set  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :param offset:  Index into the array of links (with the given link type)                                                 at the start of the range you wish to cut and replace.                                                Valid values are 0 through                                                 (number of links with the given link type in the udo - 1)                                                and -(number of links with the given link type in the udo) through -1.                                                If the offset is negative, it is used to count back                                                 from the end of the link array.                                                  Therefore using -1 or (number of links with the given link type in the udo -1)                                                for the offset will give the same result.  
        :type offset: int 
        :param length:  The number of links (with the given link type) in the range you wish to cut  
        :type length: int 
        :param links:  Array of links (with the given link type) to paste in place of the specified range.  
        :type links: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PopLinks(self, linkType: UserDefinedObjectLinkType, numLinks: int) -> 'list[UserDefinedObjectLinkDefinition_Struct]':
        """
        Removes the links stored at the end of the given link type's link array for this UDO, 
        and returns them in an array  
        
        Signature ``PopLinks(linkType, numLinks)`` 
        
        :param linkType:  The type of links you wish to remove  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :param numLinks: 
        :type numLinks: int 
        :returns:  Array of links (with the given link type) that have been 
        removed from this UDO  
        :rtype: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def PushLinks(self, linkType: UserDefinedObjectLinkType, links: 'list[UserDefinedObjectLinkDefinition_Struct]') -> None:
        """
        Add the specified links to the end of the given link type's link array for this UDO 
        
        Signature ``PushLinks(linkType, links)`` 
        
        :param linkType:  The type of links you wish to add  
        :type linkType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkType` 
        :param links:  Array of new links (with the given link type) to add to this UDO.                                                         This routine is cumulutive, and will not remove                                                         any links already stored with the UDO.                                                         It simply adds these new links to the end of                                                         the existing link array for the given link type and increases                                                          the total number of links of the given type stored with the UDO  
        :type links: list of :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    ClassName: str = ...
    """
    Returns  the class name of this UDO 
    
    <hr>
    
    Getter Method
    
    Signature ``ClassName`` 
    
    :returns:  The name of the class for this UDO  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UserDefinedClass: UserDefinedClass = ...
    """
    Returns or sets  the :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` for this UDO 
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedClass`` 
    
    :returns:  The class of this UDO  
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``UserDefinedClass`` 
    
    :param userDefinedClass:  The new class for this UDO  
    :type userDefinedClass: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    Null: UserDefinedObject = ...  # unknown typename


class UserDefinedEventReasonMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedEventReason():
    """
    Available link types for a :py:class:`UserDefinedObject`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Display", "Display UDO event"
       "Delete", "An associated object was deleted - UDO cleanup event"
       "Update", "Update UDO event"
       "Selection", "Select UDO event"
       "Fit", "Fit display event"
       "AttentionPoint", "Find Attention Point for the UDO event"
       "Info", "Query UDO Information event"
       "Edit", "Edit UDO event"
       "Suppress", "Suppress/Unsuppress UDO event"
       "ScreenSizeFit", "Fit operation for screen-size geometry"
    """
    Display = 0  # UserDefinedEventReasonMemberType
    Delete = 1  # UserDefinedEventReasonMemberType
    Update = 2  # UserDefinedEventReasonMemberType
    Selection = 3  # UserDefinedEventReasonMemberType
    Fit = 4  # UserDefinedEventReasonMemberType
    AttentionPoint = 5  # UserDefinedEventReasonMemberType
    Info = 7  # UserDefinedEventReasonMemberType
    Edit = 8  # UserDefinedEventReasonMemberType
    Suppress = 9  # UserDefinedEventReasonMemberType
    ScreenSizeFit = 10  # UserDefinedEventReasonMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedEvent(NXOpen.TransientObject):
    """
    Implements the Event Object for UDO's   
    
    .. versionadded:: NX5.0.0
    """
    
    class Reason():
        """
        Available link types for a :py:class:`UserDefinedObject`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Display", "Display UDO event"
           "Delete", "An associated object was deleted - UDO cleanup event"
           "Update", "Update UDO event"
           "Selection", "Select UDO event"
           "Fit", "Fit display event"
           "AttentionPoint", "Find Attention Point for the UDO event"
           "Info", "Query UDO Information event"
           "Edit", "Edit UDO event"
           "Suppress", "Suppress/Unsuppress UDO event"
           "ScreenSizeFit", "Fit operation for screen-size geometry"
        """
        Display = 0  # UserDefinedEventReasonMemberType
        Delete = 1  # UserDefinedEventReasonMemberType
        Update = 2  # UserDefinedEventReasonMemberType
        Selection = 3  # UserDefinedEventReasonMemberType
        Fit = 4  # UserDefinedEventReasonMemberType
        AttentionPoint = 5  # UserDefinedEventReasonMemberType
        Info = 7  # UserDefinedEventReasonMemberType
        Edit = 8  # UserDefinedEventReasonMemberType
        Suppress = 9  # UserDefinedEventReasonMemberType
        ScreenSizeFit = 10  # UserDefinedEventReasonMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is
        called, it is illegal to use the object.  In .NET and Java,
        his method is automatically called when the object is
        deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    EventReason: UserDefinedEventReason = ...
    """
    Returns  the reason we fired this event.  
    
    <hr>
    
    Getter Method
    
    Signature ``EventReason`` 
    
    :returns:  The reason for the event  
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedEventReason` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    UserDefinedObject: UserDefinedObject = ...
    """
    Returns  the related UDO.  
    
    <hr>
    
    Getter Method
    
    Signature ``UserDefinedObject`` 
    
    :returns:  The UDO that caused the event to fire  
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class UserDefinedLinkEvent(UserDefinedEvent):
    """
    Implements the Display Event Object for UDO's   
    
    .. versionadded:: NX5.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is
        called, it is illegal to use the object.  In .NET and Java,
        his method is automatically called when the object is
        deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    AssociatedObject: NXOpen.TaggedObject = ...
    """
    Returns  the associated object.  
    
    <hr>
    
    Getter Method
    
    Signature ``AssociatedObject`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.TaggedObject` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LinkStatus: int = ...
    """
    Returns  the link status.  
    
    <hr>
    
    Getter Method
    
    Signature ``LinkStatus`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    LinkType: int = ...
    """
    Returns  the link type.  
    
    <hr>
    
    Getter Method
    
    Signature ``LinkType`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class UserDefinedClassAllowOwnedObjectSelectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedClassAllowOwnedObjectSelection():
    """
    Allow owned object selection on all objects owned by an object of this :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "You do NOT have permission to select objects owned by this class."
       "On", "You have permission to select objects owned by this class."
    """
    Off = 1  # UserDefinedClassAllowOwnedObjectSelectionMemberType
    On = 2  # UserDefinedClassAllowOwnedObjectSelectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedClassAllowQueryClassMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedClassAllowQueryClass():
    """
    Allow query class from name options for a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` of this class. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "You do NOT have permission to query the class from it's name."
       "On", "You have permission to query the class from it's name."
    """
    Off = 1  # UserDefinedClassAllowQueryClassMemberType
    On = 2  # UserDefinedClassAllowQueryClassMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedClassSelectionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedClassSelection():
    """
    Allow query class from name options for a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Off", "UDO's of this class will NOT be selectable."
       "On", "UDO's of this class will be selectable."
    """
    Off = 1  # UserDefinedClassSelectionMemberType
    On = 2  # UserDefinedClassSelectionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedClass(NXOpen.TransientObject):
    """
    JA interface for the UserDefinedClass object   
    
    To create a new instance of this class, use :py:meth:`NXOpen.UserDefinedObjects.UserDefinedClassManager.NewUserDefinedClass`
    
    .. versionadded:: NX5.0.0
    """
    
    class AllowOwnedObjectSelection():
        """
        Allow owned object selection on all objects owned by an object of this :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "You do NOT have permission to select objects owned by this class."
           "On", "You have permission to select objects owned by this class."
        """
        Off = 1  # UserDefinedClassAllowOwnedObjectSelectionMemberType
        On = 2  # UserDefinedClassAllowOwnedObjectSelectionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class AllowQueryClass():
        """
        Allow query class from name options for a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` of this class. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "You do NOT have permission to query the class from it's name."
           "On", "You have permission to query the class from it's name."
        """
        Off = 1  # UserDefinedClassAllowQueryClassMemberType
        On = 2  # UserDefinedClassAllowQueryClassMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class Selection():
        """
        Allow query class from name options for a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Off", "UDO's of this class will NOT be selectable."
           "On", "UDO's of this class will be selectable."
        """
        Off = 1  # UserDefinedClassSelectionMemberType
        On = 2  # UserDefinedClassSelectionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the memory associated with this object.  
        
        After invocation of this
        method, the object is no longer valid.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetIsOccurrenceableFlag(self) -> bool:
        """
        Gets the is occurrenceable flag for this class.  
        
        Legacy Open C UDO's required a reference UDO to determine Occurrenceability.  Occurrenceability is now set
        on a class by class basis (no reference UDO required).  In the event that you have a legacy UDO you wish to query for occurenceability, 
        you will need set the is occurrenceable flag with the new native language method (which does not require a reference UDO) 
        If you do not set the is occurrenceable flag, and instead use the old open c is occurrenceable callback, you will risk error raising during this
        method because we will automatically pass None in as the reference UDO to the legacy is occurrenceable callback. 
        
        Signature ``GetIsOccurrenceableFlag()`` 
        
        :returns:  Specifies whether or not to populate occurrences for :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`'s of this class.  
        :rtype: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetIsOccurrenceableFlag(self, isOccurrenceable: bool) -> None:
        """
        Sets the is occurrenceable flag for this class.  
        
        Signature ``SetIsOccurrenceableFlag(isOccurrenceable)`` 
        
        :param isOccurrenceable:  Specifies whether or not to populate occurrences for :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`'s of this class.  
        :type isOccurrenceable: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDisplayHandler(self, displayEvent: typing.Callable) -> None:
        """
        Registers UDO display callback.  
        
        Signature ``AddDisplayHandler(displayEvent)`` 
        
        :param displayEvent: 
        :type displayEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddSelectionHandler(self, displayEvent: typing.Callable) -> None:
        """
        Registers the UDO selection callback.  
        
        Signature ``AddSelectionHandler(displayEvent)`` 
        
        :param displayEvent: 
        :type displayEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddAttentionPointHandler(self, displayEvent: typing.Callable) -> None:
        """
        Registers the attention point callback.  
        
        Signature ``AddAttentionPointHandler(displayEvent)`` 
        
        :param displayEvent: 
        :type displayEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddFitHandler(self, displayEvent: typing.Callable) -> None:
        """
        Registers the fit callback.  
        
        Signature ``AddFitHandler(displayEvent)`` 
        
        :param displayEvent: 
        :type displayEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddScreenSizeFitHandler(self, displayEvent: typing.Callable) -> None:
        """
        Registers the screen size fit callback.  
        
        The screen size fit callback is called when
        it is necesary to determine the bounding box of a screen size object (one which
        remains the same size on the screen independent of the view scale) during a fit
        computation.  As of NX 8.0 the only geometry types supported for User Defined Objects
        which are screen size are ScreenStandardText and AbsoluteRotationScreenSizeText.
        If your User Defined Object does not have any of these objects, then you should not
        call :py:meth:`NXOpen.UserDefinedObjects.UserDefinedClass.AddScreenSizeFitHandler` because to do
        do would incur a performance penalty. 
        
        Signature ``AddScreenSizeFitHandler(displayEvent)`` 
        
        :param displayEvent: 
        :type displayEvent: CallableObject 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddUpdateHandler(self, linkEvent: typing.Callable) -> None:
        """
        Registers the update callback.  
        
        Signature ``AddUpdateHandler(linkEvent)`` 
        
        :param linkEvent: 
        :type linkEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddDeleteHandler(self, linkEvent: typing.Callable) -> None:
        """
        Registers the delete callback.  
        
        Signature ``AddDeleteHandler(linkEvent)`` 
        
        :param linkEvent: 
        :type linkEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddInformationHandler(self, udoEvent: typing.Callable) -> None:
        """
        Registers the information callback.  
        
        Signature ``AddInformationHandler(udoEvent)`` 
        
        :param udoEvent: 
        :type udoEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddEditHandler(self, udoEvent: typing.Callable) -> None:
        """
        Registers the edit callback.  
        
        Signature ``AddEditHandler(udoEvent)`` 
        
        :param udoEvent: 
        :type udoEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def AddSuppressHandler(self, udoEvent: typing.Callable) -> None:
        """
        Registers the suppress callback.  
        
        Note this callback is not called unless you have a UDO FEATURE.  Also it *may* not
        get called when the system automatically suppresses the feature during update.
        
        Also note the user should check the suppression status of the feature in their callback to
        see if the input udo feature is currently getting suppressed or unsuppressed. 
        
        Signature ``AddSuppressHandler(udoEvent)`` 
        
        :param udoEvent: 
        :type udoEvent: CallableObject 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    AllowOwnedObjectSelectionOption: UserDefinedClassAllowOwnedObjectSelection = ...
    """
    Returns or sets  the allow owned object selection flag.  
    
    Specifies whether or not you have permission to select objects owned by :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject`'s of this class. 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowOwnedObjectSelectionOption`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClassAllowOwnedObjectSelection` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowOwnedObjectSelectionOption`` 
    
    :param allowOwnedObjectSelectionOption: 
    :type allowOwnedObjectSelectionOption: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClassAllowOwnedObjectSelection` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    AllowQueryClassFromName: UserDefinedClassAllowQueryClass = ...
    """
    Returns or sets  the allow query class from name flag.  
    
    Specifies whether or not you are allowed to query the :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` from the class name. 
    
    <hr>
    
    Getter Method
    
    Signature ``AllowQueryClassFromName`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClassAllowQueryClass` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AllowQueryClassFromName`` 
    
    :param allowQueryClassFromName: 
    :type allowQueryClassFromName: :py:class:`NXOpen.UserDefinedObjects.UserDefinedClassAllowQueryClass` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    ClassName: str = ...
    """
    Returns  the class name of the :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass`.  
    
    <hr>
    
    Getter Method
    
    Signature ``ClassName`` 
    
    :returns:  The real class name (non-displayed, non-user-friendly).  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    FriendlyName: str = ...
    """
    Returns  the friendly name of the :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass`.  
    
    <hr>
    
    Getter Method
    
    Signature ``FriendlyName`` 
    
    :returns:  The Friendly Name is the displayed class name inside of NX.
    For example, if you select an object in NX and filter by type, 
    this is the name shown for type selection  
    :rtype: str 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """
    WarnUserFlag: bool = ...
    """
    Returns or sets  the warn user flag.  
    
    Specifies the behavior of warning the user if a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObject` 
    of the given :py:class:`NXOpen.UserDefinedObjects.UserDefinedClass` 
    is found in a part, but the code implementing the methods for the UDO is not loaded.
    The default action is to not warn the user. If the UDO author sets this flag
    to TRUE, all UDO's of this class that are created will be marked so that the
    user will be warned if the UDO methods have not been loaded, but a UDO of the
    class is in the part. This warning will be issued to the listing window,
    when the first object of the given class is retrieved. This warning will
    only be given once per session.
    
    This flag is set on every UDO object. Therefore for any part, there may be a mixture UDO objects of a given class, 
    some having this flag set to TRUE and some objects having the flag set to FALSE. This is particularly true since all 
    UDO objects created before NX 3.0 will have this flag set to FALSE. If the UDO methods for a class are not loaded, 
    any one UDO with this flag set to TRUE in a part is enough for the warning to be issued to the listing window. 
    
    <hr>
    
    Getter Method
    
    Signature ``WarnUserFlag`` 
    
    :returns:  TRUE - the user will be warned when opening a part containing a UDO of this class without first loading it's required methods. FALSE - the user will NOT be warned.  
    :rtype: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``WarnUserFlag`` 
    
    :param warnUser:  TRUE - the user will be warned when opening a part containing a UDO of this class without first loading it's required methods. FALSE - the user will NOT be warned.  
    :type warnUser: bool 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class UserDefinedDisplayEvent(UserDefinedEvent):
    """
    Implements the Display Event Object for UDO's   
    
    .. versionadded:: NX5.0.0
    """
    
    def Dispose(self) -> None:
        """
        Frees the object from memory.  
        
        After this method is
        called, it is illegal to use the object.  In .NET and Java,
        his method is automatically called when the object is
        deleted by the garbage collector.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    DisplayContext: UserDefinedObjectDisplayContext = ...
    """
    Returns  the display context.  
    
    <hr>
    
    Getter Method
    
    Signature ``DisplayContext`` 
    
    :returns:  The context of the given display event  
    :rtype: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


class UserDefinedObjectDisplayContextPolyMarkerMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextPolyMarker():
    """
    This enumerated type specifies the type of marker to be displayed. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NoMarker", " - "
       "Point", " - "
       "Dot", " - "
       "Asterisk", " - "
       "Circle", " - "
       "Poundsign", " - "
       "X", " - "
       "Gridpoint", " - "
       "Square", " - "
       "TriangleMarker", " - "
       "Diamond", " - "
       "Centerline", " - "
       "ConsFix", " - "
       "ConsHorizontal", " - "
       "ConsVertical", " - "
       "ConsParallel", " - "
       "ConsPerpendicular", " - "
       "ConsTangent", " - "
       "ConsConcentric", " - "
       "ConsCoincident", " - "
       "ConsCollinear", " - "
       "ConsPointOnCurve", " - "
       "ConsMidpoint", " - "
       "ConsEqualLength", " - "
       "ConsEqualRadius", " - "
       "ConsConstantLength", " - "
       "ConsConstantAngle", " - "
       "ConsMirror", " - "
       "DimRadius", " - "
       "DimDiameter", " - "
       "DimParallel", " - "
       "DimPerpendicular", " - "
       "ConsSlope", " - "
       "ConsString", " - "
       "ConsUniformScaled", " - "
       "ConsNonUniformScaled", " - "
       "ConsAssocTrim", " - "
       "ConsAssocOffset", " - "
       "Disp2tResSpotWeld", " - "
       "Disp3tResSpotWeld", " - "
       "Disp4tResSpotWeld", " - "
       "Disp2tDcSpotWeld", " - "
       "Disp3tDcSpotWeld", " - "
       "Disp4tDcSpotWeld", " - "
       "Disp2tKpcSpotWeld", " - "
       "Disp3tKpcSpotWeld", " - "
       "Disp4tKpcSpotWeld", " - "
       "Disp2tProcSpotWeld", " - "
       "Disp3tProcSpotWeld", " - "
       "Disp4tProcSpotWeld", " - "
       "ArcSpotWeld", " - "
       "ClinchWeld", " - "
       "Anchor", " - "
       "LeftLeaderConnection", " - "
       "RightLeaderConnection", " - "
       "FilledCircle", " - "
       "FilledSquare", " - "
       "LargeFilledSquare", " - "
       "DatumPoint", " - "
       "SnappingDiamond", " - "
       "CircleInCircle", " - "
       "CircleInSquare", " - "
       "SquareInSquare", " - "
       "FilledLeftTriangle", " - "
       "FilledRightTriangle", " - "
       "FilledUpTriangle", " - "
       "FilledDownTriangle", " - "
       "FilledLeftTriangleInCircle", " - "
       "FilledRightTriangleInCircle", " - "
       "FilledUpTriangleInCircle", " - "
       "FilledDownTriangleInCircle", " - "
       "FilledLeftTriangleInSquare", " - "
       "FilledRightTriangleInSquare", " - "
       "FilledUpTriangleInSquare", " - "
       "FilledDownTriangleInSquare", " - "
       "RoundedCross", " - "
       "FilledDiamond", " - "
       "UpDownTriangles", " - "
       "LeftRightTriangles", " - "
       "SmallWheel", " - "
       "LargeWheel", " - "
       "HollowCircle", " - "
       "PreviewPerpendicular", " - "
       "PreviewHorizontal", " - "
       "PreviewVertical", " - "
       "PreviewTangent", " - "
       "PreviewParallel", " - "
       "PreviewPointOnCurve", " - "
       "PreviewCollinear", " - "
       "Ruler", " - "
       "Protractor", " - "
       "SketchNotebook", " - "
       "ArcEndPoint", " - "
       "Disp2PtArcMarker", " - "
       "BigAsterisk", " - "
       "LineInCircle", " - "
       "PlusInCircle", " - "
       "CenterOfRotation", " - "
       "PreviewX", " - "
       "PreviewY", " - "
       "PreviewZ", " - "
       "Disp2tGeneralSpotWeld", " - "
       "Disp3tGeneralSpotWeld", " - "
       "Disp4tGeneralSpotWeld", " - "
       "Disp2tVitalSpotWeld", " - "
       "Disp3tVitalSpotWeld", " - "
       "Disp4tVitalSpotWeld", " - "
       "Disp2tImportantSpotWeld", " - "
       "Disp3tImportantSpotWeld", " - "
       "Disp4tImportantSpotWeld", " - "
       "Disp2tSemipanelSpotWeld", " - "
       "Disp3tSemipanelSpotWeld", " - "
       "Disp4tSemipanelSpotWeld", " - "
       "InvalidMarker", " - "
    """
    NoMarker = 0  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Point = 1  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Dot = 2  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Asterisk = 3  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Circle = 4  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Poundsign = 5  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    X = 6  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Gridpoint = 7  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Square = 8  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    TriangleMarker = 9  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Diamond = 10  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Centerline = 11  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsFix = 12  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsHorizontal = 13  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsVertical = 14  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsParallel = 15  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsPerpendicular = 16  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsTangent = 17  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsConcentric = 18  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsCoincident = 19  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsCollinear = 20  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsPointOnCurve = 21  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsMidpoint = 22  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsEqualLength = 23  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsEqualRadius = 24  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsConstantLength = 25  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsConstantAngle = 26  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsMirror = 27  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    DimRadius = 28  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    DimDiameter = 29  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    DimParallel = 30  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    DimPerpendicular = 31  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsSlope = 32  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsString = 33  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsUniformScaled = 34  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsNonUniformScaled = 35  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsAssocTrim = 36  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ConsAssocOffset = 37  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tResSpotWeld = 38  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tResSpotWeld = 39  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tResSpotWeld = 40  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tDcSpotWeld = 41  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tDcSpotWeld = 42  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tDcSpotWeld = 43  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tKpcSpotWeld = 44  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tKpcSpotWeld = 45  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tKpcSpotWeld = 46  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tProcSpotWeld = 47  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tProcSpotWeld = 48  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tProcSpotWeld = 49  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ArcSpotWeld = 50  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ClinchWeld = 51  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Anchor = 52  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    LeftLeaderConnection = 53  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    RightLeaderConnection = 54  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledCircle = 55  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledSquare = 56  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    LargeFilledSquare = 57  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    DatumPoint = 58  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    SnappingDiamond = 59  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    CircleInCircle = 60  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    CircleInSquare = 61  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    SquareInSquare = 62  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledLeftTriangle = 63  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledRightTriangle = 64  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledUpTriangle = 65  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledDownTriangle = 66  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledLeftTriangleInCircle = 67  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledRightTriangleInCircle = 68  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledUpTriangleInCircle = 69  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledDownTriangleInCircle = 70  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledLeftTriangleInSquare = 71  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledRightTriangleInSquare = 72  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledUpTriangleInSquare = 73  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledDownTriangleInSquare = 74  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    RoundedCross = 75  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    FilledDiamond = 76  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    UpDownTriangles = 77  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    LeftRightTriangles = 78  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    SmallWheel = 79  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    LargeWheel = 80  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    HollowCircle = 81  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewPerpendicular = 82  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewHorizontal = 83  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewVertical = 84  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewTangent = 85  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewParallel = 86  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewPointOnCurve = 87  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewCollinear = 88  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Ruler = 89  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Protractor = 90  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    SketchNotebook = 91  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    ArcEndPoint = 92  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2PtArcMarker = 93  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    BigAsterisk = 94  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    LineInCircle = 95  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PlusInCircle = 96  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    CenterOfRotation = 97  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewX = 98  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewY = 99  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    PreviewZ = 100  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tGeneralSpotWeld = 101  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tGeneralSpotWeld = 102  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tGeneralSpotWeld = 103  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tVitalSpotWeld = 104  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tVitalSpotWeld = 105  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tVitalSpotWeld = 106  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tImportantSpotWeld = 107  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tImportantSpotWeld = 108  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tImportantSpotWeld = 109  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp2tSemipanelSpotWeld = 110  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp3tSemipanelSpotWeld = 111  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    Disp4tSemipanelSpotWeld = 112  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    InvalidMarker = 113  # UserDefinedObjectDisplayContextPolyMarkerMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContextFacetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextFacetType():
    """
    The enumerated type facet to be displayed 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Triangle", "The facet topology is a triangle facet"
       "Polygon", "The facet topology is a polygon facet"
       "Tristrip", "The facet topology is a tristrip facet"
    """
    Triangle = 0  # UserDefinedObjectDisplayContextFacetTypeMemberType
    Polygon = 1  # UserDefinedObjectDisplayContextFacetTypeMemberType
    Tristrip = 2  # UserDefinedObjectDisplayContextFacetTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContextTextRefMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextTextRef():
    """
    This enumerated type specifies the type of reference point used in the text box. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SystemDefault", "Display the text using the system default"
       "TopLeft", "Display the text with the given position in the top left of the text box"
       "TopCenter", "Display the text with the given position in the top center of the text box"
       "TopRight", "Display the text with the given position in the top right of the text box"
       "MiddleLeft", "Display the text with the given position in the middle left of the text box"
       "MiddleCenter", "Display the text with the given position in middle center of text box"
       "MiddleRight", "Display the text with the given position in middle right of text box"
       "BottomLeft", "Display the text with the given position in bottom left of text box"
       "BottomCenter", "Display the text with the given position in bottom center of text box"
       "BottomRight", "Display the text with the given position in bottom right of text box"
    """
    SystemDefault = 0  # UserDefinedObjectDisplayContextTextRefMemberType
    TopLeft = 1  # UserDefinedObjectDisplayContextTextRefMemberType
    TopCenter = 2  # UserDefinedObjectDisplayContextTextRefMemberType
    TopRight = 3  # UserDefinedObjectDisplayContextTextRefMemberType
    MiddleLeft = 4  # UserDefinedObjectDisplayContextTextRefMemberType
    MiddleCenter = 5  # UserDefinedObjectDisplayContextTextRefMemberType
    MiddleRight = 6  # UserDefinedObjectDisplayContextTextRefMemberType
    BottomLeft = 7  # UserDefinedObjectDisplayContextTextRefMemberType
    BottomCenter = 8  # UserDefinedObjectDisplayContextTextRefMemberType
    BottomRight = 9  # UserDefinedObjectDisplayContextTextRefMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContextStandardTextRefMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextStandardTextRef():
    """
    This enumerated type specifies the type of reference point used in the text box
    for standard_text methods. 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SystemDefault", "Display the text using the system default reference point position"
       "BaselineStart", "Display the text starting on the baseline, at the left end of the text box for left-to-right text, or at the right end of the text box for right-to-left text"
       "BaselineCenter", "Display the text with the given position in the horizontal center of the text box at the baseline"
       "BaselineEnd", "Display the text starting on the baseline, at the right end of the text box for left-to-right text, or at the left end of the text box for right-to-left text"
       "TopLeft", "Display the text with the given position in the top left of the text box"
       "TopCenter", "Display the text with the given position in the top center of the text box"
       "TopRight", "Display the text with the given position in the top right of the text box"
       "MiddleLeft", "Display the text with the given position in the middle left of the text box"
       "MiddleCenter", "Display the text with the given position in middle center of text box"
       "MiddleRight", "Display the text with the given position in middle right of text box"
       "BottomLeft", "Display the text with the given position in bottom left of text box"
       "BottomCenter", "Display the text with the given position in bottom center of text box"
       "BottomRight", "Display the text with the given position in bottom right of text box"
    """
    SystemDefault = 0  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BaselineStart = 0  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BaselineCenter = 1  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BaselineEnd = 2  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    TopLeft = 3  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    TopCenter = 4  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    TopRight = 5  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    MiddleLeft = 6  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    MiddleCenter = 7  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    MiddleRight = 8  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BottomLeft = 9  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BottomCenter = 10  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    BottomRight = 11  # UserDefinedObjectDisplayContextStandardTextRefMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContextTextSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextTextSize():
    """
    Provides a way to specify the size of the desired text, as small,
    medium or large (normal is a synonym for medium). 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Small", " - "
       "Normal", " - "
       "Medium", " - "
       "Large", " - "
       "NumSizes", " - "
    """
    Small = 0  # UserDefinedObjectDisplayContextTextSizeMemberType
    Normal = 1  # UserDefinedObjectDisplayContextTextSizeMemberType
    Medium = 1  # UserDefinedObjectDisplayContextTextSizeMemberType
    Large = 2  # UserDefinedObjectDisplayContextTextSizeMemberType
    NumSizes = 3  # UserDefinedObjectDisplayContextTextSizeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContextViewModeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class UserDefinedObjectDisplayContextViewMode():
    """
    The enumerated view mode 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotShaded", "The view is not shaded"
       "PartiallyShaded", "The view is partially shaded"
       "FullyShaded", "The view is fully shaded"
       "AnalysisShaded", "The view is analysis shaded"
       "StudioShaded", "The view is studio shaded"
    """
    NotShaded = 1  # UserDefinedObjectDisplayContextViewModeMemberType
    PartiallyShaded = 2  # UserDefinedObjectDisplayContextViewModeMemberType
    FullyShaded = 3  # UserDefinedObjectDisplayContextViewModeMemberType
    AnalysisShaded = 4  # UserDefinedObjectDisplayContextViewModeMemberType
    StudioShaded = 5  # UserDefinedObjectDisplayContextViewModeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class UserDefinedObjectDisplayContext(NXOpen.TransientObject):
    """
    This class is used to display User Defined Objects   
    
    .. versionadded:: NX5.0.0
    """
    
    class PolyMarker():
        """
        This enumerated type specifies the type of marker to be displayed. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NoMarker", " - "
           "Point", " - "
           "Dot", " - "
           "Asterisk", " - "
           "Circle", " - "
           "Poundsign", " - "
           "X", " - "
           "Gridpoint", " - "
           "Square", " - "
           "TriangleMarker", " - "
           "Diamond", " - "
           "Centerline", " - "
           "ConsFix", " - "
           "ConsHorizontal", " - "
           "ConsVertical", " - "
           "ConsParallel", " - "
           "ConsPerpendicular", " - "
           "ConsTangent", " - "
           "ConsConcentric", " - "
           "ConsCoincident", " - "
           "ConsCollinear", " - "
           "ConsPointOnCurve", " - "
           "ConsMidpoint", " - "
           "ConsEqualLength", " - "
           "ConsEqualRadius", " - "
           "ConsConstantLength", " - "
           "ConsConstantAngle", " - "
           "ConsMirror", " - "
           "DimRadius", " - "
           "DimDiameter", " - "
           "DimParallel", " - "
           "DimPerpendicular", " - "
           "ConsSlope", " - "
           "ConsString", " - "
           "ConsUniformScaled", " - "
           "ConsNonUniformScaled", " - "
           "ConsAssocTrim", " - "
           "ConsAssocOffset", " - "
           "Disp2tResSpotWeld", " - "
           "Disp3tResSpotWeld", " - "
           "Disp4tResSpotWeld", " - "
           "Disp2tDcSpotWeld", " - "
           "Disp3tDcSpotWeld", " - "
           "Disp4tDcSpotWeld", " - "
           "Disp2tKpcSpotWeld", " - "
           "Disp3tKpcSpotWeld", " - "
           "Disp4tKpcSpotWeld", " - "
           "Disp2tProcSpotWeld", " - "
           "Disp3tProcSpotWeld", " - "
           "Disp4tProcSpotWeld", " - "
           "ArcSpotWeld", " - "
           "ClinchWeld", " - "
           "Anchor", " - "
           "LeftLeaderConnection", " - "
           "RightLeaderConnection", " - "
           "FilledCircle", " - "
           "FilledSquare", " - "
           "LargeFilledSquare", " - "
           "DatumPoint", " - "
           "SnappingDiamond", " - "
           "CircleInCircle", " - "
           "CircleInSquare", " - "
           "SquareInSquare", " - "
           "FilledLeftTriangle", " - "
           "FilledRightTriangle", " - "
           "FilledUpTriangle", " - "
           "FilledDownTriangle", " - "
           "FilledLeftTriangleInCircle", " - "
           "FilledRightTriangleInCircle", " - "
           "FilledUpTriangleInCircle", " - "
           "FilledDownTriangleInCircle", " - "
           "FilledLeftTriangleInSquare", " - "
           "FilledRightTriangleInSquare", " - "
           "FilledUpTriangleInSquare", " - "
           "FilledDownTriangleInSquare", " - "
           "RoundedCross", " - "
           "FilledDiamond", " - "
           "UpDownTriangles", " - "
           "LeftRightTriangles", " - "
           "SmallWheel", " - "
           "LargeWheel", " - "
           "HollowCircle", " - "
           "PreviewPerpendicular", " - "
           "PreviewHorizontal", " - "
           "PreviewVertical", " - "
           "PreviewTangent", " - "
           "PreviewParallel", " - "
           "PreviewPointOnCurve", " - "
           "PreviewCollinear", " - "
           "Ruler", " - "
           "Protractor", " - "
           "SketchNotebook", " - "
           "ArcEndPoint", " - "
           "Disp2PtArcMarker", " - "
           "BigAsterisk", " - "
           "LineInCircle", " - "
           "PlusInCircle", " - "
           "CenterOfRotation", " - "
           "PreviewX", " - "
           "PreviewY", " - "
           "PreviewZ", " - "
           "Disp2tGeneralSpotWeld", " - "
           "Disp3tGeneralSpotWeld", " - "
           "Disp4tGeneralSpotWeld", " - "
           "Disp2tVitalSpotWeld", " - "
           "Disp3tVitalSpotWeld", " - "
           "Disp4tVitalSpotWeld", " - "
           "Disp2tImportantSpotWeld", " - "
           "Disp3tImportantSpotWeld", " - "
           "Disp4tImportantSpotWeld", " - "
           "Disp2tSemipanelSpotWeld", " - "
           "Disp3tSemipanelSpotWeld", " - "
           "Disp4tSemipanelSpotWeld", " - "
           "InvalidMarker", " - "
        """
        NoMarker = 0  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Point = 1  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Dot = 2  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Asterisk = 3  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Circle = 4  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Poundsign = 5  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        X = 6  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Gridpoint = 7  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Square = 8  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        TriangleMarker = 9  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Diamond = 10  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Centerline = 11  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsFix = 12  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsHorizontal = 13  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsVertical = 14  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsParallel = 15  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsPerpendicular = 16  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsTangent = 17  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsConcentric = 18  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsCoincident = 19  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsCollinear = 20  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsPointOnCurve = 21  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsMidpoint = 22  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsEqualLength = 23  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsEqualRadius = 24  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsConstantLength = 25  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsConstantAngle = 26  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsMirror = 27  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        DimRadius = 28  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        DimDiameter = 29  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        DimParallel = 30  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        DimPerpendicular = 31  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsSlope = 32  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsString = 33  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsUniformScaled = 34  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsNonUniformScaled = 35  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsAssocTrim = 36  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ConsAssocOffset = 37  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tResSpotWeld = 38  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tResSpotWeld = 39  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tResSpotWeld = 40  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tDcSpotWeld = 41  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tDcSpotWeld = 42  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tDcSpotWeld = 43  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tKpcSpotWeld = 44  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tKpcSpotWeld = 45  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tKpcSpotWeld = 46  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tProcSpotWeld = 47  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tProcSpotWeld = 48  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tProcSpotWeld = 49  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ArcSpotWeld = 50  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ClinchWeld = 51  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Anchor = 52  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        LeftLeaderConnection = 53  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        RightLeaderConnection = 54  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledCircle = 55  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledSquare = 56  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        LargeFilledSquare = 57  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        DatumPoint = 58  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        SnappingDiamond = 59  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        CircleInCircle = 60  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        CircleInSquare = 61  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        SquareInSquare = 62  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledLeftTriangle = 63  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledRightTriangle = 64  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledUpTriangle = 65  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledDownTriangle = 66  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledLeftTriangleInCircle = 67  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledRightTriangleInCircle = 68  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledUpTriangleInCircle = 69  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledDownTriangleInCircle = 70  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledLeftTriangleInSquare = 71  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledRightTriangleInSquare = 72  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledUpTriangleInSquare = 73  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledDownTriangleInSquare = 74  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        RoundedCross = 75  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        FilledDiamond = 76  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        UpDownTriangles = 77  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        LeftRightTriangles = 78  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        SmallWheel = 79  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        LargeWheel = 80  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        HollowCircle = 81  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewPerpendicular = 82  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewHorizontal = 83  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewVertical = 84  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewTangent = 85  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewParallel = 86  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewPointOnCurve = 87  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewCollinear = 88  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Ruler = 89  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Protractor = 90  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        SketchNotebook = 91  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        ArcEndPoint = 92  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2PtArcMarker = 93  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        BigAsterisk = 94  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        LineInCircle = 95  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PlusInCircle = 96  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        CenterOfRotation = 97  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewX = 98  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewY = 99  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        PreviewZ = 100  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tGeneralSpotWeld = 101  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tGeneralSpotWeld = 102  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tGeneralSpotWeld = 103  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tVitalSpotWeld = 104  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tVitalSpotWeld = 105  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tVitalSpotWeld = 106  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tImportantSpotWeld = 107  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tImportantSpotWeld = 108  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tImportantSpotWeld = 109  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp2tSemipanelSpotWeld = 110  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp3tSemipanelSpotWeld = 111  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        Disp4tSemipanelSpotWeld = 112  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        InvalidMarker = 113  # UserDefinedObjectDisplayContextPolyMarkerMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class FacetType():
        """
        The enumerated type facet to be displayed 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Triangle", "The facet topology is a triangle facet"
           "Polygon", "The facet topology is a polygon facet"
           "Tristrip", "The facet topology is a tristrip facet"
        """
        Triangle = 0  # UserDefinedObjectDisplayContextFacetTypeMemberType
        Polygon = 1  # UserDefinedObjectDisplayContextFacetTypeMemberType
        Tristrip = 2  # UserDefinedObjectDisplayContextFacetTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TextRef():
        """
        This enumerated type specifies the type of reference point used in the text box. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SystemDefault", "Display the text using the system default"
           "TopLeft", "Display the text with the given position in the top left of the text box"
           "TopCenter", "Display the text with the given position in the top center of the text box"
           "TopRight", "Display the text with the given position in the top right of the text box"
           "MiddleLeft", "Display the text with the given position in the middle left of the text box"
           "MiddleCenter", "Display the text with the given position in middle center of text box"
           "MiddleRight", "Display the text with the given position in middle right of text box"
           "BottomLeft", "Display the text with the given position in bottom left of text box"
           "BottomCenter", "Display the text with the given position in bottom center of text box"
           "BottomRight", "Display the text with the given position in bottom right of text box"
        """
        SystemDefault = 0  # UserDefinedObjectDisplayContextTextRefMemberType
        TopLeft = 1  # UserDefinedObjectDisplayContextTextRefMemberType
        TopCenter = 2  # UserDefinedObjectDisplayContextTextRefMemberType
        TopRight = 3  # UserDefinedObjectDisplayContextTextRefMemberType
        MiddleLeft = 4  # UserDefinedObjectDisplayContextTextRefMemberType
        MiddleCenter = 5  # UserDefinedObjectDisplayContextTextRefMemberType
        MiddleRight = 6  # UserDefinedObjectDisplayContextTextRefMemberType
        BottomLeft = 7  # UserDefinedObjectDisplayContextTextRefMemberType
        BottomCenter = 8  # UserDefinedObjectDisplayContextTextRefMemberType
        BottomRight = 9  # UserDefinedObjectDisplayContextTextRefMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class StandardTextRef():
        """
        This enumerated type specifies the type of reference point used in the text box
        for standard_text methods. 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SystemDefault", "Display the text using the system default reference point position"
           "BaselineStart", "Display the text starting on the baseline, at the left end of the text box for left-to-right text, or at the right end of the text box for right-to-left text"
           "BaselineCenter", "Display the text with the given position in the horizontal center of the text box at the baseline"
           "BaselineEnd", "Display the text starting on the baseline, at the right end of the text box for left-to-right text, or at the left end of the text box for right-to-left text"
           "TopLeft", "Display the text with the given position in the top left of the text box"
           "TopCenter", "Display the text with the given position in the top center of the text box"
           "TopRight", "Display the text with the given position in the top right of the text box"
           "MiddleLeft", "Display the text with the given position in the middle left of the text box"
           "MiddleCenter", "Display the text with the given position in middle center of text box"
           "MiddleRight", "Display the text with the given position in middle right of text box"
           "BottomLeft", "Display the text with the given position in bottom left of text box"
           "BottomCenter", "Display the text with the given position in bottom center of text box"
           "BottomRight", "Display the text with the given position in bottom right of text box"
        """
        SystemDefault = 0  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BaselineStart = 0  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BaselineCenter = 1  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BaselineEnd = 2  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        TopLeft = 3  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        TopCenter = 4  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        TopRight = 5  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        MiddleLeft = 6  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        MiddleCenter = 7  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        MiddleRight = 8  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BottomLeft = 9  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BottomCenter = 10  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        BottomRight = 11  # UserDefinedObjectDisplayContextStandardTextRefMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class TextSize():
        """
        Provides a way to specify the size of the desired text, as small,
        medium or large (normal is a synonym for medium). 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Small", " - "
           "Normal", " - "
           "Medium", " - "
           "Large", " - "
           "NumSizes", " - "
        """
        Small = 0  # UserDefinedObjectDisplayContextTextSizeMemberType
        Normal = 1  # UserDefinedObjectDisplayContextTextSizeMemberType
        Medium = 1  # UserDefinedObjectDisplayContextTextSizeMemberType
        Large = 2  # UserDefinedObjectDisplayContextTextSizeMemberType
        NumSizes = 3  # UserDefinedObjectDisplayContextTextSizeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ViewMode():
        """
        The enumerated view mode 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotShaded", "The view is not shaded"
           "PartiallyShaded", "The view is partially shaded"
           "FullyShaded", "The view is fully shaded"
           "AnalysisShaded", "The view is analysis shaded"
           "StudioShaded", "The view is studio shaded"
        """
        NotShaded = 1  # UserDefinedObjectDisplayContextViewModeMemberType
        PartiallyShaded = 2  # UserDefinedObjectDisplayContextViewModeMemberType
        FullyShaded = 3  # UserDefinedObjectDisplayContextViewModeMemberType
        AnalysisShaded = 4  # UserDefinedObjectDisplayContextViewModeMemberType
        StudioShaded = 5  # UserDefinedObjectDisplayContextViewModeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def Dispose(self) -> None:
        """
        Frees the memory associated with this object.  
        
        After invocation of this
        method, the object is no longer valid.  
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayArc(self, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, startAngle: float, endAngle: float) -> None:
        """
        Displays an arc for a :py:class:`UserDefinedObject`.  
        The arc will be created in a plane whose normal is the Z axis 
        of the orientation matrix  
        (matrix[0-2] is the X axis of the orientation matrix,  
        matrix[3-5] is the Y axis of the orientation matrix, and
        matrix[6-8] is the Z axis of the orientation matrix.)
        The start and end angles are measured relative to
        the X and Y axis of this orientation matrix. 
        
        Signature ``DisplayArc(center, original, radius, startAngle, endAngle)`` 
        
        :param center:  Center of the arc (absolute coordinates transformed by the orientation matrix)  
        :type center: :py:class:`NXOpen.Point3d` 
        :param original:  Orientation matrix for the arc.  
        
        :type original: :py:class:`NXOpen.Matrix3x3` 
        :param radius:  Radius of the arc.  Must be greater than zero.  
        :type radius: float 
        :param startAngle:  Start angle in radians   
        :type startAngle: float 
        :param endAngle:  End angle in radians  
        :type endAngle: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayCircle(self, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, filled: bool) -> None:
        """
        Displays a circle for a :py:class:`UserDefinedObject`.  
        The circle will be created in a plane which is normal to
        the Z axis of the orientation matrix.  
        (matrix[0-2] is the X axis of the orientation matrix,  
        matrix[3-5] is the Y axis of the orientation matrix, and
        matrix[6-8] is the Z axis of the orientation matrix.) 
        
        Signature ``DisplayCircle(center, original, radius, filled)`` 
        
        :param center:  Center of the arc (absolute coordinates transformed by the orientation matrix)  
        :type center: :py:class:`NXOpen.Point3d` 
        :param original:  Orientation matrix for the arc.  
        
        :type original: :py:class:`NXOpen.Matrix3x3` 
        :param radius:  Radius of the arc.  Must be greater than zero.  
        :type radius: float 
        :param filled:  True if the interior of the circle is solid filled,                                          otherwise the interior is not filled  
        :type filled: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayPolyline(self, points: 'list[NXOpen.Point3d]') -> None:
        """
        Displays a polyline (a connected set of line segements) for a :py:class:`UserDefinedObject`.  
        The line segments are defined by an array of points.
        
        Signature ``DisplayPolyline(points)`` 
        
        :param points:  Array of point coordinates which define the polyline.  
        
        points[0-2] defines the first point, points[3-5] defines the second point, etc.  
        :type points: list of :py:class:`NXOpen.Point3d` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayPoints(self, points: 'list[NXOpen.Point3d]', markerType: UserDefinedObjectDisplayContextPolyMarker) -> None:
        """
        Displays a series of points for a :py:class:`UserDefinedObject`. 
        
        Signature ``DisplayPoints(points, markerType)`` 
        
        :param points:  Array of point coordinates.  
        
        points[0-2] defines the first point, points[3-5] defines the second point, etc. 
        :type points: list of :py:class:`NXOpen.Point3d` 
        :param markerType:  The type of marker displayed for each point  
        :type markerType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextPolyMarker` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayPolygon(self, points: 'list[NXOpen.Point3d]', filled: bool) -> None:
        """
        Displays a polygon (a closed set of line segements) for a :py:class:`UserDefinedObject`.  
        The line segments are defined by an array of points. 
        
        Signature ``DisplayPolygon(points, filled)`` 
        
        :param points:  Array of point coordinates which define the polyline.  
        
        points[0-2] defines the first end point, points[3-5] defines the second end point, etc.  
        :type points: list of :py:class:`NXOpen.Point3d` 
        :param filled:  True if the interior of the polygon is solid filled,                                          otherwise the interior is not filled  
        :type filled: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayFacets(self, numVertices: int, numFacets: int, vertices: 'list[NXOpen.Point3d]', normals: 'list[NXOpen.Vector3d]', typeOfFacet: UserDefinedObjectDisplayContextFacetType) -> None:
        """
        Displays a series of facets for a :py:class:`UserDefinedObject`. 
        
        Signature ``DisplayFacets(numVertices, numFacets, vertices, normals, typeOfFacet)`` 
        
        :param numVertices:  Number of points to define a facet.  
        
        :type numVertices: int 
        :param numFacets:  Number of facets to display.  
        :type numFacets: int 
        :param vertices:  Array of point coordinates which define the vertices of the facets.            For example assume num_facets = 2 and num_vertices = 3, then vertices[0-2] defines the point of the first vertex of the first facet,            vertices[3-5] defines the second vertex point of the first facet, and vertices[6-8] defines the last vertex point of the first facet.            Next vertices[9-11] define the first vertex point of the second facet, vertices[12-14] is the second vertex of the second facet, and last            vertices[15-17] defines the last vertex of the second facet.  
        :type vertices: list of :py:class:`NXOpen.Point3d` 
        :param normals:  Array of vectors which define the normal to the facet at a vertex point.            Normal vectors must be unit vectors, and they should point out away from the faceted object.            For example assume num_facets = 2 and num_vertices = 3, then normals[0-8] define the normal vectors at each vertex point in the first facet,             and normals[9-17] define the normals for the vertex points of the second facet.              More specifically normals[0-2] should define a unit normal vector out away from the facet at the point defined by vertices[0-2].              Likewise normals[3-5] should define a unit normal vector out away from the facet at the point defined by vertices[3-5].  
        :type normals: list of :py:class:`NXOpen.Vector3d` 
        :param typeOfFacet:  The format of the facet in the facet array  
        :type typeOfFacet: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextFacetType` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayText(self, text: str, textCoordinates: NXOpen.Point3d, referencePoint: UserDefinedObjectDisplayContextTextRef) -> None:
        """
        Displays a text string using an NX text font for a
        :py:class:`UserDefinedObject`. 
        
        Signature ``DisplayText(text, textCoordinates, referencePoint)`` 
        
        :param text:   Text string to display  
        :type text: str 
        :param textCoordinates:  Position of text box reference point in abs  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePoint:  Reference point of text box  
        :type referencePoint: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextRef` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayAbsoluteStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, string: str, glyphWidth: float, glyphHeight: float) -> None:
        """
        Displays a single line "Standard Text" string using "Absolute Geometry" for a
        :py:class:`UserDefinedObject`. A "Standard Text" string uses one
        of the fonts available from the operating system.  "Absolute Geometry"
        means that the text scales and rotates with the view, so it appears larger
        when you zoom in and smaller when you zoom out.  This is the type of text
        normally used by NX Drafting.   Note that the text will be displayed on
        the Absolute XY plane. 
        
        Signature ``DisplayAbsoluteStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, string, glyphWidth, glyphHeight)`` 
        
        :param fontIndex:   Index of the text font to be used.  
        
        This must be an index of a standard font.                                                    It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                    Specify NULL to use the default style for the font,                                                    which usually is Regular (no bold, no italic).                                                    If a non-NULL style does not exist for the font,                                                    the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                   in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param string:   Text string to display  
        :type string: str 
        :param glyphWidth:  Width  of text in units of the Displayed Part  
        :type glyphWidth: float 
        :param glyphHeight:  Height of text in units of the Displayed Part  
        :type glyphHeight: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayMultiLineAbsoluteStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, strings: 'list[str]', glyphWidth: float, glyphHeight: float) -> None:
        """
        Displays a multi-line "Standard Text" string using "Absolute Geometry" for a
        :py:class:`UserDefinedObject`. A "Standard Text" string uses one
        of the fonts available from the operating system.  "Absolute Geometry"
        means that the text scales and rotates with the view, so it appears larger
        when you zoom in and smaller when you zoom out.  This is the type of text
        normally used by NX Drafting.   Note that the text will be displayed on
        the Absolute XY plane. 
        
        Signature ``DisplayMultiLineAbsoluteStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, strings, glyphWidth, glyphHeight)`` 
        
        :param fontIndex:   Index of the text font to be used.  
        
        This must be an index of a standard font.                                                     It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                    Specify NULL to use the default style for the font,                                                    which usually is Regular (no bold, no italic).                                                    If a non-NULL style does not exist for the font,                                                    the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                    in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param strings:  Array of text strings to display  
        :type strings: list of str 
        :param glyphWidth:  Width  of text in units of the Displayed Part  
        :type glyphWidth: float 
        :param glyphHeight:  Height of text in units of the Displayed Part  
        :type glyphHeight: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayScreenStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, string: str, textSize: UserDefinedObjectDisplayContextTextSize) -> None:
        """
        Displays a single line "Standard Text" string using "Screen Geometry" for a
        :py:class:`UserDefinedObject`. A "Standard Text" string uses one
        of the fonts available from the operating system.  "Screen Geometry" means
        that the text remains parallel to the screen and appears the same physical
        size on the screen regardless of the view scale. This method is not
        supported for 2D output such as CGM.  Note that the text will be displayed on
        the Absolute XY plane.
        
        Signature ``DisplayScreenStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, string, textSize)`` 
        
        :param fontIndex:   Index of the text font to be used.  
        
        This must be an index of a standard font.                                                    It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                    Specify NULL to use the default style for the font,                                                    which usually is Regular (no bold, no italic).                                                    If a non-NULL style does not exist for the font,                                                    the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                   in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param string:   Text string to display  
        :type string: str 
        :param textSize:  see enum values  
        :type textSize: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextSize` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayMultiLineScreenStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, strings: 'list[str]', textSize: UserDefinedObjectDisplayContextTextSize) -> None:
        """
        Displays a multi-line "Standard Text" string using "Screen Geometry" for a
        :py:class:`UserDefinedObject`. A "Standard Text" string uses one
        of the fonts available from the operating system.  "Screen Geometry" means
        that the text remains parallel to the screen and appears the same physical
        size on the screen regardless of the view scale. This method is not
        supported for 2D output such as CGM.  Note that the text will be displayed on
        the Absolute XY plane.
        
        Signature ``DisplayMultiLineScreenStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, strings, textSize)`` 
        
        :param fontIndex:   Index of the text font to be used.  
        
        This must be an index of a standard font.                                                     It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                     Specify NULL to use the default style for the font,                                                     which usually is Regular (no bold, no italic).                                                     If a non-NULL style does not exist for the font,                                                     the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                    in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param strings:  Array of text strings to display  
        :type strings: list of str 
        :param textSize:  see enum values  
        :type textSize: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextSize` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayAbsoluteRotationScreenSizeStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, string: str, textSize: UserDefinedObjectDisplayContextTextSize) -> None:
        """
        Displays a single line "Standard Text" string using "Absolute Rotation and Screen
        Size Geometry" for a :py:class:`UserDefinedObject`. A "Standard Text"
        string uses one of the fonts available from the operating system.
        "Absolute Rotation and Screen Size Geometry" means the text appears the
        same physical sized on the screen regardless of the view scale (like
        "Screen Geometry"), the text remains front-facing and approximately
        upright (similar to "Screen Geometry"), but the orientation of the text
        changes as the user rotates the view (like "Absolute Geometry").
        The text will be displayed on the XY plane of the absolute coordinate system.
        This method is not supported for 2D output such as CGM. 
        
        Signature ``DisplayAbsoluteRotationScreenSizeStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, string, textSize)`` 
        
        :param fontIndex:  Index of the text font to be used.  
        
        This must be an index of a standard font.                                                   It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                    Specify NULL to use the default style for the font,                                                    which usually is Regular (no bold, no italic).                                                    If a non-NULL style does not exist for the font,                                                    the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                   in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param string:  Text string to display  
        :type string: str 
        :param textSize:  see enum values  
        :type textSize: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextSize` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayMultiLineAbsoluteRotationScreenSizeStandardText(self, fontIndex: int, fontStyle: str, textCoordinates: NXOpen.Point3d, referencePointType: UserDefinedObjectDisplayContextStandardTextRef, strings: 'list[str]', textSize: UserDefinedObjectDisplayContextTextSize) -> None:
        """
        Displays a multi-line "Standard Text" string using "Absolute Rotation and Screen
        Size Geometry" for a :py:class:`UserDefinedObject`. A "Standard Text"
        string uses one of the fonts available from the operating system.
        "Absolute Rotation and Screen Size Geometry" means the text appears the
        same physical sized on the screen regardless of the view scale (like
        "Screen Geometry"), the text remains front-facing and approximately
        upright (similar to "Screen Geometry"), but the orientation of the text
        changes as the user rotates the view (like "Absolute Geometry").
        The text will be displayed on the XY plane of the absolute coordinate system.
        This method is not supported for 2D output such as CGM. 
        
        Signature ``DisplayMultiLineAbsoluteRotationScreenSizeStandardText(fontIndex, fontStyle, textCoordinates, referencePointType, strings, textSize)`` 
        
        :param fontIndex:  Index of the text font to be used.  
        
        This must be an index of a standard font.                                                    It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:   The name of a style supported by the given font.                                                     Specify NULL to use the default style for the font,                                                     which usually is Regular (no bold, no italic).                                                     If a non-NULL style does not exist for the font,                                                     the font's default style will be used.  
        :type fontStyle: str 
        :param textCoordinates:  Position of text box reference point                                                    in Absolute Coordinates  
        :type textCoordinates: :py:class:`NXOpen.Point3d` 
        :param referencePointType:  Reference point type of text box  
        :type referencePointType: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef` 
        :param strings:  Array of text strings to display  
        :type strings: list of str 
        :param textSize:  see enum values  
        :type textSize: :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextSize` 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DisplayUnicodeMarker(self, unicodeChar: str, fontIndex: int, fontStyle: str, markerCoordinates: NXOpen.Point3d, markerSize: float) -> None:
        """
        Displays a single character in the given font and style centered at the given position.  
        
        The character will always be displayed parallel to the screen.
        
        Signature ``DisplayUnicodeMarker(unicodeChar, fontIndex, fontStyle, markerCoordinates, markerSize)`` 
        
        :param unicodeChar:  A single Unicode character to display                                                     at the given coordinate position.  
        :type unicodeChar: str 
        :param fontIndex:  Index of the text font to be used.                                                     This must be an index of a standard font.                                                     It may be 0 to use the default font.  
        :type fontIndex: int 
        :param fontStyle:  The name of a style supported by the given font.                                                     Specify NULL to use the default style for the font,                                                     which usually is Regular (no bold, no italic).                                                     If a non-NULL style does not exist for the font,                                                     the font's default style will be used.  
        :type fontStyle: str 
        :param markerCoordinates:  Position for the center of the marker                                                                 in Absolute Coordinates  
        :type markerCoordinates: :py:class:`NXOpen.Point3d` 
        :param markerSize:  In inches on the screen  
        :type markerSize: float 
        
        .. versionadded:: NX8.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetViewMode(self) -> tuple:
        """
        Get information about the current view mode and display context in which geometry is displayed.  
        
        Signature ``GetViewMode()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (view, isViewModeValid, viewMode, isAttenPtValid, attentionPoint, isDrawingViewOpen). view is a :py:class:`NXOpen.View`.   View being displayed isViewModeValid is a bool.   True if the view mode was returned and False if no information was available viewMode is a :py:class:`NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextViewMode`.   View mode describes the views shading                                                                        and face analysis mode - see enum values for more details isAttenPtValid is a bool.   True if the attention point was returned and                                                                        False if no information was available attentionPoint is a :py:class:`NXOpen.Point3d`.   The attention point of the geometry just displayed isDrawingViewOpen is a bool.   Is the drawing view open for display?                                                                        If true then geometry may be added to                                                                        the drawing. If false another view                                                                        which is not the drawing is open 
        
        .. versionadded:: NX8.5.0
        
        License requirements: None.
        """
        ...
    


