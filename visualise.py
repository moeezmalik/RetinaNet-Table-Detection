import torch
from retinanet import model

modelPath = "models/epoch-50.pt"

device = torch.device('cpu')

rnet = model.resnet50(num_classes=1, pretrained=False)

loaded = torch.load(modelPath, map_location=device)

rnet.load_state_dict(loaded.module.state_dict())

rnet.training = False
rnet.eval()