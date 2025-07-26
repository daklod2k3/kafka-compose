ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_replication_slots = 10;
ALTER SYSTEM SET max_wal_senders = 10;

CREATE ROLE debezium WITH LOGIN PASSWORD 'dbz';
ALTER ROLE debezium WITH REPLICATION;
GRANT CONNECT ON DATABASE source TO debezium;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO debezium;