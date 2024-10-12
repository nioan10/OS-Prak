class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def remove_file(self, file_name):
        for file in self.files:
            if file.name == file_name:
                self.files.remove(file)
                print(f"Файл {file_name} удалён из директории.")
                return
        print(f"Файл {file_name} не найден в директории.")

class FileSystem:
    def __init__(self, total_space):
        self.total_space = total_space
        self.cluster_size = 512
        self.clusters = total_space // self.cluster_size
        self.cluster_map = [None] * self.clusters
        self.directories = []

    def create_file(self, file_name, file_size):
        if file_size > self.total_space:
            print(f"Недостаточно место для размещения файла: {file_name}")
            return

        new_file = File(file_name, file_size)
        clusters_needed = file_size // self.cluster_size
        if file_size % self.cluster_size != 0:
            clusters_needed += 1

        free_clusters = self.find_free_clusters(clusters_needed)
        if not free_clusters:
            print(f"Недостаточно место для размещения файла: {file_name}")
            return

        for cluster in free_clusters:
            self.cluster_map[cluster] = new_file

        print(f"Файл {file_name} успешной создан.")

    def delete_file(self, file_name):
        for i, file in enumerate(self.cluster_map):
            if file and file.name == file_name:
                self.cluster_map[i] = None
                print(f"Файл {file_name} успешно удалён.")
                return

        print(f"Файл {file_name} не найден.")

    def find_free_clusters(self, clusters_needed):
        free_clusters = []
        i = 0
        while len(free_clusters) < clusters_needed and i < len(self.cluster_map):
            if self.cluster_map[i] is None:
                free_clusters.append(i)
            i += 1
        return free_clusters

    def visualize_memory_status(self):
        used_space = sum(1 for cluster in self.cluster_map if cluster is not None)
        free_space = self.clusters - used_space
        print(f"Используемое место: {used_space * self.cluster_size} байтов")
        print(f"Свободное место: {free_space * self.cluster_size} байтов")

    def read_file(self, file_name):
        for file in self.cluster_map:
            if file and file.name == file_name:
                print(f"Чтение файла {file_name}:")
                print(file.data)
                return

        print(f"Файл {file_name} не существует.")

    def write_to_file(self, file_name, data):
        for file in self.cluster_map:
            if file and file.name == file_name:
                file.data = data
                print(f"Информация записана в {file_name} успешно.")
                return

        print(f"Файл {file_name} не найден.")

    def find_directory(self, directory_name):
        for directory in self.directories:
            if directory.name == directory_name:
                return directory
        return None

    def move_file(self, file_name, new_directory_name):
        for directory in self.directories:
            for file in directory.files:
                if file.name == file_name:
                    new_directory = self.find_directory(new_directory_name)
                    if new_directory:
                        new_directory.add_file(file)
                        directory.remove_file(file_name)
                        print(f"Файл {file_name} перемещён в {new_directory_name}.")
                        return
                    else:
                        print(f"Директория {new_directory_name} не найдена.")
                        return
        print(f"Директория {file_name} не найден.")

    def rename_file(self, file_name, new_file_name):
        for directory in self.directories:
            for file in directory.files:
                if file.name == file_name:
                    file.name = new_file_name
                    print(f"Файл {file_name} переименован в {new_file_name}.")
                    return
        print(f"Файл {file_name} не найден.")

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.data = ""

fs = FileSystem(total_space=64*1024)
dir1 = Directory("dir1")
fs.directories.append(dir1)
file1 = File("file1.txt", 300)
dir1.add_file(file1)
fs.move_file("file1.txt", "dir2")
fs.rename_file("file1.txt", "new_file1.txt")
fs.create_file("file1.txt", 300)
fs.visualize_memory_status()
fs.create_file("file2.txt", 700)
fs.visualize_memory_status()
fs.read_file("file1.txt")
fs.read_file("file3.txt")
fs.write_to_file("file2.txt", "Hello, World!")
fs.read_file("file2.txt")
fs.delete_file("file1.txt")
fs.visualize_memory_status()