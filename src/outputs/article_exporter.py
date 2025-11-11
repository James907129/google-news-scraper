thonimport json

def export_articles(articles, file_path='output.json'):
    with open(file_path, 'w') as f:
        json.dump(articles, f, indent=4)