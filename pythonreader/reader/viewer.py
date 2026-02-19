# viewer.py

def show(article):
    """Show one article"""
    print(article)

def show_list(site, titles):
    """Show list of articles"""
    print(f"The latest tutorials from {site}. To read an article run the same command and put the id number.")
    for article_id, title in enumerate(titles):
        print(f"{article_id:>3} {title}")