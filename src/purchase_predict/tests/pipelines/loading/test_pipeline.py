from kedro.runner import SequentialRunner

from purchase_predict.pipelines.loading.pipeline import create_pipeline

import pandas as pd


def test_pipeline(catalog_test):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    runner.run(pipeline, catalog_test)
    df = catalog_test.load("primary")
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 16
    assert "purchased" in df
