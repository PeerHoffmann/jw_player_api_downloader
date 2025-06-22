#!/usr/bin/env python3
"""
JW Player Audio/Video Downloader
Downloads all audio files from a JW Player site
"""

import requests
import os
import time
import json
import argparse
from urllib.parse import urlparse
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jwplayer_download.log'),
        logging.StreamHandler()
    ]
)

class JWPlayerDownloader:
    def __init__(self, api_secret, site_id, download_dir="downloads", download_type="audio"):
        self.api_secret = api_secret
        self.site_id = site_id
        self.download_dir = Path(download_dir)
        self.download_type = download_type  # "audio", "video", "both"
        self.base_url = "https://api.jwplayer.com/v2"
        self.delivery_url = "https://cdn.jwplayer.com/v2"
        self.headers = {
            'Authorization': f'Bearer {api_secret}',
            'Content-Type': 'application/json'
        }
        
        # Create download directory
        self.download_dir.mkdir(exist_ok=True)
        
        # Session for better performance
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_all_media(self):
        """Fetches all media items from the site"""
        media_list = []
        page = 1
        page_limit = 100  # Maximum per request
        
        while True:
            url = f"{self.base_url}/sites/{self.site_id}/media/"
            params = {
                'page': page,
                'page_length': page_limit
            }
            
            try:
                response = self.session.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                media_items = data.get('media', [])
                if not media_items:
                    break
                    
                media_list.extend(media_items)
                logging.info(f"Page {page}: {len(media_items)} videos found")
                
                # Check if more pages are available
                if len(media_items) < page_limit:
                    break
                    
                page += 1
                time.sleep(0.1)  # Rate limiting
                
            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching media list: {e}")
                break
        
        logging.info(f"Total {len(media_list)} videos found")
        return media_list
    
    def get_video_sources(self, media_id):
        """Fetches video sources via the Delivery API"""
        url = f"{self.delivery_url}/media/{media_id}"
        
        try:
            # Get all sources (audio and video)
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if 'playlist' in data and data['playlist']:
                return data['playlist'][0]  # Erstes (und einziges) Playlist-Item
            else:
                logging.warning(f"No playlist data found for {media_id}")
                return None
                
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching video sources for {media_id}: {e}")
            return None
    
    def select_audio_source(self, sources):
        """Selects the audio source"""
        audio_sources = [s for s in sources if s.get('type') == 'audio/mp4']
        
        if audio_sources:
            # Take the first (and usually only) audio source
            return audio_sources[0]
        else:
            # Fallback: Take the smallest video (usually has the best audio quality)
            video_sources = [s for s in sources if s.get('type') == 'video/mp4' and 'height' in s]
            if video_sources:
                return min(video_sources, key=lambda x: x.get('height', 0))
        
        return None
    
    def select_best_source(self, sources):
        """Selects the best source based on download type"""
        if self.download_type == "audio":
            return self.select_audio_source(sources)
        elif self.download_type == "video":
            video_sources = [s for s in sources if s.get('type') == 'video/mp4' and 'height' in s]
            if video_sources:
                return max(video_sources, key=lambda x: x.get('height', 0))
        elif self.download_type == "both":
            # For "both" will be handled separately later
            return None
        
        return None
    
    def sanitize_filename(self, filename):
        """Sanitizes filenames for the file system"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename.strip()
    
    def format_file_size(self, size_bytes):
        """Formats file size into readable format"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024**2:
            return f"{size_bytes/1024:.1f} KB"
        elif size_bytes < 1024**3:
            return f"{size_bytes/(1024**2):.1f} MB"
        else:
            return f"{size_bytes/(1024**3):.1f} GB"
    
    def download_file(self, url, filepath, media_title="Unknown", expected_size=None):
        """Downloads a file"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', expected_size or 0))
            downloaded = 0
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        # Show progress
                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            size_info = f"{self.format_file_size(downloaded)}/{self.format_file_size(total_size)}"
                            print(f"\r{media_title}: {percent:.1f}% ({size_info})", end='', flush=True)
            
            print()  # New line after progress
            logging.info(f"Download completed: {filepath} ({self.format_file_size(downloaded)})")
            return True
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Download error for {url}: {e}")
            return False
    
    def download_single_file(self, source, media_title, file_type, skip_existing, media_id):
        """Downloads a single file"""
        download_url = source.get('file')
        file_size = source.get('filesize', 0)
        
        if not download_url:
            logging.warning(f"No download URL available")
            return False
        
        # Filename based on Media-ID for unique assignment
        if file_type == "audio":
            extension = ".m4a"
            safe_filename = f"{media_id}_audio{extension}"
        else:
            extension = ".mp4"
            label = source.get('label', f"{source.get('height', 'unknown')}p")
            safe_filename = f"{media_id}_{label}{extension}"
        
        safe_filename = self.sanitize_filename(safe_filename)
        filepath = self.download_dir / safe_filename
        
        # Skip if file already exists
        if skip_existing and filepath.exists():
            logging.info(f"Skipping (already exists): {safe_filename}")
            return True
        
        # Show download info
        size_info = self.format_file_size(file_size) if file_size else "Unknown"
        logging.info(f"Downloading: {file_type.upper()} - {media_title} ({size_info}) -> {safe_filename}")
        
        # Start download
        return self.download_file(download_url, filepath, f"{media_title}", file_size)
    
    def download_media_file(self, media_id, media_title, video_data, skip_existing):
        """Downloads a single media file"""
        if not video_data or 'sources' not in video_data:
            logging.warning(f"No sources found for {media_id}")
            return False
        
        sources = video_data['sources']
        
        if self.download_type == "both":
            # Download both audio and video
            audio_source = self.select_audio_source(sources)
            video_sources = [s for s in sources if s.get('type') == 'video/mp4' and 'height' in s]
            video_source = max(video_sources, key=lambda x: x.get('height', 0)) if video_sources else None
            
            success = True
            if audio_source:
                success &= self.download_single_file(audio_source, media_title, "audio", skip_existing, media_id)
            if video_source:
                success &= self.download_single_file(video_source, media_title, "video", skip_existing, media_id)
            
            return success
        else:
            # Download only audio or only video
            selected_source = self.select_best_source(sources)
            if not selected_source:
                logging.warning(f"No suitable {self.download_type} source found for {media_id}")
                return False
            
            file_type = "audio" if selected_source.get('type') == 'audio/mp4' else "video"
            return self.download_single_file(selected_source, media_title, file_type, skip_existing, media_id)
    
    def download_all_videos(self, skip_existing=True):
        """Downloads all videos"""
        media_list = self.get_all_media()
        
        if not media_list:
            logging.warning("No videos found!")
            return
        
        success_count = 0
        error_count = 0
        skipped_count = 0
        
        # Create mapping file for Media-ID to title
        mapping = {}
        
        for i, media in enumerate(media_list, 1):
            media_id = media.get('id')
            media_title = media.get('metadata', {}).get('title', f'Video_{media_id}')
            original_title = media_title  # Keep original title for mapping
            media_title = self.sanitize_filename(media_title)
            
            # Save mapping
            mapping[media_id] = {
                'title': original_title,
                'sanitized_title': media_title,
                'audio_file': f"{media_id}_audio.m4a" if self.download_type in ["audio", "both"] else None,
                'created': media.get('created'),
                'duration': media.get('metadata', {}).get('duration'),
                'description': media.get('metadata', {}).get('description')
            }
            
            logging.info(f"[{i}/{len(media_list)}] Processing: {original_title} ({media_id})")
            
            # Fetch video sources via Delivery API
            video_data = self.get_video_sources(media_id)
            
            # Download the file(s)
            if self.download_media_file(media_id, media_title, video_data, skip_existing):
                success_count += 1
            else:
                error_count += 1
            
            # Rate limiting between videos
            time.sleep(0.5)
        
        # Save mapping file
        mapping_file = self.download_dir / "media_mapping.json"
        with open(mapping_file, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Media mapping saved to: {mapping_file}")
        
        # Summary
        logging.info(f"\nDownload completed:")
        logging.info(f"Successful: {success_count}")
        logging.info(f"Skipped: {skipped_count}")
        logging.info(f"Errors: {error_count}")
        logging.info(f"\nAudio files have format: MEDIA_ID_audio.m4a")
        logging.info(f"Use media_mapping.json to map Media-IDs to titles")
    
    def export_metadata(self):
        """Exports metadata of all videos as JSON"""
        media_list = self.get_all_media()
        
        # Extend metadata with video sources
        enhanced_metadata = []
        for media in media_list:
            media_id = media.get('id')
            video_data = self.get_video_sources(media_id)
            
            enhanced_media = media.copy()
            if video_data:
                enhanced_media['delivery_sources'] = video_data.get('sources', [])
            
            enhanced_metadata.append(enhanced_media)
            time.sleep(0.1)  # Rate limiting
        
        metadata_file = self.download_dir / "metadata_with_sources.json"
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(enhanced_metadata, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Extended metadata exported to: {metadata_file}")

def main():
    parser = argparse.ArgumentParser(description='JW Player Video/Audio Downloader')
    parser.add_argument('--api-secret', default=os.getenv('JW_API_SECRET'), help='JW Player API Secret')
    parser.add_argument('--site-id', default=os.getenv('JW_SITE_ID'), help='JW Player Site ID')
    parser.add_argument('--download-dir', default=os.getenv('JW_DOWNLOAD_DIR', './downloads'), help='Download directory')
    parser.add_argument('--type', default='audio', choices=['audio', 'video', 'both'], help='What to download: audio (default), video or both')
    parser.add_argument('--skip-existing', action='store_true', default=True, help='Skip existing files')
    parser.add_argument('--export-metadata', action='store_true', help='Export metadata only')
    
    args = parser.parse_args()
    
    if not args.api_secret or not args.site_id:
        print("Error: API Secret and Site ID are required!")
        print("Use --api-secret and --site-id parameters or set JW_API_SECRET and JW_SITE_ID environment variables")
        exit(1)
    
    downloader = JWPlayerDownloader(
        api_secret=args.api_secret,
        site_id=args.site_id,
        download_dir=args.download_dir,
        download_type=args.type
    )
    
    if args.export_metadata:
        downloader.export_metadata()
    else:
        downloader.download_all_videos(skip_existing=args.skip_existing)

if __name__ == "__main__":
    main()