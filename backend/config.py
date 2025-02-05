import os

class Config:
    # Define your allowed origins (could be an array of URLs)
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",  # React local dev server
        "http://192.168.31.249:3000",
        "https://home-price-prediction-three.vercel.app/"  # Production frontend URL
    ]

    # Optionally, you can also configure other CORS settings (e.g., allowed headers, methods, etc.)
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization']
    CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'DELETE']
