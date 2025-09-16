# module 'NXOpen.ShapeSearch'
#
# Automatically generated 2025-06-09T14:38:47.466626
#
"""Default documentation for NXOpen.ShapeSearch."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class SearchManager():
    """
    This class manages Shape Search.  
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.PartCollection`
    
    .. versionadded:: NX6.0.0
    """
    
    def CreateShapeSearchBuilder(self, part: NXOpen.Part) -> ShapeSearchBuilder:
        """
        Creates a :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilder` object.  
        
        Signature ``CreateShapeSearchBuilder(part)`` 
        
        :param part:  the part  
        :type part: :py:class:`NXOpen.Part` 
        :returns:  ShapeSearchBuilder object  
        :rtype: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    


class ShapeSearchBuilderSearchByTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShapeSearchBuilderSearchByType():
    """
    The search type enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Attribute", "search by attributes"
       "Body", "search by bodies"
       "Part", "search by part"
    """
    Attribute = 0  # ShapeSearchBuilderSearchByTypeMemberType
    Body = 1  # ShapeSearchBuilderSearchByTypeMemberType
    Part = 2  # ShapeSearchBuilderSearchByTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShapeSearchBuilderShapeSimilarityMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShapeSearchBuilderShapeSimilarity():
    """
    The search shape similarity enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Identical", "search with identical condition"
       "VerySimilar", "search with very similar condition"
       "Similar", "search with similar condition"
    """
    Identical = 0  # ShapeSearchBuilderShapeSimilarityMemberType
    VerySimilar = 1  # ShapeSearchBuilderShapeSimilarityMemberType
    Similar = 2  # ShapeSearchBuilderShapeSimilarityMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShapeSearchBuilderShapeSizeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShapeSearchBuilderShapeSize():
    """
    The search shape size enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "P90P110", "search with shape size 90%-110% condition"
       "P80P120", "search with shape size 80%-120% condition"
       "P70P130", "search with shape size 70%-130% condition"
       "P50P200", "search with shape size 50%-200% condition"
       "P25P400", "search with shape size 25%-400% condition"
    """
    P90P110 = 0  # ShapeSearchBuilderShapeSizeMemberType
    P80P120 = 1  # ShapeSearchBuilderShapeSizeMemberType
    P70P130 = 2  # ShapeSearchBuilderShapeSizeMemberType
    P50P200 = 3  # ShapeSearchBuilderShapeSizeMemberType
    P25P400 = 4  # ShapeSearchBuilderShapeSizeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShapeSearchBuilderOpenPartTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class ShapeSearchBuilderOpenPartType():
    """
    The open part type enum 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "NotSetDisplayPart", "Not set the opened part as display part"
       "SetDisplayPartOnlyWhenOpen", "Set the opened part as display part only when it doesn't exist in the session"
       "AlwaysSetDisplayPart", "Always set the opened part as display part whether it exists in the session"
    """
    NotSetDisplayPart = 0  # ShapeSearchBuilderOpenPartTypeMemberType
    SetDisplayPartOnlyWhenOpen = 1  # ShapeSearchBuilderOpenPartTypeMemberType
    AlwaysSetDisplayPart = 2  # ShapeSearchBuilderOpenPartTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class ShapeSearchBuilder(NXOpen.Builder):
    """
    This class provides the methods to execute shape search and get the searched results.  
    
    The operation that this builder supports has three types: (set by :py:meth:`ShapeSearch.ShapeSearchBuilder.SearchType`)
    
      #.  Search by attributes.
    
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesName` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter` 
    
      #. Search by body combined attributes with shape similarity and shape size condition. Support multiple bodies.
    
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.InputBody` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesName` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SearchShapeSize` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit` 
    
      #. Search by part combined attributes with shape similarity and shape size condition. Support loaded part, OS part, Teamcenter part and component.
    
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.InputPart` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesName` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SetInputAttributesFilter` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.ReferenceSetName` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SearchShapeSimilarity` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.SearchShapeSize` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.UseCustomShapeSize` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.CustomShapeSizeLowerLimit` 
        *  :py:meth:`ShapeSearch.ShapeSearchBuilder.CustomShapeSizeUpperLimit` 
    
    When initialize builder, we will load all saved searches from work directory and add them to
    search list. You can implement 
    :py:meth:`ShapeSearch.ShapeSearchBuilder.ExecuteSearch` to run the saved search.
    
    After define the search criteria, function :py:meth:`ShapeSearch.ShapeSearchBuilder.ExecuteSearch` can search
    the shape from database and return the searched results count and error message if fails.  The search is specified by 'searchName' parameter.
    
    The method :py:meth:`ShapeSearch.ShapeSearchBuilder.GetResults`  can get the specified results from database.         The range of results is specified by the parameters 'startResultId' and 'endResultId', the search is
    specified by 'searchName' parameter.
    
    The method :py:meth:`ShapeSearch.ShapeSearchBuilder.OpenResultPart` can open the selected result part of the
    specified search. The result is specified by 'resultId' parameter, the search is specified by 'searchName' parameter.
    
    To create a new instance of this class, use :py:meth:`NXOpen.ShapeSearch.SearchManager.CreateShapeSearchBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class SearchByType():
        """
        The search type enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Attribute", "search by attributes"
           "Body", "search by bodies"
           "Part", "search by part"
        """
        Attribute = 0  # ShapeSearchBuilderSearchByTypeMemberType
        Body = 1  # ShapeSearchBuilderSearchByTypeMemberType
        Part = 2  # ShapeSearchBuilderSearchByTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ShapeSimilarity():
        """
        The search shape similarity enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Identical", "search with identical condition"
           "VerySimilar", "search with very similar condition"
           "Similar", "search with similar condition"
        """
        Identical = 0  # ShapeSearchBuilderShapeSimilarityMemberType
        VerySimilar = 1  # ShapeSearchBuilderShapeSimilarityMemberType
        Similar = 2  # ShapeSearchBuilderShapeSimilarityMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class ShapeSize():
        """
        The search shape size enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "P90P110", "search with shape size 90%-110% condition"
           "P80P120", "search with shape size 80%-120% condition"
           "P70P130", "search with shape size 70%-130% condition"
           "P50P200", "search with shape size 50%-200% condition"
           "P25P400", "search with shape size 25%-400% condition"
        """
        P90P110 = 0  # ShapeSearchBuilderShapeSizeMemberType
        P80P120 = 1  # ShapeSearchBuilderShapeSizeMemberType
        P70P130 = 2  # ShapeSearchBuilderShapeSizeMemberType
        P50P200 = 3  # ShapeSearchBuilderShapeSizeMemberType
        P25P400 = 4  # ShapeSearchBuilderShapeSizeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OpenPartType():
        """
        The open part type enum 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "NotSetDisplayPart", "Not set the opened part as display part"
           "SetDisplayPartOnlyWhenOpen", "Set the opened part as display part only when it doesn't exist in the session"
           "AlwaysSetDisplayPart", "Always set the opened part as display part whether it exists in the session"
        """
        NotSetDisplayPart = 0  # ShapeSearchBuilderOpenPartTypeMemberType
        SetDisplayPartOnlyWhenOpen = 1  # ShapeSearchBuilderOpenPartTypeMemberType
        AlwaysSetDisplayPart = 2  # ShapeSearchBuilderOpenPartTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    def GetInputAttributesName(self) -> 'list[str]':
        """
        The input attributes name to be searched  
        
        Signature ``GetInputAttributesName()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def SetInputAttributesName(self, inputAttributesName: 'list[str]') -> None:
        """
        The input attributes name to be searched 
        
        Signature ``SetInputAttributesName(inputAttributesName)`` 
        
        :param inputAttributesName:  Search attributes Name  
        :type inputAttributesName: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def GetInputAttributesFilter(self) -> 'list[str]':
        """
        The input attributes filter to be searched  
        
        Signature ``GetInputAttributesFilter()`` 
        
        :returns: 
        :rtype: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def SetInputAttributesFilter(self, inputAttributesFilter: 'list[str]') -> None:
        """
        The input attributes filter to be searched 
        
        Signature ``SetInputAttributesFilter(inputAttributesFilter)`` 
        
        :param inputAttributesFilter:  Search attributes filter  
        :type inputAttributesFilter: list of str 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def ExecuteSearch(self, isNew: bool, searchName: str) -> tuple:
        """
        Execute new search or saved search and output error message if error.  
        
        Signature ``ExecuteSearch(isNew, searchName)`` 
        
        :param isNew:  True is executing new search, False is executing saved search  
        :type isNew: bool 
        :param searchName:  Search name  
        :type searchName: str 
        :returns: a tuple 
        :rtype: A tuple consisting of (nTotalResults, errorMessage). nTotalResults is a int.   Search result total number errorMessage is a str.   Search error message 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def GetResults(self, searchName: str, startResultId: int, endResultId: int) -> None:
        """
        Get specified search results from database.  
        
        Signature ``GetResults(searchName, startResultId, endResultId)`` 
        
        :param searchName:  Search name  
        :type searchName: str 
        :param startResultId:  Start result id  
        :type startResultId: int 
        :param endResultId:  End result id  
        :type endResultId: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    
    def OpenResultPart(self, openPartType: ShapeSearchBuilderOpenPartType, searchName: str, resultId: int) -> None:
        """
        Open the searched result part.  
        
        Signature ``OpenResultPart(openPartType, searchName, resultId)`` 
        
        :param openPartType:  Open part type  
        :type openPartType: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderOpenPartType` 
        :param searchName:  Search name  
        :type searchName: str 
        :param resultId:  Result id  
        :type resultId: int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: shape_search ("Shape Search")
        """
        ...
    
    CustomShapeSizeLowerLimit: int = ...
    """
    Returns or sets  the custom shape size lower limit to be set for search.  
    
    It is used only when use custom shape size is true.
    It must be greater than zero and less than upper limit. 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomShapeSizeLowerLimit`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomShapeSizeLowerLimit`` 
    
    :param customShapeSizeLowerLimit: 
    :type customShapeSizeLowerLimit: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    CustomShapeSizeUpperLimit: int = ...
    """
    Returns or sets  the custom shape size upper limit to be set for search.  
    
    It is used only when use custom shape size is true.
    It must be greater than lower limit. 
    
    <hr>
    
    Getter Method
    
    Signature ``CustomShapeSizeUpperLimit`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``CustomShapeSizeUpperLimit`` 
    
    :param customShapeSizeUpperLimit: 
    :type customShapeSizeUpperLimit: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    InputBody: NXOpen.SelectNXObjectList = ...
    """
    Returns  the input body to be searched 
    
    <hr>
    
    Getter Method
    
    Signature ``InputBody`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.SelectNXObjectList` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    InputPart: str = ...
    """
    Returns or sets  the input part to be searched 
    
    <hr>
    
    Getter Method
    
    Signature ``InputPart`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``InputPart`` 
    
    :param inputPart: 
    :type inputPart: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    ReferenceSetName: str = ...
    """
    Returns or sets  the part reference set name to be set for search 
    
    <hr>
    
    Getter Method
    
    Signature ``ReferenceSetName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``ReferenceSetName`` 
    
    :param referenceSetName: 
    :type referenceSetName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    SearchShapeSimilarity: ShapeSearchBuilderShapeSimilarity = ...
    """
    Returns or sets  the shape similarity to be set for search 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchShapeSimilarity`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderShapeSimilarity` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchShapeSimilarity`` 
    
    :param searchShapeSimilarity: 
    :type searchShapeSimilarity: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderShapeSimilarity` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    SearchShapeSize: ShapeSearchBuilderShapeSize = ...
    """
    Returns or sets  the shape size to be set for search.  
    
    It is used only when use custom shape size is false. 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchShapeSize`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderShapeSize` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchShapeSize`` 
    
    :param searchShapeSize: 
    :type searchShapeSize: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderShapeSize` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    SearchType: ShapeSearchBuilderSearchByType = ...
    """
    Returns or sets  the search type 
    
    <hr>
    
    Getter Method
    
    Signature ``SearchType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderSearchByType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``SearchType`` 
    
    :param searchType: 
    :type searchType: :py:class:`NXOpen.ShapeSearch.ShapeSearchBuilderSearchByType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    UseCustomShapeSize: bool = ...
    """
    Returns or sets  the use custom shape size to control use shape size option or custom shape size 
    
    <hr>
    
    Getter Method
    
    Signature ``UseCustomShapeSize`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    
    <hr>
    
    Setter Method
    
    Signature ``UseCustomShapeSize`` 
    
    :param useCustomShapeSize: 
    :type useCustomShapeSize: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: shape_search ("Shape Search")
    """
    Null: ShapeSearchBuilder = ...  # unknown typename


