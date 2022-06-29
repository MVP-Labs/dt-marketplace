# dt-marketplace

## Prerequisites

```shell
> git clone https://github.com/ownership-labs/dt-contracts
> git clone https://github.com/ownership-labs/DataToken
> git clone https://github.com/ownership-labs/Compute-to-Data
> git clone https://github.com/ownership-labs/dt-marketplace
```

## Quick Start

Prepare the datatoken environments and deploy a grid network with two on-premise data sandbox.

```shell
> cd dt-marketplace/examples
> ./scripts/init_datatoken_env.sh
> ./scripts/deploy_dsb_network.sh
```

The console will display leaf datatoken identifiers for three private datasets. You need to fill them in `./samples/ddo/3rd_algo_attr.json`.

```shell
> ./scripts/get_compose_perm.sh
```

The console will display the composable datatoken identifier for the 3rd algorithm. You need to fill it in `./scripts/run_remote_execution.sh`. Then 3rd-party can execute computation on two remote sandbox.

```shell
> ./scripts/run_remote_execution.sh
```

The console will display the `job_id`. You can see the algorithm running logs.

```shell
> cat ./workdir/job_`job_id`/outputs/test.log
```

```shell
2021-06-15 13:32:08,813 - INFO - ==================
2021-06-15 13:32:08,813 - INFO - DistributedCommunicator with rank 0
2021-06-15 13:32:08,813 - INFO - ==================
2021-06-15 13:32:28,695 - INFO - World size = 2
2021-06-15 13:32:28,963 - INFO - CrypTen Training
2021-06-15 13:32:29,096 - INFO - Epoch 0, Batch 0 --- Loss 0.6741, Accuracy 62.00
2021-06-15 13:32:29,189 - INFO - Epoch 0, Batch 1 --- Loss 0.6776, Accuracy 61.00
2021-06-15 13:32:29,277 - INFO - Epoch 0, Batch 2 --- Loss 0.6854, Accuracy 57.00
2021-06-15 13:32:29,359 - INFO - Epoch 0, Batch 3 --- Loss 0.6868, Accuracy 56.00
2021-06-15 13:32:29,443 - INFO - Epoch 0, Batch 4 --- Loss 0.6853, Accuracy 56.00
2021-06-15 13:32:29,550 - INFO - Epoch 0, Batch 5 --- Loss 0.6683, Accuracy 67.00
...
```

Alternatively, set up the tracer and marketplace UIs to browse the data assets.

```shell
> ./scripts/setup_platform_ui.sh
```
