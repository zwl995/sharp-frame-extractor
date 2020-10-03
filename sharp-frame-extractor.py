import argparse
import os

import cv2


def extractImages(video_file, output_path, step_size, output_format):
    count = 0
    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    success = True

    # prepare paths
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    while success:
        time_code = count * step_size
        vidcap.set(cv2.CAP_PROP_POS_MSEC,time_code)
        success, image = vidcap.read()

        if not success:
            return

        frame_path = os.path.join(output_path, "frame%04d%s" % (count, output_format))

        print("frame %s at %s s..." % (count, time_code // 1000))
        cv2.imwrite(frame_path, image)
        count = count + 1


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("video", help="Path to video file")
    a.add_argument("output", help="Path to output folder")
    a.add_argument("--step", default=1000, help="Step size per evaluation")
    a.add_argument("--format", default=".jpg", help="Frame output format")
    args = a.parse_args()
    extractImages(args.video, args.output, int(args.step), args.format)
