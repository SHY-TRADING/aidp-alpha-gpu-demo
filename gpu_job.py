import torch

def run_gpu_job():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Running on device: {device}")

    # Simulated GPU workload (matrix multiplication)
    a = torch.randn(2048, 2048).to(device)
    b = torch.randn(2048, 2048).to(device)

    result = torch.matmul(a, b)
    print("GPU compute task completed.")
    return result

if __name__ == "__main__":
    run_gpu_job()
