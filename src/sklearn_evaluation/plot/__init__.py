"""
Plotting functions
"""

from .classification import (confusion_matrix, feature_importances,
                             precision_at_proportions, ConfusionMatrix)

from .roc import roc
from .precision_recall import precision_recall
from .grid_search import grid_search
from .validation_curve import validation_curve
from .learning_curve import learning_curve
from .metrics import metrics_at_thresholds
from .clustering import elbow_curve, elbow_curve_from_results, silhouette_plot, silhouette_plot_from_results

from .calibration import calibration_curve, scores_distribution
from .classification_report import classification_report, ClassificationReport


__all__ = [
    'confusion_matrix',
    'feature_importances',
    'precision_recall',
    'roc',
    'precision_at_proportions',
    'grid_search',
    'validation_curve',
    'learning_curve',
    'metrics_at_thresholds',
    'ConfusionMatrix',
    'elbow_curve',
    'elbow_curve_from_results',
    'silhouette_plot',
    'calibration_curve',
    'scores_distribution',
    'classification_report',
    'ClassificationReport',
]
