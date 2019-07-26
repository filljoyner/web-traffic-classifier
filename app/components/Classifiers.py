from app.components.WordPressClassifier import WordPressClassifier


class Classifiers:
    @staticmethod
    def get(classifier):
        if classifier == 'WordPress':
            return WordPressClassifier()
