# Analytics Worker

A background worker service for processing and analyzing data.

## Features

- Asynchronous task processing
- Scalable architecture
- Real-time analytics
- Error handling and retries

## Requirements

- Python 3.8+
- Redis 6.0+
- PostgreSQL 12+

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and set your environment variables:

```bash
cp .env.example .env
```

## Usage

Run the worker:

```bash
python -m analytics_worker
```

## Development

Run tests:

```bash
pytest
```

## License

MIT