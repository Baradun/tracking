--drop database jira;
--CREATE DATABASE jira;
--GRANT ALL PRIVILEGES ON DATABASE jira TO postgres;

CREATE TABLE "task_statuses"(
    "status_name" VARCHAR(50) NOT NULL
);
ALTER TABLE "task_statuses" ADD PRIMARY KEY("status_name");

CREATE TABLE "transitions"(
    "previous" VARCHAR(50) NOT NULL,
    "next" VARCHAR(50) NOT NULL
);
ALTER TABLE "transitions" ADD PRIMARY KEY("previous", "next");
ALTER TABLE "transitions" ADD CONSTRAINT "transitions_task_statuses_foreign" FOREIGN KEY("previous") REFERENCES "task_statuses"("status_name");
ALTER TABLE "transitions" ADD CONSTRAINT "transitions_task_statuses1_foreign" FOREIGN KEY("next") REFERENCES "task_statuses"("status_name");
  
CREATE TABLE "users"(
    "id" INTEGER NOT NULL,
    "login" VARCHAR(50) NOT NULL,
    "password" VARCHAR(50) NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "is_root" BOOLEAN NOT NULL,
    "email" VARCHAR(50) NOT NULL
);
ALTER TABLE "users" ADD PRIMARY KEY("id");
ALTER TABLE "users" ADD CONSTRAINT "users_login_unique" UNIQUE("login");

CREATE TABLE "projects"(
    "id" INTEGER NOT NULL,
    "manager_id" INTEGER NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "description" TEXT NOT NULL,
    "is_archive" BOOLEAN NOT NULL DEFAULT '0',
    "creation_date" DATE NOT NULL
);
ALTER TABLE  "projects" ADD PRIMARY KEY("id");
ALTER TABLE  "projects" ADD CONSTRAINT "projects_manager_id_foreign" FOREIGN KEY("manager_id") REFERENCES "users"("id");   

CREATE TABLE "tasks"(
    "project_id" INTEGER NOT NULL,
    "task_id" INTEGER NULL,
    "author_id" INTEGER NOT NULL,
    "asignee_id" INTEGER NOT NULL,
    "status_name" VARCHAR(50) NOT NULL,
    "name" VARCHAR(150) NOT NULL,
    "description" TEXT NOT NULL
);
ALTER TABLE "tasks" ADD PRIMARY KEY("project_id", "task_id");
ALTER TABLE "tasks" ADD CONSTRAINT "project_task_foreign" FOREIGN KEY("project_id") REFERENCES "projects"("id");
ALTER TABLE "tasks" ADD CONSTRAINT "status_name_task_foreign" FOREIGN KEY("status_name") REFERENCES "task_statuses"("status_name");
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_asignee_id_foreign" FOREIGN KEY("asignee_id") REFERENCES "users"("id");
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_author_id_foreign" FOREIGN KEY("author_id") REFERENCES "users"("id");

CREATE TABLE "user_roles"("role_name" VARCHAR(50) NOT NULL);
ALTER TABLE "user_roles" ADD PRIMARY KEY("role_name");

CREATE TABLE "project_users"(
    "user_id" INTEGER NOT NULL,
    "project_id" INTEGER NOT NULL,
    "role_name" VARCHAR(50) NOT NULL
);
ALTER TABLE "project_users" ADD PRIMARY KEY("user_id", "project_id", "role_name");
ALTER TABLE "project_users" ADD CONSTRAINT "project_users_users_foreign" FOREIGN KEY("user_id") REFERENCES "users"("id");
ALTER TABLE "project_users" ADD CONSTRAINT "project_users_projects_foreign" FOREIGN KEY("project_id") REFERENCES "projects"("id");
ALTER TABLE "project_users" ADD CONSTRAINT "project_users_project_users_foreign" FOREIGN KEY("role_name") REFERENCES "user_roles"("role_name");

CREATE TABLE "attachments"(
    "project_id" INTEGER NOT NULL,
    "task_id" INTEGER NOT NULL,
    "file_path" VARCHAR(50) NOT NULL,
    "attachment_date" DATE NOT NULL
);
ALTER TABLE "attachments" ADD PRIMARY KEY("project_id", "task_id", "file_path");
ALTER TABLE "attachments" ADD CONSTRAINT "attachments_tasks_foreign" FOREIGN KEY("project_id", "task_id") REFERENCES "tasks"("project_id", "task_id");

--- INITIAL DATA ZONE

INSERT INTO public.users (id, login, "password", "name", is_root, email) VALUES 
(0, 'root', 'root', 'admin', true, 'test@mail.ru');

INSERT INTO public.user_roles (role_name)
VALUES ('Администратор'),('Руководитель проекта'),('Тестировщик'),('Руководитель тестирования'),('Пользователь');

INSERT INTO public.task_statuses (status_name)
VALUES('Новая задача'),('Задача назначена'),('Задача в работе'),('Задача отклонена'),
('Ожидает тестирования'),('Задача на тестировании'), ('Задача нуждается в исправлении'), ('Задача выполнена');

INSERT INTO public.transitions
(previous, "next")
VALUES
('Новая задача', 'Задача назначена'),
('Задача назначена', 'Задача в работе'),
('Задача назначена', 'Задача отклонена'),
('Задача в работе', 'Задача отклонена'),
('Задача в работе', 'Ожидает тестирования'),
('Ожидает тестирования', 'Задача на тестировании'),
('Задача на тестировании', 'Задача нуждается в исправлении'),
('Задача на тестировании', 'Задача выполнена'),
('Задача нуждается в исправлении', 'Задача назначена');

