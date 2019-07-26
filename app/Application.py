import csv
from app.bootstrap.Directories import Directories
from app.components.Classifiers import Classifiers
from app.components.Log import Log


class Application:
    log_filename = None
    datasets = {}
    _dirs = None
    _log = None
    _classifier = None


    def __init__(self):
        self._dirs = Directories()


    def log(self, log_filename):
        self.log_filename = log_filename
        self._log = Log(self._dirs.get('logs') + '/' + self.log_filename)
        return self


    def classifier(self, classifier):
        self._classifier = Classifiers.get(classifier)
        return self


    def process(self):
        self.datasets = self._classifier.process(self._log)
        return self


    def toCsv(self):
        for dataset_key, dataset in self.datasets.items():
            try:
                dataset_keys = dataset[0].keys()
            except:
                dataset_keys = ['no_data']

            with open(self._dirs.get('workspace') + '/' + self.log_filename + '.' + dataset_key + '.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=dataset_keys)
                writer.writeheader()
                for item in dataset:
                    writer.writerow(item)

