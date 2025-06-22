# JW Player API Downloader

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue)](https://www.paypal.me/peerhoffmann)

**If you find this project helpful, consider supporting me with a small donation.**

## Introduction

JW Player API Downloader is a Python command-line tool for downloading audio and video content from JW Player sites using the JW Player API. This tool enables bulk downloading of media files with metadata preservation, progress tracking, and flexible format selection.

**Key Features:**
- Download audio-only files (.m4a format)
- Download video files (.mp4 format) 
- Download both audio and video simultaneously
- Bulk download all media from a JW Player site
- Metadata export with source information
- Progress tracking and file size display
- Automatic filename sanitization
- Skip existing files option
- Comprehensive logging

## Prerequisites

- **Python 3.6+** - Required for running the application
- **JW Player API credentials** - API Secret and Site ID from your JW Player dashboard
- **Internet connection** - Required for API calls and media downloads

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 512MB available
- **Storage**: Sufficient space for downloaded media files
- **Network**: Stable internet connection for API requests

## Installation

### Recommended: Clone from GitHub (Virtual Environment)

It's highly recommended to install this script in a virtual environment to avoid dependency conflicts:

#### On Linux/macOS:
```bash
# Clone the repository
git clone https://github.com/PeerHoffmann/jwplayer_api_downloader.git
cd jwplayer_api_downloader

# Create virtual environment
python3 -m venv jwplayer-downloader-env

# Activate virtual environment
source jwplayer-downloader-env/bin/activate

# Install dependencies
pip install requests
```

#### On Windows:
```cmd
# Clone the repository
git clone https://github.com/PeerHoffmann/jwplayer_api_downloader.git
cd jwplayer_api_downloader

# Create virtual environment
python -m venv jwplayer-downloader-env

# Activate virtual environment
jwplayer-downloader-env\Scripts\activate

# Install dependencies
pip install requests
```

#### Using the Virtual Environment:
```bash
# Always activate the virtual environment before using the script
source jwplayer-downloader-env/bin/activate  # Linux/macOS
# or
jwplayer-downloader-env\Scripts\activate     # Windows

# Run the script
python jwplayer_api_downloader.py --help

# When done, deactivate the virtual environment
deactivate
```

### Alternative: Download Single File
```bash
# Create directory and download just the script file
mkdir jwplayer_api_downloader
cd jwplayer_api_downloader

# Download the script directly from GitHub
wget https://raw.githubusercontent.com/PeerHoffmann/jwplayer_api_downloader/main/jwplayer_api_downloader.py

# Install dependencies (consider using virtual environment)
pip install requests
```

### Alternative: System-wide Installation (Not Recommended)
```bash
# Clone repository
git clone https://github.com/PeerHoffmann/jwplayer_api_downloader.git
cd jwplayer_api_downloader

# Install dependencies system-wide
pip install requests
```

### Verification
Test the installation:
```bash
python jwplayer_api_downloader.py --help
```

## Configuration

### Environment Variables
Create a `.env` file or set environment variables:

```bash
# Required API credentials
export JW_API_SECRET="enter_your_api_key_here"
export JW_SITE_ID="enter_your_site_id_here"

# Optional settings
export JW_DOWNLOAD_DIR="./downloads"
```

### Configuration Files

#### Example .env file:
```env
JW_API_SECRET=enter_your_api_key_here
JW_SITE_ID=enter_your_site_id_here
JW_DOWNLOAD_DIR=./downloads
```

### Getting JW Player API Credentials

1. Log into your JW Player dashboard
2. Navigate to **Account** > **API Credentials**
3. Copy your **API Secret**
4. Navigate to **Content** > **Sites** 
5. Copy your **Site ID** from the URL or site settings

## Usage

### Basic Usage

#### Download all audio files:
```bash
python jwplayer_api_downloader.py --api-secret YOUR_API_SECRET --site-id YOUR_SITE_ID
```

#### Download all video files:
```bash
python jwplayer_api_downloader.py --api-secret YOUR_API_SECRET --site-id YOUR_SITE_ID --type video
```

#### Download both audio and video:
```bash
python jwplayer_api_downloader.py --api-secret YOUR_API_SECRET --site-id YOUR_SITE_ID --type both
```

### Advanced Usage

#### Custom download directory:
```bash
python jwplayer_api_downloader.py --download-dir /path/to/downloads --type audio
```

#### Export metadata only:
```bash
python jwplayer_api_downloader.py --export-metadata
```

#### Force re-download existing files:
```bash
python jwplayer_api_downloader.py --skip-existing false
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--api-secret` | JW Player API Secret | From `JW_API_SECRET` env var |
| `--site-id` | JW Player Site ID | From `JW_SITE_ID` env var |
| `--download-dir` | Download directory path | `./downloads` |
| `--type` | Download type: audio, video, both | `audio` |
| `--skip-existing` | Skip existing files | `true` |
| `--export-metadata` | Export metadata only | `false` |

### Output Files

- **Audio files**: `{MEDIA_ID}_audio.m4a`
- **Video files**: `{MEDIA_ID}_{QUALITY}.mp4`
- **Metadata**: `media_mapping.json`
- **Extended metadata**: `metadata_with_sources.json`
- **Logs**: `jwplayer_download.log`

### Troubleshooting

**Common Issues:**

1. **Authentication Error**: Verify API Secret and Site ID are correct
2. **Rate Limiting**: Tool includes automatic rate limiting (0.1-0.5s delays)
3. **Network Timeouts**: Check internet connection stability
4. **Insufficient Storage**: Ensure adequate disk space for downloads
5. **Permission Errors**: Check write permissions for download directory
6. **Virtual Environment Issues**: Ensure virtual environment is activated before running

**Debug Mode:**
Check `jwplayer_download.log` for detailed error information.

## Tools & Dependencies

### Core Dependencies
- **[Python](https://python.org/)** - Programming language runtime | [GitHub](https://github.com/python/cpython) | [Docs](https://docs.python.org/)
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for API calls | [GitHub](https://github.com/psf/requests) | [Docs](https://requests.readthedocs.io/)

### Standard Library Modules
- **[argparse](https://docs.python.org/3/library/argparse.html)** - Command-line argument parsing
- **[logging](https://docs.python.org/3/library/logging.html)** - Logging framework
- **[pathlib](https://docs.python.org/3/library/pathlib.html)** - File path operations
- **[urllib.parse](https://docs.python.org/3/library/urllib.parse.html)** - URL parsing utilities
- **[json](https://docs.python.org/3/library/json.html)** - JSON data handling
- **[time](https://docs.python.org/3/library/time.html)** - Time-related functions
- **[os](https://docs.python.org/3/library/os.html)** - Operating system interface

### External APIs
- **[JW Player Management API v2](https://developer.jwplayer.com/jwplayer/reference/get_v2-sites-site-id-media)** - Media listing and metadata
- **[JW Player Delivery API v2](https://developer.jwplayer.com/jwplayer/docs/delivery-api-reference)** - Media source URLs

## Contributing

### Development Setup
1. Fork the repository
2. Create a virtual environment (recommended)
3. Create a feature branch
4. Make your changes
5. Test thoroughly
6. Submit a pull request

### Coding Standards
- Follow PEP 8 style guidelines
- Include docstrings for all functions
- Add logging for important operations
- Handle errors gracefully
- Maintain backward compatibility

### Pull Request Process
1. Update documentation for any new features
2. Add tests if applicable
3. Ensure all existing functionality works
4. Update CHANGELOG.md with changes

---

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue)](https://www.paypal.me/peerhoffmann)

**If you find this project helpful, consider supporting me with a small donation.**

More information about me and my projects can be found at https://www.peer-hoffmann.de.

If you need support with search engine optimization for your website, online shop, or international project, feel free to contact me at https://www.om96.de.