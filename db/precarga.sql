CREATE TABLE developer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    skills  VARCHAR(255) NOT NULL,
    salary INT(6) NOT NULL,
    avatar VARCHAR(255) NOT NULL,
)


INSERT INTO developer (name, skills, salary, avatar) VALUES 
('Developer 1', 'HTML, CSS, JavaScript', 150000, 'https://ibb.co/QjBYyqf'),
('Developer 2', 'Python, Django', 200000, 'https://ibb.co/ZVJgjGz'),
('Developer 3', 'Java, Spring Boot', 300000, 'https://ibb.co/61RYBGd'),
('Developer 4', 'React, Node.js', 400000, 'https://ibb.co/QjBYyqf'),
('Developer 5', 'C#, .NET', 500000, 'https://ibb.co/ZVJgjGz'),
('Developer 6', 'PHP, Laravel', 600000, 'https://ibb.co/61RYBGd'),
('Developer 7', 'Python, Flask', 700000, 'https://ibb.co/QjBYyqf'),
('Developer 8', 'PHP, Symfony', 800000, 'https://ibb.co/ZVJgjGz'),
('Developer 9', 'C++, Qt', 900000, 'https://ibb.co/61RYBGd'),
('Developer 10', 'JavaScript, React', 100000, 'https://ibb.co/QjBYyqf'),
('Developer 11', 'Go, Gin', 200000, 'https://ibb.co/ZVJgjGz'),
('Developer 12', 'Ruby, Rails', 400000, 'https://ibb.co/61RYBGd');