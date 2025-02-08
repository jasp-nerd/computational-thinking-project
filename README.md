# iTrade - Stock Market Analysis Tool

iTrade is a Python-based command-line tool designed to help novice traders make informed decisions in the stock market. The application analyzes a database of approximately 500 stocks and provides recommendations based on user preferences, including performance metrics, industry sectors, company age, and ESG (Environmental, Social, and Governance) scores.

## Features

- **Performance-based Filtering**: Get the top performing stocks based on your specified criteria
- **Industry Selection**: Filter stocks by specific industries including:
  - Agriculture
  - Clothing
  - Construction
  - Electronics
  - Energy
  - Entertainment
  - Mining
- **Historical Context**: Filter companies based on their establishment year (1800-2020)
- **ESG Scoring**: Consider environmental, social, and governance factors with customizable minimum scores (0-10)
- **Smart Defaults**: Automatic adjustment of criteria if initial filters are too strict
- **Clear Data Presentation**: Results displayed in an easy-to-read tabular format

## Requirements

- Python 3.x
- CSV module (built-in)
- Operating System: Windows/Mac/Linux

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jasp-nerd/computational-thinking-project
cd computational-thinking-project
```

2. Ensure you have the `stocks.csv` file in the root directory with the following columns:
   - ID
   - Performance
   - Industry
   - FoundationYear
   - Environment
   - Social
   - Governance

## Usage

Run the program using Python:

```bash
python iTrade.py
```

Follow the interactive prompts to:
1. Specify the number of stocks you want to see (1-100)
2. Choose whether to filter by industry
3. Set a maximum establishment year (optional)
4. Define minimum ESG criteria (optional)

## Example Output

```
ID    |  Performance    |  Industry        |  Foundation Year   |  Environment    |  Social    |  Governance    |
------|-----------------|------------------|--------------------|-----------------|------------|----------------|
AAPL  |  25.4          |  Electronics     |  1976             |  8              |  7         |  9             |
```

## Features in Detail

### Performance Calculation
- Stocks are ranked based on their performance metrics
- The system automatically adjusts if there aren't enough stocks meeting all criteria

### Industry Filtering
- Users can specify one industry to focus on
- Invalid industry inputs are handled with appropriate error messages

### Establishment Year
- Filter companies established before a specific year
- Valid range: 1800-2020
- Defaults to 1950 if no matches are found with original criteria

### ESG Criteria
- Set minimum scores for Environmental, Social, and Governance factors
- Each factor can be scored from 0-10
- Defaults to minimum scores of 6 if no matches are found with original criteria

## Error Handling

The program includes robust error handling for:
- Invalid numeric inputs
- Out-of-range values
- Invalid industry selections
- Empty result sets

## Acknowledgments

- Vrije Universiteit Amsterdam
- Computational Thinking Course
- Project completed: December 2024
