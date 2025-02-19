"""Unit tests of FitInTransform functionality."""

__author__ = ["aiwalter"]
__all__ = []

from pandas.testing import assert_series_equal

from aeon.forecasting.model_selection import temporal_train_test_split
from aeon.transformations.compose import FitInTransform
from aeon.transformations.series.boxcox import BoxCoxTransformer
from aeon.utils._testing.forecasting import make_forecasting_problem

X = make_forecasting_problem()
X_train, X_test = temporal_train_test_split(X)


def test_transform_fitintransform():
    """Test fit/transform against BoxCoxTransformer."""
    fitintransform = FitInTransform(BoxCoxTransformer())
    fitintransform.fit(X=X_train)
    y_hat = fitintransform.transform(X=X_test)

    y_hat_expected = BoxCoxTransformer().fit_transform(X_test)
    assert_series_equal(y_hat, y_hat_expected)
