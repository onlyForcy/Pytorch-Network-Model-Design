#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Description :

import csv

import torch
from torch.utils.data.dataloader import DataLoader

from dataset import TestDataset
from model import Model

HASHDIR = ""
FILENAME = ""


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataloader = DataLoader(dataset=TestDataset(), batch_size=1024)
    model = Model().to(device)
    model.load_state_dict(
        torch.load(f"./parameter/{HASHDIR}/{FILENAME}", map_location=device))

    pred_result = [
        ["...", "..."]
    ]

    model.eval()
    for data, id in dataloader:
        data = data.to(device)
        pred = model(data)

        for id, pred_index in zip(id.tolist(), pred.argmax(dim=1).tolist()):
            pred_result.append([id, ...])

    # 将数据写入 CSV 文件
    with open("dataset/result.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(pred_result)


if __name__ == "__main__":
    main()
