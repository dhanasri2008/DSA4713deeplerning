import tensorflow as tf
for opt in [tf.keras.optimizers.SGD(),
            tf.keras.optimizers.Adam()]:
    print(opt.get_config()['name'])
