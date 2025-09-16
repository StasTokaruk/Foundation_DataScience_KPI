import kagglehub

# Download latest version
path = kagglehub.dataset_download("shivamb/amazon-prime-movies-and-tv-shows")

print("Path to dataset files:", path)