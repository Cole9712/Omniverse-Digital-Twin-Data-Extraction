import fiftyone as fo
import fiftyone.zoo as foz


dataset = foz.load_zoo_dataset(
    "coco-2017",
    label_types=["detections"],
    classes=["cow"],
    max_samples=200,
)

export_dir = "G:\CMPT 732 Project\yolov5_coco"
label_field = "ground_truth"  # for example

# The splits to export
splits = ["train", "validation"]

# All splits must use the same classes list
classes = ["cow"]

# The dataset or view to export
# We assume the dataset uses sample tags to encode the splits to export

# Export the splitsS
for split in splits:
    split_view = dataset.match_tags(split)
    split_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )

# # Visualize the dataset in the FiftyOne App
# session = fo.launch_app(dataset)
# session.wait()