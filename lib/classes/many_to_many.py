class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception('author must be of instance Author')
        else:
            self._author = author
        
        if not isinstance(magazine, Magazine):
            raise Exception('magazine must be of instance Magazine')
        else:
            self._magazine = magazine
            
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise Exception('Title must be str of 5-50 characters')
        else:
            self._title = title
        
        Article.all.append(self)
        
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, t):
        if hasattr(self, "title"):
            raise AttributeError('title exists and is immutable')
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, auth):
        if not isinstance(auth, Author):
            raise Exception('author must be of type Author')
        else:
            self._author = auth
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, mag):
        if not isinstance(mag, Magazine):
            raise Exception('magazine must be of type Magazine')
        else:
            self._magazine = mag
            
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 0:
            raise Exception('Name must be string longer than 0 characters.')
        else:
            self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        raise Exception('Author name is immutable.')

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(self, magazine=magazine, title=title)

    def topic_areas(self):
        magz = self.magazines() 
        return list(set([mag.category for mag in magz])) if len(magz) > 0 else None

class Magazine:
    
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise Exception('Name must be of type string and between 2-16 characters.')
        else:
            self._name = name
        if not isinstance(category, str) or not 0 < len(category):
            raise Exception('Category must be of type string and longer than 0 characters.')
        else:
            self._category = category
        Magazine.all.append(self)    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        if not isinstance(n, str) or not 2 <= len(n) <= 16:
            raise Exception('Name must be of type string and between 2-16 characters.')
        else:
            self._name = n
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, c):
        if not isinstance(c, str) or not 0 < len(c):
            raise Exception('Category must be of type string and longer than 0 characters.')
        else:
            self._category = c
            
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in self.articles()] if len(self.articles()) > 0 else None

    def contributing_authors(self):
        all_authors = [article.author for article in self.articles()]
        unique_authors = list(set(all_authors))
        if len(all_authors) > len(unique_authors):
            d = {author: all_authors.count(author) for author in unique_authors}
            return [author for author in d if d[author] > 2]
        else:
            return None

    @classmethod
    def top_publisher(cls):
        lens = [len(magazine.articles()) for magazine in cls.all]
        if all(l == 0 for l in lens):
            return None
        else:
            for magazine in cls.all:
                if len(magazine.articles()) == sorted(lens, reverse=True)[0]:
                    return magazine
                