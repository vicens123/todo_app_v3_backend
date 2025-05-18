"""create todos table

Revision ID: 62ec693f8f66
Revises: 
Create Date: 2025-05-05 22:59:56.920116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62ec693f8f66'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    CREATE TABLE todos (
        id BIGSERIAL PRIMARY KEY,
        name TEXT,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    )
    """)

def downgrade():
    op.execute("DROP TABLE todos;")

