# GoldenPort (Not Final README, project ongoing)

GoldenPort is a fully AI-powered Analyzer Port Scanner with API access. This project leverages modern technologies like FastAPI, Python, PostgreSQL, Docker, and MongoDB to provide a robust and efficient port scanning and analysis tool.

**For educational purposes only.**

## Folder Structure

```
GoldenPort/
├── Analyzer/         # AI-based analysis tools
├── API/              # FastAPI implementation for API access
├── Resources/        # Static resources and configuration files
├── Scanner/          # Core port scanning logic
│   ├── Objects/      # Object definitions for scanning
├── Scrapper/         # Web scrapping utilities
├── README.md         # Project documentation
├── .gitignore        # Git ignore file
├── pyscan.py         # Basic testing script
```

## Features

- **AI-Powered Analysis**: Advanced AI algorithms for port scanning and analysis.
- **FastAPI Integration**: A modern API for seamless interaction.
- **Database Support**: PostgreSQL for relational data and MongoDB for non-relational data.
- **Dockerized Deployment**: Easy setup and deployment using Docker.

## Requirements

- Python 3.9+
- FastAPI
- PostgreSQL
- MongoDB
- Docker

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CodeAndChaosDev/cyber-tools/tree/master/GoldenPort.git
    cd GoldenPort
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure PostgreSQL and MongoDB connections in the `Resources/` folder.

5. Run the application:
    ```bash
    python pyscan.py
    ```

## Usage

- Use the API to interact with the port scanner.
- Analyze results using the AI-powered Analyzer module.
- Extend functionality by adding custom scrappers or objects.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.