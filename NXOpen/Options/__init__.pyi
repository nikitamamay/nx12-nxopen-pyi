# module 'NXOpen.Options'
#
# Automatically generated 2025-06-09T14:38:47.187736
#
"""Default documentation for NXOpen.Options."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class LevelTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LevelType():
    """
    Specifies level type. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Shipped", "Shipped level"
       "Package", "Package level"
       "Site", "Site level"
       "Group", "Group level"
       "User", "User level"
    """
    Shipped = 0  # LevelTypeMemberType
    Package = 1  # LevelTypeMemberType
    Site = 2  # LevelTypeMemberType
    Group = 3  # LevelTypeMemberType
    User = 4  # LevelTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptionsScopeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptionsScope():
    """
    Represents the scope of an option. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Part", "Option scope is part"
       "Session", "Option scope is session"
    """
    Part = 0  # OptionsScopeMemberType
    Session = 1  # OptionsScopeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ChangeList(NXOpen.TransientObject):
    """
    Records changes to option values at the specified level.  
    
    A ChangeList is created with a given level, and all of the edit operations apply to that
    level.  Each method for setting a value throws an error if the option value is locked at a
    higher level, or the specified value is not valid.
    
    All methods in this class use an option
    name as a unique identifier for accessing individual options and throw an error if an
    option with the given name is not found. All existing option names and their allowed
    values are described in the Online Documentation.
    
    Use :py:meth:`Options.OptionsManager.NewOptionsChangeList` to create a new instance of this class
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def SetValue(self, name: str, value: int) -> None:
        """
        Sets the value of an :py:class:` OptionsOptionType.Int  < OptionsOptionType>` option.
        If the option is of type :py:class:` OptionsOptionType.Real  < OptionsOptionType>` then the value parameter is converted to double.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Int  < OptionsOptionType>` or :py:class:` OptionsOptionType.Real  < OptionsOptionType>`. 
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value.  
        :type value: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: float) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Real  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Real  < OptionsOptionType>`.
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value.  
        :type value: float 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: str) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.String  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.String  < OptionsOptionType>`.
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.StringList  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.StringList  < OptionsOptionType>`.
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: bool) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Logical  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Logical  < OptionsOptionType>`.
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>`.
        
        Signature ``SetUtf8Value(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetUtf8Value(self, name: str, value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Utf8stringList  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Utf8stringList  < OptionsOptionType>`.
        
        Signature ``SetUtf8Value(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueOrder(self, name: str, value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option for which the list entries can be reordered.  
        
        Throws an error if the option type is not :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``SetValueOrder(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueSelection(self, name: str, selection: 'list[bool]', value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option for which the list entries can be reordered as well as selected.  
        
        Throws an error if the option type is not :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``SetValueSelection(name, selection, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param selection:  the selection bit  
        :type selection: list of bool 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserComment(self, name: str, comment: str) -> None:
        """
        Sets the user comment.  
        
        Throws an error if the value does not exist at this level. 
        
        Signature ``SetUserComment(name, comment)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param comment:  User comment text.  
        :type comment: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteValue(self, name: str) -> None:
        """
        Delete an option value.  
        
        Throws an error if the value does not exist at this level. 
        
        Signature ``DeleteValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LockValue(self, name: str) -> None:
        """
        Lock option value.  
        
        Signature ``LockValue(name)`` 
        
        :param name:  Option name  
        :type name: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnlockValue(self, name: str) -> None:
        """
        Unlock option value.  
        
        Signature ``UnlockValue(name)`` 
        
        :param name:  Option name  
        :type name: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves options values at the current level.  
        
        Signature ``Save()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Signature ``Dispose()`` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    CurrentLevel: LevelType = ...
    """
    Returns  the current level of options  
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentLevel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Options.LevelType` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """
    LockedByDefault: LevelLockedByDefault = ...
    """
    Returns  the default lock status for the options level.  
    
    Valid only for :py:class:` OptionsLevelType.Site  < OptionsLevelType>` and :py:class:` OptionsLevelType.Group  < OptionsLevelType>`.  
    
    <hr>
    
    Getter Method
    
    Signature ``LockedByDefault`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Options.LevelLockedByDefault` 
    
    .. versionadded:: NX4.0.0
    
    License requirements: None.
    """


class OptionsManager():
    """
    Manages options.  
    
    OptionsManager methods use an option name as a unique identifier for
    accessing individual options and throw an error if an option with a given name is not
    found.  All existing option names are listed in the Online Documentation.
    
    If a level parameter is not supplied to a query method then the option value effective in
    current session is returned.  If a level parameter is supplied then then value
    that is stored at the specified level is returned. This may not be the same as the value
    effective in the current session and may take effect only after the session is restarted.
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Session`
    
    .. versionadded:: NX4.0.0
    """
    
    @typing.overload
    def GetIntValue(self, name: str) -> int:
        """
        Gets the value of an :py:class:` OptionsOptionType.Int  < OptionsOptionType>` option. 
        Throws an error if option type is not :py:class:` OptionsOptionType.Int  < OptionsOptionType>`. 
        
        Signature ``GetIntValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option value  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetIntValue(self, name: str, level: LevelType) -> int:
        """
        Gets the value of an :py:class:` OptionsOptionType.Int  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Int  < OptionsOptionType>`.
        
        Signature ``GetIntValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: int 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetRealValue(self, name: str) -> float:
        """
        Gets the value of a :py:class:` OptionsOptionType.Real  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Real  < OptionsOptionType>`.
        
        Signature ``GetRealValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option value.  
        :rtype: float 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetRealValue(self, name: str, level: LevelType) -> float:
        """
        Gets the value of a :py:class:` OptionsOptionType.Real  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Real  < OptionsOptionType>`.
        
        Signature ``GetRealValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: float 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetStringValue(self, name: str) -> str:
        """
        Gets the value of a :py:class:` OptionsOptionType.String  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.String  < OptionsOptionType>`.
        
        Signature ``GetStringValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option value.  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetStringValue(self, name: str, level: LevelType) -> str:
        """
        Gets the value of a :py:class:` OptionsOptionType.String  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.String  < OptionsOptionType>`.
        
        Signature ``GetStringValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetUtf8stringValue(self, name: str) -> str:
        """
        Gets the value of a :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>`.
        
        Signature ``GetUtf8stringValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option utf8 value.  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetUtf8stringValue(self, name: str, level: LevelType) -> str:
        """
        Gets the value of a :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.String  < OptionsOptionType>`.
        
        Signature ``GetUtf8stringValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetStringListValue(self, name: str) -> 'list[str]':
        """
        Gets the value of a :py:class:` OptionsOptionType.StringList  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.StringList  < OptionsOptionType>`.
        
        Signature ``GetStringListValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option value.  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetStringListValue(self, name: str, level: LevelType) -> 'list[str]':
        """
        Gets the value of a :py:class:` OptionsOptionType.StringList  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.StringList  < OptionsOptionType>`.
        
        Signature ``GetStringListValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetReorderSelectableStringListValue(self, name: str) -> tuple:
        """
        Gets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``GetReorderSelectableStringListValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (value, selection). value is a list of str.   Option value selection is a list of bool.   the selection bit 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetReorderSelectableStringListValue(self, name: str, level: LevelType) -> tuple:
        """
        Gets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option at the specified level. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``GetReorderSelectableStringListValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns: a tuple 
        :rtype: A tuple consisting of (value, selection). value is a list of str.   Option value selection is a list of bool.   the selection bit 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    @typing.overload
    def GetLogicalValue(self, name: str) -> bool:
        """
        Gets the value of a :py:class:` OptionsOptionType.Logical  < OptionsOptionType>` option. 
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Logical  < OptionsOptionType>`.  
        
        Signature ``GetLogicalValue(name)`` 
        
        :param name:  Option name.  
        :type name: str 
        :returns:  Option value.  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def GetLogicalValue(self, name: str, level: LevelType) -> bool:
        """
        Gets the value of a :py:class:` OptionsOptionType.Logical  < OptionsOptionType>` option at the specified level.  
        Throws an error if the option is not of type :py:class:` OptionsOptionType.Logical  < OptionsOptionType>`.
        
        Signature ``GetLogicalValue(name, level)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Option value  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewOptionsChangeList(self, level: LevelType, lockedByDefault: LevelLockedByDefault) -> ChangeList:
        """
        Creates an instance of :py:class:`NXOpen.Options.ChangeList` class, in order to edit a set of options.  
        
        It is not possible to create an instance of :py:class:`NXOpen.Options.ChangeList` for :py:class:` OptionsLevelType.Shipped  < OptionsLevelType>` level, 
        or for a level that is not defined or is not writeable.   
        
        Signature ``NewOptionsChangeList(level, lockedByDefault)`` 
        
        :param level:  Options level.   
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :param lockedByDefault:  Specifies whether Options level is locked by default.             Ignored at :py:class:` OptionsLevelType.User  < OptionsLevelType>` level as locks at :py:class:` OptionsLevelType.User  < OptionsLevelType>` level are not supported.             If specified default lock status is different from the current one, then all exisitng locks are cleared.   
        :type lockedByDefault: :py:class:`NXOpen.Options.LevelLockedByDefault` 
        :returns:  An instanse of :py:class:`NXOpen.Options.ChangeList` class  
        :rtype: :py:class:`NXOpen.Options.ChangeList` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def NewOptionsDraftingStandardChangeList(self, level: LevelType, filename: str) -> DraftingStandardChangeList:
        """
        Creates an instance of :py:class:`NXOpen.Options.DraftingStandardChangeList` class, in order to edit a set of options.  
        
        It is not possible to create an instance of :py:class:`NXOpen.Options.DraftingStandardChangeList` for :py:class:` OptionsLevelType.Shipped  < OptionsLevelType>` level, 
        or for a level that is not defined or is not writeable.   
        
        Signature ``NewOptionsDraftingStandardChangeList(level, filename)`` 
        
        :param level:  Options level.   
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :param filename:  Specifies the filename to save/save as. 
        :type filename: str 
        :returns:  An instanse of :py:class:`NXOpen.Options.DraftingStandardChangeList` class  
        :rtype: :py:class:`NXOpen.Options.DraftingStandardChangeList` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetAllOptions(self) -> 'list[str]':
        """
        Gets the names of all available options.  
        
        Signature ``GetAllOptions()`` 
        
        :returns:  List of names of all available options.  
        :rtype: list of str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsValueLocked(self, name: str, level: LevelType) -> bool:
        """
        Returns true if the option value is locked at the specified level.  
        
        Locks are not supported at :py:class:` OptionsLevelType.User  < OptionsLevelType>` and :py:class:` OptionsLevelType.Shipped  < OptionsLevelType>` levels.  
        
        Signature ``IsValueLocked(name, level)`` 
        
        :param name:  Option name  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  Lock status  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsValueSet(self, name: str, level: LevelType) -> bool:
        """
        Returns true if the option value exists at the specified level.  
        
        Always true for the :py:class:` OptionsLevelType.Shipped  < OptionsLevelType>` level.  
        
        Signature ``IsValueSet(name, level)`` 
        
        :param name:  Option name  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  True if value is set  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetUserComment(self, name: str, level: LevelType) -> str:
        """
        Returns then user comment at the specified level.  
        
        User comments are not supported at the :py:class:` OptionsLevelType.Shipped  < OptionsLevelType>` level.  
        
        Signature ``GetUserComment(name, level)`` 
        
        :param name:  Option name  
        :type name: str 
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  User comment text.  
        :rtype: str 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptionType(self, name: str) -> OptionType:
        """
        Returns an option's type.  
        
        Signature ``GetOptionType(name)`` 
        
        :param name:  Option name  
        :type name: str 
        :returns:  Option type  
        :rtype: :py:class:`NXOpen.Options.OptionType` 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def IsLevelLockedByDefault(self, level: LevelType) -> bool:
        """
        Returns true if the option's values at the specified level are locked by default.  
        
        Locked by default means that if an option value does not exist at this level, 
        then it is locked.
        
        Signature ``IsLevelLockedByDefault(level)`` 
        
        :param level:  Options level.  
        :type level: :py:class:`NXOpen.Options.LevelType` 
        :returns:  True if options values are locked by default  
        :rtype: bool 
        
        .. versionadded:: NX4.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetScope(self, name: str) -> OptionsScope:
        """
        Returns scope of an option.  
        
        Signature ``GetScope(name)`` 
        
        :param name:  Option name  
        :type name: str 
        :returns:  Option scope  
        :rtype: :py:class:`NXOpen.Options.OptionsScope` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    


class OptionTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptionType():
    """
    Describes type of an option. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Int", "Option value is an integer number"
       "Real", "Option value is a real number"
       "String", "Option value is an ascii string"
       "StringList", "Option value is a list of ascii strings"
       "Logical", "Option value is logical"
       "Utf8string", "Option value is a utf8 string"
       "Utf8stringList", "Option value is a list of utf8 strings"
       "ReorderSelList", "Option value is a list which can be selected and re-ordered"
    """
    Int = 0  # OptionTypeMemberType
    Real = 1  # OptionTypeMemberType
    String = 2  # OptionTypeMemberType
    StringList = 3  # OptionTypeMemberType
    Logical = 4  # OptionTypeMemberType
    Utf8string = 5  # OptionTypeMemberType
    Utf8stringList = 6  # OptionTypeMemberType
    ReorderSelList = 7  # OptionTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class LevelLockedByDefaultMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class LevelLockedByDefault():
    """
    Specifies default lock status for the options level. 
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "False", "Unlocked"
       "True", "Locked"
    """
    FalseValue = 0  # LevelLockedByDefaultMemberType
    TrueValue = 1  # LevelLockedByDefaultMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DraftingStandardChangeList(NXOpen.TransientObject):
    """
    Records changes to option values at the specified level.  
    
    A DraftingStandardChangeList is created with a given level, and all of the edit operations apply to that
    level for drafting standard defaults.  Each method for setting a value throws an error if the option value 
    is locked at a higher level, or the specified value is not valid. 
    
    All methods in this class use an option
    name as a unique identifier for accessing individual options and throw an error if an
    option with the given name is not found. All existing option names and their allowed
    values are described in the Online Documentation. 
    
    Use :py:meth:`Options.OptionsManager.NewOptionsDraftingStandardChangeList` to create a new instance of this class
    
    .. versionadded:: NX5.0.0
    """
    
    @typing.overload
    def SetValue(self, name: str, value: int) -> None:
        """
        Sets the value of an :py:class:` OptionsOptionType.Int  < OptionsOptionType>` option. 
        If the option is of type :py:class:` OptionsOptionType.Real  < OptionsOptionType>` then the value parameter is converted to double.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Int  < OptionsOptionType>` or :py:class:` OptionsOptionType.Real  < OptionsOptionType>`. 
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value.  
        :type value: int 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: float) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Real  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Real  < OptionsOptionType>`. 
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value.  
        :type value: float 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: str) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.String  < OptionsOptionType>` option. 
        Throws an error if the option type is not :py:class:` OptionsOptionType.String  < OptionsOptionType>`. 
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.StringList  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.StringList  < OptionsOptionType>`.     
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    @typing.overload
    def SetValue(self, name: str, value: bool) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Logical  < OptionsOptionType>` option.
        Throws an error if the option type is not :py:class:` OptionsOptionType.Logical  < OptionsOptionType>`.         
        
        Signature ``SetValue(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: bool 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUtf8Value(self, name: str, value: str) -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>` option.  
        
        Throws an error if the option type is not :py:class:` OptionsOptionType.Utf8string  < OptionsOptionType>`. 
        
        Signature ``SetUtf8Value(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value:  Option value  
        :type value: str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueOrder(self, name: str, value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option for which the list entries can be reordered.  
        
        Throws an error if the option type is not :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``SetValueOrder(name, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetValueSelection(self, name: str, selection: 'list[bool]', value: 'list[str]') -> None:
        """
        Sets the value of a :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>` option for which the list entries can be reordered as well as selected.  
        
        Throws an error if the option type is not :py:class:` OptionsOptionType.ReorderSelList  < OptionsOptionType>`.
        
        Signature ``SetValueSelection(name, selection, value)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param selection:  the selection bit  
        :type selection: list of bool 
        :param value: 
        :type value: list of str 
        
        .. versionadded:: NX7.5.0
        
        License requirements: None.
        """
        ...
    
    
    def SetUserComment(self, name: str, comment: str) -> None:
        """
        Sets the user comment.  
        
        Throws an error if the value does not exist at this level. 
        
        Signature ``SetUserComment(name, comment)`` 
        
        :param name:  Option name.  
        :type name: str 
        :param comment:  User comment text.  
        :type comment: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def LockValue(self, name: str) -> None:
        """
        Lock option value.  
        
        Signature ``LockValue(name)`` 
        
        :param name:  Option name  
        :type name: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnlockValue(self, name: str) -> None:
        """
        Unlock option value.  
        
        Signature ``UnlockValue(name)`` 
        
        :param name:  Option name  
        :type name: str 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Save(self) -> None:
        """
        Saves the drafting standard defaults at the current level.  
        
        Signature ``Save()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Dispose(self) -> None:
        """
        Dispose the changes
        
        Signature ``Dispose()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Load(self) -> None:
        """
        Load the drafting standard defaults at the current level.  
        
        Signature ``Load()`` 
        
        .. versionadded:: NX5.0.0
        
        License requirements: None.
        """
        ...
    
    CurrentLevel: LevelType = ...
    """
    Returns  the current level of options  
    
    <hr>
    
    Getter Method
    
    Signature ``CurrentLevel`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Options.LevelType` 
    
    .. versionadded:: NX5.0.0
    
    License requirements: None.
    """


