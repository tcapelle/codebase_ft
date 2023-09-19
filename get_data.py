import argparse
import wandb
from pathlib import Path

at_name = "capecape/vllm_llm/vllm_python:latest"
format = "jsonl"
data_path = "data/"

def parse_args():
    parser = argparse.ArgumentParser(description="Download data from wandb artifact")
    parser.add_argument("--artifact_name", type=str, default=at_name)
    parser.add_argument("--file_format", type=str, default=format)
    parser.add_argument("--data_path", type=str, default=data_path)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    api = wandb.Api()
    artifact = api.artifact(args.artifact_name)
    data = Path(artifact.download(root=args.data_path))
    ds = list(data.rglob(f"*.{args.file_format}"))
    if ds[0].exists():
        print(f"Dowloaded data succesufully: {ds}")
    else:
        print("Something went wrong")