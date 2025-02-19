class ModelEvaluator:

    def __init__(self, model_name , metrics=["accuracy"]):
        self.model_name = model_name
        self.metrics = metrics

    def evaluate(self):
        return f"Evaluating {self.model_name} using {', '.join(self.metrics)}"

ins=ModelEvaluator("ImageClassifier")
print(ins.evaluate())

ins2= ModelEvaluator("VoiceCancancelation", ["MSE", "precision"])
print(ins2.evaluate())