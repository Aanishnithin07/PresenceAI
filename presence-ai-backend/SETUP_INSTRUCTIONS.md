# Setup Instructions for PresenceAI Backend

## Required: Google AI API Key

1. **Get a free API key** from Google AI Studio:
   - Visit: https://aistudio.google.com/
   - Sign in with your Google account
   - Create a new API key
   - Copy the API key

2. **Create a .env file** in the `presence-ai-backend` folder:
   ```
   GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
   ```

3. **Replace YOUR_ACTUAL_API_KEY_HERE** with your real API key from step 1.

## Example .env file:
```
GOOGLE_API_KEY="AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Security Note:
- Never commit the .env file to version control
- Keep your API key private
- The .env file is already in .gitignore
