# JBFinder

A lightweight Python reconnaissance tool for directory and DNS enumeration using custom wordlists.

## Features

- Directory Enumeration
- DNS Subdomain Enumeration
- Custom Wordlist Support
- HTTP Status Code Detection
- Colored Console Output

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/JOSEBOSE/jbfinder.git
cd jbfinder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

```txt
requests
colorama
```

## Usage

Run the tool:

```bash
python jbfinder.py
```

### Directory Enumeration

Select:

```text
dir
```

Provide:

```text
https://example.com
```

Provide a wordlist path:

```text
wordlists/common.txt
```

Example output:

```text
200 => https://example.com/admin
301 => https://example.com/login
403 => https://example.com/private
```

### DNS Enumeration

Select:

```text
dns
```

Provide a target domain:

```text
example.com
```

Provide a wordlist path:

```text
wordlists/subdomains.txt
```

Example output:

```text
host found => www.example.com
host found => mail.example.com
```

## Example Wordlist

```txt
admin
login
dashboard
backup
uploads
```

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning domains, websites, or systems.

## License

MIT License
