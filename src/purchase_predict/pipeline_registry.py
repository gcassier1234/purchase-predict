"""Project pipelines."""

from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from purchase_predict.pipelines.processing import pipline as processing_pipeline
from purchase_predict.pipelines.training import pipeline as training_pipeline
from purchase_predict.pipelines.loading import pipeline as loading_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    pipelines["processing"] = processing_pipeline.create_pipeline()
    pipelines["training"] = training_pipeline.create_pipeline()
    pipelines["loading"] = loading_pipeline.create_pipeline()
    pipelines["global"] = Pipeline([pipelines["loading"], pipelines["processing"], pipelines["training"]])
    return pipelines
