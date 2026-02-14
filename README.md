# AI-Integrated Recommendation System

A complete full-stack AI-powered recommendation system using Spring Boot, Python Flask, Bootstrap 5, and MySQL.

## Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│  Bootstrap  │ ───► │ Spring Boot  │ ───► │   Python    │
│   Frontend  │      │   Backend    │      │ Flask AI    │
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │    MySQL     │
                     │  Database    │
                     └──────────────┘
```

## Tech Stack

- **Backend**: Spring Boot 3.2 (Java 17)
- **Security**: JWT Authentication
- **Database**: MySQL 8.0
- **AI Engine**: Python 3.10 + Flask + scikit-learn
- **Frontend**: Bootstrap 5 + Vanilla JavaScript

## Project Structure

```
├── java/                          # Spring Boot Backend
│   ├── src/main/java/com/recommendation/
│   │   ├── config/               # Security & JWT Config
│   │   ├── controller/           # REST Controllers
│   │   ├── dto/                  # Data Transfer Objects
│   │   ├── entity/               # JPA Entities
│   │   ├── repository/           # Spring Data Repositories
│   │   └── service/              # Business Logic
│   └── pom.xml
│
├── python-ai-service/            # Flask AI Service
│   ├── model/
│   │   └── similarity_engine.py  # Content-Based Recommender
│   ├── app.py                    # Flask Entry Point
│   └── requirements.txt
│
├── frontend/                     # Bootstrap UI
│   ├── index.html               # Login/Register
│   ├── dashboard.html           # User Dashboard
│   ├── admin.html               # Admin Panel
│   └── js/                      # JavaScript
│
└── database/                     # MySQL Schema
    └── schema.sql
```

## Features

### 1. User Authentication (JWT)
- Secure registration and login
- Role-based access control (USER, ADMIN)
- Token-based stateless authentication

### 2. User Preferences Management
- Add categories with weighted importance
- Visual preference display
- Used for AI recommendation personalization

### 3. AI-Powered Recommendations
- Content-based filtering using TF-IDF
- Cosine similarity matching
- Category boosting for better results

### 4. Admin Dashboard
- Add new items (movies, books, tech)
- View all items in the system
- Admin-only access

### 5. Responsive Bootstrap UI
- Mobile-first design
- Gradient themes
- Card-based layouts
- Modal dialogs

## Setup Instructions

### Prerequisites
- Java 17+
- Maven 3.8+
- Python 3.10+
- MySQL 8.0+
- Node.js (optional, for live-server)

### 1. Database Setup

```bash
# Start MySQL server
mysql -u root -p

# Run schema
source database/schema.sql
```

### 2. Backend (Spring Boot)

```bash
cd java

# Update application.properties with your MySQL credentials
# Build and run
mvn spring-boot:run
```

Backend will run on `http://localhost:8080`

### 3. AI Service (Flask)

```bash
cd python-ai-service

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

AI service will run on `http://localhost:5000`

### 4. Frontend

```bash
cd frontend

# Option 1: Use Python's HTTP server
python -m http.server 3000

# Option 2: Use VS Code Live Server extension

# Option 3: Use npx serve
npx serve -l 3000
```

Frontend will be available at `http://localhost:3000`

## API Documentation

### Authentication

**POST** `/api/auth/register`
```json
{
  "username": "john",
  "password": "password123"
}
```

**POST** `/api/auth/login`
```json
{
  "username": "john",
  "password": "password123"
}
```

### Preferences

**GET** `/api/preferences`  
Headers: `Authorization: Bearer <token>`

**POST** `/api/preferences`
```json
{
  "category": "action",
  "weight": 3.0
}
```

### Recommendations

**GET** `/api/recommendations`  
Headers: `Authorization: Bearer <token>`

Returns personalized items based on user preferences.

### Admin

**POST** `/api/admin/items`  
Headers: `Authorization: Bearer <token>`
```json
{
  "title": "The Dark Knight",
  "category": "movies",
  "description": "Batman saga",
  "tags": "action,superhero,dc"
}
```

## How It Works

### Recommendation Algorithm

1. **User Profile**: System collects user's category preferences
2. **TF-IDF Vectorization**: Convert item tags and categories to numerical vectors
3. **Cosine Similarity**: Calculate similarity between user profile and all items
4. **Category Boosting**: Items matching user's preferred categories get 1.5x score boost
5. **Ranking**: Return top 10 items with highest scores

### Sequence Flow

```
User → Login → Add Preferences → Request Recommendations
                                         ↓
                                   Spring Boot
                                         ↓
                              Fetch User Preferences
                                         ↓
                              Send to Flask AI
                                         ↓
                           Compute Similarity Scores
                                         ↓
                        Return Ranked Item IDs
                                         ↓
                          Display to User
```

## Testing

### Default Credentials

**Admin**:
- Username: `admin`
- Password: `admin123` (Note: Update password hash in schema.sql)

### Test Workflow

1. Register a new user
2. Add preferences (e.g., "action", "sci-fi")
3. Click "Get Recommendations"
4. View personalized items

## Security Features

- BCrypt password hashing
- JWT token authentication
- CORS configuration
- Role-based endpoint protection
- Stateless session management

## Future Enhancements

- [ ] Collaborative filtering
- [ ] User ratings integration
- [ ] Real-time updates with WebSockets
- [ ] Advanced filtering options
- [ ] Rating-based recommendations
- [ ] User profile management
- [ ] Item image uploads

## License

MIT License
