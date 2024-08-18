
# from __future__ import with_statement
# from logging.config import fileConfig
# from sqlalchemy import engine_from_config, pool
# from alembic import context
# import os
# import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app.database import Base
# from app import models

# config = context.config
# fileConfig(config.config_file_name)
# target_metadata = Base.metadata

# def run_migrations_offline():
#     context.configure(
#         url=config.get_main_option("sqlalchemy.url"),
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()

# def run_migrations_online():
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(connection=connection, target_metadata=target_metadata)

#         with context.begin_transaction():
#             context.run_migrations()

# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()

from __future__ import with_statement
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import Base, engine  # Import engine if you want to use it directly
from app import models  # Import models to register them with SQLAlchemy

# Get the alembic configuration object
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set the target metadata to your SQLAlchemy Base
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


from app.database import engine  # Make sure this is the correct import path

def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# def run_migrations_online():
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#     """
#     # Optionally, use the engine directly from your app (better for avoiding duplicates)
#     connectable = engine

#     # If not using the engine from your app, use the one from config
#     # connectable = engine_from_config(
#     #     config.get_section(config.config_ini_section),
#     #     prefix="sqlalchemy.",
#     #     poolclass=pool.NullPool,
#     # )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata,
#             compare_type=True,  # Compare column types and reflect changes in migrations
#         )

#         with context.begin_transaction():
#             context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
