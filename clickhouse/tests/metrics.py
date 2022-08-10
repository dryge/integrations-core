# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This is not actually every metric, but rather the metrics that are
# immediately available upon the start up of our environment. Some
# metrics take a while to show up and others we cannot trigger.
# Additionally, these are metrics that are present across all versions
# we support (v18-v22).
BASE_METRICS = [
    'clickhouse.background_pool.schedule.task.active',
    'clickhouse.connection.http',
    'clickhouse.connection.interserver',
    'clickhouse.connection.send.external',
    'clickhouse.connection.tcp',
    'clickhouse.dictionary.item.current',
    'clickhouse.dictionary.load',
    'clickhouse.dictionary.memory.used',
    'clickhouse.dictionary.request.cache',
    'clickhouse.file.open.read',
    'clickhouse.file.open.total',
    'clickhouse.file.open.write',
    'clickhouse.file.read.size.total',
    'clickhouse.file.read.total',
    'clickhouse.file.write.size.total',
    'clickhouse.file.write.total',
    'clickhouse.lock.context.acquisition.total',
    'clickhouse.merge.active',
    'clickhouse.merge.disk.reserved',
    'clickhouse.query.active',
    'clickhouse.query.insert.delayed',
    'clickhouse.query.memory',
    'clickhouse.query.mutation',
    'clickhouse.query.select.total',
    'clickhouse.query.total',
    'clickhouse.query.waiting',
    'clickhouse.syscall.read',
    'clickhouse.syscall.write',
    'clickhouse.table.buffer.row',
    'clickhouse.table.buffer.size',
    'clickhouse.table.distributed.connection.inserted',
    'clickhouse.table.mergetree.part.current',
    'clickhouse.table.mergetree.row.current',
    'clickhouse.table.mergetree.size',
    'clickhouse.table.replicated.active',
    'clickhouse.table.replicated.log.max',
    'clickhouse.table.replicated.log.pointer',
    'clickhouse.table.replicated.part.check',
    'clickhouse.table.replicated.part.fetch',
    'clickhouse.table.replicated.part.future',
    'clickhouse.table.replicated.part.send',
    'clickhouse.table.replicated.part.suspect',
    'clickhouse.table.replicated.queue.insert',
    'clickhouse.table.replicated.queue.merge',
    'clickhouse.table.replicated.queue.size',
    'clickhouse.table.replicated.readonly',
    'clickhouse.table.replicated.total',
    'clickhouse.table.replicated.version',
    'clickhouse.thread.lock.context.waiting',
    'clickhouse.thread.lock.rw.active.read',
    'clickhouse.thread.lock.rw.active.write',
    'clickhouse.thread.lock.rw.waiting.read',
    'clickhouse.thread.lock.rw.waiting.write',
    'clickhouse.thread.query',
    'clickhouse.zk.connection',
    'clickhouse.zk.node.ephemeral',
    'clickhouse.zk.request',
    'clickhouse.zk.watch',
]

# These are the metrics that are not always available
OPTIONAL_METRICS = [
    'clickhouse.background_pool.buffer_flush_schedule.task.active',
    'clickhouse.background_pool.distributed.task.active',
    'clickhouse.background_pool.fetches.task.active',
    'clickhouse.background_pool.message_broker.task.active',
    'clickhouse.background_pool.move.task.active',
    'clickhouse.cache_dictionary.update_queue.batches',
    'clickhouse.cache_dictionary.update_queue.keys',
    'clickhouse.CompiledExpressionCacheCount',
    'clickhouse.connection.http.create.count',
    'clickhouse.connection.http.create.total',
    'clickhouse.connection.mysql',
    'clickhouse.connection.send.scalar',
    'clickhouse.cpu.time',
    'clickhouse.database.total',
    'clickhouse.ddl.max_processed',
    'clickhouse.disk.write.size.count',
    'clickhouse.disk.write.size.total',
    'clickhouse.drained_connections.async',
    'clickhouse.drained_connections.async.active',
    'clickhouse.drained_connections.sync',
    'clickhouse.drained_connections.sync.active',
    'clickhouse.file.open.count',
    'clickhouse.file.read.count',
    'clickhouse.file.read.size.count',
    'clickhouse.file.seek.count',
    'clickhouse.file.seek.total',
    'clickhouse.file.write.count',
    'clickhouse.file.write.size.count',
    'clickhouse.fs.read.size.count',
    'clickhouse.fs.read.size.total',
    'clickhouse.fs.write.size.count',
    'clickhouse.fs.write.size.total',
    'clickhouse.jemalloc.active',
    'clickhouse.jemalloc.allocated',
    'clickhouse.jemalloc.background_thread.run_interval',
    'clickhouse.jemalloc.background_thread.num_runs',
    'clickhouse.jemalloc.background_thread.num_threads',
    'clickhouse.jemalloc.mapped',
    'clickhouse.jemalloc.metadata',
    'clickhouse.jemalloc.metadata_thp',
    'clickhouse.jemalloc.resident',
    'clickhouse.jemalloc.retained',
    'clickhouse.lock.context.acquisition.count',
    'clickhouse.merge.count',
    'clickhouse.merge.read.size.uncompressed.count',
    'clickhouse.merge.read.size.uncompressed.total',
    'clickhouse.merge.row.read.count',
    'clickhouse.merge.row.read.total',
    'clickhouse.merge.time',
    'clickhouse.merge.total',
    'clickhouse.mmapped.file.current',
    'clickhouse.mmapped.file.size',
    'clickhouse.MarkCacheFiles',
    'clickhouse.network.receive.elapsed.time',
    'clickhouse.network.receive.size.count',
    'clickhouse.network.receive.size.total',
    'clickhouse.network.send.elapsed.time',
    'clickhouse.network.send.size.count',
    'clickhouse.network.send.size.total',
    'clickhouse.network.threads.receive',
    'clickhouse.network.threads.send',
    'clickhouse.part.max',
    'clickhouse.parts.committed',
    'clickhouse.parts.compact',
    'clickhouse.parts.delete_on_destroy',
    'clickhouse.parts.deleting',
    'clickhouse.parts.inmemory',
    'clickhouse.parts.outdated',
    'clickhouse.parts.precommitted',
    'clickhouse.parts.temporary',
    'clickhouse.parts.wide',
    'clickhouse.postgresql.connection',
    'clickhouse.query.count',
    'clickhouse.query.select.count',
    'clickhouse.query.select.time',
    'clickhouse.query.time',
    'clickhouse.read.compressed.block.count',
    'clickhouse.read.compressed.block.total',
    'clickhouse.read.compressed.raw.size.count',
    'clickhouse.read.compressed.raw.size.total',
    'clickhouse.read.compressed.size.count',
    'clickhouse.read.compressed.size.total',
    'clickhouse.replica.delay.absolute',
    'clickhouse.replica.delay.relative',
    'clickhouse.replica.queue.size',
    'clickhouse.ReplicasMaxInsertsInQueue',
    'clickhouse.ReplicasMaxMergesInQueue',
    'clickhouse.ReplicasMaxQueueSize',
    'clickhouse.ReplicasSumInsertsInQueue',
    'clickhouse.ReplicasSumMergesInQueue',
    'clickhouse.selected.bytes.count',
    'clickhouse.selected.bytes.total',
    'clickhouse.selected.rows.count',
    'clickhouse.selected.rows.total',
    'clickhouse.syscall.read.wait',
    'clickhouse.syscall.write.wait',
    'clickhouse.table.distributed.file.insert.broken',
    'clickhouse.table.distributed.file.insert.pending',
    'clickhouse.table.insert.row.count',
    'clickhouse.table.insert.row.total',
    'clickhouse.table.insert.size.count',
    'clickhouse.table.insert.size.total',
    'clickhouse.table.mergetree.insert.block.already_sorted.count',
    'clickhouse.table.mergetree.insert.block.already_sorted.total',
    'clickhouse.table.mergetree.insert.block.count',
    'clickhouse.table.mergetree.insert.block.total',
    'clickhouse.table.mergetree.insert.row.count',
    'clickhouse.table.mergetree.insert.row.total',
    'clickhouse.table.mergetree.insert.write.size.compressed.count',
    'clickhouse.table.mergetree.insert.write.size.compressed.total',
    'clickhouse.table.mergetree.insert.write.size.uncompressed.count',
    'clickhouse.table.mergetree.insert.write.size.uncompressed.total',
    'clickhouse.table.mergetree.replicated.fetch.replica.count',
    'clickhouse.table.mergetree.replicated.fetch.replica.total',
    'clickhouse.table.mergetree.replicated.leader.elected.count',
    'clickhouse.table.mergetree.replicated.leader.elected.total',
    'clickhouse.table.mergetree.storage.mark.cache',
    'clickhouse.table.total',
    'clickhouse.tables_to_drop.queue.total',
    'clickhouse.thread.cpu.wait',
    'clickhouse.thread.global.active',
    'clickhouse.thread.global.total',
    'clickhouse.thread.local.active',
    'clickhouse.thread.local.total',
    'clickhouse.thread.process_time',
    'clickhouse.thread.system.process_time',
    'clickhouse.thread.user.process_time',
    'clickhouse.UncompressedCacheBytes',
    'clickhouse.UncompressedCacheCells',
    'clickhouse.uptime',
]

V_18_19_METRICS = [
    'clickhouse.background_pool.processing.task.active',
    'clickhouse.background_pool.processing.memory',
    'clickhouse.background_pool.schedule.memory',
    'clickhouse.merge.memory',
    'clickhouse.replica.leader.election',
    'clickhouse.table.replicated.leader',
]

V_20_METRICS = [
    'clickhouse.background_pool.processing.task.active',
    'clickhouse.background_pool.buffer_flush_schedule.task.active',
    'clickhouse.background_pool.distributed.task.active',
    'clickhouse.background_pool.fetches.task.active',
    'clickhouse.background_pool.message_broker.task.active',
    'clickhouse.postgresql.connection',
    'clickhouse.tables_to_drop.queue.total',
    'clickhouse.query.time',
    'clickhouse.query.select.time',
    'clickhouse.selected.rows.total',
    'clickhouse.selected.bytes.total',
]

V_21_METRICS = [
    'clickhouse.background_pool.processing.task.active',
    'clickhouse.ddl.max_processed',
    'clickhouse.parts.committed',
    'clickhouse.parts.compact',
    'clickhouse.parts.delete_on_destroy',
    'clickhouse.parts.deleting',
    'clickhouse.parts.inmemory',
    'clickhouse.parts.outdated',
    'clickhouse.parts.precommitted',
    'clickhouse.parts.temporary',
]

V_22_METRICS = [
    'clickhouse.parts.pre_active',
    'clickhouse.parts.active',
]

version_mapper = {
    '18': V_18_19_METRICS,
    '19': V_18_19_METRICS,
    '20': V_20_METRICS,
    '21': V_21_METRICS,
    '22': V_22_METRICS,
}


def get_metrics(version):
    return BASE_METRICS + version_mapper.get(version.split(".")[0], [])
