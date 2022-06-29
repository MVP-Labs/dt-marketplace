#!/usr/bin/env python3

import os
import json
import logging
import argparse
import numpy as np
import crypten
import crypten.communicator as comm


class DNN(crypten.nn.Module):
    def __init__(self, n_features, layers):
        super().__init__()

        hidden_dim = layers[0]
        out_dim = layers[1]
        self.fc1 = crypten.nn.Linear(n_features, hidden_dim)
        self.fc2 = crypten.nn.Linear(hidden_dim, out_dim)

    def forward(self, x):
        out = (self.fc1(x)).relu()
        out = (self.fc2(out))
        return out


def train_model(model, X, Y, lr, batch_size, epochs):
    rank = comm.get().get_rank()
    loss = crypten.nn.CrossEntropyLoss()

    for epoch in range(epochs):

        for batch in range(X.size(0) // batch_size):
            # define the start and end of the training mini-batch
            start, end = batch * batch_size, (batch + 1) * batch_size

            x_train = X[start:end]
            x_train.requires_grad = True

            y_train = Y[start:end]
            y_train.requires_grad = True

            # perform forward pass:
            output = model(x_train)
            loss_value = loss(output, y_train)

            # set gradients to "zero"
            model.zero_grad()

            # perform backward pass:
            loss_value.backward()

            # update parameters
            model.update_parameters(lr)

            # Print progress every batch
            loss_plain = loss_value.get_plain_text(dst=0)
            y_plain = y_train.get_plain_text(dst=0)
            o_plain = output.get_plain_text(dst=0)
            if rank == 0:
                y_label = np.argmax(y_plain.numpy(), axis=-1)
                o_pred = np.argmax(o_plain.numpy(), axis=-1)
                acc = np.mean(np.equal(y_label, o_pred))
                logging.info(
                    f"Epoch {epoch}, Batch {batch} --- Loss {loss_plain.item():.4f}, Accuracy {acc * 100:.2f}")


def jointly_train(inputs, model_args):

    x_a_enc = crypten.load(inputs['0'], src=0)
    x_b_enc = crypten.load(inputs['1'], src=1)
    y_a_enc = crypten.load(inputs['2'], src=0)

    x_combined_enc = crypten.cat([x_a_enc, x_b_enc], dim=1)

    n_features = x_combined_enc.size(1)

    model = DNN(n_features, model_args['layers']).encrypt()

    logging.info("CrypTen Training")

    lr = model_args['learning_rate']
    batch_size = model_args['batch_size']
    epochs = model_args['num_epochs']

    train_model(model, x_combined_enc, y_a_enc,
                lr, batch_size, epochs)


def update_env(world_size, master_ip, master_port, self_rank):
    env_settings = {
        "WORLD_SIZE": str(world_size),
        "RENDEZVOUS": "env://",
        "MASTER_ADDR": master_ip,
        "MASTER_PORT": str(master_port)
    }

    os.environ.update(env_settings)

    os.environ["RANK"] = str(self_rank)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True)

    args = parser.parse_args()
    crypten_args = json.load(open(args.config))

    self_rank = crypten_args['self_rank']
    world_size = crypten_args['world_size']
    master_ip = crypten_args['master_ip']
    master_port = crypten_args['master_port']
    inputs = crypten_args['inputs']
    outputs = crypten_args['outputs']
    model_args = crypten_args['model_args']

    update_env(world_size, master_ip, master_port, self_rank)

    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        filename=outputs['0'], level=logging.DEBUG, format=LOG_FORMAT)

    crypten.init()

    jointly_train(inputs, model_args)
