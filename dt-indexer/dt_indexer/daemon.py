"""Daemon module."""
# Copyright 2021 The ownership-dapp Authors
# SPDX-License-Identifier: LGPL-2.1-only

from dt_indexer.routes import app

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, debug=True, use_reloader=False)