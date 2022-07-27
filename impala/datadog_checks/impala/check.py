# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.impala.config_models import ConfigMixin
from datadog_checks.impala.metrics_daemon import METRIC_MAP


class ImpalaCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = 'impala'

    def get_default_config(self):
        return {
            "metrics": [METRIC_MAP],
        }
