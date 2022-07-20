# Agent Check: Impala

## Overview

This check monitors [Impala][1].

## Setup

### Installation

The Impala check is included in the [Datadog Agent][2] package.
No additional installation is needed on your server.

### Configuration

1. Edit the `impala.d/conf.yaml` file, in the `conf.d/` folder at the root of your
   Agent's configuration directory to start collecting your impala performance data.
   See the [sample impala.d/conf.yaml][3] for all available configuration options.

   This check has a limit of 350 metrics per instance. The number of returned metrics is indicated when running the Datadog Agent [status command][4].
   You can specify the metrics you are interested in by editing the [configuration][3].
   To learn how to customize the metrics to collect visit the [JMX Checks documentation][5] for more detailed instructions.
   If you need to monitor more metrics, contact [Datadog support][6].

2. [Restart the Agent][7]

### Validation

[Run the Agent's `status` subcommand][4] and look for `impala` under the Checks section.

## Data Collected

### Metrics

Impala does not include any metrics.

### Events

The Impala integration does not include any events.

### Service Checks

The Impala integration does not include any service checks.

See [service_checks.json][8] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Datadog support][6].


[1]: **LINK_TO_INTEGERATION_SITE**
[2]: https://app.datadoghq.com/account/settings#agent
[3]: https://github.com/DataDog/integrations-core/blob/master/jmx/datadog_checks/jmx/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[5]: https://docs.datadoghq.com/integrations/java/
[6]: https://docs.datadoghq.com/help/
[7]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[8]: https://github.com/DataDog/integrations-core/blob/master/jmx/assets/service_checks.json
