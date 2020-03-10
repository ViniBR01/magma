/**
 * Copyright 2004-present Facebook. All Rights Reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 * @format
 */
const express = require('express');
const querystring = require('querystring');
const proxy = require('http-proxy-middleware');
const {GRAPH_HOST} = require('../config');
import {accessRoleToString} from '@fbcnms/auth/roles';
import type {ClientRequest} from 'http';
import type {FBCNMSRequest} from '@fbcnms/auth/access';

const router = express.Router();

router.use(
  '/',
  proxy({
    // hostname to the target server
    target: 'http://' + GRAPH_HOST,

    // enable websocket proxying
    ws: true,

    // rewrite paths
    pathRewrite: (path: string): string => path.replace(/^\/graph/, ''),

    // subscribe to http-proxy's proxyReq event
    onProxyReq: (proxyReq: ClientRequest, req: FBCNMSRequest): void => {
      if (req.user.organization) {
        proxyReq.setHeader('x-auth-organization', req.user.organization);
      }
      proxyReq.setHeader('x-auth-user-email', req.user.email);
      proxyReq.setHeader('x-auth-user-role', accessRoleToString(req.user.role));

      if (!req.body || !Object.keys(req.body).length) {
        return;
      }

      const writeBody = (body: string) => {
        proxyReq.setHeader(
          'Content-Length',
          Buffer.byteLength(body).toString(),
        );
        proxyReq.write(body);
        proxyReq.end();
      };

      const contentType = proxyReq.getHeader('Content-Type');
      if (contentType.includes('application/json')) {
        writeBody(JSON.stringify(req.body));
      } else if (contentType.includes('application/x-www-form-urlencoded')) {
        writeBody(querystring.stringify(req.body));
      }
    },
  }),
);

module.exports = router;