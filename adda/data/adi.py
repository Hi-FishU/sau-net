import os
import shelve
import numpy as np

from adda.data import ImageDataset
from adda.data.dataset import register_dataset


@register_dataset('adi')
class ADI(object):
    """Light Sheeting Dataset.

   Images are 296x296x3 images in the range [0, 255].
    """

    data_path = 'ADI'

    data_files = {
            'all': 'ADI',
            }

    def __init__(self, seed, shuffle=True):
        self.image_shape = (152, 152, 3)
        self.label_shape = (152, 152)
        self.seed = seed
        self.shuffle = shuffle
        self._load_datasets()

    def _load_datasets(self):
        abspaths = {name: os.path.join(self.data_path, path)
                    for name, path in self.data_files.items()}

        data = shelve.open(abspaths['all'])
        imgs = data['imgs'].astype(np.float32)
        counts = data['counts'].astype(np.float32)

        np.random.seed(self.seed)
        ind = np.random.permutation(200)
        train_img_num = 50

        self.train = ImageDataset(imgs[ind[:train_img_num], ...],
                                  counts[ind[:train_img_num]],
                                  image_shape=self.image_shape,
                                  label_shape=self.label_shape,
                                  shuffle=self.shuffle)

        self.test = ImageDataset(imgs[ind[train_img_num:], ...],
                                 counts[ind[train_img_num:]],
                                 image_shape=self.image_shape,
                                 label_shape=self.label_shape,
                                 shuffle=self.shuffle)
