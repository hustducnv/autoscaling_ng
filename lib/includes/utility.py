"""
  Author:  thangbk2209
  Project: Autoscaling
  Created: 3/15/19 16:48
  Purpose:
"""
import matplotlib
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

from config import *
matplotlib.use(Config.PLT_ENV)
import matplotlib.pyplot as plt


def draw_time_series(data, title, x_label, y_label, file_name):
    plt.plot(data)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    # plt.legend([/], loc='upper left')
    plt.savefig(file_name + '.png')
    plt.show()
    plt.close()


def get_scaler(scaler_method):
    if scaler_method == 'min_max_scaler':
        return MinMaxScaler(feature_range=(0, 1))
    else:
        print(f'|-> ERROR: Not support {scaler_method}')


def get_activation(activation_name):
    if activation_name == 'sigmoid':
        return tf.nn.sigmoid
    elif activation_name == 'relu':
        return tf.nn.relu
    elif activation_name == 'tanh':
        return tf.nn.tanh
    elif activation_name == 'elu':
        return tf.nn.elu
    else:
        print(">>> Can not apply your activation <<<")


def get_optimizer(optimizer_name, lr):
    if optimizer_name == 'momentum':
        return tf.train.MomentumOptimizer(learning_rate=lr, momentum=0.9)
    elif optimizer_name == 'adam':
        return tf.train.AdamOptimizer(learning_rate=lr)
    elif optimizer_name == 'rmsprop':
        return tf.train.RMSPropOptimizer(learning_rate=lr)
    else:
        print(">>> Can not apply your optimizer <<<")


def early_stopping(array, patience):
    value = array[len(array) - patience - 1]
    arr = array[len(array) - patience:]
    check = 0
    for val in arr:
        if(val > value):
            check += 1
    if(check == patience):
        return False
    else:
        return True


def draw_train_loss(loss_train, loss_valid, save_path):
    plt.plot(loss_train)
    plt.plot(loss_valid)

    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.savefig(save_path)
    plt.close()


def average(arr):
    return sum(arr) / len(arr)


def create_name(**kwargs):
    key = list(kwargs.keys())  # collect the first key in kwargs dict
    name = []
    for _key in key:
        value = str(kwargs[_key]).replace('[', '')
        value = value.replace(']', '')
        _name = f'{_key}_{value}'
        name.append(_name)
    return '-'.join(name)
