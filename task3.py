class AIPipeline:
    pipeline_count = 0

    def __init__(self, name, *steps):
        self.name = name
        self.steps = list(steps)
        AIPipeline.pipeline_count += 1

    def __str__(self):
        return f"{self.name},{self.steps}, {AIPipeline.pipeline_count}"


ingestion = AIPipeline("Ingestion", "cleaning", "training", "evaluation")
print(ingestion)

ingestion2 = AIPipeline("Ingestion2", "cleaning", "training", "evaluation")
print(ingestion2)
