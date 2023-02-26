"""
Simple script to get the cuda status of pytorch
# https://pytorch.org/docs/stable/backends.html
"""
import torch
import os

print(f'PyTorch binary were run a machine \n \
with working CUDA drivers and devices: {torch.backends.cuda.is_built()}\n')

print(f'CUDA is available: {torch.cuda.is_available()}')
print(f'cudnn is available: {torch.backends.cudnn.is_available()}')
print(f'Enable cudnn: {torch.backends.cudnn.enabled}\n')

print(f'Pytorch version {torch.__version__}')
print(f'Pytorch CUDA {torch.version.cuda}')
print(f'Pytorch cudnn {torch.backends.cudnn.version()}\n')

print(f'{torch.cuda.device_count()} CUDA devices available')
for i in range(torch.cuda.device_count()):
    print(f'{torch.cuda.get_device_name(i)}')