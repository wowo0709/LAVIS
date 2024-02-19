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
Text2ShapeEvalDataset = CaptionEvalDataset
