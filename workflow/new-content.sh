#!/bin/bash
# New Content Workflow - Create folder structure for new video topic

if [ -z "$1" ]; then
    echo "Enter video topic name (use hyphens, e.g., battle-of-stalingrad):"
    read TOPIC
else
    TOPIC="$1"
fi

DATE=$(date +%Y-%m-%d)
FOLDER_NAME="${DATE}_${TOPIC}"
mkdir -p "research/$FOLDER_NAME/assets"

echo "✅ Created: research/$FOLDER_NAME"
echo "Next: Push to GitHub and run Gemini AI workflow!"
