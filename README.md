
# Lets-Shortify
A simple web application to shorten URLs built using Flask, MySQL, and Redis.

## Features

- Convert a long URL to a shortened URL.
- Store and retrieve URL mappings in MySQL.
- Cache URL mappings in Redis for faster access.
- Docker support for easy deployment.

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Installation

1. Clone this repository:
   ```bash
   git clone [Your GitHub Repo URL]
   cd [Your Repo Directory Name]
   ```

2. Start the Docker Container(s):
   ```bash
   docker-compose up -d
   ```

3. Navigate to the application in your web browser:
   ```
   http://localhost:1215/api/home
   ```

4. Enter the URL you want to shorten. The output screen will give you the shortened URL.

5. Navigate to the shortened URL by navigating to:
   ```
   http://localhost:1215/s/{shorten_url}
   ```

## Running the Tests

This is work in Progress. If you would like to contribute, please feel free to do so.

## Contributing

If you wish to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.


## Licensing

The code in this project is licensed under **MIT license**.



