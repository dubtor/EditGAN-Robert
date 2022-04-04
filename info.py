# checking system settings: cuda version, pytorch version, python version
import sys
import torch
version_str="".join([
    f"py3{sys.version_info.minor}_cu",
    torch.version.cuda.replace(".",""),
    f"_pyt{torch.__version__[0:5:2]}"
])

print("Python: ", sys.version)
print("PyTorch: ", torch.__version__)
print("CUDA: ", torch.version.cuda)
print(version_str)