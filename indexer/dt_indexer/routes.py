"""Routes module."""
# Copyright 2021 The ownership-dapp Authors
# SPDX-License-Identifier: LGPL-2.1-only

import logging
import json
from flask_cors import CORS
from flask import Flask, request, jsonify

from datatoken.config import Config
from datatoken.service.asset import AssetService
from datatoken.service.tracer import TracerService

app = Flask(__name__)
CORS(app)

config = Config(filename='./config.ini')

asset_service = AssetService(config)
tracer_service = TracerService(config)


@app.route('/api/get_stat_info', methods=['GET'])
def marketplace_stat():
    """
    tags:
       - services
    consumes:
       - application/json
    responses:
       200:
         description: Success
       400:
         description: Error
    """
    try:
        stats = tracer_service.get_marketplace_stat()

        return jsonify(stats=stats, result="Success"), 200
    except Exception as e:
        logging.error(f'Exception when granting permission: {e}')
        return jsonify(error="Error"), 400


@app.route('/api/get_dt_list', methods=['GET'])
def dt_marketplace_list():
    """
    tags:
       - services
    consumes:
       - application/json
    responses:
       200:
         description: Success
       400:
         description: Error
    """
    try:
        dt_list = asset_service.get_dt_marketplace()

        return jsonify(dt_list=dt_list, result="Success"), 200
    except Exception as e:
        logging.error(f'Exception when granting permission: {e}')
        return jsonify(error="Error"), 400


@app.route('/api/view_dt_details', methods=['POST'])
def get_dt_details():
    """
    tags:
       - services
    consumes:
       - application/json
    parameters:
       - name: dt
         in: query
         description: the data token
         type: string
         required: True
    responses:
       200:
         description: Success
       400:
         description: Error
    """
    try:
        data = json.loads(request.get_data())
        dt = data.get("dt")

        if dt == None:
            logging.error(f'A datatoken must be provided {e}')
            return jsonify(error="Error"), 400

        details = asset_service.get_dt_details(dt)

        if not details:
            logging.error(f'Do not find results for this dt {e}')
            return jsonify(error="Error"), 400

        dt_info, service_lists, union_data = details

        return jsonify(dt_info=dt_info, service_lists=service_lists,
                       union_data=union_data, result="Success"), 200
    except Exception as e:
        logging.error(f'Exception when granting permission: {e}')
        return jsonify(error="Error"), 400


@app.route('/api/trace_by_dt', methods=['POST'])
def tracer_search_by_dt():
    """
    tags:
       - services
    consumes:
       - application/json
    parameters:
       - name: dt
         in: query
         description: the data token
         type: string
         required: True
    responses:
       200:
         description: Success
       400:
         description: Error
    """
    try:
        data = json.loads(request.get_data())
        dt = data.get("dt")

        if dt == None:
            logging.error(f'A datatoken must be provided {e}')
            return jsonify(error="Error"), 400

        paths = tracer_service.trace_dt_lifecycle(dt, prefix=[])
        job_list_data = tracer_service.job_list_format(paths)

        tree = tracer_service.tree_format(paths)

        lifecycle_data = None
        if tree:
            lifecycle_data = tracer_service.tree_to_json(tree)

        return jsonify(job_list=job_list_data, lifecycle=lifecycle_data, result="Success"), 200
    except Exception as e:
        logging.error(f'Exception when granting permission: {e}')
        return jsonify(error="Error"), 400
