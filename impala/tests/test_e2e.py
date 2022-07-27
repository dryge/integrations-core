# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.impala import ImpalaCheck


@pytest.mark.e2e
def test_check_e2e_assert_metrics(dd_agent_check, instance):
    aggregator = dd_agent_check(instance, rate=True)

    expected_metrics = [
        {
            "name": "impala.jvm.gc.count",
            "type": aggregator.COUNT,
        },
    ]

    for expected_metric in expected_metrics:
        aggregator.assert_metric(
            name=expected_metric["name"],
            metric_type=expected_metric.get("type", aggregator.GAUGE),
            tags=expected_metric.get("tags", ["endpoint:http://localhost:25000/metrics_prometheus"]),
        )

    aggregator.assert_all_metrics_covered()


@pytest.mark.e2e
def test_check_e2e_assert_service_check(dd_agent_check, instance):
    aggregator = dd_agent_check(instance, rate=True)
    aggregator.assert_service_check("impala.openmetrics.health", status=ImpalaCheck.OK)


@pytest.mark.e2e
def test_check_e2e_assert_metrics_using_metadata(dd_agent_check, instance):
    aggregator = dd_agent_check(instance, rate=True)
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())
