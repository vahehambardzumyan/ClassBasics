class AIDataset:
    data_format = "CSV"

    def __init__(self, dataset_name, sample_count):
        self.dataset_name = dataset_name
        self.sample_count = sample_count
        AIDataset.data_format = "CSV"

    def __str__(self):
        return f"Dataset: {self.dataset_name}, Samples: {self.sample_count}, Format : {AIDataset.data_format}"



mnist= AIDataset("MNIST", 10000)
print(mnist)