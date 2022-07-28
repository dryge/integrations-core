# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.base import ConfigurationError
from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.impala import ImpalaCheck


@pytest.mark.unit
def test_config_unknown_service_type():
    instance = {
        "openmetrics_endpoint": "http://localhost:25000/metrics_prometheus",
        "service_type": "unknown",
    }

    with pytest.raises(ConfigurationError) as exception_info:
        check = ImpalaCheck("Impala", {}, [instance])
        check.load_configuration_models()

    assert exception_info.value.args[0] == 'Detected 1 error while loading configuration model `InstanceConfig`:\nservice_type\n  unexpected value; permitted: \'daemon\', \'statestore\', \'catalog\''


@pytest.mark.unit
@pytest.mark.parametrize(
    'service_type',
    [
        "daemon",
        "statestore",
        "catalog",
    ],
)
def test_config_valid_service_type(service_type):
    instance = {
        "openmetrics_endpoint": "http://localhost:25000/metrics_prometheus",
        "service_type": service_type,
    }

    check = ImpalaCheck("Impala", {}, [instance])
    check.load_configuration_models()
