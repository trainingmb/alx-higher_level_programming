-- creates the MySQL server user user_0d_1
-- Create Statement
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant Priveleges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Change Password
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Flush Privileges
FLUSH PRIVILEGES;

