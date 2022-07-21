# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os
from unittest import mock

import pytest

from datadog_checks.dev import docker_run, get_docker_hostname, get_here
from datadog_checks.dev.conditions import CheckDockerLogs
from datadog_checks.impala import ImpalaCheck


@pytest.fixture(scope="session")
def dd_environment():
    url = f"http://{get_docker_hostname()}:25000/metrics_prometheus"
    instance = {"openmetrics_endpoint": url}

    compose_file = os.path.join(get_here(), "compose", "docker-compose.yaml")
    with docker_run(
        compose_file=compose_file,
        conditions=[
            CheckDockerLogs(
                identifier=compose_file,
                patterns=[
                    "Connected to metastore.",
                    "Impala has started.",
                    "CatalogService started",
                ],
                matches='all',
                wait=5,
                attempts=20,
            )
        ],
        endpoints=[url],
    ):
        yield instance


@pytest.fixture
def instance():
    return {
        "openmetrics_endpoint": f"http://{get_docker_hostname()}:25000/metrics_prometheus",
    }


@pytest.fixture
def check(instance):
    return ImpalaCheck("impala", {}, [instance])


@pytest.fixture()
def mock_metrics(fixture_filename="impalad-metrics.txt"):
    with open(os.path.join(os.path.dirname(__file__), "fixtures", fixture_filename), "r") as fixture_file:
        content = fixture_file.read()

    with mock.patch(
        "requests.get",
        return_value=mock.MagicMock(
            status_code=200,
            iter_lines=lambda **kwargs: content.split("\n"),
            headers={"Content-Type": "text/plain"},
        ),
    ):
        yield
