class FileAnalyzer:
    def __init__(self, repository):
        self.repository = repository

    def get_most_changed_files(self):
        nodes = self.repository.get_nodes()
        file_stats = {}
        for node in nodes:
            files = node.files()
            for file in files:
                if not file in file_stats:
                    file_stats[file] = 0
                file_stats[file] += 1
        top = sorted(file_stats.items(), key=lambda x: x[1], reverse=True)
        return top

