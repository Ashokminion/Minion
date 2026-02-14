-- MySQL Database Schema for AI Recommendation System

CREATE DATABASE IF NOT EXISTS recommendation_db;
USE recommendation_db;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'USER'
);

-- Items Table
CREATE TABLE IF NOT EXISTS items (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    category VARCHAR(100) NOT NULL,
    tags VARCHAR(500)
);

-- Preferences Table
CREATE TABLE IF NOT EXISTS preferences (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    category VARCHAR(100) NOT NULL,
    weight DOUBLE NOT NULL DEFAULT 1.0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Ratings Table
CREATE TABLE IF NOT EXISTS ratings (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    item_id BIGINT NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE
);

-- Insert Sample Admin User (password: admin123)
INSERT INTO users (username, password, role) VALUES 
('admin', '$2a$10$8YnZ4YvXL8L.1.Y9Y9Y9YuL8L.1.Y9Y9YvXL8L.1.Y9Y9YvXL8L.1', 'ADMIN');

-- Insert Sample Items
INSERT INTO items (title, description, category, tags) VALUES
('Avengers Endgame', 'Epic superhero finale', 'movies', 'action,superhero,marvel,adventure'),
('The Matrix', 'Sci-fi action thriller', 'movies', 'sci-fi,action,cyberpunk'),
('Interstellar', 'Space exploration epic', 'movies', 'sci-fi,drama,space'),
('The Shawshank Redemption', 'Prison drama masterpiece', 'movies', 'drama,hope,friendship'),
('Inception', 'Dream heist thriller', 'movies', 'sci-fi,thriller,mystery'),
('Clean Code', 'Software craftsmanship guide', 'books', 'programming,tech,software'),
('The Lean Startup', 'Entrepreneurship methodology', 'books', 'business,startup,tech'),
('Deep Work', 'Productivity and focus', 'books', 'productivity,self-improvement'),
('iPhone 15 Pro', 'Latest Apple smartphone', 'tech', 'smartphone,apple,gadget'),
('MacBook Pro M3', 'Powerful laptop for creators', 'tech', 'laptop,apple,performance');
