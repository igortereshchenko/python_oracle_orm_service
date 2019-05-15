SELECT
    col.column_id,
    col.owner AS schema_name,
    col.table_name,
    col.column_name,
    col.data_type,
    col.data_length,
    col.data_precision,
    col.data_scale,
    col.nullable
FROM
    sys.all_tab_columns col
    INNER JOIN sys.all_tables t
    ON col.owner = t.owner AND col.table_name = t.table_name
WHERE
    col.owner = 'DEVELOPER'
    AND col.table_name = 'ORDERS'
ORDER BY
    col.column_id;


SELECT
    *
FROM
    sys.all_tab_columns;

SELECT
    *
FROM
    sys.all_tables;