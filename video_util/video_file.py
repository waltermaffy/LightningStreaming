from pathlib import Path
import os, sys
import cv2
import os
import time
import numpy as np
import binascii
from video_util.merkle_tree import MerkleTree

PRICE = 1
CHUNK_SIZE = 1024


class VideoFile:
    """ A video file for the LightningStreaming peer server. """

    def __init__(self, url_path, chunk_size=CHUNK_SIZE):
        self.url_path = url_path
        self.file_name = Path(url_path).stem
        self.opened = False
        self.chunk_size = chunk_size
        self.price = PRICE
        self.video = self.open_video(url_path)
        self.frame_num = 0
        self.frame_iter = self.frame_itererator()
      
      
    def calculate_hash(self, path):
        """Calculate a hash of a given file"""
        print('Calculating Merkle Tree Hash of file {}'.format(path))
        t_start = time.time()
        mht = MerkleTree('sha1', self.chunk_size)
        hash = mht.get_file_hash(path)
        if hash is None:
            print('Error calculating file hash!')
            return

        print('Given file hash is: {}. Calculated in {:.2f} s.'.format(
            str(binascii.hexlify(hash)), time.time() - t_start))

      
    def get_frame_chunk_len(self):
        return int(1 * self.fps) 
    
    def get_n_chunks(self):
        """Return tot number of video chunks (1 MB)"""
        return self.file_size // self.chunk_size + 1
    
    def get_price(self):
        return self.price
        
    def get_file_size(self):
        if os.path.isfile(self.url_path):
            return os.path.getsize(self.url_path)
        else:
            return 0
    
    def get_file_name(self):
        return self.file_name
    
    def get_url_path(self):
        return self.url_path
        
    def open_video(self, url_path):
        assert os.path.exists(self.url_path), f"{url_path} does not exist"
        video = cv2.VideoCapture(str(self.url_path))
        self.width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(video.get(cv2.CAP_PROP_FPS))
        self.n_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))   
        self.frame_chunk_len = self.get_frame_chunk_len()
        self.file_size = self.get_file_size()
        self.opened = True
        return video
        
    
    def reset_stream(self):
        self.frame_num = 0
        print("Resetting stream...")
        self.video = cv2.VideoCapture(str(self.url_path))
        
        
    def frame_itererator(self):
        while self.frame_num < self.n_frames:    
            self.video.grab()
            self.frame_num += 1
            frame = self.video.retrieve()[1]
            frame = np.random.random((200,200))
            yield self.frame_num, frame
        self.reset_stream()                    
                            
    def __repr__(self):
        return f"Video: {self.file_name} ({self.file_size} bytes)"    
    