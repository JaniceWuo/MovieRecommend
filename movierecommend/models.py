# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class ColumnsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    column_name = models.CharField(db_column='Column_name', max_length=64)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'columns_priv'
        unique_together = (('host', 'db', 'user', 'table_name', 'column_name'),)


class Db(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db'
        unique_together = (('host', 'db', 'user'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EngineCost(models.Model):
    engine_name = models.CharField(max_length=64)
    device_type = models.IntegerField()
    cost_name = models.CharField(primary_key=True, max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engine_cost'
        unique_together = (('cost_name', 'engine_name', 'device_type'),)


class Event(models.Model):
    db = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    body = models.TextField()
    definer = models.CharField(max_length=93)
    execute_at = models.DateTimeField(blank=True, null=True)
    interval_value = models.IntegerField(blank=True, null=True)
    interval_field = models.CharField(max_length=18, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_executed = models.DateTimeField(blank=True, null=True)
    starts = models.DateTimeField(blank=True, null=True)
    ends = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18)
    on_completion = models.CharField(max_length=8)
    sql_mode = models.CharField(max_length=478)
    comment = models.CharField(max_length=64)
    originator = models.IntegerField()
    time_zone = models.CharField(max_length=64)
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'
        unique_together = (('db', 'name'),)


class Func(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    ret = models.IntegerField()
    dl = models.CharField(max_length=128)
    type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'func'


class GeneralLog(models.Model):
    event_time = models.DateTimeField()
    user_host = models.TextField()
    thread_id = models.BigIntegerField()
    server_id = models.IntegerField()
    command_type = models.CharField(max_length=64)
    argument = models.TextField()

    class Meta:
        managed = False
        db_table = 'general_log'


class GtidExecuted(models.Model):
    source_uuid = models.CharField(primary_key=True, max_length=36)
    interval_start = models.BigIntegerField()
    interval_end = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'gtid_executed'
        unique_together = (('source_uuid', 'interval_start'),)


class HelpCategory(models.Model):
    help_category_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    parent_category_id = models.SmallIntegerField(blank=True, null=True)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_category'


class HelpKeyword(models.Model):
    help_keyword_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'help_keyword'


class HelpRelation(models.Model):
    help_topic_id = models.IntegerField()
    help_keyword_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'help_relation'
        unique_together = (('help_keyword_id', 'help_topic_id'),)


class HelpTopic(models.Model):
    help_topic_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    help_category_id = models.SmallIntegerField()
    description = models.TextField()
    example = models.TextField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'help_topic'


class InnodbIndexStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    index_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    stat_name = models.CharField(max_length=64)
    stat_value = models.BigIntegerField()
    sample_size = models.BigIntegerField(blank=True, null=True)
    stat_description = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'innodb_index_stats'
        unique_together = (('database_name', 'table_name', 'index_name', 'stat_name'),)


class InnodbTableStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    n_rows = models.BigIntegerField()
    clustered_index_size = models.BigIntegerField()
    sum_of_other_index_sizes = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'innodb_table_stats'
        unique_together = (('database_name', 'table_name'),)


class NdbBinlogIndex(models.Model):
    position = models.BigIntegerField(db_column='Position')  # Field name made lowercase.
    file = models.CharField(db_column='File', max_length=255)  # Field name made lowercase.
    epoch = models.BigIntegerField(primary_key=True)
    inserts = models.IntegerField()
    updates = models.IntegerField()
    deletes = models.IntegerField()
    schemaops = models.IntegerField()
    orig_server_id = models.IntegerField()
    orig_epoch = models.BigIntegerField()
    gci = models.IntegerField()
    next_position = models.BigIntegerField()
    next_file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ndb_binlog_index'
        unique_together = (('epoch', 'orig_server_id', 'orig_epoch'),)


class Plugin(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    dl = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'plugin'


class Proc(models.Model):
    db = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=9)
    specific_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)
    sql_data_access = models.CharField(max_length=17)
    is_deterministic = models.CharField(max_length=3)
    security_type = models.CharField(max_length=7)
    param_list = models.TextField()
    returns = models.TextField()
    body = models.TextField()
    definer = models.CharField(max_length=93)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    sql_mode = models.CharField(max_length=478)
    comment = models.TextField()
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proc'
        unique_together = (('db', 'name', 'type'),)


class ProcsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    routine_name = models.CharField(db_column='Routine_name', max_length=64)  # Field name made lowercase.
    routine_type = models.CharField(db_column='Routine_type', max_length=9)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    proc_priv = models.CharField(db_column='Proc_priv', max_length=27)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procs_priv'
        unique_together = (('host', 'db', 'user', 'routine_name', 'routine_type'),)


class ProxiesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    proxied_host = models.CharField(db_column='Proxied_host', max_length=60)  # Field name made lowercase.
    proxied_user = models.CharField(db_column='Proxied_user', max_length=32)  # Field name made lowercase.
    with_grant = models.IntegerField(db_column='With_grant')  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proxies_priv'
        unique_together = (('host', 'user', 'proxied_host', 'proxied_user'),)


class Ratings(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    movieid = models.AutoField(db_column='movieId', primary_key=True)  # Field name made lowercase.
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'ratings'


class Result(models.Model):
    movieid = models.AutoField(db_column='movieId', primary_key=True)  # Field name made lowercase.
    imdbid = models.IntegerField(db_column='imdbId')  # Field name made lowercase.
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'result'


class Resulttable(models.Model):
    movieid = models.IntegerField(db_column='movieId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    imdbid = models.IntegerField(db_column='imdbId')  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resulttable'

    def __str__(self):
        return self.userid+':'+self.rating


class Rtotaltable(models.Model):
    movieid = models.IntegerField(db_column='movieId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    imdbid = models.IntegerField(db_column='imdbId')  # Field name made lowercase.
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rtotaltable'


class ServerCost(models.Model):
    cost_name = models.CharField(primary_key=True, max_length=64)
    cost_value = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField()
    comment = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_cost'


class Servers(models.Model):
    server_name = models.CharField(db_column='Server_name', primary_key=True, max_length=64)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=64)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=64)  # Field name made lowercase.
    wrapper = models.CharField(db_column='Wrapper', max_length=64)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servers'


class SlaveMasterInfo(models.Model):
    number_of_lines = models.IntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=64, blank=True, null=True)  # Field name made lowercase.
    user_name = models.TextField(db_column='User_name', blank=True, null=True)  # Field name made lowercase.
    user_password = models.TextField(db_column='User_password', blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    connect_retry = models.IntegerField(db_column='Connect_retry')  # Field name made lowercase.
    enabled_ssl = models.IntegerField(db_column='Enabled_ssl')  # Field name made lowercase.
    ssl_ca = models.TextField(db_column='Ssl_ca', blank=True, null=True)  # Field name made lowercase.
    ssl_capath = models.TextField(db_column='Ssl_capath', blank=True, null=True)  # Field name made lowercase.
    ssl_cert = models.TextField(db_column='Ssl_cert', blank=True, null=True)  # Field name made lowercase.
    ssl_cipher = models.TextField(db_column='Ssl_cipher', blank=True, null=True)  # Field name made lowercase.
    ssl_key = models.TextField(db_column='Ssl_key', blank=True, null=True)  # Field name made lowercase.
    ssl_verify_server_cert = models.IntegerField(db_column='Ssl_verify_server_cert')  # Field name made lowercase.
    heartbeat = models.FloatField(db_column='Heartbeat')  # Field name made lowercase.
    bind = models.TextField(db_column='Bind', blank=True, null=True)  # Field name made lowercase.
    ignored_server_ids = models.TextField(db_column='Ignored_server_ids', blank=True, null=True)  # Field name made lowercase.
    uuid = models.TextField(db_column='Uuid', blank=True, null=True)  # Field name made lowercase.
    retry_count = models.BigIntegerField(db_column='Retry_count')  # Field name made lowercase.
    ssl_crl = models.TextField(db_column='Ssl_crl', blank=True, null=True)  # Field name made lowercase.
    ssl_crlpath = models.TextField(db_column='Ssl_crlpath', blank=True, null=True)  # Field name made lowercase.
    enabled_auto_position = models.IntegerField(db_column='Enabled_auto_position')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.
    tls_version = models.TextField(db_column='Tls_version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_master_info'


class SlaveRelayLogInfo(models.Model):
    number_of_lines = models.IntegerField(db_column='Number_of_lines')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name')  # Field name made lowercase.
    relay_log_pos = models.BigIntegerField(db_column='Relay_log_pos')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    sql_delay = models.IntegerField(db_column='Sql_delay')  # Field name made lowercase.
    number_of_workers = models.IntegerField(db_column='Number_of_workers')  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_relay_log_info'


class SlaveWorkerInfo(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    relay_log_name = models.TextField(db_column='Relay_log_name')  # Field name made lowercase.
    relay_log_pos = models.BigIntegerField(db_column='Relay_log_pos')  # Field name made lowercase.
    master_log_name = models.TextField(db_column='Master_log_name')  # Field name made lowercase.
    master_log_pos = models.BigIntegerField(db_column='Master_log_pos')  # Field name made lowercase.
    checkpoint_relay_log_name = models.TextField(db_column='Checkpoint_relay_log_name')  # Field name made lowercase.
    checkpoint_relay_log_pos = models.BigIntegerField(db_column='Checkpoint_relay_log_pos')  # Field name made lowercase.
    checkpoint_master_log_name = models.TextField(db_column='Checkpoint_master_log_name')  # Field name made lowercase.
    checkpoint_master_log_pos = models.BigIntegerField(db_column='Checkpoint_master_log_pos')  # Field name made lowercase.
    checkpoint_seqno = models.IntegerField(db_column='Checkpoint_seqno')  # Field name made lowercase.
    checkpoint_group_size = models.IntegerField(db_column='Checkpoint_group_size')  # Field name made lowercase.
    checkpoint_group_bitmap = models.TextField(db_column='Checkpoint_group_bitmap')  # Field name made lowercase.
    channel_name = models.CharField(db_column='Channel_name', primary_key=True, max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slave_worker_info'
        unique_together = (('channel_name', 'id'),)


class SlowLog(models.Model):
    start_time = models.DateTimeField()
    user_host = models.TextField()
    query_time = models.TimeField()
    lock_time = models.TimeField()
    rows_sent = models.IntegerField()
    rows_examined = models.IntegerField()
    db = models.CharField(max_length=512)
    last_insert_id = models.IntegerField()
    insert_id = models.IntegerField()
    server_id = models.IntegerField()
    sql_text = models.TextField()
    thread_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'slow_log'


class TablesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=93)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    table_priv = models.CharField(db_column='Table_priv', max_length=98)  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tables_priv'
        unique_together = (('host', 'db', 'user', 'table_name'),)


class TimeZone(models.Model):
    time_zone_id = models.AutoField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    use_leap_seconds = models.CharField(db_column='Use_leap_seconds', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone'


class TimeZoneLeapSecond(models.Model):
    transition_time = models.BigIntegerField(db_column='Transition_time', primary_key=True)  # Field name made lowercase.
    correction = models.IntegerField(db_column='Correction')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_leap_second'


class TimeZoneName(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=64)  # Field name made lowercase.
    time_zone_id = models.IntegerField(db_column='Time_zone_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_name'


class TimeZoneTransition(models.Model):
    time_zone_id = models.IntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_time = models.BigIntegerField(db_column='Transition_time')  # Field name made lowercase.
    transition_type_id = models.IntegerField(db_column='Transition_type_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition'
        unique_together = (('time_zone_id', 'transition_time'),)


class TimeZoneTransitionType(models.Model):
    time_zone_id = models.IntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_type_id = models.IntegerField(db_column='Transition_type_id')  # Field name made lowercase.
    offset = models.IntegerField(db_column='Offset')  # Field name made lowercase.
    is_dst = models.IntegerField(db_column='Is_DST')  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_zone_transition_type'
        unique_together = (('time_zone_id', 'transition_type_id'),)


class User(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=32)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    reload_priv = models.CharField(db_column='Reload_priv', max_length=1)  # Field name made lowercase.
    shutdown_priv = models.CharField(db_column='Shutdown_priv', max_length=1)  # Field name made lowercase.
    process_priv = models.CharField(db_column='Process_priv', max_length=1)  # Field name made lowercase.
    file_priv = models.CharField(db_column='File_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    show_db_priv = models.CharField(db_column='Show_db_priv', max_length=1)  # Field name made lowercase.
    super_priv = models.CharField(db_column='Super_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    repl_slave_priv = models.CharField(db_column='Repl_slave_priv', max_length=1)  # Field name made lowercase.
    repl_client_priv = models.CharField(db_column='Repl_client_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    create_user_priv = models.CharField(db_column='Create_user_priv', max_length=1)  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.
    create_tablespace_priv = models.CharField(db_column='Create_tablespace_priv', max_length=1)  # Field name made lowercase.
    ssl_type = models.CharField(max_length=9)
    ssl_cipher = models.TextField()
    x509_issuer = models.TextField()
    x509_subject = models.TextField()
    max_questions = models.IntegerField()
    max_updates = models.IntegerField()
    max_connections = models.IntegerField()
    max_user_connections = models.IntegerField()
    plugin = models.CharField(max_length=64)
    authentication_string = models.TextField(blank=True, null=True)
    password_expired = models.CharField(max_length=1)
    password_last_changed = models.DateTimeField(blank=True, null=True)
    password_lifetime = models.SmallIntegerField(blank=True, null=True)
    account_locked = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('host', 'user'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    nickname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
