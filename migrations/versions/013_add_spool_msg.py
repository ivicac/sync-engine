"""Add SpoolMessage table

Revision ID: f7dbd9bf4a6
Revises: 13102e0e6fbd
Create Date: 2014-04-16 03:51:49.484697

"""

# revision identifiers, used by Alembic.
revision = "f7dbd9bf4a6"
down_revision = "193802835c33"

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "message", sa.Column("inbox_uid", sa.String(length=64), nullable=True)
    )
    op.add_column("message", sa.Column("type", sa.String(length=16), nullable=True))

    op.create_table(
        "spoolmessage",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_date", sa.DateTime(), nullable=True),
        sa.Column(
            "is_sent",
            sa.Boolean,
            server_default=sa.sql.expression.false(),
            nullable=False,
        ),
        sa.Column("resolved_message_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["message.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["resolved_message_id"], ["message.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("message", "type")
    op.drop_column("message", "inbox_uid")

    op.drop_table("spoolmessage")
    ### end Alembic commands ###
