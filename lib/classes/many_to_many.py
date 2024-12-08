class Article:
    all=[]
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        # Adds the article to the 'all' class variable
        Article.all.append(self)
        
        # Adds the current article (self) to the list of articles associated with the author
        author._articles.append(self)
        magazine._articles.append(self)
       # allows you to access the title of the current article
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        # Ensure the new author is an instance of Author
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        # Ensure the new magazine is an instance of Magazine
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self._magazine = new_magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []
    # allows you to access the author's name
    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
    # If no articles, return None
      if not self._articles:
        return None
      return list(set(magazine.category for magazine in self.magazines()))
      
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        # Stores the magazine's name and category, and initializes an empty list for articles.
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # If no articles, return None
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Create a dictionary to count the number of articles per author
        author_article_count = {}
        for article in self._articles:
            author = article.author
            author_article_count[author] = author_article_count.get(author, 0) + 1

        authors_with_more_than_two = [
            author for author, count in author_article_count.items() if count > 2
        ]
        if not authors_with_more_than_two:
            return None
        return authors_with_more_than_two
