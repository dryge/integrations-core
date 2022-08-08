# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.impala import ImpalaCheck


@pytest.mark.unit
@pytest.mark.metrics_filename("statestored-metrics.txt")
def test_statestore_mock_assert_metrics_using_metadata(dd_run_check, aggregator, statestore_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [statestore_instance])
    dd_run_check(check)
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


@pytest.mark.unit
@pytest.mark.metrics_filename("statestored-metrics.txt")
def test_statestore_mock_assert_service_check(dd_run_check, aggregator, statestore_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [statestore_instance])
    dd_run_check(check)
    aggregator.assert_service_check(
        "impala.statestore.openmetrics.health",
        status=ImpalaCheck.OK,
        tags=['endpoint:http://localhost:25010/metrics_prometheus'],
    )


@pytest.mark.unit
@pytest.mark.metrics_filename("statestored-metrics.txt")
def test_statestore_mock_assert_metrics(dd_run_check, aggregator, statestore_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [statestore_instance])
    dd_run_check(check)

    expected_metrics = [
        {
            "name": "impala.statestore.live_backends",
            "value": 2,
        },
    ]

    for expected_metric in expected_metrics:
        aggregator.assert_metric(
            name=expected_metric["name"],
            value=expected_metric["value"],
            metric_type=expected_metric.get("type", aggregator.GAUGE),
            tags=expected_metric.get("tags", ["endpoint:http://localhost:25010/metrics_prometheus"]),
        )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_no_duplicate_all()
