# module 'NXOpen.Diagramming.Tables'
#
# Automatically generated 2025-06-09T14:38:45.464879
#

import typing

import NXOpen
import NXOpen.Diagramming



class CellBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder):
    """
    Represents a CellBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def GetCellSettings(self) -> CellSettingsBuilder:
        """
        Gets cell settings.  
        
        Signature ``GetCellSettings()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.CellSettingsBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetImageFileLocation(self, fileName: str) -> None:
        """
        Sets cell image file location.  
        
        Signature ``SetImageFileLocation(fileName)`` 
        
        :param fileName: 
        :type fileName: str 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def DeleteContent(self) -> None:
        """
        Delete cell contents.  
        
        Signature ``DeleteContent()`` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetContent(self) -> 'list[SizedSymbol]':
        """
        Gets cell content.  
        
        Signature ``GetContent()`` 
        
        :returns: 
        :rtype: list of :py:class:`NXOpen.Diagramming.Tables.SizedSymbol` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetContent(self, symbols: 'list[SizedSymbol]') -> None:
        """
        Sets cell content.  
        
        Signature ``SetContent(symbols)`` 
        
        :param symbols: 
        :type symbols: list of :py:class:`NXOpen.Diagramming.Tables.SizedSymbol` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    BottomBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns or sets  the bottom border line rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``BottomBorder`` 
    
    :param properties: 
    :type properties: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FormattedStringBuilder: NXOpen.Diagramming.FormattedStringBuilder = ...
    """
    Returns  the formatted string of the text.  
    
    <hr>
    
    Getter Method
    
    Signature ``FormattedStringBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.FormattedStringBuilder` 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LeftBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns or sets  the left border line rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeftBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``LeftBorder`` 
    
    :param properties: 
    :type properties: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Locked: bool = ...
    """
    Returns or sets  the locked flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``Locked`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Locked`` 
    
    :param locked: 
    :type locked: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    RightBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns or sets  the right border line rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``RightBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RightBorder`` 
    
    :param properties: 
    :type properties: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Text: str = ...
    """
    Returns or sets  the text on cell.  
    
    <hr>
    
    Getter Method
    
    Signature ``Text`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Text`` 
    
    :param strValue: 
    :type strValue: str 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TopBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns or sets  the top border line rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``TopBorder`` 
    
    :param properties: 
    :type properties: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CellBuilder = ...  # unknown typename


class CellRangeBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder):
    """
    Represents a CellRangeBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    CanHide: bool = ...
    """
    Returns or sets  the can hide flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``CanHide`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``CanHide`` 
    
    :param canHide: 
    :type canHide: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Hidden: bool = ...
    """
    Returns or sets  the hidden flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``Hidden`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Hidden`` 
    
    :param hidden: 
    :type hidden: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Size: float = ...
    """
    Returns or sets  the size.  
    
    <hr>
    
    Getter Method
    
    Signature ``Size`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Size`` 
    
    :param size: 
    :type size: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    SizingMethod: SizingMethod = ...
    """
    Returns or sets  the sizing method.  
    
    <hr>
    
    Getter Method
    
    Signature ``SizingMethod`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.SizingMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``SizingMethod`` 
    
    :param sizingMethod: 
    :type sizingMethod: :py:class:`NXOpen.Diagramming.Tables.SizingMethod` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CellRangeBuilder = ...  # unknown typename


class ColumnBuilder(CellRangeBuilder):
    """
    Represents a ColumnBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def SetWidth(self, size: float) -> None:
        """
        The method to set the width of a column.  
        
        Signature ``SetWidth(size)`` 
        
        :param size: 
        :type size: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: ColumnBuilder = ...  # unknown typename


class ContinuationDataBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder):
    """
    Represents a ContinuationDataBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    Location: ContinuationLocation = ...
    """
    Returns or sets  the location to continue a table if it won't fit.  
    
    <hr>
    
    Getter Method
    
    Signature ``Location`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.ContinuationLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Location`` 
    
    :param location: 
    :type location: :py:class:`NXOpen.Diagramming.Tables.ContinuationLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    MaximumSize: float = ...
    """
    Returns or sets  the maximum size of any section of a table.  
    
    <hr>
    
    Getter Method
    
    Signature ``MaximumSize`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaximumSize`` 
    
    :param maximumSize: 
    :type maximumSize: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Spacing: float = ...
    """
    Returns or sets  the spacing between sections of a table.  
    
    <hr>
    
    Getter Method
    
    Signature ``Spacing`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Spacing`` 
    
    :param spacing: 
    :type spacing: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: ContinuationDataBuilder = ...  # unknown typename


class Table(NXOpen.Diagramming.Annotation):
    """
    Represents the Table class.  
    
    To create or edit an instance of this class, use :py:class:`NXOpen.Diagramming.Tables.TableBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    def GetTitleBlock(self) -> NXOpen.Diagramming.TitleBlock:
        """
        Get the title block attached to the table.  
        
        Signature ``GetTitleBlock()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.TitleBlock` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    
    def RemoveTitleBlock(self) -> None:
        """
        Remove the title block attached to the table.  
        
        Signature ``RemoveTitleBlock()`` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    Null: Table = ...  # unknown typename


class ZeroDisplayMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ZeroDisplay():
    """
    Represents the cell zero display.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Zero", "Zero filled display"
       "Dash", "Dash filled display"
       "Empty", "Empty zero display"
    """
    Zero = 0  # ZeroDisplayMemberType
    Dash = 1  # ZeroDisplayMemberType
    Empty = 2  # ZeroDisplayMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SizedSymbol():
    """
    Represents sized symbol information.  
    
    .. versionadded:: NX10.0.0
    
    .
    Constructor: 
    NXOpen.Diagramming.Tables.SizedSymbol()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    PaddingFromLastSymbol: float = ...
    """
    Padding from last symbol 
    <hr>
    
    Field Value
    Type:float
    """
    Symbol: NXOpen.TaggedObject = ...
    """
    The symbol 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.TaggedObject`
    """
    Height: float = ...
    """
    The symbol height 
    <hr>
    
    Field Value
    Type:float
    """
    Width: float = ...
    """
    The symbol width 
    <hr>
    
    Field Value
    Type:float
    """


class HeaderLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HeaderLocation():
    """
    Represents the table header location.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Start", "Start header location"
       "End", "End header location"
    """
    Start = 0  # HeaderLocationMemberType
    End = 1  # HeaderLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class RowBuilder(CellRangeBuilder):
    """
    Represents a RowBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def SetHeight(self, size: float) -> None:
        """
        The method to set the height of a row.  
        
        Signature ``SetHeight(size)`` 
        
        :param size: 
        :type size: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    Null: RowBuilder = ...  # unknown typename


class TableSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder):
    """
    Represents a TableSettingsBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    AnchorLocation: AnchorLocation = ...
    """
    Returns or sets  the anchor location of the table settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``AnchorLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.AnchorLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AnchorLocation`` 
    
    :param anchorLocation: 
    :type anchorLocation: :py:class:`NXOpen.Diagramming.Tables.AnchorLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    HeaderLocation: HeaderLocation = ...
    """
    Returns or sets  the header location of the table settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``HeaderLocation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.HeaderLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeaderLocation`` 
    
    :param headerLocation: 
    :type headerLocation: :py:class:`NXOpen.Diagramming.Tables.HeaderLocation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    HeaderOrientation: HeaderOrientation = ...
    """
    Returns or sets  the header orientation of the table settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``HeaderOrientation`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.HeaderOrientation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``HeaderOrientation`` 
    
    :param headerOrientation: 
    :type headerOrientation: :py:class:`NXOpen.Diagramming.Tables.HeaderOrientation` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ProtectedFlag: bool = ...
    """
    Returns or sets  the protected flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``ProtectedFlag`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ProtectedFlag`` 
    
    :param flag: 
    :type flag: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: TableSettingsBuilder = ...  # unknown typename


class AnchorLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class AnchorLocation():
    """
    Represents the table anchor location.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TopLeft", "Top left anchor location"
       "TopRight", "Top right anchor location"
       "BottomLeft", "Bottom left anchor location"
       "BottomRight", "Bottom right anchor location"
    """
    TopLeft = 0  # AnchorLocationMemberType
    TopRight = 1  # AnchorLocationMemberType
    BottomLeft = 2  # AnchorLocationMemberType
    BottomRight = 3  # AnchorLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TableBuilderInheritOptionMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class TableBuilderInheritOption():
    """
    Represents the inherit option.
    
    .. versionadded:: NX11.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Preferences", "Setting the inherit from preferences option"
       "CustomerDefaults", "Setting the inherit from customer defaults option"
       "Selection", "Setting the inherit from selection option"
    """
    Preferences = 0  # TableBuilderInheritOptionMemberType
    CustomerDefaults = 1  # TableBuilderInheritOptionMemberType
    Selection = 2  # TableBuilderInheritOptionMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TableBuilder(NXOpen.Diagramming.AnnotationBuilder):
    """
    Represents a TableBuilder.  
    
    To create a new instance of this class, use :py:meth:`NXOpen.Diagramming.Tables.TableCollection.CreateTableBuilder`
    
    .. versionadded:: NX10.0.0
    """
    
    class InheritOption():
        """
        Represents the inherit option.
        
        .. versionadded:: NX11.0.0
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Preferences", "Setting the inherit from preferences option"
           "CustomerDefaults", "Setting the inherit from customer defaults option"
           "Selection", "Setting the inherit from selection option"
        """
        Preferences = 0  # TableBuilderInheritOptionMemberType
        CustomerDefaults = 1  # TableBuilderInheritOptionMemberType
        Selection = 2  # TableBuilderInheritOptionMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetNumberOfColumns(self) -> int:
        """
        Returns the initial number of columns.  
        
        Signature ``GetNumberOfColumns()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberOfHeaders(self) -> int:
        """
        Returns the number of headers.  
        
        Signature ``GetNumberOfHeaders()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetNumberOfRows(self) -> int:
        """
        Returns the number of rows.  
        
        Signature ``GetNumberOfRows()`` 
        
        :returns: 
        :rtype: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertHeaders(self, headerIndex: int, numHeaders: int) -> None:
        """
        The method to insert the given number of headers after the given header index.  
        
        Signature ``InsertHeaders(headerIndex, numHeaders)`` 
        
        :param headerIndex: 
        :type headerIndex: int 
        :param numHeaders: 
        :type numHeaders: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertColumns(self, columnIndex: int, numColumns: int) -> None:
        """
        The method to insert the given number of columns after the given column index.  
        
        Signature ``InsertColumns(columnIndex, numColumns)`` 
        
        :param columnIndex: 
        :type columnIndex: int 
        :param numColumns: 
        :type numColumns: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def InsertRows(self, rowIndex: int, numRows: int) -> None:
        """
        The method to insert the given number of rows after the given row index.  
        
        Signature ``InsertRows(rowIndex, numRows)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param numRows: 
        :type numRows: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveHeaders(self, headerIndex: int, numHeaders: int) -> None:
        """
        The method to remove the given number of headers starting with the given header index.  
        
        Signature ``RemoveHeaders(headerIndex, numHeaders)`` 
        
        :param headerIndex: 
        :type headerIndex: int 
        :param numHeaders: 
        :type numHeaders: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveColumns(self, columnIndex: int, numColumns: int) -> None:
        """
        The method to remove the given number of columns starting with the given column index.  
        
        Signature ``RemoveColumns(columnIndex, numColumns)`` 
        
        :param columnIndex: 
        :type columnIndex: int 
        :param numColumns: 
        :type numColumns: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveRows(self, rowIndex: int, numRows: int) -> None:
        """
        The method to remove the given number of rows starting with the given row index.  
        
        Signature ``RemoveRows(rowIndex, numRows)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param numRows: 
        :type numRows: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHeaderCell(self, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
        The method to get the header cell at the given row and column indexes.  
        
        Signature ``GetHeaderCell(rowIndex, columnIndex)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.CellBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetCell(self, rowIndex: int, columnIndex: int) -> CellBuilder:
        """
        The method to get the cell at the given row and column indexes.  
        
        Signature ``GetCell(rowIndex, columnIndex)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.CellBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetHeader(self, headerIndex: int) -> CellRangeBuilder:
        """
        The method to get the header at the given header index.  
        
        Signature ``GetHeader(headerIndex)`` 
        
        :param headerIndex: 
        :type headerIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.CellRangeBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetColumn(self, columnIndex: int) -> ColumnBuilder:
        """
        The method to get the column at the given column index.  
        
        Signature ``GetColumn(columnIndex)`` 
        
        :param columnIndex: 
        :type columnIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.ColumnBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetRow(self, rowIndex: int) -> RowBuilder:
        """
        The method to get the row at the given row index.  
        
        Signature ``GetRow(rowIndex)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.RowBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetFillColor(self) -> tuple:
        """
        The method to get the fill color.  
        
        Signature ``GetFillColor()`` 
        
        :returns: a tuple 
        :rtype: A tuple consisting of (color, opacity). color is a Id. opacity is a float. 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetFillColor(self, color: NXOpen.NXColor, opacity: float) -> None:
        """
        The method to set the fill color.  
        
        Signature ``SetFillColor(color, opacity)`` 
        
        :param color: 
        :type color: Id 
        :param opacity: 
        :type opacity: float 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MergeHeaderCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
        The method to merge the header cells in the given ranges.  
        
        Signature ``MergeHeaderCells(topRow, leftColumn, bottomRow, rightColumn)`` 
        
        :param topRow: 
        :type topRow: int 
        :param leftColumn: 
        :type leftColumn: int 
        :param bottomRow: 
        :type bottomRow: int 
        :param rightColumn: 
        :type rightColumn: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def MergeCells(self, topRow: int, leftColumn: int, bottomRow: int, rightColumn: int) -> None:
        """
        The method to merge the cells in the given ranges.  
        
        Signature ``MergeCells(topRow, leftColumn, bottomRow, rightColumn)`` 
        
        :param topRow: 
        :type topRow: int 
        :param leftColumn: 
        :type leftColumn: int 
        :param bottomRow: 
        :type bottomRow: int 
        :param rightColumn: 
        :type rightColumn: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnMergeHeaderCell(self, rowIndex: int, columnIndex: int) -> None:
        """
        The method to unmerge the header cell at the given row and column indexes.  
        
        Signature ``UnMergeHeaderCell(rowIndex, columnIndex)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def UnMergeCell(self, rowIndex: int, columnIndex: int) -> None:
        """
        The method to unmerge the cell at the given row and column indexes.  
        
        Signature ``UnMergeCell(rowIndex, columnIndex)`` 
        
        :param rowIndex: 
        :type rowIndex: int 
        :param columnIndex: 
        :type columnIndex: int 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def Inherit(self, inheritOption: TableBuilderInheritOption, annotation: NXOpen.Diagramming.Annotation) -> None:
        """
        Inherit.  
        
        Signature ``Inherit(inheritOption, annotation)`` 
        
        :param inheritOption: 
        :type inheritOption: :py:class:`NXOpen.Diagramming.Tables.TableBuilderInheritOption` 
        :param annotation: 
        :type annotation: :py:class:`NXOpen.Diagramming.Annotation` 
        
        .. versionadded:: NX11.0.0
        
        License requirements: None.
        """
        ...
    
    BottomBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns  the bottom border rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``BottomBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    CellSettingsBuilder: CellSettingsBuilder = ...
    """
    Returns  the default cell border settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``CellSettingsBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.CellSettingsBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ContinuationDataBuilder: ContinuationDataBuilder = ...
    """
    Returns  the continuation data.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContinuationDataBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.ContinuationDataBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    InitialColumnWidth: float = ...
    """
    Returns or sets  the initial width of column.  
    
    <hr>
    
    Getter Method
    
    Signature ``InitialColumnWidth`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``InitialColumnWidth`` 
    
    :param columnWidth: 
    :type columnWidth: float 
    
    .. versionadded:: NX11.0.1
    
    License requirements: None.
    """
    LeftBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns  the left border rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``LeftBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Locked: bool = ...
    """
    Returns or sets  the locked flag.  
    
    <hr>
    
    Getter Method
    
    Signature ``Locked`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``Locked`` 
    
    :param locked: 
    :type locked: bool 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    RightBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns  the right border rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``RightBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TableSettingsBuilder: TableSettingsBuilder = ...
    """
    Returns  the table settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``TableSettingsBuilder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.TableSettingsBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    TopBorder: NXOpen.Diagramming.RenderingPropertiesBuilder = ...
    """
    Returns  the top border rendering properties.  
    
    <hr>
    
    Getter Method
    
    Signature ``TopBorder`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.RenderingPropertiesBuilder` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: TableBuilder = ...  # unknown typename


class ContentAlignmentMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContentAlignment():
    """
    Represents the cell content alignment.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "TopLeft", "Top left content alignment"
       "TopCenter", "Top center content alignment"
       "TopRight", "Top right content alignment"
       "MiddleLeft", "Middle left content alignment"
       "MiddleCenter", "Middle center content alignment"
       "MiddleRight", "Middle right content alignment"
       "BottomLeft", "Bottom left content alignment"
       "BottomCenter", "Bottom center content alignment"
       "BottomRight", "Bottom right content alignment"
    """
    TopLeft = 0  # ContentAlignmentMemberType
    TopCenter = 1  # ContentAlignmentMemberType
    TopRight = 2  # ContentAlignmentMemberType
    MiddleLeft = 3  # ContentAlignmentMemberType
    MiddleCenter = 4  # ContentAlignmentMemberType
    MiddleRight = 5  # ContentAlignmentMemberType
    BottomLeft = 6  # ContentAlignmentMemberType
    BottomCenter = 7  # ContentAlignmentMemberType
    BottomRight = 8  # ContentAlignmentMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class SizingMethodMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class SizingMethod():
    """
    Represents the column/row sizing method.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Auto", "Auto sizing method"
       "Fixed", "Fixed sizing method"
    """
    Auto = 0  # SizingMethodMemberType
    Fixed = 1  # SizingMethodMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ContinuationLocationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ContinuationLocation():
    """
    Represents the table continuation location.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Up", "Up continuation location"
       "Down", "Down continuation location"
       "Left", "Left continuation location"
       "Right", "Right continuation location"
       "NextSheet", "Next sheet continuation location"
    """
    Up = 0  # ContinuationLocationMemberType
    Down = 1  # ContinuationLocationMemberType
    Left = 2  # ContinuationLocationMemberType
    Right = 3  # ContinuationLocationMemberType
    NextSheet = 4  # ContinuationLocationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OverflowBehaviorMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OverflowBehavior():
    """
    Represents the cell overflow behavior.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Wrap", "Wrap overflow behavior"
       "Truncate", "Truncate overflow behavior"
       "OverflowBorder", "Overflow border overflow behavior"
       "ShrinkToFit", "Shrink to fit overflow behavior"
    """
    Wrap = 0  # OverflowBehaviorMemberType
    Truncate = 1  # OverflowBehaviorMemberType
    OverflowBorder = 2  # OverflowBehaviorMemberType
    ShrinkToFit = 3  # OverflowBehaviorMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class TableCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a collection of Table.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.Diagramming.DiagrammingManager`
    
    .. versionadded:: NX10.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateTableBuilder(self, table: Table) -> TableBuilder:
        """
        Creates a :py:class:`NXOpen.Diagramming.Tables.TableBuilder`.  
        
        Signature ``CreateTableBuilder(table)`` 
        
        :param table:  :py:class:`NXOpen.Diagramming.Tables.Table` to be edited, if None then create a new one  
        :type table: :py:class:`NXOpen.Diagramming.Tables.Table` 
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.Tables.TableBuilder` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    
    
    def FindObject(self, journalIdentifier: str) -> Table:
        """
        Finds the :py:class:`NXOpen.Diagramming.Tables.Table` with the given identifier as recorded in a journal.  
        
        An exception will be thrown if no object can be found with given name.  
        
        Signature ``FindObject(journalIdentifier)`` 
        
        :param journalIdentifier:  Identifier to be found  
        :type journalIdentifier: str 
        :returns:  :py:class:`NXOpen.Diagramming.Tables.Table` with this name.  
        :rtype: :py:class:`NXOpen.Diagramming.Tables.Table` 
        
        .. versionadded:: NX10.0.0
        
        License requirements: None.
        """
        ...
    


class HeaderOrientationMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class HeaderOrientation():
    """
    Represents the table header orientation.   
    
    .. versionadded:: NX10.0.0
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Vertical", "Vertical header orientation"
       "Horizontal", "Horizontal header orientation"
    """
    Vertical = 0  # HeaderOrientationMemberType
    Horizontal = 1  # HeaderOrientationMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class CellSettingsBuilder(NXOpen.Diagramming.BaseTaggedObjectBuilder):
    """
    Represents a CellSettingsBuilder.  
    
    This is a sub-builder class and cannot be directly instantiated
    
    .. versionadded:: NX10.0.0
    """
    
    def GetContentTextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Gets context text style .  
        
        Signature ``GetContentTextStyle()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Diagramming.TextStyleBuilder` 
        
        .. versionadded:: NX11.0.1
        
        License requirements: None.
        """
        ...
    
    ContentAlignment: ContentAlignment = ...
    """
    Returns or sets  the content alignment of the cell settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``ContentAlignment`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.ContentAlignment` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ContentAlignment`` 
    
    :param contentAlignment: 
    :type contentAlignment: :py:class:`NXOpen.Diagramming.Tables.ContentAlignment` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FillColor: NXOpen.NXColor = ...
    """
    Returns or sets  the fill color.  
    
    <hr>
    
    Getter Method
    
    Signature ``FillColor`` 
    
    :returns: 
    :rtype: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillColor`` 
    
    :param colorId: 
    :type colorId: Id 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    FillOpacity: float = ...
    """
    Returns or sets  the fill opacity.  
    
    The range of opacity is from 0.0 to 1.0. 0.0 is completely transparent and 1.0 is completely opaque. 
    
    <hr>
    
    Getter Method
    
    Signature ``FillOpacity`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``FillOpacity`` 
    
    :param opacity: 
    :type opacity: float 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    OverflowBehavior: OverflowBehavior = ...
    """
    Returns or sets  the overflow behavior of the cell settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``OverflowBehavior`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.OverflowBehavior` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OverflowBehavior`` 
    
    :param overflowBehavior: 
    :type overflowBehavior: :py:class:`NXOpen.Diagramming.Tables.OverflowBehavior` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    ZeroDisplay: ZeroDisplay = ...
    """
    Returns or sets  the zero display of the cell settings.  
    
    <hr>
    
    Getter Method
    
    Signature ``ZeroDisplay`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Diagramming.Tables.ZeroDisplay` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ZeroDisplay`` 
    
    :param zeroDisplay: 
    :type zeroDisplay: :py:class:`NXOpen.Diagramming.Tables.ZeroDisplay` 
    
    .. versionadded:: NX10.0.0
    
    License requirements: None.
    """
    Null: CellSettingsBuilder = ...  # unknown typename


