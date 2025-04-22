import json
import logging
import sys
from typing import List, Dict, Any, Tuple

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def parse_json_chunks(json_data: str) -> List[List[Dict[str, Any]]]:
    chunks = []
    remaining_data = json_data.strip()
    
    if not remaining_data:
        raise ValueError("Input JSON data is empty")
    
    while remaining_data:
        try:
            obj, idx = json.JSONDecoder().raw_decode(remaining_data)
            chunks.append(obj)
            remaining_data = remaining_data[idx:].strip()
        except json.JSONDecodeError:
            logger.warning("Encountered JSON decode error, stopping parsing")
            break
    
    if not chunks:
        raise ValueError("No valid JSON objects found in input data")
    
    return chunks


def format_cookies(json_data: str) -> List[str]:
    formatted_cookies = []
    
    try:
        chunks = parse_json_chunks(json_data)
        
        for chunk in chunks:
            formatted_chunk = format_cookie_chunk(chunk)
            if formatted_chunk:
                formatted_cookies.append(formatted_chunk)
    except Exception as e:
        logger.error(f"Error formatting cookies: {e}")
        raise
    
    return formatted_cookies


def format_cookie_chunk(chunk: List[Dict[str, Any]]) -> str:
    chunk_cookies = []
    
    for cookie in chunk:
        if "name" in cookie and "value" in cookie:
            chunk_cookies.append(f"{cookie['name']}={cookie['value']}")
    
    return "; ".join(chunk_cookies) if chunk_cookies else ""


def read_json_file(filename: str = "cleinkelvinn.json") -> Tuple[str, bool]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                logger.error(f"File is empty: {filename}")
                return "", False
            return content, True
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        return "", False
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        return "", False


def write_output_file(cookies: List[str], filename: str = "cookies.txt") -> bool:
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            for cookie in cookies:
                f.write(cookie + "\n")
        return True
    except Exception as e:
        logger.error(f"Error writing to file: {e}")
        return False


def main() -> int:
    try:
        json_data, success = read_json_file()
        if not success:
            return 1
        
        try:
            formatted_cookies = format_cookies(json_data)
        except ValueError as e:
            logger.error(f"Format error: {e}")
            return 1
        
        if not formatted_cookies:
            logger.warning("No valid cookies found in the input file")
            return 1
        
        if write_output_file(formatted_cookies):
            logger.info("Cookies formatted and saved to cookies.txt")
            return 0
        else:
            return 1
            
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 