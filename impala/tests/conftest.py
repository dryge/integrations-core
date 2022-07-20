# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev import docker_run, load_jmx_config
from datadog_checks.dev.conditions import CheckDockerLogs

from .common import HERE


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(HERE, 'compose', 'docker-compose.yaml')
    with docker_run(
        compose_file,
        conditions=[
            CheckDockerLogs(
                identifier=compose_file,
                patterns="Connected to metastore.",
                matches='all',
                wait=5,
                attempts=20,
            )
        ],
    ):
        config = load_jmx_config()
        config['instances'] = []
        yield config, {'use_jmx': True}
