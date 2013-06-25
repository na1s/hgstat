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

    def get_commit_average_files(self):
        nodes = self.repository.get_nodes()
        file_counts = []
        for node in nodes:
            files = node.files()
            file_counts.append(len(files))
        return  reduce(lambda x, y: float(x) + float(y), file_counts) / len(file_counts)

    def get_most_changed_extensions(self):
        nodes = self.repository.get_nodes()
        file_stats = {}
        for node in nodes:
            files = node.files()
            for file in files:
                file_extension = self.get_extension(file)
                if not file_extension in file_stats:
                    file_stats[file_extension] = 0
                file_stats[file_extension] += 1
        top = sorted(file_stats.items(), key=lambda x: x[1], reverse=True)
        return top

    def get_extension(self, file):
        dot_index = file.rfind(".")
        if dot_index != -1:
            return file[dot_index:]
        return ""