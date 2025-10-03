#!/bin/bash

# Start the PresenceAI frontend server
echo "Starting PresenceAI Frontend..."
cd presence-ai-frontend

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

# Start the React development server
echo "Starting React development server on http://localhost:3000"
npm start
