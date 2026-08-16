import torch
import torchvision

from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import v2

from pathlib import Path


data_transforms = transforms.Compose({ #transform the images
    transforms.Resize((224,224)), #224 * 224 size in pixels
    transforms.ToTensor() #convert to PyTorch
})

data_dir = Path(__file__).parent #this file

uploaded_folder = data_dir / "PetImages" #pet image folder 


#below gives each image a label
image_dataset = datasets.ImageFolder(root=uploaded_folder, transform=data_transforms)

#below creates the data loader that groups the images in 32 and shuffles them
data_loader = DataLoader(image_dataset, batch_size=32, shuffle=True)


# BELOW IS NOT SWITCHED TO MY CODE

print(class_names := image_dataset.classes)  # Outputs: ['cat', 'dog']
print(f"Total images found: {len(image_dataset)}")

# # Example of looping through a batch during training
# for images, labels in data_loader:
#     print(f"Batch shape: {images.shape}")  # e.g., [32, 3, 224, 224]
#     print(f"Labels in this batch: {labels}")
#     break  # Stop after the first batch for demonstration