# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.impala.config_models import ConfigMixin
from datadog_checks.impala.metrics import CATALOG_METRIC_MAP, DAEMON_METRIC_MAP, STATESTORE_METRIC_MAP


class ImpalaCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = 'impala'

    def get_default_config(self):
        if self.instance["service_type"] == "daemon":
            return {
                "metrics": [DAEMON_METRIC_MAP],
            }

        if self.instance["service_type"] == "statestore":
            return {
                "metrics": [STATESTORE_METRIC_MAP],
            }

        if self.instance["service_type"] == "catalog":
            return {
                "metrics": [CATALOG_METRIC_MAP],
            }

        return {}
