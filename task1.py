class AIModel:

    def __init__(self, model_name, accurancy, framework='Tensorflow'):
        self.model_name = model_name
        self.accurancy = accurancy
        AIModel.framework = framework

    def display_info(self):
        print(self.model_name, self.accurancy, AIModel.framework)


VGG16 = AIModel("VG16G", 91)
VGG16.display_info()
VGG18 = AIModel("VGG18", 93, "Pytorch")
VGG18.display_info()
