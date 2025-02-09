import os
import csv


def list_videos_and_labels(directory, label, output_csv):
    """
    Reads video files from a directory and writes their paths with a label to a CSV file.

    :param directory: Directory containing video files
    :param label: Label to assign to each video
    :param output_csv: Path to the output CSV file
    """
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv'}  # Add more if needed
    video_files = [os.path.join(directory, f) for f in os.listdir(directory)
                   if os.path.isfile(os.path.join(directory, f)) and os.path.splitext(f)[1].lower() in video_extensions]

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for video in video_files:
            writer.writerow([f"{video} {label}"])

    print(f"CSV file '{output_csv}' created successfully with {len(video_files)} entries.")


# Example usage
directory = "/home/debashis/Desktop/ResearchProject/Code/cholec_subset80/videos"  # Change this to the actual directory
label = "1"  # Change this to the desired label
output_csv = "video_list.csv"  # Output CSV file

list_videos_and_labels(directory, label, output_csv)
