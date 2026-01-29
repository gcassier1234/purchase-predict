import pytest

from kedro.io import DataCatalog, MemoryDataset


@pytest.fixture(scope="module")
def project_id():
    return "mlops-485718"


@pytest.fixture(scope="module")
def primary_folder():
    return "purchase-predict-blent/data-test"


@pytest.fixture(scope="module")
def catalog_test(project_id, primary_folder):
    catalog = DataCatalog(
        {"params:gcp_project_id": MemoryDataset(project_id), "params:gcs_primary_folder": MemoryDataset(primary_folder)}
    )
    return catalog
