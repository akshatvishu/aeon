"""Retrieval utility for test scenarios."""

__author__ = ["fkiraly"]

__all__ = ["retrieve_scenarios"]


from aeon.base import BaseObject
from aeon.registry import BASE_CLASS_IDENTIFIER_LIST, get_identifiers
from aeon.utils._testing.scenarios_classification import (
    scenarios_classification,
    scenarios_early_classification,
    scenarios_regression,
)
from aeon.utils._testing.scenarios_clustering import scenarios_clustering
from aeon.utils._testing.scenarios_forecasting import scenarios_forecasting
from aeon.utils._testing.scenarios_transformers import scenarios_transformers

scenarios = dict()
scenarios["classifier"] = scenarios_classification
scenarios["early_classifier"] = scenarios_early_classification
scenarios["clusterer"] = scenarios_clustering
scenarios["forecaster"] = scenarios_forecasting
scenarios["regressor"] = scenarios_regression
scenarios["transformer"] = scenarios_transformers


def retrieve_scenarios(obj, filter_tags=None):
    """Retrieve test scenarios for obj, or by estimator type string.

    Exactly one of the arguments obj, estimator_type must be provided.

    Parameters
    ----------
    obj : class or object, or string, or list of str.
        Which kind of estimator/object to retrieve scenarios for.
        If object, must be a class or object inheriting from BaseObject.
        If string(s), must be in registry.BASE_CLASS_REGISTER (first col)
            for instance 'classifier', 'regressor', 'transformer', 'forecaster'
    filter_tags: dict of (str or list of str), default=None
        subsets the returned objectss as follows:
            each key/value pair is statement in "and"/conjunction
                key is tag name to sub-set on
                value str or list of string are tag values
                condition is "key must be equal to value, or in set(value)"

    Returns
    -------
    scenarios : list of objects, instances of BaseScenario
    """
    if not isinstance(obj, (str, BaseObject)) and not issubclass(obj, BaseObject):
        raise TypeError("obj must be a str or inherit from BaseObject")
    if isinstance(obj, str) and obj not in BASE_CLASS_IDENTIFIER_LIST:
        raise ValueError(
            "if obj is a str, then obj must be a valid identifier, "
            "see registry.BASE_CLASS_IDENTIFIER_LIST for valid identifier strings"
        )

    # if class, get identifier from inference; otherwise, str or list of str
    if not isinstance(obj, str):
        estimator_type = get_identifiers(obj)
    else:
        estimator_type = obj

    # coerce to list, ensure estimator_type is list of str
    if not isinstance(estimator_type, list):
        estimator_type = [estimator_type]

    # now loop through types and retrieve scenarios
    scenarios_for_type = []
    for est_type in estimator_type:
        scens = scenarios.get(est_type)
        if scens is not None:
            scenarios_for_type += scenarios.get(est_type)

    # instantiate all scenarios by calling constructor
    scenarios_for_type = [x() for x in scenarios_for_type]

    # if obj was an object, filter to applicable scenarios
    if not isinstance(obj, str) and not isinstance(obj, list):
        scenarios_for_type = [x for x in scenarios_for_type if x.is_applicable(obj)]

    if filter_tags is not None:
        scenarios_for_type = [
            scen for scen in scenarios_for_type if _check_tag_cond(scen, filter_tags)
        ]

    return scenarios_for_type


def _check_tag_cond(obj, filter_tags=None):
    """Check whether object satisfies filter_tags condition.

    Parameters
    ----------
    obj: object inheriting from aeon BaseObject
    filter_tags: dict of (str or list of str), default=None
        subsets the returned objectss as follows:
            each key/value pair is statement in "and"/conjunction
                key is tag name to sub-set on
                value str or list of string are tag values
                condition is "key must be equal to value, or in set(value)"

    Returns
    -------
    cond_sat: bool, whether estimator satisfies condition in filter_tags
    """
    if not isinstance(filter_tags, dict):
        raise TypeError("filter_tags must be a dict")

    cond_sat = True

    for key, value in filter_tags.items():
        if not isinstance(value, list):
            value = [value]
        cond_sat = cond_sat and obj.get_class_tag(key) in set(value)

    return cond_sat
