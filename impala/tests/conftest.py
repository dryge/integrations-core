# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os
from unittest import mock

import pytest

from datadog_checks.dev import docker_run, get_docker_hostname, get_here
from datadog_checks.dev.conditions import CheckDockerLogs


@pytest.fixture(scope="session")
def dd_environment(request):
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
        endpoints=[
            f"http://{get_docker_hostname()}:25000/metrics_prometheus",
            f"http://{get_docker_hostname()}:25010/metrics_prometheus",
            f"http://{get_docker_hostname()}:25020/metrics_prometheus",
        ],
    ):
        yield {
            "openmetrics_endpoint": f"http://{get_docker_hostname()}:25000/metrics_prometheus",
            "service_type": "daemon",
        }


@pytest.fixture
def daemon_instance():
    return {
        "openmetrics_endpoint": f"http://{get_docker_hostname()}:25000/metrics_prometheus",
        "service_type": "daemon",
    }


@pytest.fixture
def statestore_instance():
    return {
        "openmetrics_endpoint": f"http://{get_docker_hostname()}:25010/metrics_prometheus",
        "service_type": "statestore",
    }


@pytest.fixture
def catalog_instance():
    return {
        "openmetrics_endpoint": f"http://{get_docker_hostname()}:25020/metrics_prometheus",
        "service_type": "catalog",
    }


@pytest.fixture()
def mock_metrics(request):
    filename = request.node.get_closest_marker("filename")
    with open(os.path.join(os.path.dirname(__file__), "fixtures", filename.args[0]), "r") as fixture_file:
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
