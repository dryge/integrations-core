# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.impala import ImpalaCheck


@pytest.mark.unit
@pytest.mark.filename("impalad-metrics.txt")
def test_daemon_mock_assert_metrics_using_metadata(dd_run_check, aggregator, daemon_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [daemon_instance])
    dd_run_check(check)
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


@pytest.mark.unit
@pytest.mark.filename("impalad-metrics.txt")
def test_daemon_mock_assert_service_check(dd_run_check, aggregator, daemon_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [daemon_instance])
    dd_run_check(check)
    aggregator.assert_service_check("impala.daemon.openmetrics.health", status=ImpalaCheck.OK)


@pytest.mark.unit
@pytest.mark.filename("impalad-metrics.txt")
def test_daemon_mock_assert_metrics(dd_run_check, aggregator, daemon_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [daemon_instance])
    dd_run_check(check)

    expected_metrics = [
        {
            "name": "impala.daemon.jvm.gc.count",
            "value": 9.0,
            "type": aggregator.MONOTONIC_COUNT,
        },
    ]

    for expected_metric in expected_metrics:
        aggregator.assert_metric(
            name=expected_metric["name"],
            value=expected_metric["value"],
            metric_type=expected_metric.get("type", aggregator.GAUGE),
            tags=expected_metric.get("tags", ["endpoint:http://localhost:25000/metrics_prometheus"]),
        )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_no_duplicate_all()


@pytest.mark.unit
@pytest.mark.filename("statestored-metrics.txt")
def test_statestore_mock_assert_metrics_using_metadata(dd_run_check, aggregator, statestore_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [statestore_instance])
    dd_run_check(check)
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


@pytest.mark.unit
@pytest.mark.filename("statestored-metrics.txt")
def test_statestore_mock_assert_service_check(dd_run_check, aggregator, statestore_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [statestore_instance])
    dd_run_check(check)
    aggregator.assert_service_check("impala.statestore.openmetrics.health", status=ImpalaCheck.OK)


@pytest.mark.unit
@pytest.mark.filename("statestored-metrics.txt")
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


@pytest.mark.unit
@pytest.mark.filename("catalogd-metrics.txt")
def test_catalog_mock_assert_metrics_using_metadata(dd_run_check, aggregator, catalog_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [catalog_instance])
    dd_run_check(check)
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


@pytest.mark.unit
@pytest.mark.filename("catalogd-metrics.txt")
def test_catalog_mock_assert_service_check(dd_run_check, aggregator, catalog_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [catalog_instance])
    dd_run_check(check)
    aggregator.assert_service_check("impala.catalog.openmetrics.health", status=ImpalaCheck.OK)


@pytest.mark.unit
@pytest.mark.filename("catalogd-metrics.txt")
def test_catalog_mock_assert_metrics(dd_run_check, aggregator, catalog_instance, mock_metrics):
    check = ImpalaCheck("impala", {}, [catalog_instance])
    dd_run_check(check)

    expected_metrics = [
        {
            "name": "impala.catalog.jvm.gc.count",
            "value": 9.0,
            "type": aggregator.MONOTONIC_COUNT,
        },
    ]

    for expected_metric in expected_metrics:
        aggregator.assert_metric(
            name=expected_metric["name"],
            value=expected_metric["value"],
            metric_type=expected_metric.get("type", aggregator.GAUGE),
            tags=expected_metric.get("tags", ["endpoint:http://localhost:25020/metrics_prometheus"]),
        )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_no_duplicate_all()
