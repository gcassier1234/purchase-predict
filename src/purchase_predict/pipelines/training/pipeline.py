from kedro.pipeline import Pipeline, node

from .nodes import auto_ml


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                auto_ml,
                ["X_train", "y_train", "X_test", "y_test", "params:auto_ml_max_evals"],
                dict(model="model"),
            )
        ]
    )
