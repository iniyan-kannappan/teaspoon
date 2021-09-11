createdb teaspoon_db
CREATE ROLE teaspoon_user WITH LOGIN PASSWORD 'teaspoon_password';
GRANT ALL PRIVILEGES ON DATABASE teaspoon_db TO teaspoon_user;