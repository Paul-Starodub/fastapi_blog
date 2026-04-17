"""add likes

Revision ID: 2d32adaf05d7
Revises: 476cf8a84a75
Create Date: 2026-04-03 22:53:17.237677

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2d32adaf05d7"
down_revision: Union[str, Sequence[str], None] = "476cf8a84a75"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("likes", sa.Integer(), server_default="0", nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "likes")
