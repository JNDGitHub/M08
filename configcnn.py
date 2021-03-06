import sys


class ConfigCNN:
    classes = ['0-2', '4-6', '8-13', '15-20', '25-32', '38-43', '48-53', '60-']
    faixa_child_adult = ["Crianca", "Adulto"]
    faixa = ['Cr', 'Ad']
    genero = ['M', 'F']
    IMAGE_LOADER_TENSORFLOW = "tensorflow"
    IMAGE_LOADER_YAHOO = "yahoo"
    window_size = (128, 128)
    dir_model = "./dados_cnn/"
    if sys.platform.startswith('win'):
        dir_model = "./dados_cnn/"
    model_architecture = dir_model + "vgg16_agegender_model.json"
    model_weights = dir_model + "vgg16_agegender_fold0_a_128_weights-15_age_0.661_ch_0.976_gd_0.906.hdf5"
    nsfw_weights_path = "tf_open_nsfw/data/open_nsfw-weights.npy"
