# British_Airways_Project


## Overview

This project involves scraping reviews and other data for British Airways, performing sentiment analysis using Natural Language Processing (NLP), and creating a data visualization dashboard in Tableau. The primary goal is to analyze and visualize customer sentiment towards British Airways.

## Project Structure

The project repository contains the following files:

- **`README.md`**: This file, providing an overview of the project.
- **`Web scrapper.py`**: Script to scrape reviews and data for British Airways.
- **`code to clean data.py`**: Script for cleaning and preprocessing the scraped data.
- **`airline_reviews_dataset.csv`**: Raw dataset of airline reviews.
- **`airline_reviews_clean.csv`**: Cleaned dataset after preprocessing.
- **`modified_dataset_with_adjectives.csv`**: Dataset enriched with adjectives for sentiment analysis.
- **`modified_dataset_with_adj_pos_neg.csv`**: Dataset with adjectives and associated positive/negative sentiment scores.
- **`modified_dataset_with_adjectives_sent_score.csv`**: Dataset with sentiment scores for adjectives.
- **`positive_words.xlsx`**: List of positive words used in sentiment analysis.
- **`negative_words.xlsx`**: List of negative words used in sentiment analysis.
- **`Positive and Negative Word List.xlsx`**: Combined list of positive and negative words.
- **`airline_reviews_clean.csv`**: Cleaned dataset with processed reviews.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd yourrepository
    ```

3. **Install the required Python libraries:**

    You may need to install the following libraries:

    ```bash
    pip install pandas numpy beautifulsoup4 requests nltk
    ```

4. **Run the web scraper:**

    ```bash
    python Web_scrapper.py
    ```

5. **Clean and preprocess the data:**

    ```bash
    python code_to_clean_data.py
    ```

6. **Perform sentiment analysis:**

    - Use the cleaned datasets (`modified_dataset_with_adjectives.csv`, `modified_dataset_with_adj_pos_neg.csv`, and `modified_dataset_with_adjectives_sent_score.csv`) to perform sentiment analysis.

7. **Visualize data in Tableau:**

    - Import the cleaned datasets into Tableau to create interactive dashboards and visualizations.

## Usage

- **Web Scraper**: The `Web_scrapper.py` script extracts reviews and other relevant data from online sources.
- **Data Cleaning**: The `code_to_clean_data.py` script prepares the data for analysis by removing inconsistencies and formatting issues.
- **Sentiment Analysis**: Analyze the sentiment of the reviews using the cleaned and processed datasets.
- **Dashboard**: Use Tableau to create a comprehensive visualization of the sentiment analysis results.

## Contributing

Feel free to fork the repository, create a branch, and submit a pull request with your contributions. Ensure that your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact [Your Name](mailto:your.email@example.com).

---

Happy analyzing!
