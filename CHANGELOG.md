# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.1] - 2025-06-22

### Changed
- Renamed script file from `jwplayer_api_downloader.py` to `jw_player_api_downloader.py`
- Updated all repository URLs in README.md to match new GitHub repository name
- Updated all script filename references in documentation

## [1.1.0] - 2025-06-22

### Added
- Comprehensive README.md with installation, usage, and configuration instructions
- Virtual environment installation instructions for better dependency management
- Structured TODO.md task management system
- English translations for all German text in codebase
- GitHub clone installation method (recommended)
- Direct single file download option from GitHub raw URL

### Changed
- Improved code documentation and comments
- Standardized Markdown formatting across all documentation
- Updated README.md installation section with GitHub repository options
- Restructured installation alternatives for better clarity

### Security
- Sanitized all sensitive information in configuration examples

## [1.0.0] - 2025-06-20

### Added
- Initial release of JW Player API Downloader
- Support for downloading audio files (.m4a format)
- Support for downloading video files (.mp4 format)
- Bulk download functionality for all media from a JW Player site
- Metadata export with source information
- Progress tracking and file size display during downloads
- Automatic filename sanitization for cross-platform compatibility
- Skip existing files functionality
- Comprehensive logging system with file and console output
- Command-line interface with multiple options
- Environment variable support for configuration
- Rate limiting to prevent API abuse
- Media mapping JSON export for ID to title correlation
- Extended metadata export including delivery sources

### Features
- **Download Types**: Audio-only, video-only, or both simultaneously
- **API Integration**: JW Player Management API v2 and Delivery API v2
- **File Management**: Automatic directory creation and file organization
- **Error Handling**: Graceful error handling with detailed logging
- **Progress Display**: Real-time download progress with file size information
- **Metadata Preservation**: Complete metadata export with source URLs

### Technical Implementation
- Python 3.6+ compatibility
- HTTP session reuse for improved performance
- Chunked file downloads for memory efficiency
- JSON-based configuration and metadata storage
- Cross-platform file path handling
- Robust error recovery and retry logic