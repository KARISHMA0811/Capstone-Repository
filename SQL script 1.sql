-- This is auto-generated code
SELECT
    TOP 100 *
FROM
    OPENROWSET(
        BULK 'https://capstonestoreacccount123.dfs.core.windows.net/capstonecontainer/projectdata.csv/**',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
       HEADER_ROW= TRUE
    ) AS [result]
