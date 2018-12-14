-- Load CSV file into Postgresql

COPY <table_name> FROM '<file.csv>' DELIMITERS ';' csv;
