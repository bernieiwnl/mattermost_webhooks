# -*- coding: utf-8 -*-
from odoo import http

# class MattermostWebhooks(http.Controller):
#     @http.route('/mattermost_webhooks/mattermost_webhooks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mattermost_webhooks/mattermost_webhooks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mattermost_webhooks.listing', {
#             'root': '/mattermost_webhooks/mattermost_webhooks',
#             'objects': http.request.env['mattermost_webhooks.mattermost_webhooks'].search([]),
#         })

#     @http.route('/mattermost_webhooks/mattermost_webhooks/objects/<model("mattermost_webhooks.mattermost_webhooks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mattermost_webhooks.object', {
#             'object': obj
#         })