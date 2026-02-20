from django.db.backends.mysql.base import DatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# 1. Bypass version check (MariaDB 10.6+ required, user has 10.4)
DatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Disable RETURNING clause (Not supported in MariaDB 10.4)
# This prevents: "You have an error in your SQL syntax ... near 'RETURNING'"
DatabaseFeatures.can_return_columns_from_insert = False
