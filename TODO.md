# TODO - JW Player API Downloader

## 🔥 Urgent
*Critical bugs and blockers (complete within days)*

- [ ] **Security Review** - Audit code for potential security vulnerabilities
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 4h
  - **Labels**: security, audit
  - **Created**: 2025-06-22
  - **Due**: 2025-06-24
  - **Notes**: Review API key handling, file path validation, and input sanitization

- [ ] **Input Validation** - Validate API credentials and user inputs
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 2h
  - **Labels**: security, validation
  - **Created**: 2025-06-22
  - **Due**: 2025-06-25
  - **Notes**: Validate API keys, site IDs, file paths, and command-line arguments

## ⚡ High Priority
*Important features and fixes (complete within weeks)*

- [ ] **Add Resume Capability** - Resume interrupted downloads
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 1d
  - **Labels**: feature, enhancement
  - **Created**: 2025-06-22
  - **Notes**: Track partial downloads and resume from last position

- [ ] **Implement Retry Logic** - Automatic retry for failed downloads
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 4h
  - **Labels**: feature, reliability
  - **Created**: 2025-06-22
  - **Notes**: Exponential backoff, max retry attempts configuration

- [ ] **Add Configuration File Support** - Support for config files (.ini, .yaml)
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 6h
  - **Labels**: feature, config
  - **Created**: 2025-06-22
  - **Notes**: Support multiple config formats, precedence order

- [ ] **Improve Error Messages** - More descriptive error messages for users
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 2h
  - **Labels**: enhancement, ux
  - **Created**: 2025-06-22
  - **Notes**: User-friendly error messages with suggested solutions

- [ ] **Add Download Verification** - Verify file integrity after download
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 3h
  - **Labels**: feature, integrity
  - **Created**: 2025-06-22
  - **Notes**: MD5/SHA256 checksums, file size verification

## 📈 Medium Priority
*Enhancements and optimizations (complete within months)*

- [ ] **Add Parallel Downloads** - Download multiple files simultaneously
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 1w
  - **Labels**: feature, performance
  - **Created**: 2025-06-22
  - **Notes**: Thread pool or async implementation, configurable concurrency

- [ ] **Quality Selection** - Allow users to select specific video quality
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 4h
  - **Labels**: feature, enhancement
  - **Created**: 2025-06-22
  - **Notes**: List available qualities, user selection interface

- [ ] **Download Statistics** - Show download speed, ETA, success rates
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 6h
  - **Labels**: feature, analytics
  - **Created**: 2025-06-22
  - **Notes**: Real-time stats display, historical data

- [ ] **Filter by Date Range** - Download only videos from specific date range
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 3h
  - **Labels**: feature, filtering
  - **Created**: 2025-06-22
  - **Notes**: Command-line date range options

- [ ] **Add Unit Tests** - Comprehensive test coverage
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 1w
  - **Labels**: test, quality
  - **Created**: 2025-06-22
  - **Notes**: Unit tests, integration tests, mock API responses

- [ ] **Bandwidth Limiting** - Control download speed to limit bandwidth usage
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 4h
  - **Labels**: feature, performance
  - **Created**: 2025-06-22
  - **Notes**: Configurable download speed limits

- [ ] **Progress Bar Enhancement** - Better progress display with multiple files
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 3h
  - **Labels**: enhancement, ux
  - **Created**: 2025-06-22
  - **Notes**: Multi-file progress, overall completion percentage

## 🔮 Future
*Long-term goals and major features*

- [ ] **Cloud Storage Integration** - Direct upload to cloud storage
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 2w
  - **Labels**: feature, integration, major
  - **Created**: 2025-06-22
  - **Notes**: Support for AWS S3, Google Drive, OneDrive

- [ ] **Webhook Support** - Trigger downloads via webhooks
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 1w
  - **Labels**: feature, api, major
  - **Created**: 2025-06-22
  - **Notes**: REST API endpoint for remote triggering

- [ ] **Scheduling** - Schedule downloads for specific times
  - **Status**: Not Started
  - **Assignee**: @peerhoffmann
  - **Estimate**: 1w
  - **Labels**: feature, automation, major
  - **Created**: 2025-06-22
  - **Notes**: Cron-like scheduling, automatic execution

## 💡 Ideas
*Brainstormed concepts for evaluation*

- [ ] **Docker Container** - Containerized deployment
  - **Status**: Idea
  - **Labels**: docker, deployment, idea
  - **Created**: 2025-06-22
  - **Notes**: Easy deployment and scaling

- [ ] **Transcription Support** - Automatic audio transcription connection to existing transcription script
  - **Status**: Idea
  - **Labels**: ai, transcription, integration, idea
  - **Created**: 2025-06-22
  - **Notes**: Integration with Peer's existing transcription script for automatic audio-to-text conversion

- [ ] **Subtitle Support** - Download closed captions/subtitles if available
  - **Status**: Idea
  - **Labels**: accessibility, subtitles, idea
  - **Created**: 2025-06-22
  - **Notes**: Extract and download subtitle tracks from JW Player content

---

## Completed
*Recently finished tasks (archived to CHANGELOG.md)*

- [x] **Initial Project Setup** - Basic project structure and core functionality
  - **Status**: Done
  - **Completed**: 2025-06-20
  - **Notes**: Core download functionality implemented

- [x] **Documentation Package** - Comprehensive project documentation
  - **Status**: Done
  - **Completed**: 2025-06-22
  - **Notes**: README.md, CHANGELOG.md, TODO.md created with full specifications