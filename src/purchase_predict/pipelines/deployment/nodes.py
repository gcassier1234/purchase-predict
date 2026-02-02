import os
import mlflow

from mlflow.tracking import MlflowClient


def push_to_model_registry(registry_name: str, run_id: int):
    mlflow.set_tracking_uri(os.getenv("MLFLOW_SERVER"))
    mlflow.set_tracking_uri(os.getenv("MLFLOW_SERVER"))
    result = mlflow.register_model("runs:/{}/model".format(run_id), registry_name)
    return result.version


def stage_model(registry_name: str, version: int):
    env = os.getenv("ENV")
    if env not in ["staging", "production"]:
        return

    client = MlflowClient()
    client.set_registered_model_alias(name=registry_name, alias=env, version=str(version))
