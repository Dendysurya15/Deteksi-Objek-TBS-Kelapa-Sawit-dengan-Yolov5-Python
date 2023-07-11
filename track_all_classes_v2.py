# limit the number of cpus used by high performance libraries
import os
from urllib import response
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

import aiohttp
import asyncio

import sys
sys.path.insert(0, './yolov5')

import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
import time
import datetime
from datetime import datetime, timedelta
import requests
import pytz

from yolov5.models.experimental import attempt_load
from yolov5.utils.downloads import attempt_download
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.datasets import LoadImages, LoadStreams
from yolov5.utils.general import (LOGGER, check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 deepsort root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
count = 0
count_now = 0
data = []
roi = 0.0
yolo_model_str = ''
confidence = 0.0
iou = 0.0
unripe = 0
ripe = 0
overripe = 0
empty_bunch = 0
abnormal = 0
countUnripe = 0
countRipe = 0
countOverripe = 0
countEmptybunch = 0
countAbnormal = 0
id_ffb =  []

timer = 25
url = 'https://srs-ssms.com/post-py.php'
headers = {"content-type": "application/x-www-form-urlencoded",
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
#set the timezone
tzInfo = pytz.timezone('Asia/Bangkok')

def detect(opt):
    out, source, yolo_model, deep_sort_model, show_vid, save_vid, save_txt, imgsz, evaluate, half, project, name, exist_ok= \
        opt.output, opt.source, opt.yolo_model, opt.deep_sort_model, opt.show_vid, opt.save_vid, \
        opt.save_txt, opt.imgsz, opt.evaluate, opt.half, opt.project, opt.name, opt.exist_ok
    webcam = source == '0' or source.startswith(
        'rtsp') or source.startswith('http') or source.endswith('.txt')

    device = select_device(opt.device)
    
    lastDate = datetime.now(tz=tzInfo)+timedelta(seconds=timer, minutes=0, hours=0)

    # initialize deepsort
    cfg = get_config()
    cfg.merge_from_file(opt.config_deepsort)
    deepsort = DeepSort(deep_sort_model,
                        device,
                        max_dist=cfg.DEEPSORT.MAX_DIST,
                        max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                        max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                        )

    # Initialize
    
    half &= device.type != 'cpu'  # half precision only supported on CUDA

    # The MOT16 evaluation runs multiple inference streams in parallel, each one writing to
    # its own .txt file. Hence, in that case, the output folder is not restored
    if not evaluate:
        if os.path.exists(out):
            pass
            shutil.rmtree(out)  # delete output folder
        os.makedirs(out)  # make new output folder

    # Directories
    log_dir = Path(os.getcwd() + '/log')
    log_dir.mkdir(parents=True, exist_ok=True)  # make dir
    save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
    save_dir.mkdir(parents=True, exist_ok=True)  # make dir

    # Load model
    device = select_device(device)
    model = DetectMultiBackend(yolo_model, device=device, dnn=opt.dnn)
    stride, names, pt, jit, _ = model.stride, model.names, model.pt, model.jit, model.onnx
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Half
    half &= pt and device.type != 'cpu'  # half precision only supported by PyTorch on CUDA
    if pt:
        model.model.half() if half else model.model.float()

    # Set Dataloader
    vid_path, vid_writer = None, None
    # Check if environment supports image displays
    if show_vid:
        show_vid = check_imshow()

    # Dataloader
    if webcam:
        show_vid = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt and not jit)
        bs = len(dataset)  # batch_size
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt and not jit)
        bs = 1  # batch_size
    vid_path, vid_writer = [None] * bs, [None] * bs

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names

    # extract what is in between the last '/' and last '.'
    txt_file_name = source.split('/')[-1].split('.')[0]
    txt_path = str(Path(save_dir)) + '/' + txt_file_name + '.txt'

    if pt and device.type != 'cpu':
        model(torch.zeros(1, 3, *imgsz).to(device).type_as(next(model.model.parameters())))  # warmup
    dt, seen = [0.0, 0.0, 0.0, 0.0], 0
    for frame_idx, (path, img, im0s, vid_cap, s) in enumerate(dataset):
        t1 = time_sync()
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        t2 = time_sync()
        dt[0] += t2 - t1

        # Inference
        visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if opt.visualize else False
        pred = model(img, augment=opt.augment, visualize=visualize)
        t3 = time_sync()
        dt[1] += t3 - t2

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, opt.classes, opt.agnostic_nms, max_det=opt.max_det)
        dt[2] += time_sync() - t3

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            seen += 1
            if webcam:  # batch_size >= 1
                p, im0, _ = path[i], im0s[i].copy(), dataset.count
                s += f'{i}: '
            else:
                p, im0, _ = path, im0s.copy(), getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # im.jpg, vid.mp4, ...
            s += '%gx%g ' % img.shape[2:]  # print string
            annotator = Annotator(im0, line_width=3, pil=not ascii)
            w, h = im0.shape[1], im0.shape[0]
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                xywhs = xyxy2xywh(det[:, 0:4])
                confs = det[:, 4]
                clss = det[:, 5]

                # pass detections to deepsort
                t4 = time_sync()
                outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), im0)
                t5 = time_sync()
                dt[3] += t5 - t4

                # draw boxes for visualization
                if len(outputs) > 0:
                    for j, (output, conf) in enumerate(zip(outputs, confs)):

                        bboxes = output[0:4]
                        id = output[4]
                        cls = output[5]
                        #count
                        c = int(cls)  # integer class 
                        count_obj(bboxes, w, h, id, c)
                        label = f'{id} {names[c]} {conf:.2f}' #clue1
                        annotator.box_label(bboxes, label, color=colors(c, True))

                        if save_txt:
                            # to MOT format
                            bbox_left = output[0]
                            bbox_top = output[1]
                            bbox_w = output[2] - output[0]
                            bbox_h = output[3] - output[1]
                            # Write MOT compliant results to file
                            with open(txt_path, 'a') as f:
                                f.write(('%g ' * 10 + '\n') % (frame_idx + 1, id, bbox_left,  # MOT format
                                                               bbox_top, bbox_w, bbox_h, -1, -1, -1, -1))

                LOGGER.info(f'{s}Done. YOLO:({t3 - t2:.3f}s), DeepSort:({t5 - t4:.3f}s)')

            else:
                deepsort.increment_ages()
                LOGGER.info('No detections')
                
            
            # Stream results
            im0 = annotator.result()
            
            
            
            if show_vid:
                global count, count_now, unripe, ripe, overripe, empty_bunch, abnormal, countUnripe, countRipe, countOverripe, countEmptybunch, countAbnormal
                color= (0, 255, 0)
                start_point = (0, int(h*(1-roi)))
                end_point = (w, int(h*(1-roi)))
                cv2.line(im0, start_point, end_point, color, thickness=2)
                thickness = 3 
                org= (150, 150)
                font = 2
                fontScale = 3
                fontRipeness = 1
                cv2.putText(im0, str(count), org, font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.putText(im0, str(count_now), (150,300), font, fontRipeness, (255, 255, 255), thickness, cv2.LINE_AA)
                cv2.putText(im0, "unripe: " + str(unripe) + " / " + str(countUnripe), (15, 350), font, fontRipeness, colors(0, True), 2, cv2.LINE_AA)
                cv2.putText(im0, "ripe: " + str(ripe)+ " / " + str(countRipe), (15, 400), font, fontRipeness, colors(1, True), 2, cv2.LINE_AA)
                cv2.putText(im0, "overripe: " + str(overripe)+ " / " + str(countOverripe), (15, 450), font, fontRipeness, colors(2, True), 2, cv2.LINE_AA)
                cv2.putText(im0, "empty_bunch: " + str(empty_bunch)+ " / " + str(countEmptybunch), (15, 500), font, fontRipeness, colors(3, True), 2, cv2.LINE_AA)
                cv2.putText(im0, "abnormal: " + str(abnormal)+ " / " + str(countAbnormal), (15, 550), font, fontRipeness, colors(4, True), 2, cv2.LINE_AA)
                cv2.imshow(str(p), im0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration
                
                if datetime.now(tz=tzInfo) > lastDate:
                    lastDate = datetime.now(tz=tzInfo) + timedelta(seconds=timer, minutes=0, hours=0)
                    try:
                        if count_now != 0:
                            save_log(str(countUnripe) + ";" + str(countRipe)+ ";" + str(countOverripe) + ";" + str(countEmptybunch) + ";" + str(countAbnormal) + ";" + str(datetime.now(tz=tzInfo).strftime("%Y-%m-%d %H:%M:%S")), str(Path(log_dir)))
                            count_now = 0
                            countUnripe = 0
                            countRipe = 0
                            countOverripe = 0
                            countEmptybunch = 0
                            countAbnormal = 0
                            LOGGER.error("Data sudah disimpan")
                    except:
                        LOGGER.error("internet e mati bos")

            # Save results (image with detections)
            if save_vid:
                if vid_path != save_path:  # new video
                    vid_path = save_path
                    if isinstance(vid_writer, cv2.VideoWriter):
                        vid_writer.release()  # release previous video writer
                    if vid_cap:  # video
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    else:  # stream
                        fps, w, h = 30, im0.shape[1], im0.shape[0]

                    vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                vid_writer.write(im0)

    # Print results
    log_path = str(Path(save_dir))
    if os.path.isdir(log_path) != True:
       os.file(log_path) 
    f = open(log_path + '/log_hasil.csv' , "a")
    t = tuple(x / seen * 1E3 for x in dt)  # speeds per image
    LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS, %.1fms deep sort update \
        per image at shape {(1, 3, *imgsz)}' % t)
    model_list = str(yolo_model_str).split('/')
    #f.write('\n' + str(model_list[-2]))
    count_real = ''
    acc = 0.0
    f.write('\n' + str(model_list[-2]) + "," + str(imgsz) + "," + str(confidence) + "," + str(roi) + "," + str(iou) + "," + str(unripe) + "," + str(ripe) + str(overripe) + "," + str(empty_bunch)+ "," + str(abnormal) 
    + "," +  str(acc) + "," + (f'%.1f,%.1f,%.1f,%.1f' % t))

    f.close()
    if save_txt or save_vid:
        print('Results saved to %s' % save_path)
        if platform == 'darwin':  # MacOS
            os.system('open ' + save_path)
    

def count_obj(box ,w , h, id, cls):
    global count, data, count_now, unripe, ripe, overripe, empty_bunch, abnormal, countUnripe, countRipe, countOverripe, countEmptybunch, countAbnormal
    center_coordinates = (int(box[0] + (box[2]-box[0])/2), int (box[1] + (box[3]-box[1])/2))
    if int (box[1] + (box[3]-box[1])/2) < (int(h*(1.0-roi))):
        if id not in data:
            id_ffb.append(id)
    if int (box[1] + (box[3]-box[1])/2) > (int(h*(1.0-roi))):
        if id not in data:
            for x in id_ffb:
                if int(id) == int(x):
                    id_ffb.remove(id)
                    count_now += 1
                    count += 1
                    match cls:
                        case 0:
                            unripe += 1
                            countUnripe +=1
                        case 1:
                            ripe += 1
                            countRipe +=1
                        case 2:
                            overripe += 1
                            countOverripe +=1
                        case 3:
                            empty_bunch += 1
                            countEmptybunch +=1
                        case 4:
                            abnormal += 1
                            countAbnormal +=1
                    data.append(id)
                    break
            
# async def post_count():
#     global count_now
#     async with aiohttp.ClientSession() as session:
#         params = {'count': str(count_now), 'timestamp': datetime.now(tz=tzInfo).strftime("%Y-%m-%d %X")}
#         async with session.post(url,data=params) as resp:
#             count_now = 0
#             response = await resp.read()
#             LOGGER.info('Response status ' + str(response))
    
def save_log(header, path):
    header_str = str(header)  + '\n'
    file_path = path + '/log.TXT'
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(file_path):
        f = open(file_path, "a")
        f.write("")
        f.close()
    with open(file_path, 'r') as z:
        content = z.readlines()
        wr = open(file_path, "a")
        try:
            if len(content[0].strip()) == 0 | content[0] in ['\n', '\r\n']:
                wr.write(header_str)
            else:
                wr.write(header_str)
        except:
            wr.write(header_str)
        wr.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--yolo_model', nargs='+', type=str, default='yolov5m.pt', help='model.pt path(s)')
    parser.add_argument('--deep_sort_model', type=str, default='osnet_x0_25')
    parser.add_argument('--source', type=str, default='0', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
    parser.add_argument('--conf_thres', type=float, default=0.3, help='object confidence threshold')
    parser.add_argument('--iou_thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--show-vid', action='store_true', help='display tracking video results')
    parser.add_argument('--save-vid', action='store_true', help='save video tracking results')
    parser.add_argument('--save-txt', action='store_true', help='save MOT compliant results to *.txt')
    # class 0 is person, 1 is bycicle, 2 is car... 79 is oven
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 16 17')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--evaluate', action='store_true', help='augmented inference')
    parser.add_argument("--config_deepsort", type=str, default="deep_sort/configs/deep_sort.yaml")
    parser.add_argument("--half", action="store_true", help="use FP16 half-precision inference")
    parser.add_argument('--visualize', action='store_true', help='visualize features')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detection per image')
    parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
    parser.add_argument('--project', default=ROOT / 'runs/track', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--roi', type=float, default=0.3, help='line height')
    opt = parser.parse_args()
    roi = opt.roi
    confidence = opt.conf_thres
    yolo_model_str = opt.yolo_model
    iou = opt.iou_thres
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
    
    #os.system('python send_query.py')

    with torch.no_grad():
        detect(opt)
