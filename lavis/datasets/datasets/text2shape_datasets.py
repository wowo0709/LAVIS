"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""
# Refer to coco_caption_datasets.py, textcaps_datasets.py
import os
import json

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

from lavis.datasets.datasets.base_dataset import BaseDataset
from lavis.datasets.datasets.caption_datasets import CaptionDataset, CaptionEvalDataset


Text2ShapeDataset = CaptionDataset

class Text2ShapeEvalDataset(CaptionEvalDataset):
    def __init__(self, vis_processor, text_processor, vis_root, ann_paths):
        """
        vis_root (string): Root directory of images (e.g. coco/images/)
        ann_root (string): directory to store the annotation file
        split (string): val or test
        """
        super().__init__(vis_processor, text_processor, vis_root, ann_paths)

    def __getitem__(self, index):
        ann = self.annotation[index]

        image_path = os.path.join(self.vis_root, ann["image"])
        image = Image.open(image_path).convert("RGB")

        image = self.vis_processor(image)

        synset_id, model_id, _, image_file_name = ann["image"].split("/")
        if "depth" in image_file_name:
            idx = image_file_name.index("depth") + 5
            img_id = "_".join(["text2shape", synset_id, model_id, image_file_name[:idx]])
        else: # "rgb"
            img_id = "_".join(["text2shape", synset_id, model_id, image_file_name, "rgb"])

        return {
            "image": image,
            "image_id": img_id,
            "instance_id": ann["instance_id"],
        }