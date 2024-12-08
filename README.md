# Phase 3 Code Challenge: Articles - without SQLAlchemy (Updated) By Jeremy Akanle

A simple python domain made to demonstrate relationships between classes and their functionality, i.e providing methods for creating, managing and querying data in these relationships.

## Features

### `Article` Class

Represents an individual article.

Has attributes `author`, `magazine` (both instances of their respective classes) and `title`(string between 5-50 characters)

Many articles belong to both authors and magazines.

### `Author` Class

Represents an individual author, writes many articles.

Has attributes `name` (non-empty string).

Methods include:
  - `articles`: Returns all articles written by said author.
  
  - `magazines`: Lists *unique* magazines the author has contributed to.

  - `add_article`: Creates a new article by said author for a magazine.

  - `topic_areas`: Returns unique magazine *categories* the author has contributed to.


### `Magazine` Class

Represents a magazine that can host multiple articles by various authors.

Has attributes `name` (string between 2-16 characters) and `category` (non-empty string).

Methods include:
  - `articles`: Returns all published articles.

  - `contributors`: Returns *unique authors* who've contributed to the magazine.

  - `article_titles`: Lists all article titles in the magazine.

  - `contributing_authors`: Returns authors who've contributed *more than two articles.*

  - `top_publisher`: Finds magazine with most articles.

Author-Magazine is a many to many relationship.


## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

You can
run `pytest` to make sure your code is functional.


## Example Usage

```
author = Author("John Doe")
magazine = Magazine("Daily Tech", "Technology")
article1 = Article(author, magazine, "AI: What we know")
article2 = Article(author, magazine, "The future of computing")

print(author.articles()) # [article1, article2]
print(magazine.contributors()) # [author]
print(author.topic_areas()) # ["Technology"]

```