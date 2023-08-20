# testing-with-selenium

### Selenium tests for https://www.metric-conversions.org/.

Test steps:

1. Navigate to the site
2. Choose conversion (from -> to)
3. Search for conversion form according to step 2.
4. Input test value and get the result.


### Weather tests

1. Get WeatherAPI key from the site.
2. Use API to get current weather temperature for zip code 20852 from www.weatherapi.com.
3. Use UI get current weather temperature for zip code 20852 from www.weather.com.
4. Compare two temperatures and determine if they're in range of 10% of each other.