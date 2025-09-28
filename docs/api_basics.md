# API Basics Guide

## What is an API?

API stands for **Application Programming Interface**. It's like a menu in a restaurant:

- The **menu** provides a list of dishes you can order
- The **kitchen** is the system that prepares the food
- You don't need to know how the kitchen works, just how to order from the menu

## REST API Fundamentals

### HTTP Methods
- **GET** - Retrieve data
- **POST** - Create new data
- **PUT** - Update existing data
- **DELETE** - Remove data

### Status Codes
- **200** - Success
- **400** - Bad request (you made an error)
- **401** - Unauthorized (invalid API key)
- **429** - Too many requests (rate limited)
- **500** - Server error

### Key Components
1. **Endpoint** - The URL you send requests to
2. **Headers** - Metadata (authentication, content type)
3. **Body** - The actual data you're sending/receiving
4. **Authentication** - How you prove who you are (API keys)

## DeepSeek API Specifics

### Authentication
```http
Authorization: Bearer your-api-key-here
