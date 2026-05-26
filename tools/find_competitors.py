import argparse
import os
import json
from googleapiclient.discovery import build

def main():
    parser = argparse.ArgumentParser(description='Find potential YouTube competitors based on a niche/keyword.')
    parser.add_argument('--keyword', type=str, required=True, help='The niche or topic of your channel (e.g., "history documentaries", "tech reviews").')
    parser.add_argument('--max_results', type=int, default=5, help='Number of channels to return.')
    args = parser.parse_args()

    api_key = os.environ.get('YOUTUBE_API_KEY')
    if not api_key:
        print("Error: YOUTUBE_API_KEY environment variable not set.")
        print("Please set it using: export YOUTUBE_API_KEY='your_api_key'")
        return

    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        print(f"Searching for channels related to: '{args.keyword}'...")
        # Step 1: Search for videos related to the keyword to find active channels
        search_response = youtube.search().list(
            q=args.keyword,
            type='video',
            part='id,snippet',
            maxResults=args.max_results * 2, # Get more results to find unique channels
            order='relevance' # Order by relevance to the keyword
        ).execute()

        channel_ids = set()
        competitors = []

        for search_result in search_response.get('items', []):
            channel_id = search_result['snippet']['channelId']

            # Avoid duplicate channels
            if channel_id not in channel_ids:
                channel_ids.add(channel_id)

                # Step 2: Get detailed channel information
                channel_response = youtube.channels().list(
                    id=channel_id,
                    part='snippet,statistics'
                ).execute()

                if channel_response.get('items'):
                    channel_info = channel_response['items'][0]
                    competitors.append({
                        'title': channel_info['snippet']['title'],
                        'url': f"https://www.youtube.com/channel/{channel_id}",
                        'description': channel_info['snippet']['description'][:200] + "...",
                        'subscribers': channel_info['statistics'].get('subscriberCount', 'Hidden'),
                        'total_views': channel_info['statistics'].get('viewCount', '0')
                    })

                if len(competitors) >= args.max_results:
                    break

        print("\n--- Potential Competitors Found ---")
        for i, comp in enumerate(competitors, 1):
            print(f"\n{i}. {comp['title']}")
            print(f"   URL: {comp['url']}")
            print(f"   Subscribers: {comp['subscribers']} | Total Views: {comp['total_views']}")
            print(f"   Description: {comp['description']}")

    except Exception as e:
         print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
