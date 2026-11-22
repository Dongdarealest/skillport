# Field notes

- Dates: normalize to ISO format (YYYY-MM-DD) only when the source format is unambiguous.
- Numbers: strip thousand separators and currency symbols only in columns that are numeric everywhere else.
- Names and addresses: trim whitespace only. Never change spelling or casing.
- Empty strings and the text "null" are not the same thing. Keep both as they are and flag the column.
