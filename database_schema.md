# Database Schema

## Tables

### users

| Column          | Type         | Constraints         |
| --------------- | ------------ | ------------------- |
| user_id         | SERIAL       | PRIMARY KEY         |
| email           | VARCHAR(255) | UNIQUE, NOT NULL    |
| hashed_password | VARCHAR(255) | NOT NULL            |
| created_at      | TIMESTAMP    | DEFAULT CURRENT_TIMESTAMP |

### notebooks

| Column      | Type      | Constraints         |
| ----------- | --------- | ------------------- |
| notebook_id | SERIAL    | PRIMARY KEY         |
| user_id     | INTEGER   | FOREIGN KEY (users) |
| title       | VARCHAR(255) | NOT NULL            |
| created_at  | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at  | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### sources

| Column             | Type         | Constraints            |
| ------------------ | ------------ | ---------------------- |
| source_id          | SERIAL       | PRIMARY KEY            |
| notebook_id        | INTEGER      | FOREIGN KEY (notebooks)|
| source_type        | VARCHAR(50)  | NOT NULL               |
| original_path_or_url | VARCHAR(2048)| NOT NULL               |
| status             | VARCHAR(50)  | NOT NULL               |
| created_at         | TIMESTAMP    | DEFAULT CURRENT_TIMESTAMP |

### chat_history

| Column      | Type    | Constraints            |
| ----------- | ------- | ---------------------- |
| message_id  | SERIAL  | PRIMARY KEY            |
| notebook_id | INTEGER | FOREIGN KEY (notebooks)|
| role        | VARCHAR(50) | NOT NULL               |
| content     | TEXT    | NOT NULL               |
| timestamp   | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| citations   | JSONB   |                        |
