from enum import Enum


class IndicatorNames(str, Enum):
    """
    Enum class to some usefull indicator names in datasource
    """

    secondary_enrolment_net_rate = "Net enrolment rate, lower secondary, both sexes (%)"
    primary_enrolment__net_rate = "Total net enrolment rate, primary, both sexes (%)"
    primary_secondary_enrolment_gross_ratio = (
        "Gross enrolment ratio, primary and lower secondary, both sexes (%)"
    )
    government_expenditure__per_student_primary = (
        "Government expenditure per primary student as % of GDP per capita (%)"
    )
    government_expenditure__per_student_secondary = (
        "Government expenditure per secondary student as % of GDP per capita (%)"
    )
