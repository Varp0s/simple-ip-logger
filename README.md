# simple-ip-logger

## Description

A simple IP logger that records the IP addresses of visitors to your website. This tool can be used for analytics, security, or other purposes.

## Sample Result

```json
{
    "public_ip": {
        "asn": 34xxx,
        "asn_organization": "Mx",
        "city": "Mx",
        "continent_code": "xx",
        "country": "Tx",
        "country_code": "xx",
        "ip": "4xx.xxx.xxx.xx",
        "isp": "Mx",
        "latitude": 3x,
        "longitude": 3x,
        "organization": "Mx",
        "postal_code": "4x",
        "region": "Mx",
        "region_code": "4xx",
        "timezone": "Europe"
    }
}
```

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Varp0s/simple-ip-logger
    ```

2. Navigate to the project directory:

    ```sh
    cd simple-ip-logger
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Start the server:

    ```sh
    python3 logger.py
    ```

2. Visit `http://localhost:5000/public-ip` in your web browser.

3. The IP addresses of visitors will be logged in the console or a specified log file.

4. You can make public with various methods.

## License

This project is licensed under the MIT License.
