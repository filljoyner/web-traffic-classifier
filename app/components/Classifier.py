import json


class Classifier:
    _log = None
    data = None
    datasets = {}

    def process(self, _log):
        self._ready(_log)
        self._classify()
        return self.datasets


    def _ready(self, _log):
        self._log = _log
        self.data = _log.data
        self.datasets = {
            'data': [],
            'classified': [],
            'unclassified': [],
            'ml_test': []
        }


    def _classify(self):
        for item in self.data:
            classification = self._classify_item(item)

            data = {
                'uri': item['endpoint']['uri'],
                'method': item['endpoint']['method'],
                'get': json.dumps(item['get']),
                'post': json.dumps(item['post']),
                'files': json.dumps(item['files']),
                'agent': item['agent'],
                'ip': item['remote_addr']
            }

            self.datasets['data'].append(data.copy())

            data['class'] = classification

            if classification:
                self.datasets['classified'].append(data.copy())
            else:
                self.datasets['unclassified'].append(data.copy())

            data['ml_class'] = ''
            self.datasets['ml_test'].append(data.copy())


    def _classify_item(self, item):
        class_name = None

        for classify in self.classifier:
            for checks in classify['checks']:
                if self._run_checks(item, checks):
                    class_name = classify['label']

        return class_name


    def _run_checks(self, item, checks):
        data = {
            'uri': item['endpoint']['uri'],
            'method': item['endpoint']['method'],
            'get': json.dumps(item['get']),
            'post': json.dumps(item['post']),
            'agent': item['agent'],
            'ip': item['remote_addr']
        }

        check_pass = False

        for check in checks:
            if check[1] == 'is':
                if data[check[0]] == check[2]:
                    check_pass = True
                else:
                    return False

            if check[1] == 'in':
                if data[check[0]] in check[2]:
                    check_pass = True
                else:
                    return False

            if check[1] == 'contains':
                if type(check[2]) is list:
                    for match in check[2]:
                        if match in data[check[0]]:
                            check_pass = True
                        else:
                            return False

                else:
                    if check[2] in data[check[0]]:
                        check_pass = True
                    else:
                        return False

            if check[1] == 'startsWith':
                if data[check[0]].startswith(check[2]):
                    check_pass = True
                else:
                    return False

            if check[1] == 'endsWith':
                if data[check[0]].endswith(check[2]):
                    check_pass = True
                else:
                    return False

        return check_pass


