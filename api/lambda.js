'use strict'

require('dotenv').config({ path: '.build.env' })
console.log('---- BUILD ENV: ' + process.env.NODE_ENV + ' ----')

const awsServerlessExpress = require('aws-serverless-express')
const app = require('./bin/index')
const binaryMimeTypes = [
	'application/octet-stream',
	'font/eot',
	'font/opentype',
	'font/otf',
	'image/jpeg',
	'image/png',
	'image/svg+xml'
]
const server = awsServerlessExpress.createServer(app, null, binaryMimeTypes);
exports.handler = (event, context) => awsServerlessExpress.proxy(server, event, context)
