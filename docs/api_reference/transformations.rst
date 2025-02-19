.. _transformations_ref:

Time series transformations
===========================

The :mod:`aeon.transformations` module contains classes for data
transformations.

.. automodule:: aeon.transformations
   :no-members:
   :no-inherited-members:

All (simple) transformers in ``aeon``can be listed using the ``aeon.registry.all_estimators`` utility,
using ``estimator_types="regressor"``, optionally filtered by tags.
Valid tags can be listed using ``aeon.registry.all_tags``.

For pairwise transformers (time series distances, kernels), instead see :ref:`_transformations_pairwise_ref`.

Transformations are categorized as follows:

.. list-table::
   :header-rows: 1

   * - Category
     - Explanation
     - Example
   * - Composition
     - Building blocks for pipelines, wrappers, adapters
     - Transformer pipeline
   * - Series-to-features
     - Transforms series to float/category vector
     - Length and mean
   * - Series-to-series
     - Transforms individual series to series
     - Differencing, detrending
   * - Series-to-Panel
     - transforms a series into a panel
     - Bootstrap, sliding window
   * - Panel transform
     - Transforms panel to panel, not by-series
     - Padding to equal length
   * - Hierarchical
     - uses hierarchy information non-trivially
     - Reconciliation

Composition
-----------

Pipeline building
~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.compose

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TransformerPipeline
    FeatureUnion
    ColumnwiseTransformer
    ColumnTransformer
    FitInTransform
    MultiplexTransformer
    OptionalPassthrough
    InvertTransform
    Id
    YtoX

.. currentmodule:: aeon.transformations.series.func_transform

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    FunctionTransformer

Sklearn and pandas adapters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.collection.reduce

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Tabularizer
    TimeBinner

.. currentmodule:: aeon.transformations.series.adapt

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TabularToSeriesAdaptor
    PandasTransformAdaptor

Series-to-features transformers
-------------------------------

Series-to-features transformers transform individual time series to a collection of primitive features.
Primitive features are usually a vector of floats, but can also be categorical.

When applied to panels or hierarchical data, the transformation result is a table with as many rows as time series in the collection.

Summarization
~~~~~~~~~~~~~

These transformers extract simple summary features.

.. currentmodule:: aeon.transformations.series.summarize

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    SummaryTransformer
    WindowSummarizer
    FittedParamExtractor


Shapelets, wavelets, and convolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.collection.shapelet_based

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    RandomShapeletTransform
    RandomDilatedShapeletTransform

.. currentmodule:: aeon.transformations.collection.convolution_based

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Rocket
    MiniRocket
    MiniRocketMultivariate
    MiniRocketMultivariateVariable
    MultiRocket
    MultiRocketMultivariate

.. currentmodule:: aeon.transformations.collection.dwt

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    DWTTransformer

Distance-based features
~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.collection.matrix_profile

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    MatrixProfile

Dictionary-based features
~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.collection.dictionary_based

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    PAA
    SFA
    SAX

Moment-based features
~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.collection.signature_based

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    SignatureTransformer

Feature collections
~~~~~~~~~~~~~~~~~~~

These transformers extract larger collections of features.

.. currentmodule:: aeon.transformations.collection.tsfresh

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TSFreshRelevantFeatureExtractor
    TSFreshFeatureExtractor

.. currentmodule:: aeon.transformations.collection.catch22

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Catch22

Series-to-series transformers
-----------------------------

Series-to-series transformers transform individual time series into another time series.

When applied to panels or hierarchical data, individual series are transformed.

Lagging
~~~~~~~

.. currentmodule:: aeon.transformations.series.lag

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Lag

Element-wise transforms
~~~~~~~~~~~~~~~~~~~~~~~

These transformations apply a function element-wise.

Depending on the transformer, the transformation parameters can be fitted.

.. currentmodule:: aeon.transformations.series.boxcox

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    BoxCoxTransformer
    LogTransformer

.. currentmodule:: aeon.transformations.series.scaledlogit

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ScaledLogitTransformer

.. currentmodule:: aeon.transformations.series.cos

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    CosineTransformer

.. currentmodule:: aeon.transformations.series.exponent

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ExponentTransformer
    SqrtTransformer

Detrending
~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.detrend

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Detrender
    Deseasonalizer
    ConditionalDeseasonalizer
    STLTransformer

.. currentmodule:: aeon.transformations.series.clear_sky

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ClearSky


Filtering and denoising
~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.bkfilter

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    BKFilter

.. currentmodule:: aeon.transformations.series.filter

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Filter

.. currentmodule:: aeon.transformations.series.kalman_filter

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    KalmanFilterTransformer

.. currentmodule:: aeon.transformations.series.theta

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ThetaLinesTransformer

Differencing and slope
~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.difference

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Differencer

.. currentmodule:: aeon.transformations.collection.slope

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    SlopeTransformer

Binning and segmentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.binning

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TimeBinAggregate

.. currentmodule:: aeon.transformations.collection.interpolate

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TSInterpolator

.. currentmodule:: aeon.transformations.collection.segment

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    IntervalSegmenter
    RandomIntervalSegmenter

Missing value imputation
~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.impute

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Imputer

Seasonality and Date-Time Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.date

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    DateTimeFeatures

.. currentmodule:: aeon.transformations.series.time_since

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TimeSince

.. currentmodule:: aeon.transformations.series.fourier

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    FourierFeatures

Auto-correlation series
~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.acf

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    AutoCorrelationTransformer
    PartialAutoCorrelationTransformer

Window-based series transforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These transformers create a series based on a sequence of sliding windows.

.. currentmodule:: aeon.transformations.series.matrix_profile

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    MatrixProfileTransformer

.. currentmodule:: aeon.transformations.collection.hog1d

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    HOG1DTransformer

Multivariate-to-univariate
~~~~~~~~~~~~~~~~~~~~~~~~~~

These transformers convert multivariate series to univariate.

.. currentmodule:: aeon.transformations.compose

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ColumnConcatenator

Augmentation
~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.augmenter

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    InvertAugmenter
    RandomSamplesAugmenter
    ReverseAugmenter
    WhiteNoiseAugmenter

FeatureSelection
~~~~~~~~~~~~~~~~

These transformers select features in `X` based on `y`.

.. currentmodule:: aeon.transformations.series.feature_selection

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    FeatureSelection

.. currentmodule:: aeon.transformations.collection.channel_selection

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ElbowClassSum
    ElbowClassPairwise

Subsetting time points and variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These transformers subset `X` by time points (`pandas` index or index level) or variables (`pandas` columns).

.. currentmodule:: aeon.transformations.series.subset

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ColumnSelect
    IndexSubset

Panel transformers
------------------

Panel transformers transform a panel of time series into a panel of time series.

A panel transformer is fitted on an entire panel, and not per series.

Equal length transforms
~~~~~~~~~~~~~~~~~~~~~~~

These transformations ensure all series in a panel have equal length

.. currentmodule:: aeon.transformations.collection.pad

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    PaddingTransformer

.. currentmodule:: aeon.transformations.collection.truncate

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    TruncationTransformer


Dimension reduction
~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.series.pca

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    PCATransformer

Series-to-Panel transformers
----------------------------

These transformers create a panel from a single series.

Bootstrap transformations
~~~~~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: aeon.transformations.bootstrap

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    STLBootstrapTransformer
    MovingBlockBootstrapTransformer

Outlier detection, changepoint detection
----------------------------------------

.. currentmodule:: aeon.transformations.series.outlier_detection

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    HampelFilter

.. currentmodule:: aeon.transformations.series.clasp

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    ClaSPTransformer

Hierarchical transformers
-------------------------

These transformers are specifically for hierarchical data and panel data.

The transformation depends on the specified hierarchy in a non-trivial way.

.. currentmodule:: aeon.transformations.hierarchical.aggregate

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Aggregator

.. currentmodule:: aeon.transformations.hierarchical.reconcile

.. autosummary::
    :toctree: auto_generated/
    :template: class.rst

    Reconciler
