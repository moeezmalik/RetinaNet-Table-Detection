import torch
import torchvision
from torchvision import models
from torchvision import transforms as T
from PIL import Image
import matplotlib.pyplot as plt

# model = models.detection.retinanet_resnet50_fpn(pretrained=True)

model = torch.load("cpu_train.pt", map_location=torch.device('cpu'))
model = model.eval()


tf_ = T.ToTensor()

img = Image.open("test_image.png")
transformed = tf_(img)
batched = transformed.unsqueeze(0) # model input
int_img = torch.tensor(transformed * 255, dtype=torch.uint8) # its for our bounding box utility






with torch.no_grad():
    out = model(batched)

print(out)

from torchvision.utils import draw_bounding_boxes
score_threshold = 0.7
first_out = out[0]
bounding_boxes_img = draw_bounding_boxes(int_img, first_out['boxes'][first_out['scores'] > score_threshold], width=8)
plt.imshow(bounding_boxes_img.permute(1, 2, 0)) # convert image to matplotlib compatible