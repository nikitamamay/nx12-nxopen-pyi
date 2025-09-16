# module 'NXOpen.Optimization'
#
# Automatically generated 2025-06-09T14:38:47.187736
#
"""Default documentation for NXOpen.Optimization."""

import typing

import NXOpen



def _handle_import() -> None:
    """internal method to handle importing an NXOpen Python module"""
    ...


class DesignStudyBuilderDesignStudyVariable_Struct():
    """
    Defined variable structure .  
    
    Constructor: 
    NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AttributeName: str = ...
    """
    Attribute name 
    <hr>
    
    Field Value
    Type:str
    """
    AttributeObject: NXOpen.NXObject = ...
    """
    Object which the attribute belongs to, it makes sense with geometry design variable type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    VariableType: DesignStudyBuilderDesignStudyAttributeType = ...
    """
    Variable type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType`
    """
    VariableLowerLimitValue: float = ...
    """
    Lower limit value 
    <hr>
    
    Field Value
    Type:float
    """
    VariableUpperLimitValue: float = ...
    """
    Upper limit value 
    <hr>
    
    Field Value
    Type:float
    """
    DistributeType: DesignStudyBuilderDesignStudyDistributeType = ...
    """
    Distribute type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyDistributeType`
    """
    LocationParameter: float = ...
    """
    Location parameter 
    <hr>
    
    Field Value
    Type:float
    """
    ScaleParameter: float = ...
    """
    Scale parameter 
    <hr>
    
    Field Value
    Type:float
    """
    ShapeParameter: float = ...
    """
    Shape parameter 
    <hr>
    
    Field Value
    Type:float
    """
    ValuesCount: int = ...
    """
    Values count 
    <hr>
    
    Field Value
    Type:int
    """


class MapleExpBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.MapleExpBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.OptimizationCollection.CreateMapleExpBuilder`
    
    .. versionadded:: NX7.5.0
    
    .. deprecated::  NX12.0.0
       Use :py:class:`NXOpen.Optimization.MathIntegrationExpBuilder` instead.
    """
    Null: MapleExpBuilder = ...  # unknown typename


class OptimizationCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a :py:class:`NXOpen.Optimization.OptimizationCollection`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateOptimizationBuilder(self) -> OptimizationBuilder:
        """
        Create builder for optimization class  
        
        Signature ``CreateOptimizationBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.OptimizationBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateOptimizationAttributeBuilder(self) -> OptimizationAttributeBuilder:
        """
        Create builder for OptimizationAttribute class  
        
        Signature ``CreateOptimizationAttributeBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.OptimizationAttributeBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateMapleExpBuilder(self) -> MapleExpBuilder:
        """
        Create builder for MapleExpBuilder class  
        
        Signature ``CreateMapleExpBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.MapleExpBuilder` 
        
        .. versionadded:: NX6.0.0
        
        .. deprecated::  NX12.0.0
           Use :py:meth:`NXOpen.Optimization.OptimizationCollection.CreateMathIntegrationExpBuilder` instead.
        
        License requirements: None.
        """
        ...
    
    
    def CreateMathIntegrationExpBuilder(self) -> MathIntegrationExpBuilder:
        """
        Create builder for MathIntegrationExpBuilder class  
        
        Signature ``CreateMathIntegrationExpBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.MathIntegrationExpBuilder` 
        
        .. versionadded:: NX12.0.0
        
        License requirements: None.
        """
        ...
    


class DesignStudyBuilderDesignStudyAttributeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignStudyBuilderDesignStudyAttributeType():
    """
    Attribute type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Expression", "Expression type"
       "KFAttribute", "KF attribute type"
       "GeometryParameter", "Geometry parameter type"
    """
    Expression = 0  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
    KFAttribute = 1  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
    GeometryParameter = 2  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DesignStudyBuilderDesignStudyConstraintLimitTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignStudyBuilderDesignStudyConstraintLimitType():
    """
    Constraint limit type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Upper", "Upper limit type"
       "Lower", "Lower limit type"
    """
    Upper = 0  # DesignStudyBuilderDesignStudyConstraintLimitTypeMemberType
    Lower = 1  # DesignStudyBuilderDesignStudyConstraintLimitTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DesignStudyBuilderDesignStudyDistributeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class DesignStudyBuilderDesignStudyDistributeType():
    """
    Distribution type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Uniform", "Uniform distribution type"
       "Normal", "Normal distribution type"
       "Gamma", "Gamma distribution type"
    """
    Uniform = 0  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
    Normal = 1  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
    Gamma = 2  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class DesignStudyBuilderDesignStudyObjective_Struct():
    """
    Defined Objective Structure .  
    
    Constructor: 
    NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AttributeName: str = ...
    """
    Attribute name 
    <hr>
    
    Field Value
    Type:str
    """
    AttributeObject: NXOpen.NXObject = ...
    """
    Object which the attribute belongs to, it makes sense with geometry design variable type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    ObjectiveType: DesignStudyBuilderDesignStudyAttributeType = ...
    """
    Objectibe type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType`
    """
    WarningLowerLimit: float = ...
    """
    Warning lower limit 
    <hr>
    
    Field Value
    Type:float
    """
    WarningUpperLimit: float = ...
    """
    Warning Upper limit 
    <hr>
    
    Field Value
    Type:float
    """
    FailureLowerLimit: float = ...
    """
    Failure Lower limit 
    <hr>
    
    Field Value
    Type:float
    """
    FailureUpperLimit: float = ...
    """
    Failure Upper limit 
    <hr>
    
    Field Value
    Type:float
    """


class DesignStudyBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.DesignStudyBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.DesignStudyCollection.CreateDesignStudyBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class DesignStudyAttributeType():
        """
        Attribute type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Expression", "Expression type"
           "KFAttribute", "KF attribute type"
           "GeometryParameter", "Geometry parameter type"
        """
        Expression = 0  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
        KFAttribute = 1  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
        GeometryParameter = 2  # DesignStudyBuilderDesignStudyAttributeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DesignStudyConstraintLimitType():
        """
        Constraint limit type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Upper", "Upper limit type"
           "Lower", "Lower limit type"
        """
        Upper = 0  # DesignStudyBuilderDesignStudyConstraintLimitTypeMemberType
        Lower = 1  # DesignStudyBuilderDesignStudyConstraintLimitTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DesignStudyDistributeType():
        """
        Distribution type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Uniform", "Uniform distribution type"
           "Normal", "Normal distribution type"
           "Gamma", "Gamma distribution type"
        """
        Uniform = 0  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
        Normal = 1  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
        Gamma = 2  # DesignStudyBuilderDesignStudyDistributeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class DesignStudyObjective():
        """
        Defined Objective Structure .  
        
        Constructor: 
        NXOpen.Optimization.DesignStudyBuilder.DesignStudyObjective()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AttributeName: str = ...
        """
        Attribute name 
        <hr>
        
        Field Value
        Type:str
        """
        AttributeObject: NXOpen.NXObject = ...
        """
        Object which the attribute belongs to, it makes sense with geometry design variable type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        ObjectiveType: DesignStudyBuilderDesignStudyAttributeType = ...
        """
        Objectibe type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType`
        """
        WarningLowerLimit: float = ...
        """
        Warning lower limit 
        <hr>
        
        Field Value
        Type:float
        """
        WarningUpperLimit: float = ...
        """
        Warning Upper limit 
        <hr>
        
        Field Value
        Type:float
        """
        FailureLowerLimit: float = ...
        """
        Failure Lower limit 
        <hr>
        
        Field Value
        Type:float
        """
        FailureUpperLimit: float = ...
        """
        Failure Upper limit 
        <hr>
        
        Field Value
        Type:float
        """
    
    
    class DesignStudyVariable():
        """
        Defined variable structure .  
        
        Constructor: 
        NXOpen.Optimization.DesignStudyBuilder.DesignStudyVariable()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AttributeName: str = ...
        """
        Attribute name 
        <hr>
        
        Field Value
        Type:str
        """
        AttributeObject: NXOpen.NXObject = ...
        """
        Object which the attribute belongs to, it makes sense with geometry design variable type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        VariableType: DesignStudyBuilderDesignStudyAttributeType = ...
        """
        Variable type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType`
        """
        VariableLowerLimitValue: float = ...
        """
        Lower limit value 
        <hr>
        
        Field Value
        Type:float
        """
        VariableUpperLimitValue: float = ...
        """
        Upper limit value 
        <hr>
        
        Field Value
        Type:float
        """
        DistributeType: DesignStudyBuilderDesignStudyDistributeType = ...
        """
        Distribute type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyDistributeType`
        """
        LocationParameter: float = ...
        """
        Location parameter 
        <hr>
        
        Field Value
        Type:float
        """
        ScaleParameter: float = ...
        """
        Scale parameter 
        <hr>
        
        Field Value
        Type:float
        """
        ShapeParameter: float = ...
        """
        Shape parameter 
        <hr>
        
        Field Value
        Type:float
        """
        ValuesCount: int = ...
        """
        Values count 
        <hr>
        
        Field Value
        Type:int
        """
    
    
    def RunDesignStudy(self) -> None:
        """
        Run design study process 
        
        Signature ``RunDesignStudy()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDesignStudyObjectives(self) -> 'list[DesignStudyBuilderDesignStudyObjective_Struct]':
        """
        Returns the objectives  
        
        Signature ``GetDesignStudyObjectives()`` 
        
        :returns:  Objectives  
        :rtype: list of :py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyObjective_Struct` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDesignStudyObjectives(self, attributeNames: 'list[str]', attributeObjects: 'list[NXOpen.NXObject]', objectiveTypes: 'list[DesignStudyBuilderDesignStudyAttributeType]', warningLowerLimit: 'list[float]', warningUpperLimit: 'list[float]', failureLowerLimit: 'list[float]', failureUpperLimit: 'list[float]') -> None:
        """
        Sets the objectives 
        
        Signature ``SetDesignStudyObjectives(attributeNames, attributeObjects, objectiveTypes, warningLowerLimit, warningUpperLimit, failureLowerLimit, failureUpperLimit)`` 
        
        :param attributeNames:  Objective attribute name array  
        :type attributeNames: list of str 
        :param attributeObjects:  Objective attribute object array  
        :type attributeObjects: list of :py:class:`NXOpen.NXObject` 
        :param objectiveTypes:  Objective attribute type array  
        :type objectiveTypes: list of :py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType` 
        :param warningLowerLimit:  Warning lower limit  
        :type warningLowerLimit: list of float 
        :param warningUpperLimit:  Warning upper limit  
        :type warningUpperLimit: list of float 
        :param failureLowerLimit:  Failure lower limit  
        :type failureLowerLimit: list of float 
        :param failureUpperLimit:  Failure upper limit  
        :type failureUpperLimit: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetDesignStudyVariables(self) -> 'list[DesignStudyBuilderDesignStudyVariable_Struct]':
        """
        Returns the variables  
        
        Signature ``GetDesignStudyVariables()`` 
        
        :returns:  Variables  
        :rtype: list of :py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyVariable_Struct` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetDesignStudyVariables(self, attributeNames: 'list[str]', attributeObjects: 'list[NXOpen.NXObject]', variableTypes: 'list[DesignStudyBuilderDesignStudyAttributeType]', variableLowerLimitValue: 'list[float]', variableUpperLimitValue: 'list[float]', distributeType: 'list[DesignStudyBuilderDesignStudyDistributeType]', locationParameter: 'list[float]', scaleParameter: 'list[float]', shapeParameter: 'list[float]', valuesCount: 'list[int]') -> None:
        """
        Sets the variables 
        
        Signature ``SetDesignStudyVariables(attributeNames, attributeObjects, variableTypes, variableLowerLimitValue, variableUpperLimitValue, distributeType, locationParameter, scaleParameter, shapeParameter, valuesCount)`` 
        
        :param attributeNames:  Variable attribute name array  
        :type attributeNames: list of str 
        :param attributeObjects:  Variable attribute object array  
        :type attributeObjects: list of :py:class:`NXOpen.NXObject` 
        :param variableTypes:  Variable attribute type array  
        :type variableTypes: list of :py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyAttributeType` 
        :param variableLowerLimitValue:  Variable lower limit value array  
        :type variableLowerLimitValue: list of float 
        :param variableUpperLimitValue:  Variable upper limit value array  
        :type variableUpperLimitValue: list of float 
        :param distributeType:  Distribute type  
        :type distributeType: list of :py:class:`NXOpen.Optimization.DesignStudyBuilderDesignStudyDistributeType` 
        :param locationParameter:  Location parameter  
        :type locationParameter: list of float 
        :param scaleParameter:  Scale parameter  
        :type scaleParameter: list of float 
        :param shapeParameter:  Shape parameter  
        :type shapeParameter: list of float 
        :param valuesCount:  Values count  
        :type valuesCount: list of int 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BuildAllObjectives(self) -> None:
        """
        Build all the objectives 
        
        Signature ``BuildAllObjectives()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllObjectives(self) -> None:
        """
        Remove all the objectives 
        
        Signature ``RemoveAllObjectives()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BuildAllVariables(self) -> None:
        """
        Build all the variables 
        
        Signature ``BuildAllVariables()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllVariables(self) -> None:
        """
        Remove all the variables 
        
        Signature ``RemoveAllVariables()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    IsShowGraph: bool = ...
    """
    Returns or sets  the property - is show graph 
    
    <hr>
    
    Getter Method
    
    Signature ``IsShowGraph`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsShowGraph`` 
    
    :param isShowGraph: 
    :type isShowGraph: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsUpdateDisp: bool = ...
    """
    Returns or sets  the property - is update display 
    
    <hr>
    
    Getter Method
    
    Signature ``IsUpdateDisp`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUpdateDisp`` 
    
    :param isUpdateDisp: 
    :type isUpdateDisp: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    StudyName: str = ...
    """
    Returns or sets  the study name which is unique in one part 
    
    <hr>
    
    Getter Method
    
    Signature ``StudyName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StudyName`` 
    
    :param studyName: 
    :type studyName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: DesignStudyBuilder = ...  # unknown typename


class MathIntegrationExpBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.MathIntegrationExpBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.OptimizationCollection.CreateMathIntegrationExpBuilder`
    
    .. versionadded:: NX12.0.0
    """
    Null: MathIntegrationExpBuilder = ...  # unknown typename


class OptimizationAttributeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.OptimizationAttributeBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.OptimizationCollection.CreateOptimizationAttributeBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def AdoptObject(self, object: NXOpen.NXObject) -> None:
        """
        Adopt object 
        
        Signature ``AdoptObject(object)`` 
        
        :param object:  Object to adopt  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: OptimizationAttributeBuilder = ...  # unknown typename


class OptimizationBuilderOptimizationVariable_Struct():
    """
    Defined variable structure .  
    
    Constructor: 
    NXOpen.Optimization.OptimizationBuilder.OptimizationVariable()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AttributeName: str = ...
    """
    Attribute name 
    <hr>
    
    Field Value
    Type:str
    """
    AttributeObject: NXOpen.NXObject = ...
    """
    Object which the attribute belongs to, it makes sense with geometry design variable type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    VariableType: OptimizationBuilderOptimizationAttributeType = ...
    """
    Variable type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
    """
    VariableLowerLimitValue: float = ...
    """
    Lower limit value 
    <hr>
    
    Field Value
    Type:float
    """
    VariableUpperLimitValue: float = ...
    """
    Upper limit value 
    <hr>
    
    Field Value
    Type:float
    """


class DesignStudyCollection(NXOpen.TaggedObjectCollection):
    """
    Represents a :py:class:`NXOpen.Optimization.DesignStudyCollection`   
    
    To obtain an instance of this class, refer to :py:class:`NXOpen.BasePart`
    
    .. versionadded:: NX6.0.0
    """
    
    def __iter__(self) -> None:
        """Implement iter(self)."""
        ...
    
    
    def CreateDesignStudyBuilder(self) -> DesignStudyBuilder:
        """
        Create builder for design study class  
        
        Signature ``CreateDesignStudyBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.DesignStudyBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def CreateDesignStudyAttributeBuilder(self) -> DesignStudyAttributeBuilder:
        """
        Create builder for DesignStudyAttribute class  
        
        Signature ``CreateDesignStudyAttributeBuilder()`` 
        
        :returns: 
        :rtype: :py:class:`NXOpen.Optimization.DesignStudyAttributeBuilder` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationTargetTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptimizationBuilderOptimizationTargetType():
    """
    Optimization type for objective 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Minimum", "Target is minimum value of design objective"
       "Maximum", "Target is maximum value of design objective"
       "Target", "Target is specified value of design objective"
    """
    Minimum = 0  # OptimizationBuilderOptimizationTargetTypeMemberType
    Maximum = 1  # OptimizationBuilderOptimizationTargetTypeMemberType
    Target = 2  # OptimizationBuilderOptimizationTargetTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationAttributeTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptimizationBuilderOptimizationAttributeType():
    """
    Attribute type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Expression", "Expression attribute"
       "KFAttribute", "KF attribute"
       "GeometryParameter", "Geometry/feature parameter attribute"
    """
    Expression = 0  # OptimizationBuilderOptimizationAttributeTypeMemberType
    KFAttribute = 1  # OptimizationBuilderOptimizationAttributeTypeMemberType
    GeometryParameter = 2  # OptimizationBuilderOptimizationAttributeTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationConstraintLimitTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptimizationBuilderOptimizationConstraintLimitType():
    """
    Constraint limit type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Upper", "Upper limit"
       "Lower", "Lower limit"
    """
    Upper = 0  # OptimizationBuilderOptimizationConstraintLimitTypeMemberType
    Lower = 1  # OptimizationBuilderOptimizationConstraintLimitTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationAlgorithmTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptimizationBuilderOptimizationAlgorithmType():
    """
    Algorithm type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "SimulatedAnnealing", "Simulated annealing"
       "GlobalSimplex", "Global simplex"
       "Powell", "Powell"
       "ConjugateGradient", "Conjugate gradient"
       "Lexicographic", "Lexicographic"
       "PatternSwarm", "Pattern swarm"
    """
    SimulatedAnnealing = 0  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    GlobalSimplex = 1  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    Powell = 2  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    ConjugateGradient = 3  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    Lexicographic = 4  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    PatternSwarm = 5  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType():
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    value = ...
    """value of enum member"""


class OptimizationBuilderOptimizationConvergenceSpeedType():
    """
    Convergence speed type 
    
    Enum Members
    
    .. csv-table::
       :header: "Enum Member", "Enum Member Description" 
    
       "Slow", "Slow convergence speed"
       "Medium", "Medium convergence speed"
       "Fast", "Fast convergence speed"
       "Infinite", "Infinite convergence speed"
    """
    Slow = 0  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
    Medium = 1  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
    Fast = 2  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
    Infinite = 3  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
    
    @staticmethod
    def ValueOf(value: int) -> None:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
        
        Signature ``ValueOf(value)`` 
        
        :param value: Any integer value or bit operation result of enum members
        :type value: int
        :returns:  Enum member equivalent to the value passed.
        :rtype: Enum Member type. 
        
        .. versionadded:: NX9.0.1
        
        License requirements: None.
        """
        ...
    


class OptimizationBuilderOptimizationObjective_Struct():
    """
    Defined Objective Structure .  
    
    Constructor: 
    NXOpen.Optimization.OptimizationBuilder.OptimizationObjective()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AttributeName: str = ...
    """
    Attribute name 
    <hr>
    
    Field Value
    Type:str
    """
    AttributeObject: NXOpen.NXObject = ...
    """
    Object which the attribute belongs to, it makes sense with geometry design variable type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    ObjectiveType: OptimizationBuilderOptimizationAttributeType = ...
    """
    Objectibe type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
    """
    ObjectiveTargetValue: float = ...
    """
    Value of objective target 
    <hr>
    
    Field Value
    Type:float
    """


class OptimizationBuilderOptimizationConstraint_Struct():
    """
    Defined constraint structure .  
    
    Constructor: 
    NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint()
    """
    
    def __str__(self) -> None:
        """Return str(self)."""
        ...
    
    AttributeName: str = ...
    """
    Attribute name 
    <hr>
    
    Field Value
    Type:str
    """
    AttributeObject: NXOpen.NXObject = ...
    """
    Object which the attribute belongs to, it makes sense with geometry design variable type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.NXObject`
    """
    ConstraintType: OptimizationBuilderOptimizationAttributeType = ...
    """
    Constraint type 
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
    """
    ConstraintLowerLimitValue: float = ...
    """
    Lower limit value 
    <hr>
    
    Field Value
    Type:float
    """
    ConstraintUpperLimitValue: float = ...
    """
    Upper limit value 
    <hr>
    
    Field Value
    Type:float
    """
    ConstraintLimitType: OptimizationBuilderOptimizationConstraintLimitType = ...
    """
    constraint limit type, lower type or upper type
    <hr>
    
    Field Value
    Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConstraintLimitType`
    """


class OptimizationBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.OptimizationBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.OptimizationCollection.CreateOptimizationBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    class OptimizationTargetType():
        """
        Optimization type for objective 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Minimum", "Target is minimum value of design objective"
           "Maximum", "Target is maximum value of design objective"
           "Target", "Target is specified value of design objective"
        """
        Minimum = 0  # OptimizationBuilderOptimizationTargetTypeMemberType
        Maximum = 1  # OptimizationBuilderOptimizationTargetTypeMemberType
        Target = 2  # OptimizationBuilderOptimizationTargetTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OptimizationAttributeType():
        """
        Attribute type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Expression", "Expression attribute"
           "KFAttribute", "KF attribute"
           "GeometryParameter", "Geometry/feature parameter attribute"
        """
        Expression = 0  # OptimizationBuilderOptimizationAttributeTypeMemberType
        KFAttribute = 1  # OptimizationBuilderOptimizationAttributeTypeMemberType
        GeometryParameter = 2  # OptimizationBuilderOptimizationAttributeTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OptimizationConstraintLimitType():
        """
        Constraint limit type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Upper", "Upper limit"
           "Lower", "Lower limit"
        """
        Upper = 0  # OptimizationBuilderOptimizationConstraintLimitTypeMemberType
        Lower = 1  # OptimizationBuilderOptimizationConstraintLimitTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OptimizationAlgorithmType():
        """
        Algorithm type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "SimulatedAnnealing", "Simulated annealing"
           "GlobalSimplex", "Global simplex"
           "Powell", "Powell"
           "ConjugateGradient", "Conjugate gradient"
           "Lexicographic", "Lexicographic"
           "PatternSwarm", "Pattern swarm"
        """
        SimulatedAnnealing = 0  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        GlobalSimplex = 1  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        Powell = 2  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        ConjugateGradient = 3  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        Lexicographic = 4  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        PatternSwarm = 5  # OptimizationBuilderOptimizationAlgorithmTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OptimizationConvergenceSpeedType():
        """
        Convergence speed type 
        
        Enum Members
        
        .. csv-table::
           :header: "Enum Member", "Enum Member Description" 
        
           "Slow", "Slow convergence speed"
           "Medium", "Medium convergence speed"
           "Fast", "Fast convergence speed"
           "Infinite", "Infinite convergence speed"
        """
        Slow = 0  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
        Medium = 1  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
        Fast = 2  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
        Infinite = 3  # OptimizationBuilderOptimizationConvergenceSpeedTypeMemberType
        
        @staticmethod
        def ValueOf(value: int) -> None:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members. 
            
            Signature ``ValueOf(value)`` 
            
            :param value: Any integer value or bit operation result of enum members
            :type value: int
            :returns:  Enum member equivalent to the value passed.
            :rtype: Enum Member type. 
            
            .. versionadded:: NX9.0.1
            
            License requirements: None.
            """
            ...
        
    
    
    class OptimizationObjective():
        """
        Defined Objective Structure .  
        
        Constructor: 
        NXOpen.Optimization.OptimizationBuilder.OptimizationObjective()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AttributeName: str = ...
        """
        Attribute name 
        <hr>
        
        Field Value
        Type:str
        """
        AttributeObject: NXOpen.NXObject = ...
        """
        Object which the attribute belongs to, it makes sense with geometry design variable type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        ObjectiveType: OptimizationBuilderOptimizationAttributeType = ...
        """
        Objectibe type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
        """
        ObjectiveTargetValue: float = ...
        """
        Value of objective target 
        <hr>
        
        Field Value
        Type:float
        """
    
    
    class OptimizationVariable():
        """
        Defined variable structure .  
        
        Constructor: 
        NXOpen.Optimization.OptimizationBuilder.OptimizationVariable()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AttributeName: str = ...
        """
        Attribute name 
        <hr>
        
        Field Value
        Type:str
        """
        AttributeObject: NXOpen.NXObject = ...
        """
        Object which the attribute belongs to, it makes sense with geometry design variable type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        VariableType: OptimizationBuilderOptimizationAttributeType = ...
        """
        Variable type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
        """
        VariableLowerLimitValue: float = ...
        """
        Lower limit value 
        <hr>
        
        Field Value
        Type:float
        """
        VariableUpperLimitValue: float = ...
        """
        Upper limit value 
        <hr>
        
        Field Value
        Type:float
        """
    
    
    class OptimizationConstraint():
        """
        Defined constraint structure .  
        
        Constructor: 
        NXOpen.Optimization.OptimizationBuilder.OptimizationConstraint()
        """
        
        def __str__(self) -> None:
            """Return str(self)."""
            ...
        
        AttributeName: str = ...
        """
        Attribute name 
        <hr>
        
        Field Value
        Type:str
        """
        AttributeObject: NXOpen.NXObject = ...
        """
        Object which the attribute belongs to, it makes sense with geometry design variable type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.NXObject`
        """
        ConstraintType: OptimizationBuilderOptimizationAttributeType = ...
        """
        Constraint type 
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType`
        """
        ConstraintLowerLimitValue: float = ...
        """
        Lower limit value 
        <hr>
        
        Field Value
        Type:float
        """
        ConstraintUpperLimitValue: float = ...
        """
        Upper limit value 
        <hr>
        
        Field Value
        Type:float
        """
        ConstraintLimitType: OptimizationBuilderOptimizationConstraintLimitType = ...
        """
        constraint limit type, lower type or upper type
        <hr>
        
        Field Value
        Type::py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConstraintLimitType`
        """
    
    
    def RunOptimization(self) -> None:
        """
        Run optimization process 
        
        Signature ``RunOptimization()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptimizationObjectives(self) -> 'list[OptimizationBuilderOptimizationObjective_Struct]':
        """
        Returns the objectives  
        
        Signature ``GetOptimizationObjectives()`` 
        
        :returns:  Objectives  
        :rtype: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationObjective_Struct` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOptimizationObjectives(self, attributeNames: 'list[str]', attributeObjects: 'list[NXOpen.NXObject]', objectiveTypes: 'list[OptimizationBuilderOptimizationAttributeType]', objectiveTargetValues: 'list[float]') -> None:
        """
        Sets the objectives 
        
        Signature ``SetOptimizationObjectives(attributeNames, attributeObjects, objectiveTypes, objectiveTargetValues)`` 
        
        :param attributeNames:  Objective attribute name array  
        :type attributeNames: list of str 
        :param attributeObjects:  Objective attribute object array  
        :type attributeObjects: list of :py:class:`NXOpen.NXObject` 
        :param objectiveTypes:  Objective attribute type array  
        :type objectiveTypes: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType` 
        :param objectiveTargetValues:  Objective target value array  
        :type objectiveTargetValues: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptimizationVariables(self) -> 'list[OptimizationBuilderOptimizationVariable_Struct]':
        """
        Returns the variables  
        
        Signature ``GetOptimizationVariables()`` 
        
        :returns:  Variables  
        :rtype: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationVariable_Struct` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOptimizationVariables(self, attributeNames: 'list[str]', attributeObjects: 'list[NXOpen.NXObject]', variableTypes: 'list[OptimizationBuilderOptimizationAttributeType]', variableLowerLimitValue: 'list[float]', variableUpperLimitValue: 'list[float]') -> None:
        """
        Sets the variables 
        
        Signature ``SetOptimizationVariables(attributeNames, attributeObjects, variableTypes, variableLowerLimitValue, variableUpperLimitValue)`` 
        
        :param attributeNames:  Variable attribute name array  
        :type attributeNames: list of str 
        :param attributeObjects:  Variable attribute object array  
        :type attributeObjects: list of :py:class:`NXOpen.NXObject` 
        :param variableTypes:  Variable attribute type array  
        :type variableTypes: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType` 
        :param variableLowerLimitValue:  Variable lower limit value array  
        :type variableLowerLimitValue: list of float 
        :param variableUpperLimitValue:  Variable upper limit value array  
        :type variableUpperLimitValue: list of float 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def GetOptimizationConstraints(self) -> 'list[OptimizationBuilderOptimizationConstraint_Struct]':
        """
        Returns the constraints  
        
        Signature ``GetOptimizationConstraints()`` 
        
        :returns:  Constraints  
        :rtype: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConstraint_Struct` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def SetOptimizationConstraints(self, attributeNames: 'list[str]', attributeObjects: 'list[NXOpen.NXObject]', constraintTypes: 'list[OptimizationBuilderOptimizationAttributeType]', constraintLowerLimitValue: 'list[float]', constraintUpperLimitValue: 'list[float]', constraintLimitType: 'list[OptimizationBuilderOptimizationConstraintLimitType]') -> None:
        """
        Sets the constraints 
        
        Signature ``SetOptimizationConstraints(attributeNames, attributeObjects, constraintTypes, constraintLowerLimitValue, constraintUpperLimitValue, constraintLimitType)`` 
        
        :param attributeNames:  Constraint attribute name array  
        :type attributeNames: list of str 
        :param attributeObjects:  Constraint attribute type array  
        :type attributeObjects: list of :py:class:`NXOpen.NXObject` 
        :param constraintTypes:  Constraint attribute type array  
        :type constraintTypes: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAttributeType` 
        :param constraintLowerLimitValue:  Constraint lower limit value array  
        :type constraintLowerLimitValue: list of float 
        :param constraintUpperLimitValue:  Constraint upper limit value array  
        :type constraintUpperLimitValue: list of float 
        :param constraintLimitType:  Constraint atribute limit type array  
        :type constraintLimitType: list of :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConstraintLimitType` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BuildAllObjectives(self) -> None:
        """
        Build all the objectives 
        
        Signature ``BuildAllObjectives()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllObjectives(self) -> None:
        """
        Remove all the objectives 
        
        Signature ``RemoveAllObjectives()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BuildAllVariables(self) -> None:
        """
        Build all the variables 
        
        Signature ``BuildAllVariables()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllVariables(self) -> None:
        """
        Remove all the variables 
        
        Signature ``RemoveAllVariables()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def BuildAllConstraints(self) -> None:
        """
        Build all the constraints 
        
        Signature ``BuildAllConstraints()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    
    def RemoveAllConstraints(self) -> None:
        """
        Remove all the constraints 
        
        Signature ``RemoveAllConstraints()`` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    AbsoluteConvergenceCriteria: float = ...
    """
    Returns or sets  the absolute criteria for optimizer to determine convergence.  
    
    This value is
    multiplied by the first objective result,and if the difference in last two 
    objective results is less than this, then it is converged 
    
    <hr>
    
    Getter Method
    
    Signature ``AbsoluteConvergenceCriteria`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AbsoluteConvergenceCriteria`` 
    
    :param absoluteConvergenceCriteria: 
    :type absoluteConvergenceCriteria: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    AlgorithmType: OptimizationBuilderOptimizationAlgorithmType = ...
    """
    Returns or sets  the algorithm type 
    
    <hr>
    
    Getter Method
    
    Signature ``AlgorithmType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAlgorithmType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``AlgorithmType`` 
    
    :param algorithmType: 
    :type algorithmType: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationAlgorithmType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    ConvergenceSpeedType: OptimizationBuilderOptimizationConvergenceSpeedType = ...
    """
    Returns or sets  the convergence speed type 
    
    <hr>
    
    Getter Method
    
    Signature ``ConvergenceSpeedType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConvergenceSpeedType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``ConvergenceSpeedType`` 
    
    :param convergenceSpeedType: 
    :type convergenceSpeedType: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationConvergenceSpeedType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsShowGraph: bool = ...
    """
    Returns or sets  the property - is show graph 
    
    <hr>
    
    Getter Method
    
    Signature ``IsShowGraph`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsShowGraph`` 
    
    :param isShowGraph: 
    :type isShowGraph: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    IsUpdateDisp: bool = ...
    """
    Returns or sets  the property - is update display 
    
    <hr>
    
    Getter Method
    
    Signature ``IsUpdateDisp`` 
    
    :returns: 
    :rtype: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``IsUpdateDisp`` 
    
    :param isUpdateDisp: 
    :type isUpdateDisp: bool 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MaxNumberIteration: int = ...
    """
    Returns or sets  the maximum number of updates allowed without converging to a solutionthe maximum iterations time
    
    <hr>
    
    Getter Method
    
    Signature ``MaxNumberIteration`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxNumberIteration`` 
    
    :param maxNumberIteration: 
    :type maxNumberIteration: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    MaxTime: int = ...
    """
    Returns or sets  the maximum time allowed for this run in seconds 
    
    <hr>
    
    Getter Method
    
    Signature ``MaxTime`` 
    
    :returns: 
    :rtype: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``MaxTime`` 
    
    :param maxTime: 
    :type maxTime: int 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    OptimizationType: OptimizationBuilderOptimizationTargetType = ...
    """
    Returns or sets  the optimization type 
    
    <hr>
    
    Getter Method
    
    Signature ``OptimizationType`` 
    
    :returns: 
    :rtype: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationTargetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``OptimizationType`` 
    
    :param optimizationType: 
    :type optimizationType: :py:class:`NXOpen.Optimization.OptimizationBuilderOptimizationTargetType` 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    RelativeConvergenceCriteria: float = ...
    """
    Returns or sets  the relative criteria for optimizer
    to determine convergence.  
    
    If one minus
    the ratio of the last two iterations is
    less than this value, the solution is converged 
    
    <hr>
    
    Getter Method
    
    Signature ``RelativeConvergenceCriteria`` 
    
    :returns: 
    :rtype: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``RelativeConvergenceCriteria`` 
    
    :param relativeConvergenceCriteria: 
    :type relativeConvergenceCriteria: float 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    StudyName: str = ...
    """
    Returns or sets  the study name which is unique in one part 
    
    <hr>
    
    Getter Method
    
    Signature ``StudyName`` 
    
    :returns: 
    :rtype: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    
    <hr>
    
    Setter Method
    
    Signature ``StudyName`` 
    
    :param studyName: 
    :type studyName: str 
    
    .. versionadded:: NX6.0.0
    
    License requirements: None.
    """
    Null: OptimizationBuilder = ...  # unknown typename


class DesignStudyAttributeBuilder(NXOpen.Builder):
    """
    Represents a :py:class:`NXOpen.Optimization.DesignStudyAttributeBuilder`   
    
    To create a new instance of this class, use :py:meth:`NXOpen.Optimization.DesignStudyCollection.CreateDesignStudyAttributeBuilder`
    
    .. versionadded:: NX6.0.0
    """
    
    def AdoptObject(self, object: NXOpen.NXObject) -> None:
        """
        Adopt object 
        
        Signature ``AdoptObject(object)`` 
        
        :param object:  Object to adopt  
        :type object: :py:class:`NXOpen.NXObject` 
        
        .. versionadded:: NX6.0.0
        
        License requirements: None.
        """
        ...
    
    Null: DesignStudyAttributeBuilder = ...  # unknown typename


