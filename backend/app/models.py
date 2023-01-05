import sqlalchemy
import databases

metadata = sqlalchemy.MetaData()

users_scheme = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("login", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("is_root", sqlalchemy.Boolean),
    sqlalchemy.Column("email", sqlalchemy.String),
)

project_scheme = sqlalchemy.Table(
	"projects",
	metadata,
	sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
	sqlalchemy.Column("manager_id", sqlalchemy.INTEGER),
	sqlalchemy.Column("name", sqlalchemy.String),
	sqlalchemy.Column("description", sqlalchemy.String),
	sqlalchemy.Column("is_archive", sqlalchemy.Boolean),
	sqlalchemy.Column("creation_data", sqlalchemy.DateTime),
)

tasks_scheme = sqlalchemy.Table(
	"tasks",
	metadata,
    sqlalchemy.Column("project_id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("task_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("author_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("asignee_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("status_name", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
)

project_users_scheme = sqlalchemy.Table(
	"project_users",
	metadata,
    sqlalchemy.Column("user_id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("project_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("role_name", sqlalchemy.String),
)

attachments_scheme = sqlalchemy.Table(
	"attachments",
	metadata,
    sqlalchemy.Column("project_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("task_id", sqlalchemy.INTEGER),
    sqlalchemy.Column("file_path", sqlalchemy.String),
    sqlalchemy.Column("attachment_date", sqlalchemy.DateTime),
)
