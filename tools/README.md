# YouTube Research Tools

This directory contains Python scripts to help automate research for your YouTube channel.

## 1. Find Competitors (`find_competitors.py`)

Since you might not know who your competitors are yet, this script uses the official YouTube Data API to search for your specific channel niche/topic and returns a list of top channels (competitors) operating in that space.

### Setup Instructions

1. **Install Python Dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Get a YouTube API Key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Go to "APIs & Services" > "Library".
   - Search for "YouTube Data API v3" and click "Enable".
   - Go to "APIs & Services" > "Credentials".
   - Click "Create Credentials" > "API key".
   - Copy the generated API key.

3. **Set the Environment Variable:**
   Before running the script, you must provide it with your API key by setting an environment variable in your terminal:
   ```bash
   # On macOS/Linux:
   export YOUTUBE_API_KEY="your_copied_api_key_here"

   # On Windows (Command Prompt):
   set YOUTUBE_API_KEY="your_copied_api_key_here"

   # On Windows (PowerShell):
   $env:YOUTUBE_API_KEY="your_copied_api_key_here"
   ```

### How to Run

Run the script from the command line, providing your channel's main topic or niche as the `--keyword` argument.

```bash
python find_competitors.py --keyword "history documentaries"
```

**Options:**
- `--keyword`: (Required) The niche or topic of your channel. Keep it descriptive (e.g., "tech reviews under 100", "ancient roman history", "cozy gaming").
- `--max_results`: (Optional) The number of competitor channels to return. Default is 5.

**Example Output:**
The script will return a list of channels, their URLs, subscriber counts, total views, and a brief description. You can then use this list to study their video titles, thumbnails, and editing styles!
