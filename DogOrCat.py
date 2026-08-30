import torch
import torchvision

from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import v2
from torchvision import models
import torch.nn as nn
import torch.optim as optim


from pathlib import Path


data_transforms = transforms.Compose([ #transform the images
    transforms.Resize((224,224)), #224 * 224 size in pixels
    transforms.ToTensor() #convert to PyTorch
])

data_dir = Path(__file__).parent #this file

uploaded_folder = data_dir / "PetImages" #pet image folder 


#below gives each image a label
image_dataset = datasets.ImageFolder(root=uploaded_folder, transform=data_transforms)

#below creates the data loader that groups the images in 32 and shuffles them
data_loader = DataLoader(image_dataset, batch_size=32, shuffle=True)

print(class_names := image_dataset.classes)  # classes: ['cat', 'dog']
print(f"Total images found: {len(image_dataset)}")


#pre trained network
model = models.resent18(weights=models.ResNet18_Weights.DEFAULT)

#freeze the pre trained layers, so only final layer changes
for param in model.parameters():
    param.requires_grad = False

#make final layer output 2 classes (cat and dog)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, len(class_names))

#loss func
criterion = nn.CrossEntropyLoss()

#optimizer
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)


#change device to gpu if avaliable
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

#training
epochs = 5

model.train()

for epoch in range(epochs):
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in data_loader:
        images, labels = images.to(device), images.to(device)

        optimizer.zero_grad() #zero gradients

        outputs = model(images) # get prediction

        loss = criterion(outputs, labels)# find loss #

        loss.backward() #compute gradients

        optimizer.step() #update weights

        #stats:
        running_loss += loss.item() * images.size(0)

        _, predicted = torch.max(outputs.data, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    epoch_loss = running_loss / total
    epoch_acc = correct / total

    print(f"Epoch {epoch+1} | Loss: {epoch_loss} | Accuracy: {epoch_acc * 100}%")


# not too sure how to load this so I wont save it
# torch.save(model.state_dict(), "cat_dog_model.pth")
# print("Model saved to cat_dog_model.pth")
