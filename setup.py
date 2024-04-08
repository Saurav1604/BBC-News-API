from setuptools import setup

with open('./bbc/BBC-News-Wrapper.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bbc-news',
    version='1.0.1',
    author='Sayad Uddin Tahsin',
    author_email='tahsin.ict@outlook.com',
    description='A simple and yet easy-to-use API for BBC News',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sayad-Uddin-Tahsin/BBC-News-API',
    packages=['bbc'],
    include_package_data=True,
    package_data={
        '': ['BBC-News-Wrapper.md', 'LICENSE', 'requirements.txt']
    },
    install_requires=[
        'requests>=2.28.2'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.7',
    project_urls={
        'Bug Tracker': 'https://github.com/Sayad-Uddin-Tahsin/bbc-news/issues',
        'PyPI': 'https://pypi.org/project/bbc-news/'
    },
    keywords=['bbc-news', 'bbc-global', 'bbc-api', 'bbc-news-api', 'bbc-api-wrapper', 'tahsin-project']
)

# Now, let's use the bbc-news package to fetch and save the news articles
from bbc.news import BBC
from datetime import datetime, timedelta

# Initialize BBC News API client
bbc = BBC()

# Define the topics and keywords
topics = {
    "nuclear_energy": "nuclear energy",
    "nuclear_weapon": "nuclear weapon"
}

# Define the date range for the last 5 years
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

# Function to fetch and save news articles for a given topic
def fetch_and_save_articles(topic, keyword):
    # Fetch news articles for the topic and keyword
    articles = bbc.search(keyword, from_date=start_date, to_date=end_date, language="en")
    
    # Save the articles to a text file
    filename = f"{topic}_articles.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for article in articles:
            # Write article title and content to the file
            file.write(article.title + "\n")
            file.write(article.content + "\n\n")

    print(f"{len(articles)} articles on {topic} saved to {filename}")

# Fetch and save news articles for each topic
for topic, keyword in topics.items():
    fetch_and_save_articles(topic, keyword)
